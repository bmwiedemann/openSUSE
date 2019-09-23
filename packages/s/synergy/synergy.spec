#
# spec file for package synergy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# since Nov 2017 synergy FOSS core is called synergy-core
%define synergy synergy-core
Name:           synergy
Version:        1.9.1
Release:        0
Summary:        Mouse, keyboard and clipboard sharing utility
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            http://synergy-project.org/
Source0:        https://github.com/symless/synergy-core/archive/v%{version}-stable.tar.gz
Source2:        qsynergy.desktop
Source3:        qsynergy.png
Source4:        synergys.socket
Source5:        synergys.service
# The test suite uses an incompatible Apache-2.0 license
# https://build.opensuse.org/request/show/616454
Patch1:         legal-disable-tests.patch
# PATCH-FIX-UPSTREAM add-support-for-latin-s-and-t-with-comma-below.patch
Patch2:         add-support-for-latin-s-and-t-with-comma-below.patch
# PATCH-FIX-UPSTREAM qt5_fixes.patch
Patch3:         qt5_fixes.patch
# patches from Gentoo (taken from Mageia)
Patch11:        synergy-1.5.0-pthread.patch
Patch14:        synergy-1.5.0-disable-version-check.patch
BuildRequires:  avahi-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  mDNSResponder-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xtst)
Provides:       %{synergy} = %{version}
Obsoletes:      %{synergy} < %{version}
%{?systemd_requires}
%if 0%{?suse_version} != 1315
BuildRequires:  libcryptopp-devel
Requires(pre):  %fillup_prereq
Provides:       synergy-plus = %{version}
Obsoletes:      synergy-plus < %{version}
%endif

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware.  It's intended for users with
multiple computers on their desk since each system uses its own
display.

Redirecting the mouse and keyboard is as simple as moving the mouse off
the edge of your screen.  Synergy also merges the clipboards of all the
systems into one, allowing cut-and-paste between systems. Furthermore,
it synchronizes screen savers so they all start and stop together and,
if screen locking is enabled, only one screen requires a password to
unlock them all.

%package -n qsynergy
Summary:        Qt GUI for easily configuring Synergy2
Group:          Productivity/Networking/Other
Requires:       synergy = %{version}

%description -n qsynergy
QSynergy is a comprehensive and easy to use graphical front end for Synergy.
Synergy lets a user control more than one computer with a single mouse and
keyboard.

%prep
%setup -q -n %{synergy}-%{version}-stable
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch11 -p1
%patch14 -p1
cp %{SOURCE2} .

%build
export SYNERGY_VERSION_STAGE="release"
%cmake
make VERBOSE=1 %{?_smp_mflags}
# leave the build subfolder
cd ..

%install
chmod -x ChangeLog
install -D build/bin/synergyd "%{buildroot}%{_bindir}/synergyd"
install -D build/bin/synergyc "%{buildroot}%{_bindir}/synergyc"
install -D build/bin/synergys "%{buildroot}%{_bindir}/synergys"
install -D build/bin/syntool  "%{buildroot}%{_bindir}/syntool"
install -D -m0644 doc/synergy.conf.example "%{buildroot}%{_sysconfdir}/synergy.conf"
install -D -m0644 doc/synergyc.man "%{buildroot}%{_mandir}/man1/synergyc.1"
install -D -m0644 doc/synergys.man "%{buildroot}%{_mandir}/man1/synergys.1"

# Unit file
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sbindir}
install -p -m 644 "%{SOURCE4}" %{buildroot}%{_unitdir}
install -p -m 644 "%{SOURCE5}" %{buildroot}%{_unitdir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcsynergys

# GUI package
install -Dm 0755 build/bin/%{name} %{buildroot}%{_bindir}/q%{name}
%suse_update_desktop_file -i q%{name}

%post
%fillup_only
%desktop_database_post
%service_add_post synergys.service synergys.socket

%postun
%desktop_database_postun
%service_del_postun synergys.service synergys.socket

%pre
%service_add_pre synergys.service synergys.socket

%preun
%service_del_preun synergys.service synergys.socket

%files
%doc ChangeLog doc/synergy.conf*
%license LICENSE
%config(noreplace) %{_sysconfdir}/synergy.conf
%{_bindir}/synergyc
%{_bindir}/synergys
%{_bindir}/synergyd
%{_bindir}/syntool
%{_mandir}/man1/synergys.1%{?ext_man}
%{_mandir}/man1/synergyc.1%{?ext_man}
%{_unitdir}/synergys.service
%{_unitdir}/synergys.socket
%{_sbindir}/rcsynergys

%files -n qsynergy
%license LICENSE
%{_bindir}/q%{name}
%{_datadir}/applications/q%{name}.desktop
%{_datadir}/pixmaps/q%{name}.png

%changelog
