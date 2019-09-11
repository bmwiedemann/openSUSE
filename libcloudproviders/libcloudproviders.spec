#
# spec file for package libcloudproviders
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


Name:           libcloudproviders
Version:        0.2.5
Release:        0
Summary:        Library/Client to integrate cloud storage providers
License:        LGPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/External/libcloudproviders
Source:         https://gitlab.gnome.org/External/libcloudproviders/uploads/32bb0a808c397d55b6d72c61540c0171/libcloudproviders-0.2.5.tar.xz
Source99:       %{name}-rpmlintrc
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.51.2
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.51.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.51.2
BuildRequires:  pkgconfig(systemd)

%description
Cross desktop library for desktop integration of cloud storage
providers and sync tools.

%package -n libcloudproviders0
Summary:        Library to integrate cloud storage providers
Group:          System/Libraries

%description -n libcloudproviders0
Cross desktop library for desktop integration of cloud storage
providers and sync tools.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       libcloudproviders0 = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%meson \
    -Denable-gtk-doc=true
%meson_build

%install
%meson_install

%check
%{meson_test}

%post -n libcloudproviders0 -p /sbin/ldconfig
%postun -n libcloudproviders0 -p /sbin/ldconfig

%files -n libcloudproviders0
%license LICENSE
%doc CHANGELOG README.md
%{_libdir}/libcloudproviders.so.*

%files devel
%{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/cloudproviders/
%{_libdir}/libcloudproviders.so
%{_libdir}/pkgconfig/cloudproviders.pc
%{_libdir}/*.so

%changelog
