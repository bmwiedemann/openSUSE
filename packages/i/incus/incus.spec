#
# spec file for package incus
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
# nodebuginfo


%go_nostrip

%define _buildshell /bin/bash
%define import_path github.com/lxc/incus

%define incus_datadir %{_datadir}/incus
%define incus_ovmfdir %{incus_datadir}/ovmf

# We need OVMF in order to support VMs with Incus. At the moment this means we
# can only support it on x86_64.
%ifarch x86_64
%define arch_vm_support 1
%else
%define arch_vm_support 0
%endif

Name:           incus
Version:        6.8
%define tag_version 6.8.0
Release:        0
Summary:        Container hypervisor based on LXC
License:        Apache-2.0
Group:          System/Management
URL:            https://linuxcontainers.org/incus/
Source:         https://github.com/lxc/%{name}/releases/download/v%{tag_version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxc/%{name}/releases/download/v%{tag_version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        %{name}-rpmlintrc
Source4:        %{name}.sysusers
# Based on <https://github.com/zabbly/incus/tree/stable/systemd>.
Source100:      incusd
Source101:      %{name}.service
Source102:      %{name}.socket
Source103:      sysconfig.%{name}
Source111:      %{name}-user.service
Source112:      %{name}-user.socket
Source113:      sysconfig.%{name}-user
Source120:      %{name}-startup
Source121:      %{name}-startup.service
# Incus upstream doesn't have a sample config file.
Source130:      %{name}-config.yml
# Additional runtime configuration.
Source201:      %{name}.dnsmasq
BuildRequires:  fdupes
BuildRequires:  file
BuildRequires:  go >= 1.22.7
BuildRequires:  golang-packaging
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  liblz4-devel
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sqlite3-devel >= 3.25
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(cowsql)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lxc) >= 5.0.0
# For completion directories.
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh
Requires:       kernel-base >= 5.4
# Bits required for images and other things at runtime.
Requires:       acl
Requires:       attr
Requires:       ebtables
BuildRequires:  dnsmasq
Requires:       dnsmasq
Requires:       lxcfs
Requires:       lxcfs-hooks-lxc
Requires:       rsync
Requires:       squashfs
Requires:       tar
Requires:       xz
%if 0%{arch_vm_support} != 0
# Needed for VM support.
Requires:       qemu-ovmf-x86_64
BuildRequires:  qemu-ovmf-x86_64
Requires:       qemu-chardev-spice
Requires:       qemu-hw-display-virtio-gpu
Requires:       qemu-hw-display-virtio-vga
Requires:       qemu-hw-usb-redirect
Requires:       qemu-img
Requires:       qemu-spice
Requires:       virtiofsd
# QEMU spice became a separate package for QEMU 5.2, which is not in Leap 15.2.
# But it exists in Tumbleweed so only require this in Tumbleweed.
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150300
Requires:       qemu-ui-spice-core
%else
Requires:       qemu-ui-spice-app
%endif
# TODO: Should we enable non-native VMs by default?
%ifarch %ix86 x86_64
Requires:       qemu-x86 >= 6.0
%endif
%ifarch aarch64 %arm
Requires:       qemu-arm >= 6.0
%endif
%endif
Recommends:     %{name}-tools
# Storage backends -- we don't recommend ZFS since it's not *technically* a
# blessed configuration.
Recommends:     lvm2
Recommends:     btrfsprogs
Recommends:     thin-provisioning-tools
# CRIU is used for certain operations but is not necessary (and is no longer
# shipped on 32-bit openSUSE).
Recommends:     criu >= 2.0
Suggests:       zfs
%sysusers_requires

%description
Incus is a system container manager. It offers a user experience
similar to virtual machines but uses Linux containers (LXC) instead.

%package tools
Summary:        Optional extra tools for %{name}
Group:          System/Management
Requires:       %{name} = %{version}

%description tools
Extra tools to help with the administration of Incus. This includes helpers for
migrating from LXD to Incus as well as a smattering of other helpers that can
be helpful for some users but are not necessary for most Incus deployments
(such as benchmarking tools and tools for managing simplestreams Incus image
servers).

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE4} %{name} %{name}.conf

# Make sure any leftover go build caches are gone.
go clean -cache

# Find all of the main packages using go-list.
readarray -t mainpkgs \
	<<<"$(go list -f '{{.Name}}:{{.ImportPath}}' %{import_path}/... | \
	      awk -F: '$1 == "main" { print $2 }' | \
	      grep -E '^github.com/lxc/incus/(v.*/)?cmd/')"

# Needed because incus and deps use funky #cgo LDFLAGS that Go blocks by default.
export CGO_LDFLAGS_ALLOW="(-Wl,-wrap,pthread_create)|(-Wl,-z,now)"

