#
# spec file for package lxd
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
# nodebuginfo


%go_nostrip

%define _buildshell /bin/bash
%define import_path github.com/lxc/lxd

%define lxd_datadir %{_datadir}/lxd
%define lxd_ovmfdir %{lxd_datadir}/ovmf

# We need OVMF in order to support VMs with LXD. At the moment this means we
# can only support it on x86_64.
%ifarch x86_64
%define arch_vm_support 1
%else
%define arch_vm_support 0
%endif

Name:           lxd
Version:        5.9
Release:        0
Summary:        Container hypervisor based on LXC
License:        Apache-2.0
Group:          System/Management
URL:            https://linuxcontainers.org/lxd
Source:         https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
Source1:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{name}-rpmlintrc
Source4:        %{name}.sysusers
# LXD upstream doesn't use systemd, they use snapd.
Source100:      %{name}.service
# LXD upstream doesn't have a sample config file.
Source101:      %{name}-config.yml
# Additional runtime configuration.
Source200:      %{name}.sysctl
Source201:      %{name}.dnsmasq
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  liblz4-devel
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  sqlite3-devel >= 3.25
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lxc) >= 4.0.0
# Due to a limitation in openSUSE's Go packaging we cannot have a BuildRequires
# for 'golang(API) >= 1.18' here, so just require 1.18 exactly. bsc#1172608
BuildRequires:  golang(API) = 1.18
# Needed to build dqlite and raft.
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(libuv) >= 1.8.0
Requires:       kernel-base >= 5.4
# Bits required for images and other things at runtime.
Requires:       acl
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
# QEMU spice became a separate package for QEMU 5.2, which is not in Leap 15.2.
# But it exists in Tumbleweed so only require this in Tumbleweed.
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150300
Requires:       qemu-ui-spice-core
%else
Requires:       qemu-ui-spice-app
%endif
%ifarch %ix86 x86_64
Requires:       qemu-x86 >= 6.0
%endif
%ifarch aarch64 %arm
Requires:       qemu-arm >= 6.0
%endif
%endif
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
LXD is a system container manager. It offers a user experience
similar to virtual machines but uses Linux containers (LXC) instead.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%prep
%setup -q

%build
%sysusers_generate_pre %{SOURCE4} %{name} %{name}.conf
# Make sure any leftover go build caches are gone.
go clean -cache

# Set up temporary installation paths.
export INSTALL_ROOT="$PWD/.install"
export INSTALL_INCLUDEDIR="$INSTALL_ROOT/%{_includedir}"
export INSTALL_LIBDIR="$INSTALL_ROOT/%{_libdir}/%{name}"

# We first need to build all of the LXD-specific dependencies. To avoid binary
# bloat, we build them as dylibs -- but we then later need to mess around with
# the ELF headers to stop the openSUSE packaging scripts from freaking out.
export CFLAGS="%{optflags} -fPIC -DPIC"

# We have a temporary-install directory which contains all of the dylib deps.
export PKG_CONFIG_SYSROOT_DIR="$INSTALL_ROOT"
export PKG_CONFIG_PATH="$INSTALL_LIBDIR/pkgconfig"
# For some reason, Leap need us to specify this explicitly now.
export CPPFLAGS="-I$INSTALL_INCLUDEDIR"

# raft
pushd "vendor/raft"
autoreconf -fiv
%configure \
	--libdir="%{_libdir}/%{name}" \
	--disable-static
make %{?_smp_mflags}
make DESTDIR="$INSTALL_ROOT" install
popd

# dqlite
pushd "vendor/dqlite"
(
autoreconf -fiv
%configure \
	--libdir="%{_libdir}/%{name}" \
	--disable-static
make clean
make %{?_smp_mflags}
make DESTDIR="$INSTALL_ROOT" install
)
popd

# Find all of the main packages using go-list.
readarray -t mainpkgs \
	<<<"$(go list -f '{{.Name}}:{{.ImportPath}}' %{import_path}/... | \
	      awk -F: '$1 == "main" { print $2 }' | \
	      grep -Ev '^github.com/lxc/lxd/(test|shared)')"

