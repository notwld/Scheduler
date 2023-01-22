import React, { Component } from 'react'
import RRForm from './RRForm'
import { Box, Typography } from '@mui/material'


export default class RoundRobins extends Component {
  render() {
    return (
      <Box sx={{marginTop:"40px"}}>
      <Typography variant="h3" sx={{textAlign:"center"}}>Round Robins</Typography>
      <RRForm />
    </Box>
    )
  }
}
