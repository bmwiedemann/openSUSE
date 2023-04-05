#
# spec file for package foot
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


Name:           foot
Version:        1.14.0
Release:        0
Summary:        A Wayland terminal emulator
License:        MIT
URL:            https://codeberg.org/dnkl/foot
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       terminfo
Requires:       utempter
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  scdoc
BuildRequires:  utempter-devel
BuildRequires:  pkgconfig(fcft) < 4.0.0
BuildRequires:  pkgconfig(fcft) >= 3.0.1
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(tllist) >= 1.0.4
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon) >= 1.0.0

%description
A Wayland terminal emulator.

%package extra-terminfo

Summary:        Extra terminfo files for the foot terminal emulator
BuildArch:      noarch

%description extra-terminfo
This package contains extra terminfo files for the foot terminal emulator
that provide more features than the files in the terminfo-base package.
Set term=foot-extra or term=foot-extra-direct in foot.ini to
take advantage of the files in this package.

%package themes

Summary:        Community-contributed themes for the foot terminal emulator
Requires:       foot
BuildArch:      noarch

%description themes
This package contains popular themes for the foot terminal emulator providing
users an easy way to theme foot.

%prep
%autosetup -n %{name}

%build
%meson \
	--sysconfdir "%{_distconfdir}" \
	-Db_lto=true \
	-Ddocs=enabled \
	-Dgrapheme-clustering=enabled \
	-Dime=true \
	-Dterminfo=enabled \
	-Dtests=false \
	-Dthemes=true
%meson_build

%install
%meson_install
rm -r %{buildroot}/%{_datadir}/doc/%{name}/
mv %{buildroot}/%{_datadir}/terminfo/f/foot %{buildroot}/%{_datadir}/terminfo/f/foot-extra
mv %{buildroot}/%{_datadir}/terminfo/f/foot-direct %{buildroot}/%{_datadir}/terminfo/f/foot-extra-direct

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/foot
%{_bindir}/footclient
%{_datadir}/applications/org.codeberg.dnkl.foot.desktop
%{_datadir}/applications/org.codeberg.dnkl.footclient.desktop
%{_datadir}/applications/org.codeberg.dnkl.foot-server.desktop
%{_datadir}/bash-completion/
%{_datadir}/fish/
%{_datadir}/zsh/
%{_datadir}/icons/hicolor/
%dir %{_distconfdir}/xdg/%{name}
%{_distconfdir}/xdg/%{name}/foot.ini
%{_mandir}/man1/foot.1.gz
%{_mandir}/man1/footclient.1.gz
%{_mandir}/man5/foot.ini.5.gz
%{_mandir}/man7/foot-ctlseqs.7.gz
%{_userunitdir}/foot-server@.service
%{_userunitdir}/foot-server@.socket

%files extra-terminfo
%{_datadir}/terminfo/f/foot-extra
%{_datadir}/terminfo/f/foot-extra-direct

%files themes
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes

%changelog
