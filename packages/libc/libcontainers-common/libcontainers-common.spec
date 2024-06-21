#
# spec file for package libcontainers-common
#
# Copyright (c) 2023 SUSE LLC
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


# commonver - version from containers/common
%define commonver 0.59.1
# storagever - version from containers/storage
%define storagever 1.54.0
# imagever - version from containers/image
%define imagever 5.31.0
# skopeover - version from containers/skopeo
%define skopeover 1.14.4
# https://github.com/containers/shortnames
%define shortnamesver 2023.02.20
Name:           libcontainers-common
Version:        20240618
Release:        0
Summary:        Configuration files common to github.com/containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containers
Source0:        image-%{imagever}.tar.xz
Source1:        storage-%{storagever}.tar.xz
Source2:        LICENSE
# https://raw.githubusercontent.com/containers/skopeo/main/default-policy.json
Source3:        https://raw.githubusercontent.com/containers/skopeo/v%{skopeover}/default-policy.json#./policy.json
# https://github.com/containers/storage/blob/main/storage.conf + custom changes
Source4:        storage.conf
# heavily modified version of https://github.com/containers/common/blob/main/pkg/subscriptions/mounts.conf
Source5:        mounts.conf
# https://raw.githubusercontent.com/containers/image/main/registries.conf with our own registries inserted
Source6:        registries.conf
# https://github.com/containers/skopeo/blob/main/default.yaml but heavily modified
Source7:        default.yaml
Source8:        common-%{commonver}.tar.xz
Source9:        https://raw.githubusercontent.com/containers/common/v%{commonver}/pkg/config/containers.conf
Source10:       %{name}.rpmlintrc
Source11:       https://raw.githubusercontent.com/containers/shortnames/v%{shortnamesver}/shortnames.conf
Source12:       openSUSE-policy.json
Patch100:       0001-containers.conf-SUSE-clear-cni-config-dir-for-ALP.patch
BuildRequires:  go-go-md2man
Requires(post): %{_bindir}/sed
# add SLE-specific mounts for only SLES systems
Requires:       (libcontainers-sles-mounts if (product(SUSE_SLE) or product(SLE-Micro)))
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

%package -n libcontainers-sles-mounts
Summary:        Default mounts for SLE distributions

%description -n libcontainers-sles-mounts
Ships a /etc/containers/mounts.conf with default mounts for SLE distributions

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
cp %{SOURCE9} .
# Apply CNI config on streams other than ALP (bsc#1213556)
# https://github.com/containers/podman/issues/19327
%if 0%{?suse_version} < 1600 && !0%{?is_opensuse}
%patch -P100 -p3
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %_builddir/containers.conf
%endif

%setup -q -Tcq -b0 -b1 -b8
# copy the LICENSE file in the build root
cp %{SOURCE2} .

%build
cd ..
# compile containers/image manpages
cd image-%{imagever}
for md in docs/*.md
do
        go-md2man -in $md -out $md
done
rename '.5.md' '.5' docs/*
rename '.md' '.1' docs/*
cd ..
# compile containers/storage manpages
cd storage-%{storagever}
for md in docs/*.md
do
        go-md2man -in $md -out $md
done
rename '.5.md' '.5' docs/*
rename '.md' '.1' docs/*
cd ..
# compile subset of containers/common manpages
cd common-%{commonver}
go-md2man -in pkg/hooks/docs/oci-hooks.5.md -out pkg/hooks/docs/oci-hooks.5
cd ..

# These would only be used on SLE-systems
# via libcontainers-sles-mounts subpackage
cat >>%{SOURCE5} <<EOL
%{_sysconfdir}/SUSEConnect:%{_sysconfdir}/SUSEConnect
%{_sysconfdir}/zypp/credentials.d/SCCcredentials:%{_sysconfdir}/zypp/credentials.d/SCCcredentials
EOL

# Default to SUSE registry on SL Micro
sed 's/unqualified-search-registries.*/unqualified-search-registries = \["registry.suse.com"\]/' %{SOURCE6} > registries.conf.suse

cd common-%{commonver}
%make_build docs
cd ..

%install
cd ..
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/oci/hooks.d
install -d -m 0755 %{buildroot}/%{_datadir}/containers/oci/hooks.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/registries.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/registries.conf.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/systemd
install -d -m 0755 %{buildroot}/%{_datadir}/containers/systemd

install -D -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/containers/policy.json.default
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/containers/policy.json.openSUSE
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_datadir}/containers/mounts.conf
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_datadir}/containers/storage.conf
install -D -m 0644 %{SOURCE11} %{buildroot}/%{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
install -D -m 0644 %{SOURCE7} %{buildroot}/%{_sysconfdir}/containers/registries.d/default.yaml
install -D -m 0644 %_builddir/containers.conf %{buildroot}/%{_datadir}/containers/containers.conf
install -D -m 0644 common-%{commonver}/pkg/seccomp/seccomp.json %{buildroot}/%{_datadir}/containers/seccomp.json

install -d %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_mandir}/man5
install -D -m 0644 image-%{imagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 image-%{imagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 storage-%{storagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 storage-%{storagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 common-%{commonver}/pkg/hooks/docs/oci-hooks.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 common-%{commonver}/docs/containers-mounts.conf.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 common-%{commonver}/docs/containers.conf.5 %{buildroot}/%{_mandir}/man5/

install -D -m 0644 %{SOURCE12} %{buildroot}/%{_sysconfdir}/containers/policy.json.openSUSE
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/containers/policy.json.default

install -D -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/containers/registries.conf.default
install -D -m 0644 registries.conf.suse %{buildroot}/%{_sysconfdir}/containers/registries.conf.suse

%post
# Comment out ostree_repo if it's blank [boo#1189893]
if [ -f %{_sysconfdir}/containers/storage.conf ]; then sed -i 's/ostree_repo = ""/\#ostree_repo = ""/g' %{_sysconfdir}/containers/storage.conf; fi

%files
%dir %{_sysconfdir}/containers
%dir %{_sysconfdir}/containers/oci
%dir %{_sysconfdir}/containers/oci/hooks.d
%dir %{_sysconfdir}/containers/registries.d
%dir %{_sysconfdir}/containers/registries.conf.d
%dir %{_sysconfdir}/containers/systemd
%dir %{_datadir}/containers
%dir %{_datadir}/containers/oci
%dir %{_datadir}/containers/oci/hooks.d
%dir %{_datadir}/containers/systemd

%config(noreplace) %{_sysconfdir}/containers/registries.d/default.yaml
%config(noreplace) %{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
%{_datadir}/containers/seccomp.json
%{_datadir}/containers/storage.conf
%{_datadir}/containers/containers.conf

%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%license LICENSE

%files -n libcontainers-sles-mounts
%{_datadir}/containers/mounts.conf

%files -n libcontainers-openSUSE-policy
%config(noreplace) %{_sysconfdir}/containers/policy.json.openSUSE

%files -n libcontainers-default-policy
%config(noreplace) %{_sysconfdir}/containers/policy.json.default

%files -n registries-conf-suse
%config(noreplace) %{_sysconfdir}/containers/registries.conf.suse

%files -n registries-conf-default
%config(noreplace) %{_sysconfdir}/containers/registries.conf.default

%changelog
