import React from "react";
import { Button, Form } from "semantic-ui-react";
import { useFormik } from "formik";
import * as Yup from "yup";
import { toast } from "react-toastify";
import { registerApi } from "../../api/user";
import { useNavigate, Link } from "react-router-dom";

export function Register() {
  const navigate = useNavigate();

  const formik = useFormik({
    initialValues: initialValues(),
    validationSchema: validationSchema(),
    onSubmit: async (formValues) => {
      try {
        const payload = {
          username: formValues.username,
          email: formValues.email,
          gamertag: formValues.gamertag,
          password: formValues.password,
        };
        const response = await registerApi(payload);
        toast.success("¡Usuario registrado exitosamente! Ahora inicia sesión.");
        navigate("/login");
      } catch (error) {
        toast.error(error.message);
      }
    },
  });

  return (
    <div className="register-admin">
      <div className="register-admin__content">
        <h1>Registro Gamer</h1>
        <div className="brand-subtitle">Crea tu perfil en PixelVault</div>
        <Form className="register-form-admin" onSubmit={formik.handleSubmit}>
          <Form.Field>
            <label>Nombre de usuario (Username)</label>
            <Form.Input
              name="username"
              placeholder="Username sin espacios"
              value={formik.values.username}
              onChange={(e) => {
                const value = e.target.value.replace(/\s+/g, "");
                formik.setFieldValue("username", value);
              }}
              onBlur={formik.handleBlur}
              error={
                formik.touched.username && formik.errors.username
                  ? { content: formik.errors.username }
                  : false
              }
            />
          </Form.Field>

          <Form.Field>
            <label>Gamertag (Apodo Gamer)</label>
            <Form.Input
              name="gamertag"
              placeholder="Ej. BusterSword99"
              value={formik.values.gamertag}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
            />
          </Form.Field>

          <Form.Field>
            <label>Correo electrónico</label>
            <Form.Input
              name="email"
              placeholder="correo@ejemplo.com"
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
              placeholder="Mínimo 8 caracteres"
              value={formik.values.password}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              error={
                formik.touched.password && formik.errors.password
                  ? { content: formik.errors.password }
                  : false
              }
              autoComplete="new-password"
            />
          </Form.Field>

          <Form.Field>
            <label>Confirmar Contraseña</label>
            <Form.Input
              name="password_confirm"
              type="password"
              placeholder="Repite tu contraseña"
              value={formik.values.password_confirm}
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              error={
                formik.touched.password_confirm && formik.errors.password_confirm
                  ? { content: formik.errors.password_confirm }
                  : false
              }
              autoComplete="new-password"
            />
          </Form.Field>

          <Button type="submit" content="Crear Cuenta Gamer" primary fluid />
        </Form>
        <div className="auth-links">
          ¿Ya tienes cuenta? <Link to="/login">Inicia sesión aquí</Link>
        </div>
      </div>
    </div>
  );
}

function initialValues() {
  return {
    username: "",
    gamertag: "",
    email: "",
    password: "",
    password_confirm: "",
  };
}

function validationSchema() {
  return Yup.object({
    username: Yup.string()
      .required("El username es obligatorio")
      .matches(/^\S*$/, "El username no debe contener espacios"),
    gamertag: Yup.string(),
    email: Yup.string()
      .email("Correo electrónico no válido")
      .required("El correo electrónico es obligatorio"),
    password: Yup.string()
      .required("La contraseña es obligatoria")
      .min(8, "La contraseña debe tener al menos 8 caracteres"),
    password_confirm: Yup.string()
      .required("La confirmación de contraseña es obligatoria")
      .oneOf([Yup.ref("password"), null], "Las contraseñas no coinciden"),
  });
}
