from setuptools import setup, find_packages


setup(name='gym_tictactoe',
      version='0.0.1',
      insatll_required=['gym', 'numpy', 'click', 'tqdm'],
      packages=find_packages()
      )
