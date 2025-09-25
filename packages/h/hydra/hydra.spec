#
# spec file for package hydra
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

Name:           hydra
Version:        9.6
Release:        0
Summary:        A network logon cracker with support for many different services
License:        AGPL-3.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/vanhauser-thc/thc-hydra
Source0:        https://github.com/vanhauser-thc/thc-hydra/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         fix-prototype-mismatches.patch
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(freerdp3)
%else
BuildRequires:  pkgconfig(freerdp2)
%endif
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libmemcached)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libsvn_client)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(smbclient)

%description
A parallelized network login cracker, created as a proof of concept
tool for security researchers to demonstrate how easy it can be to
crack logins for a particular target.

Hydra works by using different approaches, such as brute-force
attacks and dictionary attacks, in order to guess the right username
and password combination.

%prep
%autosetup -n thc-%{name}-%{version} -p1

%build
%configure --fhs DATADIR=/share/hydra
%make_build

prev="$PWD"
cd hydra-gtk
%configure
%make_build
cd "$prev"

# Replace /bin/sh with /bin/bash in hydra-wizard.sh, as it uses bashisms
sed -i '1s|^.*$|#!/bin/bash|' hydra-wizard.sh

%install
%make_install MANDIR=/share/man/man1/ DATADIR=/share/hydra
%make_install -C hydra-gtk MANDIR=/share/man/man1/ DATADIR=/share/hydra

%fdupes -s %{buildroot}/%{_mandir}
%fdupes %{buildroot}/%{_prefix}

%files
%license LICENSE LICENSE_OPENSSL
%doc README CHANGES TODO
%{_bindir}/%{name}
%{_bindir}/xhydra
%{_bindir}/%{name}-wizard.sh
%{_bindir}/pw-inspector
%{_bindir}/dpl4hydra.sh
%{_mandir}/man1/hydra.1%{?ext_man}
%{_mandir}/man1/pw-inspector.1%{?ext_man}
%{_mandir}/man1/xhydra.1%{?ext_man}
%{_datarootdir}/%{name}
%{_datarootdir}/pixmaps/xhydra.png

%changelog
