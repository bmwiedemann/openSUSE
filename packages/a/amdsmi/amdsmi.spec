#
# spec file for package amdsmi
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


%global upstreamname amdsmi

%global pkg_library_name amd_smi
%global pkg_library_version 26

%global rocm_release 7.2
%global rocm_patch 1
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}

%global rocm_version %{rocm_release}.%{rocm_patch}

%if 0%{?suse_version}
%global library_package_name lib%{pkg_library_name}%{pkg_library_version}
%global shimlib_package_name libgoamdsmi_shim64-1
%endif

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix %{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

# Downloads its own googletest
# Testing also depends on having AMD hardware cpu and/or gpu installed.
# Not suitable for a general check
#
# Non root result for gfx1100 and this kernel 6.13.0-0.rc0.20241126git7eef7e306d3c.10.fc42.x86_64
# 25 pass, 5 fail
# No oops
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

%bcond_with static
%if %{with static}
%global build_static ON
%else
%global build_static OFF
%endif

%global esmi_ver 4.2

Name:           amdsmi%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        AMD System Management Interface

License:        GPL-2.0-only WITH Linux-syscall-note AND MIT AND NCSA
# Main license is MIT
#
# This file is GPL-2.0
# include/amd_smi/impl/amd_hsmp.h
# esmi_ib_library/include/asm/amd_hsmp.h
# Both carry this license
# /* SPDX-License-Identifier: GPL-2.0 WITH Linux-syscall-note */
# But license check says, incorrectly they are
# *No copyright* GNU General Public License, Version 2
#
# NCSA
# Covers the bundled esmi_ib_library

URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
# esmi_ib_library is not suitable for packaging
# https://github.com/amd/esmi_ib_library/issues/13
Source1:        https://github.com/amd/esmi_ib_library/archive/refs/tags/esmi_pkg_ver-%{esmi_ver}.tar.gz
# https://github.com/ROCm/amdsmi/pull/165
Patch1:         0001-Fix-compilation-with-libdrm-2.4.130.patch
Patch2:         0001-amdsmi-silence-pack-warnings.patch

ExclusiveArch:  x86_64

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kernel-devel
BuildRequires:  libdrm-devel
# No python install in compat mode.
%if %{without compat}
%if 0%{?suse_version}
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: %{python_module devel}
%else
BuildRequires: python3-devel
%endif
%endif
BuildRequires:  rocm-filesystem%{pkg_suffix}

%if %{with test}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
%endif

%if %{without compat}
%if 0%{?suse_version}
Requires:      python3-PyYAML
Requires:      python3-%{name}
%else
Requires:      python3dist(pyyaml)
%endif
%endif

%if %{with compat}
Requires:       rocm-filesystem%{pkg_suffix}
%endif

# University of Illinois/NCSA Open Source License
Provides:       bundled(esmi_ib_library) = %{esmi_ver}

%define python_subpackage_only 1
%python_subpackages

%description
The AMD System Management Interface Library, or AMD SMI library, is a C
library for Linux that provides a user space interface for applications
to monitor and control AMD devices.

%if 0%{?suse_version}
%package -n %library_package_name
Summary:     Shared libraries for %{name}

%description -n %library_package_name
%{summary}

%{ldconfig_scriptlets -n %library_package_name}

%package -n %shimlib_package_name
Summary:     Shared libraries for %{name}

%description -n %shimlib_package_name
%{summary}

%{ldconfig_scriptlets -n %shimlib_package_name}

%package -n python-%{name}
Summary:     Python Modules for %{name}
Requires:    %library_package_name = %{version}-%{release}

%description -n python-%{name}
%{summary}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?suse_version}
Requires: %library_package_name = %{version}-%{release}
Requires: %shimlib_package_name = %{version}-%{release}
%endif

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?suse_version}
Requires:       libgoamdsmi_shim64-1%{?_isa} = %{version}-%{release}
%endif
Requires:       libdrm-devel

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}

tar xf %{SOURCE1}
mv esmi_ib_library-* esmi_ib_library
# So we can pick up this license
mv esmi_ib_library/License.txt esmi_ib_library_License.txt
# The esmi version check uses git tags, but we use tar's without git files.
# Just inject in the tag that we've pulled into the version check:
sed -i 's/NOT latest_esmi_tag/NOT "esmi_pkg_ver-%{esmi_ver}"/' CMakeLists.txt

# W: spurious-executable-perm /usr/share/doc/amdsmi/README.md
chmod a-x README.md

# /usr/libexec/amdsmi_cli/BDF.py:126: SyntaxWarning: invalid escape sequence '\.'
#   bdf_regex = "(?:[0-6]?[0-9a-fA-F]{1,4}:)?[0-2]?[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}\.[0-7]"
sed -i -e 's@bdf_regex = "@bdf_regex = r"@' amdsmi_cli/BDF.py

# Fix script shebang
sed -i -e 's@env python3@python3@' amdsmi_cli/*.py

# Install local gtests in same dir as tests
sed -i -e 's@${CPACK_PACKAGING_INSTALL_PREFIX}/lib@${SHARE_INSTALL_PREFIX}/tests@' tests/amd_smi_test/CMakeLists.txt

# fix cstdint include
# https://github.com/ROCm/amdsmi/issues/123
sed -i '/#include <unordered_set.*/a#include <cstdint>' rocm_smi/include/rocm_smi/rocm_smi_common.h

