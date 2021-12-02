import { client } from ".";

const signup = async (payload) => {
    let url = payload.userType === 'owner'
        ? '/users/signup/'
        : '/walkers/signup/';
    
    try {
        delete payload.userType;
        delete payload.confirmPassword;
        payload.last_name = payload.lastName
        delete payload.lastName

        let response = await client.post(url, payload);
        return response.status === 201;
    } catch (err) {
        console.log(err.response.data)
        return false;
    }
};

const loginUser = async (email, password) => {
    const url = '/account/login/';
    try {
        let response = await client.post(url, { email, password });
        return response;
    } catch (err) {
        return err.response;
    }
};

export { signup, loginUser };
