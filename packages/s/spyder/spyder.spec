#
# spec file for package spyder
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# The test suite is very peculiar about the testing environment, impossible to replicate for rpmbuild
# Also, the tests fail randomly with segfaults on the obs servers
# You MUST checkout the app in your live system and play with it before submitting an update.
%bcond_with     test
Name:           spyder
Version:        6.0.4
Release:        0
Summary:        The Scientific Python Development Environment
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.spyder-ide.org/
Source:         https://github.com/spyder-ide/spyder/archive/v%{version}.tar.gz#/spyder-%{version}.tar.gz
Source1:        spyder-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.7
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools >= 49.6.0
BuildRequires:  python3-wheel
Requires:       %{name}-lang
Requires:       python3-PyQt5 >= 5.15
Requires:       python3-PyQtWebEngine >= 5.15
Requires:       python3-Pygments >= 2.0
Requires:       python3-QtPy >= 2.4
Requires:       python3-Rtree >= 0.9.7
Requires:       python3-Sphinx >= 0.6.6
Requires:       python3-aiohttp >= 3.9.3
Requires:       python3-atomicwrites >= 1.2.0
Requires:       python3-chardet >= 2.0.0
Requires:       python3-cloudpickle >= 0.5.0
Requires:       python3-cookiecutter >= 1.6.0
Requires:       python3-diff-match-patch >= 20181111
Requires:       python3-importlib-metadata >= 4.6.0
Requires:       python3-intervaltree
Requires:       python3-jellyfish >= 0.7
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-keyring >= 17.0.0
Requires:       python3-nbconvert >= 4.0
Requires:       python3-numpydoc >= 0.6.0
Requires:       python3-parso >= 0.7.0
Requires:       python3-pexpect >= 4.4.0
Requires:       python3-pickleshare >= 0.4
Requires:       python3-psutil >= 5.3
Requires:       python3-pygithub >= 2.3.0
Requires:       python3-pylint-venv >= 3.0.2
Requires:       python3-pyls-spyder >= 0.4.0
Requires:       python3-pyuca >= 1.2
Requires:       python3-pyxdg >= 0.26
Requires:       python3-pyzmq >= 24
Requires:       python3-qstylizer >= 0.2.2
Requires:       python3-setuptools >= 49.6.0
Requires:       python3-textdistance >= 4.2.0
Requires:       python3-three-merge >= 0.1.1
Requires:       python3-watchdog
Requires:       python3-yarl >= 1.9.4
Requires:       (python3-QDarkStyle >= 3.2.0 with python3-QDarkStyle < 3.3.0)
Requires:       (python3-QtAwesome >= 1.3.1 with python3-QtAwesome < 1.4)
Requires:       (python3-asyncssh >= 2.14 with python3-asyncssh < 3)
Requires:       (python3-ipython >= 8.13 with python3-ipython < 9)
Requires:       (python3-jedi >= 0.17.2 with python3-jedi < 0.20)
Requires:       (python3-pylint >= 3.1 with python3-pylint < 4)
Requires:       (python3-python-lsp-black >= 2.0.0 with python3-python-lsp-black < 3)
Requires:       (python3-python-lsp-server-all >= 1.12.0 with python3-python-lsp-server-all < 1.13)
Requires:       (python3-qtconsole >= 5.6.1 with python3-qtconsole < 5.7)
Requires:       (python3-spyder-kernels >= 3.0.3 with python3-spyder-kernels < 3.1)
Requires:       (python3-superqt >= 0.6.2 with python3-superqt < 1)
Recommends:     git-core
Recommends:     python3-Cython
Recommends:     python3-Pillow
Recommends:     python3-matplotlib
Recommends:     python3-matplotlib-qt
Recommends:     python3-numpy
Recommends:     python3-opengl
Recommends:     python3-pandas
Recommends:     python3-scipy
Recommends:     python3-sympy
Suggests:       %{name}-line-profiler
Suggests:       %{name}-memory-profiler
Suggests:       %{name}-notebook
Suggests:       %{name}-terminal
Suggests:       %{name}-unittest
Provides:       python3-spyder = %{version}
Provides:       python3-spyderlib = %{version}
Provides:       spyder3 = %{version}
Provides:       spyder3-breakpoints = %{version}
Provides:       spyder3-profiler = %{version}
Provides:       spyder3-pylint = %{version}
Obsoletes:      python3-spyder < %{version}
Obsoletes:      python3-spyderlib < %{version}
Obsoletes:      spyder3 < %{version}
Obsoletes:      spyder3-breakpoints < %{version}
Obsoletes:      spyder3-profiler < %{version}
Obsoletes:      spyder3-pylint < %{version}
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
# purely for testing
BuildRequires:  python3-flaky
BuildRequires:  python3-pyaml
BuildRequires:  python3-pytest >= 5.0
BuildRequires:  python3-pytest-lazy-fixture
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-order
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-timeout
BuildRequires:  xdpyinfo
BuildRequires:  xvfb-run
# extras
BuildRequires:  git-core
BuildRequires:  python3-Cython
BuildRequires:  python3-Pillow
BuildRequires:  python3-matplotlib
BuildRequires:  python3-matplotlib-qt
BuildRequires:  python3-matplotlib-tk
BuildRequires:  python3-numpy
BuildRequires:  python3-opengl
BuildRequires:  python3-pandas
BuildRequires:  python3-scipy
BuildRequires:  python3-sympy
%endif
# runtime
BuildRequires:  python3-Pygments >= 2.0
BuildRequires:  python3-PyQt5 >= 5.15
BuildRequires:  python3-PyQtWebEngine >= 5.15
BuildRequires:  python3-QtPy >= 2.4
BuildRequires:  python3-Rtree >= 0.9.7
BuildRequires:  python3-Sphinx >= 0.6.6
BuildRequires:  python3-aiohttp >= 3.9.3
BuildRequires:  python3-atomicwrites >= 1.2.0
BuildRequires:  python3-chardet >= 2.0.0
BuildRequires:  python3-cloudpickle >= 0.5.0
BuildRequires:  python3-cookiecutter >= 1.6.0
BuildRequires:  python3-diff-match-patch >= 20181111
BuildRequires:  python3-importlib-metadata >= 4.6.0
BuildRequires:  python3-intervaltree
BuildRequires:  python3-jellyfish >= 0.7
BuildRequires:  python3-jsonschema >= 3.2.0
BuildRequires:  python3-keyring >= 17.0.0
BuildRequires:  python3-nbconvert >= 4.0
BuildRequires:  python3-numpydoc >= 0.6.0
BuildRequires:  python3-parso >= 0.7.0
BuildRequires:  python3-pexpect >= 4.4.0
BuildRequires:  python3-pickleshare >= 0.4
BuildRequires:  python3-psutil >= 5.3
BuildRequires:  python3-pygithub >= 2.3.0
BuildRequires:  python3-pylint-venv >= 3.0.2
BuildRequires:  python3-pyls-spyder >= 0.4.0
BuildRequires:  python3-pyuca >= 1.2
BuildRequires:  python3-pyxdg >= 0.26
BuildRequires:  python3-pyzmq >= 24
BuildRequires:  python3-qstylizer >= 0.2.2
BuildRequires:  python3-setuptools >= 49.6.0
BuildRequires:  python3-textdistance >= 4.2.0
BuildRequires:  python3-three-merge >= 0.1.1
BuildRequires:  python3-watchdog
BuildRequires:  python3-yarl >= 1.9.4
BuildRequires:  (python3-QDarkStyle >= 3.2.0 with python3-QDarkStyle < 3.3.0)
BuildRequires:  (python3-QtAwesome >= 1.3.1 with python3-QtAwesome < 1.4)
BuildRequires:  (python3-asyncssh >= 2.14 with python3-asyncssh < 3)
BuildRequires:  (python3-ipython >= 8.13 with python3-ipython < 9)
BuildRequires:  (python3-jedi >= 0.17.2 with python3-jedi < 0.20)
BuildRequires:  (python3-pylint >= 3.1 with python3-pylint < 4)
BuildRequires:  (python3-python-lsp-black >= 2.0.0 with python3-python-lsp-black < 3)
BuildRequires:  (python3-python-lsp-server-all >= 1.12.0 with python3-python-lsp-server-all < 1.13)
BuildRequires:  (python3-qtconsole >= 5.6.1 with python3-qtconsole < 5.7)
BuildRequires:  (python3-spyder-kernels >= 3.0.3 with python3-spyder-kernels < 3.1)
BuildRequires:  (python3-superqt >= 0.6.2 with python3-superqt < 1)
# /SECTION

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.
It features a combination of the editing, analysis, debugging
and profiling functionality of a development tool with the
data exploration, interactive execution, deep inspection and
visualization capabilities of an analysis package. Additionally,
Spyder offers built-in integration with scientific
libraries, including NumPy, SciPy, Pandas, IPython, QtConsole,
Matplotlib, SymPy, and more, and can be extended further with
full plugin support.

