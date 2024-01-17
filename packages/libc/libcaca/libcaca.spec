#
# spec file for package libcaca
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libcaca
Version:        0.99.beta20
Release:        0
Summary:        Library for Colour ASCII Art, text mode graphics
License:        WTFPL
Group:          Development/Languages/C and C++
URL:            http://caca.zoy.org
Source0:        https://github.com/cacalabs/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         libcaca-0.99-texbuild.patch
Patch2:         libcaca-X11_test.patch
Patch4:         libcaca-ruby_am_cflags.patch
Patch5:         libcaca-ruby_vendor_install.patch
Patch7:         libcaca-0.99.beta16-missing-GLU.patch
Patch9:         caca-no-build-date.patch
Patch10:        libcaca-ncurses6.patch
Patch13:        Bug1143286_libcaca_configure_ac_chg_for_lto.patch
Patch99:        bsc1184751-add-space-for-NUL-byte.patch
# PATCH-FIX-UPSTREAM correctly-handle-zero-width-or-height-images.patch bsc#1197028
Patch100:       bsc1197028-correctly-handle-zero-width-or-height-images.patch
Patch101:       libcaca-autoconf-2.69.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(slang)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)

%description
libcaca is the Colour AsCii Art library. It provides high level
functions for colour text drawing, simple primitives for line, polygon
and ellipse drawing, as well as powerful image to text conversion
routines.

%package -n libcaca0
Summary:        Library for Colour ASCII Art, text mode graphics
Group:          Development/Languages/C and C++
Provides:       libcaca = %{version}
Obsoletes:      libcaca < %{version}

%description -n libcaca0
libcaca is the Colour AsCii Art library. It provides high level
functions for colour text drawing, simple primitives for line, polygon
and ellipse drawing, as well as powerful image to text conversion
routines.

%package devel
Summary:        Library for Colour ASCII Art, text mode graphics
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}0-plugins = %{version}

%description devel
This package contains the header files and static libraries needed to
compile applications or shared objects that use libcaca.

%package -n python3-caca
Summary:        Python3 support for libcaca
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
BuildArch:      noarch

%description -n python3-caca
This package contains all that is needed to use libcaca from python3.

%package -n libcaca0-plugins
Summary:        Plugins for libcaca
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description -n libcaca0-plugins
This package contains gl and x11 plugins for caca.

%package ruby
Summary:        Ruby bindings for libcaca
Group:          Development/Languages/Ruby
Requires:       %{name} = %{version}
Requires:       ruby

%description ruby
All that is needed to use libcaca from ruby code.

%package -n caca-utils
Summary:        Colour ASCII Art Text mode graphics utilities based on libcaca
Group:          Amusements/Toys/Graphics
Requires:       imlib2-loaders
Requires:       toilet

%description -n caca-utils
This package contains utilities and demonstration programs for libcaca,
the Colour AsCii Art library.

cacaview is a simple image viewer for the terminal. It opens most image
formats such as JPEG, PNG, GIF etc. and renders them on the terminal
using ASCII art. The user can zoom and scroll the image, set the
dithering method or enable anti-aliasing.

cacaball is a tiny graphic program that renders animated ASCII
metaballs on the screen, cacafire is a port of AALib's aafire and
displays burning ASCII art flames, and cacademo is a simple application
that shows the libcaca rendering features such as line and ellipses
drawing, triangle filling and sprite blitting.

%prep
%setup -q
%patch2
%patch4
%patch5
%patch7
%patch9
%patch1
%patch10 -p1
%patch13 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
RUBY="ruby-`echo %{rb_ver} | sed 's|\.[^\.]*$||'`"
find . -type f -exec sed -i "s|ruby-1.9|$RUBY|" \{\} \;
pushd python
#Change python script headers to python3
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done
popd

%build
autoreconf -fvi
export CFLAGS="$CFLAGS %{optflags} -I../caca/"
export CXXFLAGS="$CXXFLAGS %{optflags}"
%configure \
    --enable-slang \
    --enable-ncurses \
    --enable-x11 \
    --enable-imlib2 \
    --enable-gl \
    --enable-csharp=no \
    --enable-doc \
    --enable-shared=yes \
    --enable-static=no \
    --enable-conio=no \
    --enable-plugins \
    --enable-java=no \
    --enable-python
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}%{_mandir}/
%fdupes -s %{buildroot}%{python3_sitelib}

%post -n libcaca0 -p /sbin/ldconfig
%postun -n libcaca0 -p /sbin/ldconfig
%post -n libcaca0-plugins -p /sbin/ldconfig
%postun -n libcaca0-plugins -p /sbin/ldconfig

%files -n libcaca0
%doc AUTHORS NEWS NOTES README THANKS
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_datadir}/doc/libcaca-dev
%dir %{_libdir}/caca
%{_libdir}/*.so
%{_libdir}/caca/libx11_plugin.so
%{_libdir}/caca/libgl_plugin.so
%{_bindir}/caca-config
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_mandir}/man1/caca-config.1%{?ext_man}
%{_mandir}/man3/*

%files ruby
%{rb_vendorarch}/*
%{rb_vendorlib}/caca.rb

%files -n python3-caca
%{python3_sitelib}/*

%files -n libcaca0-plugins
%dir %{_libdir}/caca
%{_libdir}/caca/libgl_plugin.so.0
%{_libdir}/caca/libgl_plugin.so.0.0.0
%{_libdir}/caca/libx11_plugin.so.0
%{_libdir}/caca/libx11_plugin.so.0.0.0

%files -n caca-utils
%{_bindir}/cacademo
%{_bindir}/cacafire
%{_bindir}/cacaview
%{_bindir}/cacaplay
%{_bindir}/cacaclock
%{_bindir}/cacaserver
%{_bindir}/img2txt
%{_datadir}/libcaca
%{_mandir}/man1/cacademo.1%{?ext_man}
%{_mandir}/man1/cacafire.1%{?ext_man}
%{_mandir}/man1/cacaview.1%{?ext_man}
%{_mandir}/man1/cacaplay.1%{?ext_man}
%{_mandir}/man1/cacaserver.1%{?ext_man}
%{_mandir}/man1/img2txt.1%{?ext_man}

%changelog
