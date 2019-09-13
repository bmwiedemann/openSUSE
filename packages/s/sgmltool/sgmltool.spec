#
# spec file for package sgmltool
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sgmltool
BuildRequires:  flex
BuildRequires:  groff
BuildRequires:  opensp
%if 0%{suse_version} > 1220
BuildRequires:  texlive-kpathsea
%endif
Provides:       sgml-tools
Requires:       opensp
Requires:       perl = %perl_version
Requires:       perl(Text::EntityMap)
%if 0%{suse_version} > 1220
Requires:       texlive-epsf
Requires:       texlive-latex
Requires:       texlive-url
%{expand: %%global _texmfmaindir %(kpsewhich -expand-var='$TEXMFMAIN')}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive
Requires(posttrans): texlive
%endif
Conflicts:      linuxdoc
Summary:        SGML-Tools - a Text-Formatting Package
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/SGML
Version:        1.0.9
Release:        0
Source:         ftp://ftp.nllgg.nl/pub2/SGMLtools/v1.0/sgml-tools-%{version}.tar.bz2
Source1:        lnd-1.0.tar.bz2
Patch:          sgml-tools-1.0.9.dif
Patch1:         sgml-tools-temp-vuln-1.0.9.diff
Patch2:         sgmltool-man-entities.diff
Patch3:         sgmltool-1.0.9-expandsyntax.diff
Patch4:         sgml-tools-1.0.9-destdir.diff
Patch5:         sgml-tools-retval.diff
Patch6:         cflags-sgml-tools-1.0.9.diff
Patch7:         sgml-tools-1.0.9-sgmlpre.diff
Patch8:         sgml-tools-1.0.9-strip.diff
Patch9:         sgml-tools-1.0.9-latex.diff
Patch10:        sgmltool-flex.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SGML-Tools is a text-formatting package based on SGML (Standard
Generalized Markup Language), which allows you to produce LaTeX, HTML,
GNU info, LyX, RTF, and plain ASCII documents (via groff) from a single
source.

This system is tailored for writing technical software documentation,
an example of which is the Linux HOWTO documents. It should be useful
for all kinds of printed and online documentation.

This package is the successor to the Linuxdoc package.

SGML-Tools cannot process arbitrary SGML documents. In such a case, try
jade_dsl and write your own DSSSL scripts (take the docbk30 package as
an example).

%define INSTALL install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define GZIP gzip --best --force

%prep
%setup -q -n sgml-tools-%{version} -a1
%patch
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1
%patch4 -p 1
%patch5
%patch6 -p 1
%patch7 -p 1
%patch8
%if 0%{suse_version} > 1220
%patch9
%if 0%{suse_version} <= 1320
%patch10 -p1
%endif
%endif

%build
export CFLAGS="%optflags -fno-strict-aliasing"
%configure --prefix="%buildroot/%_prefix" \
            --with-installed-nsgmls
make %{?_smp_mflags}
make install DESTDIR="%buildroot" prefix="%_prefix"
(cd doc; PATH="$PATH:%buildroot/%_bindir" sh Makedoc.sh)
cp -p doc/README doc/README.doc
# the Makefiles are a bit nasty
make clean
%configure \
            --with-installed-nsgmls
make %{?_smp_mflags}

%install
> doc/Makedoc.sh
make install DESTDIR="%buildroot";
rm -fr $RPM_BUILD_ROOT/usr/doc/sgml-tools
perlpath=`ls -1d /usr/lib/perl5/5.*/Text`
mkdir -p $RPM_BUILD_ROOT$perlpath
mv $RPM_BUILD_ROOT/usr/lib/perl5/Text/EntityMap.pm $RPM_BUILD_ROOT$perlpath/

%if 0%{suse_version} > 1220
%post
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr

%postun
if test $1 = 0; then
    %{_bindir}/mktexlsr 2> /dev/null || :
    exit 0
fi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr

%posttrans
VERBOSE=false %{_texmfmaindir}/texconfig/update || :
%endif

%files
%defattr(-,root,root)
%doc lnd-1.0
%doc COPYING BUGS CHANGES CONTRIBUTORS README TODO
%doc doc/README.doc doc/example.sgml doc/guide.info doc/guide.lyx
%doc doc/guide.ps.gz doc/guide.sgml doc/guide.txt
%doc doc/html doc/rtf
/usr/bin/sgmlsasp
/usr/bin/rtf2rtf
/usr/bin/sgmltools.v1
/usr/bin/sgml2html
/usr/bin/sgml2info
/usr/bin/sgml2latex
/usr/bin/sgml2lyx
/usr/bin/sgml2rtf
/usr/bin/sgml2txt
/usr/bin/sgmlcheck
/usr/bin/sgmlpre
%dir /usr/lib/entity-map
/usr/lib/entity-map/0.1.0
/usr/lib/perl5/5.*/Text/EntityMap.pm
%dir /usr/lib/sgml
/usr/lib/sgml-tools
/usr/lib/sgml/iso-entities-8879.1986
%if 0%{suse_version} > 1220
%{_texmfmaindir}/tex/latex/sgml-tools
%endif
%{_mandir}/man1/sgml2html.1.gz
%{_mandir}/man1/sgml2info.1.gz
%{_mandir}/man1/sgml2latex.1.gz
%{_mandir}/man1/sgml2lyx.1.gz
%{_mandir}/man1/sgml2rtf.1.gz
%{_mandir}/man1/sgml2txt.1.gz
%{_mandir}/man1/sgmlsasp.1.gz
%{_mandir}/man1/sgmlcheck.1.gz
%{_mandir}/man1/sgmltools.1.gz

%changelog
