#
# spec file for package racket
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012, 2013 Togan Muftuoglu toganm@opensuse.org
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


Name:           racket
Version:        8.7
Release:        0
Summary:        Scheme implementation with teaching tools
License:        Apache-2.0 OR MIT
Group:          Development/Languages/Scheme
URL:            http://racket-lang.org
Source0:        http://download.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz
Source2:        racket-completion.bash
Source3:        racket-rpmlintrc
Source4:        config.sub
Patch0:         racket-doc.patch
BuildRequires:  ImageMagick
BuildRequires:  ca-certificates
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-fonts-std
BuildRequires:  google-roboto-fonts
BuildRequires:  libexpat1
BuildRequires:  libjpeg-devel
BuildRequires:  librsvg-devel
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1) >= 0.22.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
# The rpmbuild does not detect those!
Requires:       libcairo2
Requires:       libedit0
Requires:       libglib-2_0-0
Requires:       libgtk-3-0
Requires:       libpango-1_0-0
Requires:       libsqlite3-0
Provides:       %{name}-drracket = %{version}-%{release}
Provides:       %{name}-games = %{version}-%{release}
Provides:       %{name}-webserver = %{version}-%{release}
Recommends:     racket-doc = %{version}-%{release}

%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

# maggia has this
# Disable the debug package since otherwise a build would create the following
# error message:
#  *** ERROR: same build ID in nonidentical files!
#          /usr/bin/mzscheme
#     and  /usr/bin/mred
# this should be set from the obs
#%%define debug_package %%nil

%description
Racket (formerly called PLT Scheme) is a multi-paradigm programming language
in the Lisp/Scheme family, that also serves as a platform for language
creation, design, and implementation.

The programming language is known for its powerful macro system which enables
the creation of embedded and domain-specific languages, language constructs
such as classes or modules, and separate dialects of Racket enable different
semantics.

%package        doc
Summary:        Documentation HTML files for Racket
Group:          Development/Languages/Scheme
Provides:       %{name}:%{_docdir}/%{name}/docindex.sqlite
BuildArch:      noarch

%description    doc
A local installation of the Racket documentation system.

%package devel
Summary:        Development header files for Racket
Group:          Development/Languages/Scheme
Requires:       %{name} = %{version}-%{release}
Requires:       glibc-devel
Requires:       libffi-devel
Recommends:     %{name}-doc = %{version}-%{release}

%description devel
This package contains the symlinks, headers and object files needed to
compile and link programs which use Racket.

%prep
%setup -q
%patch0 -p0

cp -p %{SOURCE2} src/
# gh#4520
cp -p %{SOURCE4} src/lt

%build
cd src/

%add_optflags -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=500 -fno-gcse -Wno-stringop-overread
%configure \
    --prefix="%{_prefix}" \
    --exec-prefix="%{_prefix}" \
    --libdir=%{_libdir} \
    --docdir="%{_defaultdocdir}/%{name}" \
    --enable-shared \
%ifarch ppc64 ppc64le s390x
    --enable-bcdefault \
%endif
    --disable-static \
    --disable-strip \
    --enable-places \
    --enable-lt="%{_bindir}/libtool" \
    --enable-libz \
    --enable-liblz4 \
    --enable-pthread
%make_build

%install
cd src/

# use the following if setting extra plt_setup options
# export LD_LIBRARY_PATH=%%{buildroot}%%{_libdir}
# export PLT_SETUP_OPTIONS="-j 1 "

install -d %{buildroot}/%{_datadir}/doc/%{name}/

%make_install

# we do not need *.la and *.a files
find %{buildroot}%{_libdir} -name "*.la" -delete
find %{buildroot}%{_libdir} -name "*.a" -delete

# make system clear
for bin in mred mzscheme racket
do
    test -e $bin || continue
    chrpath --delete %{buildroot}%{_bindir}/$bin || :
done
for bin in gracket starter
do
    test -e $bin || continue
    chrpath --delete %{buildroot}%{_libdir}/$bin || :
done
for bin in c-printf crypt esd magick sndfile tcl xmmsctrl xosd
do
    bin=%{buildroot}%{_datadir}/%{name}/pkgs/racket-doc/ffi/examples/use-${bin}.rkt
    test -e $bin || continue
    sed -ri '1s@(/usr/bin/)env +@\1@p' $bin
    chmod 755 $bin
done

