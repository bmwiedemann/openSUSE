#
# spec file for package python-python-sofa
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python36 1
Name:           python-python-sofa
Version:        0.2.0
Release:        0
Summary:        Spatially Oriented Format for Acoustics (SOFA) API for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spatialaudio/python-sofa
# get examples for rudimentary testing from GitHub archive
Source:         %{url}/archive/v%{version}.tar.gz#/python-sofa-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM python-sofa-pr4-scipy1_6.patch gh#spatialaudio/python-sofa#4
Patch0:         https://github.com/spatialaudio/python-sofa/pull/4.patch#/python-sofa-pr4-scipy1_6.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module nbval}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-netCDF4
Requires:       python-numpy
Requires:       python-scipy >= 1.2.0
BuildArch:      noarch

%python_subpackages

%description
A Python API for reading, writing and creating SOFA files as defined
by the SOFA conventions (version 1.0).

%prep
%autosetup -p1 -n python-sofa-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
echo "
[regex1]
regex: DateCreated: .*
replace: DateCreated: 0000-00-00 00:00:00

[regex2]
regex: <module 'sofa' from '.*'
replace: <module 'sofa' from 'somewhere'

" > nbval_sanitize.cfg
%pytest --nbval --sanitize-with nbval_sanitize.cfg doc/examples/SOFA-file-access.ipynb

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
