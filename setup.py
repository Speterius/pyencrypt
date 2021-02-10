from setuptools import setup


setup(
    name='pyencrypt',
    version='0.0.1',
    description='Encrpytion using password utility.',
    license="MIT",
    author='Peter S',
    packages=['pyencrypt'],
    install_requires=['cryptography', 'easygui']
)
