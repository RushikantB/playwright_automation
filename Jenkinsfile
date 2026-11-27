
pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh '''
                    . venv/bin/activate
                    playwright install chromium
                '''
            }
        }

        stage('Execute Automation Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p reports
                    pytest --custom-browser=chromium -v --html=reports/report.html --self-contained-html --junitxml=reports/junit.xml
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*',
                             allowEmptyArchive: true

            junit testResults: 'reports/junit.xml',
                  allowEmptyResults: true
        }

        success {
            echo 'Automation execution successful!'
        }

        failure {
            echo 'Automation execution failed!'
        }
    }
}
