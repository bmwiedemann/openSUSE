#
# spec file for package glycin-loaders
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


Name:           glycin-loaders
Version:        0.1.1
Release:        0
Summary:        Sandboxed image rendering
License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        %{name}-%{version}.tar.zst
Source2:        vendor.tar.zst
Source3:        cargo_config

BuildRequires:  cargo-packaging
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Sandboxed and extendable image decoding.

%prep
%autosetup -p1 -a2
mkdir .cargo
cp %{SOURCE3} .cargo/config

%build
export RUSTFLAGS="%{build_rustflags}"
%meson \
	-Dloaders=glycin-heif,glycin-image-rs,glycin-jxl,glycin-svg \
	%{nil}
%meson_build

%install
export RUSTFLAGS="%{build_rustflags}"
%meson_install

%files
%dir %{_libexecdir}/glycin-loaders
%dir %{_libexecdir}/glycin-loaders/0+
%{_libexecdir}/glycin-loaders/0+/glycin-heif
%{_libexecdir}/glycin-loaders/0+/glycin-image-rs
%{_libexecdir}/glycin-loaders/0+/glycin-jxl
%{_libexecdir}/glycin-loaders/0+/glycin-svg
%dir %{_datadir}/glycin-loaders
%dir %{_datadir}/glycin-loaders/0+
%dir %{_datadir}/glycin-loaders/0+/conf.d
%{_datadir}/glycin-loaders/0+/conf.d/glycin-heif.conf
%{_datadir}/glycin-loaders/0+/conf.d/glycin-image-rs.conf
%{_datadir}/glycin-loaders/0+/conf.d/glycin-jxl.conf
%{_datadir}/glycin-loaders/0+/conf.d/glycin-svg.conf

%changelog
