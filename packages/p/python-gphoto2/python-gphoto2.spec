#
# spec file for package python-gphoto2
#
# Copyright (c) 2020 SUSE LLC
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
Version:        2.2.3
Release:        0
Summary:        Python interface to libgphoto2
License:        GPL-3.0-or-later
URL:            https://github.com/jim-easterbrook/python-gphoto2
Source0:        https://files.pythonhosted.org/packages/source/g/gphoto2/gphoto2-%{version}.tar.gz
# PATCH-FIX-OPENSUSE python-gphoto2-do_not_install_data.patch
Patch0:         %{name}-do_not_install_data.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libgphoto2)
%python_subpackages

%description
Python bindings to libgphoto2. The module is built using SWIG to
automatically generate the interface code. This gives direct
access to nearly all of the libgphoto2 functions, although sometimes
in a nonstandard manner.

%prep
%setup -q -n gphoto2-%{version}
%patch0 -p1
# remove unwanted shebang
sed -e '1d' -i examples/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.txt README.rst examples
%{python_sitearch}/*

%changelog
