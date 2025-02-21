#
# spec file for package wlopm
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


Name:           wlopm
Version:        1.0.0
Release:        0
Summary:        Wayland output power management
License:        GPL-3.0-only
URL:            https://git.sr.ht/~leon_plickat/wlopm
Source0:        https://git.sr.ht/~leon_plickat/wlopm/archive/v%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  pkgconfig(wayland-client)

%description
Simple client implementing zwlr-output-power-management-v1. Helps
turning off screen output e.g. laptops after closing the lid
and turning it on e.g. laptops after opening the lid

%prep
%autosetup -n %{name}-v%{version}

%build
%make_build PREFIX="/usr" CFLAGS="%{optflags} $(pkg-config --cflags wayland-client)"

%install
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
%make_install PREFIX=/usr

%files
%license LICENSE
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/bash-completion/completions/wlopm

%changelog
