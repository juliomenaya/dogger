import React from 'react'
import { Formik } from 'formik'
import { useDispatch } from 'react-redux';
import { useAlert } from 'react-alert';

import { login } from '../../reducers/account';
import {
  Button,
  Input
} from '../../components'
import { logInValidation } from '../../validationSchemas'
import {
  Container,
  FormContainer,
  Logo,
  Title
} from './styled'

const initialValues = {
  email: '',
  password: ''
}

const LogIn = () => {
  const dispatch = useDispatch();
  const alert = useAlert();
  
  return (
    <Container>
      <Logo src={require('../../assets/img/png/logo/dogger_logo.png')} alt='Dogger' />
      <FormContainer>
        <Title>Iniciar Sesión</Title>
        <Formik
          initialValues={initialValues}
          validationSchema={logInValidation}
          onSubmit={(props) => {
            let { email, password } = props;
            dispatch(login(email, password)).then(({loggedIn, error}) => {
              if (error) {
                alert.show(error, { type: 'error'} );
              }
            });
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
                error={errors.email}
                label='Correo'
                name='email'
                onBlur={handleBlur}
                onChange={handleChange}
                type='email'
                value={values.email}
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
              <Button
                disabled={!isValid || isSubmitting}
                onPress={handleSubmit}
                wide
              >
                Entrar
              </Button>
            </>
          )}
        </Formik>
      </FormContainer>
    </Container>
  )
}

export default LogIn