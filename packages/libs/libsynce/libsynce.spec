#
# spec file for package libsynce
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} > 1110
%bcond_with hal
%else
%bcond_without hal
%endif

%define major		0

Name:           libsynce
Version:        0.15.1
Release:        1
License:        MIT
Summary:        Core library for the SynCE project
Url:            http://www.synce.org
Group:          System/Libraries
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source0:        %{name}-%{version}.tar.bz2
Patch0:         libsynce-date-undef.patch

BuildRequires:  dbus-1-glib-devel
%if %{with hal}
BuildRequires:  hal-devel
%endif

%description
The purpose of the SynCE project is to provide a means of communication with a Windows Mobile, or Windows CE, device from a computer running Linux, FreeBSD or a similar operating system.

%package -n %{name}%{major}

Summary:        Core library for the SynCE project
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{name}%{major}
The purpose of the SynCE project is to provide a means of communication with a Windows Mobile, or Windows CE, device from a computer running Linux, FreeBSD or a similar operating system.

Libsynce is a common library for various SynCE project tools, containing various utility and helper functions.

%package devel

Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       dbus-1-glib-devel
%if %{with hal}
Requires:       hal-devel
%endif

%description devel
This package contains the header files, static libraries and development documentation for %{name}. If you like to develop programs using %{name}, you will need to install %{name}-devel.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-rpath \
	--disable-static \
%if %{with hal}
	--enable-hal-support
%else
	--disable-hal-support
%endif

make %{?_smp_mflags}

%install
%makeinstall DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.{la,a}

%clean
rm -rf %{buildroot}

%post -n %{name}%{major} -p /sbin/ldconfig

%postun -n %{name}%{major} -p /sbin/ldconfig

%files -n %{name}%{major}
%defattr(-,root,root)
%doc ChangeLog LICENSE README TODO
%{_mandir}/man7/synce.7.gz
%{_libdir}/libsynce.so.0.0.0
%{_libdir}/libsynce.so.0

%files devel
%defattr(-,root,root)
%{_mandir}/man3/*
%{_includedir}/synce_socket.h
%{_includedir}/synce_sys_error.h
%{_includedir}/synce.h
%{_includedir}/synce_log.h
%{_includedir}/synce_hash.h
%{_includedir}/synce_types.h
%{_includedir}/synce_ini.h
%{_includedir}/synce_vector_template.h
%{_libdir}/pkgconfig/libsynce.pc
%{_libdir}/libsynce.so

%changelog
