#
# spec file for package matrix-synapse
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without email_notifs
%bcond_without postgres
%bcond_with    oidc
%bcond_without saml
%bcond_without url_preview
%bcond_without jwt
%bcond_with    redis
# missing deps
%bcond_with    opentracing
# matrix-synapse-ldap isn't packaged on openSUSE.
%bcond_with    ldap
# txacme is broken in openSUSE.
%bcond_with    acme
# sentry-sdk isn't packaged on openSUSE.
%bcond_with    sentry

## Package updates
#
# * Update version in _service to the most recent released one
# * Call `osc service dr`
# * Update changelog manually from
#   https://github.com/matrix-org/synapse/releases or synapse/CHANGES.md
# * Commit+submit

# Synapse 1.1.0 and onwards only supports Python >= 3.5.
%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         modname synapse
%define         pkgname matrix-synapse
Name:           %{pkgname}
Version:        1.21.2
Release:        0
Summary:        Matrix protocol reference homeserver
License:        Apache-2.0
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/matrix-org/synapse
Source0:        %{pkgname}-%{version}.tar.xz
Source48:       README.SUSE
Source49:       matrix-synapse.tmpfiles.d
Source50:       %{pkgname}.service
Source51:       matrix-synapse-generate-config.sh
# track series file so we can easily use quilt
# cd synapse ; ln -s .. patches ; quilt push -a
# to clean up your working copy afterwards: git reset --hard ; rm -rv .pc patches
Source99:       series
Patch:          matrix-synapse-1.4.1-paths.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module psutil >= 2.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module treq >= 15.1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  unzip
%{?systemd_requires}
Requires(pre):  shadow
%ifpython3
Requires:       %{python_flavor} >= 3.5
%endif
# NOTE: Keep this is in the same order as synapse/python_dependencie.py.
BuildRequires:  python3-Pillow >= 4.3.0
%requires_eq    python3-Pillow
BuildRequires:  python3-PyNaCl >= 1.2.1
%requires_eq    python3-PyNaCl
BuildRequires:  python3-PyYAML >= 3.11
%requires_eq    python3-PyYAML
BuildRequires:  python3-Twisted >= 20.3.0
%requires_eq    python3-Twisted
BuildRequires:  python3-attrs >= 17.4.0
%requires_eq    python3-attrs
BuildRequires:  python3-bcrypt >= 3.1.0
%requires_eq    python3-bcrypt
BuildRequires:  python3-bleach >= 1.4.3
%requires_eq    python3-bleach
BuildRequires:  python3-canonicaljson >= 1.3.0
%requires_eq    python3-canonicaljson
BuildRequires:  python3-frozendict >= 1
%requires_eq    python3-frozendict
BuildRequires:  python3-idna >= 2.5
%requires_eq    python3-idna
BuildRequires:  python3-jsonschema >= 2.5.1
%requires_eq    python3-jsonschema
BuildRequires:  python3-msgpack >= 0.5.2
%requires_eq    python3-msgpack
BuildRequires:  python3-netaddr >= 0.7.18
%requires_eq    python3-netaddr
BuildRequires:  python3-phonenumbers >= 8.2.0
%requires_eq    python3-phonenumbers
BuildRequires:  (python3-prometheus_client >= 0.4.0 with python3-prometheus_client < 0.9.0)
%requires_eq    python3-prometheus_client
BuildRequires:  python3-psutil >= 2.0.0
%requires_eq    python3-psutil
BuildRequires:  python3-pyOpenSSL >= 16.0.0
%requires_eq    python3-pyOpenSSL
BuildRequires:  python3-pyasn1 >= 0.1.9
%requires_eq    python3-pyasn1
BuildRequires:  python3-pyasn1-modules >= 0.0.7
%requires_eq    python3-pyasn1-modules
BuildRequires:  python3-pymacaroons >= 0.13.0
%requires_eq    python3-pymacaroons
BuildRequires:  python3-service_identity >= 18.1.0
%requires_eq    python3-service_identity
BuildRequires:  python3-signedjson >= 1.1.0
%requires_eq    python3-signedjson
BuildRequires:  python3-six >= 1.10
%requires_eq    python3-six
BuildRequires:  python3-sortedcontainers >= 1.4.4
%requires_eq    python3-sortedcontainers
BuildRequires:  python3-systemd  >= 231
%requires_eq    python3-systemd
BuildRequires:  python3-typing_extensions >= 3.7.4
%requires_eq    python3-typing_extensions
BuildRequires:  python3-treq >= 15.1
%requires_eq    python3-treq
BuildRequires:  python3-unpaddedbase64 >= 1.1.0
%requires_eq    python3-unpaddedbase64
# Specify all CONDITIONAL_REQUIREMENTS (we Require them to avoid no-recommends
# breaking very commonly-used bits of matrix-synapse such as postgresql).
%if %{with email_notifs}
BuildRequires:  python3-Jinja2 >= 2.9
%requires_eq    python3-Jinja2
%endif
%if %{with ldap}
BuildRequires:  python3-matrix-synapse-ldap3 >= 0.1
%requires_eq    python3-matrix-synapse-ldap3
%endif
%if %{with postgres}
BuildRequires:  python3-psycopg2 >= 2.7
%requires_eq    python3-psycopg2
%endif
%if %{with acme}
BuildRequires:  python3-txacme >= 0.9.2
%requires_eq    python3-txacme
%endif
%if %{with saml}
BuildRequires:  python3-pysaml2 >= 4.5.0
%requires_eq    python3-pysaml2
%endif
%if %{with oidc}
BuildRequires:  python3-authlib >= 0.15.1
%requires_eq    python3-authlib
%endif
%if %{with url_preview}
BuildRequires:  python3-lxml >= 3.5.0
%requires_eq    python3-lxml
%endif
%if %{with sentry}
BuildRequires:  python3-sentry-sdk >= 0.7.2
%requires_eq    python3-sentry-sdk
%endif
%if %{with jwt}
BuildRequires:  python3-PyJWT >= 1.6.4
%requires_eq    python3-PyJWT
%endif
%if %{with opentracing}
BuildRequires:  python3-jaeger-client >= 4.0.0
%requires_eq    python3-jaeger-client
BuildRequires:  python3-opentracing   >= 2.2.0
%requires_eq    python3-opentracing
%endif
%if %{with redis}
BuildRequires:  python3-txredisapi >= 1.4.7
%requires_eq    python3-txredisapi
BuildRequires:  python3-hiredis
%requires_eq    python3-hiredis
%endif
BuildArch:      noarch
# We only provide/obsolete python2 to ensure that users upgrade.
Obsoletes:      python2-matrix-synapse < %{version}-%{release}
Provides:       python2-matrix-synapse = %{version}-%{release}
Obsoletes:      python3-matrix-synapse < %{version}-%{release}
Provides:       python3-matrix-synapse = %{version}-%{release}

