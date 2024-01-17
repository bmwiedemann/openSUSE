#
# spec file for package kmscon
#
# Copyright (c) 2022 SUSE LLC
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
Version:        9.0.0
Release:        0
Summary:        Linux KMS/DRM based virtual Console Emulator
License:        MIT
Group:          System/Console
URL:            https://github.com/Aetf/kmscon/
Source:         https://github.com/Aetf/kmscon/releases/download/v%version/kmscon-%version.tar.xz
Patch1:         kmscon-no-date-time.patch
Patch2:         0001-Use-correct-systemd-system-unit-directory.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libtsm-devel >= 4.0.2
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  xsltproc
BuildRequires:  xz
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
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
%meson
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
%{_libdir}/kmscon/
%dir %{_libexecdir}/kmscon
%{_libexecdir}/kmscon/kmscon
%{_mandir}/man1/kmscon.1%{?ext_man}
%{_unitdir}/*.service

%changelog
