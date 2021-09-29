import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addUserAction } from "reducers/user.reducer";
import styled from "styled-components"


export default function UserJoin() {
    const [email, setEmail] = useState('')
    const [pw, setPw] = useState('')
    const dispatch = useDispatch()

    const submitForm = e => {
        e.preventDefault()
        const newUser = {
            email : email,
            pw : pw
        }
        addUser(newUser)
        setEmail('')
        setPw('')
    }
    const addUser = user => {
        return(dispatch(addUserAction(user)))
    }
    const joinId = e => {
        e.preventDefault()
        setEmail(e.target.value)
    }
    const joinPw = e => {
        e.preventDefault()
        setPw(e.target.value)
    }
    return (<>

    <Div>
        <form onSubmit={submitForm} method='POST'>
            E-mail : <input type='text' id='email' onChange={joinId} value={email}/><br/>
            PassWord : <input type='text' id='pw' onChange={joinPw} value={pw}/><br/>
            <input type='submit' value='JOIN US'/>
        </form>
    </Div>
    </>)
}
const Div = styled.div`
    text-align : center;
    padding : 100px;
`