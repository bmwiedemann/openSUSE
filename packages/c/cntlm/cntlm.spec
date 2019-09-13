#
# spec file for package cntlm
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007 Scorpio IT, Deidesheim, Germany
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

Name:           cntlm
Version:        0.92.3
Release:        0
Summary:        Fast NTLM authentication proxy with tunneling
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Proxy
Url:            http://cntlm.sourceforge.net/
Source0:        http://sourceforge.net/projects/cntlm/files/cntlm/cntlm%%20%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}.init
Source2:        %{name}.sysconfig
Source3:        %{name}.service
Source4:        %{name}.tmpfiles
# PATCH-FIX-UPSTREAM cntlm-override-CFLAGS-CXXFLAGS-makefile.patch --fix empty debuginfo package
Patch0:         cntlm-override-CFLAGS-CXXFLAGS-makefile.patch
# PATCH-FIX-UPSTREAM cntlm-0.92.3-HTTP-1.1-persistent-connections-with-HTTP-1.0-clients.patch --cntlm doesn't handle correctly
# between HTTP-1.0 and HTTP-1.1
Patch1:         cntlm-0.92.3-HTTP-1.1-persistent-connections-with-HTTP-1.0-clients.patch
Requires(pre):  grep
Requires(pre):  pwdutils
Requires(pre):  group(nogroup)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} < 1230
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
%else
BuildRequires:  systemd-devel
Requires(pre):  %fillup_prereq
%{?systemd_requires}
%endif

%description
Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling,
authenticated connection caching, ACLs, proper daemon logging and behaviour
and much more. It has up to ten times faster responses than similar NTLM
proxies, while using by orders or magnitude less RAM and CPU. Manual page
contains detailed information.

%prep
%setup -q
%patch0 -p1
%patch1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%if 0%{?suse_version} < 1230
install -D -m 755 %{SOURCE1} %{buildroot}/%{_initddir}/%{name}
ln -s -f ../..%{_sysconfdir}/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
%else
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -D -m 644 %{SOURCE3} %{buildroot}/%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE4} %{buildroot}/%{_tmpfilesdir}/%{name}.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%endif
install -D -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%pre
# on `rpm -ivh` PARAM is 1
# on `rpm -Uvh` PARAM is 2
# user cntlm
if [ -z  "`%{_bindir}/getent passwd "%{name}"`" ]; then
  %{_sbindir}/useradd -c "CNTLM Proxy Auth" -d %{_localstatedir}/run/%{name} -g nogroup \
	-r -s /bin/false %{name};
fi
%if 0%{?suse_version} >= 1230
%service_add_pre %{name}.service
%endif

%preun
# on `rpm -e` PARAM is 0
%if 0%{?suse_version} < 1230
%stop_on_removal cntlm
%else
%service_del_preun %{name}.service
%endif
#if [ "$1" -eq 0 ]; then
#  %{_sbindir}/userdel %{name} 
#fi

%post
# on `rpm -ivh` PARAM is 1
# on `rpm -Uvh` PARAM is 2
%if 0%{?suse_version} < 1230
%{fillup_and_insserv cntlm}
%else
%fillup_only
%service_add_post %{name}.service
%if 0%{?suse_version} <= 1320
systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf || :
%else
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%endif
%endif

%postun
# on `rpm -e` PARAM is 0
%if 0%{?suse_version} < 1230
%restart_on_update cntlm
%insserv_cleanup
%else
%service_del_postun %{name}.service
%endif

%files
%defattr(-,root,root,-)
%doc COPYRIGHT LICENSE README VERSION
%config(noreplace) %{_sysconfdir}/%{name}.conf
%if 0%{?suse_version} < 1230
%config(noreplace) %{_initddir}/%{name}
%else
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%ghost %dir %attr(755,%{name},root) /run/%{name}
%endif
%{_sbindir}/*
%{_mandir}/man1/%{name}.1*
%{_fillupdir}/sysconfig.%{name}

%changelog
