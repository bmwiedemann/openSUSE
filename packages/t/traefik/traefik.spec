#
# spec file for package traefik
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


%define project github.com/traefik/traefik
%ifarch ppc64 s390x
%define buildmode default
%else
%define buildmode pie
%endif
Name:           traefik
Version:        3.2.1
Release:        0
Summary:        The Cloud Native Application Proxy
License:        MIT
Group:          Productivity/Networking/Web/Proxy
URL:            https://traefik.io/
# set the desired version in the spec-file
# download the source files and create the vendor tarball with "osc service mr"
Source0:        https://github.com/traefik/traefik/releases/download/v%{version}/%{name}-v%{version}.src.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.service
Source3:        %{name}.yml
Source4:        %{name}-user.conf
Source5:        90-%{name}.conf
BuildRequires:  go-bindata
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  (golang(API) >= 1.22)
Recommends:     podman
Conflicts:      traefik2
Provides:       group(%{name})
Provides:       user(%{name})
%sysusers_requires
%{?systemd_requires}
%{go_provides}

%description
Traefik (pronounced traffic) is a modern HTTP reverse proxy and load balancer
that makes deploying microservices easy. Traefik integrates with your existing
infrastructure components (Docker, Swarm mode, Kubernetes, Marathon, Consul,
Etcd, Rancher, Amazon ECS) and configures itself automatically and dynamically.

Pointing Traefik at your orchestrator should be the only configuration step you need.

%prep
%setup -q -c %{name}-%{version} -b0 -a1
%autopatch -p1

%build
%sysusers_generate_pre %{SOURCE4} %{name} %{name}-user.conf
%{goprep} %{project}
# see script/generate
go generate

build_date=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +"%%Y%%m%%d")
# see script/binary
CGO_ENABLED=1 GOGC=off go build \
  -buildmode=%{buildmode} \
  -mod=vendor \
  -ldflags "-X github.com/traefik/traefik/v3/pkg/version.Version=%{version} \
            -X github.com/traefik/traefik/v3/pkg/version.Codename='' \
            -X github.com/traefik/traefik/v3/pkg/version.BuildDate=${build_date}" \
  -installsuffix nocgo \
  -o traefik \
  ./cmd/traefik

%install
# system user
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}-user.conf

install -d %{buildroot}/%{_sbindir}
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# configuration
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}/%{name}.yml
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d

# install configuration to increase UDP buffer sizes
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_prefix}/lib/sysctl.d/90-%{name}.conf

# acme storage
install -d -m 0700 %{buildroot}%{_localstatedir}/lib/%{name}
touch  %{buildroot}%{_localstatedir}/lib/%{name}/acme.json

# logging
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only -n %{name}}
# fix ownership for config and logging directory
chown -R traefik: %{_sysconfdir}/%{name} %{_localstatedir}/log/%{name}

# try to move acme.json file from old directory to new
if [ -e "%{_sysconfdir}/%{name}/acme.json" ] ; then
	if [ -s "%{_sysconfdir}/%{name}/acme.json" ] ; then
		if [ -s "%{_localstatedir}/lib/%{name}/acme.json" ] ; then
			# if not-empty acme.json files exists on old and new location, write warning
			echo "A non-empty acme.json file exists in:" 1>&2
			echo "%{_sysconfdir}/%{name} and %{_localstatedir}/lib/%{name}" 1>&2
			echo "Please clean up this situation and place the correct file in %{_localstatedir}/lib/%{name}" 1>&2
		else
			# if not-empty acme.json exists on old location and no file or empty file exists on new location
			# move it to the new location
			mv "%{_sysconfdir}/%{name}/acme.json" "%{_localstatedir}/lib/%{name}/acme.json"
			sed -i -e 's|%{_sysconfdir}/traefik/acme.json|%{_localstatedir}/lib/traefik/acme.json|' %{_sysconfdir}/%{name}/%{name}.yml
		fi
	else
		# remove empty acme.json file from old location
		rm "%{_sysconfdir}/%{name}/acme.json"
		sed -i -e 's|%{_sysconfdir}/traefik/acme.json|%{_localstatedir}/lib/traefik/acme.json|' %{_sysconfdir}/%{name}/%{name}.yml
	fi
fi

# fix ownership for acme file
chown -R traefik: %{_localstatedir}/lib/%{name}/*

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{_sysusersdir}/%{name}-user.conf

%license LICENSE.md
%doc README.md SECURITY.md CONTRIBUTING.md
%{_bindir}/%{name}

%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_prefix}/lib/sysctl.d/90-%{name}.conf

%defattr(0600, traefik, traefik, 0700)
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d

%dir %{_localstatedir}/lib/%{name}
%config(noreplace) %{_localstatedir}/lib/%{name}/acme.json

%config(noreplace) %{_sysconfdir}/%{name}/%{name}.yml
%dir %{_localstatedir}/log/%{name}

%changelog
