#
# spec file for package libgnt
#
# Copyright (c) 2025 SUSE LLC
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


%define sover   0
Name:           libgnt
Version:        2.14.4
Release:        0
Summary:        TUI toolkit based on GLib and ncurses
License:        GPL-2.0-or-later
URL:            https://pidgin.im/
Source0:        https://downloads.sf.net/pidgin/%{name}-%{version}-dev.tar.xz
Source1:        https://downloads.sf.net/pidgin/%{name}-%{version}-dev.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x40de1dc7288fe3f50ab938c548f66affd9bdb729#/%{name}.keyring
Source3:        baselibs.conf
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses)

%description
GNT is an ncurses toolkit for creating text-mode graphical user
interfaces.

%package -n %{name}%{sover}
Summary:        TUI Toolkit based on GLib and ncurses

%description -n %{name}%{sover}
GNT is an ncurses toolkit for creating text-mode graphical user
interfaces.

%package -n %{name}-devel
Summary:        Development files of GNT
Requires:       %{name}%{sover} = %{version}

%description -n %{name}-devel
GNT is an ncurses toolkit for creating text-mode graphical user
interfaces.

The GNT development package includes the header files, libraries,
and development tools necessary for compiling and linking
applications which will use GNT.

%prep
%autosetup -p1 -n %{name}-%{version}-dev

%build
%meson -D python2=false
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%doc ChangeLog README.md
%{_libdir}/%{name}.so.%{sover}*

%files -n %{name}-devel
%{_datadir}/gtk-doc/html/%{name}
%{_includedir}/gnt
%{_libdir}/%{name}.so
%{_libdir}/gnt
%{_libdir}/pkgconfig/gnt.pc

%changelog
