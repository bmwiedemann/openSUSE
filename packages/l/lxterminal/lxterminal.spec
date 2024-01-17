#
# spec file for package lxterminal
#
# Copyright (c) 2021 SUSE LLC
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


Name:           lxterminal
Version:        0.4.0
Release:        0
Summary:        Lightweight LXDE Terminal
License:        GPL-2.0-only
Group:          System/GUI/LXDE
URL:            https://www.lxde.org/
Source0:        https://sourceforge.net/projects/lxde/files/LXTerminal%20%28terminal%20emulator%29/LXTerminal%200.4.x/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE lxterminal-0.1.8-disable-f10.patch andrea@opensuse.org
# disable f10 shortcut because yast use it
Patch0:         %{name}-0.1.8-disable-f10.patch
BuildRequires:  docbook-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(vte-2.91)
Recommends:     %{name}-lang

%description
LXTerminal is a lightweight Terminal Emulator.
This package even if DE independent is part
of the LXDE project.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-man \
	--enable-gtk3=yes
%make_build

%install
%make_install
%suse_update_desktop_file %{name} System
%find_lang %{name}
%fdupes -s %{buildroot}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/lxterminal.desktop
%dir %{_datadir}/lxterminal
%{_datadir}/lxterminal/lxterminal.conf
%{_datadir}/lxterminal/*.ui
%{_datadir}/icons/hicolor/128x128/apps/lxterminal.png
%{_mandir}/man1/lxterminal.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
