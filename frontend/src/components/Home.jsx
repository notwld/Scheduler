import { Container, Typography } from '@mui/material'
import React from 'react'
import Card from './Card'

export default function Home() {
    const algorithms = [
        {
            title: "FCFS",
            description: "The first come first serve algorithm is a scheduling algorithm that schedules the processes in the order of their arrival in the ready queue.",
            route: "/fcfs",
            isThreaded:false
        },
        {
            title: "SJF",
            description: "The shortest job first algorithm is a scheduling algorithm that schedules the processes in the order of their burst time.",
            route: "/sjf",
            isThreaded:false
        },
        {
            title: "Priority",
            description: "The priority scheduling algorithm is a scheduling algorithm that schedules the processes in the order of their priority.",
            route: "/priority",
            isThreaded:false
        },
        {
            title: "Round Robin",
            description: "The round robin algorithm is a scheduling algorithm that schedules the processes in the order of their arrival in the ready queue.",
            route: "/roundrobins",
            isThreaded:false
        },
        {
            title: "FCFS Threaded",
            description: "The first come first serve algorithm is a scheduling algorithm that schedules the processes in the order of their arrival in the ready queue.",
            route: "/fcfs-threaded",
            isThreaded:true
        },
        {
            title: "SJF Threaded",
            description: "The shortest job first algorithm is a scheduling algorithm that schedules the processes in the order of their burst time.",
            route: "/sjf-threaded",
            isThreaded:true
        },
        {
            title: "Priority Threaded",
            description: "The priority scheduling algorithm is a scheduling algorithm that schedules the processes in the order of their priority.",
            route: "/priority-threaded",
            isThreaded:true
        },
        {
            title: "Round Robin Threaded",
            description: "The round robin algorithm is a scheduling algorithm that schedules the processes in the order of their arrival in the ready queue.",
            route: "/roundrobins-threaded",
            isThreaded:true
        }

    ]
    return (
        <Container style={{marginTop: "30px"}}>
            <Typography variant='h5' style={{ textAlign: "center", textDecoration: "underline", fontSize: "24px"}}> Normal Algorithms</Typography>
            <Container style={{ marginTop: "30px", marginBottom: "20px", display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: "20px" }}>
                {algorithms
                    .filter(algorithm => !algorithm.isThreaded)
                    .map((algorithm, index) => (
                        <Card key={index} title={algorithm.title} description={algorithm.description} route={algorithm.route} isThreaded={algorithm.isThreaded} />
                    ))}
            </Container>
            <Typography variant='h5' style={{ textAlign: "center", textDecoration: "underline", fontSize: "24px"}}>Threaded Algorithms</Typography>
            <Container style={{ marginTop: "30px", marginBottom: "20px", display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: "20px" }}>
{algorithms.map((algorithm, index) => {
if(algorithm.isThreaded) {
return <Card key={index} title={algorithm.title} description={algorithm.description} route={algorithm.route} isThreaded={algorithm.isThreaded} />
}
})}
</Container>
        </Container>
)
}
