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
                    args '-e SNYK_TOKEN -u root:root'
                }
            }
            steps {
                echo 'Testing...'
                sh 'cd bottle; pip install -r requirements.txt'
                sh 'cd bottle; snyk test || true'
            }

        }
    }
}