#
# spec file for package budgie-wayland-session
#
# Copyright (c) 2025 SUSE LLC
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


Name:           budgie-wayland-session
Version:        0.0.0+10
Release:        0
Summary:        Budgie Magpie v1 Wayland Session
License:        MPL-2.0
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/budgie-wayland-session
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  sddm-qt6
Requires:       (sddm-qt6 or sddm)
Requires:       (layer-shell-qt6 if sddm-qt6)
Requires:       (layer-shell-qt5 if sddm)
Requires:       (qt6-wayland if sddm-qt6)
Requires:       (libqt5-qtwayland if sddm)
Requires:       magpie-1
# Future move to labwc
Provides:       budgie-session-manager = %{version}
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
This package contains the scripts and data files for setting up the
Budgie Desktop to run in a Wayland environment.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-waylandsession.desktop
ln -s %{_sysconfdir}/alternatives/default-waylandsession.desktop %{buildroot}%{_datadir}/wayland-sessions/default.desktop

%post
%{_sbindir}/update-alternatives --install %{_datadir}/wayland-sessions/default.desktop \
  default-waylandsession.desktop %{_datadir}/wayland-sessions/budgie-desktop-wayland.desktop 20

%postun
[ -f %{_datadir}/wayland-sessions/budgie-desktop-wayland.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-waylandsession.desktop %{_datadir}/wayland-sessions/budgie-desktop-wayland.desktop

%files
%{_prefix}/lib/sddm/sddm.conf.d/*
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/budgie-desktop-wayland.desktop
%{_datadir}/wayland-sessions/default.desktop
%ghost %{_sysconfdir}/alternatives/default-waylandsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop

%changelog
