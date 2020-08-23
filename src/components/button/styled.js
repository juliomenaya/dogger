import styled from 'styled-components'

export const ButtonContainer = styled.button`
  background: ${({secondary}) => secondary ? '#D6DD70' : '#5C5F30'};
  border-radius: 5px;
  border: 0;
  padding: .8rem 1rem;
  &:hover {
    background: ${({secondary}) => secondary ? '#FFFFF9' : '#D6DD70'};
  }
`

export const Text = styled.span`
  color: ${({secondary}) => secondary ? '#5C5F30' : '#FFFFF9'};
  ${ButtonContainer}:hover & {
    color: #5C5F30;
  }
`