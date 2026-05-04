#
# spec file for package libcontainers-common
#
# Copyright (c) 2026 SUSE LLC
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


# clibsver - version from containers/container-libs (common/ tag)
%define clibsver 0.67.1
# https://github.com/containers/shortnames
%define shortnamesver 8ce3e7d11ca3425a9899fc7291f4256ba5da225c
Name:           libcontainers-common
Version:        20260429
Release:        0
Summary:        Configuration files common to github.com/containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containers/container-libs
Source0:        container-libs-%{clibsver}.tar.xz
Source1:        LICENSE
# Heavily stripped from upstream containers/common/pkg/subscriptions/mounts.conf
Source2:        mounts.conf
# SUSE-specific sigstore-attachments configs for SUSE registries
Source3:        registry.suse.com.yaml
Source4:        registry.suse.de.yaml
Source5:        %{name}.rpmlintrc
Source6:        https://raw.githubusercontent.com/containers/shortnames/%{shortnamesver}/shortnames.conf
Source7:        openSUSE-policy.json
# SUSE distro overrides shipped as containers.conf.d/ drop-ins
Source10:       00-suse-containers.conf
# CNI plugin dirs override for older SLE/ALP streams (bsc#1213556)
Source11:       01-suse-cni.conf
# Search registries variants - picked at install time via subpackages
Source12:       00-suse-registries-default.conf
Source13:       00-suse-registries-microos.conf
BuildRequires:  go-go-md2man
Requires:       libcontainers-policy >= %{version}
Suggests:       (libcontainers-policy-openSUSE if openSUSE-release)
# Default to SUSE registry on SL Micro,
# keep SUSE, openSUSE and dockerhub registries otherwise.
# (jsc#SMO-376, jsc#PED-8289)
Requires:       registries-conf >= %{version}
Suggests:       (registries-conf-suse if (product(SL-Micro) or (product(SUSE_SLE) >= 15.5)))
Suggests:       (registries-conf-default if openSUSE-release)
Provides:       libcontainers-image = %{version}
Provides:       libcontainers-storage = %{version}
Obsoletes:      libcontainers-image < %{version}
Obsoletes:      libcontainers-storage < %{version}
BuildArch:      noarch

%description
Configuration files and manpages shared by tools that are based on the
github.com/containers libraries, such as Buildah, CRI-O, Podman and Skopeo.

%package -n libcontainers-openSUSE-policy
Summary:        Policy to enforce image verification for SLE BCI
Provides:       libcontainers-policy = %{version}-%{release}

RemovePathPostfixes: .openSUSE
Conflicts:      libcontainers-default-policy

%description -n libcontainers-openSUSE-policy
This package ships a /etc/containers/policy.json which enforces image verification for SLE BCI.

%package -n libcontainers-default-policy
Summary:        Default containers policy.json
Provides:       libcontainers-policy = %{version}-%{release}

RemovePathPostfixes: .default
Conflicts:      libcontainers-openSUSE-policy

%description -n libcontainers-default-policy
This package ships the default /etc/containers/policy.json

%package -n registries-conf-suse
Summary:                Defaults to SUSE Registry on SL Micro
Provides:               registries-conf = %{version}-%{release}
RemovePathPostfixes:    .suse
Conflicts:              registries-conf-default

%description -n registries-conf-suse
Ships a modified registries.conf with registry.suse.com as the only unqualified search registry.

%package -n registries-conf-default
Summary:                Add SUSE and openSUSE registries to be used to pull images along with dockerhub
Provides:               registries-conf = %{version}-%{release}
RemovePathPostfixes:    .default
Conflicts:              registries-conf-suse

%description -n registries-conf-default
Ships the upstream registries.conf with registry.opensuse.org and registry.suse.com as additional unqualified search registries.

%prep
%setup -q -n container-libs-%{clibsver}
cp %{SOURCE1} .

# Substitute @LIBEXECDIR@ in CNI drop-in for older SLE/ALP streams (bsc#1213556)
%if 0%{?suse_version} < 1600 && !0%{?is_opensuse}
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' %{SOURCE11} > 01-suse-cni.conf
%endif

