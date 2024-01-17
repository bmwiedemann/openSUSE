#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without  test
%define pyname  xkbcommon
Name:           python-%{pyname}
Version:        0.8
Release:        0
Summary:        Python bindings for libxkbcommon using cffi
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/sde1000/python-xkbcommon
Source0:        https://files.pythonhosted.org/packages/source/x/xkbcommon/%{pyname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Patch0:         fix-xkbcommon-paths.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
%python_subpackages

%description
Python bindings for libxkbcommon using cffi

%prep
%setup -q -n %{pyname}-%{version}
#%%patch0 -p1

%build
export CFLAGS="-I/usr/include/libxkbcommon ${CFLAGS}"
%python_exec xkbcommon/ffi_build.py
%python_build

%install
export CFLAGS="%optflags $(pkg-config --cflags xkbcommon)"
%python_install

%{python_expand %fdupes %{buildroot}%{$python_sitearch}}

%if %{with test}
%check
export CFLAGS="%optflags $(pkg-config --cflags xkbcommon)"
export LC_TYPE=en_US.UTF-8
export PYTHONPATH="%{buildroot}%{python3_sitearch}/%{pyname}:${PYTHONPATH}"
export PYTHONDONTWRITEBYTECODE=1
%pytest -vv
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
