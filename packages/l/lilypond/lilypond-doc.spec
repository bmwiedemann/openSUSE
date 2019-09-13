#
# spec file for package lilypond-doc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define ver     2.18
%define plevel  2
Name:           lilypond-doc
Version:        %{ver}.%{plevel}
Release:        0
Summary:        Documentation for the LilyPond Typesetter
License:        GFDL-1.3-only
Group:          Documentation/HTML
Url:            http://lilypond.org/
Source0:        http://download.linuxaudio.org/lilypond/sources/v%{ver}/lilypond-%{version}.tar.gz
# Patches taken from Debian, see headers for info.
Patch2:         0101-read_relocation_dir-in-lilypond_datadir-too.patch
Patch3:         add_dircategories_to_documentation.patch
Patch4:         add_set-global-fonts_function.patch
Patch5:         hurd_file_name_support.patch
Patch6:         Issue-5243-1-editor-scm-Add-shell-quote-argument-function.diff
Patch7:         Issue-5243-2-Let-get-editor-use-shell-quote-argument.diff
Patch8:         Issue-5243-3-More-conservative-parsing-of-textedit-URIs.diff
Patch9:         use_cstring_and_ctype_includes.patch
Patch10:        use_system_correctly.patch
BuildRequires:  ImageMagick-extra
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  dblatex
BuildRequires:  dejavu
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  fontconfig-devel >= 2.4.0
BuildRequires:  fontforge-devel
BuildRequires:  fonts-arabic
BuildRequires:  freetype2-devel >= 2.1.10
BuildRequires:  gcc-c++
BuildRequires:  gentium
BuildRequires:  gettext-tools
#BuildRequires:  ghostscript-fonts-rus
BuildRequires:  bitstream-vera-fonts
BuildRequires:  ghostscript >= 8.60
BuildRequires:  ghostscript-fonts-other
BuildRequires:  ghostscript-fonts-std
BuildRequires:  guile1 >= 1.8.2
BuildRequires:  gzip
BuildRequires:  ifntjapa
BuildRequires:  liberation-fonts
BuildRequires:  libgnutls-devel
BuildRequires:  libguile1-devel >= 1.8.2
BuildRequires:  libtool
BuildRequires:  lilypond = %{version}
BuildRequires:  lndir
BuildRequires:  mftrace
BuildRequires:  netpbm
BuildRequires:  pango-devel >= 1.12
BuildRequires:  perl
BuildRequires:  python-devel >= 2.4
BuildRequires:  rsync
BuildRequires:  t1utils
BuildRequires:  texlive-avantgar-fonts
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  texlive-dejavu-fonts
BuildRequires:  texlive-gnu-freefont-fonts
BuildRequires:  texlive-lh
BuildRequires:  texlive-libertine-fonts
BuildRequires:  texlive-metafont-bin
BuildRequires:  texlive-metapost
BuildRequires:  ttf-wqy-zenhei
BuildRequires:  xfntjp
BuildRequires:  xorg-x11-fonts
BuildRequires:  zip
Requires:       lilypond = %{version}
Requires(pre):   %{install_info_prereq} %{_bindir}/touch %{_bindir}/sed
Provides:       lilypond-documentation = %{version}
Obsoletes:      lilypond-documentation < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version} > 1320
Patch0:         lilypond-doc-texinfo4.patch
# NOTE: when lilypond documentation build with texinfo 5.x is fixed by upstream remove patch, the 4s from makeinfo,
# NOTE: texinfo and update buildrequires with:
#BuildRequires: texi2html
BuildRequires:  makeinfo4
BuildRequires:  texinfo4
%else
BuildRequires:  texinfo
BuildRequires:  texlive-filesystem
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
%if 0%{?suse_version} > 1320
%patch0
%endif
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10

# Convert translations to UTF-8
for file in $(grep -L charset=UTF-8 po/*.po) ; do
    msgconv -t UTF-8 $file >$file.new
    mv $file.new $file
done
mkdir -p out/examples/
tar -cf - input/  | tar -C out/examples/ -xf- || true

%define _buildir $PWD

%build
chmod 644 Documentation/pictures/*.png
# export GS_LIB="/home/$USER/.fonts" is a work around for bnc#568280
#export GS_LIB="/home/$USER/.fonts:%%{_buildir}/mf/out"
export CFLAGS="-fmessage-length=0 -O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables -ggdb"
%if 0%{?suse_version} == 1210
export CFLAGS="$CFLAGS -fno-optimize-sibling-calls"
%endif
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
pushd Documentation
# Don't build documentation in paralell. It fails randomly.
LILYPOND_EXTERNAL_BINARY="%{_bindir}/lilypond" LILYPOND_BINARY=$LILYPOND_EXTERNAL_BINARY make -e doc \
|| (cat internals.texi2pdf.log && false)
#|| (lndir  -ignorelinks out-www/notation . && \
#LILYPOND_EXTERNAL_BINARY="%%{_bindir}/lilypond" LILYPOND_BINARY=$LILYPOND_EXTERNAL_BINARY make doc)
popd
make -j1 out=www WWW-post

%install
mkdir -p "%{buildroot}%{_datadir}/lilypond/%{rlversion}"
# install documentation
make install-doc DESTDIR=%{buildroot} webdir=%{_docdir}/lilypond
cp -a COPYING LICENSE LICENSE.DOCUMENTATION \
  DEDICATION HACKING ROADMAP AUTHORS.txt NEWS.txt \
  VERSION \
  %{buildroot}%{_docdir}/lilypond

find %{buildroot}%{_docdir}/lilypond -name *.signature -exec rm {} \;
# Fix any .py files with shebangs and wrong permissions.
if test -z `find %{buildroot}%{_datadir}/lilypond/ -name *.py -perm 0644 -print0|xargs -0r grep -l '#!'`; \
then break;
else chmod -f 0755 `find %{buildroot}%{_datadir}/lilypond/ -name *.py -perm 0644 -print0|xargs -0r grep -l '#!'`; \
fi
LILYPOND_EXTERNAL_BINARY=%{_bindir}/lilypond
%find_lang lilypond
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
for f in LICENSE LICENSE.DOCUMENTATION COPYING DEDICATION \
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

%files de -f files-de
%defattr(-,root,root)

%files es -f files-es
%defattr(-,root,root)

%files fr -f files-fr
%defattr(-,root,root)

%files hu -f files-hu
%defattr(-,root,root)

%files it -f files-it
%defattr(-,root,root)

%files ja -f files-ja
%defattr(-,root,root)

%files nl -f files-nl
%defattr(-,root,root)

%files zh -f files-zh
%defattr(-,root,root)

%files -f files-en
%defattr(-,root,root)

%changelog
