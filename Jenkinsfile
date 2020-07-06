node{
     stage('SCM Checkout'){
        git 'https://github.com/bhavanimahalingam/airflow_deploy/'
     }
     stage ('Deploy python in remote instance') {
        sh 'sudo python bavani15.py'
       sh 'python app.py'
       
       }

            


}
