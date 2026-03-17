pipeline {
    agent any

    stages {
        stage('Install Python & Run Model') {
            steps {
                sh '''
                apt update
                apt install -y python3 python3-pip
                pip3 install -r requirements.txt
                python3 src/train_weather.py
                '''
            }
        }
    }
}