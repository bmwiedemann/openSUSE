#
# spec file for package libtracecmd
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


Name:           libtracecmd
%define lname   libtracecmd1
Version:        1.3.1
Release:        0
Summary:        Library for creating and reading trace-cmd data files
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git
Source:         https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-libtracecmd-%version.tar.gz
Patch1:         0001-libtracecmd-Add-initial-support-for-meson.patch
Patch2:         0002-trace-cmd-Add-initial-support-for-meson.patch
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  libtraceevent-devel
BuildRequires:  libtracefs-devel >= 1.6
BuildRequires:  libzstd-devel
BuildRequires:  meson
BuildRequires:  source-highlight
BuildRequires:  xmlto

%description
Library for creating and reading trace-cmd data files

%package -n %lname
Summary:        Library for creating and reading trace-cmd data files
Group:          System/Libraries

%description -n %lname
Library for creating and reading trace-cmd data files

%package devel
Summary:        Development files for libtracecmd
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Development files of the libtracecmd library

%prep
%autosetup -p1 -n trace-cmd-libtracecmd-%version

%build
cd lib
%meson \
    --default-library=shared \
    -Dhtmldir="%_docdir/%name"
%meson_build
%meson_build docs

%install
cd lib
%meson_install

%fdupes %buildroot/%_prefix

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libtracecmd.so.1*
%license COPYING.LIB

%files devel
%_includedir/trace-cmd
%_libdir/libtracecmd.so
%_libdir/pkgconfig/*.pc
%_mandir/man*/*
%_docdir/libtracecmd
%license COPYING.LIB
%doc README

%changelog
