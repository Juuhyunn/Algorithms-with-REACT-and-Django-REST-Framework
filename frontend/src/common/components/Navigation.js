import React from 'react'
import { Link } from 'react-router-dom'
import styled from 'styled-components';

const Navigation = () => {
    return(<>   
    <Nav>
        <Navul>
            <Navli><Link to="/home">Home</Link></Navli>
            <Navli><Link to="/signin">SignIn</Link></Navli>
            <Navli><Link to="/counter">Counter</Link></Navli>
            <Navli><Link to="/todo">Todo</Link></Navli>
        </Navul>
    </Nav>
    <Nav>
        <Navul>
            <Navli>Algorithm</Navli>
            <Navli><Link to="/bruteforce">bruteForce</Link></Navli>  
            <Navli><Link to="/divideconquer">Divide_Conquer</Link></Navli>  
            <Navli><Link to="/greedy">Greedy</Link></Navli>  
            <Navli><Link to="/dynamicprogramming">DynamicProgramming</Link></Navli>  
            <Navli><Link to="/backtracking">BackTracking</Link></Navli>  
        </Navul>
    </Nav>
    <Nav>
        <Navul>
            <Navli>Data Structure</Navli>
            <Navli><Link to="/mathematics">Mathematics</Link></Navli>
            <Navli><Link to="/linear">Linear</Link></Navli>
            <Navli><Link to="/nonlinear">Non - Linear</Link></Navli>
        </Navul>
    </Nav>
    </>)
}
export default Navigation

const Nav = styled.div`
    // position:fixed;
    text-align:center;
    background: lightgray;
    margin-top:-15px;
    width:100%;
    height:100px;
`

const Navul = styled.ul`
    list-style:none;
    height:50px;
    padding-top:30px;
    padding-bottom:5px;
`

const Navli = styled.li`
    text-align:center;
    float:left;
    font-size:20px;
    // background-color: yellow;
    width: 15%;
`