#
# spec file for package mypaint-brushes
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mypaint-brushes
Version:        1.3.0
Release:        0
Summary:        Brushes to be used with the MyPaint library
# According to Licenses.dep5 the files used for building/installing are GPLv2+
# but the shipped brush files are CC0-1.0
License:        CC0-1.0
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://github.com/Jehan/mypaint-brushes

Source0:        https://github.com/Jehan/mypaint-brushes/archive/v%{version}.tar.gz#/mypaint-brushes-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mypaint-brushes-1.3.0-automake16.patch -- autogen: add automake 1.16 support.
Patch0:         mypaint-brushes-1.3.0-automake16.patch

BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

BuildArch:      noarch

%description
This package contains brush files for use with MyPaint and other programs.

%package devel
Summary:        Files for developing with mypaint-brushes
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++

%description devel
This package contains a pkgconfig file which makes it easier to develop
programs using these brush files.

%prep
%autosetup

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING Licenses.dep5 Licenses.md
%doc AUTHORS NEWS README.md
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/1.0
%{_datadir}/mypaint-data/1.0/brushes

%files devel
%license COPYING Licenses.dep5 Licenses.md
%{_datadir}/pkgconfig/mypaint-brushes-1.0.pc

%changelog
