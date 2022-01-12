#
# spec file for package keylime
#
# Copyright (c) 2022 SUSE LLC
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


%global srcname keylime
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%if 0%{?suse_version} >= 1550
%bcond_without cfssl
%else
%bcond_with cfssl
%endif
Name:           keylime
Version:        6.2.1
Release:        0
Summary:        Open source TPM software for Bootstrapping and Maintaining Trust
License:        Apache-2.0 AND MIT
URL:            https://github.com/keylime/keylime
Source0:        %{name}-v%{version}.tar.xz
Source1:        keylime.xml
# PATCH-FIX-OPENSUSE version.diff
Patch1:         version.diff
# PATCH-FIX-OPENSUSE keylime.conf.diff
Patch2:         keylime.conf.diff
# PATCH-FIX-OPENSUSE config-libefivars.diff
Patch3:         config-libefivars.diff
# PATCH-FIX-UPSTREAM 0001-Drop-dataclasses-module-usage.patch (gh#keylime/keylime!827)
Patch4:         0001-Drop-dataclasses-module-usage.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  firewall-macros
BuildRequires:  python-rpm-macros
Requires:       libtss2-tcti-device0
Requires:       libtss2-tcti-tabrmd0
Requires:       procps
Requires:       python-M2Crypto
Requires:       python-PyYAML
Requires:       python-SQLAlchemy
Requires:       python-alembic
Requires:       python-cryptography
Requires:       python-psutil
Requires:       python-python-gnupg
Requires:       python-pyzmq
Requires:       python-requests
Requires:       python-simplejson
Requires:       python-tornado
Requires:       tpm2-0-tss
Requires:       tpm2.0-abrmd
Requires:       tpm2.0-tools
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Keylime is a TPM based highly scalable remote boot attestation
and runtime integrity measurement solution.

%package -n %{name}-config
Summary:        Configuration file for keylime
Requires:       python3-%{name} = %{version}

%description -n %{name}-config
Subpackage of %{name} for the shared configuration file of the agent
and the server components.

%package -n %{name}-firewalld
Summary:        Firewalld service file for keylime
Requires:       python3-%{name} = %{version}

%description -n %{name}-firewalld
Subpackage of %{name} for the firewalld XML service file.

%package -n %{name}-tpm_cert_store
Summary:        Certify store for the TPM
Requires:       python3-%{name} = %{version}

%description -n %{name}-tpm_cert_store
Subpackage of %{name} for storing the TPM certificates.

%package -n %{name}-agent
Summary:        Keylime agent service
Requires:       %{name}-config = %{version}
Requires:       %{name}-tpm_cert_store = %{version}
Requires:       python3-%{name} = %{version}
Recommends:     %{name}-firewalld = %{version}
Recommends:     dmidecode

%description -n %{name}-agent
Subpackage of %{name} for agent service.

%package -n %{name}-registrar
Summary:        Keylime registrar service
Requires:       %{name}-config = %{version}
Requires:       %{name}-tpm_cert_store = %{version}
Requires:       python3-%{name} = %{version}
Recommends:     %{name}-firewalld = %{version}
Recommends:     cfssl

%description -n %{name}-registrar
Subpackage of %{name} for registrar service.

%package -n %{name}-verifier
Summary:        Keylime verifier service
Requires:       %{name}-config = %{version}
Requires:       %{name}-tpm_cert_store = %{version}
Requires:       python3-%{name} = %{version}
Recommends:     %{name}-firewalld = %{version}

%description -n %{name}-verifier
Subpackage of %{name} for verifier service.

%prep
%autosetup -p1 -n %{name}-v%{version}
%if !%{with cfssl}
sed -i "s/ca_implementation = cfssl/ca_implementation = openssl/g" keylime.conf
%endif

%build
%python_build

%install
export VERSION=%{version}
%python_install

cp -r %{srcname}/static %{buildroot}%{python_sitelib}/%{srcname}

%python_clone -a %{buildroot}%{_bindir}/%{srcname}_verifier
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_registrar
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_agent
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_tenant
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_ca
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_migrations_apply
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_provider_platform_init
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_provider_registrar
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_provider_vtpm_add
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_userdata_encrypt
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_ima_emulator
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_webapp

%python_expand %fdupes %{buildroot}%{$python_sitelib}

install -Dpm 600 %{srcname}.conf %{buildroot}%{_sysconfdir}/%{srcname}.conf
install -Dpm 644 ./services/%{srcname}_agent.service %{buildroot}%{_unitdir}/%{srcname}_agent.service
install -Dpm 644 ./services/%{srcname}_verifier.service %{buildroot}%{_unitdir}/%{srcname}_verifier.service
install -Dpm 644 ./services/%{srcname}_registrar.service %{buildroot}%{_unitdir}/%{srcname}_registrar.service

