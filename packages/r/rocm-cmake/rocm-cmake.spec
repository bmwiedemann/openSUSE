#
# spec file for package rocm-cmake
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


%global debug_package %{nil}

%global rocm_release 6.4
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocm-cmake
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        CMake modules for common build and development tasks for ROCm
License:        MIT
URL:            https://github.com/ROCm/rocm-cmake
Source:         %{url}/archive/rocm-%{version}.tar.gz#/rocm-cmake-rocm-%{version}.tar.gz
# https://github.com/ROCm/rocm-cmake/issues/276
Patch0:         0001-rocm-cmake-follow-cmake-install-rules.patch

BuildArch:      noarch
BuildRequires:  cmake
Requires:       cmake

%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.

%prep
%autosetup -p1 -n rocm-cmake-rocm-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocm-cmake/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocm-cmake/LICENSE
fi

%files
%dir %{_datadir}/rocm
%dir %{_datadir}/rocmcmakebuildtools

%doc CHANGELOG.md
%license LICENSE
%{_datadir}/rocm/*
%{_datadir}/rocmcmakebuildtools/*

%changelog
