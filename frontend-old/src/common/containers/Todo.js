import { TodoList, TodoInput } from "common/index";
import React from "react";
import styled from 'styled-components'

export default function Todo() {
    return (<><Div>
    <h1>할 일 목록</h1>
    <TodoList/>
    <TodoInput/>
    </Div></>)
}
const Div = styled.div`
    text-align : center;
    padding : 100px;
`