import React from 'react'
import {
  Container,
  Logo,
  TextContainer,
  Title,
  TitleContainer,
  SubTitle,
  Paragraph
} from './styled'

const Home = () => {
  return (
    <Container>
      <Logo src={require('../../assets/img/png/logo/dogger_logo.png')} alt='Dogger' />
      <TextContainer>
        <TitleContainer>
          <Title align='right'>¿Necesitas pasear a tu perro?</Title>
          <Title align='left'>¿No tienes tiempo para ello?</Title>
          <Title align='right'>¿Necesitas alguien de confianza?</Title>
        </TitleContainer>
        <SubTitle>Dogger es para tí</SubTitle>
        <Paragraph>Es una plataforma donde dueños de perros pueden contactar con personas dispuestas a pasear a sus lomitos.</Paragraph>
      </TextContainer>
    </Container>
  )
}

export default Home