# fix iomanip include
# https://github.com/ROCm/amdsmi/issues/124
sed -i '/#include <string.*/a#include <iomanip>' tests/amd_smi_test/test_common.h

# Do not hardcode share dir
sed -i 's@set(SHARE_INSTALL_PREFIX@#set(SHARE_INSTALL_PREFIX@' CMakeLists.txt

%build
%cmake \
    -DAUTO_BUILD_STATIC_LIBS=%{build_static} \
    -DBUILD_BOTH_LIBS=%{build_static} \
    -DBUILD_KERNEL_ASM_DIR=/usr/include/asm \
    -DBUILD_TESTS=%{build_test} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
    -DSHARE_INSTALL_PREFIX=%{pkg_prefix}/share \
    -DUSE_SYSTEM_GTEST=%{build_test} \
    %{nil}

%cmake_build

%install
%cmake_install

%if %{without compat}
%if 0%{?suse_version}
src=%{buildroot}%{pkg_prefix}/share
[ -d $src/amd_smi/amdsmi ] && src=$src/amd_smi
%{python_expand #
mkdir -p %{buildroot}/%{$python_sitelib}
cp -r $src/amdsmi %{buildroot}/%{$python_sitelib}
cp $src/pyproject.toml %{buildroot}/%{$python_sitelib}/amdsmi/
 }
%python_compileall
%{python_expand #
  %fdupes %{buildroot}/%{$python_sitelib}/amdsmi/__pycache__
 }
rm -rf $src/amdsmi $src/pyproject.toml
%else
mkdir -p %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
if [ -d %{buildroot}%{pkg_prefix}/share/amd_smi/amdsmi ]; then
    mv %{buildroot}%{pkg_prefix}/share/amd_smi/amdsmi %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
    mv %{buildroot}%{pkg_prefix}/share/amd_smi/pyproject.toml %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/
else
    mv %{buildroot}%{pkg_prefix}/share/amdsmi %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages
    mv %{buildroot}%{pkg_prefix}/share/pyproject.toml %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/
fi
%endif

# W: unstripped-binary-or-object /usr/lib/python3.13/site-packages/amdsmi/libamd_smi.so
# Does an explict open, so can not just rm it
# let's just strip it
strip %{buildroot}/%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi/*.so
# E: non-executable-script .../amdsmi_cli/amdsmi_cli_exceptions.py 644 /usr/bin/env python3
chmod a+x %{buildroot}/%{pkg_prefix}/libexec/amdsmi_cli/amdsmi_*.py

%else
rm -f %{buildroot}/%{pkg_prefix}/bin/amd-smi
rm -rf %{buildroot}/%{pkg_prefix}/libexec/amdsmi_cli
rm -rf %{buildroot}/%{pkg_prefix}/share/amdsmi
rm -rf %{buildroot}/%{pkg_prefix}/share/pyproject.toml

# Not going to handle golang in compat mode
rm -rf %{buildroot}/%{pkg_prefix}/%{pkg_libdir}/libgoamdsmi_shim64*
%endif

# Remove some things
rm -rf %{buildroot}/%{pkg_prefix}/share/example
rm -rf %{buildroot}/%{pkg_prefix}/share/amd_smi/example
rm -rf %{buildroot}/%{pkg_prefix}/share/doc/amd_smi-asan/LICENSE.txt
rm -f %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/LICENSE.txt
rm -f %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/README.md
rm -rf %{buildroot}/%{pkg_prefix}/share/doc/amd-smi-lib/copyright
rm -f %{buildroot}%{pkg_prefix}/share/_version.py
rm -f %{buildroot}%{pkg_prefix}/share/amd_smi/_version.py
rm -f %{buildroot}%{pkg_prefix}/share/setup.py
rm -f %{buildroot}%{pkg_prefix}/share/amd_smi/setup.py

if [ -e %{buildroot}%{pkg_prefix}/share/tests ]; then
  # put the test files in a reasonable place
  mkdir %{buildroot}%{pkg_prefix}/share/amdsmi
  mv %{buildroot}%{pkg_prefix}/share/tests %{buildroot}%{pkg_prefix}/share/amdsmi/
fi

%if 0%{?suse_version}
%files
%{pkg_prefix}/bin/amd-smi
%{pkg_prefix}/libexec/amdsmi_cli

%files %{python_files %name}
%{python_sitelib}/amdsmi

%files -n %library_package_name
%doc README.md
%license LICENSE
%license esmi_ib_library_License.txt
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%if %{without compat}

%files -n %shimlib_package_name
%doc README.md
%license esmi_ib_library_License.txt
%{pkg_prefix}/%{pkg_libdir}/libgoamdsmi_shim64.so.1{,.*}
%endif

%else

%files
%doc README.md
%license LICENSE
%license esmi_ib_library_License.txt
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%if %{without compat}
%{pkg_prefix}/%{pkg_libdir}/libgoamdsmi_shim64.so.1{,.*}
%{pkg_prefix}/bin/amd-smi
%{pkg_prefix}/libexec/amdsmi_cli
%{pkg_prefix}/lib/python%{python3_version}/site-packages/amdsmi
%endif
%endif

%files devel
%{pkg_prefix}/include/amd_smi/
%{pkg_prefix}/include/*.h
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%{pkg_prefix}/%{pkg_libdir}/cmake/amd_smi/
%if %{without compat}
%{pkg_prefix}/%{pkg_libdir}/libgoamdsmi_shim64.so
%endif

%if %{with test}
%files test
%{pkg_prefix}/share/amdsmi/
%endif

%changelog
