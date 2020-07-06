node{
     stage('SCM Checkout'){
        git 'https://github.com/bhavanimahalingam/pythontest/'
     }
     stage ('Deploy python in remote instance') {
        sshagent(['airflow_tom']) {
             sh 'scp -o StrictHostKeyChecking=no /var/lib/jenkins/workspace/python_bavani/*.py  ec2-user@100.25.223.179:/home/ec2-user'
    sh 'pwd'
         sh " ssh ec2-user@100.25.223.179 'sudo python bavani15.py'"
           sh "ssh ec2-user@100.25.223.179 'python app.py'"
      //  sh "ssh ec2-user@3.81.85.44 'airflow webserver -p 8080 & airflow scheduler && fg'"
       
       }

            


}
