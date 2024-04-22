from setuptools import setup, find_packages

setup(
    name='cs240functions',
    version='0.1',
    package_dir={'': 'src'},  # Specifies that packages are under the src directory
    packages=find_packages(where='src'),  # Tells setuptools to look for packages in src
    description='CS240 Functions - for personal use',
    long_description='Package containing all functions and classes created during CS240 Spring 2023',
    author='Eric Folsom',
    author_email='eric.folsom17@gmail.com',
    license='MIT'
)