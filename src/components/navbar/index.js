import React from 'react'
import { connect } from 'react-redux'
import {
  ButtonsContainer,
  Container,
  Logo,
  Title,
  TitleContainer
} from './styled'

const Navbar = (props) => {
  const { isLogged } = props
  return (
    <Container>
      <TitleContainer>
        <Logo src={require('../../assets/img/png/logo/dogger_icon.png')} alt='Logo' />
        <Title>
          Dogger
        </Title>
      </TitleContainer>
      { !isLogged &&
        (
          <ButtonsContainer>
            <Title>
              Log in
            </Title>
            <Title>
              Log up
            </Title>
          </ButtonsContainer>
        )
      }
    </Container>
  )
}

const mapStateToProps = ({ account }) => ({
  isLogged: account.isLogged
})

export default connect(mapStateToProps)(Navbar)