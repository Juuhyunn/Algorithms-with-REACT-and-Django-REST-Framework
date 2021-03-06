import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { UserListForm } from 'features/user/index';

export function UserList() {
  const SERVER = 'http://localhost:8000'
  const [list, setList] = useState([])
  
  const fetchList = () => {
    axios.get(`${SERVER}/api/users/list`)
    .then(res =>{
      alert('?')
      setList(res.data)}
    )
    .catch(err => console.log(err))
  }

  useEffect(() => {
    fetchList()
  }, [])
  return (<>
    <div>
      <h1>사용자 목록</h1>
      <UserListForm list = {list}/>
    </div>
  </>);
}
