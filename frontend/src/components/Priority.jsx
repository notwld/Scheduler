import React, { Component } from 'react'
import { Box, Typography } from '@mui/material'
import PriorityForm from './PriorityForm'

export default class Priority extends Component {
  render() {
    return (
        <Box sx={{marginTop:"40px"}}>
        <Typography variant="h3" sx={{textAlign:"center"}}>Priority Based Scheduling</Typography>
        <PriorityForm />
      </Box>
    )
  }
}
