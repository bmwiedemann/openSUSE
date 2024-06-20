#
# spec file for package dkimproxy
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


%if %{undefined _fillupdir}
%define _fillupdir /var/adm/fillup-templates/
%endif

%define dkimproxy_prefix /usr/share/dkimproxy
Summary:        DKIMproxy is an SMTP-proxy that implements the DKIM and DomainKeys standards
License:        GPL-2.0-only
Group:          Productivity/Networking/Email/Utilities
Name:           dkimproxy
Version:        1.4.1
Release:        0
URL:            https://dkimproxy.sourceforge.net/
Source:         %{name}-%{version}.tar.gz
Source2:        %{name}.sysconfig
Source3:        %{name}-in.service
Source4:        %{name}-out.service
Source5:        %{name}_env.sh
Source6:        %{name}-tmpfiles
%define services %{name}-in.service %{name}-out.service

Patch0:         dkimproxy-1.4.1-avoid-perl-provides.diff
#PATCH-FIX-UPSTREAM Port the perl-IO-Socket-INET6 code to use perl-IO-Socket-IP
# upstream: https://sourceforge.net/p/dkimproxy/bugs/39
Patch1:         dkimproxy-port-perl-IO-Socket-INET6-to-IP.patch
BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  perl-Mail-DKIM
BuildRequires:  perl-Net-Server
BuildRequires:  pwdutils
PreReq:         %fillup_prereq
PreReq:         pwdutils
Requires:       git-core
Requires:       perl-Mail-DKIM
Requires:       perl-Net-Server

%description
DKIMproxy is an SMTP-proxy that signs and/or verifies emails, using the
Mail::DKIM module. It is designed for Postfix, but should work with any
mail server. It comprises two separate proxies, an "outbound" proxy for
signing outgoing email, and an "inbound" proxy for verifying signatures
of incoming email. With Postfix, the proxies can operate as either
Before-Queue or After-Queue content filters.

%prep
%autosetup -p1 -n %{name}-%{version}

# ---------------------------------------------------------------------------

%build
./configure --prefix %{dkimproxy_prefix}
# ---------------------------------------------------------------------------

%install
%makeinstall
chmod 644 $( find %{buildroot}/%{dkimproxy_prefix} -name "*.pm" )
    mkdir -p %{buildroot}%{_fillupdir}
    mkdir -p %{buildroot}%{_unitdir}
    mkdir -p %{buildroot}%{_libexecdir}/%{name}
    install -m 0644 %{S:2} %{buildroot}%{_fillupdir}/sysconfig.%{name}
    install -m 0644 %{S:3} %{buildroot}%{_unitdir}/
    sed -i s#_LIBEXECDIR#%{_libexecdir}# %{buildroot}%{_unitdir}/%{name}-in.service
    install -m 0644 %{S:4} %{buildroot}%{_unitdir}/
    install -m 0755 %{S:5} %{buildroot}%{_libexecdir}/%{name}
    mkdir -p %{buildroot}%{_tmpfilesdir}
    install -m 0744 %{S:6} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# ---------------------------------------------------------------------------
### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}
# ---------------------------------------------------------------------------

%pre
/usr/sbin/groupadd -r dkim  2> /dev/null || :
/usr/sbin/useradd -r -g dkim -s /bin/false -c "DKIMproxy Daemon" -d /var/spool/dkim dkim 2> /dev/null || :
%service_add_pre %services

%preun
%service_del_preun %services

%post
%service_add_post %services
%{fillup_only}
%tmpfiles_create %{name}.conf

%postun
%service_del_postun %services

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO smtpprox.ChangeLog smtpprox.README smtpprox.TODO
%license COPYING
%{dkimproxy_prefix}
%{_fillupdir}/sysconfig.%{name}
%{_unitdir}/%{name}-in.service
%{_unitdir}/%{name}-out.service
%{_libexecdir}/%{name}/
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%ghost %{_rundir}/%{name}
# ---------------------------------------------------------------------------

%changelog
