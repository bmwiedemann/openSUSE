#
# spec file for package python-ligo-lw
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


Name:           python-ligo-lw
Version:        1.7.0
Release:        0
Summary:        Python LIGO Light-Weight XML I/O Library
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://git.ligo.org/kipp.cannon/python-ligo-lw
Source:         http://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ligo-lw-segments-test-fix.patch badshah400@gmail.com -- Fix a test that randomly fails due to dictionary ordering being undefined
Patch0:         ligo-lw-segments-test-fix.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-glue
Requires:       python-lal
Requires:       python-ligo-segments
Requires:       python-python-dateutil
Requires:       python-six
Requires:       python-tqdm
# SECTION Test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module glue}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tqdm}
BuildRequires:  diffutils
BuildRequires:  libxml2-tools
BuildRequires:  python3
# /SECTION
%python_subpackages

%description
The LIGO Light-Weight XML format is used extensively by compact object
detection pipeline and associated tool sets.  This package provides a Python
I/O library for reading, writing, and interacting with documents in this
format.

%prep
%setup -q
%patch0 -p1
# Replace distutils.core by setuptools to fix namespace errors
# https://git.ligo.org/kipp.cannon/python-ligo-lw/-/issues/16
sed -i "1{s/distutils.core/setuptools/}" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Tests designed to work only for 64-bits
%ifnarch %ix86
%check
pushd test
# Test-suite works only for python3
export PYTHON=%{__python3}
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PATH+=:%{buildroot}%{_bindir}
%make_build check
popd
%endif

%files %{python_files}
%license LICENSE
%python3_only %{_bindir}/ligolw_*
%{python_sitearch}/*

%changelog
