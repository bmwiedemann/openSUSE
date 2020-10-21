#
# spec file for package python-asciitree
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-asciitree
Version:        0.3.3
Release:        0
Summary:        Python module to draw ASCII trees
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mbr/asciitree
# https://github.com/mbr/asciitree/issues/16 -- no tests on PyPI
Source:         https://github.com/mbr/asciitree/archive/%{version}.tar.gz#/asciitree-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
ASCIItree draws tree structures using characters.

%prep
%setup -q -n asciitree-%{version}
sed -i '1{/env python/ d}' asciitree/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/asciitree
%{python_sitelib}/asciitree-%{version}*info

%changelog
