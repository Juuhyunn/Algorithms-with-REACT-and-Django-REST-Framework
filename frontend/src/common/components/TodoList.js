import React from "react";
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';

export default function TodoList() {
    return(<>
    <Div>
    <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
    <AlertTitle>등록된 할 일 목록이 없습니다.</AlertTitle>
    </Alert>
    </Stack>
    </Div>
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 10px;
`