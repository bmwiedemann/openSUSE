#
# spec file for package hawknl
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define major_ver 1
%define minor_ver 6
%define patch_ver 8

Name:           hawknl
Version:        %{major_ver}.%{minor_ver}.%{patch_ver}
Release:        0
Url:            http://www.hawksoft.com/hawknl/
Summary:        Game oriented network API
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Source:         HawkNL%{major_ver}%{minor_ver}%{patch_ver}src.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Hawk Network Library is a wrapper over Berkeley/Unix Sockets. NL
provides support for groups of sockets, socket statistics, high
accuracy timer, CRC functions, macros to read and write data to
packets with endian conversion, and support for multiple network
transports.

%package libs
Summary:        Game oriented network API
Group:          System/Libraries

%description libs
The Hawk Network Library is a wrapper over Berkeley/Unix Sockets. NL
provides support for groups of sockets, socket statistics, high
accuracy timer, CRC functions, macros to read and write data to
packets with endian conversion, and support for multiple network
transports.

%package devel
Summary:        Development files for the Hawk Network Library
Group:          Development/Libraries/C and C++
Requires:       %{name}-libs = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of hawknl.

%prep
%setup -q -n hawknl%{major_ver}.%{minor_ver}%{patch_ver}

%build
make %{?_smp_mflags} -f makefile.linux OPTFLAGS="%optflags -fno-strict-aliasing -D_GNU_SOURCE -D_REENTRANT"

%install
install -D -m 0644 include/nl.h %{buildroot}/%{_includedir}/nl.h
mkdir -p "%{buildroot}/%{_libdir}"
cp -a src/libNL.so.* "%{buildroot}/%{_libdir}/"
/sbin/ldconfig -Nv "%{buildroot}/%{_libdir}/"
ln -fs NL.so.1.6 "%{buildroot}/%{_libdir}/libNL.so"

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%defattr(-,root,root)
%{_libdir}/*NL.so.*

%files devel
%defattr(-,root,root)
%doc src/nlchanges.txt src/readme.txt
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
