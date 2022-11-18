## Ci pipelines

Ci dessous, un exemple de fichiers de configuration de ci pour github et azure devops.

=== "github :material-console:"
    ```yaml
  
    name: ci
  
    on:
      push:
        branches:
          - master
          - main
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - uses: actions/setup-python@v2
            with:
              python-version: 3.x
          - run: pip install mkdocs-material
          - run: mkdocs gh-deploy --force
    ```
=== "Azure :material-shimmer:"

    ```yaml
  
    trigger:
      - main
    
    pool:
      vmImage: ubuntu-latest
      
      variables:
      imageName: 'flask_test_app'
      DOCKER_BUILDKIT: 1
    
    stages:
      - stage: test_app_dependencies_and_test
        steps:
          - task: UsePythonVersion@0
            inputs:
            versionSpec: '3.9'
            displayName: 'Use Python 3.9'
        
          - script: python -m pip install --upgrade pip setuptools wheel
            displayName: 'Install tools'
        
          - script: |
              python -m pip install --upgrade pip
              pip install -r requirements.txt
              displayName: 'Install dependencies'
    
          - script: |
              pip install pytest pytest-azurepipelines
              pip install pytest-cov
              pytest --doctest-modules --junitxml=junit/test-results.xml --cov=. --cov-report=xml
              displayName: 'pytest'
    
          - task: PublishTestResults@2
            condition: succeededOrFailed()
            inputs:
              testResultsFiles: '**/test-*.xml'
              testRunTitle: 'Publish test results'
        
          - stage: build_doc
            steps:
              - script: |
                  pip install mkdocs-material mkdocs-material-extensions mkdocs mkdocstrings
                  mkdocs build
                  displayName: 'Install and Build MkDocs Material'
    
      - stage: deploy
        jobs:
          - job: build_push_app_container
            steps:
              - task: Docker@2
                displayName: 'Build et Push app image'
                inputs:
                  containerRegistry: 'clogic_docker_registry'
                  repository: 'flask_app_auto'
                  command: 'buildAndPush'
                  Dockerfile: '**/Dockerfile'
          - job: build_push_doc_container
            steps:
              - task: Docker@2
                displayName: 'Build et Push doc image'
                inputs:
                  containerRegistry: 'clogic_docker_registry'
                  repository: 'oa-formation'
                  command: 'buildAndPush'
                  Dockerfile: '**/Dockerfile_doc'
    ```


