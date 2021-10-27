import { UserJoin, UserList } from "features/users/index";
import React from "react";
import styled from "styled-components"

export default function SignUp() {
    return(<>
    <Div>
        <h1>Sign Up</h1>
        <UserList/>
        <UserJoin/>
    </Div>
    </>)
}
const Div = styled.div`
    text-align : center;
    padding : 100px;
`