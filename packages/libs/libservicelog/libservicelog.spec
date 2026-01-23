#
# spec file for package libservicelog
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname	libservicelog-1_1-1
%if 0%{?suse_version} < 1500
%global system_user_pkg 0
%else
%global system_user_pkg 1
%endif
Name:           libservicelog
Version:        1.1.19
Release:        0
Summary:        Servicelog Database and Library
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/power-ras/libservicelog/
#Git-Clone:	https://github.com/power-ras/libservicelog.git
#Git-Web:	https://github.com/power-ras/libservicelog/
Source0:        https://github.com/power-ras/libservicelog/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        libservicelog-rpmlintrc
Source3:        system-group-service.conf
Patch1:         libservicelog-Fix-timezone-handling-in-servicelog-ev.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  librtas-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
ExclusiveArch:  ppc ppc64 ppc64le
%if %{system_user_pkg}
Requires(pre):  sysuser-tools
%else
Requires(pre):  %{_sbindir}/groupadd
%endif

%description
The libservicelog package contains a library to create and maintain a
database for storing events related to system service. This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the
system.

%package -n %{lname}
Summary:        Servicelog Database and Library
Group:          System/Libraries
Requires:       %{name}

%description -n %{lname}
The libservicelog package contains a library to create and maintain a
database for storing events related to system service. This database
allows for the logging of serviceable and informational events, and for
the logging of service procedures that have been performed upon the
system.

%package        devel
Summary:        Development files for libservicelog
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Requires:       sqlite3-devel

%description    devel
Header files for building with libservicelog.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}
%if %{system_user_pkg}
%sysusers_generate_pre %{SOURCE3} libservicelog system-group-service.conf
%else
cat > libservicelog.pre <<EOF
getent group service >/dev/null || %{_sbindir}/groupadd -r service
EOF
%endif

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if %{system_user_pkg}
install -m 0644 -D -t %{buildroot}%{_sysusersdir}/ %{SOURCE3}
%endif

%pre -f libservicelog.pre

%post    -n %{lname} -p /sbin/ldconfig
%postun  -n %{lname} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%attr( 754, root, service ) %dir %{_localstatedir}/lib/servicelog
%attr( 644, root, service ) %{_localstatedir}/lib/servicelog/servicelog.db
%if %{system_user_pkg}
%{_sysusersdir}/system-group-service.conf
%endif

%files -n %{lname}
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/servicelog-1
%{_libdir}/pkgconfig/servicelog-1.pc
%{_libdir}/*.so

%changelog
