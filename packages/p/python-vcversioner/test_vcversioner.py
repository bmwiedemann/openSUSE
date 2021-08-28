# Copyright (c) Aaron Gallagher <_@habnab.it>
# See COPYING for details.

from __future__ import unicode_literals

import os

import pytest

import vcversioner


try:
    unicode
except NameError:
    unicode = str


class FakePopen(object):
    def __init__(self, stdout, stderr=b''):
        self.stdout = stdout
        self.stderr = stderr

    def communicate(self):
        return self.stdout, self.stderr

    def __call__(self, *args, **kwargs):
        return self

class RaisingFakePopen(object):
    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        raise OSError('hi!')

empty = FakePopen(b'')
invalid = FakePopen(b'foob')
basic_version = FakePopen(b'1.0-0-gbeef')
dev_version = FakePopen(b'1.0-2-gfeeb')
hg_version = FakePopen(b'1.0-1-hgbeef')
git_failed = FakePopen(b'', b'fatal: whatever')


class FakeOpen(object):
    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        raise OSError('hi!')


@pytest.fixture
def gitdir(tmpdir):
    tmpdir.chdir()
    tmpdir.join('.git').mkdir()
    return tmpdir

@pytest.fixture
def hgdir(tmpdir):
    tmpdir.chdir()
    tmpdir.join('.hg').mkdir()
    return tmpdir


def test_astounding_success(gitdir):
    "Successful output from git is cached and returned."
    version = vcversioner.find_version(Popen=basic_version)
    assert version == ('1.0', '0', 'gbeef')
    with gitdir.join('version.txt').open() as infile:
        assert infile.read() == '1.0-0-gbeef'

def test_no_git(gitdir):
    "If git fails and there's no version.txt, abort."
    with pytest.raises(SystemExit) as excinfo:
        vcversioner.find_version(Popen=empty)
    assert excinfo.value.args[0] == 2
    assert not gitdir.join('version.txt').check()

def test_when_Popen_raises(gitdir):
    "If *spawning* git fails and there's no version.txt, abort."
    with pytest.raises(SystemExit) as excinfo:
        vcversioner.find_version(Popen=RaisingFakePopen())
    assert excinfo.value.args[0] == 2
    assert not gitdir.join('version.txt').check()

def test_no_git_but_version_file(gitdir):
    "If git fails but there's a version.txt, that's fine too."
    with gitdir.join('version.txt').open('w') as outfile:
        outfile.write('1.0-0-gbeef')
    version = vcversioner.find_version(Popen=empty)
    assert version == ('1.0', '0', 'gbeef')

def test_Popen_raises_but_version_file(gitdir):
    "If spawning git fails but there's a version.txt, that's similarly fine."
    with gitdir.join('version.txt').open('w') as outfile:
        outfile.write('1.0-0-gbeef')
    version = vcversioner.find_version(Popen=RaisingFakePopen())
    assert version == ('1.0', '0', 'gbeef')

def test_version_file_with_root(gitdir):
    "version.txt gets read from the project root by default."
    with gitdir.join('version.txt').open('w') as outfile:
        outfile.write('1.0-0-gbeef')
    version = vcversioner.find_version(
        root=gitdir.strpath, Popen=RaisingFakePopen())
    assert version == ('1.0', '0', 'gbeef')

def test_invalid_git(gitdir):
    "Invalid output from git is a failure too."
    with pytest.raises(SystemExit) as excinfo:
        vcversioner.find_version(Popen=invalid)
    assert excinfo.value.args[0] == 2
    assert not gitdir.join('version.txt').check()

def test_invalid_version_file(gitdir):
    "Invalid output in version.txt is similarly a failure."
    with gitdir.join('version.txt').open('w') as outfile:
        outfile.write('foob')
    with pytest.raises(SystemExit) as excinfo:
        vcversioner.find_version(Popen=empty)
    assert excinfo.value.args[0] == 2

def test_dev_version(gitdir):
    ".post version numbers are automatically created."
    version = vcversioner.find_version(Popen=dev_version)
    assert version == ('1.0.post2', '2', 'gfeeb')
    with gitdir.join('version.txt').open() as infile:
        assert infile.read() == '1.0-2-gfeeb'

def test_dev_version_disabled(gitdir):
    ".post version numbers can also be disabled."
    version = vcversioner.find_version(Popen=dev_version, include_dev_version=False)
    assert version == ('1.0', '2', 'gfeeb')
    with gitdir.join('version.txt').open() as infile:
        assert infile.read() == '1.0-2-gfeeb'

def test_custom_vcs_args(gitdir):
    "The command to execute to get the version can be customized."
    popen = RaisingFakePopen()
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=popen, vcs_args=('foo', 'bar'))
    assert popen.args[0] == ['foo', 'bar']

def test_custom_vcs_args_substitutions(gitdir):
    "The command arguments have some substitutions performed."
    popen = RaisingFakePopen()
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=popen, vcs_args=('foo', 'bar', '%(pwd)s', '%(root)s'))
    assert popen.args[0] == ['foo', 'bar', gitdir.strpath, gitdir.strpath]

