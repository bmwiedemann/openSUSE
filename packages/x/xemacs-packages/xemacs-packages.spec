#
# spec file for package xemacs-packages
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xemacs-packages
#!BuildIgnore:  xemacs-packages-info xemacs-packages-el xemacs-packages
BuildRequires:  compface
BuildRequires:  db-devel
%if 0%{?suse_version} >= 1110
BuildRequires:  fdupes
%endif
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  krb5
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  openldap2-devel
BuildRequires:  texlive
BuildRequires:  texlive-latex
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xemacs-el > 21.5.29
%if 0%{?suse_version} >= 1220
BuildRequires:  bdftopcf
BuildRequires:  mkfontdir
%else
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-devel
%endif
%if %suse_version > 1220
BuildRequires:  glibc-locale
BuildRequires:  info
BuildRequires:  makeinfo
BuildRequires:  par
BuildRequires:  texinfo
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-ec
%endif
URL:            http://www.xemacs.org
Provides:       xemacs:%{_datadir}/xemacs/xemacs-packages/etc/auctex/style/amsart.elc
Obsoletes:      Mule-UCS-xemacs
Obsoletes:      apel-xemacs <= 10.7
Obsoletes:      mule-ucs-xemacs
Version:        20130822
Release:        0
Requires:       /usr/bin/env
#
# HG version >= 1.9.3
#   hg --version
#   hg clone https://bitbucket.org/xemacs/xemacs-packages packages
#   cd packages/
# Check for last version
#   head -n 1 ChangeLog
#   hg archive -S -p packages -X '.hg*' -X '.cvs*' -t tbz2 ../xemacs-sumo-<version>.tar.bz
#
Source1:        xe-list.el
Source3:        texi2utf8
Source0:        %{name}-%{version}.tar.bz2
Source20:       xemacs-packages-rpmlintrc
# PATCH-FIX-OPENSUSE xemacs-packages-expand-kw.diff ailin.nemui@gmail.com -- expand CVS keywords which does not happen in hg (can be removed when new packages get releases from hg)
Patch1:         xemacs-packages-expand-kw.diff
Patch2:         xemacs-packages.patch
# keep in sync with the similar patch to the app-defaults in the main xemacs package:
Patch3:         app-defaults.patch
Patch4:         packages-cvs-xemacs-sumo-2005-12-08-apel.patch
Patch5:         edict-utf-8.patch
Patch6:         packages-cvs-xemacs-sumo-2005-12-08-diff-mode.patch
Patch7:         gnus-utf-8.patch
Patch11:        packages-cvs-xemacs-sumo-2002-03-29-ps-print.patch
Patch15:        packages-cvs-sumo-2002-09-19-comint.patch
Patch17:        packages-cvs-sumo-2004-02-02-awk.patch
Patch18:        dinbrief.patch
Patch19:        disable-skk.patch
Patch24:        texi-coding.patch
Patch28:        texi.patch
Patch32:        bugzilla-183805-missing-autoload-cookies.patch
Patch34:        mode-local.patch
Patch35:        xemacs-packages-20130822-tramp.patch
Patch36:        reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Summary:        XEmacs Packages
License:        GPL-3.0-or-later
Group:          Productivity/Editors/Emacs
%define _default_patch_fuzz 2

%description -n xemacs-packages
A collection of additional lisp packages for XEmacs. You must install
this package when you want to use the XEmacs package, they are needed
for most non-trivial XEmacs functions.



Authors:
--------
    Chuck Thompson   <cthomp@cs.uiuc.edu>
    Ben Wing <wing@666.com>
    and many other contributors

%package     -n xemacs-packages-el
Summary:        Emacs-Lisp source files for the XEmacs packages
Group:          Productivity/Editors/Emacs
Provides:       xemacs-el:%{_datadir}/xemacs/xemacs-packages/etc/auctex/style/amsart.el

%description -n xemacs-packages-el
Most Emacs-Lisp source files are not needed for running XEmacs. Most of
them are also available in byte compiled form and therefore not
necessary at runtime. The true XEmacs addict will install them
nevertheless because it is often useful and enlightening to have a look
at the Lisp sources.



Authors:
--------
    Chuck Thompson   <cthomp@cs.uiuc.edu>
    Ben Wing <wing@666.com>
    and many other contributors

%package     -n xemacs-packages-info
Summary:        Info Files for the XEmacs Packages
Group:          Productivity/Editors/Emacs
Provides:       xemacs-info:%{_datadir}/xemacs/xemacs-packages/info/auctex.info.gz

%description -n xemacs-packages-info
This package contains all the info files for the extra packages for
XEmacs. All these files can be read online with XEmacs and describe
XEmacs and some of its modes.



Authors:
--------
    Chuck Thompson   <cthomp@cs.uiuc.edu>
    Ben Wing <wing@666.com>
    and many other contributors

%prep
%setup -q
%patch -P 1   -p1 -b .keywords
find -name '*.pl' -o -name file-newer | \
  xargs -r sed -ri '1 {s@(^#[[:blank:]]*\!)(.*/perl5?)@\1/usr/bin/perl@p}'
chmod -R u+rw,g+r,o+r .
%patch -P 2   -p1 -b .packages
%patch -P 3   -p1 -b .app-defaults
%patch -P 4   -p1 -b .apel
%patch -P 5   -p1 -b .edict-utf-8
%patch -P 6   -p1 -b .diff-mode
%patch -P 7   -p1 -b .gnus-utf-8
%patch -P 11  -p1 -b .psprint
#%patch -P 15 -p1 -b .comint
%patch -P 17  -p1 -b .awk
%patch -P 18  -p1 -b .dinbrief
%patch -P 19  -p1 -b .disable-skk
%patch -P 24  -p1 -b .texi-coding
%patch -P 28  -p1 -b .texi-patch
%patch -P 32  -p1 -b .cookie
%patch -P 34  -p1 -b .mode-local
# PATCH-FIX-SUSE boo#857207 -- xemacs tramp ssh completion returns "Wrong type argument: symbolp, ..."
%patch -P 35  -p1 -b .tramp
%patch -P 36 -p1
rm -vf xemacs-packages/tramp/texi/tramp.texi.tramp
chmod 755 %{S:3}
%{S:3}

