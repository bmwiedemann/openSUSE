#
# spec file for package sgmltool
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           sgmltool
Version:        1.0.9
Release:        0
Summary:        SGML-Tools - a Text-Formatting Package
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/SGML
Source:         ftp://ftp.nllgg.nl/pub2/SGMLtools/v1.0/sgml-tools-%{version}.tar.bz2
Source1:        lnd-1.0.tar.bz2
Patch0:         sgml-tools-1.0.9.dif
Patch1:         sgml-tools-temp-vuln-1.0.9.diff
Patch2:         sgmltool-man-entities.diff
Patch3:         sgmltool-1.0.9-expandsyntax.diff
Patch4:         sgml-tools-1.0.9-destdir.diff
Patch5:         sgml-tools-retval.diff
Patch6:         cflags-sgml-tools-1.0.9.diff
Patch7:         sgml-tools-1.0.9-sgmlpre.diff
Patch8:         sgml-tools-1.0.9-strip.diff
Patch9:         sgml-tools-1.0.9-latex.diff
BuildRequires:  flex
BuildRequires:  groff
BuildRequires:  opensp
BuildRequires:  texlive-kpathsea
Requires:       opensp
Requires:       perl = %{perl_version}
Requires:       perl(Text::EntityMap)
Conflicts:      linuxdoc
Provides:       sgml-tools
%{expand: %%global _texmfmaindir %(kpsewhich -expand-var='$TEXMFMAIN')}

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

%package latex
Summary:        SGML-Tools - LaTeX generator
Group:          Productivity/Publishing/SGML
Requires:       sgmltool
Requires:       texlive-epsf
Requires:       texlive-latex
Requires:       texlive-url
Requires(post): coreutils
Requires(posttrans): texlive-filesystem
Requires(postun): coreutils
Requires(postun): texlive-kpathsea
Supplements:    (sgmltool and texlive-filesystem)
Provides:       sgmltool:%{_bindir}/sgml2latex

%description latex
This package contains the LaTeX generator (sgml2latex) from sgmltool.

%prep
%setup -q -n sgml-tools-%{version} -a1
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5
%patch6 -p1
%patch7 -p1
%patch8
%patch9

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --prefix="%{buildroot}/%{_prefix}" \
    --with-installed-nsgmls
make %{?_smp_mflags}
make %{?_smp_mflags} install DESTDIR=%{buildroot} prefix="%{_prefix}"
(cd doc; PATH="$PATH:%buildroot/%{_bindir}" sh Makedoc.sh)
cp -p doc/README doc/README.doc
# the Makefiles are a bit nasty
make %{?_smp_mflags} clean
%configure \
    --with-installed-nsgmls
make %{?_smp_mflags}

%install
> doc/Makedoc.sh
make install DESTDIR="%{buildroot}";
rm -fr %{buildroot}%{_prefix}/doc/sgml-tools
perlpath=`ls -1d %{_prefix}/lib/perl5/5.*/Text`
mkdir -p %{buildroot}$perlpath
mv %{buildroot}%{_prefix}/lib/perl5/Text/EntityMap.pm %{buildroot}$perlpath/

%post latex
mkdir -p %{_localstatedir}/run/texlive
> %{_localstatedir}/run/texlive/run-mktexlsr

%postun latex
if test $1 = 0; then
    %{_bindir}/mktexlsr 2> /dev/null || :
    exit 0
fi
mkdir -p %{_localstatedir}/run/texlive
> %{_localstatedir}/run/texlive/run-mktexlsr

%posttrans latex
VERBOSE=false %{_texmfmaindir}/texconfig/update || :

%files
%license COPYING
%doc lnd-1.0
%doc BUGS CHANGES CONTRIBUTORS README TODO
%doc doc/README.doc doc/example.sgml doc/html
%doc doc/guide.ps.gz doc/guide.sgml doc/guide.txt
%{_bindir}/sgmlsasp
%{_bindir}/rtf2rtf
%{_bindir}/sgmltools.v1
%{_bindir}/sgml2html
%{_bindir}/sgml2info
%{_bindir}/sgml2lyx
%{_bindir}/sgml2rtf
%{_bindir}/sgml2txt
%{_bindir}/sgmlcheck
%{_bindir}/sgmlpre
%dir %{_prefix}/lib/entity-map
%{_prefix}/lib/entity-map/0.1.0
%{_prefix}/lib/perl5/5.*/Text/EntityMap.pm
%dir %{_prefix}/lib/sgml
%{_prefix}/lib/sgml-tools
%{_prefix}/lib/sgml/iso-entities-8879.1986
%{_mandir}/man1/sgml2html.1%{?ext_man}
%{_mandir}/man1/sgml2info.1%{?ext_man}
%{_mandir}/man1/sgml2lyx.1%{?ext_man}
%{_mandir}/man1/sgml2rtf.1%{?ext_man}
%{_mandir}/man1/sgml2txt.1%{?ext_man}
%{_mandir}/man1/sgmlsasp.1%{?ext_man}
%{_mandir}/man1/sgmlcheck.1%{?ext_man}
%{_mandir}/man1/sgmltools.1%{?ext_man}

%files latex
%{_bindir}/sgml2latex
%{_texmfmaindir}/tex/latex/sgml-tools
%{_mandir}/man1/sgml2latex.1%{?ext_man}

%changelog
