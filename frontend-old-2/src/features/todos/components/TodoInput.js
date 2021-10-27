import React, {useState} from "react";
import { useDispatch } from "react-redux";
import { v4 as uuidv4} from 'uuid'
import styled from 'styled-components'
import { addTodoAction } from "../modules/todoSlice";


export default function TodoInput () {
    const [todo, setTodo] = useState('')
    const dispatch = useDispatch()
    const handlerChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
    }
    const submitForm = e => {
        e.preventDefault()
        const newTodo = {
            id: uuidv4(),
            name : todo,
            complete : false
        }
        addTodo(newTodo)
        setTodo('')
    }
    const addTodo = todo => dispatch(addTodoAction(todo))
    return(<>
    <Div>
    <form onSubmit={submitForm} method='POST'>
        <input type='text'
                id='todo'
                name='todo'
                placeholder='할 일 입력'
                value = {todo}
                onChange={handlerChange}/>
        <input type='submit'
                value='ADD'/>
    </form>
    </Div>    
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 100px;
`