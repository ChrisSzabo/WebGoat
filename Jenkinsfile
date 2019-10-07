pipeline {
  agent {
    docker {
      image 'registry.assertsecurity.io/whitesnake'
    }

  }
  stages {
    stage('Security Scan') {
      steps {
        sh 'python scan.py'
      }
    }
  }
}