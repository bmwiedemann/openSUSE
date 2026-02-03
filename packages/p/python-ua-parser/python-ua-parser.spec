#
# spec file for package python-ua-parser
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.0.1
Release:        0
Summary:        Python Implementation of UA Parser
License:        Apache-2.0
URL:            https://github.com/ua-parser/uap-python
Source0:        https://files.pythonhosted.org/packages/source/u/ua-parser/ua_parser-%{version}.tar.gz
# Current submodule commit for uap-core, required to build ua-parser-builtins
Source1:        https://github.com/ua-parser/uap-core/archive/d668d6c6157db7737edfc0280adc6610c1b88029.tar.gz#/uap-core.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioningit}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A python implementation of the UA Parser (https://github.com/ua-parser, formerly
https://github.com/tobie/ua-parser)

%prep
%autosetup -n ua_parser-%{version}
mkdir uap-core
tar zx --strip-components=1 -C uap-core -f %{SOURCE1}
echo "Version: %{version}" > uap-core/PKG-INFO
pushd ua-parser-builtins
ln -s ../uap-core .
popd

%build
%pyproject_wheel
# Also build the builtins
pushd ua-parser-builtins
%pyproject_wheel
popd

%install
%pyproject_install
pushd ua-parser-builtins
%pyproject_install
popd
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/ua_parser
%{python_sitelib}/ua_parser_builtins
%{python_sitelib}/ua_parser-%{version}.dist-info
%{python_sitelib}/ua_parser_builtins-%{version}.dist-info

%changelog
