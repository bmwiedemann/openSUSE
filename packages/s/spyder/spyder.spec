#
# spec file for package spyder
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with     test
%define         X_display         ":98"
Name:           spyder
Version:        3.3.4
Release:        0
Url:            https://www.spyder-ide.org/
Summary:        The Scientific Python Development Environment
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/spyder/spyder-%{version}.tar.gz
Source1:        spyder-rpmlintrc
# Packaging utility
Source2:        changelog.sh
BuildRequires:  fdupes
BuildRequires:  python-Pygments >= 2.0
BuildRequires:  python-QtAwesome >= 0.5.7
BuildRequires:  python-QtPy >= 1.5.0
BuildRequires:  python-Sphinx >= 0.6.0
BuildRequires:  python-chardet >= 2.0.0
BuildRequires:  python-devel
BuildRequires:  python-jedi >= 0.9.0
BuildRequires:  python-nbconvert
BuildRequires:  python-numpydoc
BuildRequires:  python-pickleshare
BuildRequires:  python-psutil
BuildRequires:  python-pycodestyle
BuildRequires:  python-pyflakes
BuildRequires:  python-pylint
BuildRequires:  python-pyzmq
BuildRequires:  python-qt5 >= 5.5
BuildRequires:  python-qtconsole >= 4.2.0
BuildRequires:  python-rope >= 0.10.5
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
BuildRequires:  update-desktop-files
%if %{with test}
BuildRequires:  python-Cython
BuildRequires:  python-Pillow
BuildRequires:  python-flaky
BuildRequires:  python-keyring
BuildRequires:  python-matplotlib
BuildRequires:  python-mock
BuildRequires:  python-pandas
BuildRequires:  python-pytest
BuildRequires:  python-pytest-cov
BuildRequires:  python-pytest-qt
BuildRequires:  python-pytest-timeout
BuildRequires:  python-pytest-xvfb
BuildRequires:  python-scipy
BuildRequires:  python-spyder-kernels >= 0.4.3
BuildRequires:  python-sympy
BuildRequires:  xauth
BuildRequires:  xorg-x11-server
%endif
Requires:       python-Pygments >= 2.0
Requires:       python-QtAwesome >= 0.5.7
Requires:       python-QtPy >= 1.5.0
Requires:       python-Sphinx >= 0.6.0
Requires:       python-chardet >= 2.0.0
Requires:       python-cloudpickle
Requires:       python-jedi >= 0.9.0
Requires:       python-keyring
Requires:       python-nbconvert
Requires:       python-numpydoc
Requires:       python-pickleshare
Requires:       python-psutil
Requires:       python-pycodestyle
Requires:       python-pyflakes
Requires:       python-pylint
Requires:       python-pyzmq
Requires:       python-qt5 >= 5.2
Requires:       python-qtconsole >= 4.2.0
Requires:       python-rope >= 0.10.5
Requires:       python-spyder-kernels >= 0.4.3
Recommends:     python-Pillow
Recommends:     python-matplotlib >= 1.0
Recommends:     python-numpy
Recommends:     python-pandas >= 0.13.1
Recommends:     python-scipy
Recommends:     python-sympy >= 0.7.3
Recommends:     %{name}-breakpoints
Recommends:     %{name}-dicom
Recommends:     %{name}-hdf5
Recommends:     %{name}-profiler
Recommends:     %{name}-pylint
Provides:       python-spyder
Provides:       python-spyderlib = %{version}
Obsoletes:      python-spyderlib < %{version}
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
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description breakpoints
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to control
breakpoints.

%package dicom
Summary:        DICOM I/O plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-pydicom

%description dicom
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to read and write
DICOM files.

%package hdf5
Summary:        HDF5 I/O plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-h5py

%description hdf5
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to read and write
HDF5 files.

%package profiler
Summary:        Profiler plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description profiler
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to profile
Python code.

%package pylint
Summary:        Pylint plugin for the Spyder IDE
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Requires:       python-pylint

%description pylint
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This package contains the plugin that allows Spyder to provide
inline pylint code analysis and warnings.

%lang_package
%lang_package -n %{name}-breakpoints
%lang_package -n %{name}-profiler
%lang_package -n %{name}-pylint

%prep
%setup -q -n spyder-%{version}
# Fix wrong-file-end-of-line-encoding RPMLint warning
sed -i 's/\r$//' spyder/app/restart.py
sed -i 's/\r$//' LICENSE.txt CHANGELOG.md
# Fix non-executable-script RPMLint warning
sed -i -e '/^#!\//, 1d' spyder/app/restart.py
sed -i -e '/^#!\//, 1d' spyder/utils/external/github.py

%build
%python2_build

%install
%python2_install

# remove windows stuff
rm %{buildroot}%{_bindir}/spyder_win_post_install.py

# install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
pushd %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ln -s %{python2_sitelib}/spyder/images/spyder.svg %{name}.svg
popd
pushd %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
ln -s %{_datadir}/icons/%{name}.png %{name}.png
popd

# get the language files
%find_lang spyder %{name}.lang
%find_lang breakpoints breakpoints.lang
%find_lang profiler profiler.lang
%find_lang pylint pylint.lang

%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{python2_sitelib}

# Deduplicating files can generate a RPMLINT warning for pyc mtime
python2    -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/plugins/tests/
python2 -O -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/plugins/tests/
python2    -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/utils/*/tests/
python2 -O -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/utils/*/tests/
python2    -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/widgets/*/tests/
python2 -O -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/widgets/*/tests/
python2    -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/widgets/tests/
python2 -O -m compileall -d %{python2_sitelib} %{buildroot}%{python2_sitelib}/spyder/widgets/tests/

%fdupes %{buildroot}%{python2_sitelib}

%if %{with test}
%check
export DISPLAY=%{X_display}
export PYTHONDONTWRITEBYTECODE=1
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10
python2 -B -m pytest spyder
%endif

%files
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{python2_sitelib}/spyder/
%{python2_sitelib}/spyder-%{version}-py*.egg-info
%exclude %{python2_sitelib}/spyder/locale/
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/%{name}.png

%files breakpoints
%license LICENSE.txt
%{python2_sitelib}/spyder_breakpoints/
%exclude %{python2_sitelib}/spyder_breakpoints/locale/

%files dicom
%license LICENSE.txt
%{python2_sitelib}/spyder_io_dcm/

%files hdf5
%license LICENSE.txt
%{python2_sitelib}/spyder_io_hdf5/

%files profiler
%license LICENSE.txt
%{python2_sitelib}/spyder_profiler/
%exclude %{python2_sitelib}/spyder_profiler/locale/

%files pylint
%license LICENSE.txt
%{python2_sitelib}/spyder_pylint/
%exclude %{python2_sitelib}/spyder_pylint/locale/

%files lang -f %{name}.lang
%license LICENSE.txt
%{python2_sitelib}/spyder/locale/

%files breakpoints-lang -f breakpoints.lang
%license LICENSE.txt
%{python2_sitelib}/spyder_breakpoints/locale/

%files profiler-lang -f profiler.lang
%license LICENSE.txt
%{python2_sitelib}/spyder_profiler/locale/

%files pylint-lang -f pylint.lang
%license LICENSE.txt
%{python2_sitelib}/spyder_pylint/locale/

%changelog
