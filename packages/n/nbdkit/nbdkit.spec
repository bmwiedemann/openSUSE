#
# spec file for package nbdkit
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_with nbdkit_libguestfs

# Architectures where the complete test suite must pass.
#
# On all other architectures, a simpler test suite must pass.  This
# omits any tests that run full qemu, since running qemu under TCG is
# often broken on non-x86_64 arches.
%global complete_test_arches x86_64
%global broken_test_arches %{arm} aarch64 %{ix86}

Name:           nbdkit
Version:        1.44.4
Release:        0
Summary:        Network Block Device server
License:        BSD-3-Clause
URL:            https://gitlab.com/nbdkit/nbdkit
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  jq
BuildRequires:  libtool
BuildRequires:  openssh
BuildRequires:  pkg-config
BuildRequires:  qemu-tools
BuildRequires:  socat
BuildRequires:  xorriso
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls) >= 3.3.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libnbd) >= 1.3.11
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib) >= 1.2.3.5
%if %{with nbdkit_libguestfs}
BuildRequires:  guestfs-tools
BuildRequires:  pkgconfig(libguestfs)
%endif

# nbdkit is a metapackage pulling the server and a useful subset
# of the plugins and filters.
Requires:       nbdkit-basic-filters = %{version}-%{release}
Requires:       nbdkit-basic-plugins = %{version}-%{release}
Requires:       nbdkit-server = %{version}-%{release}

%description
NBD is a protocol for accessing block devices (hard disks and
disk-like things) over the network.

nbdkit is a toolkit for creating NBD servers.

The key features are:

* Multithreaded NBD server written in C.

* Minimal dependencies for the basic server.

* Documented plugin API with a stable ABI guarantee.
  Lets you to export "unconventional" block devices.

* You can write plugins in C or many other languages.

* Filters can be stacked in front of plugins to transform the output.

'%{name}' is a meta-package which pulls in the core server and a
subset of plugins and filters with minimal dependencies.

If you want just the server, install '%{name}-server'.

To develop plugins, install the '%{name}-devel' package and start by
reading the nbdkit(1) and nbdkit-plugin(3) manual pages.

%package server
Summary:        Network Block Device server

%description server
This package contains the %{name} server with  only the null plugin
and no filters.  To install a basic set of plugins and filters you
need to install "nbdkit-basic-plugins", "nbdkit-basic-filters" or
the metapackage "nbdkit".

%package basic-plugins
Summary:        Basic plugins for %{name}
Requires:       %{name}-server = %{version}-%{release}
Provides:       %{name}-data-plugin = %{version}-%{release}
Provides:       %{name}-eval-plugin = %{version}-%{release}
Provides:       %{name}-file-plugin = %{version}-%{release}
Provides:       %{name}-floppy-plugin = %{version}-%{release}
Provides:       %{name}-full-plugin = %{version}-%{release}
Provides:       %{name}-info-plugin = %{version}-%{release}
Provides:       %{name}-memory-plugin = %{version}-%{release}
Provides:       %{name}-ondemand-plugin = %{version}-%{release}
Provides:       %{name}-ones-plugin = %{version}-%{release}
Provides:       %{name}-partitioning-plugin = %{version}-%{release}
Provides:       %{name}-pattern-plugin = %{version}-%{release}
Provides:       %{name}-random-plugin = %{version}-%{release}
Provides:       %{name}-sh-plugin = %{version}-%{release}
Provides:       %{name}-sparse-random-plugin = %{version}-%{release}
Provides:       %{name}-split-plugin = %{version}-%{release}
Provides:       %{name}-zero-plugin = %{version}-%{release}

%description basic-plugins
This package contains plugins for %{name} which depend on a handful of
C libraries: glibc, gnutls, libzstd.  Other plugins for nbdkit with
more complex dependencies are packaged separately.

nbdkit-data-plugin          Serves small amounts of data from the command line.

nbdkit-eval-plugin          Writes a shell script plugin on the command line.

nbdkit-file-plugin          The normal file plugin for serving files.

nbdkit-floppy-plugin        Creates a virtual floppy disk from a directory.

nbdkit-full-plugin          A virtual disk that returns ENOSPC errors.

nbdkit-info-plugin          Serves client and server information.

