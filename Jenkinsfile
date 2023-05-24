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
                sh 'cd bottle'
                sh 'pip install -r requirements.txt'
                sh 'snyk test --fail-on-issues=false'
            }

        }
    }
}