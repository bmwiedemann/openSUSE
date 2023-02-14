#
# spec file for package libaom
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 3
%define __builder ninja
%define __builddir _build
Name:           libaom
Version:        3.6.0
Release:        0
Summary:        AV1 codec library
License:        BSD-2-Clause
Group:          Productivity/Multimedia/Other
URL:            https://aomedia.googlesource.com/aom/
Source0:        %{name}-%{version}.tar.xz
Source99:       baselibs.conf
Patch0:         libaom-0001-Do-not-disable-_FORTIFY_SOURCE.patch

BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.6
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  yasm

%description
This is a library for AOMedia Video 1 (AV1), an open, royalty-free
video coding format designed for video transmissions over the Internet.

%package -n %{name}%{sover}
Summary:        AV1 codec library
Group:          System/Libraries

%description -n %{name}%{sover}
This is a library for AOMedia Video 1 (AV1), an open, royalty-free
video coding format designed for video transmissions over the Internet.

%package devel
Summary:        Development files for libaom, an AV1 codec library
Group:          Development/Languages/C and C++
Requires:       %{name}%{sover} = %{version}

%description devel
This package contains the development headers and library files for
libaom, a library for the AOMedia Video 1 (AV1) video coding format.

%package devel-doc
Summary:        Documentation for the libaom API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains the API documentation for libaom, a library
for the AOMedia Video 1 (AV1) video coding format.

%package -n aom-tools
Summary:        AV1 Codec Library Tools
Group:          Productivity/Multimedia/Other

%description -n aom-tools
This package contains tools included with libaom, a library for
the AOMedia Video 1 (AV1) video coding format.

%prep
%autosetup -p1

%build

%cmake \
	-DCONFIG_LOWBITDEPTH=1 \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
%ifnarch aarch64 %{arm} %{ix86} x86_64
	-DAOM_TARGET_CPU=generic \
%endif
%ifarch %{arm}
	-DAOM_TARGET_CPU=arm \
%ifarch armv3l armv4b armv4l armv4tl armv5tl armv5tel armv5tejl armv6l armv6hl armv7l armv7hl armv7hnl
	-DENABLE_NEON=OFF \
%endif
%endif
%ifarch aarch64
	-DAOM_TARGET_CPU=arm64 \
%endif
%ifarch %{ix86}
	-DAOM_TARGET_CPU=x86 \
%endif
%ifarch x86_64
	-DAOM_TARGET_CPU=x86_64 \
%endif
	%{nil}
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/%{name}.a

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE PATENTS
%doc AUTHORS CHANGELOG
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/aom
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/aom.pc

%files devel-doc
%doc %{__builddir}/docs/html/*

%files -n aom-tools
%{_bindir}/aomdec
%{_bindir}/aomenc

%changelog
