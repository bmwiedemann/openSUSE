#
# spec file for package libimobiledevice
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname	6
Name:           libimobiledevice
Version:        1.2.0+git20180427.26373b3
Release:        0
Summary:        Native protocols library for iOS devices
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.libimobiledevice.org
#Source:         http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Source:		%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libplist++-devel >= 1.11
BuildRequires:  libplist-devel >= 1.11
BuildRequires:  libtool
BuildRequires:  libusbmuxd-devel >= 1.0.9
BuildRequires:  pkg-config
BuildRequires:  python-cython
BuildRequires:  python-devel
BuildRequires:  python-plist
BuildRequires:  readline-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libimobiledevice is a software library that talks the protocols to support
iOS devices. It does not depend on any existing libraries from Apple.

%package -n %{name}%{soname}
Summary:        Native protocols library for iOS devices
License:        LGPL-2.1+
Group:          System/Libraries
Requires:       libusbmuxd4 >= 1.0.9
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Provides:       libiphone0 = %{version}
Obsoletes:      libiphone0 < 0.9.6

%description -n %{name}%{soname}
libimobiledevice is a software library that talks the protocols to support
iOS devices. It does not depend on any existing libraries from Apple.

%package devel
Summary:        Development files for %{name}
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}
Requires:       libplist-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n imobiledevice-tools
Summary:        Tools using %{name} for iOS devices
License:        GPL-2.0+ and LGPL-2.1+
Group:          Productivity/Multimedia/Other
Requires:       %{name}%{soname} = %{version}
Provides:       %{name}-tools = %{version}
Obsoletes:      %{name}-tools < %{version}

%description -n imobiledevice-tools
libimobiledevice is a software library that talks the protocols to support
iOS devices. It does not depend on any existing libraries from Apple.

%package -n python-imobiledevice
Summary:        Python bindings for %{name}
License:        LGPL-2.1+
Group:          Development/Languages/Python
Requires:       %{name}%{soname} = %{version}
Requires:       python-plist >= 1.11

%description -n python-imobiledevice
Contains Python bindings for developing applications that use %{name}.

%prep
%setup -q
autoreconf -fi
sed -i -e '/Requires:/d' src/%{name}-1.0.pc.in
sed -i -e 's/-L${libdir}//' src/%{name}-1.0.pc.in

%build
%configure --disable-silent-rules \
	--disable-static --disable-dev-tools
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}/%{_libdir}/%{name}.*a*

%post -n %{name}%{soname} -p /sbin/ldconfig

%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-,root,root)
%doc COPYING.LESSER
%{_libdir}/%{name}.so.%{soname}
%{_libdir}/%{name}.so.%{soname}.0.0

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files -n imobiledevice-tools
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LESSER NEWS README
%{_bindir}/idevice_id
%{_bindir}/idevicecrashreport
%{_bindir}/idevicepair
%{_bindir}/ideviceinfo
%{_bindir}/idevicesyslog
%{_bindir}/idevicebackup
%{_bindir}/idevicebackup2
%{_bindir}/idevicedebug
%{_bindir}/idevicedebugserverproxy
%{_bindir}/idevicediagnostics
%{_bindir}/ideviceimagemounter
%{_bindir}/idevicename
%{_bindir}/idevicescreenshot
%{_bindir}/ideviceenterrecovery
%{_bindir}/idevicedate
%{_bindir}/ideviceprovision
%{_bindir}/idevicenotificationproxy
%doc %{_mandir}/man1/idevice_id.1%{?ext_man}
%doc %{_mandir}/man1/idevicecrashreport.1%{?ext_man}
%doc %{_mandir}/man1/idevicepair.1%{?ext_man}
%doc %{_mandir}/man1/ideviceinfo.1%{?ext_man}
%doc %{_mandir}/man1/idevicesyslog.1%{?ext_man}
%doc %{_mandir}/man1/idevicebackup.1%{?ext_man}
%doc %{_mandir}/man1/idevicebackup2.1%{?ext_man}
%doc %{_mandir}/man1/idevicedebug.1%{?ext_man}
%doc %{_mandir}/man1/idevicedebugserverproxy.1%{?ext_man}
%doc %{_mandir}/man1/idevicediagnostics.1%{?ext_man}
%doc %{_mandir}/man1/ideviceimagemounter.1%{?ext_man}
%doc %{_mandir}/man1/idevicename.1%{?ext_man}
%doc %{_mandir}/man1/idevicescreenshot.1%{?ext_man}
%doc %{_mandir}/man1/ideviceenterrecovery.1%{?ext_man}
%doc %{_mandir}/man1/idevicedate.1%{?ext_man}
%doc %{_mandir}/man1/ideviceprovision.1%{?ext_man}
%doc %{_mandir}/man1/idevicenotificationproxy.1%{?ext_man}

%files -n python-imobiledevice
%defattr(-,root,root)
%{python_sitearch}/imobiledevice.so

%changelog