%python_subpackages

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
# Force the usage of python_flavor.
find ./ -type f \
	-exec sed -i '1s|^#!/usr/bin/python$|#!/usr/bin/%{python_flavor}|' {} \;

# Update the python flavour in the service file.
sed -i 's|@PYTHON_FLAVOR@|%{_bindir}/%{python_flavor}|g' %{S:50}

%build
%python_build

%install
cp %{S:48} README.SUSE
# We install scripts into /usr/lib to avoid silly conflicts with other pkgs.
install -d -m 0755 %{buildroot}%{_libexecdir}/%{pkgname}
%python_install "--install-scripts=%{_libexecdir}/%{pkgname}/"

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
#
install -D -m 0755 %{S:51} %{buildroot}%{_sbindir}/matrix-synapse-generate-config

# User directory.
install -d -m 0750 %{buildroot}%{_rundir}/%{pkgname}
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/%{pkgname}
install -d -m 0750 %{buildroot}%{_localstatedir}/log/%{pkgname}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
getent group synapse >/dev/null || groupadd -r synapse
getent passwd synapse >/dev/null || \
    /usr/sbin/useradd -r -g synapse -s /bin/false -c 'Matrix Synapse' \
        -d %{_rundir}/%{pkgname} synapse
usermod --shell=/bin/false --home=%{_localstatedir}/lib/%{pkgname} --gid=synapse synapse
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
%{python_sitelib}
# Python helper scripts.
%{_bindir}/synctl
%{_libexecdir}/%{pkgname}
# systemd service.
%{_sbindir}/rc%{pkgname}
%{_sbindir}/matrix-synapse-generate-config
%{_unitdir}/%{pkgname}.service
%{_tmpfilesdir}/%{pkgname}.conf
# Man pages.
%{_mandir}/man*/*
%ghost %dir %attr(750,%{modname},%{modname}) /run/matrix-synapse

%changelog
