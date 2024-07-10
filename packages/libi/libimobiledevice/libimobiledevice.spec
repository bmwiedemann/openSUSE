#
# spec file for package libimobiledevice
#
# Copyright (c) 2023 SUSE LLC
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


%define libname libimobiledevice-1_0-6
Name:           libimobiledevice
Version:        1.3.0+190git.20230705
Release:        0
Summary:        Native protocols library for iOS devices
License:        LGPL-2.1-or-later
URL:            https://www.libimobiledevice.org
Source:         %{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  (python3-Cython >= 0.17 with python3-Cython < 3)
BuildRequires:  python3-plist
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libimobiledevice-glue-1.0) >= 1.0.0
BuildRequires:  pkgconfig(libplist-2.0) >= 2.3.0
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libusbmuxd-2.0) >= 2.0.2
BuildRequires:  pkgconfig(python3)

%description
libimobiledevice is a software library that talks the protocols to support
iOS devices. It does not depend on any existing libraries from Apple.

%package -n %{libname}
Summary:        Native protocols library for iOS devices
License:        LGPL-2.1-or-later

%description -n %{libname}
libimobiledevice is a software library that talks the protocols to support
iOS devices. It does not depend on any existing libraries from Apple.

%package devel
Summary:        Development files for %{name}
License:        LGPL-2.1-or-later
Requires:       %{libname} = %{version}
Requires:       pkgconfig(libplist-2.0)

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n imobiledevice-tools
Summary:        Tools using %{name} for iOS devices
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Requires:       %{libname} = %{version}
Provides:       %{name}-tools = %{version}
Obsoletes:      %{name}-tools < %{version}

%description -n imobiledevice-tools
libimobiledevice is a software library that talks the protocols to support
iOS devices. It does not depend on any existing libraries from Apple.

%package -n python3-imobiledevice
Summary:        Python bindings for %{name}
License:        LGPL-2.1-or-later
Requires:       %{libname} = %{version}
Requires:       python3-plist >= 1.11

%description -n python3-imobiledevice
Contains Python bindings for developing applications that use %{name}.

%prep
%setup -q
sed -i -e '/Requires:/d' src/%{name}-1.0.pc.in
sed -i -e 's/-L${libdir}//' src/%{name}-1.0.pc.in

%build
autoreconf -fvi
%configure \
  --disable-silent-rules \
  --disable-static \
  PYTHON=%{_bindir}/python3 PACKAGE_VERSION=%{version}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING.LESSER
%{_libdir}/%{name}-1.0.so.6*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}-1.0.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files -n imobiledevice-tools
%doc AUTHORS NEWS README.md
%{_bindir}/idevice_id
%{_bindir}/idevicebtlogger
%{_bindir}/idevicecrashreport
%{_bindir}/idevicedevmodectl
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
%{_bindir}/idevicesetlocation
%{_bindir}/ideviceprovision
%{_bindir}/idevicenotificationproxy
%{_mandir}/man1/idevice_id.1%{?ext_man}
%{_mandir}/man1/idevicebtlogger.1%{?ext_man}
%{_mandir}/man1/idevicecrashreport.1%{?ext_man}
%{_mandir}/man1/idevicedevmodectl.1%{?ext_man}
%{_mandir}/man1/idevicepair.1%{?ext_man}
%{_mandir}/man1/ideviceinfo.1%{?ext_man}
%{_mandir}/man1/idevicesyslog.1%{?ext_man}
%{_mandir}/man1/idevicebackup.1%{?ext_man}
%{_mandir}/man1/idevicebackup2.1%{?ext_man}
%{_mandir}/man1/idevicedebug.1%{?ext_man}
%{_mandir}/man1/idevicedebugserverproxy.1%{?ext_man}
%{_mandir}/man1/idevicediagnostics.1%{?ext_man}
%{_mandir}/man1/ideviceimagemounter.1%{?ext_man}
%{_mandir}/man1/idevicename.1%{?ext_man}
%{_mandir}/man1/idevicescreenshot.1%{?ext_man}
%{_mandir}/man1/ideviceenterrecovery.1%{?ext_man}
%{_mandir}/man1/idevicesetlocation.1%{?ext_man}
%{_mandir}/man1/idevicedate.1%{?ext_man}
%{_mandir}/man1/ideviceprovision.1%{?ext_man}
%{_mandir}/man1/idevicenotificationproxy.1%{?ext_man}

%files -n python3-imobiledevice
%{python3_sitearch}/imobiledevice.so

%changelog
