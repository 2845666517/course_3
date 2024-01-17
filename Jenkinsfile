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
                echo "${url_clone_url}"

            }
        }
    }
}
