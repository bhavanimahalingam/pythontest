node{
     stage('SCM Checkout'){
        git 'https://github.com/bhavanimahalingam/airflow_deploy/'
     }
     stage ('Deploy python in remote instance') {
       sh 'sudo python app.py'
       sh 'python bavani15.py'
       }

            


}
