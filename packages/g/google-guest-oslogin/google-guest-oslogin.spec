#
# spec file for package google-guest-oslogin
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 01500
%bcond_without use_selinux
%define selinuxtype targeted
%else
%bcond_with use_selinux
%endif

%{!?_pam_moduledir: %define _pam_moduledir %{_pamdir}}

Name:           google-guest-oslogin
Version:        20251022.00
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
BuildRequires:  checkpolicy
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libjson-c-devel
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  policycoreutils
BuildRequires:  systemd-rpm-macros
%if %{with use_selinux}
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-%{selinuxtype}
BuildRequires:  selinux-policy-devel
BuildRequires:  pkgconfig(systemd)
%endif
Requires:       google-guest-agent >= 20231003
Requires:       google-guest-configs
%if %{with use_selinux}
Requires:       (%{name}-selinux if selinux-policy-base)
%endif
Provides:       google-compute-engine-oslogin = %{version}
Obsoletes:      google-compute-engine-oslogin < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Google Cloud Guest OS Login

%if %{with use_selinux}
%package        selinux
Summary:        SELinux module for Google Cloud Guest OS Login
Requires:       %{name} = %{version}
BuildArch:      noarch
%{selinux_requires}

%description    selinux
This package provides the SELinux module for Google Cloud Guest OS Login.
%endif

%prep
%setup -q -n guest-oslogin-%{version}

%build
%if 0%{?suse_version} && 0%{?suse_version} > 1315
make %{?_smp_mflags} VERSION=%{version}
%else
make %{?_smp_mflags} LDLIBS='-lcurl -ljson-c -lboost_regex' VERSION=%{version}
%endif

%install
make install \
     DESTDIR=%{buildroot} \
     LIBDIR=/%{_libdir} \
     PAMDIR=%{_pam_moduledir} \
     SYSTEMDDIR=%{_unitdir} \
     PRESETDIR=%{_presetdir} \
     INSTALL_SELINUX=y \
     VERSION=%{version}

%if %{with use_selinux}
mkdir %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
mv %{buildroot}%{_datadir}/selinux/packages/oslogin.pp %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
%endif

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

%if %{with use_selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/%{selinuxtype}/oslogin.pp

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 oslogin
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}
%endif

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
%if %{without use_selinux}
%{_datadir}/selinux
%{_datadir}/selinux/packages
%{_datadir}/selinux/packages/oslogin.pp
%endif

%if %{with use_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/oslogin.pp
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/oslogin
%endif

%changelog
