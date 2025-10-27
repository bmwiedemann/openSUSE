#
# spec file for package glycin
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define flavor @BUILD_FLAVOR@
%if "%{flavor}" == ""
Name:           glycin
ExclusiveArch:  do-not-build
%else
Name:           %{flavor}
%endif
%define _name glycin

Version:        2.0.4
Release:        0
Summary:        Sandboxed image rendering
License:        LGPL-2.1-or-later OR MPL-2.0
URL:            https://gitlab.gnome.org/GNOME/glycin
Source0:        %{_name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        baselibs.conf
Source90:       libglycin.spec.inc
Source91:       libglycin-gtk4.spec.inc
Source92:       glycin-loaders.spec.inc

BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libseccomp)
%if "%{name}" == "glycin-loaders"
BuildRequires:  (pkgconfig(libjxl) >= 0.8.2 with pkgconfig(libjxl) < 0.13.0)
BuildRequires:  pkgconfig(libheif) >= 1.17.4
BuildRequires:  pkgconfig(librsvg-2.0)
Requires:       bubblewrap
Obsoletes:      gdk-pixbuf-loader-rsvg <= 2.60.0
Provides:       gdk-pixbuf-loader-rsvg
Obsoletes:      rsvg-thumbnailer <= 2.60.0
Provides:       rsvg-thumbnailer
%endif

%description
Sandboxed and extendable image decoding.

%include %{_sourcedir}/%{name}.spec.inc

%changelog
