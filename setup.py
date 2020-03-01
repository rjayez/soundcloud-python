import re

from setuptools import setup


version = None
for line in open('./soundcloud/__init__.py'):
    m = re.search('__version__\s*=\s*(.*)', line)
    if m:
        version = m.group(1).strip()[1:-1]  # quotes
        break
assert version
print(version)

setup(
    name='soundcloud',
    version=version,
    description='A friendly wrapper library for the Soundcloud API',
    author='SoundCloud',
    author_email='api@soundcloud.com',
    url='https://github.com/soundcloud/soundcloud-python',
    license='BSD',
    packages=['soundcloud'],
    include_package_data=True,
    package_data={
        '': ['README.rst']
    },
    install_requires=[
        'nose>=1.3.7',
        'fudge==1.1.1',
        'requests>=2.22.0',
        'simplejson>=3.17.0',
        'six>=1.13.0'
    ],
    tests_require=[
        'nose>=1.3.7',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