files_to_filter="
syntax/module-helpers
rackunit/api
reference/collects
guide/exns
math/array_broadcasting
math/array_construct
math/array_convert
math/array_fold
math/array_indexing
math/array_nonstrict
math/array_pointwise
math/array_quick
math/array_sequences
math/array_slicing
math/array_strict
math/array_transform
math/array_types
math/matrix_construction
math/matrix_intro
math/matrix_poly
math/stats
ts-reference/Typed_Classes
"
for html in $files_to_filter
do
    html=%{buildroot}%{_docdir}/%{name}/${html}.html
    test -e $html || continue
    sed -ri 's@%{buildroot}@@g' $html
done

# Bash completion
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/bash_completion/completions/%{name}
install -Dm 644 %{_builddir}/%{name}-%{version}/share/pkgs/drracket/drracket/drracket.png %{buildroot}%{_datadir}/pixmaps/drracket.png

# rewrite path in .desktop files
%suse_update_desktop_file -c drracket "DrRacket" "DrRacket is an interactive, integrated, graphical programming environment for the Racket programming languages" "%{_bindir}/drracket" "drracket" Development IDE
%suse_update_desktop_file -c slideshow "Slideshow" "Slideshow is a Racket-based tool for writing slide presentations as programs" "%{_bindir}/slideshow" "drracket" Development Documentation

# Due package split we do this explicit to support older rpm version as well
install -m 0644 ../README %{buildroot}%{_docdir}/%{name}/README

%fdupes %{buildroot}%{_prefix}

%post
/sbin/ldconfig
%desktop_database_post

%postun
/sbin/ldconfig
%desktop_database_postun

%files
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README
%{_bindir}/drracket
%{_bindir}/gracket
%{_bindir}/gracket-text
%{_bindir}/mred
%{_bindir}/mred-text
%{_bindir}/mzc
%{_bindir}/mzpp
%{_bindir}/mzscheme
%{_bindir}/mztext
%{_bindir}/pdf-slatex
%{_bindir}/plt-games
%{_bindir}/plt-help
%{_bindir}/plt-r5rs
%{_bindir}/plt-r6rs
%{_bindir}/plt-web-server
%{_bindir}/racket
%{_bindir}/raco
%{_bindir}/scribble
%{_bindir}/setup-plt
%{_bindir}/slatex
%{_bindir}/slideshow
%{_bindir}/swindle
%{_libdir}/%{name}/starter
%{_libdir}/%{name}/gracket
%{_libdir}/%{name}/starter-sh
%verify(not md5 size mtime) %{_libdir}/%{name}/*.rktd
%dir %{_libdir}/%{name}/compiled/
%{_libdir}/%{name}/compiled/*
%ifnarch ppc64 ppc64le s390x
%{_libdir}/%{name}/petite.boot
%{_libdir}/%{name}/racket.boot
%{_libdir}/%{name}/scheme.boot
%endif
%ifarch ppc64 ppc64le s390x
%{_libdir}/libracket3m*
%{_libdir}/%{name}/buildinfo
%{_libdir}/%{name}/mzdyn3m.lo
%endif
%{_mandir}/man1/mz*
%{_mandir}/man1/racket*
%{_mandir}/man1/raco*
%{_mandir}/man1/setup-plt*
%{_mandir}/man1/drracket*
%{_mandir}/man1/gracket*
%{_mandir}/man1/mred*
%{_mandir}/man1/plt-help*
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/bash_completion
%dir %{_datadir}/bash_completion/completions
%{_datadir}/bash_completion/completions/%{name}
%{_datadir}/applications/drracket.desktop
%{_datadir}/applications/slideshow.desktop
%{_datadir}/pixmaps/drracket.png
%exclude %dir %{_datadir}/%{name}/pkgs/mzscheme-lib/mzscheme/examples/
%exclude %{_datadir}/%{name}/pkgs/mzscheme-lib/mzscheme/examples/*.c*
%verify(not md5 size mtime) %{_datadir}/%{name}/*.rktd
%verify(not md5 size mtime) %{_datadir}/%{name}/pkgs/*.rktd
%{_datadir}/%{name}/*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/config.rktd

%files doc
%doc %{_docdir}/%{name}/*
%exclude %{_docdir}/%{name}/README

%files devel
%{_includedir}/%{name}/*
%dir %{_includedir}/%{name}
%dir %{_datadir}/%{name}/pkgs/mzscheme-lib/mzscheme/examples/
%{_datadir}/%{name}/pkgs/mzscheme-lib/mzscheme/examples/*.c*

%changelog
