import React from "react";
import { Button, Form } from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup";
import { toast } from "react-toastify";
import { loginApi } from "../../api/user";
import { useAuth } from "../../hooks/useAuth";
import { useNavigate, Link } from "react-router-dom";

export function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: initialValues(),
    validationSchema: validationSchema(),
    onSubmit: async (formValues) => {
      try {
        const response = await loginApi(formValues);
        const { access } = response;
        console.log("Token obtenido:", access);
        await login(access);
        navigate("/dashboard");
      } catch (error) {
        toast.error(error.message);
      }
    },
  });

  return (
    <div className="login-admin">
      <div className="login-admin__content">
        <h1>PixelVault Login</h1>
        <div className="brand-subtitle">Comunidad Gamer &amp; Dashboard</div>
        <Form className="login-form-admin" onSubmit={formik.handleSubmit}>
          <Form.Field>
            <label>Correo electrónico</label>
            <Form.Input
              name="email"
              placeholder="admin@pixelvault.gg"
              value={formik.values.email}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              error={
                formik.touched.email && formik.errors.email
                  ? { content: formik.errors.email }
                  : false
              }
            />
          </Form.Field>
          <Form.Field>
            <label>Contraseña</label>
            <Form.Input
              name="password"
              type="password"
              placeholder="Contraseña"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              error={
                formik.touched.password && formik.errors.password
                  ? { content: formik.errors.password }
                  : false
              }
              autoComplete="current-password"
            />
          </Form.Field>
          <Button type="submit" content="Iniciar Sesión" primary fluid />
        </Form>
        <div className="auth-links">
          ¿No tienes una cuenta gamer? <Link to="/register">Regístrate aquí</Link>
        </div>
      </div>
    </div>
  );
}

function initialValues() {
  return {
    email: "",
    password: "",
  };
}

function validationSchema() {
  return Yup.object({
    email: Yup.string()
      .email("Correo electrónico no válido")
      .required("El correo electrónico es obligatorio"),
    password: Yup.string().required("La contraseña es obligatoria"),
  });
}
