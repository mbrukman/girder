#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  Copyright 2013 Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################

from setuptools import setup, find_packages


# perform the install
setup(
    name='girder-google-analytics',
    version='0.2.0a2',
    description='Allow the tracking of page views via Google Analytics.',
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    url='http://girder.readthedocs.io/en/latest/plugins.html#google-analytics',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ],
    include_package_data=True,
    packages=find_packages(exclude=['plugin_tests']),
    zip_safe=False,
    setup_requires=['setuptools-git'],
    install_requires=['girder>=3.0.0a1'],
    entry_points={
        'girder.plugin': [
            'google_analytics = girder_google_analytics:GoogleAnalyticsPlugin'
        ]
    }
)
