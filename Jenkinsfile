pipeline {
    agent any
    environment{

    USER = credentials('USER')
    PASS = credentials('PASS')
    }
    stages {
        stage("Build") {
            steps {
                sh "bash ./scripts/swarm.sh"
                
            }
        }
        stage("Test"){
            steps {
                sh "bash ./scripts/test.sh"
            }
        }
        stage("Swarm"){
            steps {
                sh "bash ./scripts/swarm.sh"
            }
        }
    }

}
