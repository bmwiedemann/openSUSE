#
# spec file for package switchboard
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover   2_0-0
Name:           switchboard
Version:        2.3.6
Release:        0
Summary:        Modular Desktop Settings Hub
License:        LGPL-2.1-only AND LGPL-3.0-only
Group:          System/GUI/Other
URL:            https://elementary.io/
Source:         https://github.com/elementary/switchboard/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(vapigen) >= 0.28.0
Requires:       gsettings-backend-dconf
Recommends:     %{name}-lang

%description
Switchboard is a modular system settings hub designed for the Pantheon desktop.

%package -n     lib%{name}-%{sover}
Summary:        Modular Desktop Settings Hub
Group:          System/Libraries

%description -n lib%{name}-%{sover}
This package contains the shared library required to run the plugs.

%package        devel
Summary:        Development Files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-%{sover} = %{version}

%description    devel
Switchboard is a modular system settings hub designed for the Pantheon desktop.

This package contains development files needed to develop plugins for
%{name}.

%lang_package

%prep
%setup -q

%build
%meson \
  -Dlibunity=false
%meson_build

%install
%meson_install
%suse_update_desktop_file io.elementary.switchboard -r System HardwareSettings
%find_lang io.elementary.switchboard %{name}.lang
%fdupes %{buildroot}%{_datadir}

%post   -n lib%{name}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc README.md
%{_bindir}/io.elementary.switchboard
%{_datadir}/applications/io.elementary.switchboard.desktop
%{_datadir}/glib-2.0/schemas/io.elementary.switchboard.gschema.xml
%{_datadir}/metainfo/io.elementary.switchboard.appdata.xml

%files -n lib%{name}-%{sover}
%{_libdir}/libswitchboard*.so.*

%files devel
%{_includedir}/switchboard*/
%{_libdir}/libswitchboard*.so
%{_libdir}/pkgconfig/switchboard*.pc
%{_datadir}/vala/vapi/switchboard*.deps
%{_datadir}/vala/vapi/switchboard*.vapi

%files lang -f %{name}.lang

%changelog
