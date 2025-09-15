# spec file for package gamescope-shaders
#
# Copyright (c) 2025 SUSE LLC
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

Name:           gamescope-shaders
Version:        0.1+git2.64d7a05
Release:        0%{?dist}
Summary:        Reshade shaders packaged with Gamescope

License:        GPL-3.0
URL:            https://github.com/misyltoad/GamescopeShaders
Source:        	GamescopeShaders-%{version}.tar.xz
BuildArch:      noarch

Requires:       gamescope
BuildRequires:  gamescope
BuildRequires:  systemd-rpm-macros
Provides:       GamescopeShaders = %{version}

%description
This package provides reshade shaders packaged with Gamescope.

# Disable debug packages
%define debug_package %{nil}

%prep
%setup -T -b 0 -q -n GamescopeShaders-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/gamescope/reshade/Shaders
cp -rv Shaders/* %{buildroot}%{_datadir}/gamescope/reshade/Shaders
mkdir -p %{buildroot}%{_datadir}/gamescope/reshade/Textures
cp -rv Textures/* %{buildroot}%{_datadir}/gamescope/reshade/Textures

%pre

%post

%files
%license LICENSE_Lilium
%dir %{_datadir}/gamescope/reshade
%dir %{_datadir}/gamescope/reshade/Shaders
%dir %{_datadir}/gamescope/reshade/Textures
%{_datadir}/gamescope/reshade/Shaders/*
%{_datadir}/gamescope/reshade/Textures/*

%changelog