nbdkit-memory-plugin        A virtual memory plugin.

nbdkit-ondemand-plugin      Creates filesystems on demand.

nbdkit-ones-plugin          Fill disk with repeated 0xff or other bytes.

nbdkit-pattern-plugin       Fixed test pattern.

nbdkit-partitioning-plugin  Creates virtual disks from partitions.

nbdkit-random-plugin        Random content plugin for testing.

nbdkit-sh-plugin            Writes plugins as shell scripts or executables.

nbdkit-sparse-random-plugin Makes sparse random disks.

nbdkit-split-plugin         Concatenates one or more files.

nbdkit-zero-plugin          Zero-length plugin for testing.

%package example-plugins
Summary:        Example plugins for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description example-plugins
This package contains example plugins for %{name}.











# The plugins below have non-trivial dependencies are so are
# packaged separately.
%package cdi-plugin
Summary:        Containerized Data Import plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}
Requires:       jq
Requires:       podman

%description cdi-plugin
This package contains Containerized Data Import support for %{name}.

%package curl-plugin
Summary:        HTTP/FTP (cURL) plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description curl-plugin
This package contains cURL (HTTP/FTP) support for %{name}.










# In theory this is noarch, but because plugins are placed in _libdir
# which varies across architectures, RPM does not allow this.
%package gcs-plugin
Summary:        Gooogle Cloud Storage plugin %{name}
Requires:       %{name}-python-plugin = %{version}-%{release}
Requires:       %{name}-server = %{version}-%{release}
# XXX Should not need to add this.
Requires:       python3-google-cloud-storage

%description gcs-plugin
This package lets you open disk images stored in Google Cloud Storage
using %{name}.

%package guestfs-plugin
Summary:        libguestfs plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description guestfs-plugin
This package is a libguestfs plugin for %{name}.

%package linuxdisk-plugin
Summary:        Virtual Linux disk plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}
# for mke2fs
Requires:       e2fsprogs

%description linuxdisk-plugin
This package is a virtual Linux disk plugin for %{name}.

%package nbd-plugin
Summary:        NBD proxy / forward plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description nbd-plugin
This package lets you forward NBD connections from %{name}
to another NBD server.

%package python-plugin
Summary:        Python 3 plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description python-plugin
This package lets you write Python 3 plugins for %{name}.

%package ssh-plugin
Summary:        SSH plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description ssh-plugin
This package contains SSH support for %{name}.

%package tmpdisk-plugin
Summary:        Remote temporary filesystem disk plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}
# For mkfs and mke2fs (defaults).
Requires:       e2fsprogs
Requires:       util-linux
# For other filesystems.
Suggests:       xfsprogs

%description tmpdisk-plugin
This package is a remote temporary filesystem disk plugin for %{name}.

%package vddk-plugin
Summary:        VMware VDDK plugin for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description vddk-plugin
This package is a plugin for %{name} which connects to
VMware VDDK for accessing VMware disks and servers.

