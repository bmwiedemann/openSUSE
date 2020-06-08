#
# spec file for package libcontainers-common
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# libpodver - version from containers/libpod
%define libpodver 1.9.3

# storagever - version from containers/storage
%define storagever 1.19.1

# imagever - version from containers/image
%define imagever 5.4.4

Name:           libcontainers-common
Version:        20200603
Release:        0
Summary:        Configuration files common to github.com/containers
License:        Apache-2.0 and GPL-3.0+
Group:          System/Management
URL:            https://github.com/containers
Source0:        image-%{imagever}.tar.xz
Source1:        storage-%{storagever}.tar.xz
Source2:        LICENSE
Source3:        policy.json
Source4:        storage.conf
Source5:        mounts.conf
Source6:        registries.conf
Source7:        libpod-%{libpodver}.tar.xz
Source8:        default.yaml
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
%setup -q -T -D -b 0 -n image-%{imagever}
%setup -q -T -D -b 1 -n storage-%{storagever}
%setup -q -T -D -b 7 -n libpod-%{libpodver}
# copy the LICENSE file in the build root
cd ..
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
# compile subset of containers/libpod manpages
cd libpod-%{libpodver}
go-md2man -in docs/source/markdown/containers-mounts.conf.5.md -out docs/source/markdown/containers-mounts.conf.5 
go-md2man -in pkg/hooks/docs/oci-hooks.5.md -out pkg/hooks/docs/oci-hooks.5
cd ..

%if 0%{?is_opensuse}
# no default mounts
%else
cat >>%{SOURCE5} <<EOL
/etc/SUSEConnect:/etc/SUSEConnect
/etc/zypp/credentials.d/SCCcredentials:/etc/zypp/credentials.d/SCCcredentials
EOL
%endif

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
install -D -m 0644 libpod-%{libpodver}/seccomp.json %{buildroot}/%{_datadir}/containers/seccomp.json
install -D -m 0644 libpod-%{libpodver}/seccomp.json %{buildroot}/%{_sysconfdir}/containers/seccomp.json

install -d %{buildroot}/%{_mandir}/man1
install -d %{buildroot}/%{_mandir}/man5
install -D -m 0644 image-%{imagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 image-%{imagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 storage-%{storagever}/docs/*.1 %{buildroot}/%{_mandir}/man1/
install -D -m 0644 storage-%{storagever}/docs/*.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 libpod-%{libpodver}/pkg/hooks/docs/oci-hooks.5 %{buildroot}/%{_mandir}/man5/
install -D -m 0644 libpod-%{libpodver}/docs/source/markdown/containers-mounts.conf.5 %{buildroot}/%{_mandir}/man5/

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

%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%license LICENSE

%changelog
