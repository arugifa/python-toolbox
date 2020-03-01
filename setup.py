from setuptools import find_namespace_packages, setup

setup(
    name='arugifa-cli',
    version='0.1.0',
    description='CLI utils for my Python projects',
    url='https://github.com/arugifa/cli',
    author='Alexandre Figura',
    license='GNU General Public License v3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_namespace_packages(include=['arugifa.*']),
    install_requires=[
        'tqdm>=4.43',
    ],
)
