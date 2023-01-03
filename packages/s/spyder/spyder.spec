#
# spec file for package spyder
#
# Copyright (c) 2023 SUSE LLC
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


# The tests fail randomly with segfaults on the obs servers.
# You MUST test locally with `osc build --with test` and checkout the app in
# your live system before submitting an update.
%bcond_with     test
Name:           spyder
Version:        5.4.1
Release:        0
Summary:        The Scientific Python Development Environment
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.spyder-ide.org/
Source:         https://github.com/spyder-ide/spyder/archive/v%{version}.tar.gz#/spyder-%{version}.tar.gz
Source1:        spyder-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools >= 49.6.0
BuildRequires:  update-desktop-files
Requires:       %{name}-lang
Requires:       cookiecutter >= 1.6.0
Requires:       python3-Pygments >= 2.0
Requires:       python3-QtAwesome >= 1.2.1
Requires:       python3-QtPy >= 2.1.0
Requires:       python3-Rtree >= 0.9.7
Requires:       python3-Sphinx >= 0.6.6
Requires:       python3-atomicwrites >= 1.2.0
Requires:       python3-autopep8
Requires:       python3-chardet >= 2.0.0
Requires:       python3-cloudpickle >= 0.5.0
Requires:       python3-diff-match-patch >= 20181111
Requires:       python3-flake8 >= 3.8.0
Requires:       python3-intervaltree
Requires:       python3-ipython >= 7.31.1
Requires:       python3-jedi >= 0.17.2
Requires:       python3-jellyfish >= 0.7
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-keyring >= 17.0.0
Requires:       python3-mccabe >= 0.6.0
Requires:       python3-nbconvert >= 4.0
Requires:       python3-numpydoc >= 0.6.0
Requires:       python3-parso >= 0.7.0
Requires:       python3-pexpect >= 4.4.0
Requires:       python3-pickleshare >= 0.4
Requires:       python3-psutil >= 5.3
Requires:       python3-pycodestyle >= 2.6.0
Requires:       python3-pydocstyle >= 2.0.0
Requires:       python3-pyflakes >= 2.2.0
Requires:       python3-pylint-venv >= 2.1.1
Requires:       python3-pyls-spyder >= 0.4.0
Requires:       python3-python-lsp-black >= 1.2.0
Requires:       python3-pyxdg >= 0.26
Requires:       python3-pyzmq >= 22.1.0
Requires:       python3-qstylizer >= 0.2.2
Requires:       python3-qt5
Requires:       python3-qtwebengine-qt5
Requires:       python3-rope >= 0.10.5
Requires:       python3-setuptools >= 49.6.0
Requires:       python3-textdistance >= 4.2.0
Requires:       python3-three-merge >= 0.1.1
Requires:       python3-watchdog
Requires:       python3-whatthepatch
Requires:       python3-yapf
Requires:       (python3-QDarkStyle >= 3.0.2 with python3-QDarkStyle < 3.1.0)
Requires:       (python3-pylint >= 2.5.0 with python3-pylint < 3)
Requires:       (python3-python-lsp-server >= 1.7.0 with python3-python-lsp-server < 1.8)
Requires:       (python3-qtconsole >= 5.4.0 with python3-qtconsole < 5.5.0)
Requires:       (python3-spyder-kernels >= 2.4.1 with python3-spyder-kernels < 2.5)
Recommends:     %{name}-dicom
Recommends:     %{name}-hdf5
Recommends:     python3-Cython >= 0.21
Recommends:     python3-Pillow
Recommends:     python3-matplotlib >= 2.0.0
Recommends:     python3-numpy >= 1.7
Recommends:     python3-pandas >= 1.1.1
Recommends:     python3-scipy >= 0.17.0
Recommends:     python3-sympy >= 0.7.3
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
BuildRequires:  cookiecutter >= 1.6.0
BuildRequires:  git-core
BuildRequires:  python3-Cython >= 0.21
BuildRequires:  python3-Pillow
BuildRequires:  python3-Pygments >= 2.0
BuildRequires:  python3-QtAwesome >= 1.2.1
BuildRequires:  python3-QtPy >= 2.1.0
BuildRequires:  python3-Rtree >= 0.9.7
BuildRequires:  python3-Sphinx >= 0.6.6
BuildRequires:  python3-atomicwrites >= 1.2.0
BuildRequires:  python3-autopep8
BuildRequires:  python3-chardet >= 2.0.0
BuildRequires:  python3-cloudpickle >= 0.5.0
BuildRequires:  python3-diff-match-patch >= 20181111
BuildRequires:  python3-flake8 >= 3.8.0
BuildRequires:  python3-flaky
BuildRequires:  python3-intervaltree
BuildRequires:  python3-ipython >= 7.31.1
BuildRequires:  python3-jedi >= 0.17.2
BuildRequires:  python3-jellyfish >= 0.7
BuildRequires:  python3-jsonschema >= 3.2.0
BuildRequires:  python3-keyring >= 17.0.0
BuildRequires:  python3-matplotlib >= 2.0.0
BuildRequires:  python3-matplotlib-qt5
BuildRequires:  python3-matplotlib-tk
BuildRequires:  python3-mccabe >= 0.6.0
BuildRequires:  python3-nbconvert >= 4.0
BuildRequires:  python3-numpydoc >= 0.6.0
BuildRequires:  python3-opengl
BuildRequires:  python3-pandas >= 1.1.1
BuildRequires:  python3-parso >= 0.7.0
BuildRequires:  python3-pexpect >= 4.4.0
BuildRequires:  python3-pickleshare >= 0.4
BuildRequires:  python3-psutil >= 5.3
BuildRequires:  python3-pyaml
BuildRequires:  python3-pycodestyle >= 2.6.0
BuildRequires:  python3-pydocstyle >= 2.0.0
BuildRequires:  python3-pyflakes >= 2.2.0
BuildRequires:  python3-pylint-venv >= 2.1.1
BuildRequires:  python3-pyls-spyder >= 0.4.0
BuildRequires:  python3-pytest >= 5.0
BuildRequires:  python3-pytest-lazy-fixture
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-order
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-python-lsp-black >= 1.2.0
BuildRequires:  python3-pyxdg >= 0.26
BuildRequires:  python3-pyzmq >= 22.1.0
BuildRequires:  python3-qstylizer >= 0.2.2
BuildRequires:  python3-qt5
BuildRequires:  python3-qtwebengine-qt5
BuildRequires:  python3-rope >= 0.10.5
BuildRequires:  python3-scipy
BuildRequires:  python3-sympy >= 0.7.3
BuildRequires:  python3-textdistance >= 4.2.0
BuildRequires:  python3-three-merge >= 0.1.1
BuildRequires:  python3-watchdog
BuildRequires:  python3-whatthepatch
BuildRequires:  python3-yapf
BuildRequires:  xdpyinfo
BuildRequires:  xvfb-run
BuildRequires:  (python3-QDarkStyle >= 3.0.2 with python3-QDarkStyle < 3.1.0)
BuildRequires:  (python3-pylint >= 2.5.0 with python3-pylint < 3)
BuildRequires:  (python3-python-lsp-server >= 1.7 with python3-python-lsp-server < 1.8)
BuildRequires:  (python3-qtconsole >= 5.4 with python3-qtconsole < 5.5)
BuildRequires:  (python3-spyder-kernels >= 2.4.1 with python3-spyder-kernels < 2.5)
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

