#
# spec file for package python-cwcwidth
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
Name:           python-cwcwidth
Version:        0.1.12
Release:        0
Summary:        Python bindings for wc(s)width
License:        MIT
URL:            https://github.com/sebastinas/cwcwidth
Source:         https://files.pythonhosted.org/packages/source/c/cwcwidth/cwcwidth-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Python bindings for wc(s)width

%prep
%setup -q -n cwcwidth-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitearch}/cwcwidth
%{python_sitearch}/cwcwidth-%{version}.dist-info

%changelog
