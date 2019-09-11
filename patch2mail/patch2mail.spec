#
# spec file for package patch2mail
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2008-2015 Christian Boltz
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           patch2mail
Version:        1.1.2
Release:        0
#
#
Summary:        Patch and package update notification via mail
#BuildRequires: bash
#
#Url:            http://blog.cboltz.de/plugin/tag/patch2mail
License:        GPL-2.0+
Group:          System/Packages
Url:            https://github.com/openSUSE/zypp-utils/tree/master/patch2mail
Source:         %{name}-%{version}.tar.bz2
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:       /bin/hostname
Requires:       /bin/rm
Requires:       /usr/bin/xsltproc
Requires:       cron
Requires:       grep
Requires:       mail
Requires:       mktemp
Requires:       zypper
# detailed requirements:
#      zypper    # (>= 11.0) zypp-refresh-rapper, zypper
#      zypper    # (<= 10.3) zypp-checkpatches-wrapper
#      libxslt   # xsltproc [NOT autodetected, even if rpmlint thinks so]
#      coreutils # rm
#      net-tools # hostname

%description
patch2mail checks for available updates and sends a mail to root
if any patches or updated packages (configureable) are available.

%prep
%setup -q

%build

%install
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/cron.daily
%{__install} -d -m 0755 %{buildroot}%{_fillupdir}/

%{__install} -m 0644 patch2mail.xsl %{buildroot}%{_datadir}/%{name}/patch2mail.xsl
%if 0%{?suse_version} < 1030
	%{__install} -m 0644 patch2mail.xsl_10.2 %{buildroot}%{_datadir}/%{name}/patch2mail.xsl
%endif

%{__install} -m 0755 patch2mail %{buildroot}%{_sysconfdir}/cron.daily/patch2mail
%if 0%{?suse_version} < 1110
	%{__install} -m 0755 patch2mail_11.0 %{buildroot}%{_sysconfdir}/cron.daily/patch2mail
%endif
%if 0%{?suse_version} < 1100
	%{__install} -m 0755 patch2mail_10.3 %{buildroot}%{_sysconfdir}/cron.daily/patch2mail
%endif
%{__install} -m 0644 patch2mail.sysconfig %{buildroot}%{_fillupdir}/sysconfig.patch2mail

echo ==== Buildroot: %{buildroot} ====
find %{buildroot}
echo ================================

%clean
%{__rm} -rf %{buildroot}

%post
%{fillup_only -n patch2mail}

%files
%defattr(-,root,root)
%{_sysconfdir}/cron.daily/%{name}
%{_datadir}/%{name}
%{_fillupdir}/sysconfig.patch2mail
%doc README COPYING

%changelog