def test_custom_vcs_args_substitutions_with_different_root(tmpdir):
    "Specifying a different root will cause that root to be substituted."
    tmpdir.chdir()
    popen = RaisingFakePopen()
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=popen, root='/spam', vcs_args=('%(root)s',))
    assert popen.args[0] == ['/spam']

def test_custom_version_file(gitdir):
    "The version.txt file can have a unique name."
    version = vcversioner.find_version(Popen=basic_version, version_file='custom.txt')
    assert version == ('1.0', '0', 'gbeef')
    with gitdir.join('custom.txt').open() as infile:
        assert infile.read() == '1.0-0-gbeef'

def test_custom_version_file_reading(gitdir):
    "The custom version.txt can be read from as well."
    with gitdir.join('custom.txt').open('w') as outfile:
        outfile.write('1.0-0-gbeef')
    version = vcversioner.find_version(Popen=empty, version_file='custom.txt')
    assert version == ('1.0', '0', 'gbeef')

def test_version_file_disabled(gitdir):
    "The version.txt file can be disabled too."
    version = vcversioner.find_version(Popen=basic_version, version_file=None)
    assert version == ('1.0', '0', 'gbeef')
    assert not gitdir.join('version.txt').check()

def test_version_file_disabled_git_failed(gitdir):
    "If version.txt is disabled and git fails, nothing can be done."
    with pytest.raises(SystemExit) as excinfo:
        vcversioner.find_version(Popen=empty, version_file=None)
    assert excinfo.value.args[0] == 2
    assert not gitdir.join('version.txt').check()

def test_version_file_disabled_Popen_raises(gitdir):
    "If version.txt is disabled and git fails to spawn, abort as well."
    with pytest.raises(SystemExit) as excinfo:
        vcversioner.find_version(Popen=RaisingFakePopen(), version_file=None)
    assert excinfo.value.args[0] == 2
    assert not gitdir.join('version.txt').check()

def test_namedtuple(tmpdir):
    "The output namedtuple has attribute names too."
    tmpdir.chdir()
    version = vcversioner.find_version(Popen=basic_version, version_file=None, vcs_args=[])
    assert version.version == '1.0'
    assert version.commits == '0'
    assert version.sha == 'gbeef'

def test_namedtuple_nonzero_commits(tmpdir):
    "The output namedtuple can have a nonzero number of commits."
    tmpdir.chdir()
    version = vcversioner.find_version(Popen=dev_version, version_file=None, vcs_args=[])
    assert version.version == '1.0.post2'
    assert version.commits == '2'
    assert version.sha == 'gfeeb'

def test_version_module_paths(gitdir):
    "Version modules can be written out too."
    paths = ['foo.py', 'bar.py']
    vcversioner.find_version(
        Popen=basic_version, version_module_paths=paths)
    for path in paths:
        with open(path) as infile:
            assert infile.read() == """
# This file is automatically generated by setup.py.
__version__ = '1.0'
__sha__ = 'gbeef'
__revision__ = 'gbeef'
"""

def test_git_arg_path_translation(gitdir, monkeypatch):
    "/ is translated into the correct path separator in git arguments."
    monkeypatch.setattr(os, 'sep', ':')
    popen = RaisingFakePopen()
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=popen, vcs_args=['spam/eggs'], version_file=None)
    assert popen.args[0] == ['spam:eggs']

def test_version_file_path_translation(gitdir, monkeypatch):
    "/ is translated into the correct path separator for version.txt."
    monkeypatch.setattr(os, 'sep', ':')
    open = FakeOpen()
    with pytest.raises(OSError):
        vcversioner.find_version(Popen=basic_version, open=open, version_file='spam/eggs', vcs_args=[])
    assert open.args[0] == 'spam:eggs'

def test_git_output_on_no_version_file(gitdir, capsys):
    "The output from git is shown if it failed and the version file is disabled."
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=git_failed, version_file=None, vcs_args=[])
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        'vcversioner: [] failed.\n'
        'vcversioner: -- VCS output follows --\n'
        'vcversioner: fatal: whatever\n')

def test_git_output_on_version_file_absent(gitdir, capsys):
    "The output from git is shown if it failed and the version file doesn't exist."
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=git_failed, version_file='version.txt', vcs_args=[])
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "vcversioner: [] failed and %r isn't present.\n"
        'vcversioner: are you installing from a github tarball?\n'
        'vcversioner: -- VCS output follows --\n'
        'vcversioner: fatal: whatever\n' % ('version.txt',))

def test_git_output_on_version_unparsable(gitdir, capsys):
    "The output from git is shown if it failed and the version couldn't be parsed."
    gitdir.join('version.txt').write('doof')
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=git_failed, version_file='version.txt', vcs_args=[])
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "vcversioner: %r (from %r) couldn't be parsed into a version.\n"
        'vcversioner: -- VCS output follows --\n'
        'vcversioner: fatal: whatever\n' % ('doof', 'version.txt'))

