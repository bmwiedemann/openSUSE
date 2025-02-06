#
# spec file for package python-gphoto2
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


Name:           python-gphoto2
Version:        2.5.1
Release:        0
Summary:        Python interface to libgphoto2
License:        LGPL-3.0-or-later
URL:            https://github.com/jim-easterbrook/python-gphoto2
Source0:        https://github.com/jim-easterbrook/python-gphoto2/archive/refs/tags/v%{version}.tar.gz#/gphoto2-%{version}.tar.gz
# PATCH-FIX-OPENSUSE python-gphoto2-do_not_install_data.patch
Patch0:         %{name}-do_not_install_data.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml if %python-setuptools < 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libgphoto2)
%python_subpackages

%description
Python bindings to libgphoto2. The module is built using SWIG to
automatically generate the interface code. This gives direct
access to nearly all of the libgphoto2 functions, although sometimes
in a nonstandard manner.

%prep
%autosetup -p1 -n python-gphoto2-%{version}
# remove unwanted shebang
sed -e '1d' -i examples/*.py

# E: spurious-executable-perm
chmod -x examples/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export IOLIBS=%{_libdir}/libgphoto2_port/$(pkg-config --variable=VERSION libgphoto2_port)
export CAMLIBS=%{_libdir}/libgphoto2/$(pkg-config --variable=VERSION libgphoto2)
# Large portions of the testsuite fail with gphoto2.GPhoto2Error: [-105] Unknown model
%pytest_arch -k 'TestList'

%files %{python_files}
%license LICENSE.txt
%doc README.rst examples
%{python_sitearch}/gphoto2
%{python_sitearch}/gphoto2-%{version}.dist-info

%changelog
