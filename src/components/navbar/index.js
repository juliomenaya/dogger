import React from 'react'
import { connect } from 'react-redux'
import {
  Container,
  Logo,
  Title,
  TitleContainer
} from './styled'

const Navbar = (props) => {
  return (
    <nav>
      <Container>
        <TitleContainer>
          <Logo/>
          <Title>
            Dogger
          </Title>
        </TitleContainer>
      </Container>
    </nav>
  )
}

const mapStateToProps = ({ account }) => ({
  isLogged: account.isLogged
})

export default connect(mapStateToProps)(Navbar)