#
# spec file for package tini
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:            tini
Version:         0.18.0
Release:         0
License:         MIT
Summary:         A tiny but valid init for containers
Url:             https://github.com/krallin/tini
Group:           System/Management
Source:          tini-%{version}.tar.xz
BuildRoot:       %{_tmppath}/%{name}-%{version}-build
BuildRequires:   cmake
BuildRequires:   gcc
BuildRequires:   glibc-devel
BuildRequires:   glibc-devel-static


%description
Tini is a trivial implementation for an "init" program.

All Tini does is spawn a single child (Tini is meant to be run in a container),
and wait for it to exit, all the while reaping zombies and performing signal forwarding.

libc will be needed inside the container.

%package static
Summary:         A tiny but valid init for containers, with libc linked statically

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
%defattr(-,root,root)
%doc README.md LICENSE
/tini

%files static
/tini-static
