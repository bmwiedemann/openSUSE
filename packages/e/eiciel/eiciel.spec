#
# spec file for package eiciel
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


%define _libnautilus_extensiondir %(pkg-config --variable extensiondir libnautilus-extension-4)

Name:           eiciel
Version:        0.10.0.rc2
Release:        0
Summary:        GNOME ACL viewer and editor
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://rofi.roger-ferrer.org/eiciel/
# Source0:        http://rofi.roger-ferrer.org/eiciel/files/%%{name}-%%{version}.tar.bz2
Source0:        https://github.com/rofirrim/eiciel/archive/refs/tags/0.10.0-rc2.tar.gz#/%{name}-%{version}.tar.gz

# FIX-UPSTREAM-PATCH 0001-Add-man-subdir-to-top-level-meson.build.patch luc14n0@opensuse.org
# Intall the manpage that was silently being ignored by Meson
Patch1:         0001-Add-man-subdir-to-top-level-meson.build.patch
# FIX-UPSTREAM-PATCH 0001-Replace-deprecated-attr-xattr.h-with-sys-xattr.h.patch luc14n0@opensuse.org
# Use sys/xattr.h in place of deprecated attr/xattr.h
Patch2:         0001-Replace-deprecated-attr-xattr.h-with-sys-xattr.h.patch

BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  libacl-devel
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(giomm-2.68) >= 2.68
BuildRequires:  pkgconfig(gtkmm-4.0) >= 4.6
BuildRequires:  pkgconfig(libnautilus-extension-4) >= 43

%description
Eiciel allows you to visually edit file ACL entries. You can add and
remove users and groups who will be granted permissions through the
graphical interface

%package -n nautilus-eiciel
Summary:        Nautilus ACL viewer and editor extension
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Supplements:    (eiciel and nautilus)

%description -n nautilus-eiciel
A Nautilus extension that allows viewing and editing ACL permissions.

%lang_package

%prep
%autosetup -p1 -n eiciel-0.10.0-rc2

%build
%meson          \
    -D man=true \
    %{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS README.md
%{_datadir}/help/C/%{name}
%{_bindir}/eiciel
%{_mandir}/man1/eiciel.1%{?ext_man}
%{_datadir}/applications/org.roger_ferrer.Eiciel.desktop
%{_datadir}/icons/hicolor/*/apps/*eiciel.*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.roger_ferrer.Eiciel.appdata.xml

%files -n nautilus-eiciel
%{_libnautilus_extensiondir}/libeiciel-nautilus.so

%files lang -f %{name}.lang

%changelog
