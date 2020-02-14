#
# spec file for package spyder3
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
%define         X_display         ":98"
Name:           spyder3
Version:        4.0.1
Release:        0
URL:            https://www.spyder-ide.org/
Summary:        The Scientific Python Development Environment
License:        MIT
Source:         https://github.com/spyder-ide/spyder/archive/v%{version}.tar.gz#/spyder-%{version}.tar.gz
Source1:        spyder3-rpmlintrc
Patch0:         0001-fix-hanging-test-when-not-in-git-repository.patch
Patch1:         0001-only-test-for-git-when-in-git.patch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Pygments >= 2.0
BuildRequires:  python3-QDarkStyle >= 2.7
BuildRequires:  python3-QtAwesome >= 0.5.7
BuildRequires:  python3-QtPy >= 1.5.0
BuildRequires:  python3-Sphinx >= 0.6.0
BuildRequires:  python3-atomicwrites
BuildRequires:  python3-chardet >= 2.0.0
BuildRequires:  python3-devel
BuildRequires:  python3-intervaltree
BuildRequires:  python3-jedi >= 0.9.0
BuildRequires:  python3-nbconvert
BuildRequires:  python3-numpydoc
BuildRequires:  python3-pexpect
BuildRequires:  python3-pickleshare
BuildRequires:  python3-psutil
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-pyflakes
BuildRequires:  python3-pygments >= 2.0
BuildRequires:  python3-pylint
BuildRequires:  python3-python-language-server >= 0.31.2
BuildRequires:  python3-pyxdg >= 0.26
BuildRequires:  python3-pyzmq
BuildRequires:  python3-qt5 >= 5.5
BuildRequires:  python3-qtconsole >= 4.6.0
BuildRequires:  python3-rope >= 0.10.5
BuildRequires:  python3-setuptools
BuildRequires:  python3-watchdog
BuildRequires:  update-desktop-files
%if %{with test}
BuildRequires:  git-core
BuildRequires:  python3-Cython
BuildRequires:  python3-Pillow
BuildRequires:  python3-diff-match-patch
BuildRequires:  python3-flaky
BuildRequires:  python3-keyring
BuildRequires:  python3-matplotlib
BuildRequires:  python3-matplotlib-qt5
BuildRequires:  python3-matplotlib-tk
BuildRequires:  python3-opengl
BuildRequires:  python3-pandas
BuildRequires:  python3-pytest < 5
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-lazy-fixture
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-scipy
BuildRequires:  python3-spyder-kernels >= 1.8.1
BuildRequires:  python3-sympy
BuildRequires:  xvfb-run
%endif
Requires:       python3-Pygments >= 2.0
Requires:       python3-QDarkStyle >= 2.7
Requires:       python3-QtAwesome >= 0.5.7
Requires:       python3-QtPy >= 1.5.0
Requires:       python3-Sphinx >= 0.6.0
Requires:       python3-atomicwrites
Requires:       python3-chardet >= 2.0.0
Requires:       python3-cloudpickle
Requires:       python3-diff-match-patch
Requires:       python3-intervaltree
Requires:       python3-jedi >= 0.9.0
Requires:       python3-keyring
Requires:       python3-nbconvert
Requires:       python3-numpydoc
Requires:       python3-opengl
Requires:       python3-pexpect
Requires:       python3-pickleshare
Requires:       python3-psutil
Requires:       python3-pycodestyle
Requires:       python3-pyflakes
Requires:       python3-pygments >= 2.0
Requires:       python3-pylint
Requires:       python3-python-language-server >= 0.31.2
Requires:       python3-pyxdg >= 0.26
Requires:       python3-pyzmq
Requires:       python3-qt5 >= 5.2
Requires:       python3-qtconsole >= 4.6.0
Requires:       python3-qtwebengine-qt5
Requires:       python3-rope >= 0.10.5
Requires:       python3-spyder-kernels >= 1.8.1
Requires:       python3-watchdog
Recommends:     python3-Pillow
Recommends:     python3-matplotlib >= 1.0
Recommends:     python3-numpy
Recommends:     python3-pandas >= 0.13.1
Recommends:     python3-scipy
Recommends:     python3-sympy >= 0.7.3
Recommends:     %{name}-breakpoints
Recommends:     %{name}-dicom
Recommends:     %{name}-hdf5
Recommends:     %{name}-profiler
Recommends:     %{name}-pylint
Provides:       python3-spyder = %{version}
Provides:       python3-spyderlib = %{version}
Obsoletes:      python3-spyderlib < %{version}
BuildArch:      noarch

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

