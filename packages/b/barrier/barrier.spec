#
# spec file for package barrier
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 Christian Mauderer <oss@c-mauderer.de>.
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


Name:           barrier
Version:        2.3.3
Release:        0
Summary:        Mouse, keyboard and clipboard sharing utility
License:        GPL-2.0-or-later
URL:            https://github.com/debauchee/barrier
Source0:        https://github.com/debauchee/barrier/archive/v%{version}/%{name}-%{version}.tar.gz
Source2:        barriers.socket
Source3:        barriers.service
#PATCH-FIX-OPENSUSE barrier-use-system-includes.patch malcolmlewis@opensuse.org -- Use the system gtest and gmock files for testing.
Patch0:         barrier-use-system-includes.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xtst)
#Provides:       synergy = %%{version}
#Obsoletes:      synergy < %%{version}
%{?systemd_ordering}

%description
Barrier lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware.  It's intended for users with
multiple computers on their desk since each system uses its own
display.

Redirecting the mouse and keyboard is as simple as moving the mouse off
the edge of your screen.  Barrier also merges the clipboards of all the
systems into one, allowing cut-and-paste between systems. Furthermore,
it synchronizes screen savers so they all start and stop together and,
if screen locking is enabled, only one screen requires a password to
unlock them all.

%prep
%autosetup -p1
# not enough categories in the desktop file
sed -i -e 's:Utility;:Utility;DesktopUtility;:g' res/barrier.desktop

%build
export BARRIER_VERSION_STAGE="release"
%cmake \
  -DBARRIER_BUILD_INSTALLER=OFF
%cmake_build

%install
%cmake_install

# Configuration
install -D -m0644 doc/barrier.conf.example "%{buildroot}%{_sysconfdir}/barrier.conf"

# Unit file
install -Dm 644 %{SOURCE2} %{buildroot}%{_unitdir}/barriers.socket
install -Dm 644 %{SOURCE3} %{buildroot}%{_unitdir}/barriers.service
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rcbarriers

# GUI package
install -D -m0644 res/barrier.desktop "%{buildroot}%{_datadir}/applications/barrier.desktop"
install -D -m0644 res/barrier.svg "%{buildroot}%{_datadir}/pixmaps/barrier.svg"
install -D -m0644 res/barrier.png "%{buildroot}%{_datadir}/pixmaps/barrier.png"
%suse_update_desktop_file -i %{name}

%post
%fillup_only
%service_add_post barriers.service barriers.socket

%postun
%service_del_postun barriers.service barriers.socket

%pre
%service_add_pre barriers.service barriers.socket

%preun
%service_del_preun barriers.service barriers.socket

%files
%doc ChangeLog debian/changelog
%config(noreplace) %{_sysconfdir}/barrier.conf
%{_bindir}/barrier
%{_bindir}/barrierc
%{_bindir}/barriers
%{_unitdir}/barriers.service
%{_unitdir}/barriers.socket
%{_sbindir}/rcbarriers
%{_datadir}/applications/barrier.desktop
%{_datadir}/pixmaps/barrier.png
%{_datadir}/pixmaps/barrier.svg
%license LICENSE

%changelog
