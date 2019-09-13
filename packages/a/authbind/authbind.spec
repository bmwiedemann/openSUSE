#
# spec file for package authbind
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           authbind
Version:        2.1.2
Release:        0
Summary:        Authentication socket binding to priviledged ports without root
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Url:            http://www.chiark.greenend.org.uk/ucgi/~ian/git/authbind.git
Source:         http://ftp.debian.org/debian/pool/main/a/authbind/authbind_%{version}.tar.gz
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         permissions

%description
Authbind allows a program which does not or should not run as
root to bind to low-numbered ports in a controlled way.

http://en.wikipedia.org/wiki/Authbind

%prep
%setup -q -n authbind

%build
make %{?_smp_mflags} OPTIMISE="%{optflags} -fPIE" LDFLAGS="-g -pie" prefix="%{_prefix}" etc_dir="%{_sysconfdir}/authbind"

%install
install -m 0755 -d %{buildroot}%{_bindir}

INSTALL_FILE="install -m 644" \
INSTALL_PROGRAM="install -m 755 -s" \
INSTALL_DIR="install -m 755 -d" \
make install install_man prefix="%{buildroot}%{_prefix}" etc_dir="%{buildroot}%{_sysconfdir}/authbind"

%post
# the actual settings for helper will come from security whitelisting in the permissions package.
%set_permissions %{_prefix}/lib/authbind/helper

%verifyscript
%verify_permissions -e %{_prefix}/lib/authbind/helper

%files
%{_bindir}/authbind
%dir %{_prefix}/lib/authbind
%verify(not mode) %attr(4755,root,root) %{_prefix}/lib/authbind/helper
%{_prefix}/lib/authbind/libauthbind.so.*

%dir %{_sysconfdir}/authbind
%dir %{_sysconfdir}/authbind/byport
%dir %{_sysconfdir}/authbind/byaddr
%dir %{_sysconfdir}/authbind/byuid

%{_mandir}/man1/authbind.1%{?ext_man}
%{_mandir}/man8/authbind-helper.8%{?ext_man}

%changelog
