import React from 'react'
import { Link } from 'react-router-dom'

export function Navigation(){
    
    return(
    <nav class="navi">
        <ul>
            <li><Link to='/home'>홈</Link></li>
            <li><Link to='/users/add'>사용자 추가</Link></li>
            <li><Link to='/users/detail'>사용자 세부 사항</Link></li>
            <li><Link to='/users/list'>사용자 목록</Link></li>
            <li><Link to='/users/login'>사용자 로그인</Link></li>
            <li><Link to='/users/modify'>사용자 수정</Link></li>
            <li><Link to='/users/remove'>사용자 삭제</Link></li>
        </ul>
    </nav>)
}