install -D -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/keylime.xml

mkdir -p %{buildroot}/%{_sharedstatedir}/%{srcname}
cp -r ./tpm_cert_store %{buildroot}%{_sharedstatedir}/%{srcname}/
%fdupes %{buildroot}%{_sharedstatedir}/%{srcname}/

# %%check
# %%pyunittest -v

%post
%python_install_alternative %{srcname}_verifier
%python_install_alternative %{srcname}_registrar
%python_install_alternative %{srcname}_agent
%python_install_alternative %{srcname}_tenant
%python_install_alternative %{srcname}_ca
%python_install_alternative %{srcname}_migrations_apply
%python_install_alternative %{srcname}_provider_platform_init
%python_install_alternative %{srcname}_provider_registrar
%python_install_alternative %{srcname}_provider_vtpm_add
%python_install_alternative %{srcname}_userdata_encrypt
%python_install_alternative %{srcname}_ima_emulator
%python_install_alternative %{srcname}_webapp

%postun
%python_uninstall_alternative %{srcname}_verifier
%python_uninstall_alternative %{srcname}_registrar
%python_uninstall_alternative %{srcname}_agent
%python_uninstall_alternative %{srcname}_tenant
%python_uninstall_alternative %{srcname}_ca
%python_uninstall_alternative %{srcname}_migrations_apply
%python_uninstall_alternative %{srcname}_provider_platform_init
%python_uninstall_alternative %{srcname}_provider_registrar
%python_uninstall_alternative %{srcname}_provider_vtpm_add
%python_uninstall_alternative %{srcname}_userdata_encrypt
%python_uninstall_alternative %{srcname}_ima_emulator
%python_uninstall_alternative %{srcname}_webapp

%post -n %{srcname}-firewalld
%firewalld_reload

%pre -n %{srcname}-verifier
%service_add_pre %{srcname}_verifier.service

%post -n %{srcname}-verifier
%service_add_post %{srcname}_verifier.service

%preun -n %{srcname}-verifier
%service_del_preun %{srcname}_agent.service

%postun -n %{srcname}-verifier
%service_del_postun %{srcname}_verifier.service

%pre -n %{srcname}-registrar
%service_add_pre %{srcname}_registrar.service

%post -n %{srcname}-registrar
%service_add_post %{srcname}_registrar.service

%preun -n %{srcname}-registrar
%service_del_preun %{srcname}_registrar.service

%postun -n %{srcname}-registrar
%service_del_postun %{srcname}_registrar.service

%pre -n %{srcname}-agent
%service_add_pre %{srcname}_agent.service

%post -n %{srcname}-agent
%service_add_post %{srcname}_agent.service

%preun -n %{srcname}-agent
%service_del_preun %{srcname}_agent.service

%postun -n %{srcname}-agent
%service_del_postun %{srcname}_agent.service

%files %{python_files}
%doc README.md
%license LICENSE keylime/static/icons/ICON-LICENSE
%python_alternative %{_bindir}/%{srcname}_verifier
%python_alternative %{_bindir}/%{srcname}_registrar
%python_alternative %{_bindir}/%{srcname}_agent
%python_alternative %{_bindir}/%{srcname}_tenant
%python_alternative %{_bindir}/%{srcname}_ca
%python_alternative %{_bindir}/%{srcname}_migrations_apply
%python_alternative %{_bindir}/%{srcname}_provider_platform_init
%python_alternative %{_bindir}/%{srcname}_provider_registrar
%python_alternative %{_bindir}/%{srcname}_provider_vtpm_add
%python_alternative %{_bindir}/%{srcname}_userdata_encrypt
%python_alternative %{_bindir}/%{srcname}_ima_emulator
%python_alternative %{_bindir}/%{srcname}_webapp
%{python_sitelib}/*

%files -n %{srcname}-config
%config(noreplace) %{_sysconfdir}/%{srcname}.conf

%files -n %{srcname}-firewalld
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/keylime.xml

%files -n %{srcname}-tpm_cert_store
%dir %{_sharedstatedir}/keylime
%dir %{_sharedstatedir}/keylime/tpm_cert_store
%{_sharedstatedir}/keylime/tpm_cert_store/*

%files -n %{srcname}-verifier
%{_unitdir}/%{srcname}_verifier.service

%files -n %{srcname}-registrar
%{_unitdir}/%{srcname}_registrar.service

%files -n %{srcname}-agent
%{_unitdir}/%{srcname}_agent.service

%changelog
