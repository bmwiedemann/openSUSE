#
# spec file for package eekboard
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define build_xtest (0%{suse_version} > 1210)

Name:           eekboard
Version:        1.0.8
Release:        0
Summary:        An easy to use virtual keyboard toolkit
License:        GPL-3.0+
Group:          System/GUI/Other
Url:            http://github.com/ueno/eekboard
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
%if 0%{?suse_version} >= 1220
BuildRequires:  pkgconfig(vapigen) >= 0.16.0
%else
BuildRequires:  libvala-0_14-devel
BuildRequires:  vala
%endif
BuildRequires:  at-spi2-core-devel
BuildRequires:  cairo-devel
BuildRequires:  gtk3-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libcroco-devel
BuildRequires:  libxklavier-devel
BuildRequires:  pango-devel
%if %{build_xtest}
BuildRequires:  libXtst-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  update-desktop-files

%glib2_gsettings_schema_requires

%description
eekboard is a virtual keyboard software package, including a set of
tools to implement desktop virtual keyboards.


%package -n typelib-1_0-Eek-0_90
Summary:        Eekboard libraries -- Introspection bindings
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n typelib-1_0-Eek-0_90
This package contains the libraries for eekboard

%package devel
Summary:        Development Files for libskk
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
The eekboard-devel package contains the header files.

%prep
%setup -q

%build
# ./autogen.sh
%configure --enable-introspection \
           --enable-vala \
           --enable-atspi \
%if %{build_xtest}
           --enable-xtest \
%endif
           --disable-schemas-compile \
           --enable-libcanberra=yes

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install 
rm -rf %{buildroot}%{_libdir}/*.la

%suse_update_desktop_file -i %{name} System Utility DesktopUtility settings
%suse_update_desktop_file -i %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%find_lang %{name}

%post 
/sbin/ldconfig
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun 
/sbin/ldconfig
%icon_theme_cache_postun
%glib2_gsettings_schema_postun

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING README AUTHORS
%{_bindir}/eekboard
%{_bindir}/eekboard-server
%{_libdir}/libeek*.so.*
%{_libexecdir}/eekboard-setup
%{_datadir}/applications/eekboard.desktop
%{_datadir}/dbus-1
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas
%config %{_sysconfdir}/xdg/autostart/eekboard-autostart.desktop
%{_datadir}/icons/hicolor

%files -n typelib-1_0-Eek-0_90
%defattr(-,root,root)
%{_libdir}/girepository-1.0/

%files devel
%defattr(-,root,root)
%{_includedir}/eek-0.90/
%{_includedir}/%{name}-0.90/
%{_libdir}/pkgconfig/eek*.pc
%{_libdir}/libeek*.so
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/*
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/eek*.vapi
%{_datadir}/vala/vapi/eek*.deps

%changelog
