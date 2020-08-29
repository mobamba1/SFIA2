pipeline {
    agent any
    environment {

    USER = credentials('USER')
    PASS = credentials('PASS')
   
    }
    stages {
        stage("Build") {
            steps {
                sh "bash ./scripts/build.sh"
                
            }
        }
    }
}
