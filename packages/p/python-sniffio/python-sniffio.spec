#
# spec file for package python-sniffio
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


%{?sle15_python_module_pythons}
%define skip_python2 1
Name:           python-sniffio
Version:        1.3.0
Release:        0
Summary:        Module to sniff which async library code runs under
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/sniffio
Source:         https://github.com/python-trio/sniffio/archive/v%{version}.tar.gz#/sniffio-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210127.3a18043
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This is a package for detecting which async library code is running
under. It supports multiple async I/O packages, like Trio, and
asyncio.

%prep
%setup -q -n sniffio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_curio'

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/sniffio
%{python_sitelib}/sniffio-%{version}*-info

%changelog