%package basic-filters
Summary:        Basic filters for %{name}
Requires:       %{name}-server = %{version}-%{release}
Provides:       %{name}-blocksize-filter = %{version}-%{release}
Provides:       %{name}-blocksize-policy-filter = %{version}-%{release}
Provides:       %{name}-cache-filter = %{version}-%{release}
Provides:       %{name}-cacheextents-filter = %{version}-%{release}
Provides:       %{name}-checkwrite-filter = %{version}-%{release}
Provides:       %{name}-cow-filter = %{version}-%{release}
Provides:       %{name}-ddrescue-filter = %{version}-%{release}
Provides:       %{name}-delay-filter = %{version}-%{release}
Provides:       %{name}-error-filter = %{version}-%{release}
Provides:       %{name}-evil-filter = %{version}-%{release}
Provides:       %{name}-exitlast-filter = %{version}-%{release}
Provides:       %{name}-exitwhen-filter = %{version}-%{release}
Provides:       %{name}-exportname-filter = %{version}-%{release}
Provides:       %{name}-extentlist-filter = %{version}-%{release}
Provides:       %{name}-fua-filter = %{version}-%{release}
Provides:       %{name}-gzip-filter = %{version}-%{release}
Provides:       %{name}-ip-filter = %{version}-%{release}
Provides:       %{name}-limit-filter = %{version}-%{release}
Provides:       %{name}-log-filter = %{version}-%{release}
Provides:       %{name}-luks-filter = %{version}-%{release}
Provides:       %{name}-multi-conn-filter = %{version}-%{release}
Provides:       %{name}-nocache-filter = %{version}-%{release}
Provides:       %{name}-noextents-filter = %{version}-%{release}
Provides:       %{name}-nofilter-filter = %{version}-%{release}
Provides:       %{name}-noparallel-filter = %{version}-%{release}
Provides:       %{name}-nozero-filter = %{version}-%{release}
Provides:       %{name}-offset-filter = %{version}-%{release}
Provides:       %{name}-partition-filter = %{version}-%{release}
Provides:       %{name}-pause-filter = %{version}-%{release}
Provides:       %{name}-protect-filter = %{version}-%{release}
Provides:       %{name}-rate-filter = %{version}-%{release}
Provides:       %{name}-readahead-filter = %{version}-%{release}
Provides:       %{name}-readonly-filter = %{version}-%{release}
Provides:       %{name}-retry-filter = %{version}-%{release}
Provides:       %{name}-retry-request-filter = %{version}-%{release}
Provides:       %{name}-rotational-filter = %{version}-%{release}
Provides:       %{name}-scan-filter = %{version}-%{release}
Provides:       %{name}-spinning-filter = %{version}-%{release}
Provides:       %{name}-swab-filter = %{version}-%{release}
Provides:       %{name}-time-limit-filter = %{version}-%{release}
Provides:       %{name}-tls-fallback-filter = %{version}-%{release}
Provides:       %{name}-truncate-filter = %{version}-%{release}

%description basic-filters
This package contains filters for %{name} which only depend on simple
C libraries: glibc, gnutls, zlib, and zstd.  Other filters for nbdkit
with more complex dependencies are packaged separately.

nbdkit-blocksize-filter     Adjusts block size of requests sent to plugins.

nbdkit-blocksize-policy-filter  Set block size constraints and policy.

nbdkit-cache-filter         Server-side cache.

nbdkit-cacheextents-filter  Caches extents.

nbdkit-checkwrite-filter    Checks writes match contents of plugin.

nbdkit-cow-filter           Copy-on-write overlay for read-only plugins.

nbdkit-ddrescue-filter      Filter for serving from ddrescue dump.

nbdkit-delay-filter         Injects read and write delays.

nbdkit-error-filter         Injects errors.

nbdkit-evil-filter          Add random data corruption to reads.

nbdkit-exitlast-filter      Exits on last client connection.

nbdkit-exitwhen-filter      Exits gracefully when an event occurs.

nbdkit-exportname-filter    Adjusts export names between client and plugin.

nbdkit-extentlist-filter    Places extent list over a plugin.

nbdkit-fua-filter           Modifies flush behaviour in plugins.

nbdkit-gzip-filter          Decompress a .gz file.

nbdkit-ip-filter            Filters clients by IP address.

nbdkit-limit-filter         Limits the number of clients that can connect concurrently.

nbdkit-log-filter           Logs all transactions to a file.

nbdkit-luks-filter          Read and write LUKS-encrypted disks.

nbdkit-multi-conn-filter    Modifies the way multiple clients can connect to the same export simultaneously.

nbdkit-nocache-filter       Disables cache requests in the underlying plugin.

nbdkit-noextents-filter     Disables extents in the underlying plugin.

nbdkit-nofilter-filter      Passthrough filter.

nbdkit-noparallel-filter    Serializes requests to the underlying plugin.

nbdkit-nozero-filter        Adjusts handling of zero requests by plugins.

nbdkit-offset-filter        Serves an offset and range.

nbdkit-partition-filter     Serves a single partition.

nbdkit-pause-filter         Pauses NBD requests.

nbdkit-protect-filter       Write-protect parts of a plugin.

nbdkit-rate-filter          Limits bandwidth by connection or server.

nbdkit-readahead-filter     Prefetches data when reading sequentially.

nbdkit-readonly-filter      Switch a plugin between read-only and writable.

nbdkit-retry-filter         Reopens connection on error.

