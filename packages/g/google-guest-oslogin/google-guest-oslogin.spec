#
# spec file for package google-guest-oslogin
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


%{!?_pam_moduledir: %define _pam_moduledir %{_pamdir}}

Name:           google-guest-oslogin
Version:        20240701.00
Release:        0
Summary:        Google Cloud Guest OS Login
License:        Apache-2.0
Group:          System/Daemons
URL:            https://github.com/GoogleCloudPlatform/guest-oslogin
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       openssh
Requires:       pam
Requires(post): glibc
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libjson-c-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  systemd-rpm-macros
Requires:       google-guest-agent >= 20231003
Requires:       google-guest-configs
Provides:       google-compute-engine-oslogin = %{version}
Obsoletes:      google-compute-engine-oslogin < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Google Cloud Guest OS Login

%prep
%setup -q -n guest-oslogin-%{version}

%build
%if 0%{?suse_version} && 0%{?suse_version} > 1315
make %{?_smp_mflags} VERSION=%{version}
%else
make %{?_smp_mflags} LDLIBS='-lcurl -ljson-c -lboost_regex' VERSION=%{version}
%endif

%install
make install DESTDIR=%{buildroot} LIBDIR=/%{_libdir} PAMDIR=%{_pam_moduledir} SYSTEMDDIR=%{_unitdir} PRESETDIR=%{_presetdir} VERSION=%{version}
mkdir -p %{buildroot}%{_sbindir}
for srv_name in %{buildroot}%{_unitdir}/*.service; do rc_name=$(basename -s '.service' $srv_name); ln -s service %{buildroot}%{_sbindir}/rc$rc_name; done

%pre
%service_add_pre google-oslogin-cache.service

%preun
%service_del_preun google-oslogin-cache.service

%post
/sbin/ldconfig
%service_add_post google-oslogin-cache.service

%postun
/sbin/ldconfig
%service_del_postun google-oslogin-cache.service

%files
%defattr(0644,root,root,0755)
%doc README.md
%license LICENSE
%attr(0755,root,root) %{_bindir}/google_authorized_keys
%attr(0755,root,root) %{_bindir}/google_authorized_keys_sk
%attr(0755,root,root) %{_bindir}/google_authorized_principals
%attr(0755,root,root) %{_bindir}/google_oslogin_nss_cache
%{_mandir}/man8/*
%{_libdir}/libnss*
%{_pam_moduledir}/*
%{_presetdir}/*
%{_sbindir}/*
%{_unitdir}/*

%changelog
