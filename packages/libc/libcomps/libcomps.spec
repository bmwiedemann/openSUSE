#
# spec file for package libcomps
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021 Neal Gompa <ngompa13@gmail.com>.
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


%define major 0
%define minor 1
%define patch 19
%define libname %{name}%{major}
%define devname %{name}-devel

Name:           libcomps
Version:        %{major}.%{minor}.%{patch}
Release:        0
Summary:        Comps XML file manipulation library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/rpm-software-management/libcomps
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libexpat-devel
BuildRequires:  libxml2-devel
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel

# prevent provides from nonstandard paths:
%define __provides_exclude ^(%{python3_sitearch}/.*\\.so)$

%description
Libcomps is library for structure-like manipulation with content of
comps XML files. Supports read/write XML file, structure(s) modification.

%package -n %{libname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{devname}
Summary:        Development files for the libcomps library
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n %{devname}
This package provides the development files for %{name}.

%package doc
Summary:        Documentation files for libcomps library
Group:          Documentation/HTML
BuildArch:      noarch
BuildRequires:  doxygen

%description doc
Documentation files for libcomps library.

%package -n python-libcomps-doc
Summary:        Documentation files for python bindings libcomps library
Group:          Documentation/HTML
BuildArch:      noarch
BuildRequires:  python3-Sphinx

%description -n python-libcomps-doc
Documentation files for python bindings libcomps library.

%package -n python3-libcomps
Summary:        Python 3 bindings for libcomps library
Group:          Development/Libraries/Python
BuildRequires:  python3-devel
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# There is no more Python 2 subpackage
Obsoletes:      python2-libcomps < 0.1.9

%description -n python3-libcomps
This package provides the Python 3 bindings for libcomps library.

%prep
%autosetup  -p1

%build
%cmake -DPYTHON_DESIRED:STRING=3 ../libcomps/
%make_build
make docs
make pydocs

%check
pushd ./build
make test
popd

%install
pushd ./build
%make_install
popd

mkdir -p %{buildroot}%{_datadir}/doc/libcomps/
cp -a build/docs/libcomps-doc/html %{buildroot}%{_datadir}/doc/libcomps/

mkdir -p %{buildroot}%{_datadir}/doc/python-libcomps/
rm build/src/python/docs/html/.doctrees/environment.pickle
cp -a build/src/python/docs/html %{buildroot}%{_datadir}/doc/python-libcomps/

%python_compileall
%fdupes %{buildroot}%{python3_sitearch}

%fdupes %{buildroot}%{_datadir}/doc/libcomps
%fdupes %{buildroot}%{_datadir}/doc/python-libcomps

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libcomps.so.%{major}
%doc README.md COPYING

%files -n %{devname}
%{_libdir}/libcomps.so
%{_libdir}/pkgconfig/libcomps.pc
%{_includedir}/*

%files doc
%doc %{_datadir}/doc/libcomps

%files -n python-libcomps-doc
%doc %{_datadir}/doc/python-libcomps

%files -n python3-libcomps
%{python3_sitearch}/libcomps/
%{python3_sitearch}/libcomps-*

%changelog
