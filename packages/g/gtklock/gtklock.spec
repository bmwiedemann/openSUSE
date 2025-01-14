#
# spec file for package gtklock
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


Name:           gtklock
Version:        4.0.0
Release:        0
Summary:        GTK-based lockscreen for Wayland
License:        GPL-3.0-only
URL:            https://github.com/jovanlanik/gtklock
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  libjson-c-devel
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  scdoc
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-session-lock-0)
BuildRequires:  pkgconfig(wayland-client)

%lang_package

%description
gtklock is a lockscreen based on gtkgreet.
It uses the wlr-layer-shell and wlr-input-inhibitor Wayland protocols.
Works on sway and other wlroots-based compositors.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
# distro provided pam files should be in _pam_vendordir
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/* %{buildroot}%{_pam_vendordir}/
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_pam_vendordir}/gtklock
%{_bindir}/gtklock
%{_mandir}/man1/gtklock.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
