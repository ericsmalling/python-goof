pipeline {
    agent any

    environment {
        SNYK_TOKEN = credentials('SNYK_TOKEN')
    }
    stages {
        stage('Scan') {
            agent {
                docker {
                    image 'snyk/snyk:python-3.9'
                    args '-e SNYK_TOKEN'
                }
            }
            steps {
                echo 'Testing...'
                sh 'cd bottle; snyk test --fail-on-issues=false'
            }

        }
    }
}