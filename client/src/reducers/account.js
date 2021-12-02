import { loginUser } from "../services";

const initialState = {
  isLogged: false,
  profile: {}
};

const account = (state = initialState, { type, payload}) => {
  switch(type) {
    case 'LOG_IN':
      return { ...state, isLogged: true }
    case 'LOG_OUT':
      return initialState
    case 'RESET':
      return initialState
    case 'SET_PROFILE':
      return { ...state, profile: payload }
    default:
      return state
  }
};

export const login = (email, password) => async (dispatch) => {
  let response = await loginUser(email, password);
  if (response.status === 200) {
    dispatch({ type: 'LOG_IN' });
    dispatch({ type: 'SET_PROFILE', payload: response.data });
    return { loggedIn: true };
  }
  return {
    loggedIn: true,
    error: response.status === 401
      ? 'Comprueba tus credenciales'
      : 'Intente más tarde'
  };
};

export default account