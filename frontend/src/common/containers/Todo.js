import React, { useState } from 'react'
import {TextField, Button} from '@mui/material';
import styled from 'styled-components'


export default function Todo () {
    const [todo, setTodo] = useState('')
    let val = ''
    const add = e => {
        e.preventDefault()
        val = e.target.value
    }
    const del = e => {
        e.preventDefault()
        setTodo('')
    }
    const submitForm = e => {
        e.preventDefault()
        setTodo(val)
        document.getElementById('todo-input').value = '' //text input 의 데이터를 리셋시켜준다
    }
    return(<><Div><form onSubmit={submitForm} method='POST'>
    <h1>할 일 목록</h1>
    <input type='text' id='todo-input' onChange={add}/>
    <input type='submit' value = 'ADD'/>
    <br/>
    {todo != '' && <div><span>{todo}</span>
    <input type='submit' value = 'Del' onClick={del}/></div>}
    </form></Div></>)
}

const Div = styled.div`
    text-align : center;
    padding : 100px;
`