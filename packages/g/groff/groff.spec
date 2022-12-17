#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "full"
%define name_ext -full
%bcond_without full_build
%else
%define name_ext %nil
%bcond_with full_build
%endif
Name:           groff%{name_ext}
Version:        1.22.4
Release:        0
Summary:        GNU troff Document Formatting System
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/Troff
URL:            http://www.gnu.org/software/groff/groff.html
Source0:        ftp://ftp.gnu.org/gnu/groff/groff-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/gnu/groff/groff-%{version}.tar.gz.sig
Source2:        groff.keyring
Source3:        zzz-groff.sh
Source4:        zzz-groff.csh
Patch0:         groff-1.20.1-nroff-empty-LANGUAGE.patch
Patch1:         groff-1.20.1-deunicode.patch
Patch2:         groff-1.21-CVE-2009-5044.patch
# http://cvsweb.openwall.com/cgi/cvsweb.cgi/Owl/packages/groff/groff-1.20.1-owl-tmp.diff?rev=1.2;content-type=text%2Fplain
Patch3:         groff-1.21-CVE-2009-5081.patch
# PATCH-FIX-OPENSUSE: FATE#312586
#  sent upstream http://lists.gnu.org/archive/html/bug-groff/2011-09/msg00002.html
Patch4:         0001-locale-support-in-papersize-definition.patch
Patch5:         0002-documentation-for-the-locale-keyword.patch
# change the papersize definition to force the locale usage
# it can be supressed by /etc/papersize if needed
Patch6:         groff-force-locale-usage.patch
Patch7:         0004-don-t-use-usr-bin-env-in-shebang.patch
# Patches from debian
Patch100:       https://salsa.debian.org/debian/groff/raw/master/debian/patches/bash-scripts.patch
Patch101:       https://salsa.debian.org/debian/groff/raw/master/debian/patches/sort-perl-hash-keys.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  distribution-release
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
%if %{with full_build}
BuildRequires:  ghostscript-library
BuildRequires:  groff
BuildRequires:  netpbm
BuildRequires:  psutils
BuildRequires:  pkgconfig(uchardet)
# for gxditview and X fontx
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Requires:       ghostscript-library
# ghostscript-library pulls in X and stuff anyways, so let's
# piggyback on that one
Supplements:    packageand(groff:ghostscript-library)
# requires the -base package
Requires:       groff = %{version}
Requires:       netpbm
Requires:       psutils
Requires(post): %{install_info_prereq}
Provides:       jgroff = %{version}-%{release}
Provides:       normal-groff = %{version}-%{release}
Obsoletes:      jgroff < %{version}
# X fonts were moved back
Provides:       groff-devx = %{version}-%{release}
Obsoletes:      groff-devx <= 1.21
# alternatives
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif

