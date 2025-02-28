#
# spec file for package kmscon
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 Adam Mizerski <adam@mizerski.pl>
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


Name:           kmscon
Version:        9.0.0+git42
Release:        0
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
Group:          System/Console
URL:            https://github.com/Aetf/kmscon/
Source:         %{name}-%{version}.tar.xz
Patch1:         kmscon-no-date-time.patch
# https://github.com/Aetf/kmscon/pull/103
Patch2:         0001-Fix-systemd-monitor-initialization.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libtsm-devel >= 4.0.2+git24
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  xsltproc
BuildRequires:  xz
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
# O/P added for 13.1
Obsoletes:      %{name}-service < %{version}-%{release}
Provides:       %{name}-service = %{version}-%{release}

%description
Kmscon is a simple terminal emulator based on linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a userspace
console.

%prep
%autosetup -p1

%build
# Work around https://github.com/Aetf/kmscon/issues/63
export CFLAGS="%{optflags} $(pkg-config xkbcommon --cflags) $(pkg-config libtsm --cflags) -Wno-error"
# Disable unifont, too fat ATM (https://github.com/Aetf/kmscon/issues/102)
# Disable 3D renderer, pulls in a dependency on Mesa into the main binary
%meson -Dtests=false -Dfont_unifont=disabled -Drenderer_gltex=disabled -Dvideo_drm3d=disabled
%meson_build

%install
%meson_install

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%{_bindir}/%{name}
%dir %{_libdir}/kmscon/
%{_libdir}/kmscon/mod-bbulk.so
%{_libdir}/kmscon/mod-pango.so
%{_libdir}/kmscon/mod-pixman.so
#%{_libdir}/kmscon/mod-unifont.so
%dir %{_libexecdir}/kmscon
%{_libexecdir}/kmscon/kmscon
%{_mandir}/man1/kmscon.1%{?ext_man}
%{_unitdir}/*.service

%changelog
