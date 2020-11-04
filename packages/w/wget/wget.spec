#
# spec file for package wget
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.20.3
Release:        0
Summary:        A Tool for Mirroring FTP and HTTP Servers
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            https://www.gnu.org/software/wget/
Source:         https://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=wget&download=1#/wget.keyring
Patch0:         wgetrc.patch
Patch1:         wget-libproxy.patch
Patch6:         wget-1.14-no-ssl-comp.patch
# PATCH-FIX-OPENSUSE fix pod syntax for perl 5.18 coolo@suse.de
Patch7:         wget-fix-pod-syntax.diff
Patch8:         wget-errno-clobber.patch
Patch9:         remove-env-from-shebang.patch
BuildRequires:  automake
BuildRequires:  gpgme-devel >= 0.4.2
BuildRequires:  libcares-devel
BuildRequires:  libidn2-devel
BuildRequires:  libpng-devel
BuildRequires:  makeinfo
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig >= 0.9.0
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}
%if %{?suse_version} > 1110
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmetalink)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(uuid)
%else
BuildRequires:  libmetalink-devel
BuildRequires:  libpsl-devel
BuildRequires:  libuuid-devel
BuildRequires:  pcre-devel
%endif
%if 0%{?suse_version} > 1110
BuildRequires:  libproxy-devel
%endif
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
%setup -q
%patch0 -p1
%if 0%{?suse_version} > 1110
%patch1 -p1
%endif
%patch6
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
%if 0%{?suse_version} > 1110
# only wget-libproxy.patch needs this
autoreconf --force
%endif
%configure \
	--with-ssl=openssl \
	--with-cares \
	--with-metalink
%make_build
sed -i 's/\/usr\/bin\/env perl -w/\/usr\/bin\/perl -w/' util/rmold.pl

%check
%if %{with regression_tests}
%make_build -C tests/ check
%endif

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files 
%license COPYING
%doc AUTHORS NEWS README MAILING-LIST
%doc doc/sample.wgetrc util/rmold.pl
%{_mandir}/*/wget*
%{_infodir}/wget*
%config(noreplace) %{_sysconfdir}/wgetrc
%{_bindir}/*

%files lang -f %{name}.lang

%changelog
