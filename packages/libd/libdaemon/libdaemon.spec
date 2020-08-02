#
# spec file for package libdaemon
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


Name:           libdaemon
Version:        0.14
Release:        0
Summary:        Lightweight C library That Eases the Writing of UNIX Daemons
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://0pointer.de/lennart/projects/libdaemon
Source:         http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libdaemon is a lightweight C library that eases the writing of UNIX
daemons.

%package -n libdaemon0
Summary:        Lightweight C library That Eases the Writing of UNIX Daemons
License:        LGPL-2.1+
Group:          System/Libraries
Provides:       %{name} = %{version}
#opensuse 10.3
Obsoletes:      %{name} <= 0.12

%description -n libdaemon0
libdaemon is a lightweight C library that eases the writing of UNIX
daemons.

%package devel
Summary:        Lightweight C library That Eases the Writing of UNIX Daemons
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libdaemon0 = %{version}

%description devel
libdaemon is a lightweight C library that eases the writing of UNIX
daemons.

%prep
%setup -q

%build
%configure \
        --disable-static \
	--with-pic \
        --disable-lynx
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/libdaemon.la
# We don't care about the HTML README
rm %{buildroot}%{_datadir}/doc/libdaemon/{README.html,style.css}

%post -n libdaemon0 -p /sbin/ldconfig
%postun -n libdaemon0 -p /sbin/ldconfig

%files -n libdaemon0
%defattr (-,root,root)
%doc LICENSE README
%{_libdir}/libdaemon.so.0*

%files devel
%defattr (-,root,root)
%{_libdir}/libdaemon.so
%{_libdir}/pkgconfig/libdaemon.pc
%dir %{_includedir}/libdaemon
%{_includedir}/libdaemon/*.h

%changelog