# Needed because lxd and deps use funky #cgo LDFLAGS that Go blocks by default.
export CGO_LDFLAGS_ALLOW="(-Wl,-wrap,pthread_create)|(-Wl,-z,now)"

# And now we can finally build LXD and all of the related binaries.
mkdir bin
for mainpkg in "${mainpkgs[@]}"
do
	# Make sure all binaries *except* "lxc" have an lxd- prefix.
	binary="$(basename "$mainpkg")"
	if  ( echo "$binary" | grep -Eqv '^lx[cd].*$' )
	then
		binary="lxd-$binary"
	fi
	case "$binary" in
		lxd-agent)
			build_static=1
			build_tags="agent,netgo"
			;;
		lxd-p2c)
			build_static=1
			build_tags="netgo"
			;;
		*)
			build_static=
			build_tags="libsqlite3"
			;;
	esac
	(
		# We need to link against our particular dylib deps.
		export \
			CGO_CFLAGS="-I $INSTALL_INCLUDEDIR" \
			CGO_LDFLAGS="-L $INSTALL_LIBDIR" ||:

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

# This part is quite ugly, so I apologise upfront.
#
# We want to have our vendor/* libraries be dylibs so that we don't bloat our
# lxd binary. Unfortunately, we are presented with a few challenges:
#
#  * Doing this naively (put it in {_libdir}) results in sqlite3 package
#    conflicts -- and we aren't going to maintain sqlite3 for all of openSUSE
#    here.
#
#  * Putting everything in a hidden {_libdir}/{name} with RUNPATH configured
#    accordingly works a little better, but still results in lxd ending up with
#    {Provides,Requires}: libsqlite3.so.0. This results in more esoteric
#    conflicts but is still an issue (we'd need to add Prefer: libsqlite3-0
#    everywhere).
#
# So, the only reasonable choice left is to use absolute paths as DT_NEEDED
# entries -- which bypasses the need for RUNPATH and allows us to set garbage
# sonames for our vendor/* libraries. Absolute paths for DT_NEEDED is
# *slightly* undefined behaviour, but glibc has had this behaviour for a very
# long time -- and others have considered using it in a similar manner[1].
#
# What F U N.
#
# [1]: https://github.com/NixOS/nixpkgs/issues/24844

(
	# A simple check that lxd isn't broken. We can't do this after patchelf
	# because we'd need to chroot(2) into {buildroot} which isn't permitted due
	# to user namespaces being blocked inside rpmbuild. boo#1138769
	export LD_LIBRARY_PATH="$INSTALL_LIBDIR"
	./bin/lxd help
)

for lib in "$INSTALL_LIBDIR"/lib*.so
do
	# Strip off last two version digits.
	name="$(basename "$(readlink "$lib")" | sed -E 's/\.[0-9]+\.[0-9]+$//')"
	# Give our libraries unrecognisable DT_SONAME entries.
	patchelf --set-soname "._LXD_INTERNAL-$name" "$lib"
	# Make sure they're executable.
	chmod +x "$lib"
done

# Switch to absolute DT_NEEDED for all dylibs we have as well as the main LXD
# binary. We do this for all dylibs to make sure we don't end up with weird
# chain-loading problems.
for target in bin/* "$INSTALL_LIBDIR"/lib*.so
do
	case "$(basename "$target")" in
		lxd-agent|lxd-p2c)
			# Cannot patch static binaries, and the patching isn't necessary
			# for them anyway.
			continue
			;;
		*)
			;;
	esac

	# Drop RPATH in case it got included during builds.
	patchelf --remove-rpath "$target"
	# And now replace all the possible DT_NEEDEDs to absolute paths.
	for lib in "$INSTALL_LIBDIR"/lib*.so
	do
		# Strip off last two version digits.
		name="$(basename "$(readlink "$lib")" | sed -E 's/\.[0-9]+\.[0-9]+$//')"
		patchelf --replace-needed {,%{_libdir}/%{name}/}"$name" "$target"
	done
done

# Generate man pages.
mkdir man
./bin/lxc manpage man/

# Final sanity-check during build.
pushd bin/
for bin in *
do
	# Ensure that all our binaries are dynamic (except for lxd-p2c and
	# lxd-agent, which must be static). boo#1138769
	case "$(basename $bin)" in
		lxd-agent|lxd-p2c)
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

%install
export INSTALL_LIBDIR="$PWD/.install/%{_libdir}/%{name}"

install -d -m 0755 %{buildroot}%{_libdir}/%{name}
# We can't use install because *.so.$n are symlinks.
cp -avt %{buildroot}%{_libdir}/%{name}/ "$INSTALL_LIBDIR"/lib*.so.*

# Install all the binaries.
pushd bin/
for bin in *
do
	install -D -m 0755 "$bin" "%{buildroot}%{_bindir}/$bin"
done
popd

# System-wide client configuration.
install -D -m0644 %{S:101} %{buildroot}/etc/lxd/config.yml
install -d -m0755 %{buildroot}/etc/lxd/servercerts

# Install man pages.
pushd man/
for man in *
do
	section="${man##*.}"
	install -D -m 0644 "$man" "%{buildroot}%{_mandir}/man$section/$man"
done
popd

# bash-completion.
install -D -m 0644 scripts/bash/lxd-client %{buildroot}%{_datadir}/bash-completion/completions/lxc

# sysv-init and systemd setup.
install -D -m 0644 %{S:100} %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# Run-time configuration.
install -D -m 0644 %{S:200} %{buildroot}%{_sysctldir}/60-lxd.conf
install -D -m 0644 %{S:201} %{buildroot}%{_sysconfdir}/dnsmasq.d/60-lxd.conf

# Run-time directories.
install -d -m 0711 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}

# sysusers.d
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf

%if 0%{arch_vm_support} != 0
# In order for VM support in LXD to function, you need to have OVMF configured
# in the way it expects. In particular, LXD depends on specific filenames for
# the firmware files so we create fake ones with symlinks.
mkdir -p %{buildroot}%{lxd_ovmfdir}
ln -s %{_datarootdir}/qemu/ovmf-x86_64-code.bin %{buildroot}%{lxd_ovmfdir}/OVMF_CODE.fd
ln -s %{_datarootdir}/qemu/ovmf-x86_64-vars.bin %{buildroot}%{lxd_ovmfdir}/OVMF_VARS.fd
ln -s OVMF_VARS.fd %{buildroot}%{lxd_ovmfdir}/OVMF_VARS.ms.fd
%endif

%fdupes %{buildroot}

%pre -f %{name}.pre

# /etc/sub[ug]id should exist already (it's part of shadow-utils), but older
# distros don't have it. LXD just parses it and doesn't need any special
# shadow-utils helpers.
touch /etc/subuid /etc/subgid ||:

# Add sub[ug]ids for LXD's unprivileged containers -- in order to support
# isolated containers we add quite a few subuids. Since LXD runs as root we add
# them for the root user (not the lxd group). We only bother if there aren't
# any mappings available already.
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

%service_add_pre %{name}.service

%post
%sysctl_apply
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%sysctl_apply
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%doc AUTHORS README.md doc/
%license COPYING
%{_bindir}/lx{c,d}*
%{_mandir}/man*/*
%{_libdir}/%{name}

%dir /etc/lxd
%config(noreplace) /etc/lxd/config.yml
%dir /etc/lxd/servercerts

%if 0%{arch_vm_support} != 0
%{lxd_datadir}
%endif

%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf

%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/log/%{name}

%{_sysctldir}/60-lxd.conf
%config(noreplace) %{_sysconfdir}/dnsmasq.d/60-lxd.conf

%files bash-completion
%defattr(-,root,root)
%{_datadir}/bash-completion/

%changelog
