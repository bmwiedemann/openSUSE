#
# spec file for package patch2mail
#
# Copyright (c) 2023 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           patch2mail
Version:        1.1.2
Release:        0
Summary:        Patch and package update notification via mail
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/openSUSE/zypp-utils/tree/master/patch2mail
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.service
Source2:        %{name}.timer
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       /bin/hostname
Requires:       /bin/rm
Requires:       /usr/bin/xsltproc
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
%{__install} -d -m 0755 %{buildroot}%{_fillupdir}/
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/%{name}.timer
%{__install} -D -m 0755 patch2mail %{buildroot}%{_bindir}/patch2mail
%{__install} -m 0644 patch2mail.sysconfig %{buildroot}%{_fillupdir}/sysconfig.patch2mail

%{__install} -m 0644 patch2mail.xsl %{buildroot}%{_datadir}/%{name}/patch2mail.xsl
%if 0%{?suse_version} < 1030
	%{__install} -m 0644 patch2mail.xsl_10.2 %{buildroot}%{_datadir}/%{name}/patch2mail.xsl
%endif

%pre
%service_add_pre %{name}.service %{name}.timer

%preun
%service_del_preun %{name}.service %{name}.timer

%post
%{fillup_only -n patch2mail}
%service_add_post %{name}.service %{name}.timer

%postun
%service_del_postun %{name}.service %{name}.timer

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%{_datadir}/%{name}
%{_fillupdir}/sysconfig.patch2mail
%doc README COPYING

%changelog
