#
# spec file for package python-ddt
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without python2
Name:           python-ddt
Version:        1.6.0
Release:        0
Summary:        Data-Driven/Decorated Tests
License:        MIT
URL:            https://github.com/txels/ddt
Source:         https://files.pythonhosted.org/packages/source/d/ddt/ddt-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-six.patch gh#datadriventests/ddt#110
Patch0:         remove-six.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
%if %{with python2}
BuildRequires:  python2-enum34
BuildRequires:  python2-mock
%endif
# /SECTION
%python_subpackages

%description
A library to multiply test cases.

%prep
%autosetup -p1 -n ddt-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CONTRIBUTING.md README.md
%license LICENSE.md
%{python_sitelib}/ddt.py
%{python_sitelib}/ddt-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
