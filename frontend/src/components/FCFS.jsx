import { Box, Typography } from '@mui/material'
import React, { Component } from 'react'
import BasicForm from './Form'

export default class FCFS extends Component {
  render() {
    return (
      <Box sx={{marginTop:"40px"}}>
        <Typography variant="h3" sx={{textAlign:"center"}}>First Come First Serve</Typography>
        <BasicForm type={"fcfs"} />
      </Box>
    )
  }
}
