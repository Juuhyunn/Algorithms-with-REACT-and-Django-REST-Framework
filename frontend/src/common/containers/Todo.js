import React, { useState } from 'react'
import Button from '@mui/material/Button';
import styled from 'styled-components'


export default function Todo () {
    const [todo, setTodo] = useState(0)
    return(<><Div> 
    {todo == 1 && <p>안녕하세요</p>}
    <Button variant="contained" style={{margin:'10px'}} onClick={()=> setTodo(1)}>Show</Button>
    <Button variant="contained" style={{margin:'10px'}} onClick={()=> setTodo(0)}>Hide</Button>
    </Div></>)
}

const Div = styled.div`
    text-align : center;
    padding : 100px;
`