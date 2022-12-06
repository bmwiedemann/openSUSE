#
# spec file
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


%bcond_without use_poetry_for_dependencies

# NOTE: Keep this is in the same order as pyproject.toml.
%if %{with use_poetry_for_dependencies}
%global Jinja2_version                3.1.2
%global Pillow_version                9.3.0
%global PyYAML_version                6.0
%global Twisted_version               22.10.0
%global attrs_version                 22.1.0
%global bcrypt_version                3.2.0
%global bleach_version                3.3.0
%global canonicaljson_version         1.6.4
%global canonicaljson_max_version     2
%global cryptography_version          38.0.3
%global frozendict_version            2.3.3
%global idna_version                  3.3
%global ijson_version                 3.1.4
%global jsonschema_version            4.17.0
%global matrix_common_version         1.3.0
%global matrix_common_max_version     2
%global msgpack_version               1.0.3
%global netaddr_version               0.8.0
%global phonenumbers_version          8.12.44
%global prometheus_client_version     0.15.0
%global psutil_version                2.0.0
%global pyOpenSSL_version             22.0.0
%global pyasn1_version                0.4.8
%global pyasn1_modules_version        0.2.8
%global pymacaroons_version           0.13.0
%global service_identity_version      21.1.0
%global signedjson_version            1.1.4
%global signedjson_max_version        2
%global sortedcontainers_version      2.4.0
%global systemd_version               234
%global typing_extensions_version     4.1.1
%global treq_version                  22.2.0
%global unpaddedbase64_version        2.1.0
%global matrix_synapse_ldap3_version  0.2.1
%global packaging_version             21.3
%global psycopg2_version              2.9.5
%global pysaml2_version               7.2.1
%global Authlib_version               0.15.5
%global lxml_version                  4.8.0
%global sentry_sdk_version            1.10.1
%global PyJWT_version                 2.4.0
%global jaeger_client_version         4.8.0
%global opentracing_version           2.4.0
%global hiredis_version               2.0.0
%global txredisapi_version            1.4.7
%global Pympler_version               1.0.1
%global pydantic_version              1.9.1
%else
# some version locks based on poetry.lock
%global Jinja2_version                3.0
%global Pillow_version                5.4.0
%global PyYAML_version                3.11
%global Twisted_version               18.9.0
%global attrs_version                 21.1.1
%global bcrypt_version                3.1.7
%global bleach_version                1.4.3
%global canonicaljson_version         1.6.3
%global canonicaljson_max_version     2
%global cryptography_version          3.4.7
%global frozendict_version            2.1.3
%global idna_version                  2.5
%global ijson_version                 3.1.4
%global jsonschema_version            3.0.0
%global matrix_common_version         1.3.0
%global matrix_common_max_version     2
%global msgpack_version               0.5.2
%global netaddr_version               0.7.18
%global phonenumbers_version          8.2.0
%global prometheus_client_version     0.4.0
%global psutil_version                2.0.0
%global pyOpenSSL_version             16.0.0
%global pyasn1_version                0.1.9
%global pyasn1_modules_version        0.0.7
%global pymacaroons_version           0.13.0
%global service_identity_version      18.1.0
%global signedjson_version            1.1.0
%global signedjson_max_version        2
%global sortedcontainers_version      1.4.4
%global systemd_version               231
%global typing_extensions_version     3.10.0
%global treq_version                  15.1
%global unpaddedbase64_version        2.1.0
%global matrix_synapse_ldap3_version  0.2.1
%global packaging_version             16.1
%global psycopg2_version              2.8
%global pysaml2_version               4.5.0
%global Authlib_version               0.15.1
%global lxml_version                  4.8.0
%global sentry_sdk_version            1.5.11
%global PyJWT_version                 1.6.4
%global jaeger_client_version         4.0.0
%global opentracing_version           2.2.0
%global hiredis_version               2.0.0
%global txredisapi_version            1.4.7
%global Pympler_version               1.0.1
%global pydantic_version              1.7.4
%endif

