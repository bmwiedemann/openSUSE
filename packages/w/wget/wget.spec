#
# spec file for package wget
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%bcond_with	regression_tests
Name:           wget
Version:        1.24.5
Release:        0
Summary:        A Tool for Mirroring FTP and HTTP Servers
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://www.gnu.org/software/wget/
Source:         https://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=90497#/%{name}.keyring
Patch0:         wgetrc.patch
Patch6:         wget-1.14-no-ssl-comp.patch
# PATCH-FIX-OPENSUSE fix pod syntax for perl 5.18 coolo@suse.de
Patch7:         wget-fix-pod-syntax.diff
Patch8:         wget-errno-clobber.patch
Patch9:         remove-env-from-shebang.patch
Patch10:        wget-do-not-propagate-credentials.patch
Patch11:        properly-re-implement-userinfo-parsing.patch
BuildRequires:  gpgme-devel >= 0.4.2
BuildRequires:  libcares-devel
BuildRequires:  libidn2-devel
BuildRequires:  libpng-devel
BuildRequires:  makeinfo
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(libmetalink)
BuildRequires:  pkgconfig(libpcre2-8)
# px_proxy_factory_free_proxies added in 0.4.16
BuildRequires:  pkgconfig(libproxy-1.0) >= 0.4.16
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(uuid)
%if %{with regression_tests}
# For the Testsuite
BuildRequires:  perl-HTTP-Daemon
BuildRequires:  perl-IO-Socket-SSL
%endif

%description
Wget enables you to retrieve WWW documents or FTP files from a server.
This can be done in script files or via the command line.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--with-ssl=openssl \
	--with-cares \
	--with-metalink \
	--enable-libproxy \
	%{nil}
%make_build
sed -i 's/\/usr\/bin\/env perl -w/\/usr\/bin\/perl -w/' util/rmold.pl

%check
%if %{with regression_tests}
%make_build -C tests/ check
%endif

%install
%make_install
%find_lang %{name} --all-name %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS README MAILING-LIST
%doc doc/sample.wgetrc util/rmold.pl
%{_mandir}/*/wget*
%{_infodir}/wget*
%config(noreplace) %{_sysconfdir}/wgetrc
%{_bindir}/*

%files lang -f %{name}.lang
%license COPYING

%changelog
