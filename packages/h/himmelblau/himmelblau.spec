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
Version:        0.8.0+git.0.249ba5f
Release:        0
Summary:        Interoperability suite for Microsoft Azure Entra Id
License:        GPL-3.0-or-later
URL:            https://github.com/himmelblau-idm/himmelblau
Group:          Productivity/Networking/Security
Source:         %{name}-%{version}.tar.bz2
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  binutils
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  dbus-1-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libclang13
BuildRequires:  libdhash-devel
BuildRequires:  libopenssl-3-devel
BuildRequires:  pam-devel
BuildRequires:  patchelf
BuildRequires:  pcre2-devel
BuildRequires:  sqlite3-devel
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  utf8proc-devel
%if 0%{?sle_version} > 150600
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  libsoup-devel
BuildRequires:  libudev-devel
BuildRequires:  mercurial
BuildRequires:  pango-devel
BuildRequires:  python3-gyp
BuildRequires:  webkit2gtk3-devel
%endif
BuildRequires:  systemd-devel
ExclusiveArch:  %{rust_tier1_arches}
Recommends:     libnss_himmelblau2
Recommends:     pam-himmelblau
Provides:       aad-cli
Provides:       aad-common
Provides:       authd
Provides:       authd-msentraid
%if 0%{?is_opensuse}
Suggests:       himmelblau-sso
%endif
Requires:       man
# This is necessary to prevent users from installing Himmelblau along side
# Microsoft's Broker, as these will conflict.
Provides:       microsoft-identity-broker

%description
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n pam-himmelblau
Summary:        Azure Entra Id authentication PAM module
Requires:       %{name} = %{version}
Provides:       libpam-aad
Suggests:       himmelblau-sshd-config

%description -n pam-himmelblau
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n libnss_himmelblau2
Summary:        Azure Entra Id authentication NSS module
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires:       %{name}
Provides:       libnss-aad
Provides:       nss-himmelblau

%description -n libnss_himmelblau2
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n himmelblau-sshd-config
Summary:        Azure Entra Id SSHD Configuration
Requires:       %{name} = %{version}
Requires:       openssh-server
BuildRequires:  openssh-server
BuildArch:      noarch

%description -n himmelblau-sshd-config
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%if 0%{?is_opensuse}
# SLE doesn't provide python3-pydbus
%package -n himmelblau-sso
Summary:        Azure Entra Id Firefox SSO Configuration
Requires:       %{name} = %{version}
Requires:       MozillaFirefox
Requires:       python3-pydbus
Provides:       linux-entra-sso

%description -n himmelblau-sso
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.
%endif

%post   -n libnss_himmelblau2 -p /sbin/ldconfig
%postun -n libnss_himmelblau2 -p /sbin/ldconfig

%prep
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
# Dependencies for interative Hello PIN changes aren't present prior to 15.6
%if 0%{?sle_version} <= 150600
%{cargo_build}
%else
%{cargo_build} --features interactive
%endif

%check

%{cargo_test}

