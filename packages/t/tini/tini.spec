#
# spec file for package tini
#
# Copyright (c) 2025 SUSE LLC
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


Name:           tini
Version:        0.19.0
Release:        0
Summary:        A tiny but valid init for containers
License:        MIT
URL:            https://github.com/krallin/tini
Source:         %{URL}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  glibc-devel-static

%description
Tini is a trivial implementation for an "init" program.

All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit, all the while reaping zombies and performing signal forwarding.

libc will be needed inside the container.

%package static
Summary:        A tiny but valid init for containers, with libc linked statically

%description static
Tini is a trivial implementation for an "init" program.

All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit, all the while reaping zombies and performing signal forwarding.

This variant is statically linked to libc so that it will not be
needed inside the container.

%prep
%autosetup

%build
# Subreaper requires kernel >= 3.4
%set_build_flags
CFLAGS="${CFLAGS-} -DPR_SET_CHILD_SUBREAPER=36 -DPR_GET_CHILD_SUBREAPER=37"
export CFLAGS

# Enable DMINIMAL to supress verbosity or any output at all, plus disable
# argument parsing. You an still set some options via env vars
# CMAKE_ARGS="-DMINIMAL=ON"
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 .
%make_build tini
%make_build tini-static

%install
mkdir -p %{buildroot}/%{_sbindir}
cp build/tini %{buildroot}/%{_sbindir}/tini
cp build/tini-static %{buildroot}/%{_sbindir}/tini-static

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_sbindir}/tini

%files static
%{_sbindir}/tini-static
%license LICENSE
%doc README.md

%changelog
