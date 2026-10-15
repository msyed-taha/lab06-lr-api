pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker compose down'
                sh 'docker compose up -d'
            }
        }
        stage('Verify API') {
            steps {
                sh '''
                    for i in $(seq 1 15); do
                        if curl -fsS "http://localhost:5000/predict?x1=2&x2=3&x3=1"; then
                            echo ""
                            echo "API is UP"
                            exit 0
                        fi
                        sleep 2
                    done
                    echo "API did not come up"
                    exit 1
                '''
            }
        }
    }
}
