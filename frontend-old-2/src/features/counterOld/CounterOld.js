import React, {useState} from "react";
import Badge from '@mui/material/Badge';
import MailIcon from '@mui/icons-material/Mail';
import Button from '@mui/material/Button';
import styled from "styled-components";
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';


export default function CounterOld() {
    const [count, setCount] = useState(0)

    return(<>
    <Div>
    { count == 0 && <Stack sx={{ width: '200px;','margin': '0 auto'}} spacing={2}>
    <Alert severity="warning">
        <AlertTitle>Warning</AlertTitle>
        메일이 없습니다!
      </Alert>
    </Stack>}
    <Badge badgeContent={count >= 0 ? count : setCount(0)} color="primary" style={{margin:'10px'}}>
        <MailIcon color="action" />
    </Badge>
    <br/>
    <br/>
    <Button variant="contained" onClick={()=> setCount(count+1)} style={{margin:'10px'}}>ADD</Button>
    <Button variant="contained" onClick={()=> setCount(count-1)} style={{margin:'10px'}}>Delete</Button>
    </Div>  
    </>)
}

const Div = styled.div`
    text-align : center;
    padding : 100px;
    `