#
# spec file for package libayatana-indicator
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "gtk2"
%global gtkver 2
%endif
%if "%{flavor}" == "gtk3"
%global psuffix 3
%global gtkver 3
%endif
%define sover   7

%define common_name ayatana-indicator%{?psuffix:%{psuffix}-}%{?sover}-common

Name:           libayatana-indicator
Version:        0.9.4
Release:        0
Summary:        Ayatana panel indicator applet libraries
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/AyatanaIndicators/libayatana-indicator
Source0:        https://github.com/AyatanaIndicators/libayatana-indicator/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
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

%package -n %{common_name}
Summary:        Common files used by libayatana-indicator
BuildArch:      noarch
# No translations provided currently.
#Recommends:    %%{common_name}-lang

%description -n %{common_name}
This library contains information to build indicators to go into
the indicator applet.

This package contains common files.



#%%lang_package -n %%{common_name}
%package -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover}
Summary:        Ayatana panel indicator applet library
Group:          System/Libraries
Requires:       %{common_name} = %{version}

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
%if 0%{?sle_version} <= 150200
  -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
%endif
  -DFLAVOUR_GTK3=ON
%endif
%cmake_build

%install
%cmake_install

#%%find_lang %%{name}

# The library is not created with the proper executable permissions for some
# reason, which creates quite a few problems, so fix that up manually.
chmod +x %{buildroot}%{_libdir}/libayatana-indicator%{?psuffix}.so.%{sover}*
%if "%{flavor}" != "gtk2"
chmod +x %{buildroot}%{_libexecdir}/libayatana-indicator/*
%endif

# Create empty directory for owning within this package.
install -d -m 755 %{buildroot}%{_libdir}/ayatana-indicators%{?psuffix}/%{sover}

%post -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%postun -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%files -n %{common_name}
%license COPYING
%doc AUTHORS INSTALL.md NEWS NEWS.Canonical
%if "%{flavor}" != "gtk2"
%{_datadir}/libayatana-indicator/
%endif

%files -n libayatana-indicator%{?psuffix:%{psuffix}-}%{sover}
%license COPYING
%dir %{_libdir}/ayatana-indicators%{?psuffix}/
%dir %{_libdir}/ayatana-indicators%{?psuffix}/%{sover}/
%{_libdir}/libayatana-indicator%{?psuffix}.so.%{sover}*
%if "%{flavor}" != "gtk2"
%{_libexecdir}/libayatana-indicator/
%endif

%files -n libayatana-indicator%{?psuffix}-devel
%{_includedir}/libayatana-indicator%{?psuffix}-0.4/
%{_libdir}/libayatana-indicator%{?psuffix}.so
%{_libdir}/pkgconfig/ayatana-indicator%{?psuffix}-0.4.pc

#%%files -n %%{common_name}-lang -f %%{name}.lang

%changelog
