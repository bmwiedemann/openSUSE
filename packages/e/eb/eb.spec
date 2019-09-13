#
# spec file for package eb
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 16
Name:           eb
Version:        4.4.3
Release:        0
Summary:        C Library for Accessing CD-ROM Books
License:        GPL-2.0+
Group:          System/Libraries
Url:            https://github.com/aehlke/eb
Source:         ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.bz2
Patch:          gettext.patch
BuildRequires:  libtool
BuildRequires:  zlib-devel
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Summary(ja): EB ライブラリは CD-ROM 書籍にアクセスするための C のライブラリです。
# %description -l ja
# EB ライブラリは CD-ROM 書籍にアクセスするための C のライブラリです。
# UNIX 系 OS のシステム上で動作させることができます。EB, EBG, EBXA, EBXA-C,
# S-EBXA および EPWING 形式の CD-ROM 書籍に対応しています。これらの形式の
# CD-ROM 書籍は、日本で一般的に使われています。CD-ROM 書籍自体は ISO 9660
# 形式になっていますので、他の ISO 9660 形式と同じ要領でマウントすること
# ができます。
#
# 著者:
# ----
#     Motoyuki Kasahara <m-kasahr@sra.co.jp>

%description
EB Library is a C library for accessing CD-ROM books.  It can be built
on UNIX-based systems.	EB Library supports accessing CD-ROM books in
EB, EBG, EBXA, EBXA-C, S-EBXA, and EPWING formats.  CD-ROM books in
those formats are popular in Japan.  Because CD-ROM books themselves
are based on the ISO 9660 format, you can mount the CDs in the same way
as other ISO 9660 CDs.

%package -n libeb%{soname}
Summary:        C Library for Accessing CD-ROM Books - shared library
Group:          System/Libraries

%description -n libeb%{soname}
EB Library is a C library for accessing CD-ROM books.  It can be built
on UNIX-based systems.	EB Library supports accessing CD-ROM books in
EB, EBG, EBXA, EBXA-C, S-EBXA, and EPWING formats.  CD-ROM books in
those formats are popular in Japan.  Because CD-ROM books themselves
are based on the ISO 9660 format, you can mount the CDs in the same way
as other ISO 9660 CDs.

%package devel
Summary:        EB Header Files and Libraries
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Obsoletes:      ebdev < %{version}-%{release}
Provides:       ebdev = %{version}-%{release}
# %description -n ebdev -l ja
# EB ライブラリのヘッダファイル及びライブラリです。

%description devel
EB header files and libraries.

%lang_package

%prep
%setup -q
%patch -p1

%build
autoreconf -fi
%configure \
	--with-zlib-libraries=/%{_lib} \
	--with-zlib-includes=%{_includedir} \
	--disable-static \
	--with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}
%find_lang ebutils %{name}.lang
rm -rf %{buildroot}%{_libdir}/libeb.la

%post -n libeb%{soname} -p /sbin/ldconfig

%postun -n libeb%{soname} -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README* ChangeLog*
%{_bindir}/ebappendix
%{_bindir}/ebfont
%{_bindir}/ebinfo
%{_bindir}/ebrefile
%{_bindir}/ebstopcode
%{_bindir}/ebunzip
%{_bindir}/ebzip
%{_bindir}/ebzipinfo
%{_datadir}/eb/
%config %{_sysconfdir}/eb.conf

%files devel
%defattr(-, root, root)
%{_includedir}/eb
%{_libdir}/libeb.so
%{_datadir}/aclocal/eb4.m4

%files -n libeb%{soname}
%defattr(-, root, root)
%{_libdir}/libeb.so.%{soname}
%{_libdir}/libeb.so.%{soname}.0.0

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
