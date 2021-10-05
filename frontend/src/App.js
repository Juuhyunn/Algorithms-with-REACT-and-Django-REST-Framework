import React from "react";

import { Navigation, Home } from 'common'
import { CounterOld } from 'features/counterOld'
import { SignIn, SignUp } from 'features/users'
import { Todo } from "features/todos";
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "features/algorithms";
import { Linear, NonLinear, Mathematics } from "features/dataStructures";
import { Route, Redirect, Switch } from "react-router-dom";

// import { createStore, combineReducers } from 'redux'
// import { Provider } from 'react-redux'
// import {todoReducer, userReducer} from 'reducers/index'
// const rootReducer = combineReducers({todoReducer, userReducer})
// const store = createStore(rootReducer)

const App = () => {
  return (<>
  <Provider store = {store}>
    <Navigation/>
    <Switch>
      <Route exact path='/' component = {Home}/>
      <Redirect from='/home' to = {'/'}/>
      <Route exact path='/counter' component = {CounterOld}/>
      <Route exact path='/signin' component = {SignIn}/>
      <Route exact path='/signup' component = {SignUp}/>
      <Route exact path='/todo' component = {Todo}/>

      <Route exact path='/backtracking' component = {BackTracking}/>
      <Route exact path='/bruteforce' component = {BruteForce}/>
      <Route exact path='/divideconquer' component = {DivideConquer}/>
      <Route exact path='/dynamicprogramming' component = {DynamicProgramming}/>
      <Route exact path='/greedy' component = {Greedy}/>


      <Route exact path='/linear' component = {Linear}/>
      <Route exact path='/nonlinear' component = {NonLinear}/>
      <Route exact path='/mathematics' component = {Mathematics}/>
    </Switch>
  </Provider>
  </>
  );
}

export default App;