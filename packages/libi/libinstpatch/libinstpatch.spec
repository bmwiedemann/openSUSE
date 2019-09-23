#
# spec file for package libinstpatch
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libinstpatch
Version:        1.0.0
Release:        0
Summary:        MIDI instrument patch library
License:        LGPL-2.1 AND GPL-2.0 AND GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://www.swamiproject.org/
# Fetch source via
# sh libinstpatch-snapshot.sh latest
Source0:        libinstpatch-%{version}+svn386.tar.bz2
# script to download sources and make tarball from svn
Source1:        libinstpatch-snapshot.sh
# .pc file fixes. Patch sent upstream via their mailing list
Patch0:         libinstpatch-cmake-fixes.patch
Patch1:         0001-Fix-improper-GValue-type-assignments-in-ipatch_dls2_.patch
Patch2:         0002-fix-incorrect-usage-of-g_value_set_flags.patch
Patch3:         0003-missing-mutex-unlock.patch
Patch4:         0004-more-locking-issues.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sndfile)

%description
libInstPatch is a library for processing digital sample based MIDI
instrument "patch" files.

%package -n libinstpatch-1_0-0
Summary:        Libinstpatch library
Group:          System/Libraries

%description -n libinstpatch-1_0-0
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument "patch" files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.

This package contains the library of %{name}.

%package devel
Summary:        Development package for %{name}
Group:          Development/Languages/C and C++
Requires:       libinstpatch-1_0-0 = %{version}

%description devel
This package includes the header files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .pkgconfig
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%post -n libinstpatch-1_0-0 -p /sbin/ldconfig
%postun -n libinstpatch-1_0-0 -p /sbin/ldconfig

%files -n libinstpatch-1_0-0
%defattr(-,root,root)
%doc COPYING
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%doc examples/create_sf2.c
%{_includedir}/%{name}*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
