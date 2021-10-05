import axios from 'axios'

const server = 'http://127.0.0.1:8000'
const header = {'Content-Type':'application/json'}
export const connect = () => axios.get(`${server}/connect`)
