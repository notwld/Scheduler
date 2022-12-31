import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { useMediaQuery } from '@material-ui/core';

const useStyles = makeStyles({
  table: {
    minWidth: 650,
  },
});

function createData(processId, arrivalTime, burstTime, completionTime, turnAroundTime, waitingTime) {
  return { processId, arrivalTime, burstTime, completionTime, turnAroundTime, waitingTime };
}

const rows = [
  createData('P1', 0, 5, 10, 10, 5),
  createData('P2', 1, 3, 8, 7, 4),
  createData('P3', 2, 4, 12, 10, 6),
  createData('P4', 3, 6, 15, 12, 6),
];

export default function ProcessTable() {
  const classes = useStyles();
  const xsScreen = useMediaQuery('(max-width:599px)');

  return (
    <TableContainer component={Paper}>
      <Table className={`${classes.table} ${xsScreen ? 'responsive' : ''}`} aria-label="process table">
        <TableHead>
          <TableRow>
            <TableCell>Process ID</TableCell>
            <TableCell align="right">Arrival Time</TableCell>
            <TableCell align="right">Burst Time</TableCell>
            <TableCell align="right">Completion Time</TableCell>
            <TableCell align="right">Turn Around Time</TableCell>
            <TableCell align="right">Waiting Time</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.processId}>
              <TableCell component="th" scope="row">
                {row.processId}
              </TableCell>
              <TableCell align="right">{row.arrivalTime}</TableCell>
              <TableCell align="right">{row.burstTime}</TableCell>
              <TableCell align="right">{row.completionTime}</TableCell>
              <TableCell align="right">{row.turnAroundTime}</TableCell>
              <TableCell align="right">{row.waitingTime}</TableCell>
            </TableRow>
          ))}
        </TableBody>
        </Table>
    </TableContainer>
    );
}

