#
# spec file for package himmelblau
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


Name:           himmelblau
Version:        0.4.0+git.2.7b57f5e
Release:        0
Summary:        Interoperability suite for Microsoft Azure AD and Intune
License:        MPL-2.0
URL:            https://github.com/openSUSE/himmelblau
Source:         %{name}-%{version}.tar.bz2
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libclang13
BuildRequires:  libdhash-devel
BuildRequires:  libldb-devel
BuildRequires:  libopenssl-3-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  sqlite3-devel
BuildRequires:  tpm2-0-tss-devel
ExclusiveArch:  %{rust_tier1_arches}
Recommends:     nss-himmelblau
Recommends:     pam-himmelblau
Provides:       aad-cli
Provides:       aad-common

%description
Himmelblau is an interoperability suite for Microsoft Azure AD and
Intune, which allows users to sign into a Linux machine using Azure
Active Directory credentials. It relies on the Microsoft
Authentication Library to communicate with the Microsoft service.

%package -n pam-himmelblau
Summary:        Azure AD authentication PAM module
Requires:       %{name} = %{version}
Provides:       libpam-aad

%description -n pam-himmelblau
Himmelblau is an interoperability suite for Microsoft Azure AD and
Intune, which allows users to sign into a Linux machine using Azure
Active Directory credentials. It relies on the Microsoft
Authentication Library to communicate with the Microsoft service.

%package -n nss-himmelblau
Summary:        Azure AD authentication NSS module
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires:       %{name} = %{version}
Provides:       libnss-aad

%description -n nss-himmelblau
Himmelblau is an interoperability suite for Microsoft Azure AD and
Intune, which allows users to sign into a Linux machine using Azure
Active Directory credentials. It relies on the Microsoft
Authentication Library to communicate with the Microsoft service.

%post   -n nss-himmelblau -p /sbin/ldconfig
%postun -n nss-himmelblau -p /sbin/ldconfig

%prep
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%check

%{cargo_test}

%install
install -D -d -m 0755 %{buildroot}/%{_sysconfdir}/himmelblau
cp src/config/himmelblau.conf.example %{buildroot}/%{_sysconfdir}/himmelblau/himmelblau.conf
cp target/release/libnss_%{name}.so target/release/libnss_%{name}.so.2
install -D -d -m 0755 %{buildroot}/%{_libdir}
install -m 0755 target/release/libnss_%{name}.so.2 %{buildroot}/%{_libdir}
install -D -d -m 0755 %{buildroot}/%{_pam_moduledir}
install -m 0755 target/release/libpam_%{name}.so %{buildroot}/%{_pam_moduledir}/pam_%{name}.so
install -D -d -m 0755 %{buildroot}%{_sbindir}
install -m 0755 target/release/himmelblaud %{buildroot}/%{_sbindir}
install -m 0755 target/release/himmelblaud_tasks %{buildroot}/%{_sbindir}
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/aad-tool %{buildroot}/%{_bindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{_builddir}/%{name}-%{version}/platform/opensuse/himmelblaud.service %{buildroot}%{_unitdir}/himmelblaud.service
install -m 0644 %{_builddir}/%{name}-%{version}/platform/opensuse/himmelblaud-tasks.service %{buildroot}%{_unitdir}/himmelblaud-tasks.service

%pre
%service_add_pre himmelblaud.service himmelblaud-tasks.service

%post
%service_add_post himmelblaud.service himmelblaud-tasks.service

%preun
%service_del_preun himmelblaud.service himmelblaud-tasks.service

%postun
%service_del_postun himmelblaud.service himmelblaud-tasks.service

%files
%dir %{_sysconfdir}/himmelblau
%config %{_sysconfdir}/himmelblau/himmelblau.conf
%{_sbindir}/himmelblaud
%{_sbindir}/himmelblaud_tasks
%{_bindir}/aad-tool
%{_unitdir}/himmelblaud.service
%{_unitdir}/himmelblaud-tasks.service

%files -n nss-himmelblau
%{_libdir}/libnss_%{name}.so.*

%files -n pam-himmelblau
%{_pam_moduledir}/pam_%{name}.so

%changelog
