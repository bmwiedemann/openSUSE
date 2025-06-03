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
Version:        9.5
Release:        0
Summary:        A very fast network logon cracker which support many different services
License:        AGPL-3.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/vanhauser-thc/thc-hydra
Source0:        https://github.com/vanhauser-thc/thc-hydra/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(apr-1)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(freerdp2)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libmemcached)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libsvn_client)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(smbclient)

%description
Number one of the biggest security holes are passwords, as every password
security study shows.
This tool is a proof of concept code, to give researchers and security
consultants the possiblity to show how easy it would be to gain unauthorized
access from remote to a system.

THIS TOOL IS FOR LEGAL PURPOSES ONLY!

There are already several login hacker tools available, however none does
either support more than one protocol to attack or support parallized
connects.

%prep
%autosetup -n thc-%{name}-%{version}

%build
%configure --fhs DATADIR=/share/hydra
%make_build

pushd hydra-gtk || exit 1
%configure
%make_build
popd || exit 1

# Replace /bin/sh with /bin/bash in hydra-wizard.sh, as it uses bashisms
sed -i '1s|^.*$|#!/bin/bash|' hydra-wizard.sh

%install
%make_install MANDIR=/share/man/man1/ DATADIR=/share/hydra

pushd hydra-gtk || exit 1
%make_install MANDIR=/share/man/man1/ DATADIR=/share/hydra
popd || exit 1

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
