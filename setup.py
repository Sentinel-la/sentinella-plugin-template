import sys
from setuptools import setup, find_packages


exclude = ['sentinella.myplugin.myplugin']

install_requires = []

install_requires.append('trollius==2.0')


setup(
    name='sentinella-myplugin',
    description='Some description',
    version='0.1',
    packages=find_packages(exclude=exclude),
    zip_safe=False,
    namespace_packages=['sentinella'],
    install_requires=install_requires,
    author='My Name',
    author_email='email@domain.com',
    url='https://github.com/Sentinel-la/sentinella-plugin',
    license='ASF',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Monitoring',
    ],
    keywords='monitoring metrics agent openstack sentinella',
)
