#
# spec file for package spyder
#
# Copyright (c) 2020 SUSE LLC
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


%ifarch x86_64 aarch64 ppc64le %{arm} %{ix86} %{ppc}
%bcond_without  test
%else
%bcond_with     test
%endif
%define skip_python2 1
Name:           spyder
Version:        4.1.2
Release:        0
Summary:        The Scientific Python Development Environment
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.spyder-ide.org/
Source:         https://github.com/spyder-ide/spyder/archive/v%{version}.tar.gz#/spyder-%{version}.tar.gz
Source1:        spyder-rpmlintrc
Patch0:         spyder-pr11704-fixpytestargs.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Pygments >= 2.0
BuildRequires:  python3-QDarkStyle >= 2.8
BuildRequires:  python3-QtAwesome >= 0.5.7
BuildRequires:  python3-QtPy >= 1.5.0
BuildRequires:  python3-Sphinx >= 0.6.0
BuildRequires:  python3-atomicwrites >= 1.2.0
BuildRequires:  python3-chardet >= 2.0.0
BuildRequires:  python3-devel
BuildRequires:  python3-intervaltree
BuildRequires:  python3-jedi >= 0.15.2
BuildRequires:  python3-nbconvert >= 4.0
BuildRequires:  python3-numpydoc >= 0.6.0
BuildRequires:  python3-pexpect >= 4.4.0
BuildRequires:  python3-pickleshare >= 0.4
BuildRequires:  python3-psutil >= 5.3
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-pyflakes
BuildRequires:  python3-pygments >= 2.0
BuildRequires:  python3-pylint >= 0.25
BuildRequires:  python3-python-language-server >= 0.31.9
BuildRequires:  python3-pyxdg >= 0.26
BuildRequires:  python3-pyzmq >= 17
BuildRequires:  python3-qt5 >= 5.5
BuildRequires:  python3-qtconsole >= 4.6.0
BuildRequires:  python3-rope >= 0.10.5
BuildRequires:  python3-setuptools
BuildRequires:  python3-watchdog
BuildRequires:  update-desktop-files
Requires:       %{name}-lang
Requires:       python3-Pygments >= 2.0
Requires:       python3-QDarkStyle >= 2.8
Requires:       python3-QtAwesome >= 0.5.7
Requires:       python3-QtPy >= 1.5.0
Requires:       python3-Sphinx >= 0.6.0
Requires:       python3-atomicwrites >= 1.2.0
Requires:       python3-chardet >= 2.0.0
Requires:       python3-cloudpickle >= 0.5.0
Requires:       python3-diff-match-patch >= 20181111
Requires:       python3-intervaltree
Requires:       python3-jedi >= 0.15.2
Requires:       python3-keyring
Requires:       python3-nbconvert >= 4.0
Requires:       python3-numpydoc >= 0.6.0
Requires:       python3-opengl
Requires:       python3-parso >= 0.5.2
Requires:       python3-pexpect >= 0.4.4
Requires:       python3-pickleshare
Requires:       python3-psutil >= 5.3
Requires:       python3-pycodestyle
Requires:       python3-pyflakes
Requires:       python3-pygments >= 2.0
Requires:       python3-pylint >= 0.25
Requires:       python3-python-language-server >= 0.31.9
Requires:       python3-pyxdg >= 0.26
Requires:       python3-pyzmq >= 17
Requires:       python3-qt5 >= 5.2
Requires:       python3-qtconsole >= 4.6.0
Requires:       python3-qtwebengine-qt5
Requires:       python3-rope >= 0.10.5
Requires:       python3-spyder-kernels >= 1.9
Requires:       python3-watchdog
Recommends:     %{name}-dicom
Recommends:     %{name}-hdf5
Recommends:     %{name}-line-profiler
Recommends:     %{name}-memory-profiler
Recommends:     %{name}-notebook
Recommends:     %{name}-terminal
Recommends:     %{name}-unittest
Recommends:     python3-Pillow
Recommends:     python3-matplotlib >= 2.0.0
Recommends:     python3-numpy >= 1.7
Recommends:     python3-pandas >= 0.13.1
Recommends:     python3-scipy >= 0.17.0
Recommends:     python3-sympy >= 0.7.3
Provides:       python3-spyder = %{version}
Provides:       python3-spyderlib = %{version}
Provides:       spyder3 = %{version}
Provides:       spyder3-breakpoints = %{version}
Provides:       spyder3-profiler = %{version}
Provides:       spyder3-pylint = %{version}
Obsoletes:      python3-spyderlib < %{version}
Obsoletes:      spyder3 < %{version}
Obsoletes:      spyder3-breakpoints < %{version}
Obsoletes:      spyder3-profiler < %{version}
Obsoletes:      spyder3-pylint < %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  git-core
BuildRequires:  python3-Cython >= 0.21
BuildRequires:  python3-Pillow
BuildRequires:  python3-autopep8
BuildRequires:  python3-diff-match-patch
BuildRequires:  python3-flaky
BuildRequires:  python3-keyring
BuildRequires:  python3-matplotlib >= 2.0.0
BuildRequires:  python3-matplotlib-qt5
BuildRequires:  python3-matplotlib-tk
BuildRequires:  python3-opengl
BuildRequires:  python3-pandas >= 0.13.1
BuildRequires:  python3-pyaml
BuildRequires:  python3-pydocstyle
BuildRequires:  python3-pytest < 5
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-faulthandler < 2.0
BuildRequires:  python3-pytest-lazy-fixture
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-ordering
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-scipy
BuildRequires:  python3-spyder-kernels >= 1.9
BuildRequires:  python3-sympy >= 0.7.3
BuildRequires:  python3-xarray
BuildRequires:  xdpyinfo
%endif

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

