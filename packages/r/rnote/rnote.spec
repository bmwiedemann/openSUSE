#
# spec file for package rnote
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2022 Fabio Pesari
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

Name:           rnote
Version:        0.13.1
Release:        0
Summary:        Sketch, take handwritten notes and annotate PDF files
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://github.com/flxzt/rnote
Source:         rnote-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  meson >= 1.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
ExcludeArch:    i586

%description
Rnote is a vector-based drawing app for sketching, handwritten notes and
to annotate documents and pictures. Targeted at students, teachers and those
who own a drawing tablet, it provides features like PDF and picture import
and export, an infinite canvas and an adaptive UI for big and small screens.

%lang_package

%prep
%autosetup -a1

%build
%meson
%meson_build

%install
%meson_install
rm -r %{buildroot}%{_datadir}/locale/{zh_Hans,zh_Hant}
%fdupes %{buildroot}%{_datadir}/locale/
%find_lang %{name}

%files
%doc README.md AUTHORS
%license LICENSE
%{_bindir}/rnote
%{_bindir}/rnote-cli
%{_datadir}/rnote
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml
%{_datadir}/fonts/rnote-fonts
%{_datadir}/thumbnailers

%files lang -f %{name}.lang

%changelog
