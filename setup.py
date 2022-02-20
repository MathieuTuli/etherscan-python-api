from setuptools import setup
from glob import glob

setup(
    name='py_etherscan',
    use_scm_version=True,
    packages=[''],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires='~=3.7',
    install_requires=[
    ],
    extras_require={
    },
    dependency_links=[
    ],
    setup_requires=[
    ],
    license='License :: Other/Proprietary License',
    author='Mathieu Tuli',
    author_email='tuli.mathieu@gmail.com',
    description="Python package for RMSGD's paper code",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3',
    ],
    scripts=glob('bin/*'),
)
