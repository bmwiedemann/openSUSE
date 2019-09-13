#
# spec file for package gmime2_6
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


%define _name gmime
%bcond_without mono
Name:           gmime2_6
Version:        2.6.23
Release:        0
Summary:        MIME Parser and Utility Library
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            http://spruce.sourceforge.net/gmime/
Source:         http://download.gnome.org/sources/gmime/2.6/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM gmime2_6-utf8.patch dimstar@opensuse.org -- Remove some non-ascii linebreaks
Patch0:         gmime2_6-utf8.patch
BuildRequires:  gobject-introspection-devel >= 1.30.0
BuildRequires:  gpgme-devel
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glib-2.0)
%if %{with mono}
BuildRequires:  mono-devel
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
%endif

%description
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%package -n libgmime-2_6-0
Summary:        MIME Parser and Utility Library
# The tools package was only for some sample applications, which are no longer installed since 2.6.5
Group:          System/Libraries
Obsoletes:      %{name}-tools < %{version}

%description -n libgmime-2_6-0
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%package -n typelib-1_0-GMime-2_6
Summary:        MIME Parser and Utility Library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GMime-2_6
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%if %{with mono}
%package sharp
Summary:        MIME Parser and Utility Library -- Mono Bindings
Group:          Development/Libraries/Other
Requires:       glib-sharp2
Requires:       libgmime-2_6-0 = %{version}
# Obsoletes without Provides: gmime-2_4-sharp was an old name
# during 2.4.x days, and even though API is different, we need to
# get rid of it since some files are common.
Obsoletes:      gmime-2_4-sharp < %{version}

%description sharp
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).
%endif

%package devel
Summary:        MIME Parser and Utility Library -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libgmime-2_6-0 = %{version}

%description devel
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%define __find_requires env sh -c 'filelist=($(cat)) && { printf "%%s\\n" "${filelist[@]}" | %{_prefix}/lib/rpm/find-requires | grep -v "no package provides" ; } '

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%ifarch %{arm}
# gcc has a bug on ARM where it fails to compile certain source files
# with >= -O2. See https://bugs.launchpad.net/gcc/+bug/836588.
CFLAGS="%{optflags} -O1"
%endif
%configure\
	--enable-largefile\
	--disable-static\
	--enable-gtk-doc \
%if %{with mono}
        --enable-mono \
%else
        --disable-mono \
%endif
        --with-gacdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
for FILE in COPYING ; do
    MD5SUM=$(md5sum $FILE | sed 's/ .*//')
    if test -f %{_datadir}/doc/licenses/md5/$MD5SUM ; then
        ln -sf %{_datadir}/doc/licenses/md5/$MD5SUM $FILE
    fi
done

%post -n libgmime-2_6-0 -p /sbin/ldconfig
%postun -n libgmime-2_6-0 -p /sbin/ldconfig

%files -n libgmime-2_6-0
# NEWS is empty
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_libdir}/*.so.*

%files -n typelib-1_0-GMime-2_6
%{_libdir}/girepository-1.0/GMime-2.6.typelib

%if %{with mono}
%files sharp
%dir %{_prefix}/lib/mono/gmime-sharp-2.6
%dir %{_prefix}/lib/mono/gac/gmime-sharp
%dir %{_prefix}/lib/mono/gac/gmime-sharp/2.6.0.0__2b75c2ad004c52e4
%{_prefix}/lib/mono/gmime-sharp-2.6/gmime-sharp.dll
%{_prefix}/lib/mono/gac/gmime-sharp/2.6.0.0__2b75c2ad004c52e4/gmime-sharp.dll
%{_prefix}/lib/mono/gac/gmime-sharp/2.6.0.0__2b75c2ad004c52e4/gmime-sharp.dll.config
%{_datadir}/gapi-2.0/gmime-api.xml
# devel file:
%{_libdir}/pkgconfig/gmime-sharp-2.6.pc
%endif

%files devel
%doc PORTING
%{_datadir}/gir-1.0/GMime-2.6.gir
%{_includedir}/gmime-2.6
%{_libdir}/*.so
%{_libdir}/pkgconfig/gmime-2.6.pc
%doc %{_datadir}/gtk-doc/html/gmime-2.6/

%changelog
