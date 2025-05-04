pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                script {
                    sh '/opt/homebrew/bin/python3 --version'
                    sh '/opt/homebrew/bin/python3 -m venv venv'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Build Package') {
                    steps {
                        script {
                            sh './venv/bin/python3 -m build'
                        }
                    }
                }
    
    }


}