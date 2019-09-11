#
# spec file for package python-pybluez
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pybluez
Version:        0.22
Release:        0
Summary:        A Python Bluetooth wrapper
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
Url:            https://github.com/karulis/pybluez/
Source:         https://github.com/karulis/pybluez/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bluez-devel
BuildRequires:  python-rpm-macros
Obsoletes:      pybluez
Provides:       pybluez
%python_subpackages

%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create
Bluetooth applications.

%prep
%setup -q -n pybluez-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install

%files %{python_files}
%license COPYING
%doc CHANGELOG README
%{python_sitearch}/bluetooth/
%{python_sitearch}/PyBluez-%{version}-py*.egg-info

%changelog
