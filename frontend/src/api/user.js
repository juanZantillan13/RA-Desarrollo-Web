const API_URL = import.meta.env.VITE_BASE_API_URL || 'http://localhost:8000';

export async function loginApi(formData) {
  try {
    const url = `${API_URL}/api/v1/auth/token/`;
    console.log('url', url);
    const params = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    };
    const response = await fetch(url, params);
    if (response.status !== 200) {
      throw new Error('Usuario o contraseña incorrecta');
    }
    const result = await response.json();
    return result;
  } catch (error) {
    throw new Error(error.message || 'Error al iniciar sesión');
  }
}

export async function getMeApi(token) {
  try {
    const url = `${API_URL}/api/v1/auth/me/`;
    const params = {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
    const response = await fetch(url, params);
    if (response.status !== 200) {
      throw new Error('No se pudo obtener la información del usuario');
    }
    const result = await response.json();
    return result;
  } catch (error) {
    throw error;
  }
}

export async function registerApi(formData) {
  try {
    const url = `${API_URL}/api/v1/auth/register/`;
    console.log('url', url);
    const params = {
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    };
    const response = await fetch(url, params);
    if (response.status !== 201) {
      const errData = await response.json().catch(() => ({}));
      const msg = errData.email
        ? errData.email[0]
        : (errData.password
            ? errData.password[0]
            : (errData.username ? errData.username[0] : 'No se puede crear el usuario'));
      throw new Error(msg);
    }
    const result = await response.json();
    return result;
  } catch (error) {
    throw new Error(error.message || 'Error al crear usuario');
  }
}