%package breakpoints
Summary:        Breakpoint plugin for the Spyder IDE
Requires:       %{name} = %{version}

%description breakpoints
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%package dicom
Summary:        DICOM I/O plugin for the Spyder IDE
Requires:       %{name} = %{version}
Requires:       python3-pydicom

%description dicom
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to read and write
DICOM files.

%package hdf5
Summary:        HDF5 I/O plugin for the Spyder IDE
Requires:       %{name} = %{version}
Requires:       python3-h5py

%description hdf5
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to read and write
HDF5 files.

%package profiler
Summary:        Profiler plugin for the Spyder IDE
Requires:       %{name} = %{version}

%description profiler
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to profile
Python code.

%package pylint
Summary:        Pylint plugin for the Spyder IDE
Requires:       %{name} = %{version}
Requires:       python3-pylint

%description pylint
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to provide
inline pylint code analysis and warnings.

%package doc
Summary:        Documentation for the Spyder IDE
Recommends:     %{name} = %{version}

%description doc
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

Documentation and help files for Spyder and its plugins.

%lang_package

%prep
%setup -q -n spyder-%{version}
# Fix wrong-file-end-of-line-encoding RPMLint warning
sed -i 's/\r$//' spyder/app/restart.py
sed -i 's/\r$//' LICENSE.txt CHANGELOG.md
# Fix non-executable-script RPMLint warning
sed -i -e '/^#!\//, 1d' spyder/app/restart.py
sed -i -e '/^#!\//, 1d' spyder/utils/external/github.py
%patch0 -p1
%patch1 -p1

%build
%python3_build

%install
%python3_install

# remove windows stuff
rm %{buildroot}%{_bindir}/spyder_win_post_install.py

# install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ln -s %{python3_sitelib}/spyder/images/spyder.svg %{name}.svg
popd
pushd %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
ln -s %{_datadir}/icons/%{name}.png %{name}.png
popd

# get the language files
%find_lang spyder %{name}.lang

%suse_update_desktop_file -r %{name} Development Science IDE NumericalAnalysis
%fdupes %{buildroot}%{python3_sitelib}

# Deduplicating files can generate a RPMLINT warning for pyc mtime
python3    -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/plugins/tests/
python3 -O -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/plugins/tests/
python3    -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/utils/*/tests/
python3 -O -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/utils/*/tests/
python3    -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/widgets/*/tests/
python3 -O -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/widgets/*/tests/
python3    -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/widgets/tests/
python3 -O -m compileall -d %{python3_sitelib} %{buildroot}%{python3_sitelib}/spyder/widgets/tests/

%fdupes %{buildroot}%{python3_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
# require Internet
skiptests="test_github_backend or test_update" 
# times out on armv7l, and is skipped on upstream CI
# with reason "It makes other tests to segfault in our CIs"
skiptests="$skiptests or test_introspection"   
# segfaults on obs (?)
skiptests="$skiptests or test_arrayeditor_edit_complex_array"
# this test runs into timeouts and is skipped on some of the
# upstream CIs for the same reason
skiptests="$skiptests or test_mpl_backend_change"
# tests not suitable for CIs or OBS as evident from the last assert which fails here
skiptests="$skiptests or test_connection_dialog_remembers_input_with_ssh_passphrase"
skiptests="$skiptests or test_connection_dialog_remembers_input_with_password"

xvfb-run -a python3 -B -m pytest -vvvv spyder -k "not ($skiptests)"
%endif

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/spyder/
%{python3_sitelib}/spyder-%{version}-py*.egg-info
%exclude %{python3_sitelib}/spyder/locale/
%exclude %{python3_sitelib}/spyder/plugins/breakpoints/
%exclude %{python3_sitelib}/spyder/plugins/io_dcm/
%exclude %{python3_sitelib}/spyder/plugins/io_hdf5/
%exclude %{python3_sitelib}/spyder/plugins/profiler/
%exclude %{python3_sitelib}/spyder/plugins/pylint/
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/%{name}.png
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml

%files breakpoints
%license LICENSE.txt
%{python3_sitelib}/spyder/plugins/breakpoints/

%files dicom
%license LICENSE.txt
%{python3_sitelib}/spyder/plugins/io_dcm/

%files hdf5
%license LICENSE.txt
%{python3_sitelib}/spyder/plugins/io_hdf5/

%files profiler
%license LICENSE.txt
%{python3_sitelib}/spyder/plugins/profiler/

%files pylint
%license LICENSE.txt
%{python3_sitelib}/spyder/plugins/pylint/

%files lang -f %{name}.lang
%license LICENSE.txt
%{python3_sitelib}/spyder/locale/

%changelog
