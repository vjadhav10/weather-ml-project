pipeline {
    agent any

    stages {
        stage('Run Weather Model') {
            steps {
                sh '''
                docker run --rm -v $(pwd):/app -w /app python:3.9 \
                bash -c "pip install -r requirements.txt && python src/train_weather.py"
                '''
            }
        }
    }
}