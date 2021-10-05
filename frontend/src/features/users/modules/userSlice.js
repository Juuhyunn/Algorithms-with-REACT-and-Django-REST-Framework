const initialState = {users:[], user:{}}
export const addUserAction = user => ({type:"ADD_USER", payload: user})
export const changePasswordAction = user => ({type:"EDIT_PW", payload: user})
export const deleteUserAction = email => ({type:"DELETE_USER", payload: email})
export const changeEmailAction = user => ({type:"EDIT_EMAIL", payload: user})

const userReducer = (state = initialState, action) => {
    switch(action.type) {
        case "ADD_USER" :
            return {...state, users:[...state.users, action.payload]}
        case "EDIT_PW" :
            // alert("email : " + action.payload.email +" // pw : " + action.payload.pw)
            return {...state, users: state.users.map(
                user => (user.email == action.payload.email ?
                    {...user, password : action.payload.password} : user))}
        case "DELETE_USER" :
            return {...state, users: state.users.filter(user => user.email != action.payload.email)}
        case "EDIT_EMAIL" :
            return {...state, users: state.users.map(
                user => user.password == action.payload.password ? {...user, email : action.payload.email} : user)}
        default : return state
    }
}
export default userReducer