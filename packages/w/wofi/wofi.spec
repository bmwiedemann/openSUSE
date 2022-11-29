#
# spec file for package wofi
#
# Copyright (c) 2022 SUSE LLC
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


Name:           wofi
Version:        1.3
Release:        0
Summary:        Launcher for wlroots compositors
License:        GPL-3.0-only
URL:            https://hg.sr.ht/~scoopta/wofi
Source:         https://hg.sr.ht/~scoopta/wofi/archive/v%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wayland-client)

%description
Wofi is a launcher/menu program for wlroots based wayland compositors such as sway.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Headers for the wofi API which are needed to build wofi plugins.

%prep
%autosetup -p1 -n wofi-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.md
%doc README.md
%{_bindir}/wofi
%{_mandir}/man?/%{name}*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}*

%changelog
