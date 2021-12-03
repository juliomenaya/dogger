import styled from "styled-components";

export const Container = styled.div`
    align-items: center;
    background: #FFFFF9;
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    padding: 5% 10%;
`;

export const Row = styled.div`
    display: flex;
    flex-direction: row;
    width: 100%;
`;


export const AddButton = styled.button`
    background: ${({secondary}) => secondary ? '#D6DD70' : '#5C5F30'};
    display: block;
    border: 0;
    &:hover {
        background: ${({secondary}) => secondary ? '#FFFFF9' : '#D6DD70'};
    }
    &:disabled {
        background: #9A9A9A;
    }
    height: 20px;
    width: 20px;
    border-radius: 50%;
`;

export const Section = styled.span`
    margin: 10px;
`;

export const FormContainer = styled.div`
    align-items: center;
    background: #FFFFF9;
    display: flex;
    flex: 1;
    flex-wrap: wrap;
    justify-content: space-evenly;
    padding: 0 30%;
`;