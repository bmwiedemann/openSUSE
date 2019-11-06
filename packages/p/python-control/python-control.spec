#
# spec file for package python-control
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-control
Version:        0.8.2
Release:        0
Summary:        Python control systems library
License:        BSD-3-Clause
URL:            http://python-control.sourceforge.net
Source:         https://files.pythonhosted.org/packages/source/c/control/control-%{version}.tar.gz
Patch0:         python-control-fixtestaugw.patch
Patch1:         python-control-pr317.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-scipy
Recommends:     python-slycot
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib-qt5}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nose-exclude}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module slycot}
BuildRequires:  libtcmalloc4
BuildRequires:  xvfb-run
# /SECTION
%python_subpackages

%description
The Python Control Systems Library is a Python module that implements basic
operations for analysis and design of feedback control systems.

%prep
%setup -q -n control-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The default Agg backend does not define the toolbar attribute in the Figure
# Manager used by some tests, so we run those tests with the Qt5 backend in a
# virtual X server environment
%if %{_arch} == i386
    export LD_PRELOAD="%{_libdir}/libtcmalloc_minimal.so.4"
%endif
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
export MPLBACKEND="Agg"
nosetests-%$python_bin_suffix \
    --exclude-test control.tests.sisotool_test \
    --exclude-test control.tests.rlocus_test
export MPLBACKEND="Qt5Agg"
export LD_PRELOAD="%{_libdir}/libtcmalloc_minimal.so.4"
xvfb-run -a nosetests-%$python_bin_suffix \
    control.tests.sisotool_test \
    control.tests.rlocus_test
}

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitelib}/control
%{python_sitelib}/control-*-py*.egg-info

%changelog
