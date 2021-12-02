import React from 'react'
import { Formik } from 'formik'
import { useHistory } from 'react-router-dom';


import {
  Button,
  Input,
  Select
} from '../../components'
import { logUpValidation } from '../../validationSchemas'
import {
  Container,
  Title
} from './styled'

import { signup } from '../../services';

const initialValues = {
  email: '',
  password: '',
  name: '',
  lastName: '',
  phone: '',
  confirmPassword: '',
  userType: 'walker'  // hack to set default option
}

const LogUp = () => {
  const history = useHistory();

  return (
    <Container>
      <Title>Registro</Title>
      <Formik
        initialValues={initialValues}
        validationSchema={logUpValidation}
        onSubmit={async (props) => {
          try {
            let created = await signup(props);
            if (created) {
              history.push('/');
            }
          } catch (err) {
            console.log('Error singning up', err);
          }
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
            <Select
              value={values.userType}
              options={[
                { value: 'walker', label: 'Walker' },
                { value: 'owner', label: 'Owner' }
              ]}
              label={'User Type'}
              onChange={handleChange}
              error={errors.name}
              name='userType'
            />
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