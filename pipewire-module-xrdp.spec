#
# spec file for package pipewire-module-xrdp
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


# Short and full commit hashes.
%define scmt    e9c6c05
%define fcmt    e9c6c05dd4327fca43d8861535c1f75c9b258aef
Name:           pipewire-module-xrdp
Version:        0~git19
Release:        0
Summary:        Enable xrdp to generate sound with pipewire
License:        MIT
URL:            https://github.com/neutrinolabs/pipewire-module-xrdp
Source:         https://github.com/neutrinolabs/%{name}/archive/%{scmt}.tar.gz#/%{name}-%{scmt}.tar.gz
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.58
BuildRequires:  update-desktop-files

%description
This module allows xrdp to generate sound on a pipewire-based system.

%prep
%autosetup -n %{name}-%{fcmt}

%build
./bootstrap
%configure --disable-static
%make_build

%install
%make_install
%suse_update_desktop_file pipewire-xrdp
rm -f %{buildroot}%{_libdir}/pipewire-0.3/*.la

%files
%license LICENSE
%doc README.md
%config %{_sysconfdir}/xdg/autostart/pipewire-xrdp.desktop
%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/load_pw_modules.sh
%{_libdir}/pipewire-0.3/lib%{name}-pipewire.so

%changelog
