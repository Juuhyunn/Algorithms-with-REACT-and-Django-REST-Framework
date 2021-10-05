import { configureStore } from '@reduxjs/toolkit';
// import counterReducer from '../features/counter/modules/counterSlice';
import commonReducer from 'common/modules/commonSlice'
import todoReducer from 'features/todos/modules/todoSlice';
import userReducer from 'features/users/modules/userSlice';



export const store = configureStore({
  reducer: {
    // counter: counterReducer,
    common: commonReducer,
    todos: todoReducer,
    users: userReducer
  },
});
