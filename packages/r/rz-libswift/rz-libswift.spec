#
# spec file for package jsdec
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Eyad Issa <eyadlorenzo@gmail.com>
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


%define rizin_plugindir %{_libdir}/rizin/plugins

Name:           rz-libswift
Version:        0.8.0
Release:        0
Summary:        Swift Demangling library for Rizin
License:        Apache-2.0 AND LGPL-3.0-only
URL:            https://github.com/rizinorg/rz-libswift
Source:         https://github.com/rizinorg/rz-libswift/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  rizin-devel
Requires:       rizin

%description
Swift demangler for RizinOrg, taken from Apple source code.

%prep
%autosetup

%build
%meson -Drizin_plugdir=%{rizin_plugindir}
%meson_build

%install
%meson_install

%files
%license LICENSES/*
%doc README.md
%{rizin_plugindir}/libswift.so

%changelog
