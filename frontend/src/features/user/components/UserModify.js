import React, { useState } from 'react';
import { Link, useHistory } from 'react-router-dom';
import axios from 'axios';


export function UserModify() {
  const SERVER = 'http://localhost:8000'
  const history = useHistory()
  const sessionUser = JSON.parse(localStorage.getItem('sessionUser'));
  const [join, setJoin] = useState({
    username: sessionUser.username, 
    password: sessionUser.password, 
    email: sessionUser.email, 
    name: sessionUser.name, 
    birth: sessionUser.birth,
    address: sessionUser.address
  })
  const { username, password, email, name, birth, address } = join
  const handleChange = e => {
    e.preventDefault()
    const { value, name } = e.target
    setJoin( {
      ...join,
      [name] : value
    })
  }
  const userJoin = joinRequest => axios.put(`${SERVER}/api/users/list`, JSON.stringify(joinRequest), {headers})
  const headers = {
    'Content-Type' : 'application/json',
    'Authorization': 'JWT fefege..'
}
  const handleSubmit = e => {
    e.preventDefault()
    const joinRequest = { ...join }
    alert(`수정 정보 : ${JSON.stringify(joinRequest)}`)
    userJoin(joinRequest)
    .then(res => {
      alert(`수정 성공 : ${res}`)
      history.push('/users/detail')
    })
    .catch(err => {
      alert(`수정 실패 : ${err}`)
    })

  }
  return (<>
    <div>
         <h1>회원정보 수정</h1>
    <form onSubmit={handleSubmit} method='POST'>
        <ul>
            <li>
                <label>
                    <span>아이디 : {sessionUser.username} </span>
                </label>
            </li>
            <li>
                <label>
                    이메일 : <input type="text" id="email" name="email" placeholder={sessionUser.email}
                                 onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    비밀 번호 : <input type="text" id="password" name="password" placeholder={sessionUser.password} onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    이름 : <input type="text" id="name" name="name" placeholder={sessionUser.name} onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    생일 : <input type="date" id="birth" name="birth" placeholder={sessionUser.birth} onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    주소 : <input type="text" id="address" name="address" placeholder={sessionUser.address} onChange={handleChange}/>
                </label>
            </li>
            <li>
                <input type="submit" value="수정확인"/>
            </li>

        </ul>
    </form>
    </div>
  </>);
}
