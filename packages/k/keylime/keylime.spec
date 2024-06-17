#
# spec file for package keylime
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


%global srcname keylime
%define skip_python2 1
# Consolidate _distconfdir and _sysconfdir
%if 0%{?_distconfdir:1}
  %define _config_norepl %{nil}
%else
  %define _distconfdir   %{_sysconfdir}
  %define _config_norepl %config(noreplace)
%endif
Name:           keylime
Version:        7.11.0
Release:        0
Summary:        Open source TPM software for Bootstrapping and Maintaining Trust
License:        Apache-2.0 AND MIT AND BSD-3-Clause
URL:            https://github.com/keylime/keylime
Source0:        %{name}-v%{version}.tar.xz
Source1:        keylime.xml
Source2:        %{name}-user.conf
Source3:        logrotate.%{name}
Source4:        tmpfiles.%{name}
# openSUSE adjustments for generated configuration files
Source10:       registrar.conf.diff
Source11:       verifier.conf.diff
Source12:       tenant.conf.diff
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  firewall-macros
BuildRequires:  python-rpm-macros
BuildRequires:  sysuser-tools
Requires:       libtss2-tcti-device0
Requires:       libtss2-tcti-tabrmd0
Requires:       procps
Requires:       python3-PyYAML
Requires:       python3-SQLAlchemy
Requires:       python3-alembic
Requires:       python3-cryptography
Requires:       python3-gpg
Requires:       python3-jsonschema
Requires:       python3-lark
Requires:       python3-packaging
Requires:       python3-psutil
Requires:       python3-pyzmq
Requires:       python3-requests
Requires:       python3-tornado
Requires:       python3-typing_extensions
Requires:       tpm2-0-tss
Requires:       tpm2.0-abrmd
Requires:       tpm2.0-tools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      rust-keylime
BuildArch:      noarch
%python_subpackages

%description
Keylime is a TPM based highly scalable remote boot attestation
and runtime integrity measurement solution.

%package -n %{name}-config
Summary:        Configuration file for keylime
Requires:       python3-%{name} = %{version}
Conflicts:      rust-keylime

%description -n %{name}-config
Subpackage of %{name} for the shared configuration files for the agent
and the server components.

%package -n %{name}-firewalld
Summary:        Firewalld service file for keylime
Requires:       python3-%{name} = %{version}
Conflicts:      rust-keylime

%description -n %{name}-firewalld
Subpackage of %{name} for the firewalld XML service file.

%package -n %{name}-tpm_cert_store
Summary:        Certify store for the TPM
Requires:       python3-%{name} = %{version}
Conflicts:      rust-keylime
Provides:       user(keylime)
%sysusers_requires

%description -n %{name}-tpm_cert_store
Subpackage of %{name} for storing the TPM certificates.

%package -n %{name}-registrar
Summary:        Keylime registrar service
Requires:       %{name}-config = %{version}
Requires:       %{name}-logrotate = %{version}
Requires:       %{name}-tpm_cert_store = %{version}
Requires:       python3-%{name} = %{version}
Recommends:     %{name}-firewalld = %{version}
Conflicts:      rust-keylime

%description -n %{name}-registrar
Subpackage of %{name} for registrar service.

%package -n %{name}-verifier
Summary:        Keylime verifier service
Requires:       %{name}-config = %{version}
Requires:       %{name}-logrotate = %{version}
Requires:       %{name}-tpm_cert_store = %{version}
Requires:       python3-%{name} = %{version}
Recommends:     %{name}-firewalld = %{version}
Conflicts:      rust-keylime

%description -n %{name}-verifier
Subpackage of %{name} for verifier service.

%package -n %{name}-tenant
Summary:        Keylime tenant command line tool
Requires:       %{name}-config = %{version}
Requires:       %{name}-tpm_cert_store = %{version}
Requires:       python3-%{name} = %{version}
Recommends:     %{name}-firewalld = %{version}
Conflicts:      rust-keylime

%description -n %{name}-tenant
Subpackage of %{name} for tenant command line tool.

%package -n %{name}-logrotate
Summary:        Logrotate for Keylime servies
Requires:       logrotate
Conflicts:      rust-keylime

%description -n %{name}-logrotate
Subpackage of %{name} for logrotate for Keylime services

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%python_build
%sysusers_generate_pre %{SOURCE2} %{name} %{name}-user.conf

%install
export VERSION=%{version}
%python_install

rm config/agent.conf
patch -s --fuzz=0 config/registrar.conf < %{SOURCE10}
patch -s --fuzz=0 config/verifier.conf < %{SOURCE11}
patch -s --fuzz=0 config/tenant.conf < %{SOURCE12}

%python_clone -a %{buildroot}%{_bindir}/%{srcname}_attest
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_ca
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_convert_runtime_policy
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_create_policy
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_registrar
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_sign_runtime_policy
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_tenant
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_upgrade_config
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_userdata_encrypt
%python_clone -a %{buildroot}%{_bindir}/%{srcname}_verifier

%python_expand %fdupes %{buildroot}%{$python_sitelib}

