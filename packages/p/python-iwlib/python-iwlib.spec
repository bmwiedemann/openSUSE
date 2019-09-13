#
# spec file for package python-iwlib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-iwlib
Version:        1.6.2
Release:        0
Summary:        Python module to interface with iwlib
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/nathan-hoad/python-iwlib
Source:         https://files.pythonhosted.org/packages/source/i/iwlib/iwlib-%{version}.tar.gz
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libiw-devel
BuildRequires:  python-rpm-macros
Requires:       python-cffi
%python_subpackages

%description
Python-iwlib is a package for interfacing with iwlib, providing an implementation to
the wireless tools in Linux.

It provides scanning, setting the ESSID of a device, and getting the current configuration
back from a device.

%prep
%setup -q -n iwlib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Fix for https://github.com/openSUSE/python-rpm-macros/issues/31
PYTHONPATH=FIX-ME
%pytest_arch

%files %{python_files}
%license COPYING
%doc AUTHORS README.rst
%{python_sitearch}/*

%changelog
