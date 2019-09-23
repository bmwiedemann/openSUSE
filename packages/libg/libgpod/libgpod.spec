#
# spec file for package libgpod
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


%define libsoname  %{name}4
%define _udevdir %(pkg-config --variable udevdir udev)
%bcond_with    mono
%bcond_without python2
Name:           libgpod
Version:        0.8.3
Release:        0
Summary:        Library to Manipulate Songs and Playlists Stored on an iPod
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.gtkpod.org/libgpod.html
Source:         http://downloads.sourceforge.net/project/gtkpod/libgpod/libgpod-0.8/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         libgpod-swig-3.0.patch
Patch1:         0001-Fix-spelling-errors-in-comments-and-strings-using-co.patch
Patch2:         0002-323-Segmentation-fault-when-opening-ipod.patch
Patch3:         0003-Fixed-PList-deprication.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libimobiledevice-devel
BuildRequires:  libplist-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  sg3_utils-devel
BuildRequires:  sqlite3-devel
BuildRequires:  swig
BuildRequires:  taglib-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(udev)
%if %{with python2}
BuildRequires:  python-devel
BuildRequires:  python-gobject2-devel
BuildRequires:  python-mutagen
%endif
%if %{with mono}
BuildRequires:  gtk-sharp2
BuildRequires:  mono-devel
%endif

%description
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

%package -n %{libsoname}
Summary:        Library to Manipulate Songs and Playlists Stored on an iPod
Group:          System/Libraries
Recommends:     %{name}-lang
# Add provides for installability of lang package
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

%package -n python2-gpod
Summary:        Python bindings for libgpod, a library to edit songs and playlists on an iPod
Group:          Development/Languages/Python
Requires:       python-mutagen
Provides:       libgpod-python = %{version}
Obsoletes:      libgpod-python < %{version}
Provides:       python-gpod = %{version}

%description -n python2-gpod
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

This package provides python2 bindings.

%package sharp
Summary:        .NET bindings for libgpod, a library to edit songs and playlists on an iPod
Group:          Development/Languages/Mono
Requires:       %{libsoname} = %{version}

%description sharp
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

This package provides .NET bindings.

%package tools
Summary:        Tools for libgpod
Group:          Productivity/Multimedia/Other
Supplements:    packageand(%{libsoname}:udev)

%description tools
libgpod is a library meant to abstract access to iPod content. It
provides an API to retrieve the list of files and
playlists stored on an iPod, modify them, and save them back to the iPod.

This package includes support tools for libgpod.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure --disable-silent-rules \
           --disable-static \
           --with-udev-dir=%{_udevdir} \
%if %{with python2}
           --with-python=yes \
%else
           --with-python=no \
%endif
           --without-hal
make %{?_smp_mflags}

%install
%make_install
%find_lang libgpod
rm bindings/python/examples/Makefile*
find %{buildroot} -type f -name "*.la" -delete -print
%if %{without mono}
rm %{buildroot}%{_libdir}/pkgconfig/libgpod-sharp.pc
%endif
%fdupes -s %{buildroot}

%post   -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%doc AUTHORS COPYING ChangeLog NEWS README README.SysInfo
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

%if %{with python2}
%files -n python2-gpod
%doc COPYING bindings/python/examples
%{python_sitearch}/gpod/
%endif

%if %{with mono}
%files sharp
%dir %{_libdir}/libgpod
%{_libdir}/libgpod/libgpod-sharp.dll*
%{_libdir}/libgpod/libgpod-sharp-test.exe*
%{_libdir}/pkgconfig/libgpod-sharp.pc
%endif

%files lang -f libgpod.lang

%changelog
