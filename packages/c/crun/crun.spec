#
# spec file for package crun
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


Summary:        OCI runtime written in C
License:        GPL-2.0-or-later
Name:           crun
Version:        0.21
Release:        0
Source0:        https://github.com/containers/crun/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        crun-rpmlintrc
URL:            https://github.com/containers/crun
# We always run autogen.sh
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glibc-devel-static
BuildRequires:  go-md2man
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libyajl-devel
BuildRequires:  python
BuildRequires:  python3-libmount
BuildRequires:  systemd-devel
%ifnarch %ix86
BuildRequires:  criu-devel >= 3.15
%endif
%ifarch x86_64 aarch64
BuildRequires:  libkrun >= 0.1.4
Requires:       libkrun >= 0.1.7
%endif

%description
crun is a runtime for running OCI containers. It is built with libkrun support

%prep
%autosetup -p1

%build
%ifarch x86_64 aarch64
export LIBKRUN="--with-libkrun"
%endif
./autogen.sh
%configure --disable-silent-rules $LIBKRUN CFLAGS='-I /usr/include/libseccomp'
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/lib*
%ifarch x86_64 aarch64
# allow easy krun usage with podman
ln -s %{_bindir}/crun %{buildroot}%{_bindir}/krun
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc README.md
%doc SECURITY.md
%{_bindir}/%{name}
%ifarch x86_64 aarch64
%{_bindir}/krun
%endif
%{_mandir}/man1/*

%changelog
