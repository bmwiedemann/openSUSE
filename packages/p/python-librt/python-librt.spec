#
# spec file for package python-librt
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


Name:           python-librt
Version:        0.7.8
Release:        0
Summary:        Mypyc runtime library
License:        MIT
URL:            https://github.com/mypyc/librt
Source:         https://files.pythonhosted.org/packages/source/l/librt/librt-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module mypy_extensions}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Mypyc runtime library

%prep
%autosetup -p1 -n librt-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python smoke_tests.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/librt
%{python_sitearch}/librt-%{version}.dist-info

%changelog
