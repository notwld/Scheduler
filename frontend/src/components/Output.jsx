import React, { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { Container, Box, TableContainer, Paper, Table, TableHead, TableRow, TableCell, TableBody, Typography, Divider } from "@mui/material";
import { useNavigate } from "react-router-dom";

function Output() {
    const [processes, setProcesses] = React.useState([]);
    const [isLoading, setIsLoading] = React.useState(false);
    const { state } = useLocation();
    const [pid, setPid] = React.useState(state.data.pid);
    const [arrivalTime, setArrivalTime] = React.useState(state.data.arrivalTime);
    const [burstTime, setBurstTime] = React.useState(state.data.burstTime);
    const [completionTime, setCompletionTime] = React.useState(state.data.completionTime);
    const [waitingTime, setWaitingTime] = React.useState(state.data.waitingTime);
    const [turnaroundTime, setTurnaroundTime] = React.useState(state.data.turnAroundTime);
    const [averageWT, setAverageWT] = React.useState(state.data.avgWT);
    const [averageTT, setAverageTT] = React.useState(state.data.avgTAT);
    const [priority, setPriority] = React.useState(state.data.priority || []);
    const [quantum, setQuantum] = React.useState(state.quantum || 0);



    return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",marginTop:"45px"}}>
             <Container sx={{ margin: "20px", display: "flex", flexDirection: ["column", "row"], justifyContent: "center", alignItems: "center" }}>
            <Box>
                <h2>Output</h2>
                
                <TableContainer component={Paper}>
                
                    <Table sx={{ minWidth: ["100%", 650] }} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Process Name</TableCell>
                                <TableCell>Arrival Time</TableCell>
                                <TableCell>Burst Time</TableCell>
                                {priority.length > 0 && <TableCell>Priority</TableCell>}
                                <TableCell>Completion Time</TableCell>
                                <TableCell>Turnaround Time</TableCell>
                                <TableCell>Waiting Time</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {pid.map((row, index) => (
                                <TableRow
                                    key={row}
                                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                                >
                                    <TableCell component="th" scope="row">
                                        P{row}
                                    </TableCell>
                                    <TableCell>{arrivalTime[index]}</TableCell>
                                    <TableCell>{burstTime[index]}</TableCell>
                                    {priority.length > 0 && <TableCell>{priority[index]}</TableCell>}
                                    <TableCell>{completionTime[index]}</TableCell>
                                    <TableCell>{turnaroundTime[index]}</TableCell>
                                    <TableCell>{waitingTime[index]}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                <Box sx={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center" }}>
                <Box sx={{ marginTop: "20px", display: "flex", justifyContent: "center", alignItems: ["center", "flex-start"] }}>
                    <Typography variant="span">Average Waiting Time: {averageWT} ms</Typography>
                    <Divider sx={{ margin: "0 10px" }} orientation="vertical" flexItem />
                    <Typography variant="span">Average Turnaround Time: {averageTT} ms</Typography>
                    {quantum > 0 && <><Divider sx={{ margin: "0 10px" }} orientation="vertical" flexItem />
                        <Typography variant="span">Time Quantum: {quantum} ms</Typography></>}
                                
                </Box>
                    <Box sx={{marginTop:"7px"}}>
                    {state.isThreaded && <>
                    
                    <Typography variant="span">Do you know? threading is <span style={{color:"lightgreen"}}>2x</span> faster than normal processing.</Typography></>}
                    </Box>


                </Box>
            </Box>
        </Container>
        </div>
    )
}

export default Output