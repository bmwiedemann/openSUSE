#
# spec file for package wayprompt
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


Name:           wayprompt
Version:        0.1.2
Release:        0
Summary:        Multi-purpose prompt tool for Wayland
License:        GPL-3.0-only
URL:            https://git.sr.ht/~leon_plickat/wayprompt/
Source0:        https://git.sr.ht/~leon_plickat/wayprompt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  fdupes
BuildRequires:  scdoc
BuildRequires:  zig = 0.13.0
BuildRequires:  zig-rpm-macros = 0.13.0
BuildRequires:  zstd
BuildRequires:  pkgconfig(fcft)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-server) >= 1.20.0
BuildRequires:  pkgconfig(xkbcommon)

Provides:       pinentry-wayprompt = %{version}

%description
Multi-purpose prompt tool for Wayland

To use as a pinentry replacement, run as 'pinentry-wayprompt'.
To use as a himitsu prompter, run as 'hiprompt-wayprompt'. (TODO)
To use as a generic prompter for scripts, run as 'wayprompt-cli'.

%prep
%autosetup -a1 -p1 -n %{name}-v%{version}

%build
%zig_build -Dpie --global-cache-dir vendor/

%install
%zig_install -Dpie --global-cache-dir vendor/
%fdupes %{buildroot}

%files
%{_bindir}/%{name}
%{_bindir}/pinentry-%{name}
%{_bindir}/%{name}-ssh-askpass
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-ssh-askpass.1%{?ext_man}
%{_mandir}/man1/pinentry-%{name}.1%{?ext_man}
%{_mandir}/man5/%{name}.5%{?ext_man}
%doc README.md
%license LICENSE

%changelog
