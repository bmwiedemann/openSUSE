#
# spec file for package polkit-default-privs
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
# icecream 0


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           polkit-default-privs
Version:        1550+20201001.cb7020b
Release:        0
Summary:        SUSE PolicyKit default permissions
License:        GPL-2.0-or-later
Group:          Productivity/Security
Source:         polkit-default-privs-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  polkit
Requires:       polkit
Supplements:    PolicyKit
Supplements:    libpolkit0, polkit
BuildArch:      noarch
# please open bugreports at bugzilla.suse.com
URL:            http://github.com/openSUSE/polkit-default-privs.git
PreReq:         %fillup_prereq

%description
Predefined polkit profiles for different usage scenarios like desktop and
server. These profiles define the kind of authentication required for various
polkit actions used across applications.

# use a separate package for the static whitelist (i.e. the one that isn't
# part of the different profile selectable during runtime). This whitelist is
# of no use for users and only needed during rpmlint time.
%package -n polkit-whitelisting
Summary:        Static polkit whitelists for processing by rpmlint-checks
Group:          Productivity/Security

%description -n polkit-whitelisting
This package contains static polkit whitelistings for polkit Java Script rule
files. The whitelistings will be processed by rpmlint-checks to determine
valid rule file installations by other packages.

%prep
%setup -q

%build

%install
make install DESTDIR=$RPM_BUILD_ROOT fillupdir="%{_fillupdir}"
mkdir -p $RPM_BUILD_ROOT/etc/polkit-1/rules.d/
> $RPM_BUILD_ROOT/etc/polkit-1/rules.d/90-default-privs.rules

%post
%{fillup_only -ns security polkit_default_privs}
/sbin/set_polkit_default_privs >/dev/null

%files
%doc README.md
%defattr(-,root,root,-)
%ghost %attr(0644,root,root) /etc/polkit-1/rules.d/90-default-privs.rules
%config /etc/polkit-default-privs.easy
%config /etc/polkit-default-privs.standard
%config /etc/polkit-default-privs.restrictive
%config(noreplace) /etc/polkit-default-privs.local
/sbin/chkstat-polkit
/sbin/set_polkit_default_privs
%_mandir/man*/*
%{_fillupdir}/sysconfig.security-polkit_default_privs

%files -n polkit-whitelisting
%defattr(-,root,root)
/etc/polkit-rules-whitelist.json

%changelog
