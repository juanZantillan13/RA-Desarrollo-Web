from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer, RegisterUserSerializer
from zeep import Client as SoapClient

class UserApiViewSet(ModelViewSet):
    """
    CRUD completo de usuarios gamers en PixelVault (solo accesible por administradores).
    """
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)


class UserView(APIView):
    """
    Endpoint para consultar los datos personales del usuario autenticado (/auth/me/).
    Requiere autenticación mediante token JWT (Bearer Token).
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class RegisterUserView(ModelViewSet):
    """
    Endpoint para el autoregistro público de nuevos usuarios gamers (manual pág. 33).
    No requiere autenticación previa.
    """
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Usuario registrado exitosamente',
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'gamertag': user.gamertag
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SoapCountryInfoView(APIView):
    """
    Parte 3 (Unidad 3): Endpoint en Django que consume un Web Service SOAP público
    utilizando la librería Zeep (CountryInfoService).
    """
    permission_classes = [AllowAny]

    def get(self, request):
        country_code = request.query_params.get('code', 'MX').upper()
        wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
        try:
            client = SoapClient(wsdl=wsdl)
            country_name = client.service.CountryName(sCountryISOCode=country_code)
            capital = client.service.CapitalCity(sCountryISOCode=country_code)
            phone_code = client.service.CountryIntPhoneCode(sCountryISOCode=country_code)
            currency = client.service.CountryCurrency(sCountryISOCode=country_code)
            currency_name = getattr(currency, 'sName', str(currency))

            return Response({
                'status': 'success',
                'protocol': 'SOAP 1.1 / WSDL',
                'service_name': 'CountryInfoService (Oorsprong Public WebService)',
                'wsdl_url': wsdl,
                'request_param': {
                    'sCountryISOCode': country_code
                },
                'soap_response': {
                    'country_code': country_code,
                    'country_name': country_name,
                    'capital_city': capital,
                    'phone_prefix': phone_code,
                    'currency': currency_name
                }
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error al consumir el servicio SOAP: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
