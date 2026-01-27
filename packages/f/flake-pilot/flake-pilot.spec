#
# spec file for package flake-pilot
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2022 Elektrobit Automotive GmbH
# Copyright (c) 2023 Marcus Schäfer
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


Name:           flake-pilot
Version:        3.1.27
Release:        0
Summary:        Launcher for flake applications
License:        MIT
%if "%{_vendor}" == "debbuild"
Packager:       Marcus Schaefer <marcus.schaefer@suse.com>
%endif
Group:          System/Management
URL:            https://github.com/OSInside/flake-pilot
Source0:        %{name}.tar.gz
Source1:        cargo_config
Source2:        %{name}-rpmlintrc
%if 0%{?debian} || 0%{?ubuntu}
Requires:       golang-github-containers-common
%endif
Requires:       rsync
Requires:       sudo
Requires:       tar
BuildRequires:  python3-docutils
%if 0%{?suse_version}
BuildRequires:  glibc-devel-static
BuildRequires:  python3-Pygments
%endif
%if 0%{?fedora}
BuildRequires:  glibc-static
%endif
%if 0%{?fedora} || 0%{?suse_version}
BuildRequires:  cargo
BuildRequires:  openssl-devel
BuildRequires:  rust
%endif
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  libssl-dev
BuildRequires:  openssl
BuildRequires:  pkg-config
BuildRequires:  python3-pygments
BuildRequires:  rust-all
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Run flake applications using a symlink structure pointing
to a launcher binary which actually launches the application through
a runtime engine like podman. Along with the launcher there is
also a control tool to register an application as a flake application

%package -n flake-pilot-podman
Summary:        Podman pilot
Group:          System/Management
Requires:       podman
Requires:       rsync
Requires:       sudo

%description -n flake-pilot-podman
Launcher for OCI containers based applications through podman

%package -n flake-pilot-firecracker
Summary:        FireCracker pilot
Group:          System/Management
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  clang
%else
BuildRequires:  clang-devel
%endif
Requires:       rsync
%if 0%{?fedora} || 0%{?suse_version} > 1600
Requires:       firecracker
%endif
Requires:       e2fsprogs
Requires:       sudo
Requires:       xz

%description -n flake-pilot-firecracker
Launcher and service tools for KVM VM based applications
through firecracker

%package -n flake-pilot-firecracker-dracut-netstart
Summary:        Dracut Module Network Startup
Group:          System/Management
%if 0%{?fedora} && 0%{?suse_version}
Requires:       systemd-network
%else
Requires:       systemd
%endif
BuildArch:      noarch

%description -n flake-pilot-firecracker-dracut-netstart
Start systemd network and resolver inside of the initrd such
that the network setup persists after switch_root if there
is no systemd process called but sci as simple command
execution interface

%package -n flake-pilot-firecracker-guestvm-tools
Summary:        FireCracker guest VM tools
Group:          System/Management

%description -n flake-pilot-firecracker-guestvm-tools
Guest VM tools to help with firecracker workloads

%prep
%setup -q -n flake-pilot

%build
mkdir -p .cargo
cp %{SOURCE1} .cargo/config.toml
make build
%ifnarch ppc64le
%if 0%{?fedora} || (0%{?suse_version} && 0%{?suse_version} >= 1600)
make compile_sci_static
%endif
%endif

%install
make DESTDIR=%{buildroot}/ install

test -f target/*-unknown-linux-gnu/static/sci && \
make DESTDIR=%{buildroot}/ install_sci_static || \
make DESTDIR=%{buildroot}/ install_sci

mkdir -p %{buildroot}/overlayroot
mkdir -p %{buildroot}/usr/lib/flake-pilot

mkdir -p %{buildroot}/var/lib/firecracker/images

mkdir -p %{buildroot}/var/lib/firecracker/storage

mkdir -p %{buildroot}/etc/dracut.conf.d
mkdir -p %{buildroot}/usr/lib/dracut/modules.d/80netstart
cp -a firecracker-pilot/dracut/usr/lib/dracut/modules.d/80netstart/* \
    %{buildroot}/usr/lib/dracut/modules.d/80netstart
install -m 644 firecracker-pilot/dracut/etc/dracut.conf.d/extramodules.conf \
    %{buildroot}/etc/dracut.conf.d/extramodules.conf

install -m 755 %{buildroot}/usr/sbin/sci \
    %{buildroot}/usr/lib/flake-pilot/sci

mkdir -p %{buildroot}/etc
install -m 644 flakes.yml %{buildroot}/etc/flakes.yml

%files
%defattr(-,root,root)
%dir /etc/flakes
%config /etc/flakes.yml
/usr/bin/flake-ctl
/usr/share/bash-completion/completions/flake-ctl
%doc /usr/share/man/man8/flake-pilot.8.gz
%doc /usr/share/man/man8/flake-ctl.8.gz
%doc /usr/share/man/man8/flake-ctl-list.8.gz

%files -n flake-pilot-podman
%config /etc/flakes/container-flake.yaml
%config /etc/flakes/storage.conf
/usr/bin/podman-pilot
/usr/sbin/flake-registry
%doc /usr/share/man/man8/flake-ctl-podman-load.8.gz
%doc /usr/share/man/man8/flake-ctl-podman-pull.8.gz
%doc /usr/share/man/man8/flake-ctl-podman-register.8.gz
%doc /usr/share/man/man8/flake-ctl-podman-remove.8.gz
%doc /usr/share/man/man8/podman-pilot.8.gz

%files -n flake-pilot-firecracker
%dir /var/lib/firecracker
%dir /var/lib/firecracker/images
%dir /var/lib/firecracker/storage
%dir /usr/lib/flake-pilot
%config /etc/flakes/firecracker-flake.yaml
%config /etc/flakes/firecracker.json
%doc /usr/share/man/man8/flake-ctl-firecracker-pull.8.gz
%doc /usr/share/man/man8/flake-ctl-firecracker-remove.8.gz
%doc /usr/share/man/man8/flake-ctl-firecracker-register.8.gz
/usr/bin/firecracker-pilot
%doc /usr/share/man/man8/firecracker-pilot.8.gz
/usr/lib/flake-pilot/sci

%files -n flake-pilot-firecracker-dracut-netstart
%dir /usr/lib/dracut
%dir /usr/lib/dracut/modules.d
%dir /usr/lib/dracut/modules.d/80netstart
%dir /etc/dracut.conf.d
/usr/lib/dracut/modules.d/80netstart
%config /etc/dracut.conf.d/extramodules.conf

%files -n flake-pilot-firecracker-guestvm-tools
%dir /overlayroot
/usr/sbin/sci
%doc /usr/share/man/man8/sci.8.gz

%changelog
