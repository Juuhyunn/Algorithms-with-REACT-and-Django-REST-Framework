import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router';

export function UserLogin() {
  const history = useHistory()
  const SERVER = 'http://localhost:8080'
  const [login, setLogin] = useState({})
  const {username, password} = login
  const handleChange = e => {
    const {value, name} = e.target
    setLogin({...login, [name]: value})
  }
  const headers = {
    'Content-Type' : 'application/json',
    'Authorization': 'JWT fefege..'
  }
  const handleClick = e => {
    e.preventDefault()
    const loginRequest = {username, password}
    alert('로그인 정보 : ' + JSON.stringify(loginRequest))
    // axios.post(`http://localhost:8080/users/login`, JSON.stringify({username:'a', password:'b'}))
    userLogin(loginRequest)
    .then(res => {
      const user = res.data
      if(user.userId != 0) {
      alert('로그인 성공 : ' + user.userId)
      localStorage.setItem('sessionUser', JSON.stringify(user))
      history.push('/users/detail')
      }else{
      alert('로그인 실패 : 아이디 또는 비밀번호를 확인해주세요.')
      document.getElementById('username').value = ''
      document.getElementById('password').value = ''
    }
      
    })
    .catch(err => {
      alert('접속 실패 : ' + err)
      document.getElementById('username').value = ''
      document.getElementById('password').value = ''
    })
  }
  const userLogin = loginRequest => axios.post(`${SERVER}/users/login`, JSON.stringify(loginRequest),{headers})
  return (
    <div>
      <h1>사용자 로그인</h1>
      <form method="POST">
          <ul>
          <li><label for="id">아이디</label>
          <input type="text" id="username" 
              name='username' value={username} onChange={handleChange}/></li>
          <li><label for="pw">비밀번호</label>
          <input type="password" id="password" name="password" onChange={handleChange}/></li>
          <li><input type="button" title="로그인" value="로그인" onClick={handleClick}/></li>
          </ul>
      </form>
    </div>
  );
}
