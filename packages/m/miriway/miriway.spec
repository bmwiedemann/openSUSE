#
# spec file for package miriway
#
# Copyright (c) 2024 Neal Gompa
# Copyright (c) 2024 Shawn W Dunn
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
%define _name Miriway

Name:           miriway
Version:        24.11
Release:        0
Summary:        Simple Wayland compositor built on Mir
License:        GPL-3.0
URL:            https://github.com/Miriway/Miriway
Source:         https://github.com/%{_name}/%{_name}/archive/v%{version}/%{_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE 0001-Fix-xkbcommon-includes.patch
Patch0:         0001-Fix-xkbcommon-includes.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig(miral) >= 5.1
BuildRequires:  pkgconfig(xkbcommon)
Requires:       inotify-tools
Requires:       xkeyboard-config
Requires:       xwayland

%description
Miriway is a starting point for creating a Wayland based
desktop environment using Mir.

%package        session
Summary:        Miriway desktop session
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    session
This package contains configuration and dependencies for the basic Miriway
session

%package -n sddm-wayland-%{name}
Summary:        Miriway SDDM greeter configuration
Requires:       %{name} = %{version}
Requires:       layer-shell-qt6
Requires:       sddm-kalpa
Supplements:    (sddm and %{name})
BuildArch:      noarch

%description -n sddm-wayland-%{name}
This package contains configuration and dependencies for the initial-setup
GUI to use Miriway for the Wayland Compositor.

%prep
%autosetup -n %{_name}-%{version} -S git_am

# Drop -Werror
sed -e "s/-Werror//g" -i CMakeLists.txt

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DSDDM=ON
%cmake_build

%install
%cmake_install

# Remove miriway-unsnap as it's kind of pointless on openSUSE distros
rm -r %{buildroot}%{_bindir}/%{name}-unsnap

# move sddm configuration snippet to the right place
mkdir -p %{buildroot}%{_prefix}/lib/sddm
mv %{buildroot}/%{_sysconfdir}/sddm.conf.d %{buildroot}%{_prefix}/lib/sddm

%check
%ctest

%files
%license LICENSE
%doc README.md CONFIGURING_MIRIWAY.md example-configs
%{_bindir}/%{name}*
%dir %{_sysconfdir}/xdg/xdg-%{name}
%config(noreplace) %{_sysconfdir}/xdg/xdg-%{name}/%{name}-shell.config

%files session
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/%{name}.desktop
%{_prefix}/lib/systemd/user/%{name}-session.target
%{_libexecdir}/%{name}-session-*

%files -n sddm-wayland-%{name}
%dir %{_prefix}/lib/sddm
%dir %{_prefix}/lib/sddm/sddm.conf.d
%{_prefix}/lib/sddm/sddm.conf.d/%{name}.conf


%changelog