nbdkit-retry-request-filter Retries single requests if they fail.

nbdkit-rotational-filter    Set if a plugin is rotational or not.

nbdkit-scan-filter          Prefetch data ahead of sequential reads.

nbdkit-spinning-filter      Add seek delays to simulate a spinning hard disk.

nbdkit-swab-filter          Filter for swapping byte order.

nbdkit-time-limit-filter    Set an overall time limit for each connection.

nbdkit-tls-fallback-filter  TLS protection filter.

nbdkit-truncate-filter      Truncates, expands, rounds up or rounds down size.

%package bzip2-filter
Summary:        BZip2 filter for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description bzip2-filter
This package is a bzip2 filter for %{name}.

%package stats-filter
Summary:        Statistics filter for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description stats-filter
Display statistics about operations.

%package tar-filter
Summary:        Tar archive filter for %{name}
Requires:       %{name}-server = %{version}-%{release}
Requires:       tar

%description tar-filter
This package is a tar archive filter for %{name}.

%package xz-filter
Summary:        XZ and lzip filters for %{name}
Requires:       %{name}-server = %{version}-%{release}

%description xz-filter
This package contains the xz and lzip filters for %{name}.

%package devel
Summary:        Development files and documentation for %{name}
Requires:       %{name}-server = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains development files and documentation
for %{name}.  Install this package if you want to develop
plugins for %{name}.

%package bash-completion
Summary:        Bash tab-completion for %{name}
BuildArch:      noarch
Requires:       %{name}-server = %{version}-%{release}
Requires:       bash-completion >= 2.0

%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.

%prep
%autosetup -p1

%build
autoreconf -fiv

%ifnarch %{complete_test_arches}
# Simplify the test suite so it doesn't require qemu.
sed -i -e 's/^LIBGUESTFS_TESTS/xLIBGUESTFS_TESTS/' tests/Makefile.am
sed -i -e '/^if HAVE_GUESTFISH/,/^endif HAVE_GUESTFISH/d' tests/Makefile.am
autoreconf -i
%endif

# Golang bindings are not enabled in the build since they don't
# need to be.  Most people would use them by copying the upstream
# package into their vendor/ directory.
export PYTHON=$(realink -f %{__python3})
export PATH=/usr/sbin:$PATH
%configure \
    --with-extra='%{name}-%{version}' \
    --disable-static \
    --disable-golang \
    --disable-rust \
    --disable-ocaml \
    --disable-lua \
    --disable-perl \
    --disable-ruby \
    --disable-tcl \
    --disable-torrent \
    --without-ext2 \
    --without-iso \
    --without-libvirt \
%if %{with nbdkit_libguestfs}
    --with-libguestfs \
%else
    --without-libguestfs \
%endif
    %{nil}

# Verify that it picked the correct version of Python
# to avoid RHBZ#1404631 happening again silently.
grep '^PYTHON_VERSION = 3' Makefile

%make_build

%install
%make_install

# Delete libtool crap.
find "%{buildroot}" -name '*.la' -delete

# If cargo happens to be installed on the machine then the
# rust plugin is built.  Delete it if this happens.
rm -f %{buildroot}/%{_mandir}/man3/nbdkit-rust-plugin.3*

# Remove some plugins we cannot --disable.
for f in cc cdi torrent; do
    rm -f %{buildroot}/%{_libdir}/%{name}/plugins/nbdkit-$f-plugin.so
    rm -f %{buildroot}/%{_mandir}/man?/nbdkit-$f-plugin.*
done
rm -f %{buildroot}/%{_libdir}/%{name}/plugins/nbdkit-S3-plugin
rm -f %{buildroot}/%{_mandir}/man1/nbdkit-S3-plugin.1*
rm -f %{buildroot}/%{_libdir}/%{name}/filters/nbdkit-qcow2dec-filter.so
rm -f %{buildroot}/%{_mandir}/man1/nbdkit-qcow2dec-filter.1*

%check
# exit 0
%ifnarch %{broken_test_arches}
# tests/test-captive.sh is racy especially on s390x.  We need to
# rethink this test upstream.
truncate -s 0 tests/test-captive.sh

