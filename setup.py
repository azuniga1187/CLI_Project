from setuptools import find_packages, setup

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='pgbackup',
	version='0.1.0',
    	author='Alex Zuniga',
    	author_email='azuniga@gmail.com',
    	desription='A utility for backups',
    	long_description=long_description,
    	long_description_content_type='text/markdown',
    	url='http://github.com/google',
    	packages=find_packages('src'),
	package_dir={'': 'src'},
	install_requires=['boto3'],
	entry_points={'console_scripts': ['pgbackup=pgbackup.cli:main'],}
)	

