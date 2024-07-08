#
# spec file for package libgpod
#
# Copyright (c) 2024 SUSE LLC
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


%define libsoname  %{name}4
%define _udevdir %(pkg-config --variable udevdir udev)
%if 0%{?suse_version} > 1500
%define libplist2 1
%else
%define libplist2 0
%endif
Name:           libgpod
Version:        0.8.3
Release:        0
Summary:        Library to Manipulate Songs and Playlists Stored on an iPod
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gtkpod.org/libgpod.html
Source:         http://downloads.sourceforge.net/project/gtkpod/libgpod/libgpod-0.8/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         libgpod-swig-3.0.patch
Patch1:         0001-Fix-spelling-errors-in-comments-and-strings-using-co.patch
Patch2:         0002-323-Segmentation-fault-when-opening-ipod.patch
Patch3:         0003-Fixed-PList-deprication.patch
Patch4:         libgpod-Use-libplist-2.0.patch
Patch5:         0004-gcc14.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libimobiledevice-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  sg3_utils-devel
BuildRequires:  sqlite3-devel
BuildRequires:  swig
BuildRequires:  taglib-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(udev)
%if %{libplist2}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libplist-2.0)
%else
BuildRequires:  pkgconfig(libplist)
%endif

%description
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

%package -n %{libsoname}
Summary:        Library to Manipulate Songs and Playlists Stored on an iPod
# Add provides for installability of lang package
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{libsoname}
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

%package devel
Summary:        Development files for libgpod
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       glib2-devel
Requires:       glibc-devel

%description devel
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

This package provides the development files to use libgpod.

%package doc
Summary:        Documentation for libgpod
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

This package provides development documentation for libgpod.

%package tools
Summary:        Tools for libgpod
Group:          Productivity/Multimedia/Other
Supplements:    (%{libsoname} and udev)

%description tools
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

This package includes support tools for libgpod.

%lang_package

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%if %{libplist2}
%patch -P 4 -p1
%endif
%patch -P 5 -p1

%build
%if %{libplist2}
autoreconf -fvi
%endif
%configure --disable-silent-rules \
           --disable-static \
           --with-udev-dir=%{_udevdir} \
           --with-python=no \
           --without-hal
%make_build

%install
%make_install
%find_lang libgpod
rm bindings/python/examples/Makefile*
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_libdir}/pkgconfig/libgpod-sharp.pc
%fdupes -s %{buildroot}

%post   -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.SysInfo
%{_libdir}/libgpod.so.4*

%files tools
%{_bindir}/ipod-read-sysinfo-extended
%{_udevdir}/ipod-set-info
%{_udevdir}/iphone-set-info
%{_udevdir}/rules.d/90-libgpod.rules

%files devel
%{_includedir}/gpod-1.0/
%{_libdir}/libgpod.so
%{_libdir}/pkgconfig/libgpod-1.0.pc

%files doc
%doc %{_datadir}/gtk-doc/html/libgpod/

%files lang -f libgpod.lang

%changelog
