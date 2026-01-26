#
# spec file for package kmscon
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        9.3.0+git1
Release:        0
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
Group:          System/Console
URL:            https://github.com/kmscon/kmscon
Source:         %{name}-%{version}.tar.xz
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtsm) >= 4.4.0
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
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
# Disable 3D renderer, pulls in a dependency on Mesa into the main binary
%meson -Dtests=false -Drenderer_gltex=disabled -Dvideo_drm3d=disabled
%meson_build

%install
%meson_install

# Remove example config from /etc, we use %%doc
rm %{buildroot}/%{_sysconfdir}/kmscon/kmscon.conf.example

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
%doc scripts/etc/kmscon.conf.example
%{_bindir}/%{name}
%{_bindir}/%{name}-launch-gui
%dir %{_libdir}/kmscon/
%{_libdir}/kmscon/mod-pango.so
%{_libdir}/kmscon/mod-unifont.so
%dir %{_libexecdir}/kmscon
%{_libexecdir}/kmscon/kmscon
%{_mandir}/man1/kmscon.1%{?ext_man}
%{_mandir}/man1/kmscon.conf.1%{?ext_man}
%{_unitdir}/kmscon.service
%{_unitdir}/kmsconvt@.service

%changelog
