#
# spec file for package power-profiles-daemon
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


Name:           power-profiles-daemon
Version:        0.23
Release:        0
Summary:        Power profiles handling over D-Bus
License:        GPL-3.0-or-later
URL:            https://gitlab.freedesktop.org/upower/power-profiles-daemon
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE hold-profile-hardening.patch boo#1189900 -- Hardening of HoldProfile D-Bus method
Patch0:         hold-profile-hardening.patch
BuildRequires:  c_compiler
BuildRequires:  cmake
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  python3-argparse-manpage
BuildRequires:  python3-dbusmock
BuildRequires:  python3-shtab
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gudev-1.0) >= 234
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.91
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(umockdev-1.0)
BuildRequires:  pkgconfig(upower-glib)
Requires:       polkit
Requires:       python3-gobject
Conflicts:      ppd-service
Provides:       ppd-service

%description
power-profiles-daemon offers to modify system behaviour based upon user-selected
power profiles. There are 3 different power profiles: a "balanced" default mode,
a "power-saver" mode, and a "performance" mode.

%package doc
Summary:        Documentation for power-profiles-daemon
BuildArch:      noarch

%description doc
This package provides documentation for %{name}.

%package -n powerprofilesctl-bash-completion
Summary:        Bash completion for powerprofilesctl
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n powerprofilesctl-bash-completion
This package provides bash shell completions for powerprofilesctl.

%package -n powerprofilesctl-zsh-completion
Summary:        Zsh shell completion for powerprofilesctl
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n powerprofilesctl-zsh-completion
This package provides zsh shell completions for powerprofilesctl.

%prep
%autosetup -p1

%build
%meson \
	-Dsystemdsystemunitdir=%{_unitdir} \
	-Dgtk_doc=true \
	-Dpylint=disabled \
	-Dtests=true \
	-Dzshcomp=%{_datadir}/zsh/site-functions/ \
	%{nil}
%meson_build

%install
%meson_install
%{python3_fix_shebang}

%check
%meson_test

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc README.md
%{_bindir}/powerprofilesctl
%{_libexecdir}/%{name}
%{_unitdir}/%{name}.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/polkit-1/actions/power-profiles-daemon.policy
%{_mandir}/man1/powerprofilesctl.1%{?ext_man}
%ghost %dir %{_localstatedir}/lib/%{name}

%files doc
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%files -n powerprofilesctl-bash-completion
%{_datadir}/bash-completion/completions/*

%files -n powerprofilesctl-zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/*

%changelog
