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
Version:        3.2.19
Release:        0
Summary:        Launcher for flake applications
License:        MIT
%if "%{_vendor}" == "debbuild"
Packager:       Marcus Schaefer <marcus.schaefer@suse.com>
%endif
Group:          System/Management
URL:            https://github.com/OSInside/flake-pilot
Source0:        %{name}.tar.gz
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
BuildRequires:  systemd-rpm-macros
%endif
%if 0%{?debian} || 0%{?ubuntu}
BuildRequires:  libssl-dev
BuildRequires:  openssl
BuildRequires:  pkg-config
BuildRequires:  python3-pygments
BuildRequires:  rust-all
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{!?_tmpfilesdir:%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d}
%global sci_static no
%ifnarch ppc64le
%if 0%{?fedora} || (0%{?suse_version} && 0%{?suse_version} >= 1600)
%global sci_static yes
%endif
%endif
%global tmpfiles_statedirs no
%if 0%{?suse_version} >= 1600
%global tmpfiles_statedirs yes
%endif

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
# the helper runs system wide flakes for the calling user
Requires:       flake-pilot = %{version}-%{release}

%description -n flake-pilot-podman
Launcher for OCI containers based applications through podman

%package -n flake-pilot-bubblewrap
Summary:        Bubblewrap pilot
Group:          System/Management
Requires:       bubblewrap
Requires:       sudo
# the helper mounts a root filesystem with mount points below it
Requires:       flake-pilot = %{version}-%{release}

%description -n flake-pilot-bubblewrap
Launcher for applications running in a bubblewrap sandbox

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
Requires:       nfs-kernel-server
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
Requires:       nfs-client

%description -n flake-pilot-firecracker-guestvm-tools
Guest VM tools to help with firecracker workloads

%prep
%setup -q -n flake-pilot

%build
make SCI_STATIC=%{sci_static} build

%install
make DESTDIR=%{buildroot}/ \
    TMPFILESDIR=%{_tmpfilesdir} \
    TMPFILES_STATEDIRS=%{tmpfiles_statedirs} \
    install

