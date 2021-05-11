#
# spec file for package python-asttokens
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2019-2020 Malcolm J Lewis <malcolmlewis@opensuse.org>
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
Name:           python-asttokens
Version:        2.0.4
Release:        0
Summary:        Annotate AST trees with source code positions
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/gristlabs/asttokens
Source:         https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz
Patch0:         py39.patch
BuildRequires:  %{python_module astroid}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
## Manual Begin
Requires:       python-six
## Manual End
BuildArch:      noarch
%python_subpackages

%description
Annotate AST trees with source code positions

%prep
%setup -q -n asttokens-%{version}
%autopatch -p1

%build
export LC_ALL=en_US.utf8
%python_build

%install
export LC_ALL=en_US.utf8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
