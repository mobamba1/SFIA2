pipeline {
    agent any
    environment{

    USER = credentials('USER')
    PASS = credentials('PASS')
    DATABASE = credetials('DATABASE')
    SECRETEKEY = credetials('SECRETKEY')
    SKEY = credetials('SKEY')
    }
    stages {
        stage("Build") {
            steps {
                sh "bash ./scripts/build.sh"
                
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
