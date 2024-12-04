#
# spec file for package libosinfo
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands.
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


%define with_lang 1

Name:           libosinfo
Version:        1.12.0
Release:        0
Summary:        Operating system and hypervisor information management library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://releases.pagure.org/libosinfo
Source0:        %{url}/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  hwdata
BuildRequires:  libcurl-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150600
BuildRequires:  pkgconfig(libsoup-2.4)
%else
BuildRequires:  pkgconfig(libsoup-3.0)
%endif
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt) >= 1.0.0
Requires:       osinfo-db
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package -n libosinfo-1_0-0
Summary:        Operating system and hypervisor information management library
Group:          System/Libraries
Requires:       %{name} >= %{version}
# for usb.ids and pci.ids
Requires:       hwdata

%description -n libosinfo-1_0-0
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package -n typelib-1_0-Libosinfo-1_0
Summary:        Typelib files for libosinfo
Group:          System/Libraries

%description -n typelib-1_0-Libosinfo-1_0
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

%package devel
Summary:        Header files for libosinfo, an OS/hypervisor information library
Group:          Development/Languages/C and C++
Requires:       libosinfo-1_0-0 = %{version}
Requires:       typelib-1_0-Libosinfo-1_0 = %{version}

%description devel
libosinfo is a library that allows virtualization provisioning tools to
determine the optimal device settings for a hypervisor/operating system
combination.

This package provides includes to compile with the libosinfo library,
as well as Vala bindings for the libosinfo library.

%if %{with_lang}
%lang_package
%endif

%prep
%autosetup -p1

%build
%meson \
    -Denable-gtk-doc=true \
    -Denable-tests=true \
    -Denable-introspection=enabled \
    -Denable-vala=enabled
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%if %{with_lang}
%find_lang %{name} %{?no_lang_C}
%endif

%ldconfig_scriptlets -n libosinfo-1_0-0

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/osinfo-detect
%{_bindir}/osinfo-install-script
%{_bindir}/osinfo-query
%{_mandir}/man1/osinfo-detect.1%{?ext_man}
%{_mandir}/man1/osinfo-install-script.1%{?ext_man}
%{_mandir}/man1/osinfo-query.1%{?ext_man}

%files -n libosinfo-1_0-0
%{_libdir}/libosinfo-1.0.so.*

%files -n typelib-1_0-Libosinfo-1_0
%{_libdir}/girepository-1.0/Libosinfo-1.0.typelib

%files devel
%{_datadir}/gtk-doc/
%{_includedir}/%{name}-1.0
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_libdir}/libosinfo-1.0.so
%{_datadir}/gir-1.0/Libosinfo-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libosinfo-1.0.deps
%{_datadir}/vala/vapi/libosinfo-1.0.vapi

%if %{with_lang}
%files lang -f %{name}.lang
%endif

%changelog