# The upstream Makefile uses "go install" which doesn't work for packaging.
mkdir bin
for mainpkg in "${mainpkgs[@]}"
do
	# Make sure all binaries contain "incus" somewhere in their name.
	binary="$(basename "$mainpkg")"
	if  ( echo "$binary" | grep -Eqv '%{name}' )
	then
		binary="%{name}-$binary"
	fi
	case "$binary" in
	incus-agent)
		build_static=1
		build_tags="agent,netgo"
		;;
	incus-migrate)
		build_static=1
		build_tags="netgo"
		;;
	*)
		build_static=
		build_tags="libsqlite3"
		;;
	esac
	(
		if [ -n "$build_static" ]
		then
			CGO_ENABLED=0 go build -ldflags "-extldflags -static" \
				-tags "$build_tags" -o "bin/$binary" "$mainpkg"
		else
			go build -buildmode=pie \
				-tags "$build_tags" -o "bin/$binary" "$mainpkg"
		fi
	)
done

# Replace @SUSE_LIBEXEC@ in our sources with the proper directory. This is needed
# because Leap 15.x still uses /usr/lib while Tumbleweed uses /usr/libexec. See
# <https://en.opensuse.org/openSUSE:Specfile_guidelines#Libexecdir> for more
# details.
readarray -t sourcefiles <<<"$(find "%{_sourcedir}" -type f)"
for sourcefile in "${sourcefiles[@]}"
do
	[[ "$(file -b --mime-encoding "$sourcefile")" == "binary" ]] && continue
	sed -i 's|@SUSE_LIBEXEC@|%{_libexecdir}|g' "$sourcefile"
done

# Generate man pages.
mkdir man
./bin/incus manpage man/

# Generate completion scripts.
mkdir -p scripts/completion
for sh in bash zsh fish
do
	./bin/incus completion $sh >scripts/completion/incus.$sh
done

# Final sanity-check during build.
pushd bin/
for bin in *
do
	# Ensure that all our binaries are dynamic (except for incus-agent, which
	# must be static). boo#1138769
	case "$(basename $bin)" in
	incus-agent | incus-migrate)
		file "$bin" | grep 'statically linked'
		;;
	*)
		file "$bin" | grep 'dynamically linked'
		# Check what they are linked against.
		ldd "$bin"
		;;
	esac
done
popd

# Drop the html docs and build-related docs as they are mostly duplicates of
# the markdown docs and give us a bad rpmlint score.
rm -rf doc/{html/,.{sphinx,.wordlist.txt}}

%install
# Install all the binaries.
pushd bin/
for bin in *
do
	case "$bin" in
	incus-user | lxd-to-incus | incus-fuidshift | incus-migrate)
		# - incus-user is only ever run by systemd as root.
		# - lxd-to-incus needs to be run as root to configure everything.
		# - fuidshift is only used by admins to fixup a broken rootfs.
		# - incus-migrate requires root access to scan the host.
		bindir="%{_sbindir}"
		;;
	incusd)
		# Our /usr/sbin/incusd is a wrapper around /usr/libexec/incus/incsud to
		# set some environment variables.
		bindir="%{_libexecdir}/%{name}"
		;;
	incus-agent)
		# incus-agent is only used internally by incus, and is a binary that
		# gets inserted into containers so it isn't even run on the host.
		bindir="%{_libexecdir}/%{name}"
		;;
	*)
		bindir="%{_bindir}"
		;;
	esac
	install -D -m 0755 "$bin" "%{buildroot}$bindir/$bin"
done
popd

# System-wide client configuration.
install -D -m0644 %{S:130} %{buildroot}/etc/incus/config.yml
install -d -m0755 %{buildroot}/etc/incus/servercerts

# Install man pages.
pushd man/
for man in *
do
	section="${man##*.}"
	install -D -m 0644 "$man" "%{buildroot}%{_mandir}/man$section/$man"
done
popd

# *sh-completion
install -D -m 0644 scripts/completion/incus.bash %{buildroot}%{_datarootdir}/bash-completion/completions/incus
install -D -m 0644 scripts/completion/incus.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/incus.fish
install -D -m 0644 scripts/completion/incus.bash %{buildroot}%{_sysconfdir}/zsh_completion.d/_incus

# systemd
install -D -m 0755 %{S:100} %{buildroot}%{_sbindir}/incusd
install -D -m 0644 %{S:101} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{S:102} %{buildroot}%{_unitdir}/%{name}.socket
install -D -m 0644 %{S:111} %{buildroot}%{_unitdir}/%{name}-user.service
install -D -m 0644 %{S:112} %{buildroot}%{_unitdir}/%{name}-user.socket

# sysconfig files
install -D -m 0644 %{S:103} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -D -m 0644 %{S:113} %{buildroot}%{_fillupdir}/sysconfig.%{name}-user

# incus-startup
install -D -m 0755 %{S:120} %{buildroot}%{_libexecdir}/%{name}/%{name}-startup
install -D -m 0644 %{S:121} %{buildroot}%{_unitdir}/%{name}-startup.service

# sysv-init
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-user

