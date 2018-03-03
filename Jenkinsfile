#!groovy

timestamps {

    ansiColor('xterm') {

        node {

            // -------------------------------------------------------------------------
            stage('build') {
                checkout scm
                try {
                  sh 'tox'
                }
                finally {
                  junit '**/test*results.xml'
                }
              }
            // -------------------------------------------------------------------------
            stage('push') {
              echo 'yep'
            }
        }
    }
}
