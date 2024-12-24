#
# spec file for package lxqt-session
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Shawn W Dunn <sfalken@opensuse.org>
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


Name:           lxqt-session
Version:        2.1.1
Release:        0
Summary:        LXQt Session Manager
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://github.com/lxqt/lxqt-session
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# mvetter@suse.com bsc#1127043 - Use Openbox as default WM
Patch1:         %{name}-default_wm.patch
BuildRequires:  cmake >= 3.18.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qtxdg-tools >= 4.1.0
BuildRequires:  xdg-user-dirs
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt) >= 6.0.0
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(qtxdg-tools)
BuildRequires:  pkgconfig(libproc2) >= 4.0.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lxqt) >= 2.1.0
BuildRequires:  pkgconfig(x11)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       %{name}-branding = %{version}-%{release}
Requires:       qtxdg-tools
Recommends:     %{name}-lang = %{version}-%{release}

%description
lxqt-session is the standard session manager used by LXQt. The lxqt-session manager
is used to automatically start a set of applications and set up a working desktop
environment. Moreover, the session manager is able to remember the applications in
use when a user logs out and to restart them the next time the user logs in.

%lang_package

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/GUI/LXQt
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for %{name}.

%prep
%autosetup -p1
sed -i 's/^\(Type=\).*/\1XSession/' xsession/lxqt.desktop.in
sed -i '/^Categories/s/\(LXQt\;\)/X-\1/' lxqt-config-session/lxqt-config-session.desktop.in

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}
%fdupes -s %{buildroot}%{_datadir}
install -Dm 0644 %{buildroot}%{_datadir}/lxqt/{lxqt,session,windowmanagers,waylandwindowmanagers}.conf -t %{buildroot}%{_sysconfdir}/xdg/lxqt/

# for default-xsession
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%find_lang %{name} --with-qt --all-name

%check
%ctest

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/lxqt.desktop 20

%postun
[ -f %{_datadir}/xsessions/lxqt.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/lxqt.desktop

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_bindir}/lxqt-config-session
%{_bindir}/%{name}
%{_bindir}/lxqt-leave
%{_datadir}/applications/lxqt-*.desktop
%{_mandir}/man?/lxqt-*%{?ext_man}
%config %{_sysconfdir}/xdg/autostart/lxqt-xscreensaver-autostart.desktop
%{_bindir}/startlxqt
%{_mandir}/man1/startlxqt.1%{?ext_man}
%{_datadir}/xsessions/lxqt.desktop
%{_datadir}/lxqt/lxqt.conf
%{_datadir}/lxqt/session.conf
%{_datadir}/lxqt/windowmanagers.conf
%{_datadir}/lxqt/waylandwindowmanagers.conf

# for default-xsession
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/default.desktop
%{_datadir}/xsessions/default.desktop

%files branding-upstream
%dir %{_sysconfdir}/xdg/
%dir %{_sysconfdir}/xdg/lxqt/
%config %{_sysconfdir}/xdg/lxqt/lxqt.conf
%config %{_sysconfdir}/xdg/lxqt/session.conf
%config %{_sysconfdir}/xdg/lxqt/windowmanagers.conf
%config %{_sysconfdir}/xdg/lxqt/waylandwindowmanagers.conf

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%dir %{_datadir}/lxqt/translations/lxqt-config-session
%dir %{_datadir}/lxqt/translations/lxqt-leave
%dir %{_datadir}/lxqt/translations/%{name}

%changelog
