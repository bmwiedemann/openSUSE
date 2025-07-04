#
# spec file for package python-ua-parser
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
Name:           python-ua-parser
Version:        0.18.0
Release:        0
Summary:        Python Implementation of UA Parser
License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
Source:         https://files.pythonhosted.org/packages/source/u/ua-parser/ua-parser-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A python implementation of the UA Parser (https://github.com/ua-parser, formerly
https://github.com/tobie/ua-parser)

%prep
%setup -q -n ua-parser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
# Tests lack fixtures in the released tarball
#%%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" $python ua_parser/user_agent_parser_test.py

%files %{python_files}
%{python_sitelib}/ua_parser
%{python_sitelib}/ua_parser-%{version}.dist-info

%changelog