%build
unset ${!LC_*}
export LC_ALL=POSIX
cp Local.rules.template Local.rules
make %{?_smp_mflags} distclean   XEMACS_INSTALLED_PACKAGES_ROOT=%{_datadir}/xemacs MAKEINFO="makeinfo --force"
make                 autoloads   XEMACS_INSTALLED_PACKAGES_ROOT=%{_datadir}/xemacs MAKEINFO="makeinfo --force"
make                 bytecompile XEMACS_INSTALLED_PACKAGES_ROOT=%{_datadir}/xemacs MAKEINFO="makeinfo --force"

%install
unset ${!LC_*}
export LC_ALL=POSIX
make %{?_smp_mflags} install     XEMACS_INSTALLED_PACKAGES_ROOT=%{buildroot}%{_datadir}/xemacs MAKEINFO="makeinfo --force"

# quick hack to install latin-unity-tables.el because latin-unity-tables.elc
# is not built:
install -m 644 mule-packages/latin-unity/latin-unity-tables.el \
    %{buildroot}%{_datadir}/xemacs/mule-packages/lisp/latin-unity/latin-unity-tables.el
gzip -n --best %{buildroot}%{_datadir}/xemacs/xemacs-packages/info/*
gzip -n --best %{buildroot}%{_datadir}/xemacs/mule-packages/info/*
######################################################################
# ugly workaround to avoid the messages
#     $ xemacs -q
#     Loading ediff-hook...
#     Loading ediff-hook...done
# on standard out when starting xemacs
echo "(require 'ediff-hook)" > %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ediff/auto-autoloads.el.new
cat %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ediff/auto-autoloads.el \
    >> %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ediff/auto-autoloads.el.new
mv  %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ediff/auto-autoloads.el.new \
    %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ediff/auto-autoloads.el
echo "(require 'advice)"     >  %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/semantic/auto-autoloads.el.new
echo "(require 'mode-local)" >> %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/semantic/auto-autoloads.el.new
cat %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/semantic/auto-autoloads.el \
    >> %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/semantic/auto-autoloads.el.new
mv  %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/semantic/auto-autoloads.el.new \
    %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/semantic/auto-autoloads.el
######################################################################
#
mkdir -p %{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/auctex/doc
install -m 644 xemacs-packages/auctex/doc/tex-ref.dvi \
	 %{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/auctex/doc/
mkdir -p %{buildroot}%{_datadir}/xemacs/xemacs-packages/man/auctex
install -m 644 xemacs-packages/auctex/{CHANGES,FAQ,README,TODO} \
	 %{buildroot}%{_datadir}/xemacs/xemacs-packages/man/auctex/
######################################################################
# Some .elc's are not needed:
find  %{buildroot}%{_datadir}/xemacs/ -name '_pkg.elc'   | xargs -r rm -f
find  %{buildroot}%{_datadir}/xemacs/ -name 'auto-autoloads.elc' | xargs -r rm -f
# add Japanese translations for liece menus to Japanese app-defaults:
chmod u+w %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja/Emacs
cat xemacs-packages/liece/etc/Emacs.ad >> %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja/Emacs
# delete a riece file which shouldn't have been installed:
rm %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/riece/riece-package-info.el.in
# Make symlinks for international app-defaults:
ln -sf de %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/de_DE
ln -sf de %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/de_DE@euro
ln -sf fr %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/fr_FR
ln -sf fr %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/fr_FR@euro
ln -sf sv %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/sv_SE
ln -sf sv %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/sv_SE@euro
ln -sf ja %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP
ln -sf ja %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.ujis
ln -sf ja %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.EUC
ln -sf ja %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.eucJP
ln -sf ro %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/ro_RO
# create international app-defaults for UTF-8 locales:
pushd %{buildroot}%{_datadir}/xemacs/mule-packages/etc/app-defaults/
    for i in de_DE fr_FR ja_JP sv_SE ro_RO
    do
	mkdir $i.UTF-8
	iconv -f $(LC_ALL=$i locale charmap) -t UTF-8 < $i/Emacs > $i.UTF-8/Emacs
        perl -pi -e 's/-\*- (mode:.*)?coding:.*-\*-/-\*- \1coding: utf-8 -\*-/' $i.UTF-8/Emacs
    done
popd
# generate info/dir files:
xemacs -batch -f Info-batch-rebuild-dir \
                 %{buildroot}%{_datadir}/xemacs/xemacs-packages/info/ \
		 %{buildroot}%{_datadir}/xemacs/mule-packages/info/
for i in %{buildroot}%{_datadir}/xemacs/*/info/dir
do
    perl -pi -e "s|%{buildroot}||" $i
done
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
ln -s %{_datadir}/xemacs/xemacs-packages/etc \
      %{buildroot}/%{_defaultdocdir}/%{name}/xemacs-packages
ln -s %{_datadir}/xemacs/mule-packages/etc \
      %{buildroot}/%{_defaultdocdir}/%{name}/mule-packages
# Remove unneeded files
rm -f %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/w3/README.NT \
      %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/w3/README.VMS