# Run-time configuration.
install -D -m 0644 %{S:201} %{buildroot}%{_sysconfdir}/dnsmasq.d/60-incus.conf

# Run-time directories.
install -d -m 0711 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}

# sysusers.d
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf

%if 0%{arch_vm_support} != 0
# In order for VM support in Incus to function, you need to have OVMF configured
# in the way it expects. In particular, Incus depends on specific filenames for
# the firmware files so we create fake ones with symlinks.
mkdir -p %{buildroot}%{incus_ovmfdir}
ln -s %{_datarootdir}/qemu/ovmf-x86_64-4m-code.bin %{buildroot}%{incus_ovmfdir}/OVMF_CODE.4MB.fd
ln -s %{_datarootdir}/qemu/ovmf-x86_64-4m-code.bin %{buildroot}%{incus_ovmfdir}/OVMF_CODE.fd
ln -s %{_datarootdir}/qemu/ovmf-x86_64-4m-vars.bin %{buildroot}%{incus_ovmfdir}/OVMF_VARS.4MB.fd
ln -s %{_datarootdir}/qemu/ovmf-x86_64-ms-4m-vars.bin %{buildroot}%{incus_ovmfdir}/OVMF_VARS.4MB.ms.fd
ln -s %{_datarootdir}/qemu/ovmf-x86_64-4m-vars.bin %{buildroot}%{incus_ovmfdir}/OVMF_VARS.fd
%endif

%fdupes %{buildroot}

%pre -f %{name}.pre

# /etc/sub[ug]id should exist already (it's part of shadow-utils), but older
# distros don't have it. Incus just parses it and doesn't need any special
# shadow-utils helpers.
touch /etc/subuid /etc/subgid ||:

# Add sub[ug]ids for Incus's unprivileged containers -- in order to support
# isolated containers we add quite a few subuids. Since Incus runs as root we add
# them for the root user (not the incus-admin group). We only bother if there
# aren't any mappings available already.
#
# We have no guarantee that the range we pick will be unique -- which ideally
# we would want it to be. There isn't a nice way to do this without
# reimplementing a bunch of range-handling code for /etc/sub[ug]id in bash. So
# we just pick the 400-900 million range, and hope for the best (most tutorials
# use the 1-million range, so we avoid that pitfall).
#
# This default setting of 500 million is enough for ~8000 isolated containers,
# which should be enough for most users.
grep -q '^root:' /etc/subuid || \
	usermod -v 400000000-900000000 root &>/dev/null || \
	echo "root:400000000:500000001" >>/etc/subuid ||:
grep -q '^root:' /etc/subgid || \
	usermod -w 400000000-900000000 root &>/dev/null || \
	echo "root:400000000:500000001" >>/etc/subgid ||:

%service_add_pre %{name}.service %{name}.socket
%service_add_pre %{name}-startup.service
%service_add_pre %{name}-user.service %{name}-user.socket

%post
%service_add_post %{name}.service %{name}.socket
%service_add_post %{name}-startup.service
%fillup_only -n %{name}

%service_add_post %{name}-user.service %{name}-user.socket
%fillup_only -n %{name}-user

%preun
%service_del_preun %{name}.service %{name}.socket
%service_del_preun %{name}-startup.service
%service_del_preun %{name}-user.service %{name}-user.socket

%postun
%service_del_postun %{name}.service %{name}.socket
%service_del_postun %{name}-startup.service
%service_del_postun %{name}-user.service %{name}-user.socket

%files
%defattr(-,root,root)
%doc AUTHORS README.md doc/
%license COPYING
%{_bindir}/incus
%{_sbindir}/incusd
%{_sbindir}/incus-user
%{_mandir}/man*/*

%dir /etc/incus
%config(noreplace) /etc/incus/config.yml
%dir /etc/incus/servercerts

%if 0%{arch_vm_support} != 0
%{incus_datadir}
%endif

%{_libexecdir}/%{name}/
%{_sbindir}/rc%{name}*
%{_unitdir}/%{name}*.service
%{_unitdir}/%{name}*.socket

%{_sysusersdir}/%{name}.conf
%{_fillupdir}/sysconfig.%{name}*

%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/log/%{name}

%config(noreplace) %{_sysconfdir}/dnsmasq.d/60-incus.conf

%files tools
%defattr(-,root,root)
%{_bindir}/incus-benchmark
%{_bindir}/incus-simplestreams
%{_bindir}/lxc-to-incus
%{_sbindir}/incus-fuidshift
%{_sbindir}/incus-migrate
%{_sbindir}/lxd-to-incus

%files bash-completion
%defattr(-,root,root)
%{_datarootdir}/bash-completion/completions/incus

%files fish-completion
%defattr(-,root,root)
%{_datadir}/fish/vendor_completions.d/incus.fish

%files zsh-completion
%defattr(-,root,root)
%{_sysconfdir}/zsh_completion.d/_incus

%changelog
