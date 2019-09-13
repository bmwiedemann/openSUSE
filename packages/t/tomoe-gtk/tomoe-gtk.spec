#
# spec file for package tomoe-gtk
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


Name:           tomoe-gtk
Version:        0.6.0
Release:        0
Summary:        TOMOE GTK+ library
License:        LGPL-2.1+
Group:          System/I18n/Japanese
Url:            http://sourceforge.net/projects/tomoe/
Source0:        http://kent.dl.sourceforge.net/sourceforge/tomoe/tomoe-gtk-0.6.0.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
# for /usr/share/gtk-doc
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  gucharmap-devel
BuildRequires:  libtool
BuildRequires:  tomoe-devel
BuildRequires:  update-desktop-files
Requires:       %{name}-lang = %{version}
Requires:       libtomoe-gtk0 = %{version}
BuildRequires:  fdupes

%description
TOMOE GTK+ library

%package -n libtomoe-gtk0
Summary:        TOMOE GTK+ library
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}

%description -n libtomoe-gtk0
TOMOE GTK+ library

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       gucharmap-devel
Requires:       tomoe-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package doc
Summary:        TOMOE GTK+ library
Group:          System/I18n/Japanese
Requires:       %{name} = %{version}

%description doc
TOMOE GTK+ library

%lang_package

%prep
%setup -q

%build
./autogen.sh
export CFLAGS="%{optflags}"
%configure\
%if 0%{?suse_version} > 1100
    --without-gucharmap \
	--enable-gtk-doc \
    --without-python \
%endif
	--disable-static
make CFLAGS="$CFLAGS" %{?_smp_mflags}

%install
%make_install
%find_lang tomoe-gtk
%fdupes %{buildroot}

%post -n libtomoe-gtk0 -p /sbin/ldconfig
%postun -n libtomoe-gtk0 -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_datadir}/tomoe-gtk

%files -n libtomoe-gtk0
%{_libdir}/*.so.*

%files lang -f tomoe-gtk.lang

%files devel
%{_libdir}/*.so
%{_libdir}/*.*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/tomoe/*

%files doc
%{_datadir}/gtk-doc/html/libtomoe-gtk

%changelog
