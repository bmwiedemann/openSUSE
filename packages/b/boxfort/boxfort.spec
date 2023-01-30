#
# spec file for package boxfort 
#
# Copyright (c) 2023 SUSE LLC
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

%define _lto_cflags %{nil}

Name:           boxfort
Version:        0.1.4
Release:        0
Summary:        A sandboxing C library for Criterion
License:        MIT
URL:            https://github.com/Snaipe/BoxFort
Source:         https://github.com/Snaipe/BoxFort/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  meson

%description
BoxFort provides an API to run user code in isolated processes.

Although BoxFort provides some kind of security of the parent process
against spawned sandboxes, a sandbox has by default the same system
permissions and access than its parent, and is hence, without care,
ill-fitted for security purposes.

The goal of this project is portable code isolation (not security).
For complete system isolation, consider using containers.

%package devel
Summary:        Development files for boxfort
Requires:       %{name} = %{version}

%description devel
Development files for boxfort.

%prep
%autosetup -p1 -n BoxFort-%{version}

%build
%meson
%meson_build

%install
%meson_install
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true

%files
%license LICENSE 
%doc README.md

%files devel
%{_includedir}/boxfort.h
%{_libdir}/lib%{name}.a
%{_libdir}/pkgconfig/boxfort.pc

%changelog
