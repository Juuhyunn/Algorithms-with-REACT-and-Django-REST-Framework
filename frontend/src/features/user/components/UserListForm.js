import React from "react";

const UserListForm = ({list}) => {
    return (<>
    {/* <table style={{border:'1px soild black'}}> */}
    <table border='1px' style={{textAlign:'center'}}>
    <thead>
        <tr>
            <th>사용자 아이디</th>
            <th>사용자 이름</th>
            <th>사용자 이메일</th>
            <th>사용자 생일</th>
            <th>사용자 주소</th>
        </tr>   
    </thead>
    <tbody>
        {list.map((user) => (
            <tr>
                <td>{user.username}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.birth}</td>
                <td>{user.address}</td>
            </tr>
        ))}
    </tbody>
    </table>
    </>)
}
export default UserListForm