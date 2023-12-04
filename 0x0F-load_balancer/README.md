# 0x0F. Load balancer
`DevOps` `SysAdmin`

#### Concepts
For this project, we expect you to look at these concepts:
- [Load balancer](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
- [Web stack debugging](https://www.youtube.com/watch?v=1_gqlbADaAw)

## Background Context
You have been given 2 additional servers:

- gc-[STUDENT\_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT\_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is [redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.
