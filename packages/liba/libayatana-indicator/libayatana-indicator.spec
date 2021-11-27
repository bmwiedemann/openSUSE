#
# spec file for package libayatana-indicator
#
# Copyright (c) 2021 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "gtk2"
%global gtkver 2
%endif
%if "%{flavor}" == "gtk3"
%global psuffix 3
%global gtkver 3
%endif
%define sover   7
Name:           libayatana-indicator
Version:        0.9.0
Release:        0
Summary:        Ayatana panel indicator applet libraries
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/AyatanaIndicators/libayatana-indicator
Source:         https://github.com/AyatanaIndicators/libayatana-indicator/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
%if "%{flavor}" == ""
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "gtk2"
BuildRequires:  pkgconfig(gtk+-2.0)
%else
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libayatana-ido3-0.4) >= 0.8.2
%endif

%description
This library contains information to build indicators to go into
the indicator applet.

%package -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover}
Summary:        Ayatana panel indicator applet library
Group:          System/Libraries

%description -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover}
This package provides the libraries required to build indicators
and to go into the indicator applet.

%package -n libayatana-indicator%{?psuffix}-devel
Summary:        Development files for the Ayatana panel indicator applet library
Group:          Development/Libraries/Other
Requires:       libayatana-indicator%{?psuffix:%{psuffix}-}%{sover} = %{version}

%description -n libayatana-indicator%{?psuffix}-devel
This package provides the development files required to build
indicators and to go into the indicator applet.

%prep
%setup -q

%build
%cmake \
%if "%{flavor}" == "gtk2"
  -DFLAVOUR_GTK2=ON
%else
  -DFLAVOUR_GTK3=ON
%endif
%cmake_build

%install
%cmake_install

%post -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%postun -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%files -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/libayatana-indicator%{?psuffix}.so.%{sover}*

%files -n libayatana-indicator%{?psuffix}-devel
%{_includedir}/libayatana-indicator%{?psuffix}-0.4/
%{_libdir}/libayatana-indicator%{?psuffix}.so
%{_libdir}/pkgconfig/ayatana-indicator%{?psuffix}-0.4.pc
%if "%{flavor}" != "gtk2"
%{_libexecdir}/libayatana-indicator/
%{_datadir}/libayatana-indicator/
%endif

%changelog
