#
# spec file for package mrsh
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


%if 0%{?suse_version} >= 1230
%define have_systemd 1
%endif

Name:           mrsh
Version:        2.12
Release:        0
Summary:        Remote shell program that uses munge authentication
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/Computing
Url:            https://github.com/chaos/mrsh
Source0:        https://github.com/chaos/mrsh/archive/%{version}.tar.gz
Source1:        README.SUSE
Patch1:         services-Do-not-require-non-standard-entries-in-etc-services.patch
Patch2:         mrlogin-Don-t-use-union-wait.patch
Patch3:         autogen.sh-Add-force-to-libtoolize.patch
Patch4:         Include-grp.h.patch
BuildRequires:  munge-devel >= 0.1-0
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  pkg-config
%if 0%{?have_systemd}
BuildRequires:  systemd-mini
%endif
BuildRequires:  fdupes

# support re-run of autogen
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Remote shell programs that use munge authentication rather than
reserved ports for security.

%package server
Summary:        Servers for remote access commands (mrsh, mrlogin, mrcp)
Group:          System/Daemons
Requires:       mrsh
Requires:       tcpd
%if 0%{?have_systemd}
%{?systemd_requires}
%else
Requires:       xinetd
%endif

%description server
Server daemons for remote access commands (mrsh, mrlogin, mrcp)

%package rsh-compat
Summary:        Rsh compatibility package for mrcp/mrlogin/mrsh
Group:          System/Base
Requires:       mrsh = %version
Provides:       rsh
Conflicts:      otherproviders(rsh)

%description rsh-compat
This package provides rsh compatibility for mrcp/mrlogin/mrsh

%package rsh-server-compat
Summary:        Rsh server compatibility package for mrlogind/mrshd
Group:          System/Daemons
Requires:       mrsh-server = %version
Provides:       rsh-server
Conflicts:      otherproviders(rsh-server)

%description rsh-server-compat
This package provides rsh server compatibility for mrlogind/mrshd

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
cp %{S:1} .

%build
./autogen.sh
%if 0%{!?suse_version:1310}%{?suse_version} < 1310
%define addflags CFLAGS+=-fpie LDFLAGS+=-pie
%endif
%configure
make %{?_smp_mflags} %{?addflags}

%install
DESTDIR="%{buildroot}" make install

ln -sf in.mrlogind %{buildroot}%{_sbindir}/in.rlogind
ln -sf in.mrshd %{buildroot}%{_sbindir}/in.rshd

for i in mrsh mrlogin
do
    sed -i 's#\(account\s\+include\s\+\)system-auth#\1common-account#' %{buildroot}/%{_sysconfdir}/pam.d/$i
    sed -i 's#\(session\s\+include\s\+\)system-auth#\1common-session#' %{buildroot}/%{_sysconfdir}/pam.d/$i
done
%if 0%{!?have_systemd}
sed -i 's#disable\s*= yes#disable			= no#' %{buildroot}/etc/xinetd.d/mrlogind
sed -i 's#disable\s*= yes#disable			= no#' %{buildroot}/etc/xinetd.d/mrshd
%endif
%fdupes -s %{buildroot}

%pre server
%if 0%{?have_systemd}
%service_add_pre mrshd.socket mrlogind.socket mrlogind@.service mrshd@.service
%endif

%post server
%if 0%{?have_systemd}
%service_add_post mrshd.socket mrlogind.socket mrlogind@.service mrshd@.service
%else
%restart_on_update xinetd
%endif

%if 0%{?suse_version} > 1320 || 0%{?sle_version} > 120100
%define service_arg 1
%endif

%preun server
%if 0%{?have_systemd}
%service_del_preun %{?service_arg:-n} mrshd.socket mrlogind.socket mrlogind@.service mrshd@.service
%endif

%postun server
%if 0%{?have_systemd}
%service_del_postun %{?service_arg:-n} mrshd.socket mrlogind.socket mrlogind@.service mrshd@.service
%else
%restart_on_update xinetd
%endif

%files
%doc NEWS README ChangeLog
%license COPYING DISCLAIMER DISCLAIMER.UC
%{_mandir}/man1/mrcp.1*
%{_mandir}/man1/mrsh.1*
%{_mandir}/man1/mrlogin.1*
%{_bindir}/mrcp
%{_bindir}/mrsh
%{_bindir}/mrlogin

%files server
%doc %{basename %{S:1}}
%{!?have_systemd:%attr(644,root,root) %config(noreplace) /etc/xinetd.d/mrshd}
%{!?have_systemd:%attr(644,root,root) %config(noreplace) /etc/xinetd.d/mrlogind}
%attr(644,root,root) %config(noreplace) /etc/pam.d/mrsh
%attr(644,root,root) %config(noreplace) /etc/pam.d/mrlogin
%{?have_systemd:%{_unitdir}/*}
%{_mandir}/man8/in.mrlogind.8*
%{_mandir}/man8/in.mrshd.8*
%{_mandir}/man8/mrlogind.8*
%{_mandir}/man8/mrshd.8*
%{_sbindir}/in.mrlogind
%{_sbindir}/in.mrshd

%files rsh-compat
%{_mandir}/man1/rcp.1*
%{_mandir}/man1/rsh.1*
%{_mandir}/man1/rlogin.1*
%{_bindir}/rcp
%{_bindir}/rsh
%{_bindir}/rlogin

%files rsh-server-compat
%{_mandir}/man8/in.rlogind.8*
%{_mandir}/man8/in.rshd.8*
%{_mandir}/man8/rlogind.8*
%{_mandir}/man8/rshd.8*
%{_sbindir}/in.rlogind
%{_sbindir}/in.rshd

%changelog