def test_no_git_output_on_version_unparsable(capsys):
    "The output from git is not shown if git succeeded but the version couldn't be parsed."
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=invalid, version_file='version.txt', vcs_args=[])
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "vcversioner: %r (from VCS) couldn't be parsed into a version.\n" % ('foob',))

def test_no_output_on_success(gitdir, capsys):
    "There is no output if everything succeeded."
    vcversioner.find_version(Popen=basic_version)
    out, err = capsys.readouterr()
    assert not out
    assert not err

def test_no_output_on_version_file_success(gitdir, capsys):
    "There is no output if everything succeeded, even if the version was read from a version file."
    gitdir.join('version.txt').write('1.0-0-gbeef')
    vcversioner.find_version(Popen=git_failed)
    out, err = capsys.readouterr()
    assert not out
    assert not err

def test_strip_leading_v(gitdir):
    "Leading 'v's are stripped from tags."
    version = vcversioner.find_version(Popen=FakePopen(b'v1.0-0-gbeef'))
    assert version == ('1.0', '0', 'gbeef')

def test_strip_leading_prefix(gitdir):
    "The leading prefix stripped from tags can be customized."
    version = vcversioner.find_version(Popen=FakePopen(b'debian/1.0-0-gbeef'), strip_prefix='debian/')
    assert version == ('1.0', '0', 'gbeef')

def test_git_args_deprecation(gitdir):
    "git_args is deprecated."
    pytest.deprecated_call(vcversioner.find_version, git_args=['git', 'spam'], Popen=basic_version)

def test_git_args_still_works(gitdir):
    "git_args still works like vcs_args."
    popen = RaisingFakePopen()
    with pytest.raises(SystemExit):
        vcversioner.find_version(git_args=['git', 'spam'], Popen=popen)
    assert popen.args[0] == ['git', 'spam']

def test_hg_detection(hgdir):
    ".hg directories get detected and the appropriate hg command gets run."
    popen = RaisingFakePopen()
    with pytest.raises(SystemExit):
        vcversioner.find_version(Popen=popen)
    assert popen.args[0] == [
        'hg', 'log', '-R', hgdir.strpath, '-r', '.', '--template',
        '{latesttag}-{latesttagdistance}-hg{node|short}']

def test_no_vcs_no_version_file(tmpdir, capsys):
    "If no VCS is detected with no version_file, vcversioner aborts."
    tmpdir.chdir()
    with pytest.raises(SystemExit):
        vcversioner.find_version(version_file=None, Popen=basic_version)
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        'vcversioner: no VCS could be detected in %r.\n' % (unicode(tmpdir.strpath),))

def test_no_vcs_absent_version_file(tmpdir, capsys):
    "If no VCS is detected with an absent version_file, vcversioner aborts."
    tmpdir.chdir()
    with pytest.raises(SystemExit):
        vcversioner.find_version(version_file='version.txt', Popen=basic_version)
    out, err = capsys.readouterr()
    assert not err
    assert out == (
        "vcversioner: no VCS could be detected in %r and %r isn't present.\n"
        "vcversioner: are you installing from a github tarball?\n" % (
            unicode(tmpdir.strpath), 'version.txt'))

def test_decrement_dev_version(gitdir):
    "decrement_dev_version will subtract one from the number of commits."
    version = vcversioner.find_version(decrement_dev_version=True, Popen=dev_version)
    assert version == ('1.0.post1', '1', 'gfeeb')

def test_decrement_dev_version_to_zero(gitdir):
    "decrement_dev_version with one commit will produce a non-dev version number."
    version = vcversioner.find_version(decrement_dev_version=True, Popen=FakePopen(b'1.0-1-gbeef'))
    assert version == ('1.0', '0', 'gbeef')

def test_automatic_decrement_dev_version_with_hg(hgdir):
    "decrement_dev_version gets turned on automatically with hg revisions."
    version = vcversioner.find_version(Popen=hg_version)
    assert version == ('1.0', '0', 'hgbeef')

def test_automatic_decrement_dev_version_disabled(hgdir):
    "decrement_dev_version does not get turned on automatically if explicitly disabled."
    version = vcversioner.find_version(decrement_dev_version=False, Popen=hg_version)
    assert version == ('1.0.post1', '1', 'hgbeef')

def test_version_file_substituted_with_no_vcs(tmpdir):
    "The version file is substituted even if no VCS is present."
    tmpdir.chdir()
    tmpdir.join('version.txt').write('1.0-0-gbeef')
    version = vcversioner.find_version(Popen=empty)
    assert version == ('1.0', '0', 'gbeef')


class Struct(object):
    pass

def test_setup_astounding_success(tmpdir):
    "``find_version`` can be called through distutils too."
    tmpdir.chdir()
    dist = Struct()
    dist.metadata = Struct()
    vcversioner.setup(
        dist, 'vcversioner',
        {str('Popen'): basic_version, str('version_file'): None,
         str('vcs_args'): []})
    assert dist.metadata.version == '1.0'
