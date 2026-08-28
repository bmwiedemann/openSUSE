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
Version:        3.1.45
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
# SUSE-specific source additions (1001+)
Source1001:     systemd-tmpfiles-for-suse.conf
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
%if 0%{?fedora} || 0%{?suse_version} == 1699
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

%if 0%{?suse_version} >= 1600
install -D -m 644 %{SOURCE1001} %{buildroot}%{_tmpfilesdir}/flake-pilot-firecracker.conf
%else
mkdir -p %{buildroot}/var/lib/firecracker/images
mkdir -p %{buildroot}/var/lib/firecracker/storage
%endif

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

%pre
# Permissions changed from previous versions, handle the transition
if [ $1 -gt 1 ]; then
    flakes_dir="/tmp/flakes/"
    if [ -d "$flakes_dir/" ]; then
        flakes_perm=$(/usr/bin/stat -c "%a" "$flakes_dir")
        if [ "$flakes_perm" -ne "1777" ]; then
            /usr/bin/chmod +t $flakes_dir
            # If the permissions were not already set we also need to worry
            # about the content.
            # For podman we need a copy of the .cid file in the new hierarchy
            # so flake-pilot knows which Container ID to use to tell podman to
            # shut the container down. podman cleans up the original cid file
            # the copy remains and eventually gets garbage collected by
            # flake pilot
            # For microVMs the .mid file needs to get moved and renamed to
            # allow flake-pilot to clean up
            for filepath in "$flakes_dir"/*; do
                [ -f "$filepath" ] || continue

                filename=$(basename "$filepath")

                # Match format: prefix_username.extension
                # Extract username (part after first '_' and before last '.')
                username=$(echo "$filename" | grep -E '^[^_]+_[^.]+\.' | awk -F'[_.]' '{print $2}')
                # Extract the command name
                cmdname=$(echo "$filename" | grep -E '^[^_]+_[^.]+\.' | awk -F'[_.]' '{print $1}')
                if [ -n "$username" ]; then
                    # Look up UID for the extracted username
                    if uid=$(id -u "$username" 2>/dev/null); then
                        user_dir="$flakes_dir/$uid"
                        # Create user directory if it doesn't exist
                        if [ ! -d "$user_dir" ]; then
                            mkdir -p "$user_dir"
                        fi
                        if [[ "$filename" == *".vmid"* ]]; then
                            mv "$filepath" "$user_dir/$cmdname.vmid"
                        else
                            # We need the .cid files in 2 places
                            cp "$filepath" "$user_dir/$cmdname.cid"
                        fi
                    fi
                    # Fix the directory permissions
                    chown "$uid" "$user_dir"
                    chgrp "$uid" "$user_dir"
                    chmod 700 "$user_dir"
                fi
            done
        fi
    fi
fi


%files
%defattr(-,root,root)
%dir /etc/flakes
%config /etc/flakes.yml
/usr/bin/flake-ctl
/usr/share/bash-completion/completions/flake-ctl
%doc /usr/share/man/man8/flake-pilot.8.gz
%doc /usr/share/man/man8/flake-ctl.8.gz
%doc /usr/share/man/man8/flake-ctl-init.8.gz
%doc /usr/share/man/man8/flake-ctl-list.8.gz

%post
if [ -d /tmp/flakes ];then
    # make sure to move an eventually existing
    # tmp flakes dir to sticky bit permissions
    chmod 1777 /tmp/flakes
fi

%files -n flake-pilot-podman
%config /etc/flakes/container-flake.yaml
%config /etc/flakes/storage.conf
/usr/bin/podman-pilot
/usr/sbin/flake-registry
%doc /usr/share/man/man8/flake-ctl-podman-load.8.gz
%doc /usr/share/man/man8/flake-ctl-podman-pull.8.gz
%doc /usr/share/man/man8/flake-ctl-podman-register.8.gz
%doc /usr/share/man/man8/flake-ctl-podman-remove.8.gz
%doc /usr/share/man/man8/flake-ctl-podman-show.8.gz
%doc /usr/share/man/man8/podman-pilot.8.gz

%files -n flake-pilot-firecracker
%if 0%{?suse_version} >= 1600
%{_tmpfilesdir}/flake-pilot-firecracker.conf
%ghost %dir /var/lib/firecracker
%ghost %dir /var/lib/firecracker/images
%ghost %dir /var/lib/firecracker/storage
%else
%dir /var/lib/firecracker
%dir /var/lib/firecracker/images
%dir /var/lib/firecracker/storage
%endif
%dir /usr/lib/flake-pilot
%config /etc/flakes/firecracker-flake.yaml
%config /etc/flakes/firecracker.json
%doc /usr/share/man/man8/flake-ctl-firecracker-pull.8.gz
%doc /usr/share/man/man8/flake-ctl-firecracker-remove.8.gz
%doc /usr/share/man/man8/flake-ctl-firecracker-register.8.gz
%doc /usr/share/man/man8/flake-ctl-firecracker-show.8.gz
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
