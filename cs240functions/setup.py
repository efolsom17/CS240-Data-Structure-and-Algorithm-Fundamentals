from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    package_dir={'': 'src'},  # Specifies that packages are under the src directory
    packages=find_packages(where='src'),  # Tells setuptools to look for packages in src
    description='A simple Python package for internal use',
    long_description='A detailed description of what my package does',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT'
)