%ifarch s390x
# Temporarily kill tests/test-cache-max-size.sh since it fails
# sometimes on s390x for unclear reasons.
truncate -s 0 tests/test-cache-max-size.sh
%endif

# Temporarily kill test-nbd-tls.sh and test-nbd-tls-psk.sh
# https://www.redhat.com/archives/libguestfs/2020-March/msg00191.html
truncate -s 0 tests/test-nbd-tls.sh tests/test-nbd-tls-psk.sh

# Make sure we can see the debug messages (RHBZ#1230160).
export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1
export PATH=/usr/sbin:$PATH

%make_build check || {
    cat tests/test-suite.log
    exit 1
  }
%endif

%files
# metapackage so empty

%files server
%doc README.md
%license LICENSE
%{_sbindir}/nbdkit
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/nbdkit-null-plugin.so
%dir %{_libdir}/%{name}/filters
%{_mandir}/man1/nbdkit.1*
%{_mandir}/man1/nbdkit-captive.1*
%{_mandir}/man1/nbdkit-client.1*
%{_mandir}/man1/nbdkit-loop.1*
%{_mandir}/man1/nbdkit-null-plugin.1*
%{_mandir}/man1/nbdkit-probing.1*
%{_mandir}/man1/nbdkit-protocol.1*
%{_mandir}/man1/nbdkit-service.1*
%{_mandir}/man1/nbdkit-security.1*
%{_mandir}/man1/nbdkit-tls.1*

%files basic-plugins
%doc README.md
%license LICENSE
%{_libdir}/%{name}/plugins/nbdkit-data-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-eval-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-file-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-floppy-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-full-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-info-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-memory-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-ondemand-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-ones-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-partitioning-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-pattern-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-random-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-sh-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-sparse-random-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-split-plugin.so
%{_libdir}/%{name}/plugins/nbdkit-zero-plugin.so
%{_mandir}/man1/nbdkit-data-plugin.1*
%{_mandir}/man1/nbdkit-eval-plugin.1*
%{_mandir}/man1/nbdkit-file-plugin.1*
%{_mandir}/man1/nbdkit-floppy-plugin.1*
%{_mandir}/man1/nbdkit-full-plugin.1*
%{_mandir}/man1/nbdkit-info-plugin.1*
%{_mandir}/man1/nbdkit-memory-plugin.1*
%{_mandir}/man1/nbdkit-ondemand-plugin.1*
%{_mandir}/man1/nbdkit-ones-plugin.1*
%{_mandir}/man1/nbdkit-partitioning-plugin.1*
%{_mandir}/man1/nbdkit-pattern-plugin.1*
%{_mandir}/man1/nbdkit-random-plugin.1*
%{_mandir}/man3/nbdkit-sh-plugin.3*
%{_mandir}/man1/nbdkit-sparse-random-plugin.1*
%{_mandir}/man1/nbdkit-split-plugin.1*
%{_mandir}/man1/nbdkit-zero-plugin.1*

%files example-plugins
%{_libdir}/%{name}/plugins/nbdkit-example*-plugin.so
%{_mandir}/man1/nbdkit-example*-plugin.1*

%files curl-plugin
%{_libdir}/%{name}/plugins/nbdkit-curl-plugin.so
%{_mandir}/man1/nbdkit-curl-plugin.1*

%files gcs-plugin
%{_libdir}/%{name}/plugins/nbdkit-gcs-plugin
%{_mandir}/man1/nbdkit-gcs-plugin.1*

%if %{with nbdkit_libguestfs}
%files guestfs-plugin
%{_libdir}/%{name}/plugins/nbdkit-guestfs-plugin.so
%{_mandir}/man1/nbdkit-guestfs-plugin.1*
%endif

%files linuxdisk-plugin
%{_libdir}/%{name}/plugins/nbdkit-linuxdisk-plugin.so
%{_mandir}/man1/nbdkit-linuxdisk-plugin.1*

%files nbd-plugin
%{_libdir}/%{name}/plugins/nbdkit-nbd-plugin.so
%{_mandir}/man1/nbdkit-nbd-plugin.1*

%files python-plugin
%{_libdir}/%{name}/plugins/nbdkit-python-plugin.so
%{_mandir}/man3/nbdkit-python-plugin.3*

