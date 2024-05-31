from setuptools import setup, find_packages

setup(
    name="mlvac",
    version="0.0.1",
    description="text_to_voice.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vladislav Kirvyakov",
    author_email="m1809131@edu.misis.ru",
    url="https://github.com/vacationl33t/mlvac.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "jinja2",
        "requests",
        "diffusers",
        "torch",
        "GPUtil",
        "numba",
        "flask-cors"
    ],
    entry_points={
        "console_scripts": [
            "app = app.app.main:app",
            "model = model.app.main:app"
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='<=3.11',
)
