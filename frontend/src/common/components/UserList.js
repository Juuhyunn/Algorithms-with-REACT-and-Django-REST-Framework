import React from "react";
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';
import { useSelector } from "react-redux";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import CommentIcon from '@mui/icons-material/Comment';

export default function UserList() {
    const users = useSelector(state => state.userReducer.users)
    return(<><Div>
    <p>??</p>
    {users.length}
    {users.length === 0 &&
    <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
    <AlertTitle>등록된 회원이 없습니다.</AlertTitle>
    </Alert>
    </Stack> }
    {users.length !== 0 &&
    <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
    <AlertTitle>{users.length}건의 회원 목록이 있습니다</AlertTitle>
    </Alert>
    </Stack>}
    </Div>
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 10px;
`