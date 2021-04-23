#
# spec file for package whohas
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 8/2011 open-slx GmbH <Sascha.Manns@open-slx.de>
# Copyright (c) 2010 - 7/2011 Sascha Manns <saigkill@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           whohas
Version:        0.29.1
Release:        0
Summary:        Package list querying tool
License:        GPL-2.0-or-later
Group:          System/Console
Url:            http://www.philippwesche.org/200811/whohas/intro.html
Source0:        https://github.com/whohas/whohas/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/whohas/whohas/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source3:        whohas.keyring
# PATCH-FIX-OPENSUSE improve-fetchdoc.patch asterios.dramis@gmail.com -- Shift some of the burden in sub fetchdoc onto the LWP::UserAgent class. This also allows us to process XML files without breaking the first line
Patch0:         improve-fetchdoc.patch
# PATCH-FIX-UPSTREAM whohas-0.29.1-fix-permissions.patch -- Fix wrong executable bits set on docs 
Patch1:         whohas-0.29.1-fix-permissions.patch
# PATCH-FIX-UPSTREAM whohas-0.29.1-update-fedora.patch -- Update information for Fedora (picked from upstream)
Patch2:         whohas-0.29.1-update-fedora.patch
# PATCH-FIX-UPSTREAM whohas-0.29.1-update-openbsd.patch -- Update information for OpenBSD (picked from upstream)
Patch3:         whohas-0.29.1-update-openbsd.patch
Requires:       perl = %{perl_version}
Requires:       perl(LWP::UserAgent)
Requires:       perl(Thread::Queue)
Requires:       perl(forks)
Recommends:     perl(Sys::CPU)
BuildArch:      noarch

%description
whohas is a command line tool that allows querying several package lists at
once - currently supported are Arch, Debian, Fedora, Gentoo, Mandriva,
openSUSE, Slackware (and linuxpackages.net), Source Mage, Ubuntu, FreeBSD,
NetBSD, OpenBSD, Fink, MacPorts, Cygwin and OpenMoko. whohas is written in Perl
and was designed to help package maintainers find ebuilds, pkgbuilds and
similar package definitions from other distributions to learn from. However, it
can also be used by normal users who want to know:

 * Which distribution provides packages on which the user depends.
 * What version of a given package is in use in each distribution, or in each
   release of a distribution (not implemented for all distributions).

%prep
%autosetup -p1

%build
# Nothing to do.

%install
%make_install PREFIX=%{_prefix} docdir=%{_docdir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%dir %{_mandir}/de/man1
%{_mandir}/de/man1/%{name}.1%{?ext_man}

%changelog