%files ssh-plugin
%{_libdir}/%{name}/plugins/nbdkit-ssh-plugin.so
%{_mandir}/man1/nbdkit-ssh-plugin.1*

%files tmpdisk-plugin
%{_libdir}/%{name}/plugins/nbdkit-tmpdisk-plugin.so
%{_mandir}/man1/nbdkit-tmpdisk-plugin.1*

%ifarch x86_64
%files vddk-plugin
%{_libdir}/%{name}/plugins/nbdkit-vddk-plugin.so
%{_mandir}/man1/nbdkit-vddk-plugin.1*
%endif

%files basic-filters
%{_libdir}/%{name}/filters/nbdkit-blocksize-filter.so
%{_libdir}/%{name}/filters/nbdkit-blocksize-policy-filter.so
%{_libdir}/%{name}/filters/nbdkit-cache-filter.so
%{_libdir}/%{name}/filters/nbdkit-cacheextents-filter.so
%{_libdir}/%{name}/filters/nbdkit-checkwrite-filter.so
%{_libdir}/%{name}/filters/nbdkit-cow-filter.so
%{_libdir}/%{name}/filters/nbdkit-ddrescue-filter.so
%{_libdir}/%{name}/filters/nbdkit-delay-filter.so
%{_libdir}/%{name}/filters/nbdkit-error-filter.so
%{_libdir}/%{name}/filters/nbdkit-evil-filter.so
%{_libdir}/%{name}/filters/nbdkit-exitlast-filter.so
%{_libdir}/%{name}/filters/nbdkit-exitwhen-filter.so
%{_libdir}/%{name}/filters/nbdkit-exportname-filter.so
%{_libdir}/%{name}/filters/nbdkit-extentlist-filter.so
%{_libdir}/%{name}/filters/nbdkit-fua-filter.so
%{_libdir}/%{name}/filters/nbdkit-gzip-filter.so
%{_libdir}/%{name}/filters/nbdkit-ip-filter.so
%{_libdir}/%{name}/filters/nbdkit-limit-filter.so
%{_libdir}/%{name}/filters/nbdkit-log-filter.so
%{_libdir}/%{name}/filters/nbdkit-luks-filter.so
%{_libdir}/%{name}/filters/nbdkit-multi-conn-filter.so
%{_libdir}/%{name}/filters/nbdkit-nocache-filter.so
%{_libdir}/%{name}/filters/nbdkit-noextents-filter.so
%{_libdir}/%{name}/filters/nbdkit-nofilter-filter.so
%{_libdir}/%{name}/filters/nbdkit-noparallel-filter.so
%{_libdir}/%{name}/filters/nbdkit-nozero-filter.so
%{_libdir}/%{name}/filters/nbdkit-offset-filter.so
%{_libdir}/%{name}/filters/nbdkit-openonce-filter.so
%{_libdir}/%{name}/filters/nbdkit-partition-filter.so
%{_libdir}/%{name}/filters/nbdkit-pause-filter.so
%{_libdir}/%{name}/filters/nbdkit-protect-filter.so
%{_libdir}/%{name}/filters/nbdkit-rate-filter.so
%{_libdir}/%{name}/filters/nbdkit-readahead-filter.so
%{_libdir}/%{name}/filters/nbdkit-readonly-filter.so
%{_libdir}/%{name}/filters/nbdkit-retry-filter.so
%{_libdir}/%{name}/filters/nbdkit-retry-request-filter.so
%{_libdir}/%{name}/filters/nbdkit-rotational-filter.so
%{_libdir}/%{name}/filters/nbdkit-scan-filter.so
%{_libdir}/%{name}/filters/nbdkit-spinning-filter.so
%{_libdir}/%{name}/filters/nbdkit-swab-filter.so
%{_libdir}/%{name}/filters/nbdkit-time-limit-filter.so
%{_libdir}/%{name}/filters/nbdkit-tls-fallback-filter.so
%{_libdir}/%{name}/filters/nbdkit-truncate-filter.so
%{_mandir}/man1/nbdkit-blocksize-filter.1*
%{_mandir}/man1/nbdkit-blocksize-policy-filter.1*
%{_mandir}/man1/nbdkit-cache-filter.1*
%{_mandir}/man1/nbdkit-cacheextents-filter.1*
%{_mandir}/man1/nbdkit-checkwrite-filter.1*
%{_mandir}/man1/nbdkit-cow-filter.1*
%{_mandir}/man1/nbdkit-ddrescue-filter.1*
%{_mandir}/man1/nbdkit-delay-filter.1*
%{_mandir}/man1/nbdkit-error-filter.1*
%{_mandir}/man1/nbdkit-evil-filter.1*
%{_mandir}/man1/nbdkit-exitlast-filter.1*
%{_mandir}/man1/nbdkit-exitwhen-filter.1*
%{_mandir}/man1/nbdkit-exportname-filter.1*
%{_mandir}/man1/nbdkit-extentlist-filter.1*
%{_mandir}/man1/nbdkit-fua-filter.1*
%{_mandir}/man1/nbdkit-gzip-filter.1*
%{_mandir}/man1/nbdkit-ip-filter.1*
%{_mandir}/man1/nbdkit-limit-filter.1*
%{_mandir}/man1/nbdkit-log-filter.1*
%{_mandir}/man1/nbdkit-luks-filter.1*
%{_mandir}/man1/nbdkit-multi-conn-filter.1*
%{_mandir}/man1/nbdkit-nocache-filter.1*
%{_mandir}/man1/nbdkit-noextents-filter.1*
%{_mandir}/man1/nbdkit-nofilter-filter.1*
%{_mandir}/man1/nbdkit-noparallel-filter.1*
%{_mandir}/man1/nbdkit-nozero-filter.1*
%{_mandir}/man1/nbdkit-offset-filter.1*
%{_mandir}/man1/nbdkit-openonce-filter.1*
%{_mandir}/man1/nbdkit-partition-filter.1*
%{_mandir}/man1/nbdkit-pause-filter.1*
%{_mandir}/man1/nbdkit-protect-filter.1*
%{_mandir}/man1/nbdkit-rate-filter.1*
%{_mandir}/man1/nbdkit-readahead-filter.1*
%{_mandir}/man1/nbdkit-readonly-filter.1*
%{_mandir}/man1/nbdkit-retry-filter.1*
%{_mandir}/man1/nbdkit-retry-request-filter.1*
%{_mandir}/man1/nbdkit-rotational-filter.1*
%{_mandir}/man1/nbdkit-scan-filter.1*
%{_mandir}/man1/nbdkit-spinning-filter.1*
%{_mandir}/man1/nbdkit-swab-filter.1*
%{_mandir}/man1/nbdkit-time-limit-filter.1*
%{_mandir}/man1/nbdkit-tls-fallback-filter.1*
%{_mandir}/man1/nbdkit-truncate-filter.1*

