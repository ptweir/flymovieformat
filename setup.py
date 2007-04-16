import sys
from distutils.core import setup
import distutils.command.sdist

from motmot_utils import get_svnversion_persistent
version_str = '0.3.dev%(svnversion)s'
version = get_svnversion_persistent('FlyMovieFormat/version.py',version_str)

if 'setuptools' in sys.modules:
    have_setuptools = True
else:
    have_setuptools = False

class sdist_error( distutils.command.sdist.sdist ):
    def run(self,*args,**kw):
        raise RuntimeError('cannot build sdist without setuptools')

if have_setuptools:
    kws=dict(
      extras_require = {
    'wxwrap':     ['wxwrap'],
    'imops':      ['imops>=0.3.dev275'],
    },

      entry_points = {
    'console_scripts': [
    'fmf2bmps = FlyMovieFormat.fmf2bmps:main',
    'fmf_collapse = FlyMovieFormat.fmf_collapse:main',
    ],
    'gui_scripts': [
    'playfmf = FlyMovieFormat.playfmf:main [wxwrap,imops]', # also need python-matplotlib, python-numpy, python-imaging, python-wxgtk2.6
    'fmf_plottimestamps = FlyMovieFormat.fmf_plottimestamps:main',
    ],
    'FlyMovieFormat.exporter_plugins':[
        'txt = FlyMovieFormat.playfmf:TxtFileSaverPlugin',
        'fmf = FlyMovieFormat.playfmf:FmfFileSaverPlugin',
        'image_sequence = FlyMovieFormat.playfmf:ImageSequenceSaverPlugin',
        ],
    },
      )
else:
    kws = dict(
        cmdclass={'sdist':sdist_error},
        )

setup(name='FlyMovieFormat',
      description='support for .fmf files',
      version=version,
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      license='BSD',
      packages = ['FlyMovieFormat'],
      package_data = {'FlyMovieFormat':['playfmf.xrc',
                                        'matplotlibrc',
                                        'description.txt']},
      **kws
      )
