#
# spec file for package libnbd
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 0

Name:           libnbd
Version:        1.7.7
Release:        0
Summary:        NBD client library in userspace
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/nbdkit/libnbd
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  ocaml(compiler)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls) >= 3.3.0
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       libnbd%{sover} = %{version}
# Only for running the test suite.
BuildRequires:  gcc-c++
BuildRequires:  jq
%if 0%{?suse_version} >= 1550
BuildRequires:  nbd
%endif
BuildRequires:  qemu-tools

%description
NBD — Network Block Device — is a protocol for accessing Block Devices
(hard disks and disk-like things) over a Network.

This is the NBD client library in userspace, a simple library for
writing NBD clients.

The key features are:

 * Synchronous and asynchronous APIs, both for ease of use and for
   writing non-blocking, multithreaded clients.

 * High performance.

 * Minimal dependencies for the basic library.

 * Well-documented, stable API.

 * Bindings in several programming languages.

%package -n libnbd%{sover}
Summary:        Core library for nbd

%description -n libnbd%{sover}
This is the NBD client library in userspace, a simple library for
writing NBD clients.

%package devel
Summary:        Development headers for %{name}
Requires:       libnbd%{sover} = %{version}-%{release}

%description devel
This package contains development headers for %{name}.

%package -n nbdfuse
Summary:        FUSE support for %{name}
Requires:       libnbd%{sover} = %{version}-%{release}

%description -n nbdfuse
This package contains FUSE support for %{name}.

%package bash-completion
Summary:        Bash tab-completion for %{name}
BuildArch:      noarch
Requires:       bash-completion >= 2.0
Requires:       libnbd%{sover} = %{version}-%{release}

%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
    --with-tls-priority=@LIBNBD,SYSTEM \
    --enable-fuse \
    --disable-golang \
    --disable-python \
    --disable-static

%make_build

%install
%make_install
%fdupes %{buildroot}
# Delete libtool crap.
find "%{buildroot}" -name '*.la' -delete

# Delete the golang man page since we're not distributing the bindings.
rm %{buildroot}/%{_mandir}/man3/libnbd-golang.3*

# Delete the ocaml man page. 'make install' should be fixed to not install it when ocaml is disabled
rm %{buildroot}/%{_mandir}/man3/libnbd-ocaml.3*

%check
# All fuse tests fail in Koji with:
# fusermount: entry for fuse/test-*.d not found in /etc/mtab
# for unknown reasons but probably related to the Koji environment.
for f in fuse/test-*.sh; do
    rm $f
    touch $f
    chmod +x $f
done

%make_build check || {
    for f in $(find . -name test-suite.log); do
        echo
        echo "==== $f ===="
        cat $f
    done
  }

%post   -n libnbd%{sover} -p /sbin/ldconfig
%postun -n libnbd%{sover} -p /sbin/ldconfig

%files
%doc README
%{_bindir}/nbdcopy
%{_bindir}/nbdinfo
%{_mandir}/man1/nbdcopy.1*
%{_mandir}/man1/nbdinfo.1*

%files -n libnbd%{sover}
%license COPYING.LIB
%{_libdir}/libnbd.so.%{sover}
%{_libdir}/libnbd.so.%{sover}.*

%files devel
%{_includedir}/libnbd.h
%{_libdir}/libnbd.so
%{_libdir}/pkgconfig/libnbd.pc
%{_mandir}/man3/libnbd.3*
%{_mandir}/man1/libnbd-release-notes-1.*.1*
%{_mandir}/man3/libnbd-security.3*
%{_mandir}/man3/nbd_*.3*

%files -n nbdfuse
%{_bindir}/nbdfuse
%{_mandir}/man1/nbdfuse.1*

%files bash-completion
%{_datadir}/bash-completion

%changelog
