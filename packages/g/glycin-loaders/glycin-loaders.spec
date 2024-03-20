#
# spec file for package glycin-loaders
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


%bcond_without jxl

Name:           glycin-loaders
Version:        1.0.0
Release:        0
Summary:        Sandboxed image rendering
License:        LGPL-2.1-or-later OR MPL-2.0
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst

BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig
%if %{with jxl}
BuildRequires:  (pkgconfig(libjxl) >= 0.8.2 with pkgconfig(libjxl) < 0.11.0)
%endif
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk4) >= 4.12.0
BuildRequires:  pkgconfig(libheif) >= 1.17.4
BuildRequires:  pkgconfig(libseccomp) >= 2.5.0
BuildRequires:  pkgconfig(libxml-2.0)

%description
Sandboxed and extendable image decoding.

%prep
%autosetup -p1 -a1

%build
export RUSTFLAGS="%{build_rustflags}"
%meson \
	-Dloaders=glycin-heif,glycin-image-rs,glycin-svg%[%{with jxl}?",glycin-jxl":""] \
	%{nil}
%meson_build

%install
export RUSTFLAGS="%{build_rustflags}"
%meson_install

%files
%dir %{_libexecdir}/glycin-loaders
%dir %{_libexecdir}/glycin-loaders/1+
%{_libexecdir}/glycin-loaders/1+/glycin-heif
%{_libexecdir}/glycin-loaders/1+/glycin-image-rs
%{_libexecdir}/glycin-loaders/1+/glycin-svg
%dir %{_datadir}/glycin-loaders
%dir %{_datadir}/glycin-loaders/1+
%dir %{_datadir}/glycin-loaders/1+/conf.d
%{_datadir}/glycin-loaders/1+/conf.d/glycin-heif.conf
%{_datadir}/glycin-loaders/1+/conf.d/glycin-image-rs.conf
%{_datadir}/glycin-loaders/1+/conf.d/glycin-svg.conf
%if %{with jxl}
%{_libexecdir}/glycin-loaders/1+/glycin-jxl
%{_datadir}/glycin-loaders/1+/conf.d/glycin-jxl.conf
%endif

%changelog
