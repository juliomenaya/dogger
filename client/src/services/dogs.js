import { client } from ".";

const addUserDog = async (payload) => {
    const url = '/users/dogs/';
    try {
        return await client.post(url, payload);
    } catch (err) {
        console.log('Error creando lomito ', err);
        return err.response;
    }
};

export { addUserDog };