%install
install -D -d -m 0755 %{buildroot}/%{_sysconfdir}/himmelblau
cp src/config/himmelblau.conf.example %{buildroot}/%{_sysconfdir}/himmelblau/himmelblau.conf
cp target/release/libnss_%{name}.so target/release/libnss_%{name}.so.2
install -D -d -m 0755 %{buildroot}/%{_libdir}
strip --strip-unneeded target/release/libnss_himmelblau.so.2
patchelf --set-soname libnss_himmelblau.so.2 target/release/libnss_himmelblau.so.2
install -m 0755 target/release/libnss_%{name}.so.2 %{buildroot}/%{_libdir}
install -D -d -m 0755 %{buildroot}/%{_pam_moduledir}
strip --strip-unneeded target/release/libpam_himmelblau.so
install -m 0755 target/release/libpam_%{name}.so %{buildroot}/%{_pam_moduledir}/pam_%{name}.so
install -D -d -m 0755 %{buildroot}%{_sbindir}
strip --strip-unneeded target/release/himmelblaud
strip --strip-unneeded target/release/himmelblaud_tasks
strip --strip-unneeded target/release/broker
install -m 0755 target/release/himmelblaud %{buildroot}/%{_sbindir}
install -m 0755 target/release/himmelblaud_tasks %{buildroot}/%{_sbindir}
install -m 0755 target/release/broker %{buildroot}/%{_sbindir}
pushd %{buildroot}%{_sbindir}
ln -s himmelblaud rchimmelblaud
ln -s himmelblaud_tasks rchimmelblaud_tasks
ln -s broker rcbroker
popd
install -D -d -m 0755 %{buildroot}%{_bindir}
strip --strip-unneeded target/release/aad-tool
install -m 0755 target/release/aad-tool %{buildroot}/%{_bindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{_builddir}/%{name}-%{version}/platform/opensuse/himmelblaud.service %{buildroot}%{_unitdir}/himmelblaud.service
install -m 0644 %{_builddir}/%{name}-%{version}/platform/opensuse/himmelblaud-tasks.service %{buildroot}%{_unitdir}/himmelblaud-tasks.service
install -D -d -m 0755 %{buildroot}%{_datarootdir}/dbus-1/services
install -m 0644 %{_builddir}/%{name}-%{version}/platform/opensuse/com.microsoft.identity.broker1.service %{buildroot}%{_datarootdir}/dbus-1/services/
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
install -m 0644 %{_builddir}/%{name}-%{version}/platform/el/sshd_config %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/himmelblau.conf
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/krb5.conf.d
install -m 0644 %{_builddir}/%{name}-%{version}/src/config/krb5_himmelblau.conf %{buildroot}%{_sysconfdir}/krb5.conf.d/krb5_himmelblau.conf

# Firefox Single Sign On
%if 0%{?is_opensuse}
install -m 0755 %{_builddir}/%{name}-%{version}/src/sso/src/linux-entra-sso.py %{buildroot}/%{_bindir}/linux-entra-sso
sed -i 's/#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/' %{buildroot}/%{_bindir}/linux-entra-sso
install -D -d -m 0755 %{buildroot}%{_libdir}/mozilla/native-messaging-hosts
install -m 0644 %{_builddir}/%{name}-%{version}/src/sso/src/firefox/linux_entra_sso.json %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/firefox/policies
install -m 0644 %{_builddir}/%{name}-%{version}/src/sso/src/firefox/policies.json %{buildroot}%{_sysconfdir}/firefox/policies/
%endif

# Man pages
install -D -d -m 0755 %{buildroot}%{_mandir}/man1
install -D -d -m 0755 %{buildroot}%{_mandir}/man5
install -D -d -m 0755 %{buildroot}%{_mandir}/man8
install -m 0644 %{_builddir}/%{name}-%{version}/man/man1/aad-tool.1 %{buildroot}%{_mandir}/man1/
install -m 0644 %{_builddir}/%{name}-%{version}/man/man5/himmelblau.conf.5 %{buildroot}%{_mandir}/man5/
install -m 0644 %{_builddir}/%{name}-%{version}/man/man8/himmelblaud.8 %{buildroot}%{_mandir}/man8/
install -m 0644 %{_builddir}/%{name}-%{version}/man/man8/himmelblaud_tasks.8 %{buildroot}%{_mandir}/man8/

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
%config(noreplace) %{_sysconfdir}/himmelblau/himmelblau.conf
%{_sysconfdir}/krb5.conf.d/krb5_himmelblau.conf
%{_sbindir}/himmelblaud
%{_sbindir}/rchimmelblaud
%{_sbindir}/himmelblaud_tasks
%{_sbindir}/rchimmelblaud_tasks
%{_sbindir}/broker
%{_sbindir}/rcbroker
%{_bindir}/aad-tool
%{_unitdir}/himmelblaud.service
%{_unitdir}/himmelblaud-tasks.service
%{_datarootdir}/dbus-1/services/com.microsoft.identity.broker1.service
%{_mandir}/man1/aad-tool.1*
%{_mandir}/man5/himmelblau.conf.5*
%{_mandir}/man8/himmelblaud.8*
%{_mandir}/man8/himmelblaud_tasks.8*

%files -n libnss_himmelblau2
%{_libdir}/libnss_%{name}.so.*

%files -n pam-himmelblau
%{_pam_moduledir}/pam_%{name}.so

%files -n himmelblau-sshd-config
# openssh-server doesn't own /etc/ssh/sshd_config.d before 15.5
%if 0%{?sle_version} <= 150500
%dir %{_sysconfdir}/ssh/sshd_config.d
%endif
%config %{_sysconfdir}/ssh/sshd_config.d/himmelblau.conf

%if 0%{?is_opensuse}
%files -n himmelblau-sso
%{_bindir}/linux-entra-sso
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/native-messaging-hosts
%{_libdir}/mozilla/native-messaging-hosts/linux_entra_sso.json
%dir %{_sysconfdir}/firefox
%dir %{_sysconfdir}/firefox/policies
%config %{_sysconfdir}/firefox/policies/policies.json
%endif

%changelog