for cfg in config/*.conf; do
  install -Dpm 0600 "$cfg" %{buildroot}%{_distconfdir}/%{srcname}/$(basename "$cfg")
done

install -Dpm 0644 ./services/%{srcname}_verifier.service %{buildroot}%{_unitdir}/%{srcname}_verifier.service
install -Dpm 0644 ./services/%{srcname}_registrar.service %{buildroot}%{_unitdir}/%{srcname}_registrar.service

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/%{srcname}.xml
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/%{name}-user.conf
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_distconfdir}/logrotate.d/%{name}
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -d %{buildroot}%{_localstatedir}/log/%{name}

mkdir -p %{buildroot}/%{_sharedstatedir}/%{srcname}
cp -r ./tpm_cert_store %{buildroot}%{_sharedstatedir}/%{srcname}/
%fdupes %{buildroot}%{_sharedstatedir}/%{srcname}/

# %%check
# %%pyunittest -v

%post
%python_install_alternative %{srcname}_attest
%python_install_alternative %{srcname}_ca
%python_install_alternative %{srcname}_convert_runtime_policy
%python_install_alternative %{srcname}_create_policy
%python_install_alternative %{srcname}_registrar
%python_install_alternative %{srcname}_sign_runtime_policy
%python_install_alternative %{srcname}_tenant
%python_install_alternative %{srcname}_upgrade_config
%python_install_alternative %{srcname}_userdata_encrypt
%python_install_alternative %{srcname}_verifier

%postun
%python_uninstall_alternative %{srcname}_attest
%python_uninstall_alternative %{srcname}_ca
%python_uninstall_alternative %{srcname}_convert_runtime_policy
%python_uninstall_alternative %{srcname}_create_policy
%python_uninstall_alternative %{srcname}_registrar
%python_uninstall_alternative %{srcname}_sign_runtime_policy
%python_uninstall_alternative %{srcname}_tenant
%python_uninstall_alternative %{srcname}_upgrade_config
%python_uninstall_alternative %{srcname}_userdata_encrypt
%python_uninstall_alternative %{srcname}_verifier

%post -n %{srcname}-firewalld
%firewalld_reload

%pre -n %{srcname}-tpm_cert_store -f %{srcname}.pre

%post -n %{srcname}-tpm_cert_store
%tmpfiles_create %{srcname}.conf

%pre -n %{srcname}-verifier
%service_add_pre %{srcname}_verifier.service

%post -n %{srcname}-verifier
%service_add_post %{srcname}_verifier.service

%preun -n %{srcname}-verifier
%service_del_preun %{srcname}_verifier.service

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

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/%{srcname}_attest
%python_alternative %{_bindir}/%{srcname}_ca
%python_alternative %{_bindir}/%{srcname}_convert_runtime_policy
%python_alternative %{_bindir}/%{srcname}_create_policy
%python_alternative %{_bindir}/%{srcname}_registrar
%python_alternative %{_bindir}/%{srcname}_sign_runtime_policy
%python_alternative %{_bindir}/%{srcname}_tenant
%python_alternative %{_bindir}/%{srcname}_upgrade_config
%python_alternative %{_bindir}/%{srcname}_userdata_encrypt
%python_alternative %{_bindir}/%{srcname}_verifier
%{python_sitelib}/keylime
%{python_sitelib}/keylime-%{version}*-info

%files -n %{srcname}-config
%dir %attr(0700,keylime,tss) %{_distconfdir}/%{srcname}
%_config_norepl %attr (0600,keylime,tss) %{_distconfdir}/%{srcname}/ca.conf
%_config_norepl %attr (0600,keylime,tss) %{_distconfdir}/%{srcname}/logging.conf

%files -n %{srcname}-firewalld
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{srcname}.xml

%files -n %{srcname}-tpm_cert_store
%dir %attr(0700,keylime,tss) %{_sharedstatedir}/%{srcname}
%dir %attr(0700,keylime,tss) %{_sharedstatedir}/%{srcname}/tpm_cert_store
%attr(0600,keylime,tss) %{_sharedstatedir}/%{srcname}/tpm_cert_store/*
# We use this subpackage to store other unrelated things, as far as is
# required by all the services
%{_sysusersdir}/%{srcname}-user.conf
%ghost %dir %attr(0700,keylime,tss) %{_rundir}/%{srcname}
%{_tmpfilesdir}/%{srcname}.conf

%files -n %{srcname}-registrar
%dir %attr(0700,keylime,tss) %{_distconfdir}/%{srcname}
%_config_norepl %attr (0600,keylime,tss) %{_distconfdir}/%{srcname}/registrar.conf
%{_unitdir}/%{srcname}_registrar.service

%files -n %{srcname}-verifier
%dir %attr(0700,keylime,tss) %{_distconfdir}/%{srcname}
%_config_norepl %attr (0600,keylime,tss) %{_distconfdir}/%{srcname}/verifier.conf
%{_unitdir}/%{srcname}_verifier.service

%files -n %{srcname}-tenant
%dir %attr(0700,keylime,tss) %{_distconfdir}/%{srcname}
%_config_norepl %attr (0600,keylime,tss) %{_distconfdir}/%{srcname}/tenant.conf

%files -n %{srcname}-logrotate
%_config_norepl %{_distconfdir}/logrotate.d/%{srcname}
%dir %attr(0750,keylime,tss) %{_localstatedir}/log/%{srcname}

%changelog
