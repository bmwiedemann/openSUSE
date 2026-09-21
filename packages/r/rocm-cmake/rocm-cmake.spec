#
# spec file for package rocm-cmake
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


%bcond_with preview
%if %{with preview}
%global rocm_release 7.14
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 0
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
# install to /usr/lib64/rocm/rocm-<major>.<minor>
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix %{rocm_release}
%else
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%global pkg_name rocm-cmake%{pkg_suffix}

# there is no debug package - this is just cmake modules
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        %{rocm_version}
%if %{with preview}
Release:        1%{?dist}
%else
Release:        4%{?dist}
%endif
Summary:        CMake modules for common build and development tasks for ROCm
License:        MIT
URL:            https://github.com/ROCm/rocm-cmake
Source:         %{url}/archive/%{pkg_src}.tar.gz#/rocm-cmake-rocm-%{version}.tar.gz
# https://github.com/ROCm/rocm-cmake/issues/276
Patch0:         0001-rocm-cmake-follow-cmake-install-rules.patch

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  rocm-filesystem%{pkg_suffix}

Requires:       cmake
Requires:       rocm-filesystem%{pkg_suffix}

%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.

%prep
%autosetup -p1 -n rocm-cmake-%{pkg_src}

# Another hardcoding of the libdir
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' share/rocmcmakebuildtools/cmake/ROCMCreatePackage.cmake
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' share/rocmcmakebuildtools/cmake/ROCMInstallTargets.cmake

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-cmake/LICENSE

%files
%if %{without compat}
%doc CHANGELOG.md
%license LICENSE
%endif
%{pkg_prefix}/share/rocm/
%{pkg_prefix}/share/rocmcmakebuildtools/

%changelog
