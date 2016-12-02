node {
    stage 'Git workspace'
    git 'https://github.com/samukasmk/grupy-flask-jenkins.git'

    stage 'Build venv'
    sh 'virtualenv --python=python3.5 venv'

    stage 'Install deps'
    sh './venv/bin/pip install -r requirements.txt'

    stage 'Unit tests'
    sh './venv/bin/py.test -ra -v --flakes tests/unit_tests'

    stage 'Functional tests'
    sh './venv/bin/py.test -ra -v --flakes --driver PhantomJS --driver-path=/opt/phantomjs/bin/phantomjs tests/functional_tests'

    stage 'Docker push'
    echo 'Se a app estivesse em um container, poderia ser um docker push'
}