%package lang
# expansion of lang_package because the macro does not handle the rename
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       %{name}-lang-all = %{version}
Provides:       spyder3-lang = %{version}
Obsoletes:      spyder3-lang < %{version}
BuildArch:      noarch

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup -p1 -n spyder-%{version}

# Fix wrong-file-end-of-line-encoding RPMLint warning
sed -i 's/\r$//' spyder/app/restart.py
sed -i 's/\r$//' LICENSE.txt CHANGELOG.md

# Remove shebang for non-executable-script RPMLint warning
sed -i -e '/^#!\//, 1d' spyder/app/restart.py

chmod -x spyder/images/*/*.svg

# macOS specific script
rm spyder/utils/check-git.sh

# Upstream brings its fixed versions for pyls, qdarksstyle and spyder-kernels for its
# test environment, but we want to test against installed packages.
rm -r external-deps/*

sed -i "s/installer = 'pip'/installer = 'openSUSE RPM'/" spyder/__init__.py
# avoid mtime destroying dedup
echo "# Unique config __init__.pyc" >> spyder/config/__init__.py

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install

# install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ln -s %{python3_sitelib}/spyder/images/spyder.svg spyder.svg
popd
pushd %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
ln -s %{_datadir}/icons/spyder.png spyder.png
popd

# get the language files
%find_lang spyder %{name}.lang
# remove source language files
find %{buildroot}%{python3_sitelib}/spyder/locale -name '*.po' -delete
find %{buildroot}%{python3_sitelib}/spyder/locale -name '*.pot' -delete
%fdupes %{buildroot}%{python3_sitelib}

%if %{with test}
%check
export CI=1
sed -i 's/if CI:/if False:/' runtests.py
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
mkdir -p /tmp/spyder-abuild

export PYTHONPATH=%{buildroot}%{python3_sitelib}:/tmp/spyder-abuild/testroot/%{python3_sitelib}
# install boilerplate test package
pushd spyder/app/tests/spyder-boilerplate
python3 setup.py install --root /tmp/spyder-abuild/testroot --prefix %{_prefix}
popd

# Upstream splits the tests into slow and fast ones.
# Add all tests which must be skipped into $donttest.

donttest="xxxxxxxxxxxxx"
export donttest

# Can't use pytest-xvfb because the tests leave widgets open and trigger https://github.com/The-Compiler/pytest-xvfb/issues/11
# create test script so that we can use one Xvfb with both test suites:
echo '
#!/bin/bash
set -e
testcmd=(python3 runtests.py -m "not no_xvfb" --timeout 1800 -ra -k "not (${donttest:4})" -x --tb long -l)
"${testcmd[@]}"
"${testcmd[@]}" --run-slow
' > runtests.sh
xvfb-run --server-args "-screen 0 1920x1080x24" bash runtests.sh
%endif

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/spyder
%{_datadir}/applications/spyder.desktop
%{python3_sitelib}/spyder/
%{python3_sitelib}/spyder-%{version}.dist-info
%exclude %{python3_sitelib}/spyder/locale/
%{_datadir}/icons/spyder.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/spyder.svg
%{_datadir}/icons/hicolor/128x128/apps/spyder.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.spyder_ide.spyder.appdata.xml

%files lang -f %{name}.lang
%license LICENSE.txt
%dir %{python3_sitelib}/spyder/locale/
%dir %{python3_sitelib}/spyder/locale/*
%dir %{python3_sitelib}/spyder/locale/*/LC_MESSAGES

%changelog
