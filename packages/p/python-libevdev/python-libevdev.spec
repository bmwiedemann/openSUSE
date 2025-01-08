#
# spec file for package python-libevdev
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
%define skip_python2 1
%global modname libevdev
%define libevdev_reqver 1.6.0
Name:           python-%{modname}
Version:        0.11
Release:        0
Summary:        Python wrapper around the libevdev C library
License:        MIT
Group:          Development/Libraries/Python
URL:            https://python-libevdev.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/l/libevdev/libevdev-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libevdev-devel >= %{libevdev_reqver}
BuildRequires:  python-rpm-macros
%define libmodule %(rpm -q --qf "%%{name}" -f $(readlink -f %{_prefix}/lib*/libevdev.so))
Requires:       %{libmodule} >= %{libevdev_reqver}
BuildArch:      noarch
%python_subpackages

%description
python-libevdev is a wrapper around the libevdev C library, with a
pythonic API.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd test
%pytest

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/libevdev*

%changelog
