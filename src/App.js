import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';
import {FormControl,Button,TextField,Select,Paper} from '@mui/material';


function App() {
  const[text1,setText1]= useState(1);
  const[text2,setText2]= useState(1);
  const[country1,setCountry1]= useState([]);
  const[country2,setCountry2]= useState([]);
  const[value1,setValue1]= useState(1);
  const[value2,setValue2]= useState(1);

  useEffect(()=>{
     getdata();
  },[])


  async function getdata(){
    const result = await axios.get(`https://api.apilayer.com/fixer/latest?base=USD&apikey=oJx3eiWRXj8IAzIkafzrcwjIKHYMEAAw`);
    console.log(result.data);
    setCountry1(result.data.rates);
    setCountry2(result.data.rates);
  }

  function convert(e){
    e.preventDefault();
    let num = (value2/value1) * text1;
    setText2(num);
  }

  return (
    <div className="App">
      <Paper  className="paper">
      <h3>Currency Converter</h3>
      <form onSubmit={convert}>
      <div>
      <TextField variant='outlined' value={text1 || ""} onChange={(e)=>setText1(e.target.value)} autoComplete='off'/> 
      <FormControl className="dropdown" variant='outlined'  onChange={(e)=>setValue1(e.target.value)}>
      <Select native>
        {Object.keys(country1).map((value,index)=>
        <option key={index} value={country1[value]}>{value}</option>
        )}
      </Select>
      </FormControl>
     </div>
     <br/>
     <div>
      <TextField  variant='outlined' value={text2 || ""} onChange={(e)=>setText2(e.target.value)} autoComplete='off'/> 
      <FormControl className="dropdown" variant='outlined' onChange={(e)=>setValue2(e.target.value)}>
      <Select native>
      {Object.keys(country2).map((value,index)=>
        <option key={index} value={country1[value]}>{value}</option>
        )}
      </Select>
      </FormControl>
     </div>
     <br/>
     <Button variant='contained' type='submit' className="button5">Convert</Button>
     </form>
     </Paper>

    </div>
  );
}

export default App;
