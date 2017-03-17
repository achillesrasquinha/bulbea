# Inspired by npm's package.json file
name              = 'bulbea'
version           = '0.1.0'
release           = '0.1.0'
description       = 'A neural stock market predictor and model builder'
long_description  = ['README.md']
keywords          = ['neural', 'network', 'machine', 'deep',
    'learning', 'tensorflow', 'stock', 'market', 'prediction']
authors           = [
    { 'name': 'Achilles Rasquinha', 'email': 'achillesrasquinha@gmail.com' }
]
maintainers       = [
    { 'name': 'Achilles Rasquinha', 'email': 'achillesrasquinha@gmail.com' }
]
license           = 'Apache 2.0'
modules           = [
    'bulbea',
    'bulbea.config',
    'bulbea._util',
    'bulbea.entity',
    'bulbea.learn',
    'bulbea.learn.models',
    'bulbea.learn.evaluation',
    'bulbea.learn.sentiment',
    'bulbea.app',
    'bulbea.app.client',
    'bulbea.app.server',
    'bulbea.app.config'
]
test_modules      = [
    'bulbea._util.tests'
]
homepage          = 'https://achillesrasquinha.github.io/bulbea'
github_username   = 'achillesrasquinha'
github_repository = 'bulbea'
github_url        = '{baseurl}/{username}/{repository}'.format(
    baseurl    = 'https://github.com',
    username   = github_username,
    repository = github_repository)
