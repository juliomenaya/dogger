import React from 'react'
import {
  ErrorLabel,
  InputElement,
  InputContainer,
  Label
} from './styled'

const Input = ({
  onChange,
  label,
  value,
  error
}) => {
  return (
    <InputContainer>
      <Label>
        { label }
      </Label>
      <InputElement
        value={value}
        onChange={onChange}
      />
      <ErrorLabel>
        { error }
      </ErrorLabel>
    </InputContainer>
  )
}

export default Input