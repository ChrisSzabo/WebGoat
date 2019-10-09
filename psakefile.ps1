Task Build `
    -description "Builds the webgoat container" `
{
    docker run `
        -it `
        --rm `
        -v ${PWD}:/src `
        -w /src `
        maven:3.6-jdk-11 `
        mvn install

}

Task Dockerize `
    -description "Builds the local webgoat docker image" `
{
    try{
        Push-Location
        cd webgoat-server
        exec{

            docker build -t ${env:DOCKER_REGISTRY}assert-webgoat-8.0 --build-arg webgoat_version=v8.0.0.M25 .
        }
    }
    finally{
        Pop-Location
    }
}
Task Default -depends BUILD

