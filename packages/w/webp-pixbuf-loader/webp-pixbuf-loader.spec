#
# spec file for package webp-pixbuf-loader
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


Name:           webp-pixbuf-loader
Version:        0.0.6
Release:        0
Summary:        WebP GDK Pixbuf Loader library
License:        LGPL-2.0-or-later
URL:            https://github.com/aruiz/webp-pixbuf-loader
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gdk-pixbuf-thumbnailer
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) > 2.22.0
BuildRequires:  pkgconfig(libwebp)
Requires:       gdk-pixbuf-query-loaders
Requires:       gdk-pixbuf-thumbnailer
%gdk_pixbuf_loader_requires

%description
webp-pixbuf-loader is a plugin to allow loading WebP images in GTK+ applications.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%post
%gdk_pixbuf_loader_post

%postun
%gdk_pixbuf_loader_postun

%files
%license LICENSE.LGPL-2
%doc README.md
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libpixbufloader-webp.so
%{_datadir}/thumbnailers/webp-pixbuf.thumbnailer

%changelog
