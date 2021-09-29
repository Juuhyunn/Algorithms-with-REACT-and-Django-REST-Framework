import { UserJoin, UserList } from "common/index";
import React from "react";
import styled from "styled-components"

export default function SignUp() {
    return(<>
    <Div>
        <UserJoin/>
        <UserList/>
    </Div>
    </>)
}
const Div = styled.div`
    text-align : center;
    padding : 100px;
`