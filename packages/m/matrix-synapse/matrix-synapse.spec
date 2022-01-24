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

%if 0%{?suse_version} >= 1550
%define use_python python38
#define __python3 #{_bindir}/python3
%else
%define use_python python3
%endif

%define         modname synapse
%define         pkgname matrix-synapse
%define         eggname matrix_synapse
Name:           %{pkgname}
Version:        1.50.2
Release:        0
Summary:        Matrix protocol reference homeserver
License:        Apache-2.0
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/matrix-org/synapse
Source0:        %{pkgname}-%{version}.tar.xz
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
Patch1:         dont-bump-cryptography-with-system-openssl.patch
# https://github.com/matrix-org/synapse/pull/10719
# disable by marking as source until we get a decision upstream
Source100:      10719-Fix-instert-of-duplicate-key-into-event_json.patch
BuildRequires:  %{use_python}-base >= 3.8
BuildRequires:  %{use_python}-setuptools
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  unzip
%{?systemd_ordering}
%{sysusers_requires}
%requires_eq    %{use_python}-base
# NOTE: Keep this is in the same order as synapse/python_dependencies.py.
BuildRequires:  %{use_python}-Jinja2 >= 2.9
%requires_eq    %{use_python}-Jinja2
BuildRequires:  %{use_python}-Pillow >= 4.3.0
%requires_eq    %{use_python}-Pillow
BuildRequires:  %{use_python}-PyNaCl >= 1.2.1
%requires_eq    %{use_python}-PyNaCl
BuildRequires:  %{use_python}-PyYAML >= 3.11
%requires_eq    %{use_python}-PyYAML
BuildRequires:  %{use_python}-Twisted >= 20.3.0
%requires_eq    %{use_python}-Twisted
BuildRequires:  ((%{use_python}-attrs >= 19.2.0 with %{use_python}-attrs < 21.1.0) or %{use_python}-attrs > 21.1.0)
%requires_eq    %{use_python}-attrs
BuildRequires:  %{use_python}-bcrypt >= 3.2.0
%requires_eq    %{use_python}-bcrypt
BuildRequires:  %{use_python}-bleach >= 1.4.3
%requires_eq    %{use_python}-bleach
BuildRequires:  %{use_python}-canonicaljson >= 1.4.0
%requires_eq    %{use_python}-canonicaljson
BuildRequires:  %{use_python}-cryptography >= 3.4.7
%requires_eq    %{use_python}-cryptography
BuildRequires:  %{use_python}-frozendict >= 2.1.3
%requires_eq    %{use_python}-frozendict
BuildRequires:  %{use_python}-idna >= 2.5
%requires_eq    %{use_python}-idna
BuildRequires:  %{use_python}-ijson >= 3.1
%requires_eq    %{use_python}-ijson
BuildRequires:  %{use_python}-jsonschema >= 3.0.0
%requires_eq    %{use_python}-jsonschema
BuildRequires:  %{use_python}-matrix_common >= 1.0.0
%requires_eq    %{use_python}-matrix_common
BuildRequires:  %{use_python}-msgpack >= 0.5.2
%requires_eq    %{use_python}-msgpack
BuildRequires:  %{use_python}-netaddr >= 0.7.18
%requires_eq    %{use_python}-netaddr
BuildRequires:  %{use_python}-phonenumbers >= 8.2.0
%requires_eq    %{use_python}-phonenumbers
BuildRequires:  %{use_python}-prometheus_client >= 0.4.0
%requires_eq    %{use_python}-prometheus_client
BuildRequires:  %{use_python}-psutil >= 2.0.0
%requires_eq    %{use_python}-psutil
BuildRequires:  %{use_python}-pyOpenSSL >= 16.0.0
%requires_eq    %{use_python}-pyOpenSSL
BuildRequires:  %{use_python}-pyasn1 >= 0.1.9
%requires_eq    %{use_python}-pyasn1
BuildRequires:  %{use_python}-pyasn1-modules >= 0.0.7
%requires_eq    %{use_python}-pyasn1-modules
BuildRequires:  %{use_python}-pymacaroons >= 0.13.0
%requires_eq    %{use_python}-pymacaroons
BuildRequires:  %{use_python}-service_identity >= 18.1.0
%requires_eq    %{use_python}-service_identity
BuildRequires:  %{use_python}-signedjson >= 1.1.0
%requires_eq    %{use_python}-signedjson
BuildRequires:  %{use_python}-six >= 1.10
%requires_eq    %{use_python}-six
BuildRequires:  %{use_python}-sortedcontainers >= 1.4.4
%requires_eq    %{use_python}-sortedcontainers
BuildRequires:  %{use_python}-systemd  >= 231
%requires_eq    %{use_python}-systemd
BuildRequires:  %{use_python}-typing_extensions >= 3.7.4
%requires_eq    %{use_python}-typing_extensions
BuildRequires:  %{use_python}-treq >= 15.1
%requires_eq    %{use_python}-treq
BuildRequires:  %{use_python}-unpaddedbase64 >= 1.1.0
%requires_eq    %{use_python}-unpaddedbase64
# Specify all CONDITIONAL_REQUIREMENTS (we Require them to avoid no-recommends
# breaking very commonly-used bits of matrix-synapse such as postgresql).
%if %{with synapse_ldap}
BuildRequires:  %{use_python}-matrix-synapse-ldap3 >= 0.1
%requires_eq    %{use_python}-matrix-synapse-ldap3
%endif
BuildRequires:  %{use_python}-psycopg2 >= 2.8
%requires_eq    %{use_python}-psycopg2
BuildRequires:  %{use_python}-pysaml2 >= 4.5.0
%requires_eq    %{use_python}-pysaml2
%if %{with synapse_oidc}
BuildRequires:  %{use_python}-Authlib >= 0.15.1
%requires_eq    %{use_python}-Authlib
%endif
BuildRequires:  %{use_python}-lxml >= 3.5.0
%requires_eq    %{use_python}-lxml
%if %{with synapse_sentry}
BuildRequires:  %{use_python}-sentry-sdk >= 0.7.2
%requires_eq    %{use_python}-sentry-sdk
%endif
BuildRequires:  %{use_python}-PyJWT >= 1.6.4
%requires_eq    %{use_python}-PyJWT
%if %{with synapse_opentracing}
BuildRequires:  %{use_python}-jaeger-client >= 4.0.0
%requires_eq    %{use_python}-jaeger-client
BuildRequires:  %{use_python}-opentracing   >= 2.2.0
%requires_eq    %{use_python}-opentracing
%endif
%if %{with synapse_redis}
BuildRequires:  %{use_python}-hiredis >= 1.0.1
%requires_eq    %{use_python}-hiredis
BuildRequires:  %{use_python}-txredisapi >= 1.4.7
%requires_eq    %{use_python}-txredisapi
%endif
BuildRequires:  %{use_python}-Pympler >= 0.8
%requires_eq    %{use_python}-Pympler
BuildArch:      noarch
# We only provide/obsolete python2 to ensure that users upgrade.
Obsoletes:      python2-matrix-synapse < %{version}-%{release}
Provides:       python2-matrix-synapse = %{version}-%{release}
Obsoletes:      %{use_python}-matrix-synapse < %{version}-%{release}
Provides:       %{use_python}-matrix-synapse = %{version}-%{release}

