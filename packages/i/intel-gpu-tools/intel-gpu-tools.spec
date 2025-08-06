#
# spec file for package intel-gpu-tools
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


Name:           intel-gpu-tools
Version:        2.1
Release:        0
Summary:        Collection of tools for development and testing of the Intel DRM driver
License:        MIT
Group:          Development/Tools/Other
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/igt-gpu-tools-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/app/igt-gpu-tools-%{version}.tar.xz.sig
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  meson >= 0.52.1
BuildRequires:  peg
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm_intel) >= 2.4.82
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libkmod)
# This is only for tests
#BuildRequires:  pkgconfig(liboping)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(xmlrpc)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xv)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
Provides:       igt-gpu-tools = %{version}
# Intel GPU is only available on x86 and x86-64
ExclusiveArch:  %{ix86} x86_64
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libproc2)
%else
BuildRequires:  pkgconfig(libprocps)
%endif

%description
This is a collection of tools for development and testing of the Intel
DRM driver.

%package devel
Summary:        Development files for %{name}
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description devel
Development files and library headers for %{name}

%prep
%autosetup -n igt-gpu-tools-%{version}

%build
%meson -Doping="disabled"
%meson_build
# build documentation
ninja -C %{_vpath_builddir} igt-gpu-tools-doc

%install
%meson_install

# fix env-script-interpreter
sed -i 's#/usr/bin/env python3#/usr/bin/python3#' \
	%{buildroot}%{_bindir}/{code_cov_gather_on_test,intel-gfx-fw-info}

%fdupes %{buildroot}%{_includedir}
%fdupes %{buildroot}%{_libexecdir}

# These are only useful with the full source tree
rm -v %{buildroot}%{_bindir}/code_cov_*

%check
%meson_test

%if 0%{?suse_version} > 1500
%ldconfig_scriptlets
%else
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%doc NEWS README.md
%license COPYING
%{_bindir}/*
%{_libexecdir}/igt-gpu-tools/
%{_datadir}/igt-gpu-tools/
%{_libdir}/libigt.so.0
%{_libdir}/libi915_perf.so.1.5
%{_libdir}/libxe_oa.so.1.5
%{_mandir}/man1/intel_*
%{_mandir}/man1/lsgpu*
%doc %{_datadir}/gtk-doc/html/igt-gpu-tools/

%files devel
%{_libdir}/libigt.so
%{_libdir}/libi915_perf.so
%{_libdir}/pkgconfig/i915-perf.pc
%{_libdir}/pkgconfig/intel-gen4asm.pc
%{_includedir}/i915-perf/
%{_includedir}/xe-oa/
%{_libdir}/libxe_oa.so
%{_libdir}/pkgconfig/xe-oa.pc

%changelog
