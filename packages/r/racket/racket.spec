#
# spec file for package racket
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        7.3
Release:        0
Summary:        Scheme implementation with teaching tools
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Development/Languages/Scheme
URL:            http://racket-lang.org
Source0:        http://download.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz
Source2:        racket-completion.bash
Source3:        racket-rpmlintrc
Patch0:         racket-doc.patch
Patch1:         dont-strip.patch
BuildRequires:  ImageMagick
BuildRequires:  ca-certificates
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-fonts-std
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
BuildRequires:  pkgconfig(libpng)
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

%description devel
This package contains the symlinks, headers and object files needed to
compile and link programs which use Racket.


%prep
%setup -q
%patch0 -p0
%patch1 -p1

cp -p %{SOURCE2} src/

%build
cd src/

%add_optflags -D_DEFAULT_SOURCE -D_XOPEN_SOURCE=500 -fno-gcse
%configure  --prefix="%{_datadir}" --docdir="%{_defaultdocdir}/%{name}" --enable-shared \
    --disable-static --disable-strip --enable-places --enable-lt="%{_bindir}/libtool" \
    --enable-pthread

make %{?_smp_mflags} VERBOSE=1

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
find %{buildroot}%{_datadir} -name ".LOCKpkgs.rktd" -delete

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
chmod 755 %{buildroot}%{_datadir}/%{name}/pkgs/htdp-lib/2htdp/uchat/xrun

for html in syntax/module-helpers rackunit/api reference/collects
do
    html=%{_docdir}/%{name}/${html}.html
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
%{_libdir}/libracket3m-%{version}.so
%{_libdir}/%{name}/mzdyn3m.o
%{_datadir}/%{name}/*
%{_libdir}/%{name}/starter
%{_libdir}/%{name}/gracket
%{_libdir}/%{name}/starter-sh
%{_libdir}/%{name}/*.rktd
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
%dir %{_sysconfdir}/%{name}
%{_datadir}/bash_completion/completions/%{name}
%config %{_sysconfdir}/%{name}/config.rktd
%{_datadir}/applications/drracket.desktop
%{_datadir}/applications/slideshow.desktop
%{_datadir}/pixmaps/drracket.png
%exclude %{_datadir}/%{name}/pkgs/mzscheme-lib/mzscheme/examples/*

%files doc
%doc %{_docdir}/%{name}/*
%exclude %{_docdir}/%{name}/README

%files devel
%{_includedir}/%{name}/*
%{_libdir}/%{name}/buildinfo
%{_libdir}/libracket3m.so
%dir %{_includedir}/%{name}
%{_datadir}/%{name}/pkgs/mzscheme-lib/mzscheme/examples/*

%changelog
