#
# spec file for package jsdec
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
# Copyright (c) 2026 Eyad Issa <eyadlorenzo@gmail.com>
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

%global quickjs_version 0.8.0

%global rizin_plugindir  %{_libdir}/rizin/plugins
%global cutter_plugindir %{_datadir}/rizin/cutter/plugins

%global cutter_native_plugindir %{cutter_plugindir}/native

%global base_builddir   %{_vpath_builddir}
%global rizin_builddir  %{base_builddir}-rizin
%global cutter_builddir %{base_builddir}-cutter

Name:           jsdec
Version:        0.9.0
Release:        0
Summary:        Simple decompiler for Rizin
License:        BSD-3-Clause AND MIT
URL:            https://github.com/rizinorg/jsdec
Source0:        https://github.com/rizinorg/jsdec/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/quickjs-ng/quickjs/archive/v%{quickjs_version}/quickjs-%{quickjs_version}.tar.gz
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  rizin-devel
BuildRequires:  rz-cutter-devel
BuildRequires:  cmake
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-svg-devel
Requires:       rizin

%description
Simple decompiler for Rizin.
Converts asm to pseudo-C code.

%package cutter
Summary:        Jsdec plugin for Cutter
Requires:       rz-cutter

%description cutter
Jsdec plugin for Cutter.
Converts asm to pseudo-C code.

%prep
%autosetup
mkdir -p ./subprojects/libquickjs
tar -xf %{SOURCE1} -C ./subprojects/libquickjs --strip-components=1

%build
# apply meson patches to subprojects
meson subprojects packagefiles --apply

# configure and build for rizin
%global _vpath_builddir %{rizin_builddir}
%meson -Dbuild_type=rizin -Drizin_plugdir=%{rizin_plugindir}
%meson_build

# configure and build for cutter
%global _vpath_builddir %{cutter_builddir}
%meson -Dbuild_type=cutter
%meson_build
cd cutter-plugin
%cmake \
    -DCUTTER_INSTALL_PLUGDIR=%{cutter_native_plugindir} \
    -DJSDEC_BUILD_DIR=../%{cutter_builddir}
%cmake_build

%install
%global _vpath_builddir %{rizin_builddir}
%meson_install
cd cutter-plugin
%cmake_install

%files
%license LICENSES/*
%doc README.md
%{rizin_plugindir}/libcore_pdd.so

%files cutter
%license LICENSES/*
%dir %{cutter_plugindir}
%dir %{cutter_native_plugindir}
%{cutter_native_plugindir}/libjsdec_cutter.so

%changelog
