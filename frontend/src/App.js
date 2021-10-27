import React from 'react';
// import logo from './logo.svg';
// import { Counter } from './features/counter/Counter';
import './App.css';
import { Route, Redirect, Switch } from 'react-router-dom'
import { Home, Navigation } from './features/common/index';
import { UserAdd, UserDetail, UserList, UserLogin, UserModify, UserRemove } from './features/user/index'

function App() {
  return (<>
  <Home/>
  <Navigation/>
  <Switch>
    <Route exact path='/' component= { Home }/>
    <Redirect from='/home' to= { '/' }/>
    <Route exact path='/users/add' component= { UserAdd }/>
    <Route exact path='/users/detail' component= { UserDetail }/>
    <Route exact path='/users/list' component= { UserList }/>
    <Route exact path='/users/login' component= { UserLogin }/>
    <Route exact path='/users/modify' component= { UserModify }/>
    <Route exact path='/users/remove' component= { UserRemove }/>    
  </Switch>

  </>);
}

export default App;
