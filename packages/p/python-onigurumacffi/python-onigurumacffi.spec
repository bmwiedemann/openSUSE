#
# spec file for package python-onigurumacffi
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
Name:           python-onigurumacffi
Version:        1.5.0
Release:        0
Summary:        Python cffi bindings for the oniguruma regex engine
License:        MIT
URL:            https://github.com/asottile/onigurumacffi
Source:         https://github.com/asottile/onigurumacffi/archive/refs/tags/v%{version}.tar.gz#/onigurumacffi-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  oniguruma-devel
Requires:       python-cffi >= 1
%python_subpackages

%description
python cffi bindings for the oniguruma regex engine

%prep
%setup -q -n onigurumacffi-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/onigurumacffi.py
%{python_sitearch}/_onigurumacffi.abi3.so
%{python_sitearch}/__pycache__/onigurumacffi*
%{python_sitearch}/onigurumacffi-%{version}.dist-info/

%changelog
