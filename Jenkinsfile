pipeline{
    agent any

     triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'commit', value: '$.after'],
                [key: 'url', value: '$.repository'],
                [key: 'branch', value: '$.ref']
            ],
            causeString: 'github webhook tigger',
            token: 'abc123',
            printContributedVariables: true,
            printPostContent: true,
            silentResponse: false,
            shouldNotFlattern: false
        )
    }

    stages{
        stage("pull code"){
            steps{
                echo "hello world!"
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '6c02c3ee-86bd-41c8-9d1a-5e34ba7a032c', url: '${url_clone_url}']])
            }
        }
    }
}
