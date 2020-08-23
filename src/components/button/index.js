import React from 'react'
import {
  ButtonContainer,
  Text
} from './styled'

const Button = ({
  children,
  onPress,
  secondary
}) => {
  return (
    <ButtonContainer
      secondary={secondary}
      onClick={onPress}
    >
      <Text
        secondary={secondary}
      >
        { children }
      </Text>
    </ButtonContainer>
  )
}

export default Button