#
# spec file for package lilypond
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


%define fontdir %{_datadir}/fonts
%define ttfdir  %{fontdir}/truetype
%define ver %(echo %{version} | cut -d . -f 1,2)

Name:           lilypond
Version:        2.20.0
Release:        0
Summary:        A typesetting system for music notation
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Other
URL:            http://www.lilypond.org
Source0:        https://lilypond.org/download/sources/v2.20/lilypond-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://savannah.gnu.org/patch/index.php?9370
Patch0:         reproducible.patch
# Patches taken from Debian, see headers for info.
Patch1:         0101-read_relocation_dir-in-lilypond_datadir-too.patch
Patch2:         add_dircategories_to_documentation.patch
Patch3:         Issue-5243-1-editor-scm-Add-shell-quote-argument-function.diff
Patch4:         use_cstring_and_ctype_includes.patch
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  dblatex
BuildRequires:  dejavu-fonts
BuildRequires:  flex
BuildRequires:  fontforge
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ghostscript >= 8.15
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  libguile1-devel >= 1.8
BuildRequires:  makeinfo >= 6.1
BuildRequires:  mftrace >= 1.1.19
BuildRequires:  potrace-devel
# Needed for pngtopnm
BuildRequires:  netpbm
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  t1utils
#BuildRequires:  texi2html4
BuildRequires:  texinfo4
BuildRequires:  texlive-extratools
BuildRequires:  texlive-filesystem
BuildRequires:  texlive-latex
BuildRequires:  texlive-lh
BuildRequires:  texlive-metafont
BuildRequires:  texlive-metapost
BuildRequires:  texlive-tex-gyre-fonts
BuildRequires:  vim-base
BuildRequires:  zip
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pango) >= 1.12.0
BuildRequires:  pkgconfig(python3)
# This is a work around for boo#1163190 pango-devel doesn't pull in cairo-devel although it requires it
BuildRequires:  pkgconfig(cairo)
Requires(post): %install_info_prereq
Requires(preun): %install_info_prereq
Requires:       ghostscript >= 8.15
Requires:       lilypond-fonts-common = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

%package texgy-fonts
Summary:        Lilypond Century Schoolbook L fonts
Group:          System/X11/Fonts
BuildArch:      noarch

%description texgy-fonts
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.
These are the lilypond Texgy fonts.

%package emmentaler-fonts
Summary:        Lilypond emmentaler fonts
Group:          System/X11/Fonts
BuildArch:      noarch

%description emmentaler-fonts
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.
These are the lilypond emmentaler fonts.

%package fonts-common
Summary:        Lilypond fonts common dir
Group:          System/X11/Fonts
BuildArch:      noarch
Requires:       lilypond-emmentaler-fonts = %{version}
Requires:       lilypond-texgy-fonts = %{version}

%description fonts-common
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.
This contains the directory common to all lilypond fonts.

%prep
%setup -q
%autopatch -p1

pushd scripts
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done
cd ../python
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done
popd
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done

%build
export LIBS="$LIBS  -lglib-2.0 -lgobject-2.0"
export TEXI2HTML=/usr/bin/texi2html4
export TEXI2PDF=/usr/bin/texi2pdf4
export TEXINDEX=/usr/bin/texindex4

%configure \
	--disable-checking
# Build sometimes fails with multiple threads.
make %{_smp_mflags} || make -j1

%install
vimver=$(vim --version | head -n1 | grep -Po "\d\.\d" | sed 's|\.||')
%make_install package_infodir=%{_infodir} \
	vimdir="%{_datadir}/vim/vim$vimver"

# Symlink lilypond-init.el in emacs' site-start.d directory
pushd %{buildroot}%{_datadir}/emacs/site-lisp
mkdir site-start.d
ln -s ../lilypond-init.el site-start.d
popd

# Change encoding to UTF8
pushd %{buildroot}%{_infodir}
iconv -f iso-8859-1 -t utf-8 music-glossary.info > music-glossary.info.utf8
mv music-glossary.info.utf8 music-glossary.info
sed -e s,lilypond/,, -i *.info
popd

rm -f %{buildroot}%{_infodir}/dir

chmod 0755  %{buildroot}%{_datadir}/lilypond/2.20.0/python/langdefs.py

%find_lang %{name}

mkdir -p %{buildroot}%{ttfdir}
mv %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf/*.otf %{buildroot}%{ttfdir}
rmdir %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf
ln -s %{ttfdir} %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf

%post
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-changes.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-contributor.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-essay.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-extending.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-internals.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-learning.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-notation.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-usage.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/lilypond-web.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-changes.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-contributor.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-essay.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-extending.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-internals.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-learning.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-notation.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-usage.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/lilypond-web.info.gz

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS.txt DEDICATION HACKING
%doc NEWS.txt README.txt ROADMAP VERSION
%license COPYING LICENSE*
%{_bindir}/*
%{_libdir}/lilypond
%{_datadir}/lilypond
%{_datadir}/emacs/site-lisp
%{_datadir}/vim/vim*
%{_infodir}/*%{ext_info}
%{_mandir}/man1/*

%files texgy-fonts
%defattr(-,root,root,-)
%{ttfdir}/texgy*otf

%files emmentaler-fonts
%defattr(-,root,root,-)
%{ttfdir}/emmentaler*otf

%files fonts-common
%defattr(-,root,root,-)
%license COPYING
%defattr(0644,root,root,0755)
%dir %{ttfdir}

%changelog
