#
# spec file for package libinstpatch
#
# Copyright (c) 2020 SUSE LLC
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


%define sover   2

Name:           libinstpatch
Version:        1.1.5
Release:        0
Summary:        MIDI instrument patch library
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://www.swamiproject.org/
# Fetch source via
# sh libinstpatch-snapshot.sh latest
Source0:        libinstpatch-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sndfile)

%description
libInstPatch is a library for processing digital sample based MIDI
instrument "patch" files.

%package -n libinstpatch-1_0-%{sover}
Summary:        Libinstpatch library
Group:          System/Libraries

%description -n libinstpatch-1_0-%{sover}
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument "patch" files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.

This package contains the library of %{name}.

%package devel
Summary:        Development package for %{name}
Group:          Development/Languages/C and C++
Requires:       libinstpatch-1_0-%{sover} = %{version}

%description devel
This package includes the header files for %{name}.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post -n libinstpatch-1_0-%{sover} -p /sbin/ldconfig
%postun -n libinstpatch-1_0-%{sover} -p /sbin/ldconfig

%files -n libinstpatch-1_0-%{sover}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README.md
%doc examples/create_sf2.c
%{_includedir}/%{name}*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
