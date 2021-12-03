import axios from 'axios';

const client = axios.create({
    baseURL: 'https://dogger-back.herokuapp.com/api/v1'
});

export default client;
