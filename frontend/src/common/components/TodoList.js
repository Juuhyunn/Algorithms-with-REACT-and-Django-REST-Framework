import React from "react";
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';
import { useSelector } from "react-redux";

export default function TodoList() {
    const todos = useSelector( state => state.todoReducer.todos )
    return(<>
    <Div>
        {todos.length === 0 &&
    <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
    <AlertTitle>등록된 할 일 목록이 없습니다.</AlertTitle>
    </Alert>
    </Stack> }
    {todos.length !== 0 &&
    <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
    <AlertTitle>{todos.length}개의 할 일 목록이 있습니다</AlertTitle>
    </Alert>
    </Stack> }
    {/* {todos.length !== 0 &&
        todos.map (todo => (
            <div key={todo.id}>
                <input type='checkbox' checked={todo.complete} onChange={toggleTodo.bind(null, todo.id)}/>
                {todo.complete ? 
                    <span style={{textDecoration:'line-through'}}>{todo.name}</span> : <span>{todo.name}</span>}
            </div>
        )
        )
    
    } */}


    </Div>
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 10px;
`