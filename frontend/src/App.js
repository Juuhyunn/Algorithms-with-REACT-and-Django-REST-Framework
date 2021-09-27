import React from "react";

import {Navigation, Home, Counter, SignIn, Todo} from 'common/index'
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "agorithm/index";
import { Linear, NonLinear, Mathematics } from "dataStructure/index";
import { Route, Redirect, Switch } from "react-router-dom";
const App = () => {
  return (<>
  <Navigation/>
  <Switch>
  <Route exact path='/' component = {Home}/>
  <Redirect from='/home' to = {'/'}/>
  <Route exact path='/counter' component = {Counter}/>
  <Route exact path='/signin' component = {SignIn}/>
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
  </>
  );
}

export default App;
