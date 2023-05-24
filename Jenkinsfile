pipeline {
    agent any

    environment {
        SNYK_TOKEN = credentials('SNYK_TOKEN')
    }
    stages {
        stage('Scan') {
            agent {
                docker {
                    image 'snyk/snyk:linux'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                echo 'Testing...'
                sh 'snyk test --fail-on-issues=false'
            }

        }
    }
}