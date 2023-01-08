#
# spec file for package python-localzone
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-localzone
Version:        0.9.8
Release:        0
Summary:        A library for managing DNS zones
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ags-slc/localzone
# The PyPI sdist does not provide the tests
Source:         https://github.com/ags-slc/localzone/archive/v%{version}.tar.gz#/localzone-%{version}.tar.gz
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dnspython
BuildArch:      noarch
%python_subpackages

%description
A simple library for managing DNS zones.

%prep
%autosetup -p1 -n localzone-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/localzone
%{python_sitelib}/localzone-%{version}*-info

%changelog