%build
mkdir -p man5
for md in common/docs/*.5.md image/docs/*.5.md storage/docs/*.5.md; do
    go-md2man -in "$md" -out "man5/$(basename "$md" .md)"
done

# oci-hooks lives outside common/docs/
go-md2man -in common/pkg/hooks/docs/oci-hooks.5.md -out man5/oci-hooks.5

%install
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/oci/hooks.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/registries.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/registries.conf.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/containers.conf.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/systemd
install -d -m 0755 %{buildroot}/%{_datadir}/containers/oci/hooks.d
install -d -m 0755 %{buildroot}/%{_datadir}/containers/systemd

# Vanilla upstream base configs from the monorepo tarball.
# Only files podman/c/common reads from /usr/share/ go here.
install -D -m 0644 storage/storage.conf              %{buildroot}/%{_datadir}/containers/storage.conf
install -D -m 0644 common/pkg/config/containers.conf %{buildroot}/%{_datadir}/containers/containers.conf
install -D -m 0644 common/pkg/seccomp/seccomp.json   %{buildroot}/%{_datadir}/containers/seccomp.json
install -D -m 0644 %{SOURCE2}                        %{buildroot}/%{_datadir}/containers/mounts.conf

# Files podman only reads from /etc/ (drop-ins, registries.conf, registries.d, policy.json).
# These are vendor-shipped but must live in /etc/ until upstream code adds /usr/share/.d/ support.
install -D -m 0644 image/registries.conf %{buildroot}/%{_sysconfdir}/containers/registries.conf
install -D -m 0644 image/default.yaml    %{buildroot}/%{_sysconfdir}/containers/registries.d/default.yaml
install -D -m 0644 %{SOURCE3}            %{buildroot}/%{_sysconfdir}/containers/registries.d/registry.suse.com.yaml
install -D -m 0644 %{SOURCE4}            %{buildroot}/%{_sysconfdir}/containers/registries.d/registry.suse.de.yaml
install -D -m 0644 %{SOURCE6}            %{buildroot}/%{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf

# SUSE distro overrides as containers.conf.d/ drop-in
install -D -m 0644 %{SOURCE10} %{buildroot}/%{_sysconfdir}/containers/containers.conf.d/00-suse-containers.conf

# CNI plugin dirs override for older SLE/ALP streams (bsc#1213556)
%if 0%{?suse_version} < 1600 && !0%{?is_opensuse}
install -D -m 0644 01-suse-cni.conf %{buildroot}/%{_sysconfdir}/containers/containers.conf.d/01-suse-cni.conf
%endif

# Search registries variants - subpackages pick which one is active
install -D -m 0644 %{SOURCE12} %{buildroot}/%{_sysconfdir}/containers/registries.conf.d/00-suse-registries.conf.default
install -D -m 0644 %{SOURCE13} %{buildroot}/%{_sysconfdir}/containers/registries.conf.d/00-suse-registries.conf.suse

# policy.json variants - subpackages pick which one is active
install -D -m 0644 image/default-policy.json %{buildroot}/%{_sysconfdir}/containers/policy.json.default
install -D -m 0644 %{SOURCE7}                %{buildroot}/%{_sysconfdir}/containers/policy.json.openSUSE

# Manpages
install -d %{buildroot}/%{_mandir}/man5
install -D -m 0644 man5/*.5 %{buildroot}/%{_mandir}/man5/

%pre
# Rotate any stale .rpmsave files from previous upgrades to avoid clobbering
for f in mounts.conf seccomp.json storage.conf containers.conf \
         policy.json registries.conf \
         registries.d/default.yaml \
         registries.conf.d/000-shortnames.conf; do
    test -f %{_sysconfdir}/containers/${f}.rpmsave && \
        mv -v %{_sysconfdir}/containers/${f}.rpmsave %{_sysconfdir}/containers/${f}.rpmsave.old ||:
done

%posttrans
# Restore user-modified configs from .rpmsave back to /etc/.
# These act as user overrides on top of the vendor defaults in /usr/share/.
for f in mounts.conf seccomp.json storage.conf containers.conf \
         policy.json registries.conf \
         registries.d/default.yaml \
         registries.conf.d/000-shortnames.conf; do
    test -f %{_sysconfdir}/containers/${f}.rpmsave && \
        mv -v %{_sysconfdir}/containers/${f}.rpmsave %{_sysconfdir}/containers/${f} ||:
done

%files
%dir %{_sysconfdir}/containers
%dir %{_sysconfdir}/containers/oci
%dir %{_sysconfdir}/containers/oci/hooks.d
%dir %{_sysconfdir}/containers/registries.d
%dir %{_sysconfdir}/containers/registries.conf.d
%dir %{_sysconfdir}/containers/containers.conf.d
%dir %{_sysconfdir}/containers/systemd
%dir %{_datadir}/containers
%dir %{_datadir}/containers/oci
%dir %{_datadir}/containers/oci/hooks.d
%dir %{_datadir}/containers/systemd

# Vendor base files in /usr/share/ (podman reads these from /usr/share/)
%{_datadir}/containers/storage.conf
%{_datadir}/containers/containers.conf
%{_datadir}/containers/mounts.conf
%{_datadir}/containers/seccomp.json

# Vendor files in /etc/ (podman only reads these from /etc/)
%config(noreplace) %{_sysconfdir}/containers/registries.conf
%config(noreplace) %{_sysconfdir}/containers/registries.d/default.yaml
%config(noreplace) %{_sysconfdir}/containers/registries.d/registry.suse.com.yaml
%config(noreplace) %{_sysconfdir}/containers/registries.d/registry.suse.de.yaml
%config(noreplace) %{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
%config(noreplace) %{_sysconfdir}/containers/containers.conf.d/00-suse-containers.conf
%if 0%{?suse_version} < 1600 && !0%{?is_opensuse}
%config(noreplace) %{_sysconfdir}/containers/containers.conf.d/01-suse-cni.conf
%endif

%{_mandir}/man5/*.5%{?ext_man}
%license LICENSE


%files -n libcontainers-openSUSE-policy
%config(noreplace) %{_sysconfdir}/containers/policy.json.openSUSE

%files -n libcontainers-default-policy
%config(noreplace) %{_sysconfdir}/containers/policy.json.default

%files -n registries-conf-suse
%config(noreplace) %{_sysconfdir}/containers/registries.conf.d/00-suse-registries.conf.suse

%files -n registries-conf-default
%config(noreplace) %{_sysconfdir}/containers/registries.conf.d/00-suse-registries.conf.default

%changelog