%files bzip2-filter
%{_libdir}/%{name}/filters/nbdkit-bzip2-filter.so
%{_mandir}/man1/nbdkit-bzip2-filter.1*

%files stats-filter
%{_libdir}/%{name}/filters/nbdkit-stats-filter.so
%{_mandir}/man1/nbdkit-stats-filter.1*

%files tar-filter
%{_libdir}/%{name}/filters/nbdkit-tar-filter.so
%{_mandir}/man1/nbdkit-tar-filter.1*

%files xz-filter
%{_libdir}/%{name}/filters/nbdkit-lzip-filter.so
%{_libdir}/%{name}/filters/nbdkit-xz-filter.so
%{_mandir}/man1/nbdkit-lzip-filter.1*
%{_mandir}/man1/nbdkit-xz-filter.1*

%files devel
%{_includedir}/nbdkit-common.h
%{_includedir}/nbdkit-filter.h
%{_includedir}/nbdkit-plugin.h
%{_includedir}/nbdkit-version.h
%{_includedir}/nbd-protocol.h
%{_mandir}/man3/nbdkit-filter.3*
%{_mandir}/man3/nbdkit-plugin.3*
%{_mandir}/man3/nbdkit-tracing.3*
%{_mandir}/man3/nbdkit_*.3*
%{_mandir}/man1/nbdkit-release-notes-1.*.1*
%{_libdir}/pkgconfig/nbdkit.pc

%files bash-completion
%{_datadir}/bash-completion

%changelog
