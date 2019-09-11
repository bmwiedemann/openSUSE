#
# spec file for package python-sniffio
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
%define skip_python2 1
Name:           python-sniffio
Version:        1.1.0
Release:        0
Summary:        Module to sniff which async library code runs under
License:        MIT OR Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/sniffio
Source:         https://github.com/python-trio/sniffio/archive/v%{version}.tar.gz#/sniffio-%{version}.tar.gz
BuildRequires:  %{python_module contextvars >= 2.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-contextvars >= 2.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module curio}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/*

%changelog
