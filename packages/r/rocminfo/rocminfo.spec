#
# spec file for package rocminfo
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


%global upstreamname rocminfo

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
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_skip_rpath OFF
%global pkg_rpath %{_prefix}/lib64/rocm/rocm-%{rocm_release}/lib
%global pkg_suffix %{rocm_release}
%else
%global pkg_prefix %{_prefix}
%global pkg_skip_rpath ON
%global pkg_rpath %{nil}
%global pkg_suffix %{nil}
%endif
%global pkg_name rocminfo%{pkg_suffix}

Name:           %{pkg_name}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        5%{?dist}
%endif

Summary:        ROCm system info utility

License:        MIT AND NCSA
# Main license is NCSA
# This file is MIT
#   rocm_agent_enumerator
URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel

# rocminfo calls lsmod to check the kernel mode driver status
Requires:       kmod
Requires:       rocm-filesystem%{pkg_suffix}
Requires:       rocm-runtime%{pkg_suffix}

%description
ROCm system info utility

%prep
%autosetup -p1 -n %{upstreamname}

%if 0%{?fedora} || 0%{?rhel}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -i %{__python3} rocm_agent_enumerator
%else
# suse
sed -i -e 's@/usr/bin/env python3@/usr/bin/python3@' rocm_agent_enumerator
%endif

%build
%cmake \
    -DROCM_DIR=%{pkg_prefix} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_INSTALL_RPATH=%{pkg_rpath} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SKIP_INSTALL_RPATH=%{pkg_skip_rpath}

%cmake_build

%install
%cmake_install

#FIXME:
chmod 755 %{buildroot}%{pkg_prefix}/bin/*

# Extra licenses
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/License.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/*/License.txt

%files
%doc README.md
%license License.txt
%{pkg_prefix}/bin/rocm_agent_enumerator
%{pkg_prefix}/bin/rocminfo

%changelog
