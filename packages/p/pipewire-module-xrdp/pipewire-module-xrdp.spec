#
# spec file for package pipewire-module-xrdp
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%define scmt    2d47559
%define fcmt    2d47559d708a93a65cc401aefa4f1f85b4fd0054
Name:           pipewire-module-xrdp
Version:        0.2
Release:        0
Summary:        Enable xrdp to generate sound with pipewire
License:        MIT
URL:            https://github.com/neutrinolabs/pipewire-module-xrdp
Source:         https://github.com/neutrinolabs/%{name}/archive/%{scmt}.tar.gz#/%{name}-%{scmt}.tar.gz
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.58

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
%{_libdir}/pipewire-0.3/lib%{name}.so

%changelog
