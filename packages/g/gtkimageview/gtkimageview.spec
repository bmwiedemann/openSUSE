#
# spec file for package gtkimageview
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


Name:           gtkimageview
Version:        1.6.4
Release:        0
Summary:        Library providing an advanced widget for GdkPixbuf
License:        LGPL-2.0-or-later
Group:          Development/Libraries/GNOME
Url:            http://trac.bjourne.webfactional.com
Source:         gtkimageview-%{version}.tar.bz2
BuildRequires:  gtk2-devel

%description
GtkImageView is a widget that provides a zoomable and panable view of a
GdkPixbuf. It is intended to be usable in most types of image viewing
applications.

%package -n libgtkimageview0
Summary:        Library providing an advanced widget for GdkPixbuf
Group:          Development/Libraries/GNOME

%description -n libgtkimageview0
GtkImageView is a widget that provides a zoomable and panable view of a
GdkPixbuf. It is intended to be usable in most types of image viewing
applications.

%package devel
Summary:        Development files for gtkimageview
Group:          Development/Libraries/GNOME
Requires:       gtk2-devel
Requires:       libgtkimageview0 = %{version}
Provides:       libgtkimageview-devel = %{version}
Obsoletes:      libgtkimageview-devel < %{version}

%description devel
GtkImageView is a widget that provides a zoomable and panable view of a
GdkPixbuf. It is intended to be usable in most types of image viewing
applications.

%prep
%setup -q
# Allow the usage of deprecated functions of gdk-pixbuf
sed -i "s:-DGDK_PIXBUF_DISABLE_DEPRECATED::g" configure
# As deprecations are still a warning, we also have to stop raising them to errors
sed -i "s:-Werror::g" configure

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post   -n libgtkimageview0 -p /sbin/ldconfig
%postun -n libgtkimageview0 -p /sbin/ldconfig

%files -n libgtkimageview0
%license COPYING
%doc README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/gtkimageview/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/gtkimageview

%changelog
