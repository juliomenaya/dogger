import React from "react";


import { DogContainer, Row } from "./styled";

const DogList = ({ dogs }) => {
    return (
        <DogContainer>
            {
                dogs.length
                ? (dogs.map((dog, idx) => {
                    let pluralAge = dog.age > 1 ? 'years' : 'year';
                    return (
                        <Row key={idx}>
                            {`${dog.name} | ${dog.size} | ${dog.age} ${pluralAge} old`}
                        </Row>
                    )
                }))
                : null
            }
        </DogContainer>
    )
};

export default DogList;
