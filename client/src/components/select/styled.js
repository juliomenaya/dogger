import styled from 'styled-components';

export const ElementSelect = styled.select`
    border-radius: 5px;
    border: 0;
    border-bottom: ${({error}) => error ? '2px solid #D1551A' : 0};
    padding: 10px;
    marging: 10px 0;
    box-shadow: 0px 3px 5px 0px rgba(0,0,0,0.3);
    &:focus {
    border: 0;
    }
`;
