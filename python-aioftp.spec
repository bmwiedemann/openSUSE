#
# spec file for package python-aioftp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-aioftp
Version:        0.13.0
Release:        0
License:        Apache-2.0
Summary:        FTP client/server for asyncio
Url:            https://github.com/aio-libs/aioftp
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/aioftp/aioftp-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module trustme}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
aioftp is a python FTP client/server based on asyncio.

%prep
%setup -q -n aioftp-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_server_side_throttle'

%files %{python_files}
%doc README.rst
%license license.txt
%{python_sitelib}/*

%changelog
