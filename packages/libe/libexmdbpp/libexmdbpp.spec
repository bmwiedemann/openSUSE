#
# spec file for package libexmdbpp
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


%{?sle15allpythons}
%define skip_python2 1
%define lname libexmdbpp0
Name:           libexmdbpp
Version:        1.11.0.58baa16
Release:        0
Summary:        A C++ implementation of the exmdb wire protocol
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://grommunio.com/
Source:         %name-%version.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?rhel} || 0%{?fedora_version}
BuildRequires:  pkgconfig(python3)
BuildRequires:  pybind11-devel
BuildRequires:  python3
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
%{?sle15allpythons}
BuildRequires:  python3-rpm-macros
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pybind11-devel}
%define python_subpackage_only 1
%python_subpackages
%endif

%description
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

%package -n %lname
Summary:        A C++ implementation of the exmdb wire protocol
Group:          System/Libraries

%description -n %lname
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

%package -n libexmdbpp-devel
Summary:        Development files for libexmdbpp
Group:          System/Libraries
Requires:       %lname = %version-%release

%description -n libexmdbpp-devel
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

This subpackage contains the header files for the library.

# section for SUSE
%package -n python-pyexmdb
Summary:        Python bindings for libexmdbpp
Group:          Development/Languages/Python
Requires:       %lname = %version-%release

%description -n python-pyexmdb
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

This subpackage contains bindings for Python.

# section for Fedora
%package -n python3-pyexmdb
Summary:        Python bindings for libexmdbpp
Group:          Development/Languages/Python
Requires:       %lname = %version-%release

%description -n python3-pyexmdb
The library provides a C++ API and implementation for constructing
exmdb protocol requests and responses and conversing with a server.

This subpackage contains bindings for Python.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
base="$PWD"
%{python_expand #
%define __builddir b%$python_bin_suffix
%cmake -DPython3_EXECUTABLE=%{_bindir}/python%$python_bin_suffix
%cmake_build
cd "$base"
}
%else
%cmake
%cmake_build
%endif

%install
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
base="$PWD"
%{python_expand #
%define __builddir b%$python_bin_suffix
%cmake_install
cd "$base"
}
%else
%cmake_install
# Stop check-rpaths from complaining about standard runpaths (fedora).
export QA_RPATHS=0x0001
%endif

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libexmdbpp.so.0
%license LICENSE.txt

%files -n libexmdbpp-devel
%_includedir/exmdbpp/
%_libdir/libexmdbpp.so
%_datadir/exmdbpp/

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
%files %{python_files pyexmdb}
%python_sitearch/*
%else
%files -n python3-pyexmdb
%python3_sitearch/*
%endif

%changelog
