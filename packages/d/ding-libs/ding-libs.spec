#
# spec file for package ding-libs
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


# Defined in version.m4
%global dhash_version 0.5.0
%global ini_config_version 2.0.0

Name:           ding-libs
Version:        0.7.0
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

%package -n libini_config8
Summary:        INI file parser for C
License:        LGPL-3.0-or-later
Group:          System/Libraries
Version:        %ini_config_version
Release:        0

%description -n libini_config8
Library to process config files in INI format into a libcollection data
structure

%package -n libini_config-devel
Summary:        Development files for libini_config
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Version:        %ini_config_version
Release:        0
Requires:       libini_config8 = %ini_config_version
Obsoletes:      libref_array-devel < %ini_config_version
Provides:       libref_array-devel = %ini_config_version

%description -n libini_config-devel
Library to process config files in INI format into a libcollection data
structure

%prep
%autosetup -p1

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

%ldconfig_scriptlets -n libdhash1
%ldconfig_scriptlets -n libini_config8

%files -n libdhash1
%_libdir/libdhash.so.*

%files -n libdhash-devel
%license COPYING COPYING.LESSER
%_includedir/dhash.h
%_libdir/libdhash.so
%_libdir/pkgconfig/dhash.pc
%doc dhash/README.dhash

%files -n libini_config8
%_libdir/libini_config.so.*

%files -n libini_config-devel
%license COPYING COPYING.LESSER
%_includedir/ini_*.h
%_includedir/ref_array.h
%_libdir/libini_config.so
%_libdir/pkgconfig/ini_config.pc
%doc ini/doc/html/

%changelog
