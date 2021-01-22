#
# spec file for package lilypond-doc
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_without docbuild
%if 0%{?is_backports} && 0%{?sle_version} == 150200
#"%%_project" == "openSUSE:Backports:SLE-15-SP2:Update"
ExcludeArch:    x86 x86_64 aarch64 ppc64le s390x
%endif

%define ver     2.22
%define plevel  0
Name:           lilypond-doc
Version:        %{ver}.%{plevel}
Release:        0
Summary:        Documentation for the LilyPond Typesetter
License:        GFDL-1.3-only
Group:          Documentation/HTML
URL:            http://lilypond.org/
Source0:        lilypond-%{version}.tar.gz
%if %{without docbuild}
#Source1:        https://lilypond.org/download/binaries/documentation/lilypond-%%{version}-1.documentation.tar.bz2
%endif
# PATCH-FIX-UPSTREAM https://savannah.gnu.org/patch/index.php?9370
Patch0:         reproducible.patch
# Patches taken from Debian, see headers for info.
Patch2:         add_dircategories_to_documentation.patch
Patch3:         Issue-5243-1-editor-scm-Add-shell-quote-argument-function.diff
Patch4:         use_cstring_and_ctype_includes.patch
BuildRequires:  ImageMagick-extra
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  bitstream-vera-fonts
BuildRequires:  dblatex
BuildRequires:  dejavu
BuildRequires:  extractpdfmark
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  fontconfig-devel >= 2.4.0
BuildRequires:  fontforge
BuildRequires:  fonts-arabic
BuildRequires:  freetype2-devel >= 2.1.10
BuildRequires:  gcc-c++
BuildRequires:  gentium
BuildRequires:  gettext-tools
BuildRequires:  ghostscript >= 8.60
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  gzip
BuildRequires:  ifntjapa
BuildRequires:  liberation-fonts
BuildRequires:  libgnutls-devel
BuildRequires:  libtool
BuildRequires:  lilypond = %{version}
BuildRequires:  lndir
BuildRequires:  makeinfo >= 6.1
BuildRequires:  mc
BuildRequires:  mftrace
BuildRequires:  netpbm
BuildRequires:  pango-devel >= 1.6.0
BuildRequires:  perl
BuildRequires:  rsync
BuildRequires:  t1utils
BuildRequires:  texlive-avantgar-fonts
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-dejavu-fonts
BuildRequires:  texlive-fancybox
BuildRequires:  texlive-gnu-freefont-fonts
BuildRequires:  texlive-lh
BuildRequires:  texlive-libertine-fonts
BuildRequires:  texlive-metafont-bin
BuildRequires:  texlive-metapost
BuildRequires:  texlive-xetex-bin
BuildRequires:  texlive-xltxtra
BuildRequires:  ttf-wqy-zenhei
BuildRequires:  xfntjp
BuildRequires:  xorg-x11-fonts
BuildRequires:  zip
BuildRequires:  pkgconfig(guile-1.8)
BuildRequires:  pkgconfig(python3)
Requires:       lilypond = %{version}
Requires(pre):   %{install_info_prereq} %{_bindir}/touch %{_bindir}/sed
Provides:       lilypond-documentation = %{version}
Obsoletes:      lilypond-documentation < %{version}
BuildArch:      noarch
%if %{with docbuild}
# NOTE: when lilypond documentation build with texinfo 5.x is fixed by upstream remove the 4s from makeinfo,
# NOTE: texinfo and update buildrequires with:
#BuildRequires: texi2html
BuildRequires:  texinfo4
%endif

%description
Common and english documentation files for the GNU LilyPond music typesetter.

%global rlversion %{version}
%define usrsrcp %{buildroot}
%define _configure ./smart-configure.sh

%package cs
Summary:        Documentation for the LilyPond Typesetter (cs)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description cs
Czech documentation files for the GNU LilyPond music typesetter.

%package de
Summary:        Documentation for the LilyPond Typesetter (de)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description de
German documentation files for the GNU LilyPond music typesetter.

%package es
Summary:        Documentation for the LilyPond Typesetter (es)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description es
Spanish documentation files for the GNU LilyPond music typesetter.

%package fr
Summary:        Documentation for the LilyPond Typesetter (fr)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description fr
French documentation files for the GNU LilyPond music typesetter.

%package hu
Summary:        Documentation for the LilyPond Typesetter (hu)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description hu
Hungary documentation files for the GNU LilyPond music typesetter.

%package it
Summary:        Documentation for the LilyPond Typesetter (it)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description it
Italian documentation files for the GNU LilyPond music typesetter.

%package ja
Summary:        Documentation for the LilyPond Typesetter (ja)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description ja
Japanese documentation files for the GNU LilyPond music typesetter.

%package nl
Summary:        Documentation for the LilyPond Typesetter (nl)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description nl
Dutch documentation files for the GNU LilyPond music typesetter.

%package zh
Summary:        Documentation for the LilyPond Typesetter (zh)
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description zh
Chinese documentation files for the GNU LilyPond music typesetter.

%prep
%setup -q -n lilypond-%{version}
%autopatch -p1

