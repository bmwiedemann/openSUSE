#
# spec file for package spamass-milter
#
# Copyright (c) 2025 SUSE LLC
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


Name:           spamass-milter
Version:        0.4.0
Release:        0
Summary:        Milter (mail filter) for spamassassin
License:        GPL-2.0-or-later
URL:            https://savannah.nongnu.org/projects/spamass-milt/
Source0:        http://savannah.nongnu.org/download/spamass-milt/spamass-milter-%{version}.tar.gz
Source1:        README.postfix
Source2:        spamass-milter.conf-tmpfiles
Source3:        spamass-milter.conf-sysusers
Source4:        spamass-milter.service
Source5:        spamass-milter-default
Source6:        COPYING
# PATCH-FIX-UPSTREAM spamass-milter-0.4.0-rcvd.patch https://bugs.debian.org/510665
Patch1:         spamass-milter-0.4.0-rcvd.patch
# PATCH-FEATURE-UPSTREAM spamass-milter-0.4.0-bits.patch brc#496769
Patch2:         spamass-milter-0.4.0-bits.patch
# PATCH-FEATURE-UPSTREAM spamass-milter-0.4.0-group.patch brc#452248
Patch3:         spamass-milter-0.4.0-group.patch
# PATCH-FEATURE-UPSTREAM spamass-milter-0.4.0-auth-no-ssf.patch brc#730308
Patch4:         spamass-milter-0.4.0-auth-no-ssf.patch
BuildRequires:  curl
BuildRequires:  gcc-c++
BuildRequires:  sendmail-devel
BuildRequires:  spamassassin
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
Requires:       postfix
%if 0%{?suse_version} == 1500
Requires:       spamassassin
%else
Requires:       spamassassin-spamc
%endif
Requires(pre):  group(postfix)
%sysusers_requires

%description
A milter (Mail Filter) application that pipes incoming mail (including things
received by rmail/UUCP) through SpamAssassin, a highly customizable spam
filter. A milter-compatible MTA such as Sendmail or Postfix is required.

%prep
%autosetup -p0

cp %{SOURCE1} .
cp %{SOURCE6} .

%build
export SENDMAIL=%{_sbindir}/sendmail
%configure
%make_build
%sysusers_generate_pre %{SOURCE3} spamass-milter

%install
%make_install

install -m 751 -d %{buildroot}%{_rundir}/spamass-milter
install -m 644 -D %{SOURCE2} \
	%{buildroot}%{_tmpfilesdir}/spamass-milter.conf
install -m 644 -D %{SOURCE3} \
	%{buildroot}%{_sysusersdir}/spamass-milter.conf
install -m 644 -D %{SOURCE4} %{buildroot}%{_unitdir}/spamass-milter.service
%if 0%{?suse_version} == 1500
install -m 644 -D %{SOURCE5} \
	%{buildroot}%{_sysconfdir}/default/spamass-milter
%else
install -m 644 -D %{SOURCE5} \
	%{buildroot}%{_distconfdir}/default/spamass-milter
%endif
# Create dummy sockets for %%ghost-ing
: > %{buildroot}%{_rundir}/spamass-milter/socket

%pre -f spamass-milter.pre
%service_add_pre spamass-milter.service

%post
%tmpfiles_create spamass-milter.conf
%service_add_post spamass-milter.service

%preun
%service_del_preun spamass-milter.service

%postun
%service_del_postun spamass-milter.service

%files
%doc README.postfix
%license COPYING
%{_mandir}/man1/spamass-milter.1%{?ext_man}
%if 0%{?suse_version} == 1500
%config %{_sysconfdir}/default/spamass-milter
%else
%config %{_distconfdir}/default/spamass-milter
%endif
%{_tmpfilesdir}/spamass-milter.conf
%{_sysusersdir}/spamass-milter.conf
%{_unitdir}/spamass-milter.service
%{_sbindir}/spamass-milter
%ghost %dir %attr(751,sa-milter,postfix) %{_rundir}/spamass-milter/
%ghost %attr(-,sa-milter,postfix) %{_rundir}/spamass-milter/socket

%changelog
