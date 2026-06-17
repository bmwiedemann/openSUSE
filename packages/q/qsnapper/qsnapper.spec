#
# spec file for package qsnapper
#
# Copyright (c) 2026 Shawn W Dunn <sfalken@opensuse.org>
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
%global rname qSnapper
%global selinuxtype targeted

Name:           qsnapper
Version:        1.3.3
Release:        0
Summary:        Qt Gui application for managing btrfs snapshots
License:        GPL-3.0-or-later
URL:            https://github.com/presire/qSnapper
Source:         %{url}/archive/v%{version}/%{rname}-%{version}.tar.gz

# PATCH-FIX-UPSTREAM
Patch0:         0001-improve-translation-installation.patch


BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libsnapper-devel
BuildRequires:  policycoreutils
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6DBus)

BuildRequires:  pkgconfig(libbtrfsutil)

%description
qSnapper is a graphical user interface for the Snapper snapshot management
tool. It provides an intuitive way to create, browse, and manage filesystem
snapshots on Btrfs and other supported filesystems.

%package selinux
Summary:        SELinux module for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
Requires(post): policycoreutils
Requires(preun): policycoreutils

%description selinux
This package provides the SELinux policy module to ensure qsnapper
runs properly under an environment with SELinux enabled.



%prep
%autosetup -C -p1

%conf
%cmake_qt6 \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_SKIP_BUILD_RPATH=ON \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DENABLE_SELINUX=ON

%build
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%post
%tmpfiles_create %{_tmpfilesdir}/qsnapper.conf

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{name}.pp

%postun selinux
if [ $1 -eq 0 ]; then
  %selinux_modules_uninstall -s %{selinuxtype} %{name}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%license LICENSE.md Licenses/*
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_libexecdir}/%{name}-dbus-service
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/system-services/com.presire.%{name}.Operations.service
%{_datadir}/dbus-1/system.d/com.presire.%{name}.Operations.conf
%{_datadir}/icons/hicolor/*/apps/%{rname}.png
%{_datadir}/polkit-1/actions/com.presire.%{name}.policy
%{_tmpfilesdir}/qsnapper.conf
%ghost %dir %attr(0700,root,root) %{_localstatedir}/log/qsnapper

%files selinux
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/selinux/
%{_datadir}/selinux/packages/%{name}.pp
%dnl %{_datadir}/selinux/devel/include/distributed/

%changelog

