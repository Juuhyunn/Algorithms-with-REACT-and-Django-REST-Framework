import { SignIn } from "features/users/index";
import React from "react";
import { connect } from "common/modules/commonAPI"

const Home = () => {
    const handleClick = e => {
        e.preventDefault()
        alert(' Home Click ')
        connect()
        .then(res => {alert(`접속 성공 : ${res.data.connection}`)})
        .then(err => {alert(`접속 실패 : ${err}`)})
    }
    return (<>
    <h1> HOME </h1>
    <button onClick={handleClick}>Connection</button>
    {/* <SignIn/> */}

</>)}
export default Home