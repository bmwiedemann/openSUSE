#
# spec file for package python-drms
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
Name:           python-drms
Version:        0.5.7
Release:        0
Summary:        Tool to access HMI, AIA and MDI data with Python
License:        MIT
URL:            https://github.com/sunpy/drms
Source:         https://github.com/sunpy/drms/archive/v%{version}.tar.gz#/drms-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.9.0
Requires:       python-pandas >= 0.15.0
Requires:       python-six >= 1.8.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.9.0}
BuildRequires:  %{python_module pandas >= 0.15.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.8.0}
# /SECTION
%python_subpackages

%description
The drms module provides an interface for accessing HMI, AIA and MDI
data with Python. It uses the publicly accessible JSOC DRMS server by
default, but can also be used with local NetDRMS sites.

%prep
%setup -q -n drms-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m drms.tests

%files %{python_files}
%doc AUTHORS.txt README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
