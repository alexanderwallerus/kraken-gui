#this file enables pip installing the package under the provided name
import setuptools

if __name__ == "__main__":
    setuptools.setup(name='krakengui',
                     version='0.1',
                     # packages=setuptools.find_packages(),
                     packages=['krakengui', 'krakengui.utils'],
                     
                     # include data files
                     package_dir={'krakengui': 'krakengui'},
                     package_data={'krakengui': ['fonts/roboto/*.txt', 'fonts/roboto/*.ttf']},
                     # include_package_data=True, #include data files defined in MANIFEST.in
                     
                     install_requires=['pynput']
                     )
