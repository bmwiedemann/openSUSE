#
# spec file for package libindicator
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname  libindicator3
%define soname_gtk2 libindicator
%define sover   7
%define _version 16.10.0+18.04.20171205.1
Name:           libindicator
Version:        16.10.0+bzr20171205
Release:        0
Summary:        Panel indicator applet libraries
License:        GPL-3.0-only
Group:          System/GUI/Other
Url:            https://launchpad.net/libindicator
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
# PATCH-FIX-OPENSUSE libindicator-disable-werror.patch hrvoje.senjan@gmail.com -- Disable -Werror.
Patch0:         libindicator-disable-werror.patch
BuildRequires:  gnome-common
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libido3-0.1)

%description
This library contains information to build indicators to go into
the indicator applet.

%package -n %{soname}-%{sover}
Summary:        Panel indicator applet library
Group:          System/Libraries

%description -n %{soname}-%{sover}
This package provides the libraries required to build indicators
and to go into the indicator applet.

%package -n %{soname_gtk2}%{sover}
Summary:        Panel indicator applet library for GTK+2
Group:          System/Libraries

%description -n %{soname_gtk2}%{sover}
This package provides the libraries required to build indicators
and to go into the indicator applet.

%package -n %{soname}-devel
Summary:        Development files for the Panel indicator applet
Group:          Development/Libraries/Other
Requires:       %{soname}-%{sover} = %{version}

%description -n %{soname}-devel
This package provides the development files required to build
indicators and to go into the indicator applet.

%package -n %{soname_gtk2}-devel
Summary:        Development files for the Panel indicator applet (GTK+2 variant)
Group:          Development/Libraries/Other
Requires:       %{soname_gtk2}%{sover} = %{version}

%description -n %{soname_gtk2}-devel
This package provides the development files required to build
indicators and to go into the indicator applet.

%prep
%setup -q -c
%patch0 -p1

%build

%global _configure ../configure
NOCONFIGURE=1 gnome-autogen.sh
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
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS NEWS
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{soname_gtk2}%{sover}
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS NEWS
%{_libdir}/%{soname_gtk2}.so.%{sover}*

%files -n %{soname}-devel
%{_includedir}/%{soname}-0.4/
%{_libexecdir}/indicator-loader3
%{_libdir}/%{soname}.so
%{_datadir}/%{name}/
%{_libdir}/pkgconfig/indicator3-0.4.pc

%files -n %{soname_gtk2}-devel
%{_includedir}/%{soname_gtk2}-0.4/
%{_libdir}/%{soname_gtk2}.so
%{_libdir}/pkgconfig/indicator-0.4.pc

%changelog
