import React from "react";
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';
import { useSelector, useDispatch } from "react-redux";
// import { changePasswordAction, deleteUserAction, changeEmailAction } from "reducers/user.reducer";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Checkbox from '@mui/material/Checkbox';
import IconButton from '@mui/material/IconButton';
import CommentIcon from '@mui/icons-material/Comment';
import { isRejected } from "@reduxjs/toolkit";
import { changeEmailAction, changePasswordAction, deleteUserAction } from "../modules/userSlice";

export default function UserList() {
    const users = useSelector(state => state.userReducer.users)
    const dispatch = useDispatch()
    let email_ = ''
    let pw_ = ''
    const submitForm1 = e => {
        e.preventDefault()
        const editUser = {
            email : email_,
            password : pw_
        }
        dispatch(changePasswordAction(editUser))
        email_ = ''
        pw_ = ''
        
    }
    const changePassword = e => {
        e.preventDefault()
        email_ = e.target.id
        pw_ = e.target.value
    }
    const submitForm2 = e => {
        e.preventDefault()
        const editUser = {
            email : email_,
            pw : pw_
        }
        dispatch(changeEmailAction(editUser))
        email_ = ''
        pw_ = ''
        
    }
    const changeEmail = e => {
        e.preventDefault()
        pw_ = e.target.id
        email_ = e.target.value
    }
    const deleteUser = email => {
        dispatch(deleteUserAction(email))
    }
    return(<><Div>
    {users.length === 0 &&
        <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
        <Alert severity="warning">
        <AlertTitle>????????? ????????? ????????????.</AlertTitle>
        </Alert>
        </Stack> }
    {users.length !== 0 &&
        <Stack sx={{ width: '300px;','margin': '0 auto'}} spacing={2}>
        <Alert severity="warning">
        <AlertTitle>{users.length}?????? ?????? ????????? ????????????</AlertTitle>
        </Alert>
        </Stack>}
    {users.length !== 0 && users.map(user => (
        <div key={user.email}>
            {user.email !== '' ?
            <span> email : {user.email} , password : {user.password}
            <form onSubmit={submitForm1}>
                <input type='text' id={user.email} onChange={changePassword}/>
                <input type='submit' value='PW ??????'/>
            </form></span> :
            <span>???????????? ?????? ??????<form onSubmit={submitForm2}>
                <input type='text' id={user.password} onChange={changeEmail}/>
                <input type='submit' value='Email ??????'/>
            </form></span>}
            {/* <input type='button' onClick={deleteUser.bind(null, user.email)} value='??????'/> */}
            </div>))}
    </Div>
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 10px;
`