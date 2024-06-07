#
# spec file for package wsdd
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


Name:           wsdd
Version:        0.8
Release:        0
Summary:        A Web Service Discovery host daemon
License:        MIT
URL:            https://github.com/christgau/wsdd
Source:         https://github.com/christgau/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source1:        %{name}-init.sh
Source2:        %{name}.service.in
%if 0%{suse_version} >= 1599 || 0%{?sle_version} >= 150600
Source3:        %{name}.xml
%endif
Source4:        sysconfig.%{name}
Source5:        %{name}.conf
Source6:        %{name}-user.conf
Patch1:         %{name}-shebang.patch
BuildRequires:  firewall-macros
BuildRequires:  python-rpm-macros
BuildRequires:  sysuser-tools
Requires(post): %fillup_prereq
Supplements:    samba
Supplements:    samba-ad-dc
BuildArch:      noarch
%sysusers_requires

%description
wsdd implements a Web Service Discovery host daemon. This enables (Samba) hosts,
like your local NAS device, to be found by Web Service Discovery Clients like Windows.

Since NetBIOS discovery is not supported by Windows anymore, wsdd makes hosts to
appear in Windows again using the Web Service Discovery method. This is beneficial
for devices running Samba, like NAS or file sharing servers on your local network.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE6} %{name} %{name}-user.conf
%if 0%{suse_version} <= 1500
%if 0%{?sle_version} < 150600
sed -i '1s/python3/python3.10/' src/wsdd.py
%else
sed -i '1s/python3/python3.11/' src/wsdd.py
%endif
%endif

%install
install -m 755 -D src/wsdd.py %{buildroot}%{_sbindir}/%{name}
install -m 644 -D man/wsdd.8 %{buildroot}/%{_mandir}/man8/wsdd.8
install -m 755 -D %{SOURCE1} %{buildroot}%{_libexecdir}/wsdd-init.sh
mkdir -p %{buildroot}%{_unitdir}
sed 's#@LIBEXECDIR@#%{_libexecdir}#' %{SOURCE2} >%{buildroot}%{_unitdir}/wsdd.service
%if 0%{?sle_version} <  150600
install -m 644 -D etc/firewalld/services/wsdd.xml %{buildroot}%{_prefix}/lib/firewalld/services/wsdd.xml
%else
install -m 644 -D %{SOURCE3} %{buildroot}%{_prefix}/lib/firewalld/services/wsdd.xml
%endif
install -m 644 -D etc/firewalld/services/wsdd-http.xml %{buildroot}%{_prefix}/lib/firewalld/services/wsdd-http.xml
install -m 644 -D %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.wsdd
install -m 755 -d %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d/
install -m 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}/run/wsdd
mkdir -p %{buildroot}%{_localstatedir}/lib/wsdd
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/
%?python3_fix_shebang

%check

%pre -f %{name}.pre
%service_add_pre wsdd.service

%post
%fillup_only
%service_add_post wsdd.service
%tmpfiles_create %{_tmpfilesdir}/wsdd.conf
%firewalld_reload

%preun
%service_del_preun wsdd.service

%postun
%service_del_postun wsdd.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}
%{_mandir}/man8/wsdd.8%{?ext_man}
%{_sbindir}/rc%{name}
%{_unitdir}/wsdd.service
%{_libexecdir}/wsdd-init.sh
%{_tmpfilesdir}/wsdd.conf
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/wsdd.xml
%{_prefix}/lib/firewalld/services/wsdd-http.xml
%{_fillupdir}/sysconfig.%{name}
%{_sysusersdir}/%{name}-user.conf
%dir %attr(0755,wsdd,wsdd) %ghost /run/%{name}
%attr(0644,wsdd,wsdd) %ghost /run/%{name}/env-vars

%changelog
