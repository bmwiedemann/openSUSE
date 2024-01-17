#
# spec file for package libpulp
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


Name:           libpulp
Version:        0.3.1
Release:        0
Summary:        Userspace live patching library and tools
License:        LGPL-2.1-only
Group:          Productivity/Security
URL:            https://github.com/suse/libpulp
Source0:        %{name}-%{version}.tar.gz
Source1:        rpm-helper
Source2:        macros.userspace-livepatch
Source99:       libpulp.rpmlintrc
# Required to hardlink identical files.
BuildRequires:  fdupes
# Required to run the tests.
BuildRequires:  gcc-c++
# Required to build the tools, which are needed to run the tests.
BuildRequires:  libjson-c-devel
BuildRequires:  libelf-devel
BuildRequires:  python3-pexpect
BuildRequires:  python3-psutil
BuildRequires:  libseccomp-devel
# Only available for these architectures.
ExclusiveArch:  x86_64

%description
Library and tools for user space live patching.

%package -n libpulp0
Summary:        User space live patching library
Group:          System/Libraries

%description -n libpulp0
Libpulp is a library (and a framework) that enables live patching of
user space libraries.

This package contains the runtime files.

%package tools
Summary:        User space live patching tools
Group:          System/Management

%description tools
This package contains the tools to apply user-space live patches.

# Disable LTO for libpulp, as it is currently not supported.
%define _lto_cflags %{nil}

%prep
%autosetup -p1

%build
%configure
%make_build

%check
%make_build check

%install
%make_install
install -D -m0755 %{SOURCE1} %{buildroot}%{_prefix}/lib/userspace-livepatch/rpm-helper
install -D -m0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/rpm/macros.d/macros.userspace-livepatch

# Convert identical files into hardlinks.
%fdupes %{buildroot}/%{_prefix}
# Remove .la and .so files.  libpulp.so is not supposed to be linked
# against any programs or libraries, but LD_PRELOAD'ed, so do not
# distribute it, not even in the devel package.
find %{buildroot}/%{_prefix} -name libpulp.la -delete
find %{buildroot}/%{_prefix} -name libpulp.so -delete

%post -n libpulp0 -p /sbin/ldconfig
%postun -n libpulp0 -p /sbin/ldconfig

%files -n libpulp0
%{_libdir}/lib*.so.*
%doc README.md
%license LICENSE

%files tools
%{_bindir}/*
%{_mandir}/*/*
%dir %{_prefix}/lib/userspace-livepatch
%{_prefix}/lib/userspace-livepatch/*
%{_prefix}/lib/rpm/*
%license LICENSE

%changelog