%package dicom
Summary:        DICOM I/O plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python3-pydicom
Provides:       spyder3-dicom = %{version}
Obsoletes:      spyder3-dicom < %{version}

%description dicom
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to read and write
DICOM files.

%package hdf5
Summary:        HDF5 I/O plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python3-h5py
Provides:       spyder3-hdf5 = %{version}
Obsoletes:      spyder3-hdf5 < %{version}

%description hdf5
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to read and write
HDF5 files.

%package doc
Summary:        Documentation for the Spyder IDE
Group:          Development/Languages/Python
Recommends:     %{name} = %{version}
Provides:       spyder3-doc = %{version}
Obsoletes:      spyder3-doc < %{version}

%description doc
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

Documentation and help files for Spyder and its plugins.

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
sed -i -e '/^#!\//, 1d' spyder/utils/external/github.py

sed -i -e '1 {s:/usr/bin/env bash.*:%{_bindir}/bash:}' spyder/plugins/ipythonconsole/scripts/conda-activate.sh

chmod -x spyder/images/*/*.svg

# macOS specific script
rm spyder/utils/check-git.sh
# windows script
rm spyder/plugins/ipythonconsole/scripts/conda-activate.bat

# remove egg package pins read at runtime startup and for the test suite dependency sync checks
sed -r \
    -e 's/(pyqt.*)<5.16/\1/' \
    -i setup.py requirements/main.yml binder/environment.yml

# Upstream brings its fixed versions for pyls, qdarksstyle and spyder-kernels for its
# test environment, but we want to test against installed packages.
rm -r external-deps/*

%build
%python3_build

%install
%python3_install

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

%suse_update_desktop_file -r spyder Development Science IDE NumericalAnalysis
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
# - Test marked with (* tested live) are skipped after making sure the tested
#   functionality still works in a real desktop environment

# requires internet connection
donttest+=" or test_github_backend"
%if 0%{?suse_version} == 1500
# fails on Leap
donttest+=" or (test_objectexplorer_collection_types and params0)"
%endif
# different PyQT version?
donttest+=" or (test_objectexplorer_collection_types and params5)"
# qtbot timeouts or too slow in OBS
donttest+=" or test_run_python_script_in_terminal"
# we are not on conda env
donttest+=" or test_status_bar_conda_interpreter_status"
# "Only for CIs", but we are not on conda/pyenv as upstream's CI
donttest+=" or test_conda"
donttest+=" or test_is_valid_interpreter"
donttest+=" or test_pyenv"
# too flaky for OBS
donttest+=" or test_update_decorations_when_scrolling"
# occational fail
donttest+=" or test_bracket_closing_new_line"
# flaky
donttest+=" or (test_ipythonconsole and test_pdb_multiline)"
donttest+=" or (test_ipythonconsole and test_auto_backend)"
# These tests are testing against buggy behavior in Qt 5.12. We have newer Qt in Tumbleweed.
# https://github.com/spyder-ide/spyder/issues/12663
donttest+=" or (test_codeeditor and test_editor_backspace_char)"
donttest+=" or (test_codeeditor and test_editor_backspace_selection)"
donttest+=" or (test_codeeditor and test_editor_delete_char)"
donttest+=" or (test_codeeditor and test_qtbug35861)"
donttest+=" or (test_shortcuts and test_select_all_shortcut)"
# (* tested live) segfault (QtAwesome?)
donttest+=" or test_apps_dialog"
# no venvs to load in our test environment
donttest+=" or test_load_time"
# no online help within qtbot timeout
donttest+=" or test_get_pydoc or test_pydocbrowser"
# segfault in openSUSE:Factory (?)
donttest+=" or  test_goto_uri_project_root_path"
# completes to math.hypot(cooordinates) instead of expected math.hypot(*coordinates)
donttest+=" or (test_introspection and test_completions)"
# test_update.py would require network connections
donttest+=" or (test_update and not test_no_update)"
# runs into timeout on obs
donttest+=" or (test_editor_and_outline and test_empty_file)"
donttest+=" or test_class_func_selector"
donttest+=" or test_console_working_directory"
# tries to download stuff
donttest+=" or test_kite_install"
# qtbot timeout
donttest+=" or test_get_hints"
# occasional segfaults. fails to get the root tree otherwise (LSP problem?)
donttest+=" or test_editor_outlineexplorer"
# too flaky on some platforms
donttest+=" or test_hide_widget_completion"
# ultimate rationale: skip whole mainwindow as these tests are leaking file descriptors
# https://github.com/spyder-ide/spyder/issues/13483
donttest+=" or test_mainwindow"
# no config for appearance.css_path without mainwindow
donttest+=" or test_ipython_config_dialog"
# fails on server but not locally
donttest+=" or (test_formatting and document and autopep8)"
# flaky
donttest+=" or (test_pdb_eventloop and qt5)"
# Test is not independent: QThread *sometimes* misses the CONF_SECTION
donttest+=" or test_handle_exception"

donttest+=" or known_leak"

# segfault in obs, successful in live system
donttest+=" or test_module_completion"

# cannot start spyder kernel
donttest+=" or test_kernel_crash"

export donttest
# Can't use pytest-xvfb because the tests leave widgets open and trigger https://github.com/The-Compiler/pytest-xvfb/issues/11
# create test script so that we can use one Xvfb with both test suites:
echo '
#!/bin/bash
set -e
testcmd=(python3 runtests.py -m "not no_xvfb" --timeout 1800 -ra -k "not (${donttest:4})")
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
%{python3_sitelib}/spyder-%{version}*-info
%exclude %{python3_sitelib}/spyder/locale/
%exclude %{python3_sitelib}/spyder/plugins/io_dcm/
%exclude %{python3_sitelib}/spyder/plugins/io_hdf5/
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

%files dicom
%license LICENSE.txt
%{python3_sitelib}/spyder/plugins/io_dcm/

%files hdf5
%license LICENSE.txt
%{python3_sitelib}/spyder/plugins/io_hdf5/

%files lang -f %{name}.lang
%license LICENSE.txt
%dir %{python3_sitelib}/spyder/locale/
%dir %{python3_sitelib}/spyder/locale/*
%dir %{python3_sitelib}/spyder/locale/*/LC_MESSAGES

%changelog
