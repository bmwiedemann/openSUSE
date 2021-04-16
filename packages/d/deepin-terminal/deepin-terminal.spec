#
# spec file for package deepin-terminal
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020 Hillwood Yang <hillwood@opensuse.org>
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


%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-terminal
Version:        5.0.4.3
Release:        0
Summary:        Deepin terminal
License:        GPL-3.0-only AND GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/linuxdeepin/deepin-terminal-gtk
Source0:        https://github.com/linuxdeepin/deepin-terminal-gtk/archive/%{version}/%{name}-gtk-%{version}.tar.gz
# PATCH-FIX-UPSTREAM deepin-terminal-xcb.vapi-missing-return-statement-at-end-of-subroutine-body.patch
Patch0:         deepin-terminal-xcb.vapi-missing-return-statement-at-end-of-subroutine-body.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.35.0
BuildRequires:  libxml2-tools
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(xcb)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%lang_package

%description
Deepin Terminal is an advanced terminal emulator with workspace, multiple
windows, remote management, quake mode and other features.

%prep
%autosetup -p1 -n %{name}-gtk-%{version}
sed -i 's|return @@PROJECT_PATH@@;|return "%{_datadir}/%{name}";|' project_path.c.in

%build
%cmake -DCMAKE_INSTALL_DIR=%{_prefix} \
       -DUSE_VENDOR_LIB=OFF \
       -DVERSION=%{version}-%{distribution}
%if 0%{?sle_version} > 150000 && 0%{?is_opensuse}
%cmake_build
%else
make %{?_smp_mflags}
%endif

%install
%cmake_install

%suse_update_desktop_file %{name}
%find_lang %{name}
%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%dir %{_datadir}/%{name}
%dir %{_prefix}/lib/%{name}
%{_bindir}/%{name}
%{_prefix}/lib/%{name}/ssh_login.sh
%{_datadir}/%{name}/style.css
%{_datadir}/%{name}/theme
%{_datadir}/%{name}/image
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%files lang -f %{name}.lang

%changelog
