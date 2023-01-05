from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
requirements = [
    'certifi==2022.12.7',
    'charset-normalizer==2.1.1',
    'idna==3.4',
    'requests==2.28.1',
    'urllib3==1.26.13',
]

setup(
    name='solvedpy',
    version='1.0.0',
    author='Youngmin Joo',
    author_email='ymjoo12@hanyang.ac.kr',
    license='MIT',
    url='https://github.com/ymjoo12/solvedac-api',
    install_requires=requirements,
    keywords=[
        'solved.ac', 'solvedac', 'solved.py', 'solvedpy',
    ],
    description='Unofficial solved.ac API wrapper for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    py_modules=['solvedpy'],
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ]
)