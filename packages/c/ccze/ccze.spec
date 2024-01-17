#
# spec file for package ccze
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Sebastian Wagner <sebix+novell.com@sebix.at>
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


Name:           ccze
Version:        0.2.1.2
Release:        0
Summary:        A log colorizer
License:        GPL-2.0+
Group:          Applications/Other
Url:            https://github.com/madhouse/ccze/
Source:         https://github.com/madhouse/ccze/archive/ccze-0.2.1-2.tar.gz
Source1:        http://http.debian.net/debian/pool/main/c/ccze/ccze_0.2.1-3.debian.tar.xz
Patch0:         license-fsf.diff
BuildRequires:  autoconf
BuildRequires:  ncurses-devel >= 5.0
BuildRequires:  pcre-devel >= 3.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%package devel
Summary:        Development files for %name
Group:          Development/Libraries/C and C++
Requires:       %name

%description
CCZE is a modular log colorizer, with plugins for apm,
exim, fetchmail, httpd, postfix, procmail, squid, syslog, ulogd,
vsftpd, xferlog and more.

%description devel
This package contains libraries and header files for developing
applications that use %name.


%prep
%setup -q -n %name-%name-0.2.1-2
%setup -D -T -b 1 -q -n %name-%name-0.2.1-2
%patch0 -p1
patch -p1 debian/patches/288834_FTBFS_unrecognized_command_line_option_-Wmulticharacter.patch
patch -p1 debian/patches/doc___ccze.1.in.patch
patch -p1 debian/patches/fix_capitalization_typo.patch
patch -p1 debian/patches/fix_passing_LDFLAGS_for_ccze-cssdump.patch
patch -p1 debian/patches/src___ccze.c.patch
patch -p1 debian/patches/src___ccze-wordcolor.c_positive-numbers.patch
patch -p1 debian/patches/src___ccze-wordcolor.c_virus+clean.patch
patch -p1 debian/patches/src___mod_syslog.c.patch

%build
autoheader
autoconf
%configure --with-builtins=all
make

%install
%make_install
install -d %{buildroot}/%{_sysconfdir}
src/ccze-dump > %{buildroot}/%{_sysconfdir}/cczerc

%check
make check

%files
%defattr(-,root,root)
%license COPYING
%doc NEWS THANKS FAQ ChangeLog ChangeLog-0.1 README
%config(noreplace) %{_sysconfdir}/cczerc
%{_bindir}/ccze
%{_bindir}/ccze-cssdump
%{_mandir}/man1/ccze.1*
%{_mandir}/man1/ccze-cssdump.1*
%{_mandir}/man7/ccze-plugin.7*

%files devel
%{_includedir}/ccze.h
%license COPYING

%changelog
