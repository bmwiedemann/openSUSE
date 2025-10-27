#
# spec file for package rocm-core
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

# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version}
# 15.6
# rocm-core.x86_64: E: shlib-policy-name-error (Badness: 10000) librocm-core1
# Your package contains a single shared library but is not named after its SONAME.
%global core_name librocm-core1
%else
%global core_name rocm-core
%endif

%global upstreamname rocm-core
%global rocm_release 6.4
%global rocm_patch 3
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:           rocm-core
Version:        %{rocm_version}
Release:        2%{?dist}
Summary:        A utility to get the ROCm release version
URL:            https://github.com/ROCm/%{upstreamname}
License:        MIT

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

Provides:       rocm-core = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
%{summary}

%if 0%{?suse_version}
%package -n %{core_name}
Summary:        Shared libraries for %{name}

%description -n %{core_name}
%{summary}

%ldconfig_scriptlets -n %{core_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{core_name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake -DROCM_VERSION=%{rocm_version}
%cmake_build

%install
%cmake_install

rm -rf %{buildroot}/%{_prefix}/.info
rm -rf %{buildroot}/%{_libdir}/rocmmod
rm -rf %{buildroot}/%{_docdir}/*/LICENSE.txt
rm -rf %{buildroot}/%{_libexecdir}/%{name}

mv  %{buildroot}/%{_includedir}/rocm-core/*.h %{buildroot}/%{_includedir}/
rm -rf %{buildroot}/%{_includedir}/rocm-core

find %{buildroot} -type f -name 'runpath_to_rpath.py' -exec rm {} \;

%files -n %{core_name}
%license copyright
%{_libdir}/librocm-core.so.*

%files devel
%dir %{_libdir}/cmake/rocm-core
%{_includedir}/*.h
%{_libdir}/librocm-core.so
%{_libdir}/cmake/rocm-core/*.cmake

%changelog
