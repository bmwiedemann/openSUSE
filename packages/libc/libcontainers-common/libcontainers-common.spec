#
# spec file for package libcontainers-common
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


# commonver - version from containers/common
%define commonver 0.50.1
# storagever - version from containers/storage
%define storagever 1.44.0
# imagever - version from containers/image
%define imagever 5.23.1
Name:           libcontainers-common
Version:        20221122
Release:        0
Summary:        Configuration files common to github.com/containers
License:        Apache-2.0 AND GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/containers
Source0:        image-%{imagever}.tar.xz
Source1:        storage-%{storagever}.tar.xz
Source2:        LICENSE
Source3:        policy.json
Source4:        storage.conf
Source5:        mounts.conf
Source6:        registries.conf
Source7:        default.yaml
Source8:        common-%{commonver}.tar.xz
Source9:        containers.conf
Source10:       %{name}.rpmlintrc
Source11:       shortnames.conf
Source12:       container-storage-driver.sh
BuildRequires:  go-go-md2man
Requires(post): %{_bindir}/grep
Requires(post): %{_bindir}/sed
Requires:       util-linux-systemd
Requires(post): util-linux-systemd
Provides:       libcontainers-image = %{version}
Provides:       libcontainers-storage = %{version}
Obsoletes:      libcontainers-image < %{version}
Obsoletes:      libcontainers-storage < %{version}
BuildArch:      noarch

%description
Configuration files and manpages shared by tools that are based on the
github.com/containers libraries, such as Buildah, CRI-O, Podman and Skopeo.

%prep
%setup -q -Tcq -b0 -b1 -b8
# copy the LICENSE file in the build root
cp %{SOURCE2} .

%build
cd ..
pwd
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

%if 0%{?is_opensuse}
# no default mounts
%else
cat >>%{SOURCE5} <<EOL
%{_sysconfdir}/SUSEConnect:%{_sysconfdir}/SUSEConnect
%{_sysconfdir}/zypp/credentials.d/SCCcredentials:%{_sysconfdir}/zypp/credentials.d/SCCcredentials
EOL
%endif

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

install -D -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/containers/policy.json
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/containers/storage.conf
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_datadir}/containers/mounts.conf
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/containers/mounts.conf
install -D -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/containers/registries.conf
install -D -m 0644 %{SOURCE11} %{buildroot}/%{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
%if 0%{?suse_version} == 1500
# /usr/etc/ does not work on Leap & SLE
install -D -m 0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/profile.d/libcontainers-common-storage.sh
%else
install -D -m 0644 %{SOURCE12} %{buildroot}%{_prefix}%{_sysconfdir}/profile.d/libcontainers-common-storage.sh
%endif
install -D -m 0644 %{SOURCE7} %{buildroot}/%{_sysconfdir}/containers/registries.d/default.yaml
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE9}
install -D -m 0644 %{SOURCE9} %{buildroot}/%{_datadir}/containers/containers.conf
install -D -m 0644 common-%{commonver}/pkg/seccomp/seccomp.json %{buildroot}/%{_datadir}/containers/seccomp.json
install -D -m 0644 common-%{commonver}/pkg/seccomp/seccomp.json %{buildroot}/%{_sysconfdir}/containers/seccomp.json

install -d %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_mandir}/man5
install -D -m 0644 image-%{imagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 image-%{imagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 storage-%{storagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 storage-%{storagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 common-%{commonver}/pkg/hooks/docs/oci-hooks.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 common-%{commonver}/docs/containers-mounts.conf.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 common-%{commonver}/docs/containers.conf.5 %{buildroot}/%{_mandir}/man5/

%post
# Comment out ostree_repo if it's blank [boo#1189893]
sed -i 's/ostree_repo = ""/\#ostree_repo = ""/g' %{_sysconfdir}/containers/storage.conf
# use btrfs storage driver if system storage is on btrfs
# For rootless it will fall back to overlay if btrfs is not working
# https://github.com/containers/storage/blob/main/docs/containers-storage.conf.5.md#storage-table
if [ $1 -eq 1 ] ; then
  for dir in %{_localstatedir}/lib/containers %{_localstatedir}/lib ; do
    test "$(findmnt -o FSTYPE -l --target '$dir' | grep -v FSTYPE)" != "btrfs" && CONTAINERS_USE_BTRFS_DRIVER=0
  done
  if [ "$CONTAINERS_USE_BTRFS_DRIVER" != "0" ]; then
    sed -i 's/driver = "overlay"/driver = "btrfs"/g' %{_sysconfdir}/containers/storage.conf
  fi
fi

%files
%dir %{_sysconfdir}/containers
%dir %{_sysconfdir}/containers/oci
%dir %{_sysconfdir}/containers/oci/hooks.d
%dir %{_sysconfdir}/containers/registries.d
%dir %{_sysconfdir}/containers/registries.conf.d
%dir %{_datadir}/containers
%dir %{_datadir}/containers/oci
%dir %{_datadir}/containers/oci/hooks.d

%config(noreplace) %{_sysconfdir}/containers/policy.json
%config(noreplace) %{_sysconfdir}/containers/storage.conf
%config(noreplace) %{_sysconfdir}/containers/mounts.conf
%if 0%{?suse_version} == 1500
%{_sysconfdir}/profile.d/libcontainers-common-storage.sh
%else
%{_prefix}%{_sysconfdir}/profile.d/libcontainers-common-storage.sh
%endif
%{_datadir}/containers/mounts.conf
%config(noreplace) %{_sysconfdir}/containers/registries.conf
%config(noreplace) %{_sysconfdir}/containers/seccomp.json
%config(noreplace) %{_sysconfdir}/containers/registries.d/default.yaml
%config(noreplace) %{_sysconfdir}/containers/registries.conf.d/000-shortnames.conf
%{_datadir}/containers/seccomp.json
%{_datadir}/containers/containers.conf

%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%license LICENSE

%changelog
