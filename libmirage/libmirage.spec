#
# spec file for package libmirage
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libmirage
%define lname   libmirage11
%define pname	3_2
Summary:        A CD-ROM image access library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Version:        3.2.2
Release:        0
URL:            http://cdemu.sf.net/about/libmirage/

#Git-Clone:     git://git.code.sf.net/p/cdemu/code
Source:         http://downloads.sf.net/cdemu/%name-%version.tar.bz2
BuildRequires:  cmake >= 2.8.5
BuildRequires:  intltool >= 0.21
BuildRequires:  pkg-config >= 0.16
%if 0%{?sles_version} && 0%{?suse_version} == 1110
# SLES 11 is still supported
# Dependencies list in an old style
BuildRequires:  glib2-devel >= 2.28
BuildRequires:  gtk-doc >= 1.4
BuildRequires:  libbz2-devel >= 1.0.0
BuildRequires:  libsamplerate-devel >= 0.1.0
BuildRequires:  libsndfile-devel >= 1.0.0
BuildRequires:  shared-mime-info
BuildRequires:  xz-devel >= 5.0.0
BuildRequires:  zlib-devel >= 1.2.4
%else
BuildRequires:  pkgconfig(bzip2) >= 1.0.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.38
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(gtk-doc) >= 1.4
BuildRequires:  pkgconfig(liblzma) >= 5.0.0
BuildRequires:  pkgconfig(samplerate) >= 0.1.0
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile) >= 1.0.0
BuildRequires:  pkgconfig(zlib) >= 1.2.4
%endif
Recommends:     %name-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A CD-ROM image access library part of the cdemu suite.

libmirage provides uniform access to the data stored in different
image formats by creating a representation of disc stored in image
file.

%package lang
Summary:        Translations for libmirage
Group:          System/Localization
Provides:       %name-lang-all = %version
Supplements:    packageand(bundle-lang-other:%lname)
BuildArch:      noarch

%description lang
Provides translations for the "%name" package.

%package -n %lname
Summary:        A CD-ROM image access library
# Technically Suggests:, but pretty useless without
Group:          System/Libraries
Requires:       libmirage-%pname >= %version

%description -n %lname
A CD-ROM image access library part of the cdemu suite.

libmirage provides uniform access to the data stored in different
image formats by creating a representation of disc stored in image
file.

%package %pname
Summary:        CD-ROM image format plugins for libmirage
Group:          System/Libraries
Recommends:     libmirage-data

%description %pname
A CD-ROM image access library part of the cdemu suite.

libmirage provides uniform access to the data stored in different
image formats by creating a representation of disc stored in image
file.

This package provides the image format plugins for libmirage.

%package devel
Summary:        Development files for libmirage, a CD-ROM image access library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glib2-devel

%description devel
A CD-ROM image access library part of the cdemu suite.

libmirage provides uniform access to the data stored in different
image formats by creating a representation of disc stored in image
file.

This package contains files needed to develop with libmirage.

%package data
Summary:        MIME type definitions and documentation for libmirage
Group:          Development/Libraries/C and C++
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
%if 0%{?suse_version} >= 1130
BuildArch:      noarch
%endif

%description data
libmirage provides uniform access to the data stored in different
image formats by creating a representation of disc stored in image
file.

This package contains the MIME type definitions and documentation.

%package -n typelib-1_0-libmirage-%pname
Summary:        The libmirage CD-ROM image access library – introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-libmirage-%pname
libmirage provides uniform access to the data stored in different
image formats by creating a representation of disc stored in image
file.

This package provides the GObject Introspection bindings for libmirage.

%prep
%setup -q

%build
%cmake -DCMAKE_MODULE_LINKER_FLAGS=""
make %{?_smp_mflags}

%install
%cmake_install
%find_lang %name

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%post data
%if 0%{?sles_version} && 0%{?suse_version} == 1110
/usr/bin/update-mime-database %{_datadir}/mime >/dev/null || :
%else
%mime_database_post
%endif

%postun data
%if 0%{?sles_version} && 0%{?suse_version} == 1110
/usr/bin/update-mime-database %{_datadir}/mime >/dev/null || :
%else
%mime_database_postun
%endif

%files -n %lname
%defattr(-,root,root)
%_libdir/libmirage.so.11*

%files %pname
%defattr(-,root,root)
%_libdir/libmirage-3*/

%files data
%defattr(-,root,root)
%_datadir/gtk-doc/
%_datadir/mime/packages/*

%files devel
%defattr(-,root,root)
%_includedir/libmirage-3*/
%_libdir/libmirage.so
%_libdir/pkgconfig/libmirage.pc
%if 0%{?suse_version} > 1110
%_datadir/gir-1.0

%files lang -f %name.lang
%defattr(-,root,root)

%files -n typelib-1_0-libmirage-%pname
%defattr(-,root,root)
%_libdir/girepository-1.0
%endif

%changelog
