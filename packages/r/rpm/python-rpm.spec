#
# spec file for package python-rpm
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017 Neal Gompa <ngompa13@gmail.com>.
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


# Enable Python build sourced from rpm spec
%global with_python 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rpm
Version:        4.18.0
Release:        0
Summary:        Python Bindings for Manipulating RPM Packages
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://rpm.org/
#Git-Clone:     https://github.com/rpm-software-management/rpm
BuildRequires:  %{python_module devel}
BuildRequires:  file-devel
BuildRequires:  libacl-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcap-devel
BuildRequires:  libelf-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  ncurses-devel
BuildRequires:  popt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libzstd)
Requires:       rpm = %{version}
%{expand:%(sed -n -e '/^Source:/,/^BuildRoot:/p' <%{_sourcedir}/rpm.spec)}
Source99:       rpm.spec
%if "%{python_flavor}" == "python2"
Obsoletes:      rpm-python < %{version}-%{release}
Provides:       rpm-python = %{version}-%{release}
%endif
%python_subpackages

%description
This package contains a module that permits applications written in
the Python programming language to use the interface supplied by
RPM Package Manager libraries.

This package should be installed if you want to develop Python programs
that will manipulate RPM packages and databases.

%prep
%{expand:%(sed -n -e '/^%%prep/,/^%%install/p' <%{_sourcedir}/rpm.spec | sed -e '1d' -e '$d')}

# The build stage is already declared and pulled in from rpm.spec
pushd python
%python_build
popd

%install
pushd python
%python_install
popd

%files %{python_files}
%{python_sitearch}/rpm*

%changelog
