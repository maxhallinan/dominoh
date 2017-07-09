from setuptools import find_packages, setup 

dependencies=['click']

setup(
        author='Max Hallinan',
        author_email='maxhallinan@riseup.net',
        entry_points={
            'console_scripts': [
                'dominoh=dominoh.cli:main']
            },
        name='dominoh',
        install_requires=dependencies,
        packages=find_packages(),
        version='0.0.0')
