import React from 'react'
import { Formik } from 'formik'
import {
  Button,
  Input
} from '../../components'
import { logUpValidation } from '../../validationSchemas'
import {
  Container,
  Title
} from './styled'

const initialValues = {
  email: '',
  password: '',
  name: '',
  lastName: '',
  phone: '',
  address: '',
  confirmPassword: ''
}

const LogUp = () => {
  return (
    <Container>
      <Title>Registro</Title>
      <Formik
        initialValues={initialValues}
        validationSchema={logUpValidation}
        onSubmit={(props) => {
          console.log('formik props >>>', props)
        }}
      >
        {({
          values,
          errors,
          handleChange,
          handleSubmit,
          handleBlur,
          isSubmitting,
          isValid
        }) => (
          <>
            <Input
              error={errors.name}
              label='Nombre(s)'
              name='name'
              onBlur={handleBlur}
              onChange={handleChange}
              value={values.name}
            />
            <Input
              error={errors.lastName}
              label='Apellidos'
              name='lastName'
              onBlur={handleBlur}
              onChange={handleChange}
              value={values.lastName}
            />
            <Input
              error={errors.email}
              label='Correo'
              name='email'
              onBlur={handleBlur}
              onChange={handleChange}
              type='email'
              value={values.email}
            />
            <Input
              error={errors.phone}
              label='Teléfono'
              name='phone'
              onBlur={handleBlur}
              onChange={handleChange}
              type='tel'
              value={values.phone}
            />
            <Input
              error={errors.password}
              label='Contraseña'
              name='password'
              onBlur={handleBlur}
              onChange={handleChange}
              type='password'
              value={values.password}
            />
            <Input
              error={errors.confirmPassword}
              label='Confirmar contraseña'
              name='confirmPassword'
              onBlur={handleBlur}
              onChange={handleChange}
              type='password'
              value={values.confirmPassword}
            />
            <Button
              disabled={!isValid || isSubmitting}
              onPress={handleSubmit}
              wide
            >
              Registrarse
            </Button>
          </>
        )}
      </Formik>
    </Container>
  )
}

export default LogUp