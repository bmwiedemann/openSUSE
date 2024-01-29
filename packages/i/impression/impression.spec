#
# spec file for package impression
#
# Copyright (c) 2023 SUSE LLC
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


Name:           impression
Version:        3.0.1
Release:        0
Summary:        A straight-forward and modern application to create bootable drives
License:        GPL-3.0-only
URL:            https://gitlab.com/adhami3310/Impression
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pango)
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  cargo-packaging
BuildRequires:  appstream-glib
BuildRequires:  python3-gobject

%description
Write disk images onto your drives with ease. Select an image, insert your drive, and you're good to go! Impression is a useful tool for both avid distro-hoppers and casual computer users. See Press for content mentioning Impression from various writers, content creators, etc.

%lang_package

%prep
%autosetup -a1

%build
%meson
%meson_build

%install
%meson_install

%find_lang impression

%files
%license COPYING
%doc README.md
%{_bindir}/impression
%{_datadir}/applications/io.gitlab.adhami3310.Impression.desktop
%{_datadir}/glib-2.0/schemas/io.gitlab.adhami3310.Impression.gschema.xml
%{_datadir}/icons/*
%dir %{_datadir}/impression
%{_datadir}/impression/resources.gresource
%{_datadir}/metainfo/io.gitlab.adhami3310.Impression.metainfo.xml

%files lang -f impression.lang

%changelog
