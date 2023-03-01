#
# spec file for package lxcfs
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


# On pre-15 SLE versions, _sharedstatedir was /usr/com -- which is just wrong.
%if 0%{?suse_version} < 1500
%define _sharedstatedir /var/lib
%endif

Name:           lxcfs
Version:        5.0.2
Release:        0
Summary:        FUSE filesystem for LXC
License:        Apache-2.0
Group:          System/Management
URL:            https://linuxcontainers.org/lxcfs
Source:         https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz
Source1:        https://linuxcontainers.org/downloads/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  meson >= 0.50
BuildRequires:  pam-devel
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  python3-Jinja2
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

%description
LXCFS is a small FUSE filesystem written with the intention of making Linux
containers feel more like a virtual machine. It started as a side-project of
LXC but is usable by any runtime.

%package hooks-lxc
Summary:        LXC hooks for %{name}
Group:          System/Management
Requires:       %{name} = %{version}
%if 0%{?sle_version} < 150000
Supplements:    packageand(%{name}:liblxc1)
%else
Supplements:    (%{name} and liblxc1)
%endif
BuildArch:      noarch

%description hooks-lxc
Configuration to add hooks for %{name} so that it automatically interoperates
with LXC for all containers.

%prep
%autosetup -p1

%build
%meson \
	-D init-script=systemd \
	-D runtime-path=%{_rundir} \
	%{nil}
%meson_build

%install
# The shared library liblxcfs.so used by lxcfs is not supposed to be used by
# any other program. lxcfs will automatically install it to {_libdir}/{name}
# which is out of the way of any other users.
%meson_install
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}

# systemd service and sysv-init compat wrapper.
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# Clean up.
find %{buildroot} -type f -name '*.la' -delete
%fdupes %{buildroot}

%pre
%service_add_pre lxcfs.service

%post
%service_add_post lxcfs.service

%preun
%service_del_preun lxcfs.service

%postun
%service_del_postun lxcfs.service

%files
%defattr(-,root,root)
%doc AUTHORS README*
%license COPYING
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_unitdir}/*

# Mountpoint for lxcfs.
%dir %{_sharedstatedir}/%{name}

# The lxcfs executable requires liblxcfs.so be installed. It calls dlopen() to
# dynamically reload the shared library on upgrade. This is important. Do *not*
# split into a separate package and do not turn this into a versioned shared
# library! (This shared library allows lxcfs to be updated without having to
# restart it which is good when you have important system containers running!)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/liblxcfs.so

%files hooks-lxc
%defattr(-,root,root)
%{_datadir}/lxc

%changelog
