#
# spec file for package tini
#
# Copyright (c) 2020 SUSE LLC
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
Group:          System/Management
URL:            https://github.com/krallin/tini
Source:         https://github.com/krallin/tini/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
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
Group:          System/Management

%description static
Tini is a trivial implementation for an "init" program.

All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit, all the while reaping zombies and performing signal forwarding.

This variant is statically linked to libc so that it will not be
needed inside the container.

%prep
%setup -q

%build
# Subreaper requires kernel >= 3.4
CFLAGS="${CFLAGS-} -DPR_SET_CHILD_SUBREAPER=36 -DPR_GET_CHILD_SUBREAPER=37"
export CFLAGS

# Enable DMINIMAL to supress verbosity or any output at all, plus disable
# argument parsing. You an still set some options via env vars
# CMAKE_ARGS="-DMINIMAL=ON"
cmake "$CMAKE_ARGS"
make tini %{?_smp_mflags} $LDFLAGS
make tini-static %{?_smp_mflags} $LDFLAGS

%install
mkdir -p %{buildroot}/%{_bindir}
cp tini %{buildroot}/tini
cp tini-static %{buildroot}/tini-static

%files
%license LICENSE
%doc README.md
/tini

%files static
/tini-static

%changelog
