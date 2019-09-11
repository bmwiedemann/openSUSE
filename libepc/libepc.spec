#
# spec file for package libepc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
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


Name:           libepc
Version:        0.4.6
Release:        0
Summary:        Easy Publish and Consume Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://live.gnome.org/libepc/
Source:         https://download.gnome.org/sources/libepc/0.4/%{name}-%{version}.tar.xz

BuildRequires:  gdbm-devel
BuildRequires:  intltool
BuildRequires:  libgnutls-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  xz
BuildRequires:  pkgconfig(avahi-ui-gtk3)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(uuid)

%description
The Easy Publish and Consume library provides an easy method to:

    * publish data using HTTPS: EpcPublisher
    * announce that information via DNS-SD: EpcDispatcher
    * find that information: EpcConsumer
    * and finally consume it

You can use this library as a key/value store published to the network,
using encryption, authentication and service discovery.

%package 1_0-2
Summary:        Easy Publish and Consume Library
Group:          System/Libraries
Recommends:     %{name}-lang = %{version}
# For lang package to be installable:
Provides:       %{name} = %{version}

%description 1_0-2
The Easy Publish and Consume library provides an easy method to:

    * publish data using HTTPS: EpcPublisher
    * announce that information via DNS-SD: EpcDispatcher
    * find that information: EpcConsumer
    * and finally consume it

You can use this library as a key/value store published to the network,
using encryption, authentication and service discovery.

%package devel
Summary:        Easy Publish and Consume Library
Group:          Development/Libraries/GNOME
Requires:       %{name}-1_0-2 = %{version}

%description devel
Development headers for libepc.

The Easy Publish and Consume library provides an easy method to:

    * publish data using HTTPS: EpcPublisher
    * announce that information via DNS-SD: EpcDispatcher
    * find that information: EpcConsumer
    * and finally consume it

You can use this library as a key/value store published to the network,
using encryption, authentication and service discovery.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post 1_0-2 -p /sbin/ldconfig
%postun 1_0-2 -p /sbin/ldconfig

%files 1_0-2
%{_libdir}/%{name}*.so.*

%files devel
%{_includedir}/%{name}-1.0
%{_includedir}/%{name}-ui-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libepc*.pc
%{_datadir}/gtk-doc/html/%{name}-1.0
# Own these repositories to not depend on gtk-doc while building:
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html

%files lang -f %{name}.lang

%changelog
