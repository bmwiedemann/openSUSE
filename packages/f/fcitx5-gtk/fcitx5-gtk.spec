#
# spec file for package fcitx5-gtk
#
# Copyright (c) 2022 SUSE LLC
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


Name:           fcitx5-gtk
Version:        5.0.21
Release:        0
Summary:        Gtk im module for fcitx5 and glib based dbus client library
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx5-gtk
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libxkbcommon-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  gtk4-devel
%endif

%description
Gtk im module for fcitx5 and glib based dbus client library.

%package -n libFcitx5GClient-devel
Summary:        Development files for libFcitx5GClient
Group:          Development/Libraries/C and C++
Requires:       libFcitx5GClient2 = %{version}

%description -n libFcitx5GClient-devel
This package provides development files for libFcitx5GClient.

%package -n libFcitx5GClient2
Summary:        GClient library for fcitx5
Group:          System/Libraries

%description -n libFcitx5GClient2
This package provides GClient library for fcitx5.

%package -n fcitx5-gtk2
Summary:        GTK+ 2.0 im module for fcitx5
Group:          System/I18n/Chinese
Provides:       fcitx-gtk2 = %{version}
Obsoletes:      fcitx-gtk2 <= 4.2.9.8
Supplements:    (fcitx5 and libgtk-2_0-0)
%{gtk2_immodule_requires}

%description -n fcitx5-gtk2
This package provides GTK+ 2.0 im module for fcitx5.

%package -n fcitx5-gtk3
Summary:        GTK+ 3.0 im module for fcitx5
Group:          System/I18n/Chinese
Provides:       fcitx-gtk3 = %{version}
Obsoletes:      fcitx-gtk3 <= 4.2.9.8
Supplements:    (fcitx5 and libgtk-3-0)
%{gtk3_immodule_requires}

%description -n fcitx5-gtk3
This package provides GTK+ 3.0 im module for fcitx5.

%if 0%{?suse_version} >= 1550
%package -n fcitx5-gtk4
Summary:        GTK+ 4.0 im module for fcitx5
Group:          System/I18n/Chinese
Requires(post): glib2-tools
Requires(postun):glib2-tools
Supplements:    (fcitx5 and libgtk-4-1)

%description -n fcitx5-gtk4
This package provides GTK+ 4.0 im module for fcitx5.
%endif

%package -n typelib-1_0-FcitxG-1_0
Summary:        Introspection bindings for fcitx5
Group:          System/Libraries
Provides:       typelib-1_0-Fcitx-1_0 = %{version}
Obsoletes:      typelib-1_0-Fcitx-1_0 <= 4.2.9.8

%description -n typelib-1_0-FcitxG-1_0
This package provides the GObject Introspection bindings for fcitx5.

%prep
%setup -q

%build
%if 0%{?suse_version} < 1550
%cmake -DENABLE_GTK4_IM_MODULE=OFF
%else
%cmake
%endif
%make_build

%install
%cmake_install

%post -n libFcitx5GClient2 -p /sbin/ldconfig

%post -n fcitx5-gtk2
%{gtk2_immodule_post}

%post -n fcitx5-gtk3
%{gtk3_immodule_post}

%postun -n libFcitx5GClient2 -p /sbin/ldconfig

%postun -n fcitx5-gtk2
%{gtk2_immodule_postun}

%postun -n fcitx5-gtk3
%{gtk3_immodule_postun}

%if 0%{?suse_version} >= 1550
%post -n fcitx5-gtk4
if [ -d %{_libdir}/gtk-4.0/4.0.0/immodules ]; then
if [ -x %{_bindir}/gio-querymodules-64 ]; then
  %{_bindir}/gio-querymodules-64 %{_libdir}/gtk-4.0/4.0.0/immodules
else
  %{_bindir}/gio-querymodules %{_libdir}/gtk-4.0/4.0.0/immodules
fi
fi

%postun -n fcitx5-gtk4
if [ $1 -eq 0 ]; then
if [ -d %{_libdir}/gtk-4.0/4.0.0/immodules ]; then
if [ -x %{_bindir}/gio-querymodules-64 ]; then
  %{_bindir}/gio-querymodules-64 %{_libdir}/gtk-4.0/4.0.0/immodules
else
  %{_bindir}/gio-querymodules %{_libdir}/gtk-4.0/4.0.0/immodules
fi
fi
fi
%endif

%files -n libFcitx5GClient-devel
%doc README.md
%license LICENSES
%dir %{_includedir}/Fcitx5
%dir %{_includedir}/Fcitx5/GClient
%dir %{_includedir}/Fcitx5/GClient/fcitx-gclient
%{_includedir}/Fcitx5/GClient/fcitx-gclient/fcitxgclient.h
%{_includedir}/Fcitx5/GClient/fcitx-gclient/fcitxgwatcher.h
%{_libdir}/cmake/Fcitx5GClient
%{_libdir}/libFcitx5GClient.so
%{_libdir}/pkgconfig/Fcitx5GClient.pc
%{_datadir}/gir-1.0/FcitxG-1.0.gir

%files -n typelib-1_0-FcitxG-1_0
%{_libdir}/girepository-1.0/FcitxG-1.0.typelib

%files -n libFcitx5GClient2
%{_libdir}/libFcitx5GClient.so.2
%{_libdir}/libFcitx5GClient.so.%{version}

%files -n fcitx5-gtk2
%{_libdir}/gtk-2.0/2.10.0/immodules/im-fcitx5.so

%files -n fcitx5-gtk3
%{_libdir}/gtk-3.0/3.0.0/immodules/im-fcitx5.so

%if 0%{?suse_version} >= 1550
%files -n fcitx5-gtk4
%dir %{_libdir}/gtk-4.0/4.0.0/immodules
%{_libdir}/gtk-4.0/4.0.0/immodules/libim-fcitx5.so
%endif

%changelog
