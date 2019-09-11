#
# spec file for package VFlib3
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libVFlib3-5
Name:           VFlib3
Version:        3.6.14
Release:        0
Summary:        Versatile Font Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Summary(ja):    "Versatile" フォントライブラリ
Url:            http://www-masu.ist.osaka-u.ac.jp/~kakugawa/VFlib/
Source0:        http://www-masu.ist.osaka-u.ac.jp/~kakugawa/download/TypeHack/VFlib3-%{version}.tar.bz2
Source1:        vflibcap-tex
Patch0:         VFlib3-compare-always-false.patch
Patch1:         VFlib3-freetype2.patch
Patch2:         VFlib3-gnu_source-declaration.patch
Patch3:         VFlib3-include.patch
Patch4:         VFlib3-info-dir.patch
BuildRequires:  autoconf213
BuildRequires:  fdupes
BuildRequires:  imake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(kpathsea)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Requires(post): %{install_info_prereq}
Requires(postun): %{install_info_prereq}

%description -l ja
VFlib は C 言語で書かれたフォントライブラリで、指定したフォン
トのビットマップを得るための関数群を持っています。VFlib の特徴は、
さまざまなフォーマットのフォントをフォーマットの違いを気にする
ことなく統一的に使うことができるところにあります。

VFlib では、以下のフォントフォーマットがサポートされています。
     TeX 関連:       PK, GF, VF, TFM
     Omega TeX 関連: OFM (レベル 0),OVF
     X Window 関連:  PCF, BDF

%description
VFlib is a font library written in C language with several functions to
obtain bitmaps of fonts. A unique feature of VFlib is that fonts in
different formats are accessed by unified interface.

VFlib supports the following font formats:
* TeX fonts: PK, GF, VF, TFM Omega
* TeX fonts: OFM (level 0), OVF
* X Window fonts: PCF, BDF.
* Other fonts: TrueType, Type 1, HBF, Syotai Club, JG, ekanji

%package -n %{libname}
Summary:        Versatile font library VFlib3
Group:          System/Libraries

%description -n %{libname}
VFlib is a font library written in C language with several functions to
obtain bitmaps of fonts. A unique feature of VFlib is that fonts in
different formats are accessed by unified interface.

VFlib supports the following font formats:
* TeX fonts: PK, GF, VF, TFM Omega
* TeX fonts: OFM (level 0), OVF
* X Window fonts: PCF, BDF.
* Other fonts: TrueType, Type 1, HBF, Syotai Club, JG, ekanji

%package -n VFlib3-devel
Summary:        Development libraries for VFlib3
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(kpathsea)

%description -n VFlib3-devel
Development headers and libraries for VFlib3

%prep
%setup -q
%autopatch -p1

# libtool files must be having proper content
rm -f config.{cache,sub,guess}
ln -s %{_datadir}/libtool/build-aux/config.guess ./
ln -s %{_datadir}/libtool/build-aux/config.sub ./

%build
autoconf-2.13
%configure \
            --with-kpathsea \
            --with-freetype2 \
            --with-freetype2-includedir=%{_includedir}/freetype2 \
            --with-texmf-root=%{_datadir}/texmf \
            --with-gettext
make %{?_smp_mflags}

%install
make prefix=%{buildroot}%{_prefix} \
     infodir=%{buildroot}%{_infodir} \
     mandir=%{buildroot}%{_mandir} \
     includedir=%{buildroot}%{_includedir} \
     libdir=%{buildroot}%{_libdir} \
     bindir=%{buildroot}%{_bindir} \
     datadir=%{buildroot}%{_datadir} \
     runtimedir=%{buildroot}%{_datadir}/VFlib/%{version} \
     install
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/VFlib/%{version}/
# remove duped docs
rm -rf %{buildroot}%{_datadir}/VFlib/%{version}/doc/
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/VFlib-36.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/VFlib-36.info%{ext_info}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc ANNOUNCE* CHANGES COPYING* DISTRIB*
%{_infodir}/VFlib*info*
%dir %{_datadir}/VFlib
%dir %{_datadir}/VFlib/%{version}
%dir %{_datadir}/VFlib/%{version}/t1lib/
%{_datadir}/VFlib/%{version}/t1lib/*
%dir %{_datadir}/VFlib/%{version}/ccv/
%{_datadir}/VFlib/%{version}/ccv/*
%dir %{_datadir}/VFlib/%{version}/ascii-jtex/
%{_datadir}/VFlib/%{version}/ascii-jtex/*
%{_datadir}/VFlib/%{version}/vflibcap*
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libVFlib3.so.*

%files -n VFlib3-devel
%{_libdir}/libVFlib3.so
%{_includedir}/*

%changelog
