import React, { Component } from 'react'
import { Box, Typography } from '@mui/material'
import BasicForm from './Form'

export default class SJF extends Component {
  render() {
    return (
        <Box sx={{marginTop:"40px"}}>
        <Typography variant="h3" sx={{textAlign:"center"}}>Shortest Job First</Typography>
        <BasicForm type={"sjf"} />
      </Box>
    )
  }
}
