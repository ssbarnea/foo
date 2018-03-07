#!groovy

timestamps {

    ansiColor('xterm') {

        node {

            // -------------------------------------------------------------------------
            stage('build') {
                checkout scm
                try {
                  sh 'tox'
                } catch(e) {
                  gerrit.review("Verified", "-1", "FAILED!")
                }
                finally {
                  junit '**/test*results.xml'
                }
                gerrit.review("Verified", "1", "PASSED!")
              }
            // -------------------------------------------------------------------------
            stage('push') {
              echo 'yep'
            }
        }
    }
}
