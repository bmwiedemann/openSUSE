#
# spec file for package ccze
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ccze
Version:        0.2.1.2
Release:        0
Summary:        A log colorizer
License:        GPL-2.0-or-later
URL:            https://git.madhouse-project.org/archive/ccze
Source:         ccze-0.2.1-2.tar.gz
Patch0:         license-fsf.diff
Patch1:         fix_capitalization_typo.patch
Patch2:         fix_passing_LDFLAGS_for_ccze-cssdump.patch
Patch3:         fix-national-encoding.patch
Patch4:         cross.patch
Patch5:         pcre2.patch
Patch6:         memory-leak.patch
Patch7:         uninitialised-value.patch
BuildRequires:  autoconf
BuildRequires:  ncurses-devel >= 5.0
BuildRequires:  pcre2-devel

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}

%description
CCZE is a modular log colorizer, with plugins for apm,
exim, fetchmail, httpd, postfix, procmail, squid, syslog, ulogd,
vsftpd, xferlog and more.

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{name}-0.2.1-2

%build
autoheader
autoconf
%configure --with-builtins=all
%make_build

%install
%make_install
install -d %{buildroot}/%{_sysconfdir}
src/ccze-dump > %{buildroot}/%{_sysconfdir}/cczerc

%check
make check TESTS="version.test bug-wnum.test bug-procmailsubj2.test \
                  bug-sysrepeat.test bug-httpd.test bug-dpkg.test"

%files
%license COPYING
%doc NEWS THANKS FAQ ChangeLog ChangeLog-0.1 README
%config(noreplace) %{_sysconfdir}/cczerc
%{_bindir}/ccze
%{_bindir}/ccze-cssdump
%{_mandir}/man1/ccze.1%{?ext_man}
%{_mandir}/man1/ccze-cssdump.1%{?ext_man}
%{_mandir}/man7/ccze-plugin.7%{?ext_man}

%files devel
%{_includedir}/ccze.h
%license COPYING

%changelog
