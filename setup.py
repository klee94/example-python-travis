from setuptools import setup, find_packages

setup(
    name = 'python-with-setup-file-example',
    install_requires = [
        'django==1.7.1',
        'PyJWT==0.4.2',
        'rsa==3.4',
        'requests==2.2.1',
        'feedparser==5.1.1',
        'pycrypto==2.4',
        'raven==1.9.4'
    ]
)
