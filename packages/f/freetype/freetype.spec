#
# spec file for package freetype
#
# Copyright (c) 2020 SUSE LLC
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


Name:           freetype
Version:        1.3.1
Release:        0
Summary:        TrueType Font Engine
License:        SUSE-Freetype OR GPL-2.0-or-later
Group:          System/Libraries
URL:            https://www.freetype.org
Source:         ftp://ftp.freetype.org/pub/freetype1/freetype-%{version}.tar.bz2
Source2:        baselibs.conf
Patch0:         freetype-tools-1.3.1.patch
Patch1:         freetype-%{version}.dif
Patch2:         freetype-%{version}-nopatent.patch
Patch3:         freetype-%{version}-gcc.patch
Patch4:         freetype-%{version}-kpathsea.patch
Patch5:         update-config-files.diff
BuildRequires:  autoconf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
Requires(pre):  fileutils

%description
A library for working with TrueType Fonts. Documentation is in the
%{_docdir}/freetype directory.

%package -n libttf2
Summary:        TrueType Font Engine
Group:          System/Libraries

%description -n libttf2
A library for working with TrueType Fonts. Documentation is in the
%{_docdir}/freetype directory.

%package devel
Summary:        Development files for the TrueType Font Engine
Group:          Development/Libraries/C and C++
Requires:       libttf2 = %{version}

%description devel
A library for working with TrueType Fonts. Documentation is in the
%{_docdir}/freetype directory.

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
%setup -q
%patch0 -p1
%patch1
%patch2
%patch3
%patch4
%patch5 -p1

%build
# fix build with newer glibc
sed "s:getline:getline_nonlibc:" -i contrib/*/*.{c,h}
export CFLAGS="%{optflags} -fno-strict-aliasing -fcommon"

# Neither %%configure nor %%{?_smp_mflags} is supported in this package..
./configure \
  --prefix=%{_prefix} \
  --with-locale-dir=%{_datadir}/locale \
  --libdir=%{_libdir} \
  %{_target_cpu}-suse-linux-gnu
make
pushd contrib/ttf2bdf
./configure \
  --prefix=%{_prefix} \
  --mandir=%{buildroot}%{_mandir} \
  --libdir=%{_libdir} \
  %{_target_cpu}-suse-linux-gnu
make
popd
pushd contrib/ttf2pfb
./configure \
  --prefix=%{_prefix} \
  --mandir=%{buildroot}%{_mandir} \
  --libdir=%{_libdir} \
  %{_target_cpu}-suse-linux-gnu
make
popd
pushd contrib/ttfbanner
./configure \
  --prefix=%{_prefix} \
  --mandir=%{buildroot}%{_mandir} \
  --libdir=%{_libdir} \
  %{_target_cpu}-suse-linux-gnu
make
popd

%install
make prefix=%{buildroot}%{_prefix} \
     libdir=%{buildroot}/%{_libdir} \
     gnulocaledir=%{buildroot}%{_datadir}/locale \
     localedir=%{buildroot}%{_datadir}/locale  install
for i in ttf2bdf ttf2pfb ttfbanner; do
    make -C contrib/$i prefix=%{buildroot}%{_prefix} install
done
# copy documentation for freetype-tools:
mkdir -p freetype-tools-doc/ttf2bdf
mkdir -p freetype-tools-doc/ttf2pfb
mkdir -p freetype-tools-doc/ttfbanner
cp contrib/ttf2bdf/README freetype-tools-doc/ttf2bdf
cp contrib/ttf2pfb/TODO freetype-tools-doc/ttf2pfb
cp contrib/ttfbanner/README freetype-tools-doc/ttfbanner
pushd %{buildroot}%{_bindir}
    # rename the utility programs to avoid the name conflict with the same
    # utilities from freetype2:
    rename ft ft1 ft*
popd
pushd %{buildroot}%{_includedir}/freetype
    # Creeate extend sub directory and link all ftx*.h into this directory
    mkdir extend
    cd extend/
    ln -sf ../ftx*.h .
popd
# don't pack t1asm, because this file is in package t1utils:
rm -f %{buildroot}%{_bindir}/t1asm
# don't pack getafm, because it is in the package psutils:
rm -f %{buildroot}%{_bindir}/getafm
find %{buildroot} -type f -name "*.la" -delete -print
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
%license license.txt
%doc README docs/FAQ docs/TODO docs/*.txt
%{_bindir}/ft1view
%{_bindir}/ft1timer
%{_bindir}/ft1lint
%{_bindir}/ft1dump
%{_bindir}/ft1zoom
%{_bindir}/ft1string
%{_bindir}/ft1strpnm
%{_bindir}/ft1error
%{_bindir}/ft1metric
%{_bindir}/ft1sbit
%{_bindir}/ft1strtto

%files -n libttf2
%{_libdir}/libttf.so.2
%{_libdir}/libttf.so.2.2.0

%files devel
%{_includedir}/freetype
%{_includedir}/freetype/extend
%{_libdir}/libttf.so

%files -n freetype-tools
%doc ./freetype-tools-doc
%{_bindir}/ttf2bdf
%{_bindir}/ttf2pfb
%{_bindir}/ttfbanner
%{_mandir}/man1/ttf2bdf.1%{?ext_man}

%changelog
