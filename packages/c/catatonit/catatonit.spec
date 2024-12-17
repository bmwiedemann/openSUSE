#
# spec file for package catatonit
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


Name:           catatonit
Version:        0.2.1
Release:        0
Summary:        A signal-forwarding process manager for containers
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/openSUSE/catatonit
Source0:        https://github.com/openSUSE/catatonit/releases/download/v%{version}/%{name}.tar.xz#/%{name}-%{version}.tar.xz
Source1:        https://github.com/openSUSE/catatonit/releases/download/v%{version}/%{name}.tar.xz.asc#/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  file
BuildRequires:  gcc
BuildRequires:  glibc-devel-static
BuildRequires:  libtool

%description
Catatonit is a /sbin/init program for use within containers. It
forwards (almost) all signals to the spawned child, tears down
the container when the spawned child exits, and otherwise
cleans up other exited processes (zombies).

This is a reimplementation of other container init programs (such as
"tini" or "dumb-init"), but uses modern Linux facilities (such as
signalfd(2)) and has no additional features.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

# Make sure we *always* build a static binary. Otherwise we'll break containers
# that don't have the necessary shared libs.
file ./%{name} | grep 'statically linked'

%install
%make_install
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/docker-init

%files
%defattr(-,root,root)
%doc README.md
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%{_bindir}/%{name}
%{_bindir}/docker-init

%changelog
