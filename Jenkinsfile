pipeline {
    agent any

    environment {
        // Задай свої креденшіали для Docker Hub у Jenkins (ID = dockerhub-creds)
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        DOCKER_IMAGE = "de6ster/python_test"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Debster22/python_test.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                python3 -m unittest tests.py
                '''
            }
        }

        stage('Check Docker Access') {
            steps {
                sh '''
                echo "=== PATH ==="
                echo $PATH
                which docker || echo "docker not found"
                docker --version || echo "docker command not working"
                echo "=== Docker socket ==="
                ls -l /var/run/docker.sock || echo "docker.sock not accessible"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh '''
                echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }
    }
}
