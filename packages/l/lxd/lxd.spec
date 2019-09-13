#
# spec file for package lxd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           lxd
Version:        3.13
Release:        0
Summary:        Container hypervisor based on LXC
License:        Apache-2.0
Group:          System/Management
URL:            https://linuxcontainers.org/lxd
Source:         https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
Source1:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{name}-rpmlintrc
# LXD upstream doesn't use systemd, they use snapd.
Source100:      %{name}.service
# Additional runtime configuration.
Source200:      %{name}.sysctl
Source201:      %{name}.dnsmasq
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  patchelf
BuildRequires:  pkg-config
BuildRequires:  golang(API) >= 1.10
BuildRequires:  pkgconfig(lxc) >= 3.0.0
# Needed to build the sqlite fork and dqlite.
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig(libuv) >= 1.8.0
BuildRequires:  pkgconfig(tcl)
# Bits required for images and other things at runtime.
Requires:       acl
Requires:       ebtables
BuildRequires:  dnsmasq
Requires:       criu >= 2.0
Requires:       dnsmasq
Requires:       lxcfs
Requires:       lxcfs-hooks-lxc
Requires:       rsync
Requires:       squashfs
Requires:       tar
Requires:       xz
# Storage backends -- we don't recommend ZFS since it's not *technically* a
# blessed configuration.
Recommends:     lvm2
Recommends:     thin-provisioning-tools
Recommends:     btrfsprogs
Suggests:       zfs

%description
LXD is a system container manager. It offers a user experience
similar to virtual machines but uses Linux containers (LXC) instead.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%prep
%setup -q
# Move dist/src (which is LXD's variant of vendoring) to vendor/.
mv -v dist/src vendor

%build
# Make sure any leftover go build caches are gone.
go clean -cache

# Set up GOPATH.
export GOPATH="$PWD/.gopath"
export PKGDIR="$GOPATH/src/%{import_path}"
mkdir -p "$PKGDIR"
cp -a * "$PKGDIR"

# First we need to build the sqlite fork and dqlite. We build them as static
# libs because they are only ever going to be used for LXD, and so it makes no
# sense to go through the pain of packaging them properly (hopefully the code
# will one day be merged into upstream sqlite).
export CFLAGS="%{optflags} -fPIC -DPIC"

# SQLite
pushd "$PKGDIR/dist/sqlite"
autoreconf -fiv
%configure \
	--libdir="%{_libdir}/%{name}" \
	--disable-static \
	--enable-replication \
	--disable-tcl \
make clean
make %{?_smp_mflags}
popd

# dqlite
pushd "$PKGDIR/dist/dqlite"
(
# We need to make sure *our* sqlite build is used.
export PKG_CONFIG_PATH="$PWD/../sqlite/"
export CPPFLAGS="-I$PWD/../sqlite/"
export LDFLAGS="-L$PWD/../sqlite/.libs/"

autoreconf -fiv
%configure \
	--libdir="%{_libdir}/%{name}" \
	--disable-static
make clean
make %{?_smp_mflags}
)
popd

# Find all of the main packages using go-list.
readarray -t mainpkgs \
	<<<"$(go list -f '{{.Name}}:{{.ImportPath}}' %{import_path}/... | \
	      awk -F: '$1 == "main" { print $2 }' | \
	      grep -Ev '^github.com/lxc/lxd/(test|shared)')"

# And now we can finally build LXD and all of the related binaries.
mkdir bin
for mainpkg in "${mainpkgs[@]}"
do
	binary="$(basename "$mainpkg")"
	(
		# We need to link against sqlite and dqlite only when dealing with lxd proper.
		[ "$binary" == "lxd" ] && export \
			BUILDTAGS="libsqlite3" \
			CGO_CFLAGS="%{optflags} -I$PKGDIR/dist/sqlite/ -I$PKGDIR/dist/dqlite/include/" \
			CGO_LDFLAGS="-L$PKGDIR/dist/sqlite/.libs/ -L$PKGDIR/dist/dqlite/.libs/" \
			PKG_CONFIG_PATH="$PKGDIR/dist/sqlite:$PKGDIR/dist/dqlite" ||:
		go build -buildmode=pie -tags "$BUILDTAGS" -o "bin/$binary" "$mainpkg"
	)
done

# This part is quite ugly, so I apologise upfront.
#
# We want to have our dist/* libraries be dylibs so that we don't bloat our lxd
# binary. Unfortunately, we are presented with a few challenges:
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
# sonames for our dist/* libraries. Absolute paths for DT_NEEDED is *slightly*
# undefined behaviour, but glibc has had this behaviour for a very long time --
# and others have considered using it in a similar manner[1].
#
# What F U N.
#
# [1]: https://github.com/NixOS/nixpkgs/issues/24844

# Give our libraries unrecognisable DT_SONAME entries.
patchelf --set-soname '._LXD_INTERNAL-libsqlite3.so.0' "$PKGDIR/dist/sqlite/.libs/libsqlite3.so.0"
patchelf --set-soname '._LXD_INTERNAL-libdqlite.so.0' "$PKGDIR/dist/dqlite/.libs/libdqlite.so.0"

# Switch to absolute DT_NEEDED for the lxd binary.
patchelf --remove-rpath bin/lxd
patchelf --replace-needed {,%{_libdir}/%{name}/}'libsqlite3.so.0' bin/lxd
patchelf --replace-needed {,%{_libdir}/%{name}/}'libdqlite.so.0'  bin/lxd
# Just to be sure, fix libdqlite.so as well.
patchelf --remove-rpath "$PKGDIR/dist/dqlite/.libs/libdqlite.so"
patchelf --replace-needed {,%{_libdir}/%{name}/}'libsqlite3.so.0' "$PKGDIR/dist/dqlite/.libs/libdqlite.so"

# Generate man pages.
mkdir man
./bin/lxc manpage man/

%install
export GOPATH="$PWD/.gopath"
export PKGDIR="$GOPATH/src/%{import_path}"

install -d -m 0755 %{buildroot}%{_libdir}/%{name}
pushd "$PKGDIR"
# We can't use install because *.so.$n are symlinks.
cp -avt %{buildroot}%{_libdir}/%{name}/ dist/sqlite/.libs/libsqlite3.so.*
cp -avt %{buildroot}%{_libdir}/%{name}/ dist/dqlite/.libs/libdqlite.so.*
popd

# Install all the binaries.
pushd bin/
for bin in *
do
	install -D -m 0755 "$bin" "%{buildroot}%{_bindir}/$bin"
done
popd

# Install man pages.
pushd man/
for man in *
do
	section="${man##*.}"
	install -D -m 0644 "$man" "%{buildroot}%{_mandir}/man$section/$man"
done
popd

# bash-completion.
install -D -m 0644 scripts/bash/lxd-client %{buildroot}%{_datadir}/bash-completion/completions/lxd-client

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

%fdupes %{buildroot}

%pre
# Group which owns the lxd socket, which allows people to administer it.
getent group %{name} >/dev/null || groupadd -r %{name}

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
	usermod -v 400000000-900000000 root ||:
grep -q '^root:' /etc/subgid || \
	usermod -w 400000000-900000000 root ||:

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
%{_bindir}/*
%{_mandir}/man*/*
%{_libdir}/%{name}

%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service

%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/log/%{name}

%{_sysctldir}/60-lxd.conf
%config(noreplace) %{_sysconfdir}/dnsmasq.d/60-lxd.conf

%files bash-completion
%defattr(-,root,root)
%{_datadir}/bash-completion/

%changelog
