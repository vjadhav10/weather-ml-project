pipeline {
    agent any

    stages {
        stage('Run Weather Model') {
            steps {
                sh '''
                python3 --version || true
                pip3 --version || true
                pip3 install --user -r requirements.txt
                python3 src/train_weather.py
                '''
            }
        }
    }
}