rm -f %{buildroot}%{_datadir}/xemacs/mule-packages/etc/mule-ucs/mule-ucs.texi
find %{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/ -name INSTALL | \
    xargs -r rm -vf
find %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ -name INSTALL | \
    xargs -r rm -vf
# Move docs from lisp to etc directories
for doc in \
	   hyperbole/{{_,.}hypb,DEMO,GNUmakefile.id,MANIFEST,file-newer,smart-clib-sym} \
	   hyperbole/kotl/{EXAMPLE.kotl,MANIFEST} \
	   oo-browser/{BR-{COPY,FEATURES,README,RELEASE,VERSION},Make-Env,Makefile,oo-browser.texi}
do
    src=%{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/$doc
    case "$doc" in
    auctex*) dst=%{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/auctex/doc/${doc##*/} ;;
    *)	     dst=%{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/$doc
    esac
    case "${doc##*/}" in
    _*) rm -vf $src ;;
    .*) rm -vf $src ;;
    *.texi)
	rm -vf $src ;;
    GNUmakefile*|Makefile)
	rm -vf $src
    esac
    test -e $src || continue
    test -d ${dst%%/*} || mkdir -p ${dst%%/*}
    mv -vf $src $dst
done
# Correct permissions
chmod a-x %{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/text-modes/*.xpm
chmod a-x %{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/jde/doc/html/jde-ug/images/*.gif
chmod a-x %{buildroot}%{_datadir}/xemacs/xemacs-packages/etc/jde/doc/src/jde-ug/images/*.gif
chmod a-x %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/text-modes/*.el
chmod a-x %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/vm/*.el
chmod a-x %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/jde/*.el
chmod a-x %{buildroot}%{_datadir}/xemacs/xemacs-packages/lisp/ede/*.el
# File duplicates
%if 0%{?suse_version} >= 1110
fdupes -q -o name -r -1 %{buildroot}%{_datadir}/xemacs/ | while read first second; do
    case "${first}" in
    *.el*)  continue ;;
    *.texi) continue
    esac
    target=
    file=
    for t in $first $second; do
	case "$t" in
	*/lisp/*)
	    file="$t"
	    continue
	esac
    done
    if test -n "$file" ; then
	for t in $first $second; do
	    test "$t" = "$file" && continue
	    target="${target:+$target }$t"
	done
    else
	file="$first"
	target="$second"
    fi
    for t in ${target} ; do
	ln -sf ${file#%{buildroot}} ${t}
    done
done
%endif
# generate file lists:
find %{buildroot} \
    \( \( \( -not -type d \) -printf '%%p\n' \) \
               -o \( -type d -printf '%%p/\n' \) \) \
	| sort -t / | uniq | sed "s|^%{buildroot}||" > xe-list
xemacs -batch -l $RPM_SOURCE_DIR/xe-list.el -f xe-list-generate-list-files
cat xe-list-el-without-elc xe-list-elc-without-el xe-list-elc-with-el \
    >> xe-list-el-without-elc_xe-list-elc-without-el_xe-list-elc-with-el

%clean
#[ "%{buildroot}" != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot}

%files -f xe-list-el-without-elc_xe-list-elc-without-el_xe-list-elc-with-el
%defattr(-,root,root)
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*
%dir %{_datadir}/xemacs/
%dir %{_datadir}/xemacs/mule-packages/
%dir %{_datadir}/xemacs/mule-packages/etc/
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/de/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/de/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/de_DE
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/de_DE.UTF-8/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/de_DE.UTF-8/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/de_DE@euro
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/fr/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/fr/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/fr_FR
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/fr_FR.UTF-8/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/fr_FR.UTF-8/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/fr_FR@euro
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/ja/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/ja/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP
%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.EUC
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.UTF-8/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.UTF-8/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.eucJP
%{_datadir}/xemacs/mule-packages/etc/app-defaults/ja_JP.ujis
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/ro/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/ro/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/ro_RO
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/ro_RO.UTF-8/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/ro_RO.UTF-8/Emacs
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/sv/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/sv/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/sv_SE
%dir %{_datadir}/xemacs/mule-packages/etc/app-defaults/sv_SE.UTF-8/
%config %{_datadir}/xemacs/mule-packages/etc/app-defaults/sv_SE.UTF-8/Emacs
%{_datadir}/xemacs/mule-packages/etc/app-defaults/sv_SE@euro
%dir %{_datadir}/xemacs/mule-packages/etc/edict/
%doc %{_datadir}/xemacs/mule-packages/etc/edict/ChangeLog.096
%doc %{_datadir}/xemacs/mule-packages/etc/edict/README
%doc %{_datadir}/xemacs/mule-packages/etc/edict/README.096
%doc %{_datadir}/xemacs/mule-packages/etc/edict/edict.doc.096
%doc %{_datadir}/xemacs/mule-packages/etc/edict/edictj.demo
%dir %{_datadir}/xemacs/mule-packages/etc/latin-unity/
%doc %{_datadir}/xemacs/mule-packages/etc/latin-unity/BLURB
%doc %{_datadir}/xemacs/mule-packages/etc/latin-unity/ChangeLog
%doc %{_datadir}/xemacs/mule-packages/etc/latin-unity/Makefile
%doc %{_datadir}/xemacs/mule-packages/etc/latin-unity/README
%dir %{_datadir}/xemacs/mule-packages/etc/mule-doc/
%doc %{_datadir}/xemacs/mule-packages/etc/mule-doc/*
%dir %{_datadir}/xemacs/mule-packages/etc/mule-ucs/
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/ChangeLog
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/Makefile
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/MuleUni.txt
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/README
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/README.Unicode
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/README.XEmacs
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/mule-ucs.sgml
%dir %{_datadir}/xemacs/mule-packages/etc/mule-ucs/reldata/
%doc %{_datadir}/xemacs/mule-packages/etc/mule-ucs/type.txt
%dir %{_datadir}/xemacs/mule-packages/etc/mule/
%doc %{_datadir}/xemacs/mule-packages/etc/mule/FAQ-Mule
%doc %{_datadir}/xemacs/mule-packages/etc/mule/FAQ-Mule.cn
%doc %{_datadir}/xemacs/mule-packages/etc/mule/FAQ-Mule.ja
%doc %{_datadir}/xemacs/mule-packages/etc/mule/FAQ-Mule.kr
%doc %{_datadir}/xemacs/mule-packages/etc/mule/FAQ-Mule.th
%doc %{_datadir}/xemacs/mule-packages/etc/mule/Makefile.in
%doc %{_datadir}/xemacs/mule-packages/etc/mule/TUTORIAL.kr
%doc %{_datadir}/xemacs/mule-packages/etc/mule/VERSIONS
%doc %{_datadir}/xemacs/mule-packages/etc/mule/coco.1
%doc %{_datadir}/xemacs/mule-packages/etc/mule/demo.ps
%doc %{_datadir}/xemacs/mule-packages/etc/mule/m2ps.1
%doc %{_datadir}/xemacs/mule-packages/etc/mule/m2ps.1.in
%doc %{_datadir}/xemacs/mule-packages/etc/mule/m2ps.ps
%doc %{_datadir}/xemacs/mule-packages/etc/mule/mule-refcard.tex
%doc %{_datadir}/xemacs/mule-packages/etc/mule/mule.1
%{_datadir}/xemacs/mule-packages/etc/mule/mule.xbm
%{_datadir}/xemacs/mule-packages/etc/mule/tom.xbm
%dir %{_datadir}/xemacs/mule-packages/etc/start-files/
%dir %{_datadir}/xemacs/mule-packages/etc/start-files/fr/
%dir %{_datadir}/xemacs/mule-packages/etc/start-files/ja/
%dir %{_datadir}/xemacs/mule-packages/etc/start-files/ro/
%dir %{_datadir}/xemacs/mule-packages/etc/start-files/French/
%dir %{_datadir}/xemacs/mule-packages/etc/start-files/Japanese/
%dir %{_datadir}/xemacs/mule-packages/etc/start-files/Romanian/
%dir %{_datadir}/xemacs/mule-packages/lisp/
%dir %{_datadir}/xemacs/mule-packages/lisp/edict/
%doc %{_datadir}/xemacs/mule-packages/lisp/edict/ChangeLog
%doc %{_datadir}/xemacs/mule-packages/lisp/edict/Makefile.GNU
%dir %{_datadir}/xemacs/mule-packages/lisp/egg-its/
%doc %{_datadir}/xemacs/mule-packages/lisp/egg-its/ChangeLog
%{_datadir}/xemacs/mule-packages/lisp/egg-its/eggrc-sj3
%{_datadir}/xemacs/mule-packages/lisp/egg-its/eggrc-wnn
%dir %{_datadir}/xemacs/mule-packages/lisp/latin-euro-standards/
%doc %{_datadir}/xemacs/mule-packages/lisp/latin-euro-standards/ChangeLog
%dir %{_datadir}/xemacs/mule-packages/lisp/latin-unity/
%doc %{_datadir}/xemacs/mule-packages/lisp/latin-unity/ChangeLog
%dir %{_datadir}/xemacs/mule-packages/lisp/leim/
%doc %{_datadir}/xemacs/mule-packages/lisp/leim/ChangeLog
%dir %{_datadir}/xemacs/mule-packages/lisp/leim/quail/
%dir %{_datadir}/xemacs/mule-packages/lisp/locale/
%doc %{_datadir}/xemacs/mule-packages/lisp/locale/ChangeLog
%dir %{_datadir}/xemacs/mule-packages/lisp/lookup/
%doc %{_datadir}/xemacs/mule-packages/lisp/lookup/ChangeLog
%dir %{_datadir}/xemacs/mule-packages/lisp/mule-base/
%doc %{_datadir}/xemacs/mule-packages/lisp/mule-base/ChangeLog
%dir %{_datadir}/xemacs/mule-packages/lisp/mule-ucs/
%doc %{_datadir}/xemacs/mule-packages/lisp/mule-ucs/ChangeLog
%dir %{_datadir}/xemacs/mule-packages/man/
%dir %{_datadir}/xemacs/mule-packages/man/latin-euro-standards/
%doc %{_datadir}/xemacs/mule-packages/man/latin-euro-standards/latin-euro-standards.texi
%dir %{_datadir}/xemacs/mule-packages/man/latin-unity/
%doc %{_datadir}/xemacs/mule-packages/man/latin-unity/latin-unity.texi
%dir %{_datadir}/xemacs/mule-packages/man/lookup/
%doc %{_datadir}/xemacs/mule-packages/man/lookup/lookup.texi
%doc %{_datadir}/xemacs/mule-packages/man/lookup/lookup-guide.texi
%dir %{_datadir}/xemacs/mule-packages/man/mule-ucs/
%doc %{_datadir}/xemacs/mule-packages/man/mule-ucs/mule-ucs.texi
%dir %{_datadir}/xemacs/mule-packages/pkginfo/
%{_datadir}/xemacs/mule-packages/pkginfo/*
%dir %{_datadir}/xemacs/xemacs-packages/
%dir %{_datadir}/xemacs/xemacs-packages/etc/
%{_datadir}/xemacs/xemacs-packages/etc/BABYL
%dir %{_datadir}/xemacs/xemacs-packages/etc/auctex/
%dir %{_datadir}/xemacs/xemacs-packages/etc/auctex/doc/
%doc %{_datadir}/xemacs/xemacs-packages/etc/auctex/doc/*.dvi
%dir %{_datadir}/xemacs/xemacs-packages/etc/auctex/images/
%{_datadir}/xemacs/xemacs-packages/etc/auctex/images/*.xpm
%{_datadir}/xemacs/xemacs-packages/etc/auctex/images/*.xbm
%dir %{_datadir}/xemacs/xemacs-packages/etc/auctex/style/
%dir %{_datadir}/xemacs/xemacs-packages/etc/auctex/latex/
%{_datadir}/xemacs/xemacs-packages/etc/auctex/latex/pr*.def
%{_datadir}/xemacs/xemacs-packages/etc/auctex/latex/prauctex.cfg
%{_datadir}/xemacs/xemacs-packages/etc/auctex/latex/preview.sty
%dir %{_datadir}/xemacs/xemacs-packages/etc/bbdb/
%{_datadir}/xemacs/xemacs-packages/etc/bbdb/bbdb-areacode-split.pl
%{_datadir}/xemacs/xemacs-packages/etc/bbdb/bbdb-cid.pl
%{_datadir}/xemacs/xemacs-packages/etc/bbdb/bbdb-srv.pl
%{_datadir}/xemacs/xemacs-packages/etc/bbdb/bbdb-unlazy-lock.pl
%dir %{_datadir}/xemacs/xemacs-packages/etc/bbdb/tex/
%doc %{_datadir}/xemacs/xemacs-packages/etc/bbdb/tex/bbdb-cols.tex
%doc %{_datadir}/xemacs/xemacs-packages/etc/bbdb/tex/bbdb-print-brief.tex
%doc %{_datadir}/xemacs/xemacs-packages/etc/bbdb/tex/bbdb-print.tex
%doc %{_datadir}/xemacs/xemacs-packages/etc/calccard.tex
%dir %{_datadir}/xemacs/xemacs-packages/etc/e/
%doc %{_datadir}/xemacs/xemacs-packages/etc/e/README
%{_datadir}/xemacs/xemacs-packages/etc/e/emancs
%{_datadir}/xemacs/xemacs-packages/etc/e/emancs.ti
%{_datadir}/xemacs/xemacs-packages/etc/e/eterm
%{_datadir}/xemacs/xemacs-packages/etc/e/eterm.ti
%dir %{_datadir}/xemacs/xemacs-packages/etc/easypg/
%{_datadir}/xemacs/xemacs-packages/etc/easypg/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/ecb/
%{_datadir}/xemacs/xemacs-packages/etc/ecb/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/ediff/
%{_datadir}/xemacs/xemacs-packages/etc/ediff/*
%{_datadir}/xemacs/xemacs-packages/etc/edt-user.doc
%{_datadir}/xemacs/xemacs-packages/etc/emerge.txt
%{_datadir}/xemacs/xemacs-packages/etc/enriched.doc
%dir %{_datadir}/xemacs/xemacs-packages/etc/erc/
%{_datadir}/xemacs/xemacs-packages/etc/erc/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/ezimage
%{_datadir}/xemacs/xemacs-packages/etc/ezimage/*
%{_datadir}/xemacs/xemacs-packages/etc/forms-d2.dat
%dir %{_datadir}/xemacs/xemacs-packages/etc/frame-icon/
%{_datadir}/xemacs/xemacs-packages/etc/frame-icon/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/gnats/
%{_datadir}/xemacs/xemacs-packages/etc/gnats/categories
%{_datadir}/xemacs/xemacs-packages/etc/gnats/xemacs.org
%dir %{_datadir}/xemacs/xemacs-packages/etc/gnus/
%{_datadir}/xemacs/xemacs-packages/etc/gnus/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/guided-tour/
%{_datadir}/xemacs/xemacs-packages/etc/guided-tour/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/haskell-mode/
%doc %{_datadir}/xemacs/xemacs-packages/etc/haskell-mode/fontlock.hs
%doc %{_datadir}/xemacs/xemacs-packages/etc/haskell-mode/indent.hs
%doc %{_datadir}/xemacs/xemacs-packages/etc/haskell-mode/index.html
%doc %{_datadir}/xemacs/xemacs-packages/etc/haskell-mode/installation-guide.html
%dir %{_datadir}/xemacs/xemacs-packages/etc/hm--html-menus/
%dir %{_datadir}/xemacs/xemacs-packages/etc/hm--html-menus/idd/
%{_datadir}/xemacs/xemacs-packages/etc/hm--html-menus/idd/drop
%{_datadir}/xemacs/xemacs-packages/etc/hm--html-menus/idd/dropmsk
%dir %{_datadir}/xemacs/xemacs-packages/etc/hm--html-menus/templates/
%{_datadir}/xemacs/xemacs-packages/etc/hm--html-menus/templates/command-description.html.tmpl
%{_datadir}/xemacs/xemacs-packages/etc/hm--html-menus/templates/frame.html.tmpl
%dir %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/
%doc %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/DEMO
%doc %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/MANIFEST
%doc %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/file-newer
%doc %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/hypb-mouse.txt
%dir %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/kotl/
%doc %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/kotl/EXAMPLE.kotl
%doc %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/kotl/MANIFEST
%doc %{_datadir}/xemacs/xemacs-packages/etc/hyperbole/smart-clib-sym
%dir %{_datadir}/xemacs/xemacs-packages/etc/idlwave/
%{_datadir}/xemacs/xemacs-packages/etc/idlwave/CHANGES
%{_datadir}/xemacs/xemacs-packages/etc/idlwave/idlwave_catalog
%dir %{_datadir}/xemacs/xemacs-packages/etc/ilisp/
%{_datadir}/xemacs/xemacs-packages/etc/ilisp/ilisp-icon.bmp
%{_datadir}/xemacs/xemacs-packages/etc/ilisp/ilisp-icon.ppm
%dir %{_datadir}/xemacs/xemacs-packages/etc/jde/
%dir %{_datadir}/xemacs/xemacs-packages/etc/jde/doc/
%doc %{_datadir}/xemacs/xemacs-packages/etc/jde/doc/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/jde/java/
%{_datadir}/xemacs/xemacs-packages/etc/jde/java/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/jde/plugins/
%{_datadir}/xemacs/xemacs-packages/etc/jde/plugins/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/mew/
%{_datadir}/xemacs/xemacs-packages/etc/mew/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/mine/
%{_datadir}/xemacs/xemacs-packages/etc/mine/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/oo-browser/
%doc %{_datadir}/xemacs/xemacs-packages/etc/oo-browser/BR-COPY
%doc %{_datadir}/xemacs/xemacs-packages/etc/oo-browser/BR-FEATURES
%doc %{_datadir}/xemacs/xemacs-packages/etc/oo-browser/BR-README
%doc %{_datadir}/xemacs/xemacs-packages/etc/oo-browser/BR-RELEASE
%doc %{_datadir}/xemacs/xemacs-packages/etc/oo-browser/BR-VERSION
%doc %{_datadir}/xemacs/xemacs-packages/etc/oo-browser/Make-Env
%dir %{_datadir}/xemacs/xemacs-packages/etc/ps-print/
%{_datadir}/xemacs/xemacs-packages/etc/ps-print/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/psgml/
%{_datadir}/xemacs/xemacs-packages/etc/psgml/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/reftex/
%doc %{_datadir}/xemacs/xemacs-packages/etc/reftex/CHANGES
%doc %{_datadir}/xemacs/xemacs-packages/etc/reftex/NUTSHELL
%dir %{_datadir}/xemacs/xemacs-packages/etc/riece/
%doc %{_datadir}/xemacs/xemacs-packages/etc/riece/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/slider/
%{_datadir}/xemacs/xemacs-packages/etc/slider/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/smilies/
%{_datadir}/xemacs/xemacs-packages/etc/smilies/*
%{_datadir}/xemacs/xemacs-packages/etc/sokoban.levels
%dir %{_datadir}/xemacs/xemacs-packages/etc/sounds/
%{_datadir}/xemacs/xemacs-packages/etc/sounds/*
%{_datadir}/xemacs/xemacs-packages/etc/spook.lines
%dir %{_datadir}/xemacs/xemacs-packages/etc/time/
%{_datadir}/xemacs/xemacs-packages/etc/time/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/text-modes/
%{_datadir}/xemacs/xemacs-packages/etc/text-modes/*.xpm
%{_datadir}/xemacs/xemacs-packages/etc/tpu-edt.xmodmap
%doc %{_datadir}/xemacs/xemacs-packages/etc/viperCard.tex
%dir %{_datadir}/xemacs/xemacs-packages/etc/vm/
%{_datadir}/xemacs/xemacs-packages/etc/vm/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/w3/
%{_datadir}/xemacs/xemacs-packages/etc/w3/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/x-symbol/
%{_datadir}/xemacs/xemacs-packages/etc/x-symbol/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/xslt-process/
%dir %{_datadir}/xemacs/xemacs-packages/etc/xslt-process/java/
%{_datadir}/xemacs/xemacs-packages/etc/xslt-process/java/*
%dir %{_datadir}/xemacs/xemacs-packages/etc/xwem/
%{_datadir}/xemacs/xemacs-packages/etc/xwem/*
%{_datadir}/xemacs/xemacs-packages/etc/yow.lines
%dir %{_datadir}/xemacs/xemacs-packages/etc/zenirc/
%{_datadir}/xemacs/xemacs-packages/etc/zenirc/*
%dir %{_datadir}/xemacs/xemacs-packages/lib-src/
%{_datadir}/xemacs/xemacs-packages/lib-src/*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/
%dir %{_datadir}/xemacs/xemacs-packages/lisp/Sun/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/Sun/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ada/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ada/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/apel/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/apel/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/apel/ChangeLog.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/apel/README.en
%doc %{_datadir}/xemacs/xemacs-packages/lisp/apel/README.ja
%dir %{_datadir}/xemacs/xemacs-packages/lisp/auctex/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/auctex/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/bbdb/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/bbdb/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/bbdb/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/build/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/build/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/c-support/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/c-support/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/calc/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/calc/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/calendar/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/calendar/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/cc-mode/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/cc-mode/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/cedet-common/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/cedet-common/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/clearcase/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/clearcase/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/cogre/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/cogre/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/cookie/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/cookie/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/crisp/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/crisp/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/debug/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/debug/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/dictionary/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/dictionary/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/dictionary/GPL
%doc %{_datadir}/xemacs/xemacs-packages/lisp/dictionary/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/dired/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/dired/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/docbookide/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/docbookide/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/docbookide/README
%doc %{_datadir}/xemacs/xemacs-packages/lisp/docbookide/dot_emacs
%dir %{_datadir}/xemacs/xemacs-packages/lisp/easypg/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/easypg/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ecb/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ecb/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ecb/README
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ecb/RELEASE_NOTES
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ecb/NEWS
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ecrypto/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ecrypto/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ede/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ede/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/edebug/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/edebug/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/edebug/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ediff/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ediff/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ediff/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/edit-utils/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/edit-utils/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/edt/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/edt/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/efs/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/efs/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/eieio/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/eieio/ChangeLog
%{_datadir}/xemacs/xemacs-packages/lisp/eieio/Project.ede
%dir %{_datadir}/xemacs/xemacs-packages/lisp/elib/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/elib/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/elib/NEWS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/elib/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/emerge/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/emerge/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/erc/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/erc/ChangeLog*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/erc/Makefile*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/erc/HACKING.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/erc/FOR-RELEASE.upstream
%dir %{_datadir}/xemacs/xemacs-packages/lisp/escreen/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/escreen/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/eshell/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/eshell/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/eterm/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/eterm/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/eterm/QUESTIONS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/eterm/README.term
%doc %{_datadir}/xemacs/xemacs-packages/lisp/eterm/TODO.term
%dir %{_datadir}/xemacs/xemacs-packages/lisp/eudc/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/eudc/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/footnote/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/footnote/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/forms/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/forms/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/fortran-modes/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/fortran-modes/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/frame-icon/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/frame-icon/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/fsf-compat/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/fsf-compat/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/fsf-compat/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/games/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/games/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/general-docs/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/general-docs/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/gnats/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnats/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/gnus/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/ChangeLog.1.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/ChangeLog.2.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/ChangeLog.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/ChangeLog.contrib.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/GNUS-NEWS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/COPYING
%doc %{_datadir}/xemacs/xemacs-packages/lisp/gnus/smiley.el.upstream
%dir %{_datadir}/xemacs/xemacs-packages/lisp/guided-tour/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/guided-tour/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/haskell-mode/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/haskell-mode/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/haskell-mode/ChangeLog.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/haskell-mode/Makefile.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/haskell-mode/NEWS
%dir %{_datadir}/xemacs/xemacs-packages/lisp/hm--html-menus/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/hm--html-menus/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/hyperbole/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/hyperbole/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/hyperbole/kotl/
%{_datadir}/xemacs/xemacs-packages/lisp/hyperbole/h-skip-bytec.lsp
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ibuffer/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ibuffer/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/idlwave/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/idlwave/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/igrep/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/igrep/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/COPYING
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/GETTING-ILISP
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/HISTORY
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/INSTALLATION
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/Makefile
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/README
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/comint-v18.el.upstream
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/Welcome
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/allegro.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/cl-chs-init.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/cl-ilisp.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/cmulisp.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/cormanlisp.lisp
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/extra/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ilisp/extra/README
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/guile-ilisp.scm
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/ilisp-pkg.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/ilisp.emacs
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/lispworks.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/lucid.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/mzscheme-ilisp.scm
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/openmcl.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/sbcl.lisp
%{_datadir}/xemacs/xemacs-packages/lisp/ilisp/sblisp.lisp
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ispell/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ispell/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/jde/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/jde/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/jde/ChangeLog.upstream
%dir %{_datadir}/xemacs/xemacs-packages/lisp/mail-lib/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mail-lib/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/ANNOUNCE
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/ChangeLog.1
%{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/LCD-entry
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/NEWS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/ONEWS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/README*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mailcrypt/WARNINGS
%dir %{_datadir}/xemacs/xemacs-packages/lisp/mew/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mew/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/mh-e/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mh-e/COPYING
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mh-e/ChangeLog*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mh-e/*NEWS*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mh-e/README*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/mine/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mine/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/misc-games/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/misc-games/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/AUTHORS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/COPYING
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/FAQ
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/NEWS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/README
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/README.Mason
%doc %{_datadir}/xemacs/xemacs-packages/lisp/mmm-mode/TODO
%dir %{_datadir}/xemacs/xemacs-packages/lisp/net-utils/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/net-utils/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ocaml/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ocaml/ChangeLog*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ocaml/README*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/oo-browser/
%{_datadir}/xemacs/xemacs-packages/lisp/oo-browser/br-c-tags
%{_datadir}/xemacs/xemacs-packages/lisp/oo-browser/br-help
%{_datadir}/xemacs/xemacs-packages/lisp/oo-browser/br-help-ms
%doc %{_datadir}/xemacs/xemacs-packages/lisp/oo-browser/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/os-utils/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/os-utils/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/pc/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/pc/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/pcl-cvs/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/pcl-cvs/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/pcomplete/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/pcomplete/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/perl-modes/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/perl-modes/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/pgg/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/pgg/ChangeLog*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/pgg/README*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/prog-modes/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/prog-modes/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ps-print/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ps-print/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ps-print/README
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ps-print/ps-print-20.new
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ps-print/ps-print-21.new
%dir %{_datadir}/xemacs/xemacs-packages/lisp/psgml-dtds/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/psgml-dtds/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/CATALOG
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ECAT
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/HTML3.2.decl
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/HTML4.01.decl
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/HTML4.decl
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/HTMLlat1.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/HTMLspecial.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/HTMLsymbol.ent
%dir %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/
%dir %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Added_Latin_1
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Added_Latin_1_for_HTML
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Added_Math_Symbols-_Delimiters
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Added_Math_Symbols-_Ordinary
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Added_Math_Symbols-_Relations
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Diacritical_Marks
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/General_Technical
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Greek_Symbols
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOamsa
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOamsb
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOamsc
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOamsn
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOamso
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOamsr
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISObox
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOcyr1
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOcyr2
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOdia
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOgrk1
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOgrk2
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOgrk3
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOgrk4
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOlat1
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOlat2
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOnum
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOpub
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/ISOtech
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/Numeric_and_Special_Graphic
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isoamsa.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isoamsb.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isoamsc.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isoamsn.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isoamso.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isoamsr.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isobox.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isocyr1.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isocyr2.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isodia.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isogrk3.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isolat1.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isolat2.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isomfrk.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isomopf.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isomscr.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isonum.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isopub.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISO_8879-1986/entities/isotech.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/ISOlat1.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/README.cdtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cals-tbl.dtd
%dir %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/docbook
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-3
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-3-r
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-3.2
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-4.01frame
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-4.01s
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-4frame
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-4s
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/html-r
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/mathml
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/xhtml1-frameset
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/xhtml1-strict
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/cdtd/xhtml1-transitional
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/datatypes.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/dbcent.mod
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/dbgenent.mod
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/dbhier.mod
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/dbnotn.mod
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/dbpool.mod
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/docbook.dcl
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/docbook.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-3.2.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-3.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-3s.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-4.01frame.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-4.01l.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-4.01s.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-4frame.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-4l.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-4s.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-icons.sgml
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-latin.sgml
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-math.sgml
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html-s.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html.decl
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/html.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/mathml.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/mmlalias.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/mmlextra.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/structures.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/versionInfo.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml-lat1.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml-special.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml-symbol.ent
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml1-frameset.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml1-strict.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml1-transitional-mathml.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml1-transitional.dtd
%doc %{_datadir}/xemacs/xemacs-packages/etc/psgml-dtds/xhtml1.dcl
%dir %{_datadir}/xemacs/xemacs-packages/etc/python-modes/
%doc %{_datadir}/xemacs/xemacs-packages/etc/python-modes/pydoc_lisp.py
%dir %{_datadir}/xemacs/xemacs-packages/lisp/psgml/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/psgml/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/python-modes/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/python-modes/ChangeLog*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/python-modes/pydoc-el-README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/re-builder/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/re-builder/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/reftex/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/reftex/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/riece/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/riece/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/rmail/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/rmail/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/ruby-modes/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ruby-modes/ChangeLog*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/ruby-modes/README*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/sasl/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/sasl/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/sasl/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/scheme/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/scheme/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/semantic/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/semantic/ChangeLog*
%doc %{_datadir}/xemacs/xemacs-packages/lisp/semantic/NEWS*
%{_datadir}/xemacs/xemacs-packages/lisp/semantic/*.ede
%{_datadir}/xemacs/xemacs-packages/lisp/semantic/*.bnf
%dir %{_datadir}/xemacs/xemacs-packages/lisp/sgml/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/sgml/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/sh-script/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/sh-script/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/sieve/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/sieve/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/slider/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/slider/ChangeLog*
%dir %{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/
%{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/BUGS
%{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/ChangeLog*
%{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/NEWS*
%{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/README*
%{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/TODO*
%{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/sml-mode.spec
%{_datadir}/xemacs/xemacs-packages/lisp/sml-mode/testcases.sml
%dir %{_datadir}/xemacs/xemacs-packages/lisp/sounds-au/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/sounds-au/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/sounds-wav/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/sounds-wav/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/speedbar/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/speedbar/ChangeLog
%{_datadir}/xemacs/xemacs-packages/lisp/speedbar/*.xpm
%dir %{_datadir}/xemacs/xemacs-packages/lisp/strokes/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/strokes/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/supercite/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/supercite/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/texinfo/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/texinfo/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/text-modes/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/text-modes/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/textools/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/textools/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/time/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/time/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/tm/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/tm/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/tooltalk/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/tooltalk/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/tpu/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/tpu/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/tramp/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/tramp/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/tramp/ChangeLog.upstream
%dir %{_datadir}/xemacs/xemacs-packages/lisp/vc-cc/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/vc-cc/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/vc/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/vc/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/vhdl/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/vhdl/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/view-process/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/view-process/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/viper/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/viper/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/viper/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/vm/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/vm/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/vm/NEWS
%dir %{_datadir}/xemacs/xemacs-packages/lisp/w3/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/w3/BUGS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/w3/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/w3/HOWTO
%doc %{_datadir}/xemacs/xemacs-packages/lisp/w3/README
%doc %{_datadir}/xemacs/xemacs-packages/lisp/w3/TODO
%doc %{_datadir}/xemacs/xemacs-packages/lisp/w3/md5.el.upstream
%dir %{_datadir}/xemacs/xemacs-packages/lisp/x-symbol/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/x-symbol/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/x-symbol/ChangeLog.2.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/x-symbol/ChangeLog.3.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/x-symbol/ChangeLog.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/x-symbol/Makefile.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/x-symbol/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/xemacs-base/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xemacs-base/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/xemacs-devel/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xemacs-devel/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/xetla/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xetla/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/xlib/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xlib/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/xslide/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslide/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslide/ChangeLog.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslide/Makefile.upstream
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslide/README.TXT
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslide/dot_emacs
%{_datadir}/xemacs/xemacs-packages/lisp/xslide/xslide-initial.xsl
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslide/NEWS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslide/TODO
%dir %{_datadir}/xemacs/xemacs-packages/lisp/xslt-process/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslt-process/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xslt-process/README
%dir %{_datadir}/xemacs/xemacs-packages/lisp/xwem/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/xwem/ChangeLog
%dir %{_datadir}/xemacs/xemacs-packages/lisp/zenirc/
%doc %{_datadir}/xemacs/xemacs-packages/lisp/zenirc/BUGS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/zenirc/ChangeLog
%doc %{_datadir}/xemacs/xemacs-packages/lisp/zenirc/NEWS
%doc %{_datadir}/xemacs/xemacs-packages/lisp/zenirc/README
%doc %{_datadir}/xemacs/xemacs-packages/lisp/zenirc/TODO
%dir %{_datadir}/xemacs/xemacs-packages/man/
%doc %{_datadir}/xemacs/xemacs-packages/man/*
%dir %{_datadir}/xemacs/xemacs-packages/pkginfo/
%{_datadir}/xemacs/xemacs-packages/pkginfo/*

%files       -n xemacs-packages-info
%defattr(-,root,root)
%dir %{_datadir}/xemacs/mule-packages/info/
%doc %{_datadir}/xemacs/mule-packages/info/*
%dir %{_datadir}/xemacs/xemacs-packages/info/
%doc %{_datadir}/xemacs/xemacs-packages/info/*

%files       -n xemacs-packages-el -f xe-list-el-with-elc
%defattr(-,root,root)

%changelog
