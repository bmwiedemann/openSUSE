#
# spec file for package libgnomeui
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


Name:           libgnomeui
Version:        2.24.6+20170807.30334c28
Release:        0
Summary:        The GNOME User Interface Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org/
# Source based on tar_scm _service
Source:         %{name}-%{version}.tar.xz
#Source:         http://ftp.gnome.org/pub/GNOME/sources/%%{name}/2.24/%%{name}-%%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM libgnomeui-bnc468821-do-not-steal-sm-connection.patch bnc468821 bgo573058 vuntz@novell.com -- Make libgnomeui only handle SM connection it has initiated
Patch0:         libgnomeui-bnc468821-do-not-steal-sm-connection.patch
#
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libbonoboui-devel
BuildRequires:  libglade2-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
#
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
Requires:       shared-mime-info
Recommends:     %{name}-lang
#
# bug437293
%ifarch ppc64
Obsoletes:      libgnomeui-64bit
%endif

%description
This library contains all the user interface-related functions for
GNOME-based software. You need the libgnomeui-devel package if you want
to develop GNOME 2.x Desktop software.

%package devel
Summary:        Development files for libgnomeui
Group:          Development/Libraries/GNOME
Requires:       libgnomeui = %{version}
# Those are listed as Libs in libgnomeui-2.0.pc, and therefore are not
# automatically added
Requires:       pkgconfig(ice)
Requires:       pkgconfig(sm)
#

%description devel
This subpackage contains the header files for developing
applications that want to make use of libgnomeui.

%package doc
Summary:        Documentation for libgnomeui
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
This library contains all the user interface related functions for
GNOME-based software. You need the libgnomeui-devel package too if you
want to develop GNOME 2.x desktop based software.

%lang_package

%prep
%setup -q
translation-update-upstream
%patch0

%build
NOCONFIGURE=1 ./autogen.sh
export CFLAGS="%{optflags} -Wno-error=format-nonliteral"
%configure \
	--enable-gtk-doc \
	--libexecdir=%{_prefix}/lib/libgnomeui-2 \
	--disable-static \
	%{nil}
make %{?_smp_mflags}

%install
%make_install
%find_lang libgnomeui-2.0
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING.LIB
%{_datadir}/pixmaps/*.png
%{_libdir}/*.so.*
%{_libdir}/libglade/2.0/libgnome*.so

%files lang -f libgnomeui-2.0.lang

%files devel
%{_includedir}/libgnomeui-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgnomeui-2.0.pc

%files doc
%doc AUTHORS README NEWS ChangeLog
%{_datadir}/gtk-doc/html/libgnomeui

%changelog
