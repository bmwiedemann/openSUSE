#
# spec file for package flake-pilot
#
# Copyright (c) 2022 Elektrobit Automotive GmbH
# Copyright (c) 2023 Marcus Schäfer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
Name:           flake-pilot
Version:        3.0.13
Release:        0
Summary:        Launcher for flake applications
License:        MIT
%if "%{_vendor}" == "debbuild"
Packager:       Marcus Schaefer <marcus.schaefer@elektrobit.com>
%endif
Group:          System/Management
Url:            https://github.com/OSInside/flake-pilot
Source0:        %{name}.tar.gz
Source1:        cargo_config
Source2:        %{name}-rpmlintrc
%if 0%{?debian} || 0%{?ubuntu}
Requires:       golang-github-containers-common
%endif
Requires:       sudo
Requires:       rsync
Requires:       tar
BuildRequires:  python3-docutils
%if 0%{?suse_version}
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  openssl-devel
BuildRequires:  glibc-devel-static
BuildRequires:  python3-Pygments
%endif
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  rust-all
BuildRequires:  libssl-dev
BuildRequires:  openssl
BuildRequires:  pkg-config
BuildRequires:  python3-pygments
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
Requires:       rsync
Requires:       podman
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
Requires:       firecracker
Requires:       xz
Requires:       e2fsprogs
Requires:       sudo

%description -n flake-pilot-firecracker
Launcher and service tools for KVM VM based applications
through firecracker

%package -n flake-pilot-firecracker-dracut-netstart
Summary:        Dracut Module Network Startup
Group:          System/Management
%if 0%{?suse_version}
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
cp %{SOURCE1} .cargo/config
make build
%ifnarch ppc64le
%if 0%{?suse_version} && 0%{?suse_version} >= 1600
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
%dir /usr/share/flakes
%dir /etc/flakes
%config /etc/flakes.yml
/usr/bin/flake-ctl
/usr/share/bash-completion/completions/flake-ctl
%doc /usr/share/man/man8/flake-pilot.8.gz
%doc /usr/share/man/man8/flake-ctl.8.gz
%doc /usr/share/man/man8/flake-ctl-list.8.gz

%files -n flake-pilot-podman
%config /etc/flakes/container-flake.yaml
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
