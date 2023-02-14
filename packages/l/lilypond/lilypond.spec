#
# spec file for package lilypond
#
# Copyright (c) 2023 SUSE LLC
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
#Unsatisfied dependency for Factory i586
ExcludeArch:    i586

Name:           lilypond
Version:        2.24.1
Release:        0
Summary:        A typesetting system for music notation
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Other
URL:            http://www.lilypond.org
Source0:        https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/lilypond-v%{version}.tar.bz2
Source1:        https://gitlab.com/lilypond/lilypond/-/releases/v%{version}/downloads/lilypond-%{version}-documentation.tar.xz
# PATCH-FIX-UPSTREAM https://savannah.gnu.org/patch/index.php?9370
Patch0:         reproducible.patch
# Patches taken from Debian, see headers for info.
#Patch1:         0101-read_relocation_dir-in-lilypond_datadir-too.patch
Patch2:         add_dircategories_to_documentation.patch
Patch4:         use_cstring_and_ctype_includes.patch
Patch5:         lilypond-missing-lgc.patch
BuildRequires:  ImageMagick
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  dblatex
BuildRequires:  dejavu-fonts
BuildRequires:  extractpdfmark
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  fontforge
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ghostscript >= 8.15
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  makeinfo >= 6.1
BuildRequires:  mc
BuildRequires:  mftrace >= 1.1.19
BuildRequires:  potrace-devel
BuildRequires:  t1utils
BuildRequires:  texlive-fontinst-bin
BuildRequires:  texlive-fontware-bin
BuildRequires:  pkgconfig(guile-3.0)
# Needed for pngtopnm
BuildRequires:  netpbm
BuildRequires:  pkgconfig
BuildRequires:  rsync
BuildRequires:  t1utils
BuildRequires:  texi2html
BuildRequires:  texinfo
#BuildRequires:  texinfo4
BuildRequires:  texlive-bibtex-bin
BuildRequires:  texlive-extratools
BuildRequires:  texlive-filesystem
BuildRequires:  texlive-latex
BuildRequires:  texlive-lh
BuildRequires:  texlive-metafont
BuildRequires:  texlive-metapost
BuildRequires:  texlive-tex-gyre-fonts
BuildRequires:  vim-base
BuildRequires:  zip
BuildRequires:  pkgconfig(bdw-gc)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pango) >= 1.12.0
BuildRequires:  pkgconfig(python3)
# This is a work around for boo#1163190 pango-devel doesn't pull in cairo-devel although it requires it
BuildRequires:  pkgconfig(cairo)
Requires:       ghostscript >= 8.15
Requires:       lilypond-fonts-common = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

%package doc
Summary:        Documentation for the LilyPond Typesetter
License:        GFDL-1.3-only
Group:          Documentation/HTML
Provides:       lilypond-documentation = %{version}
Obsoletes:      lilypond-documentation < %{version}
BuildArch:      noarch

%description doc
Common and english documentation files for the
GNU LilyPond music typesetter.

%package doc-cs
Summary:        Documentation for the LilyPond Typesetter (cs)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-cs
Czech documentation files for the GNU LilyPond music typesetter.

%package doc-de
Summary:        Documentation for the LilyPond Typesetter (de)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-de
German documentation files for the GNU LilyPond music typesetter.

%package doc-es
Summary:        Documentation for the LilyPond Typesetter (es)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-es
Spanish documentation files for the GNU LilyPond music typesetter.

%package doc-fr
Summary:        Documentation for the LilyPond Typesetter (fr)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-fr
French documentation files for the GNU LilyPond music typesetter.

%package doc-hu
Summary:        Documentation for the LilyPond Typesetter (hu)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-hu
Hungary documentation files for the GNU LilyPond music typesetter.

%package doc-it
Summary:        Documentation for the LilyPond Typesetter (it)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-it
Italian documentation files for the GNU LilyPond music typesetter.

%package doc-ja
Summary:        Documentation for the LilyPond Typesetter (ja)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-ja
Japanese documentation files for the GNU LilyPond music typesetter.

