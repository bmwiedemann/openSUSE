#
# spec file for package pound
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


%if 0%{?suse_version} > 1230
%bcond_without systemd
%else
%bcond_with    systemd
%endif
Name:           pound
Version:        2.8
Release:        0
Summary:        Reverse proxy and load balancer
License:        SUSE-GPL-3.0+-with-openssl-exception
Group:          Productivity/Networking/Web/Proxy
URL:            http://www.apsis.ch/pound/
Source0:        http://www.apsis.ch/pound/Pound-%{version}.tgz
Source1:        pound.cfg
Source2:        init.pound
Source3:        %{name}.service
Patch0:         pound.diff
# PATCH-FIX-UPSTREAM add-openssl_1.1-support.patch
Patch1:         add-openssl_1.1-support.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
Requires(pre):  shadow
%if %{with systemd}
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
%else
Requires(pre):         %insserv_prereq
%endif

%description
The Pound program is a reverse proxy, load balancer and HTTPS front-end
for Web server(s). Pound was developed to enable distributing the load
among several web servers and to allow for a convenient SSL wrapper for
those web servers that do not offer it natively.

%package doc
Summary:        Doumentation for pound
Group:          Documentation/Other

%description doc
The Pound program is a reverse proxy, load balancer and HTTPS front-end
for web server(s). Pound was developed to enable distributing the load
among several web servers and to allow for a convenient SSL wrapper for
those web servers that do not offer it natively.

This package contains the documentation for pound.

%prep
%setup -q -n Pound-%{version}
%patch0
%patch1 -p1

%build
%configure \
  --enable-msdav \
  --with-ssl=%{_includedir}/openssl \
  --with-owner=pound \
  --with-group=pound
make %{?_smp_mflags}

%install
%make_install
# Install pound init script
%if %{with systemd}
install -Dm 0644 %{SOURCE3} %{buildroot}/%{_unitdir}/pound.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
install -Dm 0744 %{SOURCE2} %{buildroot}%{_initddir}/pound
ln -sf ../..%{_initddir}/pound %{buildroot}%{_sbindir}/rcpound
%endif
install -Dm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pound.cfg
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/examples
install -m644 GPL.txt README FAQ %{buildroot}%{_defaultdocdir}/%{name}/
install -m755 z2_2_5_1.py z2_2_6_1.py %{buildroot}%{_defaultdocdir}/%{name}/examples/

%pre
# Add the "pound" user and group
getent group pound >/dev/null || %{_sbindir}/groupadd -r pound
getent passwd pound >/dev/null || \
	%{_sbindir}/useradd -c "Pound" -g pound -r -d %{_localstatedir}/lib/pound pound
%if %{with systemd}
%service_add_pre %{name}.service
%endif

%post
%if %{with systemd}
%service_add_post %{name}.service
%else
%{fillup_and_insserv -f -n pound pound}
%endif

%postun
%if %{with systemd}
%service_del_postun %{name}.service
%else
%restart_on_update pound
%insserv_cleanup
%endif

%preun
%if %{with systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal pound
%endif

%files
%doc %{_defaultdocdir}/%{name}/GPL.txt
%if %{with systemd}
%{_unitdir}/%{name}.service
%else
%{_initddir}/pound
%endif
%attr(555, root, root) %{_sbindir}/pound
%attr(555, root, root) %{_sbindir}/poundctl
%{_sbindir}/rcpound
%{_mandir}/man8/pound.8%{?ext_man}
%{_mandir}/man8/poundctl.8%{?ext_man}
%config(noreplace) %{_sysconfdir}/pound.cfg

%files doc
%doc %{_defaultdocdir}/%{name}
%exclude %{_defaultdocdir}/%{name}/GPL.txt

%changelog
