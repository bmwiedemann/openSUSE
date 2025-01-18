#
# spec file for package python-asttokens
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019-2021 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define skip_python2 1
%define skip_python36 1
%{?sle15_python_module_pythons}
Name:           python-asttokens
Version:        3.0.0
Release:        0
Summary:        Annotate AST trees with source code positions
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/gristlabs/asttokens
Source:         https://files.pythonhosted.org/packages/source/a/asttokens/asttokens-%{version}.tar.gz
BuildRequires:  %{python_module astroid}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Annotate AST trees with source code positions

%prep
%autosetup -n asttokens-%{version}

%build
export LC_ALL=en_US.utf8
%python_build

%install
export LC_ALL=en_US.utf8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not TestAstroid'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/asttokens-%{version}-*-info
%{python_sitelib}/asttokens

%changelog
