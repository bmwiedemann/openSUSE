#
# spec file for package jsdec
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
# Copyright (c) 2025, Eyad Issa <eyadlorenzo@gmail.com>
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
%define quickjs_version 1682540214.c81f05c

Name:           jsdec
Version:        0.7.0
Release:        0
Summary:        Simple decompiler for Rizin
License:        BSD-3-Clause AND MIT
URL:            https://github.com/rizinorg/jsdec
Source0:        %{name}-%{version}.tar.gz
Source1:        quickjs-%{quickjs_version}.tar.gz
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  rizin-devel
Requires:       rizin

%description
Simple decompiler for Rizin.
Converts asm to pseudo-C code.

%prep
%autosetup
pushd subprojects || exit 1
mkdir libquickjs
tar -xf %{SOURCE1} -C libquickjs --strip-components=1
popd || exit 1

%build
meson subprojects packagefiles --apply
%meson -Drizin_plugdir=%{rizin_plugindir}
%meson_build

%install
%meson_install

%files
%license LICENSES/*
%doc README.md
%{rizin_plugindir}/libcore_pdd.so

%changelog
