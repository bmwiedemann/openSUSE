#
# spec file for package python-ua-parser
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define _pkgname ua-parser
Name:           python-ua-parser
Version:        0.8.0
Release:        0
Summary:        Python Implementation of UA Parser
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ua-parser/uap-python
Source:         https://files.pythonhosted.org/packages/source/u/%{_pkgname}/%{_pkgname}-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A python implementation of the UA Parser (https://github.com/ua-parser, formerly
https://github.com/tobie/ua-parser)

%prep
%setup -q -n %{_pkgname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}/%{$python_sitelib}

%check
# Tests lack fixtures in the released tarball
#%%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" $python ua_parser/user_agent_parser_test.py

%files %{python_files}
%{python_sitelib}/*

%changelog
