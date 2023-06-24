#
# spec file for package ding-libs
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


# Defined in version.m4
%global path_utils_version 0.2.1
%global dhash_version 0.5.0
%global collection_version 0.7.0
%global ref_array_version 0.1.5
%global basicobjects_version 0.1.1
%global ini_config_version 1.3.1

Name:           ding-libs
Version:        0.6.2
Release:        0
Summary:        "Ding is not GLib" assorted utility libraries
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/SSSD/ding-libs

Source:         https://github.com/SSSD/ding-libs/releases/download/%version/%name-%version.tar.gz
Source2:        https://github.com/SSSD/ding-libs/releases/download/%version/%name-%version.tar.gz.asc
Source3:        %name.keyring
Source4:        baselibs.conf
Patch1:         0001-increase-ini-max-value-length.patch
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check) >= 0.9.5

%description
Assorted C utility libraries: libcollection, libdhash, libini_config,
librefarray, libpath_utils and libbasicobjects.

%package -n libbasicobjects0
Summary:        Library containing basic objects like dynamic string
License:        GPL-3.0-or-later
Group:          System/Libraries
Version:        %basicobjects_version
Release:        0

%description -n libbasicobjects0
A small library that provides a buffer object.

%package -n libbasicobjects-devel
Summary:        Library containing basic objects like dynamic string
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        %basicobjects_version
Release:        0
Requires:       libbasicobjects0 = %version

%description -n libbasicobjects-devel
A small library that provides a buffer object.

%package -n libcollection4
Summary:        Collection data type for C
License:        LGPL-3.0-or-later
Group:          System/Libraries
Version:        %collection_version
Release:        0

%description -n libcollection4
A data-type to collect data in a hierarchical structure for easy iteration
and serialization

%package -n libcollection-devel
Summary:        Development files for libcollection
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        %collection_version
Release:        0
Requires:       libcollection4 = %collection_version

%description -n libcollection-devel
A data-type to collect data in a hierarchical structure for easy iteration
and serialization

%package -n libdhash1
Summary:        Dynamic hash table library
License:        LGPL-3.0-or-later
Group:          System/Libraries
Version:        %dhash_version
Release:        0

%description -n libdhash1
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%package -n libdhash-devel
Summary:        Development files for libdhash
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        %dhash_version
Release:        0
Requires:       libdhash1 = %dhash_version

%description -n libdhash-devel
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%package -n libini_config5
Summary:        INI file parser for C
License:        LGPL-3.0-or-later
Group:          System/Libraries
Version:        %ini_config_version
Release:        0

%description -n libini_config5
Library to process config files in INI format into a libcollection data
structure

%package -n libini_config-devel
Summary:        Development files for libini_config
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        %ini_config_version
Release:        0
Requires:       libini_config5 = %ini_config_version

%description -n libini_config-devel
Library to process config files in INI format into a libcollection data
structure

%package -n libpath_utils1
Summary:        Filesystem Path Utilities
License:        LGPL-3.0-or-later
Group:          System/Libraries
Version:        %path_utils_version
Release:        0

%description -n libpath_utils1
Utility functions to manipulate filesystem pathnames

%package -n libpath_utils-devel
Summary:        Development files for libpath_utils
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        %path_utils_version
Release:        0
Requires:       libpath_utils1 = %path_utils_version

%description -n libpath_utils-devel
Utility functions to manipulate filesystem pathnames

%package -n libref_array1
Summary:        A refcounted array for C
License:        GPL-3.0-or-later
Group:          System/Libraries
Version:        %ref_array_version
Release:        0

%description -n libref_array1
A dynamically-growing, reference-counted array

%package -n libref_array-devel
Summary:        Development files for libref_array
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        %ref_array_version
Release:        0
Requires:       libref_array1 = %ref_array_version

%description -n libref_array-devel
A dynamically-growing, reference-counted array

%prep
%setup -q
%autopatch -p1

%build
%configure --disable-static
%make_build all docs

%check
%make_build check

%install
%make_install
rm -fv "%buildroot/%_libdir"/*.la

# Remove the example files from the output directory
# We will copy them directly from the source directory
# for packaging
rm -fv \
	"%buildroot/%_datadir/doc/ding-libs"/README.* \
	"%buildroot/%_datadir/doc/ding-libs/examples/dhash_example.c" \
	"%buildroot/%_datadir/doc/ding-libs/examples/dhash_test.c"

# Remove document install script. RPM is handling this
rm -f */doc/html/installdox

%post   -n libbasicobjects0 -p /sbin/ldconfig
%postun -n libbasicobjects0 -p /sbin/ldconfig
%post   -n libcollection4 -p /sbin/ldconfig
%postun -n libcollection4 -p /sbin/ldconfig
%post   -n libdhash1 -p /sbin/ldconfig
%postun -n libdhash1 -p /sbin/ldconfig
%post   -n libini_config5 -p /sbin/ldconfig
%postun -n libini_config5 -p /sbin/ldconfig
%post   -n libpath_utils1 -p /sbin/ldconfig
%postun -n libpath_utils1 -p /sbin/ldconfig
%post   -n libref_array1 -p /sbin/ldconfig
%postun -n libref_array1 -p /sbin/ldconfig

%files -n libbasicobjects0
%_libdir/libbasicobjects.so.0*

%files -n libbasicobjects-devel
%_includedir/simplebuffer.h
%_libdir/libbasicobjects.so
%_libdir/pkgconfig/basicobjects.pc

%files -n libcollection4
%_libdir/libcollection.so.4*

%files -n libcollection-devel
%license COPYING COPYING.LESSER
%_includedir/collection.h
%_includedir/collection_tools.h
%_includedir/collection_queue.h
%_includedir/collection_stack.h
%_libdir/libcollection.so
%_libdir/pkgconfig/collection.pc
%doc collection/doc/html/

%files -n libdhash1
%_libdir/libdhash.so.1*

%files -n libdhash-devel
%license COPYING COPYING.LESSER
%_includedir/dhash.h
%_libdir/libdhash.so
%_libdir/pkgconfig/dhash.pc
%doc dhash/README.dhash

%files -n libini_config5
%_libdir/libini_config.so.5*

%files -n libini_config-devel
%license COPYING COPYING.LESSER
%_includedir/ini_*.h
%_libdir/libini_config.so
%_libdir/pkgconfig/ini_config.pc
%doc ini/doc/html/

%files -n libpath_utils1
%_libdir/libpath_utils.so.1*

%files -n libpath_utils-devel
%license COPYING COPYING.LESSER
%_includedir/path_utils.h
%_libdir/libpath_utils.so
%_libdir/pkgconfig/path_utils.pc
%doc path_utils/README.path_utils
%doc path_utils/doc/html/

%files -n libref_array1
%_libdir/libref_array.so.1*

%files -n libref_array-devel
%license COPYING COPYING.LESSER
%_includedir/ref_array.h
%_libdir/libref_array.so
%_libdir/pkgconfig/ref_array.pc
%doc refarray/README.ref_array
%doc refarray/doc/html/

%changelog
