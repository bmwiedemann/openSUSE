#
# spec file for package freetype
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


Name:           freetype
BuildRequires:  autoconf
BuildRequires:  pkgconfig(x11)
# bug437293
%ifarch ppc64
Obsoletes:      freetype-64bit
%endif
#
PreReq:         fileutils
Version:        1.3.1
Release:        0
Url:            http://www.freetype.org
Summary:        TrueType Font Engine
License:        SUSE-Freetype or GPL-2.0+
Group:          System/Libraries
Source:         ftp://ftp.freetype.org/pub/freetype1/freetype-%{version}.tar.bz2
Source2:        baselibs.conf
Patch0:         freetype-tools-1.3.1.patch
Patch1:         freetype-%{version}.dif
Patch2:         freetype-%{version}-nopatent.patch
Patch3:         freetype-%{version}-gcc.patch
Patch4:         freetype-%{version}-kpathsea.patch
Patch5:         update-config-files.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A library for working with TrueType Fonts. Documentation is in the
/usr/share/doc/packages/freetype directory.

%package -n libttf2
Summary:        TrueType Font Engine
Group:          System/Libraries

%description -n libttf2
A library for working with TrueType Fonts. Documentation is in the
/usr/share/doc/packages/freetype directory.

%package devel
Summary:        Development files for the TrueType Font Engine
Group:          Development/Libraries/C and C++
Requires:       libttf2 = %version

%description devel
A library for working with TrueType Fonts. Documentation is in the
/usr/share/doc/packages/freetype directory.

%package -n freetype-tools
Summary:        Bundled Tests, Demos and Tools for FreeType  (Needed for CJK-LaTeX)
Group:          Development/Libraries/C and C++
Requires:       freetype
Recommends:     texlive-ttfutils

%description -n freetype-tools
Bundled tests, demos and tools for FreeType. Needed for CJK-LaTeX.

The FreeType engine is a free and portable TrueType font rendering
engine. It has been developed to provide TT support to a great variety
of platforms and environments.

This package contains several programs bundled with the FreeType engine
for testing and demonstration purposes as well as some contributed
utilities, such as ttf2bdf, ttf2pfb, and ttfbanner.

%prep
%setup
%patch0 -p1
%patch1
%patch2
%patch3
%patch4
%patch5 -p1

%build
# fix build with newer glibc
sed "s:getline:getline_nonlibc:" -i contrib/*/*.{c,h}
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" 

# Neither %%configure nor %%_smp_mflags is supported in this package..
./configure --prefix=/usr \
                   --with-locale-dir=/usr/share/locale \
		   --libdir=%{_libdir} \
                   %{_target_cpu}-suse-linux-gnu
make 
pushd contrib/ttf2bdf
    ./configure --prefix=/usr --mandir=$RPM_BUILD_ROOT%{_mandir} \
	        --libdir=%{_libdir} \
		%{_target_cpu}-suse-linux-gnu
    make
popd
pushd contrib/ttf2pfb
    ./configure --prefix=/usr --mandir=$RPM_BUILD_ROOT%{_mandir} \
		--libdir=%{_libdir} \
		%{_target_cpu}-suse-linux-gnu
    make
popd
pushd contrib/ttfbanner
    ./configure --prefix=/usr --mandir=$RPM_BUILD_ROOT%{_mandir} \
		--libdir=%{_libdir} \
		%{_target_cpu}-suse-linux-gnu
    make
popd

%install
make prefix=$RPM_BUILD_ROOT/usr \
     libdir=$RPM_BUILD_ROOT/%{_libdir} \
     gnulocaledir=$RPM_BUILD_ROOT/usr/share/locale \
     localedir=$RPM_BUILD_ROOT/usr/share/locale  install
for i in ttf2bdf ttf2pfb ttfbanner; do
    make -C contrib/$i prefix=$RPM_BUILD_ROOT/usr install
done
# copy documentation for freetype-tools:
mkdir -p freetype-tools-doc/ttf2bdf
mkdir -p freetype-tools-doc/ttf2pfb
mkdir -p freetype-tools-doc/ttfbanner
cp contrib/ttf2bdf/README freetype-tools-doc/ttf2bdf
cp contrib/ttf2pfb/TODO freetype-tools-doc/ttf2pfb
cp contrib/ttfbanner/README freetype-tools-doc/ttfbanner
pushd $RPM_BUILD_ROOT/usr/bin
    # rename the utility programs to avoid the name conflict with the same
    # utilities from freetype2:
    rename ft ft1 ft* 
popd
pushd $RPM_BUILD_ROOT/usr/include/freetype
    # Creeate extend sub directory and link all ftx*.h into this directory
    mkdir extend
    cd extend/
    ln -sf ../ftx*.h .
popd
# don't pack t1asm, because this file is in package t1utils:
rm -f $RPM_BUILD_ROOT/usr/bin/t1asm
# don't pack getafm, because it is in the package psutils:
rm -f $RPM_BUILD_ROOT/usr/bin/getafm
rm -f "%buildroot/%_libdir"/*.la
%find_lang %{name}

%post -n libttf2 -p /sbin/ldconfig

%postun -n libttf2 -p /sbin/ldconfig

%post -n freetype-tools
mkdir -p var/adm/SuSEconfig ; touch var/adm/SuSEconfig/run-texhash
test -x usr/bin/texhash && usr/bin/texhash
exit 0

%postun -n freetype-tools
mkdir -p var/adm/SuSEconfig ; touch var/adm/SuSEconfig/run-texhash
test -x usr/bin/texhash && usr/bin/texhash
exit 0

%files -f %{name}.lang
%defattr(-,root,root)
%doc README license.txt docs/FAQ docs/TODO docs/*.txt
/usr/bin/ft1view
/usr/bin/ft1timer
/usr/bin/ft1lint
/usr/bin/ft1dump
/usr/bin/ft1zoom
/usr/bin/ft1string
/usr/bin/ft1strpnm
/usr/bin/ft1error
/usr/bin/ft1metric
/usr/bin/ft1sbit
/usr/bin/ft1strtto

%files -n libttf2
%defattr(-,root,root)
%{_libdir}/libttf.so.2
%{_libdir}/libttf.so.2.2.0

%files devel
%defattr(-,root,root)
/usr/include/freetype
/usr/include/freetype/extend
%{_libdir}/libttf.so

%files -n freetype-tools
%defattr(-, root, root)
%doc ./freetype-tools-doc
/usr/bin/ttf2bdf
/usr/bin/ttf2pfb
/usr/bin/ttfbanner
/usr/share/man/man1/ttf2bdf.1.gz

%changelog
