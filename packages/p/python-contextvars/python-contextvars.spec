#
# spec file for package python-contextvars
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15allpythons}
%define skip_python2 1
Name:           python-contextvars
Version:        2.4
Release:        0
License:        Apache-2.0
Summary:        PEP 567 (context variables) backport
URL:            https://github.com/MagicStack/contextvars
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/c/contextvars/contextvars-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module immutables >= 0.9}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-immutables >= 0.9
BuildArch:      noarch

%python_subpackages

%description
PEP 567 (Context Variables) backport.

%prep
%setup -q -n contextvars-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
