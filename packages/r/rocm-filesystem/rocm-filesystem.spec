#
# spec file for package rocm-filesystem
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


%global rocm_release 7.2
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
# This is a noarch package, _lib macro is 'lib', we need lib64
# So hardcode pkg_libdir to lib64
%global pkg_libdir lib64
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

Name:           rocm-filesystem%{pkg_suffix}
Version:        %{rocm_version}
Release:        6%{?dist}

Summary:        ROCm directories

URL:            https://fedoraproject.org
License:        MIT

# the devel subpackage is only headers and cmake infra
%if 0%{?suse_version}
# OBS has many complaints like this
# [   13s] rocm-filesystem.noarch: E: filelist-forbidden-noarch (Badness: 10000) /usr/lib64/rocm
# Only have x86_64 for suse
ExclusiveArch:  x86_64
%else
BuildArch:      noarch
%endif

%if %{with compat}
BuildRequires:  rocm-filesystem
Requires:       rocm-filesystem
%endif

%description
%{summary}

%prep
# Empty

%build
# Empty

%install

# Make directories users of rocm-rpm-modules will install to
%global modules_gpu_list gfx8 gfx9 gfx10 gfx11 gfx12 gfx906 gfx908 gfx90a gfx942 gfx950 gfx1031 gfx1036 gfx1100 gfx1101 gfx1102 gfx1103 gfx1150 gfx1151 gfx1152 gfx1153 gfx1200 gfx1201
for gpu in %{modules_gpu_list}
do
    mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rocm/$gpu/lib/cmake
    mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rocm/$gpu/bin
    mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rocm/$gpu/include
done
mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rocm/lib/cmake
mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rocm/bin
mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rocm/include

%if %{with compat}
mkdir -p %{buildroot}%{pkg_prefix}/bin
mkdir -p %{buildroot}%{pkg_prefix}/include
mkdir -p %{buildroot}%{pkg_prefix}/libexec
mkdir -p %{buildroot}%{pkg_prefix}/share
mkdir -p %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake
%endif

%files
%if %{with compat}
%dir %{pkg_prefix}/
%dir %{pkg_prefix}/bin
%dir %{pkg_prefix}/include
%dir %{pkg_prefix}/libexec
%dir %{pkg_prefix}/share
%dir %{pkg_prefix}/%{pkg_libdir}
%dir %{pkg_prefix}/%{pkg_libdir}/cmake
%endif
%dir %{pkg_prefix}/%{pkg_libdir}/rocm
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx8
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx8/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx8/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx8/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx8/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx9
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx9/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx9/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx9/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx9/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx10
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx10/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx10/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx10/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx10/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx11
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx11/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx11/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx11/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx11/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx12
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx12/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx12/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx12/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx12/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx906
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx906/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx906/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx906/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx906/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx908
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx908/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx908/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx908/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx908/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx90a
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx90a/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx90a/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx90a/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx90a/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx942
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx942/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx942/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx942/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx942/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx950
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx950/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx950/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx950/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx950/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1031
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1031/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1031/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1031/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1031/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1036
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1036/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1036/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1036/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1036/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1100
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1100/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1100/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1100/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1100/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1101
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1101/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1101/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1101/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1101/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1102
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1102/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1102/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1102/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1102/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1103
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1103/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1103/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1103/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1103/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1150
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1150/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1150/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1150/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1150/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1151
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1151/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1151/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1151/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1151/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1152
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1152/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1152/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1152/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1152/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1153
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1153/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1153/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1153/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1153/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1200
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1200/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1200/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1200/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1200/lib/cmake
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1201
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1201/bin
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1201/include
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1201/lib
%dir %{pkg_prefix}/%{pkg_libdir}/rocm/gfx1201/lib/cmake

%changelog
