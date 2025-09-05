# spec file for package sdgyrodsu
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

Name:           sdgyrodsu
Version:        2.1.1
Release:        0%{?dist}
Summary:        DSU server for motion data running on Steam Deck
License:        MIT
URL:            https://github.com/kmicki/SteamDeckGyroDSU
Source:         https://github.com/kmicki/SteamDeckGyroDSU/archive/refs/tags/v%version.tar.gz
Patch0:         rpm.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRequires:  libhidapi-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
Provides:       SteamDeckGyroDSU = %{version}

%description
This package provides the DSU (cemuhook protocol)
server for motion data running on the Steam Deck.

%prep
%autosetup -p0 -n SteamDeckGyroDSU-%{version}

%build
%set_build_flags
%make_build

%install
install -Dsm 755 bin/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 pkg/%{name}.service %{buildroot}%{_userunitdir}/%{name}.service

%pre
%systemd_user_pre %{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service


%files
%license LICENSE
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
