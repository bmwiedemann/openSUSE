#
# spec file for package foot
#
# Copyright (c) 2021 SUSE LLC
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


Name:           foot
Version:        1.8.1
Release:        0
Summary:        A Wayland terminal emulator
License:        MIT
URL:            https://codeberg.org/dnkl/foot
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  pkgconfig(fcft) < 3.0.0
BuildRequires:  pkgconfig(fcft) >= 2.4.0
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(tllist) >= 1.0.4
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon) >= 1.0.0

%description
A Wayland terminal emulator.

%prep
%autosetup -n %{name}

%build
%meson -Db_lto=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/foot
%{_bindir}/footclient
%{_datadir}/applications/foot.desktop
%{_datadir}/applications/foot-server.desktop
%{_datadir}/bash-completion/
%{_datadir}/doc/%{name}/
%{_datadir}/fish/
%{_datadir}/zsh/
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/
%{_datadir}/terminfo/f/foot
%{_datadir}/terminfo/f/foot-direct
%{_mandir}/man1/foot.1.gz
%{_mandir}/man1/footclient.1.gz
%{_mandir}/man5/foot.ini.5.gz
%{_mandir}/man7/foot-ctlseqs.7.gz

%changelog
