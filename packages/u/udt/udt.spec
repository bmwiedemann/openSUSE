#
# spec file for package udt
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global sover 0
%global libname lib%{name}%{sover}
%global devname lib%{name}-devel

Name:           udt
Version:        4.11
Release:        0
Summary:        UDP-based Data Transfer Protocol
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++

Url:            http://udt.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/udt/udt/%{version}/udt.sdk.%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
UDT is a reliable UDP-based application level data transport protocol
for distributed data intensive applications over wide area high-speed
networks. UDT uses UDP to transfer bulk data with its own reliability
control and congestion control mechanisms. The new protocol can
transfer data at a much higher speed than TCP does. UDT is also a
highly configurable framework that can accommodate various congestion
control algorithms.

%package -n %{libname}
Summary:        UDP-based Data Transfer Protocol
Group:          System/Libraries

%description -n %{libname}
UDT is a reliable UDP-based application level data transport protocol
for distributed data intensive applications over wide area high-speed
networks. UDT uses UDP to transfer bulk data with its own reliability
control and congestion control mechanisms. The new protocol can
transfer data at a much higher speed than TCP does. UDT is also a
highly configurable framework that can accommodate various congestion
control algorithms.

This package provides the libraries used by applications to use UDT.

%package -n %{devname}
Summary:        Development files for the UDP-based Data Transfer Protocol library
Group:          Development/Libraries/C and C++
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}


%description -n %{devname}
UDT is a reliable UDP-based application level data transport protocol
for distributed data intensive applications over wide area high-speed
networks. UDT uses UDP to transfer bulk data with its own reliability
control and congestion control mechanisms. The new protocol can
transfer data at a much higher speed than TCP does. UDT is also a
highly configurable framework that can accommodate various congestion
control algorithms.

This package provides the files for developing applications to use UDT.

%prep
%setup -q -n udt4

sed 's!-O3!%{optflags}!' -i src/Makefile app/Makefile
sed 's!-shared!-shared -lpthread -Wl,-soname,libudt.so.0!' \
    -i src/Makefile
sed 's/\r//' -i doc/doc/udtdoc.css

%build
ARCH=
%ifarch %{ix86}
ARCH=IA32
%endif
%ifarch x86_64
ARCH=AMD64
%endif
%ifarch ia64
ARCH=IA64
%endif

# Parallel build fails - no _smp_mflags
make arch=$ARCH

%install
# Manually install the libraries and headers
mkdir -p %{buildroot}%{_libdir}
install src/libudt.so %{buildroot}%{_libdir}/libudt.so.0
ln -s libudt.so.0 %{buildroot}%{_libdir}/libudt.so
mkdir -p %{buildroot}%{_includedir}/udt
install -p -m 644 src/*.h %{buildroot}%{_includedir}/udt

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc RELEASE_NOTES.txt
%license LICENSE.txt
%{_libdir}/libudt.so.%{sover}

%files -n %{devname}
%doc doc
%{_libdir}/libudt.so
%{_includedir}/udt

%changelog
