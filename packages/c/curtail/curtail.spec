#
# spec file for package curtail
#
# Copyright (c) 2024 SUSE LLC
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


Name:           curtail
Version:        1.10.0
Release:        0
Summary:        A simple and useful image compressor
License:        GPL-3.0-or-later
URL:            https://github.com/Huluti/curtail
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk4-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
# Note: Needs libadwaita's AboutWindow which is only available from version 1.2
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2
Requires:       jpegoptim
Requires:       libwebp-tools
Requires:       optipng
Requires:       pngquant
Requires:       python3-gobject-Gdk
BuildArch:      noarch

%description
Curtail (previously ImCompressor) is an useful image compressor, supporting
PNG, JPEG and WEBP file types. It support both lossless and lossy compression
modes with an option to whether keep or not metadata of images.

%lang_package

%prep
%setup -q -n Curtail-%{version}

%build
%meson
%meson_build

%suse_update_desktop_file com.github.huluti.Curtail RasterGraphics

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/curtail
%{_datadir}/metainfo/*.xml
%{_datadir}/curtail/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/*.svg

%files lang -f %{name}.lang

%changelog