%description
The groff package is a stripped-down package containing the necessary
components to read manual pages in ASCII, Latin-1, and UTF-8, plus the
PostScript device (groff's default).

%package -n groff-doc
Summary:        HTML documentation and examples for groff
Group:          Productivity/Publishing/Troff
BuildArch:      noarch

%description -n groff-doc
The groff package provides compatible versions of troff, nroff, eqn,
tbl, and other Unix text formatting utilities.

Groff is used to "compile" man pages stored in groff or nroff format
for different output devices, for example, displaying to a screen or in
PostScript format for printing on a PostScript printer.

%package -n gxditview
Summary:        Ditroff Output Displayer for Groff
Group:          Productivity/Publishing/Troff
Requires:       groff-full = %{version}
# bnc#668254
Supplements:    packageand(groff:xorg-x11-libX11)
Conflicts:      jgxdview
Provides:       gxdview = %{version}-%{release}
Obsoletes:      gxdview < %{version}

%description -n gxditview
This version of xditview is called gxditview and has some extensions
used by the groff command.  gxditview is used by groff if called with
the -X option.

%prep
%setup -q -n groff-%{version}
%autopatch -p1

# remove hardcoded docdir
sed -i \
    -e '/^docdir=/d' \
    Makefile.am

%build
# bsc#1185613
. /etc/os-release
sed -i "s:\(doc-volume-operating-system\) BSD:\1 $PRETTY_NAME:" tmac/doc-common-u
sed -i "s:\(doc-default-operating-system\) BSD:\1 $PRETTY_NAME:" tmac/doc-common-u
# -----------
autoreconf -fvi
# libdir redefined as it is just bunch of perl scripts
%configure \
    --disable-silent-rules \
    --docdir=%{_defaultdocdir}/groff \
    --libdir=%{_libexecdir} \
    --with-appresdir=%{_datadir}/X11/app-defaults \
    --with-grofferdir=%{_libexecdir}/groff/groffer
make %{?_smp_mflags}

%install
%make_install

%if %{with full_build}
# remove groff basic files from bellow
rm -f %{buildroot}%{_sysconfdir}/profile.d/zzz-groff.csh
rm -f %{buildroot}%{_sysconfdir}/profile.d/zzz-groff.sh
rm -f %{buildroot}%{_bindir}/eqn
rm -f %{buildroot}%{_bindir}/groff
rm -f %{buildroot}%{_bindir}/grog
rm -f %{buildroot}%{_bindir}/grops
rm -f %{buildroot}%{_bindir}/grotty
rm -f %{buildroot}%{_bindir}/mmroff
rm -f %{buildroot}%{_bindir}/neqn
rm -f %{buildroot}%{_bindir}/nroff
rm -f %{buildroot}%{_bindir}/pic
rm -f %{buildroot}%{_bindir}/preconv
rm -f %{buildroot}%{_bindir}/soelim
rm -f %{buildroot}%{_bindir}/tbl
rm -f %{buildroot}%{_bindir}/troff
rm -f %{buildroot}%{_libexecdir}/groff/grog/subs.pl
rm -f %{buildroot}%{_datadir}/groff/current
rm -f %{buildroot}%{_datadir}/groff/1.22.4/eign
rm -rf %{buildroot}%{_datadir}/groff/1.22.4/font/devascii
rm -rf %{buildroot}%{_datadir}/groff/1.22.4/font/devlatin1
rm -rf %{buildroot}%{_datadir}/groff/1.22.4/font/devps
rm -rf %{buildroot}%{_datadir}/groff/1.22.4/font/devutf8
rm -rf %{buildroot}%{_datadir}/groff/1.22.4/pic
rm -rf %{buildroot}%{_datadir}/groff/1.22.4/tmac
rm -rf %{buildroot}%{_datadir}/groff/site-tmac
rm -rf %{buildroot}%{_datadir}/groff/site-font
rm -f %{buildroot}%{_mandir}/man1/eqn.1*
rm -f %{buildroot}%{_mandir}/man1/groff.1*
rm -f %{buildroot}%{_mandir}/man1/grog.1*
rm -f %{buildroot}%{_mandir}/man1/grops.1*
rm -f %{buildroot}%{_mandir}/man1/grotty.1*
rm -f %{buildroot}%{_mandir}/man1/mmroff.1*
rm -f %{buildroot}%{_mandir}/man1/neqn.1*
rm -f %{buildroot}%{_mandir}/man1/nroff.1*
rm -f %{buildroot}%{_mandir}/man1/pic.1*
rm -f %{buildroot}%{_mandir}/man1/preconv.1*
rm -f %{buildroot}%{_mandir}/man1/soelim.1*
rm -f %{buildroot}%{_mandir}/man1/tbl.1*
rm -f %{buildroot}%{_mandir}/man1/troff.1*

# Prepare alternatives
find %{buildroot}%{_mandir}
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
mv -v %{buildroot}%{_mandir}/man7/roff.7* \
    %{buildroot}%{_mandir}/man7/roff-gf.7%{?ext_man}
ln -s -f %{_sysconfdir}/alternatives/roff.7%{?ext_man} \
    %{buildroot}%{_mandir}/man7/roff.7%{?ext_man}
# full_build
%else
# fix permission for devps/generate/afmname
# used by ghostscript-fonts-grops
chmod +x %{buildroot}%{_datadir}/groff/%{version}/font/devps/generate/afmname
# install files needed by ghostscript-fonts-grops
install -m 0644 font/devps/generate/symbolsl.awk %{buildroot}%{_datadir}/groff/%{version}/font/devps/generate
install -m 0644 font/devps/generate/zapfdr.sed %{buildroot}%{_datadir}/groff/%{version}/font/devps/generate
install -m 0644 font/devps/generate/freeeuro.sfd %{buildroot}%{_datadir}/groff/%{version}/font/devps/generate
install -m 0644 font/devps/generate/sfdtopfa.pe %{buildroot}%{_datadir}/groff/%{version}/font/devps/generate
install -m 0644 font/devps/symbolsl.ps %{buildroot}%{_datadir}/groff/%{version}/font/devps/
# remove all not really wanted files (they are present in -full variant)
rm -rf %{buildroot}%{_mandir}/man5/
rm -rf %{buildroot}%{_mandir}/man7/
rm -rf %{buildroot}%{_infodir}/

rm -rf %{buildroot}%{_libexecdir}/groff/groffer/
rm -rf %{buildroot}%{_libexecdir}/groff/gpinyin/
rm -rf %{buildroot}%{_libexecdir}/groff/glilypond/
rm -f %{buildroot}%{_libexecdir}/groff/{groff_opts_no_arg.txt,groff_opts_with_arg.txt}

rm -rf %{buildroot}%{_docdir}/groff

rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/font/devcp1047
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/font/devdvi
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/font/devhtml
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/font/devlbp
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/font/devlj4
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/font/devpdf
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/oldfont/

for i in addftinfo afmtodit chem eqn2graph gdiffmk glilypond gperl gpinyin grap2graph grn grodvi groffer grolbp grolj4 gropdf hpftodit indxbib lkbib lookbib pdfmom pdfroff pfbtops pic2graph post-grohtml pre-grohtml refer roff2dvi roff2html roff2pdf roff2ps roff2text roff2x tfmtodit; do
  rm -f %{buildroot}%{_bindir}/$i
  rm -f %{buildroot}%{_mandir}/man1/$i.1*
done
# this man does werdly not have reflecting binary
rm -f %{buildroot}%{_mandir}/man1/grohtml.1*

# compat symlinks
ln -s -f eqn %{buildroot}%{_bindir}/geqn
ln -s -f tbl %{buildroot}%{_bindir}/gtbl

# install profiles to disable the use of ANSI colour sequences by default:
install -d -m 0755 %{buildroot}/%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{SOURCE4} %{buildroot}/%{_sysconfdir}/profile.d/

# full_build
%endif

%fdupes -s %{buildroot}

%if %{with full_build}
%post -n groff-full
%install_info --info-dir=%{_infodir} %{_infodir}/groff.info.gz
if test -f %{_mandir}/man7/roff-gf.7%{?ext_man} ; then
   update-alternatives --install \
      %{_mandir}/man7/roff.7%{?ext_man} roff.7%{?ext_man} \
          %{_mandir}/man7/roff-gf.7%{?ext_man} 500
fi

%preun -n groff-full
%install_info_delete --info-dir=%{_infodir} %{_infodir}/groff.info.gz
if [ $1 -eq 0 ] ; then
   update-alternatives --remove man.7%{?ext_man} %{_mandir}/man7/man-gf.7%{?ext_man}
fi
%endif

%if !%{with full_build}
%files
%license COPYING FDL LICENSES
%doc BUG-REPORT ChangeLog* MANIFEST MORE.STUFF NEWS PROBLEMS PROJECTS README
%{_bindir}/eqn
%{_bindir}/geqn
%{_bindir}/groff
%{_bindir}/grog
%{_bindir}/grops
%{_bindir}/grotty
%{_bindir}/gtbl
%{_bindir}/mmroff
%{_bindir}/neqn
%{_bindir}/nroff
%{_bindir}/pic
%{_bindir}/preconv
%{_bindir}/soelim
%{_bindir}/tbl
%{_bindir}/troff
%{_mandir}/man1/eqn.1%{?ext_man}
%{_mandir}/man1/groff.1%{?ext_man}
%{_mandir}/man1/grog.1%{?ext_man}
%{_mandir}/man1/grops.1%{?ext_man}
%{_mandir}/man1/grotty.1%{?ext_man}
%{_mandir}/man1/mmroff.1%{?ext_man}
%{_mandir}/man1/neqn.1%{?ext_man}
%{_mandir}/man1/nroff.1%{?ext_man}
%{_mandir}/man1/pic.1%{?ext_man}
%{_mandir}/man1/preconv.1%{?ext_man}
%{_mandir}/man1/soelim.1%{?ext_man}
%{_mandir}/man1/tbl.1%{?ext_man}
%{_mandir}/man1/troff.1%{?ext_man}
%config %{_sysconfdir}/profile.d/zzz-%{name}.*sh
%{_datadir}/%{name}
%dir %{_libexecdir}/groff
%dir %{_libexecdir}/groff/grog
%{_libexecdir}/groff/grog/subs.pl
%{_datadir}/groff/current

%else #groff_base_only

%files -n groff-full
%dir %{_datadir}/groff/%{version}
%dir %{_libexecdir}/groff
%doc %{_docdir}/groff
%dir %{_libexecdir}/groff
%dir %{_libexecdir}/groff/glilypond
%{_libexecdir}/groff/glilypond/args.pl
%{_libexecdir}/groff/glilypond/oop_fh.pl
%{_libexecdir}/groff/glilypond/subs.pl
%dir %{_libexecdir}/groff/gpinyin
%{_libexecdir}/groff/gpinyin/subs.pl
%{_libexecdir}/groff/groff_opts_no_arg.txt
%{_libexecdir}/groff/groff_opts_with_arg.txt
%exclude %{_docdir}/groff/html
%exclude %{_docdir}/groff/examples
%{_infodir}/groff*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%exclude %{_mandir}/man1/gxditview.1*
%ghost %{_sysconfdir}/alternatives/roff.7%{?ext_man}
%{_bindir}/*
%exclude %{_bindir}/gxditview
%dir %{_datadir}/groff
%{_datadir}/groff/%{version}/font
%{_datadir}/groff/%{version}/oldfont
%{_libexecdir}/groff/groffer

%files -n groff-doc
%dir %{_docdir}/groff
%doc %{_docdir}/groff/html
%doc %{_docdir}/groff/examples

%files -n gxditview
%dir %{_datadir}/X11/app-defaults
%doc src/devices/xditview/ChangeLog
%doc src/devices/xditview/README
%doc src/devices/xditview/TODO
%{_bindir}/gxditview
%{_mandir}/man1/gxditview.1%{?ext_man}
%{_datadir}/X11/app-defaults/GXditview
%{_datadir}/X11/app-defaults/GXditview-color

%endif #groff_base_only

%changelog
