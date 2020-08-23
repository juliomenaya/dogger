import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'
import { Navbar } from './components'
import { Home } from './containers';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Switch>
          <Route path="/">
            <Home />
          </Route>
          {/* <Route path="/log-in">
            <LogIn />
          </Route>
          <Route path="/log-up">
            <LogUp />
          </Route>
          <Route path="/dashboard">
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
