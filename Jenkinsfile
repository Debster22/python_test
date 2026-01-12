pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Клонування репозиторію з гілки main
                git branch: 'main', url: 'https://github.com/Debster22/python_test.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Запуск одного файлу tests.py
                sh '''
                python3 -m unittest tests.py
                '''
            }
        }
    }
}
