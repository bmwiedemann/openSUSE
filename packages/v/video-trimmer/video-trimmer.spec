#
# spec file for package video-trimmer
#
# Copyright (c) 2025 mantarimay
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


%define rurl ae720db1ea4142329be911b7a048a301
Name:           video-trimmer
Version:        25.03
Release:        0
Summary:        Trim videos quickly
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/YaLTeR/video-trimmer
Source0:        https://gitlab.gnome.org/-/project/11135/uploads/%{rurl}/%{name}-%{version}.tar.xz
BuildRequires:  blueprint-compiler
BuildRequires:  cargo-packaging
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.6.0

%description
Video Trimmer cuts out a fragment of a video given the start and end
timestamps. The video is never re-encoded, so the process is very fast and
does not reduce the video quality.

%lang_package

%prep
%autosetup 

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/video-trimmer/
%{_datadir}/icons/*/*/*/*.svg

%files lang -f %{name}.lang

%changelog
