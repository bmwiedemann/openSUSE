#
# spec file for package libdnf-plugin-txnupd
#
# Copyright (c) 2021 Neal Gompa <ngompa13@gmail.com>.
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


Name:           libdnf-plugin-txnupd
Version:        0.1.3
Release:        0
Summary:        Plugin for libdnf to implement transactional updates
License:        LGPL-2.1-or-later
URL:            https://code.opensuse.org/microos/libdnf-plugin-txnupd
# TODO: Use once releases are enabled on code.o.o
#Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  meson

# We need at least GCC 10
%if 0%{?suse_version} && 0%{?suse_version} < 1550
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++ >= 10
%endif

BuildRequires:  pkgconfig(libdnf) >= 0.60
BuildRequires:  pkgconfig(tukit) >= 3.1.2

# To keep OBS and rpmlint from complaining about directory ownership
BuildRequires:  dnf-data

# Do not permit normal DNF snapper plugin on the same system
Conflicts:      dnf-plugin-snapper

# We need the transactional update dracut module
Requires:       dracut-transactional-update

# Either MicroDNF or PackageKit can be used as frontends
Requires:       (microdnf or PackageKit)
# This is intended to be used with PackageKit using DNF
Requires:       (PackageKit-backend-dnf if PackageKit)
# To ensure directories for configuration files are in place
Requires:       dnf-data

# Stricter dependency to keep things sane
%requires_ge %(rpm -qf "$(readlink -f %{_libdir}/libdnf.so)")
%requires_ge %(rpm -qf "$(readlink -f %{_libdir}/libtukit.so)")

%description
This package contains the plugin to implement transactional updates
as a libdnf plugin. This plugin hooks into the DNF "context" for
Micro DNF and PackageKit to enable this functionality in normal use.


%prep
%autosetup -p1


%build
%if 0%{?suse_version} && 0%{?suse_version} < 1550
# Where GCC 10 is the alternate compiler, use that
export CC=gcc-10
export CXX=g++-10
%endif

%meson
%meson_build


%install
%meson_install

# Add configuration to mark this package as protected by libdnf
mkdir -p %{buildroot}%{_sysconfdir}/dnf/protected.d
echo "%{name}" > %{buildroot}%{_sysconfdir}/dnf/protected.d/txnupd.conf


%files
%license LICENSE
%doc README.md
%{_libdir}/libdnf/plugins/txnupd.so
%{_sysconfdir}/dnf/protected.d/txnupd.conf


%changelog
