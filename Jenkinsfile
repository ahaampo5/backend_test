pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Pull code from your source control (Git)
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Build container image (assuming Dockerfile exists)
                sh 'docker build -t my-registry/my-app:${BUILD_NUMBER} .'
            }
        }
        stage('Test') {
            steps {
                // Run tests in container or local environment
                sh 'docker run --rm my-registry/my-app:${BUILD_NUMBER} /app/run-tests.sh'
            }
        }
        stage('Push') {
            steps {
                // Push container to registry
                sh 'docker push my-registry/my-app:${BUILD_NUMBER}'
            }
        }
        stage('Deploy to K8s') {
            steps {
                // Use kubectl to update the Kubernetes Deployment
                // sh '''
                // kubectl set image deployment/my-app-deployment my-app-container=my-registry/my-app:${BUILD_NUMBER} --record
                // kubectl rollout status deployment/my-app-deployment
                // '''
                echo 'hello'
            }
        }
    }
}
