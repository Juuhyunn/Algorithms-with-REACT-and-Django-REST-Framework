import React from "react";
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';
import { useSelector } from "react-redux";

export default function TodoList() {
    const todos = useSelector( state => state.todos )
    return(<>
    <Div>
        {todos == null &&
    <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
    <AlertTitle>등록된 할 일 목록이 없습니다.</AlertTitle>
    </Alert>
    </Stack> }
    {todos != null &&
    <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
    <AlertTitle>{todos.length}개의 할일 목록이 있습니다</AlertTitle>
    </Alert>
    </Stack> }
    </Div>
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 10px;
`