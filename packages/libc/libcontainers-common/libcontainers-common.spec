#
# spec file for package libcontainers-common
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


# commonver - version from containers/common
%define commonver 0.14.6

# podman - version from containers/podman
%define podmanver 2.0.3

# storagever - version from containers/storage
%define storagever 1.20.2

# imagever - version from containers/image
%define imagever 5.5.1

Name:           libcontainers-common
Version:        20200727
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
Source7:        podman-%{podmanver}.tar.xz
Source8:        default.yaml
Source9:        common-%{commonver}.tar.xz
Source10:       containers.conf
BuildRequires:  go-go-md2man
Provides:       libcontainers-image
Provides:       libcontainers-storage
Obsoletes:      libcontainers-image
Obsoletes:      libcontainers-storage
Requires(post): util-linux
Requires(post): grep
BuildArch:      noarch

%description
Configuration files and manpages shared by tools that are based on the
github.com/containers libraries, such as Buildah, CRI-O, Podman and Skopeo.

%prep
%setup -Tcq -b0 -b1 -b7 -b9
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
# compile subset of containers/podman manpages
cd podman-%{podmanver}
go-md2man -in docs/source/markdown/containers-mounts.conf.5.md -out docs/source/markdown/containers-mounts.conf.5 
go-md2man -in pkg/hooks/docs/oci-hooks.5.md -out pkg/hooks/docs/oci-hooks.5
cd ..

cd common-%{commonver}
make docs
cd ..

%install
cd ..
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/oci/hooks.d
install -d -m 0755 %{buildroot}/%{_datadir}/containers/oci/hooks.d
install -d -m 0755 %{buildroot}/%{_sysconfdir}/containers/registries.d

install -D -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/containers/policy.json
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/containers/storage.conf
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_datadir}/containers/mounts.conf
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/containers/mounts.conf
install -D -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/containers/registries.conf
install -D -m 0644 %{SOURCE8} %{buildroot}/%{_sysconfdir}/containers/registries.d/default.yaml
sed -e 's-@LIBEXECDIR@-%{_libexecdir}-g' -i %{SOURCE10}
install -D -m 0644 %{SOURCE10} %{buildroot}/%{_datadir}/containers/containers.conf
install -D -m 0644 podman-%{podmanver}/seccomp.json %{buildroot}/%{_datadir}/containers/seccomp.json
install -D -m 0644 podman-%{podmanver}/seccomp.json %{buildroot}/%{_sysconfdir}/containers/seccomp.json

install -d %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_mandir}/man5
install -D -m 0644 image-%{imagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 image-%{imagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 storage-%{storagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 storage-%{storagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 podman-%{podmanver}/pkg/hooks/docs/oci-hooks.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 podman-%{podmanver}/docs/source/markdown/containers-mounts.conf.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 common-%{commonver}/docs/containers.conf.5 %{buildroot}/%{_mandir}/man5/

%post
# If installing, check if /var/lib/containers (or /var/lib in its defect) is btrfs and set driver
# to "btrfs" if true
if [ $1 -eq 1 ] ; then
  fstype=$((findmnt -o FSTYPE -l --target /var/lib/containers || findmnt -o FSTYPE -l --target /var/lib) | grep -v FSTYPE)
  if [ "$fstype" = "btrfs" ]; then
    sed -i 's/driver = ""/driver = "btrfs"/g' %{_sysconfdir}/containers/storage.conf
  fi
fi

%files
%dir %{_sysconfdir}/containers
%dir %{_sysconfdir}/containers/oci
%dir %{_sysconfdir}/containers/oci/hooks.d
%dir %{_sysconfdir}/containers/registries.d
%dir %{_datadir}/containers
%dir %{_datadir}/containers/oci
%dir %{_datadir}/containers/oci/hooks.d

%config(noreplace) %{_sysconfdir}/containers/policy.json
%config(noreplace) %{_sysconfdir}/containers/storage.conf
%config(noreplace) %{_sysconfdir}/containers/mounts.conf
%{_datadir}/containers/mounts.conf
%config(noreplace) %{_sysconfdir}/containers/registries.conf
%config(noreplace) %{_sysconfdir}/containers/seccomp.json
%config(noreplace) %{_sysconfdir}/containers/registries.d/default.yaml
%{_datadir}/containers/seccomp.json
%{_datadir}/containers/containers.conf

%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%license LICENSE

%changelog
