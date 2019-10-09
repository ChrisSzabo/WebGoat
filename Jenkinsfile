pipeline {
  parameters{
    string(name: 'DOCKER_REGISTRY', defaultValue: params.DOCKER_REGISTRY)
    string(name: 'SWARM_MANAGER_ADDR', defaultValue: params.SWARM_MANAGER_ADDR)
    string(name: 'ENDPOINT_HOSTNAME', defaultValue: params.ENDPOINT_HOSTNAME)
    string(name: 'VENARI_MASTER_URL', defaultValue: params.VENARI_MASTER_URL)
  }
  agent none
  stages {
    stage('Security Scan') {
      agent {
        docker {
          image "${DOCKER_REGISTRY}whitesnake"
        }
      }
      steps {
        withDockerRegistry(credentialsId: 'b367c07a-2e58-49ab-ab4b-46c980764afe', url: "https://${params.DOCKER_REGISTRY}") {
          withCredentials([
            string(credentialsId: 'venari-client_secret', variable: 'CLIENT_SECRET'),
            string(credentialsId: 'venari-client_id', variable: 'CLIENT_ID'),
          ]){
            //Deploy webgoat and make sure it's running
            sh "python /app/whitesnake/scan.py --swarm-host ${SWARM_MANAGER_ADDR} --stackname webgoat --tlsverify --compose-file ./Venari/docker-compose.yml --tls-folder /home/.docker"
            sh "cd Venari"
            sh 'python scan.py upload-templates'
          }
        }
      }
    }
  }
}