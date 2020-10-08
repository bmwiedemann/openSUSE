#
# spec file for package python-uamqp
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
Name:           python-uamqp
Version:        1.2.11
Release:        0
Summary:        AMQP 10 Client Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-uamqp-python
Source:         https://files.pythonhosted.org/packages/source/u/uamqp/uamqp-%{version}.tar.gz
Patch1:         u_strip-werror.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module certifi >= 2017.4.17}
BuildRequires:  %{python_module six >= 1.0}
# /SECTION
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
Requires:       python-certifi >= 2017.4.17
Requires:       python-six >= 1.0
Suggests:       python-enum34 >= 1.0.4

%python_subpackages

%description
AMQP 1.0 Client Library for Python

%prep
%setup -q -n uamqp-%{version}
%patch1 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
#%%check
#%%python_exec setup.py test

%files %{python_files}
%doc HISTORY.rst README.rst
%{python_sitearch}/*

%changelog
