from setuptools import setup, find_packages

setup(
    name='image_converter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'PyQt6',  # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'image_converter=image_converter.cli:main',  # Adjust as needed
        ],
    },
    author='hexzhen3x7',
    author_email='hexzhen3x7@outlook.de',
    description='A simple image converter tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/org-blackzspace-de/image-converter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13',
)