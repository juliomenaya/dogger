import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'
import { Navbar } from './components'
import {
  Home,
  LogIn,
  LogUp
} from './containers';

function App() {
  return (
    <Router>
      <div className='principal-container'>
        <Navbar />
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/log-in">
            <LogIn />
          </Route>
          <Route path="/log-up">
            <LogUp />
          </Route>
          {/* <Route path="/dashboard">
            <Dashboard />
          </Route>
          <Route path="/dashboard/details">
            <Details />
          </Route> */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;
