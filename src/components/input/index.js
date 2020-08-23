import React from 'react'
import {
  ErrorLabel,
  InputElement,
  InputContainer,
  Label
} from './styled'

const Input = ({
  error,
  label,
  onChange,
  type,
  value,
}) => {
  return (
    <InputContainer>
      <Label>
        { label }
      </Label>
      <InputElement
        onChange={onChange}
        type={type || 'text'}
        value={value}
      />
      <ErrorLabel>
        { error }
      </ErrorLabel>
    </InputContainer>
  )
}

export default Input