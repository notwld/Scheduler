import React, { useEffect } from "react";
import { useLocation } from "react-router-dom";
import { Container, Box, TableContainer, Paper, Table, TableHead, TableRow, TableCell, TableBody } from "@mui/material";
import { useNavigate } from "react-router-dom";

function Output() {
    const location = useLocation();
    const navigate = useNavigate()

    useEffect(() => {
        if (!location.state) {
            navigate("/");
        }
    }, [location.state, navigate]);
    

    const processes = location.state.processes;

    return (
        <Container sx={{ margin: "20px", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }}>
            <Box>
                <h2>Output</h2>
                <TableContainer component={Paper}>
                    <Table sx={{ minWidth: 650 }} aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Process Name</TableCell>
                                <TableCell>Arrival Time</TableCell>
                                <TableCell>Burst Time</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {processes.map((p, index) => {
                                return (
                                    <TableRow key={index}>
                                        <TableCell>{p.name}</TableCell>
                                        <TableCell>{p.arrivalTime}</TableCell>
                                        <TableCell>{p.burstTime}</TableCell>
                                    </TableRow>
                                )
                            })}
                        </TableBody>
                    </Table>
                </TableContainer>
            </Box>
        </Container>
    );
}

export default Output;