%define requires_peq() %(echo '%*' | LC_ALL=C xargs -r rpm -q --whatprovides --qf 'Requires: %%{name} = %%{epoch}:%%{version}\\n' | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")
%define pythons python3

# These come from matrix-synapse's CONDITIONAL_REQUIREMENTS.
# missing deps
%if 0%{?suse_version} >= 1550
%bcond_without synapse_oidc
%else
%bcond_with    synapse_oidc
%endif
%bcond_with    synapse_redis
%bcond_with    synapse_opentracing
%bcond_with    synapse_sentry
# matrix-synapse-ldap isn't packaged on openSUSE.
%bcond_with    synapse_ldap

## Package updates
#
# * Update version in _service to the most recent released one
# * Call `osc service dr`
# * Update changelog manually from
#   https://github.com/matrix-org/synapse/releases or synapse/CHANGES.md
# * Commit+submit

#if 0%{?suse_version} >= 1550
#define use_python python38
#define __python3 #{_bindir}/python3
#else
%define use_python python310
#endif

%define         modname synapse
%define         pkgname matrix-synapse
%define         eggname matrix_synapse
Name:           %{pkgname}
Version:        1.72.0
Release:        0
Summary:        Matrix protocol reference homeserver
License:        Apache-2.0
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/matrix-org/synapse
Source0:        %{pkgname}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source47:       matrix-synapse-user.conf
Source48:       README.SUSE
Source49:       matrix-synapse.tmpfiles.d
Source50:       %{pkgname}.service
Source51:       matrix-synapse-generate-config.sh
# track series file so we can easily use quilt
# cd synapse ; ln -s .. patches ; quilt push -a
# to clean up your working copy afterwards: git reset --hard ; rm -rv .pc patches
Source99:       series
Patch:          matrix-synapse-1.4.1-paths.patch
Patch1:         bump-dependencies.patch
# https://github.com/matrix-org/synapse/pull/10719
# disable by marking as source until we get a decision upstream
Source100:      10719-Fix-instert-of-duplicate-key-into-event_json.patch
BuildRequires:  %{use_python}-base >= 3.8
BuildRequires:  %{use_python}-pip
BuildRequires:  %{use_python}-poetry-core >= 1.0.0
BuildRequires:  %{use_python}-setuptools
BuildRequires:  %{use_python}-wheel
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  unzip
%{?systemd_ordering}
%{sysusers_requires}
%requires_peq   %{use_python}-base
BuildRequires:  (%{use_python}-setuptools-rust >= 1.3 with %{use_python}-setuptools-rust < 1.5.3)
# NOTE: Keep this is in the same order as pyproject.toml.
# some version locks based on poetry.lock
BuildRequires:  %{use_python}-Jinja2 >= %{Jinja2_version}
%requires_peq   %{use_python}-Jinja2
BuildRequires:  %{use_python}-Pillow >= %{Pillow_version}
%requires_peq   %{use_python}-Pillow
BuildRequires:  %{use_python}-PyYAML >= %{PyYAML_version}
%requires_peq   %{use_python}-PyYAML
BuildRequires:  %{use_python}-Twisted >= %{Twisted_version}
%requires_peq   %{use_python}-Twisted
BuildRequires:  %{use_python}-attrs >= %{attrs_version}
%requires_peq   %{use_python}-attrs
BuildRequires:  %{use_python}-bcrypt >= %{bcrypt_version}
%requires_peq   %{use_python}-bcrypt
BuildRequires:  %{use_python}-bleach >= %{bleach_version}
%requires_peq   %{use_python}-bleach
BuildRequires:  (%{use_python}-canonicaljson >= %{canonicaljson_version} with %{use_python}-canonicaljson <  %{canonicaljson_max_version})
%requires_peq   %{use_python}-canonicaljson
BuildRequires:  %{use_python}-cryptography >= %{cryptography_version}
%requires_peq   %{use_python}-cryptography
BuildRequires:  %{use_python}-frozendict >= %{frozendict_version}
%requires_peq   %{use_python}-frozendict
BuildRequires:  %{use_python}-idna >= %{idna_version}
%requires_peq   %{use_python}-idna
BuildRequires:  %{use_python}-ijson >= %{ijson_version}
%requires_peq   %{use_python}-ijson
BuildRequires:  %{use_python}-jsonschema >= %{jsonschema_version}
%requires_peq   %{use_python}-jsonschema
BuildRequires:  (%{use_python}-matrix_common >= %{matrix_common_version} with %{use_python}-matrix_common <  %{matrix_common_max_version})
%requires_peq   %{use_python}-matrix_common
BuildRequires:  %{use_python}-msgpack >= %{msgpack_version}
%requires_peq   %{use_python}-msgpack
BuildRequires:  %{use_python}-netaddr >= %{netaddr_version}
%requires_peq   %{use_python}-netaddr
BuildRequires:  %{use_python}-phonenumbers >= %{phonenumbers_version}
%requires_peq   %{use_python}-phonenumbers
BuildRequires:  %{use_python}-prometheus_client >= %{prometheus_client_version}
%requires_peq   %{use_python}-prometheus_client
BuildRequires:  %{use_python}-psutil >= %{psutil_version}
%requires_peq   %{use_python}-psutil
BuildRequires:  %{use_python}-pyOpenSSL >= %{pyOpenSSL_version}
%requires_peq   %{use_python}-pyOpenSSL
BuildRequires:  %{use_python}-pyasn1 >= %{pyasn1_version}
%requires_peq   %{use_python}-pyasn1
BuildRequires:  %{use_python}-pyasn1-modules >= %{pyasn1_modules_version}
%requires_peq   %{use_python}-pyasn1-modules
BuildRequires:  %{use_python}-pymacaroons >= %{pymacaroons_version}
%requires_peq   %{use_python}-pymacaroons
BuildRequires:  %{use_python}-service_identity >= %{service_identity_version}
%requires_peq   %{use_python}-service_identity
BuildRequires:  (%{use_python}-signedjson >= %{signedjson_version} with %{use_python}-signedjson < %{signedjson_max_version})
%requires_peq   %{use_python}-signedjson
BuildRequires:  %{use_python}-sortedcontainers >= %{sortedcontainers_version}
%requires_peq   %{use_python}-sortedcontainers
BuildRequires:  %{use_python}-systemd  >= %{systemd_version}
%requires_peq   %{use_python}-systemd
BuildRequires:  %{use_python}-typing_extensions >= %{typing_extensions_version}
%requires_peq   %{use_python}-typing_extensions
BuildRequires:  %{use_python}-treq >= %{treq_version}
%requires_peq   %{use_python}-treq
BuildRequires:  %{use_python}-unpaddedbase64 >= %{unpaddedbase64_version}
%requires_peq   %{use_python}-unpaddedbase64
# Specify all CONDITIONAL_REQUIREMENTS (we Require them to avoid no-recommends
# breaking very commonly-used bits of matrix-synapse such as postgresql).
%if %{with synapse_ldap}
BuildRequires:  %{use_python}-matrix-synapse-ldap3 >= %{matrix_synapse_ldap3_version}
%requires_peq   %{use_python}-matrix-synapse-ldap3
%endif
BuildRequires:  %{use_python}-packaging >= %{packaging_version}
%requires_peq   %{use_python}-packaging
BuildRequires:  %{use_python}-pydantic >= %{pydantic_version}
%requires_peq   %{use_python}-pydantic
BuildRequires:  %{use_python}-psycopg2 >= %{psycopg2_version}
%requires_peq   %{use_python}-psycopg2
BuildRequires:  %{use_python}-pysaml2 >= %{pysaml2_version}
%requires_peq   %{use_python}-pysaml2
%if %{with synapse_oidc}
BuildRequires:  %{use_python}-Authlib >= %{Authlib_version}
%requires_peq   %{use_python}-Authlib
%endif
BuildRequires:  %{use_python}-lxml >= %{lxml_version}
%requires_peq   %{use_python}-lxml
%if %{with synapse_sentry}
BuildRequires:  %{use_python}-sentry-sdk >= %{sentry_sdk_version}
%requires_peq   %{use_python}-sentry-sdk
%endif
%if %{with synapse_opentracing}
BuildRequires:  %{use_python}-jaeger-client >= %{jaeger_client_version}
%requires_peq   %{use_python}-jaeger-client
BuildRequires:  %{use_python}-opentracing   >= %{opentracing_version}
%requires_peq   %{use_python}-opentracing
%endif
%if %{with synapse_redis}
BuildRequires:  %{use_python}-hiredis >= %{hiredis_version}
%requires_peq   %{use_python}-hiredis
BuildRequires:  %{use_python}-txredisapi >= %{txredisapi_version}
%requires_peq   %{use_python}-txredisapi
%endif
BuildRequires:  %{use_python}-Pympler >= %{Pympler_version}
%requires_peq   %{use_python}-Pympler
# We only provide/obsolete python2 to ensure that users upgrade.
Obsoletes:      python2-matrix-synapse < %{version}-%{release}
Provides:       python2-matrix-synapse = %{version}-%{release}
Obsoletes:      %{use_python}-matrix-synapse < %{version}-%{release}
Provides:       %{use_python}-matrix-synapse = %{version}-%{release}

%description
Synapse is a Python-based reference "homeserver" implementation of
Matrix. Matrix is a system for federated Instant Messaging and VoIP.

%prep
%autosetup -p1 -a1
install -m 0644 -D %{SOURCE2} .cargo/config

# Remove all un-needed #!-lines.
find synapse/ -type f -not -path './vendor/**' -exec sed -i '1{/^#!/d}' {} \;
# Replace all #!/usr/bin/env lines to use #!/usr/bin/$1 directly.
find ./ -type f -not -path './vendor/**' -exec \
	sed -i '1s|^#!/usr/bin/env |#!/usr/bin/|' {} \;
# Force the usage of the default python3 sys executable
find ./ -type f -not -path './vendor/**' \
	-exec sed -i '1s|^#!/usr/bin/python.*$|#!%{__python3}|' {} \;

# Update the python flavour in the service file.
sed -i 's|@PYTHON_FLAVOR@|%{__python3}|g' %{S:50}

%build
%pyproject_wheel
%sysusers_generate_pre %{SOURCE47} %{name}

%install
cp %{S:48} README.SUSE
# We install scripts into /usr/lib to avoid silly conflicts with other pkgs.
install -d -m 0755 %{buildroot}%{_libexecdir}/%{pkgname}
%pyproject_install

install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_libexecdir}/%{pkgname}/
# move scripts to the old place.
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{pkgname}/
# While we provide a systemd service, link synctl so it's simpler to use.
ln -s %{_libexecdir}/%{pkgname}/synctl %{buildroot}%{_bindir}/synctl

