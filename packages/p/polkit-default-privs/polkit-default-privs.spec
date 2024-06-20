#
# spec file for package polkit-default-privs
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1550+20240620.095c860
Release:        0
Summary:        SUSE PolicyKit default permissions
License:        GPL-2.0-or-later
Group:          Productivity/Security
Source:         polkit-default-privs-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Supplements:    PolicyKit
Supplements:    libpolkit0
BuildRequires:  polkit
Requires(pre):  polkit
Supplements:    polkit
BuildArch:      noarch
# please open bugreports at bugzilla.suse.com
URL:            http://github.com/openSUSE/polkit-default-privs.git
PreReq:         %fillup_prereq

%description
Predefined polkit profiles for different usage scenarios like desktop and
server. These profiles define the kind of authentication required for various
polkit actions used across applications.

%prep
%setup -q

%build

%install
make install DESTDIR=$RPM_BUILD_ROOT fillupdir="%{_fillupdir}"
mkdir -p $RPM_BUILD_ROOT/etc/polkit-1/rules.d/
> $RPM_BUILD_ROOT/etc/polkit-1/rules.d/90-default-privs.rules

%post
%{fillup_only -ns security polkit_default_privs}
/usr/sbin/set_polkit_default_privs >/dev/null

%files
%define basedir %{_distconfdir}/polkit-default-privs
%define profiledir %{basedir}/profiles
%define confdir /etc/polkit-1
%doc README.md
%ghost %attr(0644,root,root) %{confdir}/rules.d/90-default-privs.rules
%dir %{basedir}
%dir %{profiledir}
%{profiledir}/easy
%{profiledir}/standard
%{profiledir}/restrictive
%{basedir}/local.template
/usr/sbin/chkstat-polkit
/usr/sbin/set_polkit_default_privs
%_mandir/man*/*
%{_fillupdir}/sysconfig.security-polkit_default_privs

%changelog
