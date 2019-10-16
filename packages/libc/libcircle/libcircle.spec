#
# spec file for package libcircle
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


Name:           libcircle
Version:        0.2.1~rc1
Release:        0

%define myversion 0.2.1-rc.1
Source:         https://github.com/hpc/libcircle/releases/download/%{myversion}/%{name}-%{myversion}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            http://github.com/hpc/libcircle
Summary:        A library used to distribute workloads
License:        BSD-3-Clause-LBNL
Group:          Development/Libraries/C and C++

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  openmpi-macros-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)

%description
A simple interface for processing workloads using an automatically distributed global queue.

%package -n libcircle2
Summary:        A library used to distribute workloads
Group:          System/Libraries
%openmpi_requires

%description -n libcircle2
A simple interface for processing workloads using an automatically distributed global queue.

%package devel
Summary:        Development headers and libraries for libcircle
Group:          Development/Libraries/C and C++
Requires:       libcircle2 = %{version}-%{release}

%description devel
A simple interface for processing workloads using an automatically distributed global queue.

This package contains development headers and libraries for libcircle

%prep
%setup -n %{name}-%{myversion}
#avoid date in doxygen footer
sed -i '/^HTML_FOOTER/s/=.*/= footer.html/' doc/Doxyfile.in
echo > doc/footer.html

%build
%setup_openmpi
%configure --enable-tests --enable-doxygen --disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r doc/html/* %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_prefix}

%check
%setup_openmpi
# Test timeout expired on OpenSuse build
#make check

%post -n libcircle2 -p /sbin/ldconfig
%postun -n libcircle2 -p /sbin/ldconfig

%files -n libcircle2
%defattr(-,root,root,0755)
%{_libdir}/libcircle.so.*
%license COPYING

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/libcircle.so
%{_libdir}/pkgconfig/libcircle.pc
%{_docdir}/%{name}

%changelog
