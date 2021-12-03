import {
  createStore,
  combineReducers,
  applyMiddleware
} from 'redux'
import thunk from 'redux-thunk'
import {
  persistStore,
  persistReducer
} from 'redux-persist'
import storage from 'redux-persist/lib/storage'

import {
  account,
  users,
  ui,
  dogs
} from '../reducers';

const persistConfig = {
  key: 'root',
  storage,
}

const reducers = combineReducers({
  account,
  users,
  ui,
  dogs
});

const persistedReducer = persistReducer(persistConfig, reducers)

let store = createStore(
  persistedReducer,
  applyMiddleware(thunk)
)

let persistor = persistStore(store)

export default { store, persistor }