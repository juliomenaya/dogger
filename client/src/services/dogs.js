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

const userDogs = async (userId) => {
    // weird but without the slash before question mark it doest work
    const url = `/users/dogs/?userId=${userId}`;
    try {
        return await client.get(url);
    } catch (err) {
        console.log('Error obteniendo lomitos del usuario ', err);
        return err.response;
    }
};

export { addUserDog, userDogs };
