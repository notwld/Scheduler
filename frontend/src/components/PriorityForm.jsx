import React from 'react'
import { TextField, Box, Container, Button} from '@mui/material'
import { useNavigate } from "react-router-dom";


export default function PriorityForm() {
    const navigate = useNavigate();
    const [num, setNum] = React.useState(0)
    const [processes, setProcesses] = React.useState([])
    const handleChange = (index, value, field) => {
        const updatedProcesses = [...processes];
        updatedProcesses[index][field] = value;
        setProcesses(updatedProcesses);

    }

    React.useEffect(() => {
        const newProcesses = []
        for (let i = 0; i < num; i++) {
            newProcesses.push({
                name: `P${i + 1}`,
                arrivalTime: "",
                burstTime: "",
                priority: ""
            })
        }
        setProcesses(newProcesses)
    }, [num])

    const runProcesses = async () => {
        const valid = processes.every(p => p.arrivalTime !== "" && p.burstTime !== "" && p.priority !== "")
        if (!valid) {
            alert("Please fill in all the fields")
            return
        }
        const isNumber = processes.every(p => !isNaN(p.arrivalTime) && !isNaN(p.burstTime) && !isNaN(p.priority))
        const isPositive = processes.every(p => p.arrivalTime >= 0 && p.burstTime >= 0 && p.priority >= 0)
        if (!isNumber || !isPositive) {
            alert("Please enter valid numbers")
            return
        }
        await fetch(`http://localhost:5000/priority`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(processes)
        }).then(res => res.json())
        .then(data => {
            console.log(data)
            navigate("/output", {
                state: {
                    data
                }
            })
        }
        )
        .catch(err => {
            console.log(err)
        }
        )

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
                            <TextField
                                id={`priority-${index}`}
                                className='process'
                                label="Priority"
                                variant="outlined"
                                placeholder="Enter Priority"
                                onChange={(e) => handleChange(index, e.target.value, "priority")}
                            />

                        </div>
                    )
                })}
                {num > 0 && <Box sx={{ marginTop: "20px", display: "flex", justifyContent: "center", alignItems: "center" }}>
                    <Button variant="contained" onClick={runProcesses}>Run</Button
                    ></Box>}
            </Box>
            
        </Container>

    )
}