# Install default matrix-synapse configuration.
# TODO: Switch to the debian default config.
install -d -m 0750 \
  %{buildroot}%{_sysconfdir}/%{pkgname}/ \
  %{buildroot}%{_sysconfdir}/%{pkgname}/{conf,keys}.d/
install -D -m 0640 contrib/systemd/log_config.yaml %{buildroot}%{_sysconfdir}/%{pkgname}/log.yaml
install -D -m 0640 contrib/systemd/log_config.yaml %{buildroot}%{_sysconfdir}/%{pkgname}/log.systemd.yaml
install -D -m 0640 contrib/example_log_config.yaml %{buildroot}%{_sysconfdir}/%{pkgname}/log.file.yaml

# Man pages.
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 debian/*.1

# system configuration.
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{pkgname}
#
install -D -m 0644 %{S:50} %{buildroot}%{_unitdir}/%{pkgname}.service
install -D -m 0644 %{S:49} %{buildroot}%{_tmpfilesdir}/%{pkgname}.conf
install -D -m 0644 %{SOURCE47} %{buildroot}%{_sysusersdir}/%{name}.conf
#
install -D -m 0755 %{S:51} %{buildroot}%{_sbindir}/matrix-synapse-generate-config

# User directory.
install -d -m 0750 %{buildroot}%{_rundir}/%{pkgname}
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/%{pkgname}
install -d -m 0750 %{buildroot}%{_localstatedir}/log/%{pkgname}

%fdupes %{buildroot}%{python3_sitearch}

%pre -f %{name}.pre
%service_add_pre %{pkgname}.service

%post
%tmpfiles_create %{_tmpfilesdir}/%{pkgname}.conf
%service_add_post %{pkgname}.service

%preun
%service_del_preun %{pkgname}.service

%postun
%service_del_postun %{pkgname}.service

%files -n %{pkgname}
%doc *.rst CHANGES.md README.SUSE
%license LICENSE
%config(noreplace) %attr(-,root,synapse) %{_sysconfdir}/%{pkgname}/
%dir %attr(0750,%{modname},%{modname}) %{_localstatedir}/lib/%{pkgname}
%dir %attr(0750,%{modname},%{modname}) %{_localstatedir}/log/%{pkgname}
%{python3_sitearch}/%{modname}
%{python3_sitearch}/%{eggname}-*-info
# Python helper scripts.
%{_bindir}/synctl
%{_libexecdir}/%{pkgname}
# systemd service.
%{_sbindir}/rc%{pkgname}
%{_sbindir}/matrix-synapse-generate-config
%{_unitdir}/%{pkgname}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{pkgname}.conf
# Man pages.
%{_mandir}/man*/*
%ghost %dir %attr(750,%{modname},%{modname}) /run/matrix-synapse

%changelog
