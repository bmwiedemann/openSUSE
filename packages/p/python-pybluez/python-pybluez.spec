#
# spec file for package python-pybluez
#
# Copyright (c) 2022 SUSE LLC
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


%define rev 5096047f90a1f6a74ceb250aef6243e144170f92
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pybluez
Version:        0.23+git%{rev}
Release:        0
Summary:        A Python Bluetooth wrapper
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://pybluez.github.io/
Source:         https://github.com/pybluez/pybluez/archive/%{rev}.tar.gz#/pybluez-%{rev}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bluez-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      pybluez < 0.22
Provides:       pybluez = %{version}
%python_subpackages

%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create
Bluetooth applications.

%prep
%setup -q -n pybluez-%{rev}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

#%%check
# no tests on upstream

%files %{python_files}
%license COPYING
%doc CHANGELOG README.md
%{python_sitearch}/bluetooth/
%{python_sitearch}/PyBluez-*.egg-info

%changelog
