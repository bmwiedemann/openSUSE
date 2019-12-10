#
# spec file for package python-dtaidistance
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
%define         skip_python2 1
Name:           python-dtaidistance
Version:        1.2.3
Release:        0
Summary:        Dynamic Time Warping (DTW) package
License:        Apache-2.0
URL:            https://github.com/wannesm/dtaidistance
Source:         https://github.com/wannesm/dtaidistance/archive/v%{version}.tar.gz#/dtaidistance-%{version}.tar.gz
Source10:       https://kdd.ics.uci.edu/databases/synthetic_control/synthetic_control.data
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Recommends:     python-scipy
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Library for time series distances (e.g. Dynamic Time Warping, DTW).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
This package contains development files needed to build packages
that use %{name}.

%prep
%setup -q -n dtaidistance-%{version}
mkdir tests/rsrc
cp %{SOURCE10} tests/rsrc

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Test are too slow in x86
%ifnarch %{ix86}
mv dtaidistance dtaidistance_temp
%pytest_arch
mv dtaidistance_temp dtaidistance
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/dtaidistance
%{python_sitearch}/dtaidistance-%{version}-py*.egg-info
%exclude %{python_sitearch}/dtaidistance/dtw_c.c

%files %{python_files devel}
%license LICENSE
%{python_sitearch}/dtaidistance/dtw_c.c

%changelog
