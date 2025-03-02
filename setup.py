from setuptools import setup, find_packages
import setuptools
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Operating System :: Microsoft :: Windows',
  'Programming Language :: Python :: 3'
]

setup(
  name='discofy',
  version='1.2',
  description='Discofy allows control of Spotify playback through Discord API, offering features like play/pause, track skipping, volume control, and device management.',
  long_description=open('README.txt', encoding='utf-8').read() + '\n\n' + open('CHANGELOG.txt', encoding='utf-8').read(),
  long_description_content_type='text/markdown',  # Ustawienie poprawnego formatu Markdown
  url='',  
  author='Echopixel',
  author_email='echopixel@proton.me', 
  project_urls={
    "Documentation": "https://xocto.readthedocs.io",
    "Changelog": "https://github.com/octoenergy/xocto/blob/main/CHANGELOG.md",
     "Issues": "https://github.com/octoenergy/xocto/issues",
  },
  classifiers=classifiers,
  license='CC BY-SA 4.0',
  keywords='spotify', 
  packages=find_packages(),
  install_requires=[],
  extras_require={
      "dev": ["pytest>=7.0", "twine>=4.0.2"],
  },
)