%package doc-nl
Summary:        Documentation for the LilyPond Typesetter (nl)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-nl
Dutch documentation files for the GNU LilyPond music typesetter.

%package doc-zh
Summary:        Documentation for the LilyPond Typesetter (zh)
Group:          Documentation/HTML
Requires:       %{name}-doc = %{version}
BuildArch:      noarch

%description doc-zh
Chinese documentation files for the GNU LilyPond music typesetter.

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

%description fonts-common
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.
This contains the directory common to all lilypond fonts.

%prep
%setup -q -n lilypond-v%{version}
%autopatch -p1

pushd scripts
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done
cd ../python
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done
popd
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done

%build
export LIBS="$LIBS  -lglib-2.0 -lgobject-2.0"
export GUILE_FLAVOR=guile-3.0
./autogen.sh --noconfigure
%configure \
    GUILE_FLAVOR=guile-3.0 \
	--disable-checking
# Build sometimes fails with multiple threads.
make --trace %{_smp_mflags} bytecode
#|| make -j1

%install
vimver=$(vim --version | head -n1 | grep -Po "\d\.\d" | sed 's|\.||')
%make_install package_infodir=%{_infodir} \
	vimdir="%{_datadir}/vim/vim$vimver" bytecode

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

chmod 0755  %{buildroot}%{_datadir}/lilypond/%{version}/python/langdefs.py

%find_lang %{name}

mkdir -p %{buildroot}%{ttfdir}
mv %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf/*.otf %{buildroot}%{ttfdir}
rmdir %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf
ln -s %{ttfdir} %{buildroot}%{_datadir}/lilypond/%{version}/fonts/otf

# Documentation section
tar -xf %{SOURCE1}
mkdir -p %{buildroot}%{_docdir}/%{name}
# lilypond main package provides info and man pages
rm -rf share/info
rm -rf share/man
cp -vr share/doc/lilypond/html %{buildroot}%{_docdir}/%{name}/
rm -f files-*
# create file lists for individual subpackages
for f in `find %{buildroot}%{_docdir}`; do
  for l in cs de es fr hu it ja nl zh; do
    if [[ $f =~ \.$l\. ]]; then
      if [ -d $f ]; then
        f="%%dir $f"
      fi
      echo "$f" | sed "s:%{buildroot}::" >> files-$l
      f=""
      break
    fi
  done

  if [ -z $f ]; then
    continue
  fi

  if [ -d $f ]; then
    f="%%dir $f"
  fi
  echo "$f" | sed "s:%{buildroot}::" >> files-en
done
for d in '.usr.share' '.usr.share.doc' '.usr.share.info' '.usr.share.doc.packages'; do
  sed -i "/^%%dir $d$/d" files-en
done
%fdupes -s share/doc/lilypond/html/Documentation
# End of Documentation section

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README.md DEDICATION
%license COPYING* LICENSE*
%{_bindir}/*
%{_datadir}/lilypond
%{_datadir}/emacs/site-lisp
%{_datadir}/vim/vim*
%{_infodir}/*%{ext_info}
%{_mandir}/man1/*

%post doc
ln -sf %{_docdir}/lilypond-doc/html/Documentation %{_infodir}/lilypond

%postun doc
rm -f %{_infodir}/lilypond

%files doc-cs -f files-cs
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-de -f files-de
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-es -f files-es
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-fr -f files-fr
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-hu -f files-hu
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-it -f files-it
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-ja -f files-ja
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-nl -f files-nl
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc-zh -f files-zh
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files doc -f files-en
%defattr(-,root,root)
%license share/doc/lilypond/html/LICENSE.DOCUMENTATION

%files emmentaler-fonts
%defattr(-,root,root,-)
%{ttfdir}/emmentaler*otf

%files fonts-common
%defattr(-,root,root,-)
%license COPYING
%defattr(0644,root,root,0755)
%dir %{ttfdir}

%changelog
