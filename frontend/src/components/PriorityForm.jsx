import React from 'react'
import { TextField, Box, Container, Button, TableContainer, Table } from '@mui/material'
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';


export default function PriorityForm() {
    const [num, setNum] = React.useState(0)
    const [processes, setProcesses] = React.useState([])
    const [showTable, setShowTable] = React.useState(false)
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

    const runProcesses = () => {
        console.log(processes)
        setShowTable(true)
    }

    return (
        <Container sx={{ margin: "20px", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }}>
            <Box component="form"
                sx={{
                    '& .MuiTextField-root': { m: 1, width: '25ch' },
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
            {showTable && <Container sx={{ marginTop: "35px" }} >
                
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Process Name</TableCell>
                                <TableCell>Arrival Time</TableCell>
                                <TableCell>Burst Time</TableCell>
                                <TableCell>Priority</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {processes.map((p, index) => {
                                return (
                                    <TableRow key={index}>
                                        <TableCell>{p.name}</TableCell>
                                        <TableCell>{p.arrivalTime}</TableCell>
                                        <TableCell>{p.burstTime}</TableCell>
                                        <TableCell>{p.priority}</TableCell>
                                    </TableRow>
                                )
                            })}
                        </TableBody>

                    </Table>
                </TableContainer>
            </Container>}
        </Container>

    )
}