%description
Synapse is a Python-based reference "homeserver" implementation of
Matrix. Matrix is a system for federated Instant Messaging and VoIP.

%prep
%autosetup -p1

# Remove all un-needed #!-lines.
find synapse/ -type f -exec sed -i '1{/^#!/d}' {} \;
# Replace all #!/usr/bin/env lines to use #!/usr/bin/$1 directly.
find ./ -type f -exec \
	sed -i '1s|^#!/usr/bin/env |#!/usr/bin/|' {} \;
# Force the usage of the default python3 sys executable
find ./ -type f \
	-exec sed -i '1s|^#!/usr/bin/python.*$|#!%{__python3}|' {} \;

# Update the python flavour in the service file.
sed -i 's|@PYTHON_FLAVOR@|%{__python3}|g' %{S:50}

%build
%python3_build
%sysusers_generate_pre %{SOURCE47} %{name}

%install
cp %{S:48} README.SUSE
# We install scripts into /usr/lib to avoid silly conflicts with other pkgs.
install -d -m 0755 %{buildroot}%{_libexecdir}/%{pkgname}
%python3_install "--install-scripts=%{_libexecdir}/%{pkgname}/"

# While we provide a systemd service, link synctl so it's simpler to use.
install -d -m 0755 %{buildroot}%{_bindir}
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

%fdupes %{buildroot}%{python3_sitelib}

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
%{python3_sitelib}/%{modname}
%{python3_sitelib}/synmark
%{python3_sitelib}/%{eggname}-*-info
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
