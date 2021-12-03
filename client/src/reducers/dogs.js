import { addUserDog } from "../services";

const initialState = {
    dogs: []
};

const dogs = (state = initialState, { type, payload }) => {
    switch (type) {
        case 'ADD_DOG':
            return {
                ...state,
                dogs: [...state.dogs, payload]
            };
        default:
            return state;
    }
};


export const addDog = (payload) => async(dispatch) => {
    let response = await addUserDog(payload);
    if (response.status === 201) {
        dispatch({ type: 'ADD_DOG', payload: response.data });
        return { dog: response.data, error: null };
    }
    return {
        dog: null,
        error: response.status === 404
            ? response.data
            : 'Por favor intenta más tarde'
    };
};

export default dogs;