# expansion of lang_package because the macro does not handle the rename
%package lang
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
%setup -q -n spyder-%{version}
%patch0 -p1
# Fix wrong-file-end-of-line-encoding RPMLint warning
sed -i 's/\r$//' spyder/app/restart.py
sed -i 's/\r$//' LICENSE.txt CHANGELOG.md
# Fix non-executable-script RPMLint warning
sed -i -e '/^#!\//, 1d' spyder/app/restart.py
sed -i -e '/^#!\//, 1d' spyder/utils/external/github.py
sed -i -e '/^#!\//, 1d' spyder/plugins/ipythonconsole/scripts/conda-activate.sh 
# remove pinned dependencies where OpenSUSE already has newer versions
# that triggers an annoying warning on startup
# gh#spyder-ide/spyder#11975
sed -i "s|JEDI_REQVER = '=|JEDI_REQVER = '>=|" spyder/dependencies.py
# parso was pinned because of JEDI (PR#11476 and PR#11809)
sed -i "s|PARSO_REQVER = '=|PARSO_REQVER = '>=|" spyder/dependencies.py

%build
%python_build

%install
%python_install

# remove windows stuff
rm %{buildroot}%{_bindir}/spyder_win_post_install.py

# install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ln -s %{python_sitelib}/spyder/images/spyder.svg spyder3.svg
popd
pushd %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
ln -s %{_datadir}/icons/spyder3.png spyder3.png
popd

# get the language files
%find_lang spyder %{name}.lang
# remove source language files
find %{buildroot}%{python_sitelib}/spyder/locale -name '*.po' -delete
find %{buildroot}%{python_sitelib}/spyder/locale -name '*.pot' -delete

%suse_update_desktop_file -r spyder3 Development Science IDE NumericalAnalysis
%fdupes %{buildroot}%{python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1

# upstream splits the tests into slow and fast ones
# we run the ipythonconsole tests separately because they pose issues with asynchonously opened sockets
skiptests="test_ipythonconsole"
skipslowtests="test_ipythonconsole"

# add all tests to skip into $skiptests or $skipttestsslow separated by whitespace
# the shortcut is not sent by the editorbot
skiptests+=" test_comment"
# the click/tab press is not sent by the bot
skiptests+=" test_tab_copies_find_to_replace"
# tests that require internet connection
skiptests+=" test_github_backend test_update"
# we modified the dependencies in %%prep, this is a pure developer test
skiptests+=" test_dependencies_for_spyder_dialog_in_sync"
# segfaults in xvfb
skiptests+=" test_arrayeditor_edit_complex_array"
# tests not suitable for CIs or OBS as evident from the last assert which fails here
skiptests+=" test_connection_dialog_remembers_input_with_ssh_passphrase"
skiptests+=" test_connection_dialog_remembers_input_with_password"
# completes to math.hypot(cooordinates) instead of expected math.hypot(*coordinates)
skipslowtests+=" test_completions"

# the linter does not report warnings with the D and E error codes
skipslowtests+=" test_ignore_warnings test_move_warnings test_get_warnings test_update_warnings"
# opens too many files ?
# likely a test before....
skipslowtests+=" test_open_notebooks_from_project_explorer"

# the following tests rely on IPythonConsole behaving well on OBS (which does not..)
skipipythontests=""
skipipythonslowtests=""
# xvfb does not like the repeating restart of the kernels in those tests
skipipythontests+=" test_load_kernel_file"
# running into timeouts
skipipythontests+=" test_mpl_backend_change"
skipipythontests+=" test_calltip"
skipipythontests+=" test_dbg_input"
# pdb seems to be the root cause of a lot of test problems
skipipythontests+=" test_pdb"
# timeout, hard abort, permission errors
skipipythontests+=" test_stderr_"
skipipythontests+=" test_kernel_kill test_conda_env_activation"
# segfault (?)
skipipythonslowtests+=" test_runfile_from_project_explorer"

%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}
for s in tests slowtests ipythontests ipythonslowtests; do
    skips=skip$s
    declare skip${s}_p="$($python -c "import sys; print(' or '.join('${!skips}'.split()))")"
done
$python runtests.py -k "not ($skiptests_p)"
# the slow tests still segfault unreproducibly at different tests. Something does not clean up
# $python runtests.py --run-slow -k "not ($skipslowtests_p)"
$python runtests.py -k "test_ipythonconsole and not ($skipipythontests_p)"
# the slow tests still fail unreproducibly at different tests. Something does not clean up
# $python runtests.py --run-slow -k "test_ipythonconsole and not ($skipipythonslowtests_p)"
}
%endif

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/spyder3
%{_datadir}/applications/spyder3.desktop
%{python_sitelib}/spyder/
%{python_sitelib}/spyder-%{version}-py*.egg-info
%exclude %{python_sitelib}/spyder/locale/
%exclude %{python_sitelib}/spyder/plugins/io_dcm/
%exclude %{python_sitelib}/spyder/plugins/io_hdf5/
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/spyder3.svg
%{_datadir}/icons/hicolor/128x128/apps/spyder3.png
%{_datadir}/icons/spyder3.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/spyder3.appdata.xml

%files dicom
%license LICENSE.txt
%{python_sitelib}/spyder/plugins/io_dcm/

%files hdf5
%license LICENSE.txt
%{python_sitelib}/spyder/plugins/io_hdf5/

%files lang -f %{name}.lang
%license LICENSE.txt
%dir %{python_sitelib}/spyder/locale/
%dir %{python_sitelib}/spyder/locale/*
%dir %{python_sitelib}/spyder/locale/*/LC_MESSAGES

%changelog
