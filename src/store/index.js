import {
  createStore,
  combineReducers,
  applyMiddleware
} from 'redux'
import thunk from 'redux-thunk'
import { persistStore, persistReducer } from 'redux-persist'
import storage from 'redux-persist/lib/storage'

const persistConfig = {
  key: 'root',
  storage,
}

const initialState = {
  username: '',
  password: '',
  email: ''
}

const account = (state = initialState, {type, payload}) => {
  switch (type) {
    case 'LOG_IN':
      return state
    case 'LOG_OUT':
      return state
    default:
      return state
  }
}

const store = combineReducers([account])

const persistedReducer = persistReducer(persistConfig, store)

export default () => {
  let store = createStore(
    persistedReducer,
    applyMiddleware(thunk)
  )
  let persistor = persistStore(store)
  return { store, persistor }
}
