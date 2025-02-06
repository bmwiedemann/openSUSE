#
# spec file for package python-aioftp
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-aioftp
Version:        0.24.1
Release:        0
Summary:        FTP client/server for asyncio
License:        Apache-2.0
URL:            https://github.com/aio-libs/aioftp
Source:         https://files.pythonhosted.org/packages/source/a/aioftp/aioftp-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-siosocks >= 0.2.0
BuildArch:      noarch
BuildRequires:  %{python_module async_timeout >= 4.0.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module siosocks >= 0.2.0}
BuildRequires:  %{python_module trustme}
%python_subpackages

%description
aioftp is a python FTP client/server based on asyncio.

%prep
%setup -q -n aioftp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license license.txt
%{python_sitelib}/aioftp-%{version}*-info
%{python_sitelib}/aioftp

%changelog
