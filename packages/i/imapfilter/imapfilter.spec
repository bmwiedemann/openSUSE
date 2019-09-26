#
# spec file for package imapfilter
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


Name:           imapfilter
Version:        2.6.13
Release:        0
Summary:        A mail filtering utility
License:        MIT
Group:          Productivity/Networking/Email/Utilities
URL:            https://github.com/lefcha/imapfilter
Source:         %{name}-%{version}.tar.gz
BuildRequires:  lua-devel >= 5.1
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig

%description
IMAPFilter is a mail filtering utility. It connects to remote mail
servers using the Internet Message Access Protocol (IMAP), sends
searching queries to the server and processes mailboxes based on the
results. It can be used to delete, copy, move, flag, etc. messages
residing in mailboxes at the same or different mail servers. The 4rev1
and 4 versions of the IMAP protocol are supported.

IMAPFilter uses the Lua programming language as a configuration and
extension language.

%prep
%setup -q

%build
make PREFIX="%{_prefix}" MANDIR="%{_mandir}" MYCFLAGS="%{optflags} -I%{lua_incdir}" %{?_smp_mflags}

%install
%make_install PREFIX="%{_prefix}" MANDIR="%{_mandir}"

%files
%{_bindir}/imapfilter
%dir %{_datadir}/imapfilter
%{_datadir}/imapfilter/*.lua
%{_mandir}/man1/imapfilter.1%{?ext_man}
%{_mandir}/man5/imapfilter_config.5%{?ext_man}
%license LICENSE
%doc README AUTHORS NEWS

%changelog
