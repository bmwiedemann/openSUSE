#
# spec file for package libdicom
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


%define sover 1
Name:           libdicom
Version:        1.3.0
Release:        0
Summary:        C library for reading DICOM files
License:        MIT
URL:            https://github.com/ImagingDataCommons/libdicom
Source:         https://github.com/ImagingDataCommons/libdicom/releases/download/v%{version}/libdicom-%{version}.tar.xz
BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  uthash-devel
BuildRequires:  pkgconfig(check)

%description
libdicom is a C library and a set of command-line tools for reading DICOM WSI files.

%package -n libdicom%{sover}
Summary:        C library for reading DICOM files

%description -n libdicom%{sover}
libdicom is a C library and a set of command-line tools for reading DICOM WSI files.

%package devel
Summary:        Development files for libdicom
Requires:       libdicom%{sover} = %{version}

%description devel
libdicom is a C library and a set of command-line tools for reading DICOM WSI files.

%prep
%autosetup -p1

%build
%meson -Dtests=true

%meson_build

%install
%meson_install

%check
# Using %%meson_check fails, invoke it manually
meson test -C %{_vpath_builddir}

%ldconfig_scriptlets -n libdicom%{sover}

%files
%doc %{_mandir}/man1/dcm-dump.1%{?ext_man}
%doc %{_mandir}/man1/dcm-getframe.1%{?ext_man}
%{_bindir}/dcm-dump
%{_bindir}/dcm-getframe

%files -n libdicom%{sover}
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/libdicom.so.*

%files devel
%{_includedir}/dicom/
%{_libdir}/libdicom.so
%{_libdir}/pkgconfig/libdicom.pc

%changelog
