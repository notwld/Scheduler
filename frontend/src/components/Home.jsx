import { Container } from '@mui/material'
import React from 'react'
import Card from './Card'

export default function Home() {
    const algorithms = [
        // generate a description for each algorithm with equal length
        { title: "FCFS", description: "The first come first serve algorithm is a scheduling algorithm that schedules the processes in the order of their arrival in the ready queue." },
        { title: "SJF", description: "The shortest job first algorithm is a scheduling algorithm that schedules the processes in the order of their burst time." },
        { title: "Priority", description: "The priority scheduling algorithm is a scheduling algorithm that schedules the processes in the order of their priority." },
        { title: "Round Robin", description: "The round robin algorithm is a scheduling algorithm that schedules the processes in the order of their arrival in the ready queue." },

    ]
    return (
        <Container style={{ marginTop: "30px", marginBottom: "20px", display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "20px" }}>
            {algorithms.map((algorithm, index) => (
                <Card key={index} title={algorithm.title} description={algorithm.description} />
            ))}

        </Container>
    )
}
