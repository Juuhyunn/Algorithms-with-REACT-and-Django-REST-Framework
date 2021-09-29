const initialState = {users:[], user:{}}
export const addUserAction = user => ({type:"ADD_USER", payload: user})
export const changePasswordAction = user => ({type:"EDIT_PW", payload: user})

const userReducer = (state = initialState, action) => {
    switch(action.type) {
        case "ADD_USER" :
            return {...state, users:[...state.users, action.payload]}
        case "EDIT_PW" :
            // alert("email : " + action.payload.email +" // pw : " + action.payload.pw)
            return {...state, users: state.users.map(
                user => (user.email == action.payload.email ?
                    {...user, pw : action.payload.pw} : user))}
        default : return state
    }
}
export default userReducer