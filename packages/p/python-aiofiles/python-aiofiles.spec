#
# spec file for package python-aiofiles
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-aiofiles
Version:        0.5.0
Release:        0
Summary:        File support for asyncio
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Tinche/aiofiles
Source:         https://github.com/Tinche/aiofiles/archive/v%{version}.tar.gz#/aiofiles-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
aiofiles: file support for asyncio

%prep
%setup -q -n aiofiles-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/aiofiles*

%changelog
