import axios from 'axios';
import React, { useState } from 'react';
import { Link, useHistory } from 'react-router-dom';


export function UserRemove() {
  const SERVER = 'http://localhost:8080'
  const sessionUser = JSON.parse(localStorage.getItem('sessionUser'))
  const history = useHistory()
  const headers = {
    'Content-Type' : 'application/json',
    'Authorization': 'JWT fefege..'
  }
  const [password, setPassword] = useState('')
  const handleChange = e => {
    setPassword(e.target.value)
  }
  const handleClick = e => {
    e.preventDefault()
    const removeRequest = sessionUser
    if(sessionUser.password === password){
      alert(JSON.stringify(removeRequest.userId))
      axios.delete(`${SERVER}/users/${sessionUser.userId}`, JSON.stringify(sessionUser.userId), {headers})
      .then(res => {
        console.log(res.data)
        localStorage.setItem('sessionUser', '')
        history.push('users/list')
      })
      .catch(err => alert(err))
    }else{
      alert('입력된 비밀번호가 틀립니다.')
      document.getElementById('password').value = ''

    }
  }
  
  return (
    <div>
      <h1>회원 탈퇴</h1>
      <form method="DELETE">
          <ul>
          <li>
              <label>
                    <span>사용자 번호 : {sessionUser.userId} </span>
                </label>
            </li>
            <li>
                <label>
                    <span>사용자 아이디 : {sessionUser.username} </span>
                </label>
            </li>
          <li><label for="pw">비밀번호</label>
          <input type="password" id="password" name="password" onChange={handleChange}/></li>
          <li><input type="submit" value="탈퇴 요청" onClick={handleClick}/></li>
          <li><input type="button" value="탈퇴 취소" onClick={ e => history.push('/users/detail')}/></li>
          </ul>
      </form>
    </div>
  );
}