# Convert translations to UTF-8
for file in $(grep -L charset=UTF-8 po/*.po) ; do
    msgconv -t UTF-8 $file >$file.new
    mv $file.new $file
done
mkdir -p out/examples/
tar -cf - input/  | tar -C out/examples/ -xf- || true

%define _buildir $PWD
pushd scripts
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done
cd ../python
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done
popd
for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s@^#!.*@#!/usr/bin/python3@' ${i} ;done

%build
mkdir -p $HOME/bin
export PATH=$HOME/bin:$PATH
echo $PATH
pushd $HOME/bin
for i in `ls -1 %{_bindir}/*texi*4`
do ln -sf ${i} $(basename --suffix 4 ${i})
done
popd
ls -l $HOME/bin

#chmod 644 Documentation/pictures/*.png
# export GS_LIB="/home/$USER/.fonts" is a work around for bnc#568280
export GS_LIB="$HOME/.fonts:%{_buildir}/mf/out"

export GUILE_AUTO_COMPILE=0
export CFLAGS="%{optflags} -ggdb -fpermissive -fabi-version=4"
export CXXFLAGS="$CFLAGS"
export LILYPOND_EXTERNAL_BINARY="%{_bindir}/lilypond"
export LILYPOND_BINARY=$LILYPOND_EXTERNAL_BINARY
rm configure
./smart-autogen.sh --noconfigure
%configure --with-ncsb-dir=%{_datadir}/ghostscript/fonts/
# build documentation
echo "*********************************"
echo "* Start the documentation build *"
echo "*********************************"
make -C scripts && make -C python
#pushd Documentation
# Don't build documentation in paralell. It fails randomly.
make -e doc LILYPOND_EXTERNAL_BINARY="%{_bindir}/lilypond" LILYPOND_BINARY=$LILYPOND_EXTERNAL_BINARY
#|| (cat out-www/suffix-lyxml.dblatex.log && false)
#|| (lndir  -ignorelinks out-www/notation . && \
#LILYPOND_EXTERNAL_BINARY="%%{_bindir}/lilypond" LILYPOND_BINARY=$LILYPOND_EXTERNAL_BINARY make doc)
#popd
#make -j1 out=www WWW-post

%install
mkdir -p "%{buildroot}%{_datadir}/lilypond/%{rlversion}"
# install documentation
make install-doc DESTDIR=%{buildroot} webdir=%{_docdir}/lilypond
cp -a DEDICATION HACKING ROADMAP AUTHORS.txt NEWS.txt \
  VERSION %{buildroot}%{_docdir}/lilypond

find %{buildroot}%{_docdir}/lilypond -name *.signature -exec rm {} \;
# Fix any .py files with shebangs and wrong permissions.
if test -z `find %{buildroot}%{_datadir}/lilypond/ -name *.py -perm 0644 -print0|xargs -0r grep -l '#!'`; \
then break;
else chmod -f 0755 `find %{buildroot}%{_datadir}/lilypond/ -name *.py -perm 0644 -print0|xargs -0r grep -l '#!'`; \
fi
LILYPOND_EXTERNAL_BINARY=%{_bindir}/lilypond
# Remove spurious executables rpm lint error
chmod 0644 %{buildroot}%{_docdir}/lilypond/Documentation/pictures/*png || true
#%%find_lang lilypond
texhash %{buildroot}%{_datadir}/lilypond/%{rlversion}
find %{buildroot}%{_docdir}/lilypond/ -type f -empty -delete -print
%fdupes -s %{buildroot}%{_docdir}
%fdupes -s %{buildroot}%{_datadir}/omf
%fdupes -s %{buildroot}%{_datadir}/locale
# remove info pages, they are part of lilypond package
rm %{buildroot}%{_infodir}/*
# create file lists for individual subpackages
for f in `find %{buildroot}/%{_datadir}`; do
  for l in cs de es fr hu it ja nl zh; do
    if [[ $f =~ \.$l\. ]]; then
      if [ -d $f ]; then
        f="%%dir $f"
      fi
      echo "$f" | sed "s:%{buildroot}/::" >> files-$l
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
  echo "$f" | sed "s:%{buildroot}/::" >> files-en
done
for d in '.usr.share' '.usr.share.doc' '.usr.share.info' '.usr.share.doc.packages'; do
  sed -i "/^%%dir $d$/d" files-en
done
for f in DEDICATION \
         HACKING ROADMAP VERSION AUTHORS.txt NEWS.txt; do
  echo "%%exclude %{_docdir}/lilypond/$f" >> files-en
done
echo "%%exclude %{_datadir}/lilypond/%{rlversion}/ls-R" >> files-en
#rm %%{_infodir}/lilypond || :

%post
ln -sf %{_docdir}/lilypond/Documentation %{_infodir}/lilypond && \
%install_info --debug --info-dir=%{_infodir} --info-file=%{_infodir}/lilypond.gz

%postun
rm -f %{_infodir}/lilypond

%files cs -f files-cs
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files de -f files-de
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files es -f files-es
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files fr -f files-fr
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files hu -f files-hu
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files it -f files-it
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files ja -f files-ja
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files nl -f files-nl
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files zh -f files-zh
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%files -f files-en
%defattr(-,root,root)
%license LICENSE LICENSE.DOCUMENTATION COPYING

%changelog
