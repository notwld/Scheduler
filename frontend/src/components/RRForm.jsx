import React from 'react'
import { Container, Box, TextField, Button } from '@mui/material'
import { useNavigate } from 'react-router-dom'
import { useLocation } from 'react-router-dom'

export default function RRForm() {
    const navigate = useNavigate();
    const [num, setNum] = React.useState(0)
    const [processes, setProcesses] = React.useState([])
    const [quantum, setQuantum] = React.useState(0)
    const handleChange = (index, value, key) => {
        let newProcesses = [...processes];
        newProcesses[index][key] = value;
        setProcesses(newProcesses);
    }
    React.useEffect(() => {
        const newProcesses = []
        for (let i = 0; i < num; i++) {
            newProcesses.push({
                name: `P${i + 1}`,
                arrivalTime: "",
                burstTime: ""
            })
        }
        setProcesses(newProcesses)
    }, [num])
    
    const handleQuantumChange = (e) => {
        setQuantum(e.target.value);
    }
    
    const runRoundRobin = async () => {
        const valid = processes.every(p => p.arrivalTime !== "" && p.burstTime !== "") && quantum !== "";
        if (!valid) {
            alert("Please enter all the values");
            return;
        }
        const isPositive = processes.every(p => p.arrivalTime >= 0 && p.burstTime >= 0) && quantum >= 0;
        const isNumber = !isNaN(quantum) && processes.every(p => !isNaN(p.arrivalTime) && !isNaN(p.burstTime));
        if (!isPositive || !isNumber) {
            alert("Please enter valid values");
            return;
        }
        await fetch(`https://schedular.herokuapp.com/rr`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                processes,
                quantum
            })
        }).then(res => res.json())
            .then(data => {
                console.log(data)
                navigate("/output", {
                    state: {
                        data,
                        quantum
                    }
                })
            }
            )
            .catch(err => console.log(err))

    }
    
    return (
        <Container sx={{ margin: "20px", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }}>
            <Box component="form"
                sx={{
                    '& .MuiTextField-root': { m: 1, width: '25ch' },
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "center",
                    alignItems: "center"
                }}
                noValidate
                autoComplete="off">
                <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
                    <TextField id="outlined-basic" label="Number of Processes" variant="outlined" onChange={(e) => setNum(e.target.value)} />
                </div>
                {processes.map((p, index) => {
                    return (
                        <div key={index}>
                            <TextField
                                id={`process-name-${index}`}
                                className='process'
                                label="Process Name"
                                variant="outlined"
                                defaultValue={p.name}
                                onChange={(e) => handleChange(index, e.target.value, "name")}
                            />
                            <TextField
                                id={`arrival-time-${index}`}
                                className='process'
                                label="Arrival Time"
                                variant="outlined"
                                placeholder="Enter Arrival Time"
                                onChange={(e) => handleChange(index, e.target.value, "arrivalTime")}
                            />
                            <TextField
                                id={`burst-time-${index}`}
                                className='process'
                                label="Burst Time"
                                variant="outlined"
                                placeholder="Enter Burst Time"
                                onChange={(e) => handleChange(index, e.target.value, "burstTime")}
                            />
                        </div>
                    )
                })}
                <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
                    <TextField id="outlined-basic" label="Quantum" variant="outlined" onChange={handleQuantumChange} />
                </div>
                {num > 0 && <Box sx={{ marginTop: "20px", display: "flex", justifyContent: "center", alignItems: "center" }}>
                    <Button variant="contained" onClick={runRoundRobin}>Run</Button>
                </Box>}
            </Box>
     
</Container>

)
}