# After 3.1.37 the organization and permission handling of state files
# has changed. Handle the transition
%triggerun -- flake-pilot <= 3.1.37
    flakes_dir="/tmp/flakes"
    if [ -d "$flakes_dir" ] && [ ! -L "$flakes_dir" ]; then
        # While we operate on the directory we need to ensure root
        # is in control
        # Do not follow symlinks for the permission operations. An
        # attacker might have replaced the directory we checked for with a
        # link by the time we get here.
        chown -h root "$flakes_dir"
        chgrp -h root /tmp/flakes
        chmod -h 600 /tmp/flakes
        # Verify we have what we expect
        flakes_perm=$(/usr/bin/stat -c "%u:%g:%a" "$flakes_dir")
        if [ "$flakes_perm" != "0:0:600" ]; then
            echo "Improper permissions on $flakes_dir please remove "
            echo "to start over"
            exit 0
        fi
        usr_flakes=$(ls -d "$flakes_dir"/*/ 2> /dev/null)
        # If subdirectories exist we are already on the version of flake
        # that has the expected structure, or the user did something they
        # were not supposed to do. In either case we skip any operation
        if [ -z "$usr_flakes" ]; then
            # For podman we need a copy of the .cid file in the new
            # hierarchy so flake-pilot knows which Container ID to
            # use to tell podman to shut the container down. podman
            # cleans up the original cid file the copy remains and
            # eventually gets garbage collected by flake pilot
            # For microVMs the .mid file needs to get moved and renamed to
            # allow flake-pilot to clean up
            created_dirs=" "
            for filepath in "$flakes_dir"/*; do
	        if [ -L "$filepath" ] || [ ! -f "$filepath" ]; then
		    continue
	        fi	     

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
		        case "$created_dirs" in
                            *" $uid "*) ;;
                            *)
                                if [ -e "$user_dir" ] || [ -L "$user_dir" ]; then
		                    echo "$user_dir exists, this is unexpected."
			            echo "Stop any running flakes (aws, az) and "
			            echo "remove $flakes_dir. Cannot migrate to"
			            echo "new structure in a safe way."
				    # Set the permissions back to what we expected before we started
	                            chmod -h 777 "$flakes_dir"
			            exit 0
                                fi
                                mkdir "$user_dir"
                                created_dirs="$created_dirs$uid "
                            ;;
                        esac
                        if [[ "$filename" == *".vmid"* ]]; then
                            mv -T "$filepath" "$user_dir/$cmdname.vmid"
                        else
                            # We need the .cid files in 2 places
                            cp --no-dereference --remove-destination "$filepath" "$user_dir/$cmdname.cid"
                        fi
                    fi
                    # Fix the directory permissions
                    chown -h "$uid" "$user_dir"
                    chgrp -h "$uid" "$user_dir"
                    chmod -h 700 "$user_dir"
                fi
            done
            # Now set the top level directory to the desired permissions
            chmod 1777 $flakes_dir
	    exit 0
        fi
	# If we get here something went wrong set the permissions back to
	# our expected starting state
	chmod -h 777 "$flakes_dir"
    fi

%post
# Create the meta data directory now, not only at the next boot.
# An existing directory which belongs to another user is handed
# over to root
%if 0%{?suse_version} || 0%{?fedora}
%tmpfiles_create flake-pilot.conf
%else
if [ -x /usr/bin/systemd-tmpfiles ]; then
    /usr/bin/systemd-tmpfiles --create %{_tmpfilesdir}/flake-pilot.conf || :
fi
%endif

%files
%defattr(-,root,root)
%dir /etc/flakes
%config /etc/flakes.yml
%{_tmpfilesdir}/flake-pilot.conf
%{_bindir}/flake-ctl
# The helper performs every privileged action of flake-pilot. It is
# called through sudo and must only be writable by root. Its path
# is compiled into the tools calling it
%dir /usr/libexec/flake-pilot
%attr(0755,root,root) /usr/libexec/flake-pilot/flake-pilot-helper
%{_datadir}/bash-completion/completions/flake-ctl
%doc doc/sudoers/flake-pilot.sudoers
%doc %{_mandir}/man8/flake-pilot-helper.8.gz
%doc %{_mandir}/man8/flake-pilot.8.gz
%doc %{_mandir}/man8/flake-ctl.8.gz
%doc %{_mandir}/man8/flake-ctl-init.8.gz
%doc %{_mandir}/man8/flake-ctl-list.8.gz

%post -n flake-pilot-podman
%if 0%{?suse_version} >= 1600
  %tmpfiles_create flake-pilot-podman.conf
%endif

%files -n flake-pilot-podman
%config /etc/flakes/container-flake.yaml
%config /etc/flakes/storage.conf
%if 0%{?suse_version} >= 1600
%{_tmpfilesdir}/flake-pilot-podman.conf
%ghost %dir /var/lib/podman
%ghost %dir %attr(0700,root,root) /var/lib/podman/storage
%else
%dir /var/lib/podman
%dir %attr(0700,root,root) /var/lib/podman/storage
%endif
%dir /usr/lib/podman
%dir %attr(0700,root,root) /usr/lib/podman/storage
%{_bindir}/podman-pilot
/usr/sbin/flake-registry
%doc %{_mandir}/man8/flake-ctl-podman-export.8.gz
%doc %{_mandir}/man8/flake-ctl-podman-load.8.gz
%doc %{_mandir}/man8/flake-ctl-podman-build.8.gz
%doc %{_mandir}/man8/flake-ctl-podman-pull.8.gz
%doc %{_mandir}/man8/flake-ctl-podman-register.8.gz
%doc %{_mandir}/man8/flake-ctl-podman-remove.8.gz
%doc %{_mandir}/man8/flake-ctl-podman-reset.8.gz
%doc %{_mandir}/man8/flake-ctl-podman-show.8.gz
%doc %{_mandir}/man8/podman-pilot.8.gz

%files -n flake-pilot-bubblewrap
%config /etc/flakes/bubblewrap-flake.yaml
%{_bindir}/bubblewrap-pilot
%doc %{_mandir}/man8/flake-ctl-bubblewrap-register.8.gz
%doc %{_mandir}/man8/flake-ctl-bubblewrap-remove.8.gz
%doc %{_mandir}/man8/flake-ctl-bubblewrap-show.8.gz
%doc %{_mandir}/man8/bubblewrap-pilot.8.gz

%if 0%{?suse_version} >= 1600
%post -n flake-pilot-firecracker
%tmpfiles_create flake-pilot-firecracker.conf
%endif

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
%config /etc/flakes/firecracker-flake.yaml
%config /etc/flakes/firecracker.json
%doc %{_mandir}/man8/flake-ctl-firecracker-pull.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-build.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-remove.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-register.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-show.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-network-init.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-network-add.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-network-remove.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-network-cleanup.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-volume-export.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-volume-release.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-volume-add.8.gz
%doc %{_mandir}/man8/flake-ctl-firecracker-volume-remove.8.gz
%{_bindir}/firecracker-pilot
%doc %{_mandir}/man8/firecracker-pilot.8.gz

%files -n flake-pilot-firecracker-dracut-netstart
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%dir %{_prefix}/lib/dracut/modules.d/80netstart
%dir /etc/dracut.conf.d
%{_prefix}/lib/dracut/modules.d/80netstart
%config /etc/dracut.conf.d/extramodules.conf

%files -n flake-pilot-firecracker-guestvm-tools
%dir /overlayroot
/usr/sbin/sci
%doc %{_mandir}/man8/sci.8.gz

%changelog
