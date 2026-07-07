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
Version:        10.0.1
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
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtsm) >= 4.6.0
BuildRequires:  pkgconfig(libudev) >= 172
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  rpm_macro(_pam_vendordir)
# O/P added for 13.1
Obsoletes:      %{name}-service < %{version}-%{release}
Provides:       %{name}-service = %{version}-%{release}

%description
Kmscon is a simple terminal emulator based on linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a userspace
console.

%package pango
Summary:        Pango renderer for kmscon
Requires:       %{name} = %{version}

%description pango
This package contains an optional renderer backend for kmscon using the pango
library for advanced text layout and rendering.

By default, kmscon uses the freetype renderer, so only special configurations
need to install this package and its dependencies.

%prep
%autosetup -p1

%build
# Disable 3D renderer, pulls in a dependency on Mesa into the main binary
# Use TERM=linux for the time being (https://github.com/kmscon/kmscon/issues/411)
%meson -Dtests=false -Dlibseat=enabled -Dterm=linux -Drenderer_gltex=disabled -Dvideo_drm3d=disabled
%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/kmscon %{buildroot}%{_pam_vendordir}/kmscon

# Remove example config from /etc, we use %%doc
rm %{buildroot}%{_sysconfdir}/kmscon/kmscon.conf.example

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
%{_libdir}/kmscon/mod-freetype.so
%{_libdir}/kmscon/mod-unifont.so
%{_mandir}/man1/kmscon.1%{?ext_man}
%{_mandir}/man5/kmscon.conf.5%{?ext_man}
%{_unitdir}/kmscon.service
%{_unitdir}/kmsconvt@.service
%{_pam_vendordir}/kmscon

%files pango
%{_libdir}/kmscon/mod-pango.so

%changelog
