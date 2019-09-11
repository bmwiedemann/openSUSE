#
# spec file for package libayatana-indicator
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


%define soname  libayatana-indicator3
%define soname_gtk2 libayatana-indicator
%define sover   7
Name:           libayatana-indicator
Version:        0.6.2
Release:        0
Summary:        Ayatana panel indicator applet libraries
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/AyatanaIndicators/libayatana-indicator
Source:         https://github.com/AyatanaIndicators/libayatana-indicator/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE libayatana-indicator-disable-werror.patch hrvoje.senjan@gmail.com -- Disable -Werror.
Patch0:         libayatana-indicator-disable-werror.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libayatana-ido3-0.4)

%description
This library contains information to build indicators to go into
the indicator applet.

%package -n %{soname}-%{sover}
Summary:        Ayatana panel indicator applet library
Group:          System/Libraries

%description -n %{soname}-%{sover}
This package provides the libraries required to build indicators
and to go into the indicator applet.

%package -n %{soname_gtk2}%{sover}
Summary:        Ayatana panel indicator applet library for GTK+2
Group:          System/Libraries

%description -n %{soname_gtk2}%{sover}
This package provides the libraries required to build indicators
and to go into the indicator applet.

%package -n %{soname}-devel
Summary:        Development files for the Ayatana panel indicator applet library
Group:          Development/Libraries/Other
Requires:       %{soname}-%{sover} = %{version}

%description -n %{soname}-devel
This package provides the development files required to build
indicators and to go into the indicator applet.

%package -n %{soname_gtk2}-devel
Summary:        Development files for the Ayatana panel indicator applet (GTK+2 variant)
Group:          Development/Libraries/Other
Requires:       %{soname_gtk2}%{sover} = %{version}

%description -n %{soname_gtk2}-devel
This package provides the development files required to build
indicators and to go into the indicator applet.

%prep
%setup -q
%patch0 -p1

%build
%global _configure ../configure
autoreconf -fi
for ver in 2 3; do
    mkdir build-gtk$ver
    pushd build-gtk$ver
    %configure --disable-static --with-gtk=$ver
    make %{?_smp_mflags} V=1
    popd
done

%install
for ver in 2 3; do
    pushd build-gtk$ver
    %make_install
    popd
done
find %{buildroot} -type f -name "*.la" -delete -print

# This dummy indicator is fairly useless, it is not shipped in Ubuntu.
rm %{buildroot}%{_libdir}/libdummy-indicator*.so

%post -n %{soname}-%{sover} -p /sbin/ldconfig

%postun -n %{soname}-%{sover} -p /sbin/ldconfig

%post -n %{soname_gtk2}%{sover} -p /sbin/ldconfig

%postun -n %{soname_gtk2}%{sover} -p /sbin/ldconfig

%files -n %{soname}-%{sover}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{soname_gtk2}%{sover}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/%{soname_gtk2}.so.%{sover}*

%files -n %{soname}-devel
%{_includedir}/%{soname}-0.4/
%{_libexecdir}/ayatana-indicator-loader3
%{_libdir}/%{soname}.so
%{_datadir}/%{name}/
%{_libdir}/pkgconfig/ayatana-indicator3-0.4.pc

%files -n %{soname_gtk2}-devel
%{_includedir}/%{soname_gtk2}-0.4/
%{_libdir}/%{soname_gtk2}.so
%{_libdir}/pkgconfig/ayatana-indicator-0.4.pc

%changelog
