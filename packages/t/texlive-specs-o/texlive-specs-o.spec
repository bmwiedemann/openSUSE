#
# spec file for package texlive-specs-o
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


%bcond_with	zypper_posttrans

%define texlive_version  2020
%define texlive_previous 2019
%define texlive_release  20200327
%define texlive_noarch   176

#!BuildIgnore:          texlive
#!BuildIgnore:          texlive-scripts
#!BuildIgnore:          texlive-scripts-extra
#!BuildIgnore:          texlive-scripts-bin
#!BuildIgnore:          texlive-scripts-extra-bin
#!BuildIgnore:          texlive-gsftopk
#!BuildIgnore:          texlive-gsftopk-bin
#!BuildIgnore:          texlive-kpathsea
#!BuildIgnore:          texlive-kpathsea-bin

%global _varlib         %{_localstatedir}/lib
%global _libexecdir     %{_prefix}/lib

%define _texmfdistdir   %{_datadir}/texmf
%if 0%{texlive_version} >= 2013
%define _texmfmaindir   %{_texmfdistdir}
%define _texmfdirs      %{_texmfdistdir}
%else
%define _texmfmaindir   %{_libexecdir}/texmf
%define _texmfdirs      \{%{_texmfdistdir},%{_texmfmaindir}\}
%endif

%define _texmfconfdir   %{_sysconfdir}/texmf
%define _texmfvardir    %{_varlib}/texmf
%define _texmfcache     %{_localstatedir}/cache/texmf
%define _fontcache      %{_texmfcache}/fonts
#
%define _x11bin         %{_prefix}/bin
%define _x11lib         %{_libdir}
%define _x11data        %{_datadir}/X11
%define _x11inc         %{_includedir}
%define _appdefdir      %{_x11data}/app-defaults

Name:           texlive-specs-o
Version:        2020
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for o
License:        BSD-3-Clause and GFDL-1.2 and GPL-2.0+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain and SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-o-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-lshort-slovak
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Slovak introduction to LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source1:        lshort-slovak.doc.tar.xz

%description -n texlive-lshort-slovak
A Slovak translation of Oetiker's (not so) short introduction.
%post -n texlive-lshort-slovak
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lshort-slovak 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lshort-slovak
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lshort-slovak
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lshort-slovak/slshorte.pdf
%{_texmfdistdir}/doc/latex/lshort-slovak/src.zip
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lshort-slovak-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-lshort-slovenian
Version:        %{texlive_version}.%{texlive_noarch}.4.20svn15878
Release:        0
Summary:        Slovenian translation of lshort
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source2:        lshort-slovenian.doc.tar.xz

%description -n texlive-lshort-slovenian
A Slovenian translation of the Not So Short Introduction to
LaTeX 2e.
%post -n texlive-lshort-slovenian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lshort-slovenian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lshort-slovenian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lshort-slovenian
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lshort-slovenian/README
%{_texmfdistdir}/doc/latex/lshort-slovenian/lshort-slovenian.pdf
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/biblio.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/contrib.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/custom.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/fancyhea.sty
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/graphic.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-a5.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-base.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-slovenian.sty
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/lshort-slovenian.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/lssym.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/math.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/mylayout.sty
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/overview.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/spec.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/things.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/title.tex
%{_texmfdistdir}/doc/latex/lshort-slovenian/src/typeset.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lshort-slovenian-%{texlive_version}.%{texlive_noarch}.4.20svn15878-%{release}-zypper
%endif

%package -n texlive-lshort-spanish
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn35050
Release:        0
Summary:        Short introduction to LaTeX, Spanish translation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source3:        lshort-spanish.doc.tar.xz

%description -n texlive-lshort-spanish
A Spanish translation of the Short Introduction to LaTeX2e,
version 20.
%post -n texlive-lshort-spanish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lshort-spanish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lshort-spanish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lshort-spanish
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/CAMBIOS
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/LEAME.utf8
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/MANIFEST
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/IEEEtrantools.sty
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/biblio.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/contrib.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/custom.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/fancyhea.sty
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/graphic.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-a4.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-a5.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-base.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort-letter.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort.ist
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lshort.sty
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/lssym.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/math.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/mylayout.sty
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/overview.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/spec.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/things.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/title.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/fuente/src/typeset.tex
%{_texmfdistdir}/doc/latex/lshort-spanish/lshort-a4.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lshort-spanish-%{texlive_version}.%{texlive_noarch}.0.0.5svn35050-%{release}-zypper
%endif

%package -n texlive-lshort-thai
Version:        %{texlive_version}.%{texlive_noarch}.1.32svn15878
Release:        0
Summary:        Introduction to LaTeX in Thai
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source4:        lshort-thai.doc.tar.xz

%description -n texlive-lshort-thai
This is the Thai translation of the Short Introduction to
LaTeX2e.
%post -n texlive-lshort-thai
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lshort-thai 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lshort-thai
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lshort-thai
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lshort-thai/lsh132.pdf
%{_texmfdistdir}/doc/latex/lshort-thai/lsh132.zip
%{_texmfdistdir}/doc/latex/lshort-thai/readme
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lshort-thai-%{texlive_version}.%{texlive_noarch}.1.32svn15878-%{release}-zypper
%endif

%package -n texlive-lshort-turkish
Version:        %{texlive_version}.%{texlive_noarch}.4.20svn15878
Release:        0
Summary:        Turkish introduction to LaTeX
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source5:        lshort-turkish.doc.tar.xz

%description -n texlive-lshort-turkish
A Turkish translation of Oetiker's (not so) short introduction.
%post -n texlive-lshort-turkish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lshort-turkish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lshort-turkish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lshort-turkish
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lshort-turkish/README
%{_texmfdistdir}/doc/latex/lshort-turkish/lshort-tr.pdf
%{_texmfdistdir}/doc/latex/lshort-turkish/trlshort-src.zip
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lshort-turkish-%{texlive_version}.%{texlive_noarch}.4.20svn15878-%{release}-zypper
%endif

%package -n texlive-lshort-ukr
Version:        %{texlive_version}.%{texlive_noarch}.4.00svn15878
Release:        0
Summary:        Ukrainian version of the LaTeX introduction
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source6:        lshort-ukr.doc.tar.xz

%description -n texlive-lshort-ukr
Ukrainian version of A Short Introduction to LaTeX2e.
%post -n texlive-lshort-ukr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lshort-ukr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lshort-ukr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lshort-ukr
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lshort-ukr/lshort-ukr-4.12.src.tar.gz
%{_texmfdistdir}/doc/latex/lshort-ukr/lshort-ukr.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lshort-ukr-%{texlive_version}.%{texlive_noarch}.4.00svn15878-%{release}-zypper
%endif

%package -n texlive-lshort-vietnamese
Version:        %{texlive_version}.%{texlive_noarch}.4.00svn15878
Release:        0
Summary:        Vietnamese version of the LaTeX introduction
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source7:        lshort-vietnamese.doc.tar.xz

%description -n texlive-lshort-vietnamese
Vietnamese version of A Short Introduction to LaTeX2e.
%post -n texlive-lshort-vietnamese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lshort-vietnamese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lshort-vietnamese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lshort-vietnamese
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lshort-vietnamese/README
%{_texmfdistdir}/doc/latex/lshort-vietnamese/lshort-vi.pdf
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/LocalVariables
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/Makefile
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/README.txt
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/abbr.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/biblio.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/contrib.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/custom.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/fancyhea.sty
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/graphic.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lshort-print-vi.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lshort-vi.sty
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lshort-vi.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/lssym.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/math.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/mylayout.sty
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/overview.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/spec.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/things.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/tiengviet.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/title.tex
%{_texmfdistdir}/doc/latex/lshort-vietnamese/src/typeset.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lshort-vietnamese-%{texlive_version}.%{texlive_noarch}.4.00svn15878-%{release}-zypper
%endif

%package -n texlive-lstaddons
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn26196
Release:        0
Summary:        Add-on packages for listings: autogobble and line background
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lstaddons-doc >= %{texlive_version}
Provides:       tex(lstautogobble.sty)
Provides:       tex(lstlinebgrd.sty)
Requires:       tex(listings.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source8:        lstaddons.tar.xz
Source9:        lstaddons.doc.tar.xz

%description -n texlive-lstaddons
The bundle contains a small collection of add-on packages for
the listings package. Current packages are: lstlinebgrd: colour
the background of some or all lines of a listing; and
lstautogobble: set the standard "gobble" option to the indent
of the first line of the code.

%package -n texlive-lstaddons-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn26196
Release:        0
Summary:        Documentation for texlive-lstaddons
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lstaddons-doc
This package includes the documentation for texlive-lstaddons

%post -n texlive-lstaddons
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lstaddons 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lstaddons
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lstaddons-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lstaddons/README
%{_texmfdistdir}/doc/latex/lstaddons/lstautogobble.pdf
%{_texmfdistdir}/doc/latex/lstaddons/lstlinebgrd.pdf

%files -n texlive-lstaddons
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/lstaddons/lstautogobble.sty
%{_texmfdistdir}/tex/latex/lstaddons/lstlinebgrd.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lstaddons-%{texlive_version}.%{texlive_noarch}.0.0.1svn26196-%{release}-zypper
%endif

%package -n texlive-lstbayes
Version:        %{texlive_version}.%{texlive_noarch}.svn48160
Release:        0
Summary:        Listings language driver for Bayesian modeling languages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lstbayes-doc >= %{texlive_version}
Provides:       tex(lstbayes.sty)
Requires:       tex(listings.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source10:       lstbayes.tar.xz
Source11:       lstbayes.doc.tar.xz

%description -n texlive-lstbayes
The package provides language drivers for the listings package
for several languages not included in that package: BUGS, JAGS,
and Stan.

%package -n texlive-lstbayes-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn48160
Release:        0
Summary:        Documentation for texlive-lstbayes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lstbayes-doc
This package includes the documentation for texlive-lstbayes

%post -n texlive-lstbayes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lstbayes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lstbayes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lstbayes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lstbayes/Makefile
%{_texmfdistdir}/doc/latex/lstbayes/README.md
%{_texmfdistdir}/doc/latex/lstbayes/examples.pdf
%{_texmfdistdir}/doc/latex/lstbayes/examples.tex
%{_texmfdistdir}/doc/latex/lstbayes/lstbayes.pdf

%files -n texlive-lstbayes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/lstbayes/lstbayes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lstbayes-%{texlive_version}.%{texlive_noarch}.svn48160-%{release}-zypper
%endif

%package -n texlive-lstfiracode
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn49503
Release:        0
Summary:        Use Fira Code font for listings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lstfiracode-doc >= %{texlive_version}
Provides:       tex(lstfiracode.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source12:       lstfiracode.tar.xz
Source13:       lstfiracode.doc.tar.xz

%description -n texlive-lstfiracode
The lstfiracode package defines FiraCodeStyle for the use with
the listings package. This style contains almost all ligatures
in Nikita Prokopov's Fira Code family of fonts.

%package -n texlive-lstfiracode-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn49503
Release:        0
Summary:        Documentation for texlive-lstfiracode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lstfiracode-doc
This package includes the documentation for texlive-lstfiracode

%post -n texlive-lstfiracode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lstfiracode 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lstfiracode
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lstfiracode-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lstfiracode/README.md
%{_texmfdistdir}/doc/latex/lstfiracode/lstfiracode.pdf
%{_texmfdistdir}/doc/latex/lstfiracode/lstfiracode.tex

%files -n texlive-lstfiracode
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/lstfiracode/lstfiracode.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lstfiracode-%{texlive_version}.%{texlive_noarch}.0.0.1csvn49503-%{release}-zypper
%endif

%package -n texlive-lt3graph
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.9svn45913
Release:        0
Summary:        Provide a graph datastructure for experimental LaTeX3
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lt3graph-doc >= %{texlive_version}
Provides:       tex(lt3graph-dry.sty)
Provides:       tex(lt3graph-packagedoc.cls)
Provides:       tex(lt3graph.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(listings.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(needspace.sty)
Requires:       tex(noindentafter.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(withargs.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source14:       lt3graph.tar.xz
Source15:       lt3graph.doc.tar.xz

%description -n texlive-lt3graph
The package defines a 'graph' data structure, for use in
documents that are using the experimental LaTeX 3 syntax.

%package -n texlive-lt3graph-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.9svn45913
Release:        0
Summary:        Documentation for texlive-lt3graph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lt3graph-doc
This package includes the documentation for texlive-lt3graph

%post -n texlive-lt3graph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lt3graph 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lt3graph
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lt3graph-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lt3graph/README
%{_texmfdistdir}/doc/latex/lt3graph/lt3graph.pdf
%{_texmfdistdir}/doc/latex/lt3graph/lt3graph.tex

%files -n texlive-lt3graph
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/lt3graph/lt3graph-dry.sty
%{_texmfdistdir}/tex/latex/lt3graph/lt3graph-packagedoc.cls
%{_texmfdistdir}/tex/latex/lt3graph/lt3graph.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lt3graph-%{texlive_version}.%{texlive_noarch}.0.0.1.9svn45913-%{release}-zypper
%endif

%package -n texlive-ltablex
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn34923
Release:        0
Summary:        Table package extensions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltablex-doc >= %{texlive_version}
Provides:       tex(ltablex.sty)
Requires:       tex(longtable.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source16:       ltablex.tar.xz
Source17:       ltablex.doc.tar.xz

%description -n texlive-ltablex
Modifies the tabularx environment to combine the features of
the tabularx package (auto-sized columns in a fixed width
table) with those of the longtable package (multi-page tables).

%package -n texlive-ltablex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn34923
Release:        0
Summary:        Documentation for texlive-ltablex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltablex-doc
This package includes the documentation for texlive-ltablex

%post -n texlive-ltablex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltablex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltablex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltablex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltablex/README
%{_texmfdistdir}/doc/latex/ltablex/ltablex.pdf
%{_texmfdistdir}/doc/latex/ltablex/ltablex.tex

%files -n texlive-ltablex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltablex/ltablex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltablex-%{texlive_version}.%{texlive_noarch}.1.1svn34923-%{release}-zypper
%endif

%package -n texlive-ltabptch
Version:        %{texlive_version}.%{texlive_noarch}.1.74dsvn17533
Release:        0
Summary:        Bug fix for longtable
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltabptch-doc >= %{texlive_version}
Provides:       tex(ltabptch.sty)
Requires:       tex(longtable.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source18:       ltabptch.tar.xz
Source19:       ltabptch.doc.tar.xz

%description -n texlive-ltabptch
A patch for LaTeX bugs tools/3180 and tools/3480. The patch
applies to version 4.11 of longtable.

%package -n texlive-ltabptch-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.74dsvn17533
Release:        0
Summary:        Documentation for texlive-ltabptch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltabptch-doc
This package includes the documentation for texlive-ltabptch

%post -n texlive-ltabptch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltabptch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltabptch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltabptch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltabptch/README
%{_texmfdistdir}/doc/latex/ltabptch/ltabptch.pdf
%{_texmfdistdir}/doc/latex/ltabptch/ltabptch.tex
%{_texmfdistdir}/doc/latex/ltabptch/ltabtest.tex

%files -n texlive-ltabptch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltabptch/ltabptch.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltabptch-%{texlive_version}.%{texlive_noarch}.1.74dsvn17533-%{release}-zypper
%endif

%package -n texlive-ltb2bib
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn43746
Release:        0
Summary:        Converts amsrefs' .ltb bibliographical databases to BibTeX format
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltb2bib-doc >= %{texlive_version}
Provides:       tex(ltb2bib.sty)
Requires:       tex(amsrefs.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source20:       ltb2bib.tar.xz
Source21:       ltb2bib.doc.tar.xz

%description -n texlive-ltb2bib
This package implements a LaTeX command that converts an
amsrefs bibliographical database (.ltb) to a BibTeX
bibliographical database (.bib). ltb2bib is the reverse of the
"amsxport" option in amsrefs. Typical uses are: produce bib
entries for some publishers which don't accept amsrefs (Taylor
& Francis, for example); import an ltb database in a database
management program, e.g. for sorting; access one's ltb database
within emacs's RefTeX mode.

%package -n texlive-ltb2bib-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn43746
Release:        0
Summary:        Documentation for texlive-ltb2bib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltb2bib-doc
This package includes the documentation for texlive-ltb2bib

%post -n texlive-ltb2bib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltb2bib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltb2bib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltb2bib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltb2bib/README
%{_texmfdistdir}/doc/latex/ltb2bib/bibdest.bib
%{_texmfdistdir}/doc/latex/ltb2bib/doltb2bib.tex
%{_texmfdistdir}/doc/latex/ltb2bib/ltb2bib.pdf
%{_texmfdistdir}/doc/latex/ltb2bib/ltbsource.ltb

%files -n texlive-ltb2bib
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltb2bib/ltb2bib.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltb2bib-%{texlive_version}.%{texlive_noarch}.0.0.01svn43746-%{release}-zypper
%endif

%package -n texlive-ltxcmds
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn53165
Release:        0
Summary:        Some LaTeX kernel commands for general use
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltxcmds-doc >= %{texlive_version}
Provides:       tex(ltxcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source22:       ltxcmds.tar.xz
Source23:       ltxcmds.doc.tar.xz

%description -n texlive-ltxcmds
This package exports some utility macros from the LaTeX kernel
into a separate namespace and also makes them available for
other formats such as plain TeX.

%package -n texlive-ltxcmds-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn53165
Release:        0
Summary:        Documentation for texlive-ltxcmds
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltxcmds-doc
This package includes the documentation for texlive-ltxcmds

%post -n texlive-ltxcmds
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxcmds 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxcmds
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxcmds-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltxcmds/README.md
%{_texmfdistdir}/doc/latex/ltxcmds/ltxcmds.pdf

%files -n texlive-ltxcmds
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/ltxcmds/ltxcmds.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxcmds-%{texlive_version}.%{texlive_noarch}.1.24svn53165-%{release}-zypper
%endif

%package -n texlive-ltxdockit
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn21869
Release:        0
Summary:        Documentation support
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltxdockit-doc >= %{texlive_version}
Provides:       tex(btxdockit.sty)
Provides:       tex(ltxdockit.cfg)
Provides:       tex(ltxdockit.cls)
Provides:       tex(ltxdockit.def)
Provides:       tex(ltxdockit.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(hypcap.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Requires:       tex(listings.sty)
Requires:       tex(multicol.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(textcomp.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source24:       ltxdockit.tar.xz
Source25:       ltxdockit.doc.tar.xz

%description -n texlive-ltxdockit
This bundle, consisting of a simple wrapper class and some
packages, forms a small LaTeX/BibTeX documentation kit; the
author uses it for some of his own packages. The package is not
supported: users should not attempt its use unless they are
capable of dealing with problems unaided. (The actual purpose
of releasing the package is to make it possible for third
parties to compile the documentation of other packages, should
that be necessary.)

%package -n texlive-ltxdockit-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn21869
Release:        0
Summary:        Documentation for texlive-ltxdockit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltxdockit-doc
This package includes the documentation for texlive-ltxdockit

%post -n texlive-ltxdockit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxdockit 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxdockit
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxdockit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltxdockit/README

%files -n texlive-ltxdockit
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltxdockit/btxdockit.sty
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.cfg
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.cls
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.def
%{_texmfdistdir}/tex/latex/ltxdockit/ltxdockit.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxdockit-%{texlive_version}.%{texlive_noarch}.1.2dsvn21869-%{release}-zypper
%endif

%package -n texlive-ltxfileinfo
Version:        %{texlive_version}.%{texlive_noarch}.2.04svn38663
Release:        0
Summary:        Print version information for a LaTeX file
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-ltxfileinfo-bin >= %{texlive_version}
#!BuildIgnore: texlive-ltxfileinfo-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltxfileinfo-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source26:       ltxfileinfo.tar.xz
Source27:       ltxfileinfo.doc.tar.xz

%description -n texlive-ltxfileinfo
ltxfileinfo displays version information for LaTeX files. If no
path information is given, the file is searched using
kpsewhich. As an extra, for developers, the script will (use
the --star or --color options) check the valididity of the
\Provides... statements in the files. The script uses code from
Uwe Luck's readprov.sty.

%package -n texlive-ltxfileinfo-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.04svn38663
Release:        0
Summary:        Documentation for texlive-ltxfileinfo
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltxfileinfo-doc
This package includes the documentation for texlive-ltxfileinfo

%post -n texlive-ltxfileinfo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxfileinfo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxfileinfo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxfileinfo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/ltxfileinfo/README
%{_texmfdistdir}/doc/support/ltxfileinfo/ltxfileinfo.pdf

%files -n texlive-ltxfileinfo
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/ltxfileinfo/ltxfileinfo
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxfileinfo-%{texlive_version}.%{texlive_noarch}.2.04svn38663-%{release}-zypper
%endif

%package -n texlive-ltxguidex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn50992
Release:        0
Summary:        An extended ltxguide class
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltxguidex-doc >= %{texlive_version}
Provides:       tex(ltxguidex.cls)
Requires:       tex(enumitem.sty)
Requires:       tex(framed.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ltxguide.cls)
Requires:       tex(showexpl.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source28:       ltxguidex.tar.xz
Source29:       ltxguidex.doc.tar.xz

%description -n texlive-ltxguidex
The ltxguidex document class extends ltxguide with a set of
environments and commands that make writing beautiful LaTeX
documentation easier and more natural.

%package -n texlive-ltxguidex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn50992
Release:        0
Summary:        Documentation for texlive-ltxguidex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltxguidex-doc
This package includes the documentation for texlive-ltxguidex

%post -n texlive-ltxguidex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxguidex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxguidex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxguidex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltxguidex/LICENSE.txt
%{_texmfdistdir}/doc/latex/ltxguidex/README.md
%{_texmfdistdir}/doc/latex/ltxguidex/ltxguidex.pdf
%{_texmfdistdir}/doc/latex/ltxguidex/ltxguidex.tex

%files -n texlive-ltxguidex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltxguidex/ltxguidex.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxguidex-%{texlive_version}.%{texlive_noarch}.0.0.2.0svn50992-%{release}-zypper
%endif

%package -n texlive-ltximg
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn51951
Release:        0
Summary:        Extract LaTeX environments into separate image files
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-ltximg-bin >= %{texlive_version}
#!BuildIgnore: texlive-ltximg-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltximg-doc >= %{texlive_version}
Requires:       perl(Archive::Tar)
#!BuildIgnore:  perl(Archive::Tar)
Requires:       perl(Config)
#!BuildIgnore:  perl(Config)
Requires:       perl(Cwd)
#!BuildIgnore:  perl(Cwd)
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Copy)
#!BuildIgnore:  perl(File::Copy)
Requires:       perl(File::Find)
#!BuildIgnore:  perl(File::Find)
Requires:       perl(File::Spec::Functions)
#!BuildIgnore:  perl(File::Spec::Functions)
Requires:       perl(File::Temp)
#!BuildIgnore:  perl(File::Temp)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(IO::Compress::Zip)
#!BuildIgnore:  perl(IO::Compress::Zip)
Requires:       perl(POSIX)
#!BuildIgnore:  perl(POSIX)
Requires:       perl(autodie)
#!BuildIgnore:  perl(autodie)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source30:       ltximg.tar.xz
Source31:       ltximg.doc.tar.xz

%description -n texlive-ltximg
ltximg is a Perl script that automates the process of
extracting and converting environments provided by TikZ,
PStricks and other packages from input file to image formats in
individual files using ghostscript and poppler-utils. It
generates a file with only extracted environments, and another
with environments converted to \includegraphics.

%package -n texlive-ltximg-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn51951
Release:        0
Summary:        Documentation for texlive-ltximg
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltximg-doc
This package includes the documentation for texlive-ltximg

%post -n texlive-ltximg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltximg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltximg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltximg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/ltximg/README.md
%{_texmfdistdir}/doc/support/ltximg/ltximg-doc.pdf

%files -n texlive-ltximg
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/ltximg/ltximg.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltximg-%{texlive_version}.%{texlive_noarch}.1.7svn51951-%{release}-zypper
%endif

%package -n texlive-ltxkeys
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.3csvn28332
Release:        0
Summary:        A robust key parser for LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltxkeys-doc >= %{texlive_version}
Provides:       tex(ltxkeys.sty)
Requires:       tex(catoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source32:       ltxkeys.tar.xz
Source33:       ltxkeys.doc.tar.xz

%description -n texlive-ltxkeys
The package provides facilities for creating and managing keys
in the sense of the keyval and xkeyval packages, but it is
intended to be more robust and faster. Its robustness comes
from its ability to preserve braces in key values throughout
parsing. The need to preserve braces in key values arises often
in parsing keys (for example, in the xwatermark package). The
package is faster than xkeyval package because (among other
things) it avoids character-wise parsing of key values (called
"selective sanitization" by the xkeyval package). The package
also provides functions for defining and managing keys.

%package -n texlive-ltxkeys-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.3csvn28332
Release:        0
Summary:        Documentation for texlive-ltxkeys
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltxkeys-doc
This package includes the documentation for texlive-ltxkeys

%post -n texlive-ltxkeys
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxkeys 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxkeys
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxkeys-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltxkeys/README
%{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide-table1.tex
%{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.cfg
%{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.pdf
%{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-guide.tex
%{_texmfdistdir}/doc/latex/ltxkeys/ltxkeys-test-20121122.tex

%files -n texlive-ltxkeys
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltxkeys/ltxkeys.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxkeys-%{texlive_version}.%{texlive_noarch}.0.0.0.3csvn28332-%{release}-zypper
%endif

%package -n texlive-ltxmisc
Version:        %{texlive_version}.%{texlive_noarch}.svn21927
Release:        0
Summary:        Miscellaneous LaTeX packages, etcetera
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(abstbook.cls)
Provides:       tex(beletter.cls)
Provides:       tex(bibcheck.sty)
Provides:       tex(concrete.sty)
Provides:       tex(flashcard.cls)
Provides:       tex(iagproc.cls)
Provides:       tex(linsys.sty)
Provides:       tex(mitpress.sty)
Provides:       tex(thrmappendix.sty)
Provides:       tex(topcapt.sty)
Provides:       tex(vrbexin.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(beton.sty)
Requires:       tex(calc.sty)
Requires:       tex(euler.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(letter.cls)
Requires:       tex(makeidx.sty)
Requires:       tex(minitoc.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pifont.sty)
Requires:       tex(report.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source34:       ltxmisc.tar.xz

%description -n texlive-ltxmisc
The ltxmisc package
%post -n texlive-ltxmisc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxmisc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxmisc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxmisc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltxmisc/abstbook.cls
%{_texmfdistdir}/tex/latex/ltxmisc/beletter.cls
%{_texmfdistdir}/tex/latex/ltxmisc/bibcheck.sty
%{_texmfdistdir}/tex/latex/ltxmisc/concrete.sty
%{_texmfdistdir}/tex/latex/ltxmisc/flashcard.cls
%{_texmfdistdir}/tex/latex/ltxmisc/iagproc.cls
%{_texmfdistdir}/tex/latex/ltxmisc/linsys.sty
%{_texmfdistdir}/tex/latex/ltxmisc/mitpress.sty
%{_texmfdistdir}/tex/latex/ltxmisc/thrmappendix.sty
%{_texmfdistdir}/tex/latex/ltxmisc/topcapt.sty
%{_texmfdistdir}/tex/latex/ltxmisc/vrbexin.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxmisc-%{texlive_version}.%{texlive_noarch}.svn21927-%{release}-zypper
%endif

%package -n texlive-ltxnew
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn21586
Release:        0
Summary:        A simple means of creating commands
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltxnew-doc >= %{texlive_version}
Provides:       tex(ltxnew.sty)
Requires:       tex(etex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source35:       ltxnew.tar.xz
Source36:       ltxnew.doc.tar.xz

%description -n texlive-ltxnew
The package ltxnew provides \new, \renew and \provide prefixes
for checking definitions. It is designed to work with e-TeX
distributions of LaTeX and relies on the LaTeX internal macro
\@ifdefinable. Local allocation of counters, dimensions, skips,
muskips, boxes, tokens and marks are provided by the etex
package. \new and \renew as well as \provide may be used for
all kind of control sequences. Please refer to the section
"Using \new" of the PDF documentation.

%package -n texlive-ltxnew-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn21586
Release:        0
Summary:        Documentation for texlive-ltxnew
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltxnew-doc
This package includes the documentation for texlive-ltxnew

%post -n texlive-ltxnew
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxnew 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxnew
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxnew-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltxnew/README
%{_texmfdistdir}/doc/latex/ltxnew/ltxnew.pdf

%files -n texlive-ltxnew
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltxnew/ltxnew.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxnew-%{texlive_version}.%{texlive_noarch}.1.3svn21586-%{release}-zypper
%endif

%package -n texlive-ltxtools
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.1asvn24897
Release:        0
Summary:        A collection of LaTeX API macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ltxtools-doc >= %{texlive_version}
Provides:       tex(ltxtools-base.sty)
Provides:       tex(ltxtools-doc.sty)
Provides:       tex(ltxtools-environ.sty)
Provides:       tex(ltxtools-incluput.sty)
Provides:       tex(ltxtools-index.sty)
Provides:       tex(ltxtools-review.sty)
Provides:       tex(ltxtools-trace.sty)
Provides:       tex(ltxtools.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(catoptions.sty)
Requires:       tex(fp.sty)
Requires:       tex(ltxkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source37:       ltxtools.tar.xz
Source38:       ltxtools.doc.tar.xz

%description -n texlive-ltxtools
This is a bundle of macros that the author uses in the coding
of others of his macro files.

%package -n texlive-ltxtools-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.1asvn24897
Release:        0
Summary:        Documentation for texlive-ltxtools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ltxtools-doc
This package includes the documentation for texlive-ltxtools

%post -n texlive-ltxtools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ltxtools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ltxtools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ltxtools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ltxtools/README

%files -n texlive-ltxtools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-base.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-doc.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-environ.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-incluput.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-index.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-review.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools-trace.sty
%{_texmfdistdir}/tex/latex/ltxtools/ltxtools.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ltxtools-%{texlive_version}.%{texlive_noarch}.0.0.0.1asvn24897-%{release}-zypper
%endif

%package -n texlive-lua-alt-getopt
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn29349
Release:        0
Summary:        Process application arguments the same way as getopt_long
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lua-alt-getopt-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source39:       lua-alt-getopt.tar.xz
Source40:       lua-alt-getopt.doc.tar.xz

%description -n texlive-lua-alt-getopt
lua_altgetopt is a MIT-licensed module for Lua, for processing
application arguments in the same way as BSD/GNU getopt_long(3)
functions do. This module is made available for lua script
writers to have consistent command line parsing routines.

%package -n texlive-lua-alt-getopt-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn29349
Release:        0
Summary:        Documentation for texlive-lua-alt-getopt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lua-alt-getopt-doc
This package includes the documentation for texlive-lua-alt-getopt

%post -n texlive-lua-alt-getopt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lua-alt-getopt 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lua-alt-getopt
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lua-alt-getopt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/lua-alt-getopt/ChangeLog
%{_texmfdistdir}/doc/support/lua-alt-getopt/Makefile
%{_texmfdistdir}/doc/support/lua-alt-getopt/NEWS
%{_texmfdistdir}/doc/support/lua-alt-getopt/README
%{_texmfdistdir}/doc/support/lua-alt-getopt/alt_getopt
%{_texmfdistdir}/doc/support/lua-alt-getopt/tests/test.out
%{_texmfdistdir}/doc/support/lua-alt-getopt/tests/test.sh

%files -n texlive-lua-alt-getopt
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/lua-alt-getopt/alt_getopt.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lua-alt-getopt-%{texlive_version}.%{texlive_noarch}.0.0.7.0svn29349-%{release}-zypper
%endif

%package -n texlive-lua-check-hyphen
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7asvn47527
Release:        0
Summary:        Mark hyphenations in a document, for checking
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lua-check-hyphen-doc >= %{texlive_version}
Provides:       tex(lua-check-hyphen.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(luatexbase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source41:       lua-check-hyphen.tar.xz
Source42:       lua-check-hyphen.doc.tar.xz

%description -n texlive-lua-check-hyphen
The package looks at all hyphenation breaks in the document,
comparing them against a white-list prepared by the author. If
a hyphenation break is found, for which there is no entry in
the white-list, the package flags the line where the break
starts. The author may then either add the hyphenation to the
white-list, or adjust the document to avoid the break.

%package -n texlive-lua-check-hyphen-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7asvn47527
Release:        0
Summary:        Documentation for texlive-lua-check-hyphen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lua-check-hyphen-doc
This package includes the documentation for texlive-lua-check-hyphen

%post -n texlive-lua-check-hyphen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lua-check-hyphen 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lua-check-hyphen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lua-check-hyphen-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/README.md
%{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/luacheckhyphenmanual.pdf
%{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/luacheckhyphenmanual.tex
%{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/mit-license.txt
%{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/sample.pdf
%{_texmfdistdir}/doc/lualatex/lua-check-hyphen/doc/sample.tex

%files -n texlive-lua-check-hyphen
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/lua-check-hyphen/lua-check-hyphen.lua
%{_texmfdistdir}/tex/lualatex/lua-check-hyphen/lua-check-hyphen.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lua-check-hyphen-%{texlive_version}.%{texlive_noarch}.0.0.7asvn47527-%{release}-zypper
%endif

%package -n texlive-lua-uca
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn54550
Release:        0
Summary:        Unicode Collation Algorithm library for Lua
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lua-uca-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source43:       lua-uca.source.tar.xz
Source44:       lua-uca.doc.tar.xz

%description -n texlive-lua-uca
The Lua-UCA library provides basic support for Unicode
Collation Algorithm in Lua. It can be used to sort arrays of
strings according to rules of particular languages. It can be
used in other Lua projects that need to sort text in a language
dependent way, like indexing processors, bibliographic
generators, etc

%package -n texlive-lua-uca-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn54550
Release:        0
Summary:        Documentation for texlive-lua-uca
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lua-uca-doc
This package includes the documentation for texlive-lua-uca

%post -n texlive-lua-uca
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lua-uca 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lua-uca
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lua-uca-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/lua-uca/CHANGELOG.md
%{_texmfdistdir}/doc/support/lua-uca/LICENSE
%{_texmfdistdir}/doc/support/lua-uca/README.md
%{_texmfdistdir}/doc/support/lua-uca/lua-uca-doc.pdf
%{_texmfdistdir}/doc/support/lua-uca/lua-uca-doc.tex

%files -n texlive-lua-uca
%defattr(-,root,root,755)
%{_texmfdistdir}/source/support/lua-uca/lua-uca-collator.lua
%{_texmfdistdir}/source/support/lua-uca/lua-uca-ducet.lua
%{_texmfdistdir}/source/support/lua-uca/lua-uca-languages.lua
%{_texmfdistdir}/source/support/lua-uca/lua-uca-reordering-table.lua
%{_texmfdistdir}/source/support/lua-uca/lua-uca-tailoring.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lua-uca-%{texlive_version}.%{texlive_noarch}.0.0.1svn54550-%{release}-zypper
%endif

%package -n texlive-lua-ul
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.4svn54690
Release:        0
Summary:        Underlining for LuaLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lua-ul-doc >= %{texlive_version}
Provides:       tex(docstrip-luacode.sty)
Provides:       tex(lua-ul.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source45:       lua-ul.tar.xz
Source46:       lua-ul.doc.tar.xz

%description -n texlive-lua-ul
This package provides underlining, strikethough, and
highlighting using features in LuaLaTeX which avoid the
restrictions imposed by other methods. In particular, kerning
is not affected, the underlined text can use arbitrary
commands, hyphenation works etc. The package requires LuaTeX
version [?] 1.12.0.

%package -n texlive-lua-ul-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.4svn54690
Release:        0
Summary:        Documentation for texlive-lua-ul
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lua-ul-doc
This package includes the documentation for texlive-lua-ul

%post -n texlive-lua-ul
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lua-ul 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lua-ul
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lua-ul-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/lua-ul/README
%{_texmfdistdir}/doc/lualatex/lua-ul/lua-ul.pdf

%files -n texlive-lua-ul
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/lua-ul/docstrip-luacode.sty
%{_texmfdistdir}/tex/lualatex/lua-ul/lua-ul.lua
%{_texmfdistdir}/tex/lualatex/lua-ul/lua-ul.sty
%{_texmfdistdir}/tex/lualatex/lua-ul/pre_append_to_vlist_filter.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lua-ul-%{texlive_version}.%{texlive_noarch}.0.0.0.4svn54690-%{release}-zypper
%endif

%package -n texlive-lua-visual-debug
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn49634
Release:        0
Summary:        Visual debugging with LuaLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lua-visual-debug-doc >= %{texlive_version}
Provides:       tex(lua-visual-debug.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(ifluatex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source47:       lua-visual-debug.tar.xz
Source48:       lua-visual-debug.doc.tar.xz

%description -n texlive-lua-visual-debug
The package uses lua code to provide visible indications of
boxes, glues, kerns and penalties in the PDF output. The
package is known to work in LaTeX and Plain TeX documents.

%package -n texlive-lua-visual-debug-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn49634
Release:        0
Summary:        Documentation for texlive-lua-visual-debug
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lua-visual-debug-doc
This package includes the documentation for texlive-lua-visual-debug

%post -n texlive-lua-visual-debug
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lua-visual-debug 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lua-visual-debug
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lua-visual-debug-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/lua-visual-debug/README.md
%{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebug-doc.pdf
%{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebug-doc.tex
%{_texmfdistdir}/doc/luatex/lua-visual-debug/lvdebugdetail1-num.png
%{_texmfdistdir}/doc/luatex/lua-visual-debug/sample-plain.pdf
%{_texmfdistdir}/doc/luatex/lua-visual-debug/sample-plain.tex
%{_texmfdistdir}/doc/luatex/lua-visual-debug/sample.pdf
%{_texmfdistdir}/doc/luatex/lua-visual-debug/sample.tex
%{_texmfdistdir}/doc/luatex/lua-visual-debug/strut.png

%files -n texlive-lua-visual-debug
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/lua-visual-debug/lua-visual-debug.lua
%{_texmfdistdir}/tex/luatex/lua-visual-debug/lua-visual-debug.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lua-visual-debug-%{texlive_version}.%{texlive_noarch}.0.0.7svn49634-%{release}-zypper
%endif

%package -n texlive-luabibentry
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1asvn31783
Release:        0
Summary:        Repeat BibTeX entries in a LuaLaTeX document body
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luabibentry-doc >= %{texlive_version}
Provides:       tex(luabibentry.sty)
Requires:       tex(ifluatex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source49:       luabibentry.tar.xz
Source50:       luabibentry.doc.tar.xz

%description -n texlive-luabibentry
The package reimplements bibentry, for use in LuaLaTeX.

%package -n texlive-luabibentry-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1asvn31783
Release:        0
Summary:        Documentation for texlive-luabibentry
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luabibentry-doc
This package includes the documentation for texlive-luabibentry

%post -n texlive-luabibentry
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luabibentry 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luabibentry
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luabibentry-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luabibentry/News
%{_texmfdistdir}/doc/lualatex/luabibentry/README
%{_texmfdistdir}/doc/lualatex/luabibentry/luabibentry.pdf

%files -n texlive-luabibentry
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luabibentry/luabibentry.lua
%{_texmfdistdir}/tex/lualatex/luabibentry/luabibentry.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luabibentry-%{texlive_version}.%{texlive_noarch}.0.0.1asvn31783-%{release}-zypper
%endif

%package -n texlive-luabidi
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn54512
Release:        0
Summary:        Bidi functions for LuaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luabidi-doc >= %{texlive_version}
Provides:       tex(luabidi-arabmaths.def)
Provides:       tex(luabidi-autofootnoterule.def)
Provides:       tex(luabidi-footnotes.def)
Provides:       tex(luabidi-test-arabmaths.tex)
Provides:       tex(luabidi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(perpage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source51:       luabidi.tar.xz
Source52:       luabidi.doc.tar.xz

%description -n texlive-luabidi
The package attempts to emulate the XeTeX bidi package, in the
context of LuaTeX.

%package -n texlive-luabidi-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn54512
Release:        0
Summary:        Documentation for texlive-luabidi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luabidi-doc
This package includes the documentation for texlive-luabidi

%post -n texlive-luabidi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luabidi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luabidi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luabidi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luabidi/LICENCE.md
%{_texmfdistdir}/doc/lualatex/luabidi/README.md
%{_texmfdistdir}/doc/lualatex/luabidi/luabidi.pdf
%{_texmfdistdir}/doc/lualatex/luabidi/luabidi.tex

%files -n texlive-luabidi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luabidi/luabidi-arabmaths.def
%{_texmfdistdir}/tex/lualatex/luabidi/luabidi-autofootnoterule.def
%{_texmfdistdir}/tex/lualatex/luabidi/luabidi-footnotes.def
%{_texmfdistdir}/tex/lualatex/luabidi/luabidi-test-arabmaths.tex
%{_texmfdistdir}/tex/lualatex/luabidi/luabidi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luabidi-%{texlive_version}.%{texlive_noarch}.0.0.5svn54512-%{release}-zypper
%endif

%package -n texlive-luacode
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn25193
Release:        0
Summary:        Helper for executing lua code from within TeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luacode-doc >= %{texlive_version}
Provides:       tex(luacode.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source53:       luacode.tar.xz
Source54:       luacode.doc.tar.xz

%description -n texlive-luacode
Executing Lua code from within TeX with directlua can sometimes
be tricky: there is no easy way to use the percent character,
counting backslashes may be hard, and Lua comments don't work
the way you expect. The package provides the \luaexec command
and the luacode(*) environments to help with these problems.

%package -n texlive-luacode-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn25193
Release:        0
Summary:        Documentation for texlive-luacode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luacode-doc
This package includes the documentation for texlive-luacode

%post -n texlive-luacode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luacode 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luacode
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luacode-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luacode/News
%{_texmfdistdir}/doc/lualatex/luacode/README
%{_texmfdistdir}/doc/lualatex/luacode/luacode.pdf

%files -n texlive-luacode
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luacode/luacode.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luacode-%{texlive_version}.%{texlive_noarch}.1.2asvn25193-%{release}-zypper
%endif

%package -n texlive-luacolor
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn53933
Release:        0
Summary:        Color support based on LuaTeX's node attributes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luacolor-doc >= %{texlive_version}
Provides:       tex(luacolor.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source55:       luacolor.tar.xz
Source56:       luacolor.doc.tar.xz

%description -n texlive-luacolor
This package implements color support based on LuaTeX's node
attributes.

%package -n texlive-luacolor-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn53933
Release:        0
Summary:        Documentation for texlive-luacolor
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luacolor-doc
This package includes the documentation for texlive-luacolor

%post -n texlive-luacolor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luacolor 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luacolor
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luacolor-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/luacolor/README.md
%{_texmfdistdir}/doc/latex/luacolor/luacolor.pdf

%files -n texlive-luacolor
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/luacolor/luacolor.lua
%{_texmfdistdir}/tex/latex/luacolor/luacolor.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luacolor-%{texlive_version}.%{texlive_noarch}.1.15svn53933-%{release}-zypper
%endif

%package -n texlive-luahbtex
Version:        %{texlive_version}.%{texlive_noarch}.svn54498
Release:        0
Summary:        LuaTeX with HarfBuzz library for glyph shaping
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-cm >= %{texlive_version}
#!BuildIgnore: texlive-cm
Requires:       texlive-etex >= %{texlive_version}
#!BuildIgnore: texlive-etex
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires:       texlive-knuth-lib >= %{texlive_version}
#!BuildIgnore: texlive-knuth-lib
Requires(pre): texlive-luahbtex-bin >= %{texlive_version}
#!BuildIgnore: texlive-luahbtex-bin
Requires:       texlive-luatex >= %{texlive_version}
#!BuildIgnore: texlive-luatex
Requires:       texlive-plain >= %{texlive_version}
#!BuildIgnore: texlive-plain
Requires:       texlive-tex-ini-files >= %{texlive_version}
#!BuildIgnore: texlive-tex-ini-files
Requires:       texlive-unicode-data >= %{texlive_version}
#!BuildIgnore: texlive-unicode-data
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       man(luahbtex.1)
Requires:       man(luatex.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source57:       luahbtex.doc.tar.xz

%description -n texlive-luahbtex
The luahbtex package
%post -n texlive-luahbtex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.luahbtex
sed -ri 's/^\#\![[= =]]+luahbtex\b.*/luahbtex luahbtex language.def,language.dat.lua luatex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :

%postun -n texlive-luahbtex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    sed -ri 's/^(luahbtex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/luahbtex/luahbtex.*
    exit 0
fi

%triggerin -n texlive-luahbtex -- texlive-cm
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-cm
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-etex
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-etex
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-luatex
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-luatex
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-plain
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-plain
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.luahbtex

%triggerin -n texlive-luahbtex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.luahbtex

%triggerun -n texlive-luahbtex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.luahbtex

%posttrans -n texlive-luahbtex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luahbtex
%defattr(-,root,root,755)
%{_mandir}/man1/luahbtex.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luahbtex-%{texlive_version}.%{texlive_noarch}.svn54498-%{release}-zypper
%endif

%package -n texlive-luahyphenrules
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn42670
Release:        0
Summary:        Loading patterns in LuaLaTeX with language.dat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luahyphenrules-doc >= %{texlive_version}
Provides:       tex(luahyphenrules.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source58:       luahyphenrules.tar.xz
Source59:       luahyphenrules.doc.tar.xz

%description -n texlive-luahyphenrules
Preloading hyphenation patterns (or 'hyphen rules.) into any
format based upon LuaTeX is not required in LuaTeX and recent
releases of babel don't do it anyway. This package is addressed
to those who just want to select the languages and load their
patterns by means of `language.dat` without loading `babel`.

%package -n texlive-luahyphenrules-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn42670
Release:        0
Summary:        Documentation for texlive-luahyphenrules
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luahyphenrules-doc
This package includes the documentation for texlive-luahyphenrules

%post -n texlive-luahyphenrules
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luahyphenrules 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luahyphenrules
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luahyphenrules-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luahyphenrules/README.md
%{_texmfdistdir}/doc/lualatex/luahyphenrules/luahyphenrules.pdf
%{_texmfdistdir}/doc/lualatex/luahyphenrules/luahyphenrules.tex

%files -n texlive-luahyphenrules
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luahyphenrules/luahyphenrules.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luahyphenrules-%{texlive_version}.%{texlive_noarch}.1.0svn42670-%{release}-zypper
%endif

%package -n texlive-luaimageembed
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn50788
Release:        0
Summary:        Embed images as base64-encoded strings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luaimageembed-doc >= %{texlive_version}
Provides:       tex(luaimageembed.sty)
Requires:       tex(luacode.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source60:       luaimageembed.tar.xz
Source61:       luaimageembed.doc.tar.xz

%description -n texlive-luaimageembed
This package allows to embed images directly as base64-encoded
strings into an LuaLaTeX document. This can be useful, e. g. to
package a document with images into a single TeX file, or with
automatically generated graphics.

%package -n texlive-luaimageembed-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn50788
Release:        0
Summary:        Documentation for texlive-luaimageembed
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luaimageembed-doc
This package includes the documentation for texlive-luaimageembed

%post -n texlive-luaimageembed
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luaimageembed 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luaimageembed
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luaimageembed-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luaimageembed/LICENSE
%{_texmfdistdir}/doc/lualatex/luaimageembed/README.md

%files -n texlive-luaimageembed
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luaimageembed/luaimageembed.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luaimageembed-%{texlive_version}.%{texlive_noarch}.0.0.1svn50788-%{release}-zypper
%endif

%package -n texlive-luaindex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1bsvn25882
Release:        0
Summary:        Create index using LuaLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luaindex-doc >= %{texlive_version}
Provides:       tex(luaindex.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase-compat.sty)
Requires:       tex(luatexbase-modutils.sty)
Requires:       tex(scrbase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source62:       luaindex.tar.xz
Source63:       luaindex.doc.tar.xz

%description -n texlive-luaindex
Luaindex provides (yet another) index processor, written in
Lua.

%package -n texlive-luaindex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1bsvn25882
Release:        0
Summary:        Documentation for texlive-luaindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luaindex-doc
This package includes the documentation for texlive-luaindex

%post -n texlive-luaindex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luaindex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luaindex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luaindex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luaindex/README
%{_texmfdistdir}/doc/lualatex/luaindex/luaindex-example.ldx
%{_texmfdistdir}/doc/lualatex/luaindex/luaindex-example.ltx
%{_texmfdistdir}/doc/lualatex/luaindex/luaindex-example.pdf
%{_texmfdistdir}/doc/lualatex/luaindex/luaindex.ltx
%{_texmfdistdir}/doc/lualatex/luaindex/luaindex.pdf

%files -n texlive-luaindex
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/luaindex/luaindex.lua
%{_texmfdistdir}/tex/lualatex/luaindex/luaindex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luaindex-%{texlive_version}.%{texlive_noarch}.0.0.1bsvn25882-%{release}-zypper
%endif

%package -n texlive-luainputenc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.973svn20491
Release:        0
Summary:        Replacing inputenc for use in LuaTeX
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luainputenc-doc >= %{texlive_version}
Provides:       tex(luainputenc.sty)
Provides:       tex(lutf8.def)
Provides:       tex(lutf8x.def)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(luatexbase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source64:       luainputenc.tar.xz
Source65:       luainputenc.doc.tar.xz

%description -n texlive-luainputenc
LuaTeX operates by default in UTF-8 input; thus LaTeX documents
that need 8-bit character-sets need special treatment. (In
fact, LaTeX documents using UTF-8 with "traditional" --
256-glyph -- fonts also need support from this package.) The
package, therefore, replaces the LaTeX standard inputenc for
use under LuaTeX. With a current LuaTeX,the package has the
same behaviour with LuaTeX as inputenc has under pdfTeX.

%package -n texlive-luainputenc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.973svn20491
Release:        0
Summary:        Documentation for texlive-luainputenc
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luainputenc-doc
This package includes the documentation for texlive-luainputenc

%post -n texlive-luainputenc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luainputenc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luainputenc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luainputenc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luainputenc/NEWS
%{_texmfdistdir}/doc/lualatex/luainputenc/README
%{_texmfdistdir}/doc/lualatex/luainputenc/inputenc.sty.diff
%{_texmfdistdir}/doc/lualatex/luainputenc/luainputenc.pdf
%{_texmfdistdir}/doc/lualatex/luainputenc/test.tex

%files -n texlive-luainputenc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luainputenc/luainputenc.lua
%{_texmfdistdir}/tex/lualatex/luainputenc/luainputenc.sty
%{_texmfdistdir}/tex/lualatex/luainputenc/lutf8.def
%{_texmfdistdir}/tex/lualatex/luainputenc/lutf8x.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luainputenc-%{texlive_version}.%{texlive_noarch}.0.0.973svn20491-%{release}-zypper
%endif

%package -n texlive-luaintro
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn35490
Release:        0
Summary:        Examples from the book "Einfuhrung in LuaTeX und LuaLaTeX"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source66:       luaintro.doc.tar.xz

%description -n texlive-luaintro
The bundle provides source of all the examples published in the
German book "Einfuhrung in LuaTeX und LuaLaTeX", published by
Lehmans Media and DANTE, Berlin.
%post -n texlive-luaintro
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luaintro 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luaintro
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luaintro
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luaintro/01-01-1.lua
%{_texmfdistdir}/doc/luatex/luaintro/01-02-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-10.ltx2
%{_texmfdistdir}/doc/luatex/luaintro/01-02-11.ltx2
%{_texmfdistdir}/doc/luatex/luaintro/01-02-12.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-13.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-02-14.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-02-15.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-02-16.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-02-17.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-02-18.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-02-19.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-20.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-21.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-22.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-6.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-02-7.sh
%{_texmfdistdir}/doc/luatex/luaintro/01-02-8.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-02-9.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-03-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-03-2.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-03-3.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-03-4.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-03-5.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-03-6.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/01-04-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-04-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-04-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-04-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/01-04-5.ctx1crop
%{_texmfdistdir}/doc/luatex/luaintro/02-01-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-01-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-01-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-01-4.sh
%{_texmfdistdir}/doc/luatex/luaintro/02-01-5.sh
%{_texmfdistdir}/doc/luatex/luaintro/02-02-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-02-10.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-02-11.lualtx2
%{_texmfdistdir}/doc/luatex/luaintro/02-02-12.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/02-02-13.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/02-02-14.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/02-02-15.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/02-02-16.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/02-02-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-02-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-02-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-02-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/02-02-6.sh
%{_texmfdistdir}/doc/luatex/luaintro/02-02-7.lualtx2
%{_texmfdistdir}/doc/luatex/luaintro/02-02-8.lualtx2
%{_texmfdistdir}/doc/luatex/luaintro/02-02-9.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-01-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-03-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-04-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/03-06-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/03-06-2.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/03-06-3.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/03-07-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-07-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-08-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-08-2.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/03-08-3.sh
%{_texmfdistdir}/doc/luatex/luaintro/03-10-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-10-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-10-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-11-1.sh
%{_texmfdistdir}/doc/luatex/luaintro/03-11-1.tex
%{_texmfdistdir}/doc/luatex/luaintro/03-11-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-11-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-11-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-11-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-11-6.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/03-11-7.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-01-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/04-01-2.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/04-01-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-10.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-11.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-12.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-13.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-14.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-15.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-16.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-17.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-5.lualtx2
%{_texmfdistdir}/doc/luatex/luaintro/04-04-6.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-7.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-8.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/04-04-9.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/05-01-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/05-01-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/05-02-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/06-02-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-03-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/06-04-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/06-05-1.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/06-05-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-06-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-07-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-07-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-07-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-07-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-07-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-09-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-10-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-1.sh
%{_texmfdistdir}/doc/luatex/luaintro/06-11-10.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-11.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-12.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-13.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-14.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-15.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-16.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-17.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-18.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-2.sh
%{_texmfdistdir}/doc/luatex/luaintro/06-11-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-6.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-11-7.sh
%{_texmfdistdir}/doc/luatex/luaintro/06-11-8.sh
%{_texmfdistdir}/doc/luatex/luaintro/06-11-9.sh
%{_texmfdistdir}/doc/luatex/luaintro/06-12-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-10.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-11.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-12.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-13.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-14.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-6.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-7.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-8.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-12-9.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/06-13-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/07-02-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/07-02-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/07-02-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/08-01-1.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-10.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-11.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-2.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-3.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-4.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-5.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-6.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-7.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-8.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-01-9.lua
%{_texmfdistdir}/doc/luatex/luaintro/08-02-1.lua
%{_texmfdistdir}/doc/luatex/luaintro/09-01-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-01-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-01-3.lualtx3
%{_texmfdistdir}/doc/luatex/luaintro/09-01-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-01-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-01-6.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-03-1.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-03-2.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-03-3.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-03-4.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-03-5.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/09-03-6.lualtx
%{_texmfdistdir}/doc/luatex/luaintro/CTdefault.tex
%{_texmfdistdir}/doc/luatex/luaintro/DEexa.sty
%{_texmfdistdir}/doc/luatex/luaintro/DEoptions.sty
%{_texmfdistdir}/doc/luatex/luaintro/Letter.ist
%{_texmfdistdir}/doc/luatex/luaintro/LetterC.ist
%{_texmfdistdir}/doc/luatex/luaintro/LoadFonts.tex
%{_texmfdistdir}/doc/luatex/luaintro/README
%{_texmfdistdir}/doc/luatex/luaintro/beispiel.cls
%{_texmfdistdir}/doc/luatex/luaintro/bspcalweekly.cls
%{_texmfdistdir}/doc/luatex/luaintro/bspdvdcoll.cls
%{_texmfdistdir}/doc/luatex/luaintro/bspfont.cls
%{_texmfdistdir}/doc/luatex/luaintro/bsppstricks.cls
%{_texmfdistdir}/doc/luatex/luaintro/exa-fontconfig.tex
%{_texmfdistdir}/doc/luatex/luaintro/exaarticle.cls
%{_texmfdistdir}/doc/luatex/luaintro/exaarticle2.cls
%{_texmfdistdir}/doc/luatex/luaintro/exaartplain.cls
%{_texmfdistdir}/doc/luatex/luaintro/exabeamer.cls
%{_texmfdistdir}/doc/luatex/luaintro/exabook.cls
%{_texmfdistdir}/doc/luatex/luaintro/exabook2.cls
%{_texmfdistdir}/doc/luatex/luaintro/exadante.cls
%{_texmfdistdir}/doc/luatex/luaintro/exafoils.cls
%{_texmfdistdir}/doc/luatex/luaintro/exafubeamer.cls
%{_texmfdistdir}/doc/luatex/luaintro/exafupd.cls
%{_texmfdistdir}/doc/luatex/luaintro/examargin.cls
%{_texmfdistdir}/doc/luatex/luaintro/examemoir.cls
%{_texmfdistdir}/doc/luatex/luaintro/examinimal-mathsymbols.cls
%{_texmfdistdir}/doc/luatex/luaintro/examinimal.cls
%{_texmfdistdir}/doc/luatex/luaintro/exapd.cls
%{_texmfdistdir}/doc/luatex/luaintro/exaprosper.cls
%{_texmfdistdir}/doc/luatex/luaintro/exareport.cls
%{_texmfdistdir}/doc/luatex/luaintro/exaseminar.cls
%{_texmfdistdir}/doc/luatex/luaintro/exaslidenotes.cls
%{_texmfdistdir}/doc/luatex/luaintro/exasymbol.cls
%{_texmfdistdir}/doc/luatex/luaintro/exaxetex.cls
%{_texmfdistdir}/doc/luatex/luaintro/screxa.cls
%{_texmfdistdir}/doc/luatex/luaintro/screxabook.cls
%{_texmfdistdir}/doc/luatex/luaintro/screxareport.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luaintro-%{texlive_version}.%{texlive_noarch}.0.0.03svn35490-%{release}-zypper
%endif

%package -n texlive-luajittex
Version:        %{texlive_version}.%{texlive_noarch}.svn54498
Release:        0
Summary:        LuaTeX with just-in-time (jit) compiler, with and without HarfBuzz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-cm >= %{texlive_version}
#!BuildIgnore: texlive-cm
Requires:       texlive-etex >= %{texlive_version}
#!BuildIgnore: texlive-etex
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires:       texlive-knuth-lib >= %{texlive_version}
#!BuildIgnore: texlive-knuth-lib
Requires(pre): texlive-luajittex-bin >= %{texlive_version}
#!BuildIgnore: texlive-luajittex-bin
Requires:       texlive-luatex >= %{texlive_version}
#!BuildIgnore: texlive-luatex
Requires:       texlive-plain >= %{texlive_version}
#!BuildIgnore: texlive-plain
Requires:       texlive-tex-ini-files >= %{texlive_version}
#!BuildIgnore: texlive-tex-ini-files
Requires:       texlive-unicode-data >= %{texlive_version}
#!BuildIgnore: texlive-unicode-data
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       man(luajithbtex.1)
Provides:       man(luajittex.1)
Requires:       man(luatex.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source67:       luajittex.doc.tar.xz

%description -n texlive-luajittex
The luajittex package
%post -n texlive-luajittex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.luajithbtex
sed -ri 's/^\#\![[= =]]+luajithbtex\b.*/luajithbtex luajithbtex language.def,language.dat.lua luatex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
> /var/run/texlive/run-fmtutil.luajittex
sed -ri 's/^\#\![[= =]]+luajittex\b.*/luajittex luajittex language.def,language.dat.lua luatex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :

%postun -n texlive-luajittex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    sed -ri 's/^(luajithbtex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/luajithbtex/luajithbtex.*
    sed -ri 's/^(luajittex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/luajittex/luajittex.*
    exit 0
fi

%triggerin -n texlive-luajittex -- texlive-cm
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-cm
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-etex
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-etex
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-luatex
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-luatex
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-plain
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-plain
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerin -n texlive-luajittex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%triggerun -n texlive-luajittex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.luajithbtex
> /var/run/texlive/run-fmtutil.luajittex

%posttrans -n texlive-luajittex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luajittex
%defattr(-,root,root,755)
%{_mandir}/man1/luajithbtex.1*
%{_mandir}/man1/luajittex.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luajittex-%{texlive_version}.%{texlive_noarch}.svn54498-%{release}-zypper
%endif

%package -n texlive-lualatex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn30473
Release:        0
Summary:        A guide to use of LaTeX with LuaTeX
License:        GFDL-1.2-only
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source68:       lualatex-doc.doc.tar.xz

%description -n texlive-lualatex-doc
The document is a map/guide to the world of LuaLaTeX. Coverage
supports both new users and package developers. Apart from the
introductory material, the document gathers information from
several sources, and offers links to others.
%post -n texlive-lualatex-doc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lualatex-doc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lualatex-doc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lualatex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/lualatex-doc/News
%{_texmfdistdir}/doc/lualatex/lualatex-doc/README
%{_texmfdistdir}/doc/lualatex/lualatex-doc/lualatex-doc.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lualatex-doc-%{texlive_version}.%{texlive_noarch}.svn30473-%{release}-zypper
%endif

%package -n texlive-lualatex-doc-de
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn30474
Release:        0
Summary:        Guide to LuaLaTeX (German translation)
License:        GFDL-1.2-only
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source69:       lualatex-doc-de.doc.tar.xz

%description -n texlive-lualatex-doc-de
The document is a German translation of the map/guide to the
world of LuaLaTeX. Coverage supports both new users and package
developers. Apart from the introductory material, the document
gathers information from several sources, and offers links to
others.
%post -n texlive-lualatex-doc-de
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lualatex-doc-de 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lualatex-doc-de
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lualatex-doc-de
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lualatex-doc-de/lualatex-doc-DE.pdf
%{_texmfdistdir}/doc/latex/lualatex-doc-de/lualatex-doc-DE.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lualatex-doc-de-%{texlive_version}.%{texlive_noarch}.1.0svn30474-%{release}-zypper
%endif

%package -n texlive-lualatex-math
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn52663
Release:        0
Summary:        Fixes for mathematics-related LuaLaTeX issues
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-etoolbox >= %{texlive_version}
#!BuildIgnore: texlive-etoolbox
Requires:       texlive-filehook >= %{texlive_version}
#!BuildIgnore: texlive-filehook
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lualatex-math-doc >= %{texlive_version}
Provides:       tex(lualatex-math.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(filehook.sty)
Requires:       tex(luatexbase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source70:       lualatex-math.tar.xz
Source71:       lualatex-math.doc.tar.xz

%description -n texlive-lualatex-math
The package patches a few commands of the LaTeX2e kernel and
the amsmath and mathtools packages to be more compatible with
the LuaTeX engine. It is only meaningful for LuaLaTeX documents
containing mathematical formulas, and does not exhibit any new
functionality. The fixes are mostly moved from the unicode-math
package to this package since they are not directly related to
Unicode mathematics typesetting.

%package -n texlive-lualatex-math-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn52663
Release:        0
Summary:        Documentation for texlive-lualatex-math
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-lualatex-math-doc:en)

%description -n texlive-lualatex-math-doc
This package includes the documentation for texlive-lualatex-math

%post -n texlive-lualatex-math
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lualatex-math 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lualatex-math
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lualatex-math-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/lualatex-math/MANIFEST
%{_texmfdistdir}/doc/lualatex/lualatex-math/README
%{_texmfdistdir}/doc/lualatex/lualatex-math/lualatex-math.pdf

%files -n texlive-lualatex-math
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/lualatex-math/lualatex-math.lua
%{_texmfdistdir}/tex/lualatex/lualatex-math/lualatex-math.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lualatex-math-%{texlive_version}.%{texlive_noarch}.1.8svn52663-%{release}-zypper
%endif

%package -n texlive-lualatex-truncate
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48469
Release:        0
Summary:        A wrapper for using the truncate package with LuaLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lualatex-truncate-doc >= %{texlive_version}
Provides:       tex(lualatex-truncate.sty)
Requires:       tex(iftex.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(truncate.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source72:       lualatex-truncate.tar.xz
Source73:       lualatex-truncate.doc.tar.xz

%description -n texlive-lualatex-truncate
This package provides a wrapper for the truncate package, thus
fixing issues related to LuaTeX's hyphenation algorithm.

%package -n texlive-lualatex-truncate-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48469
Release:        0
Summary:        Documentation for texlive-lualatex-truncate
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lualatex-truncate-doc
This package includes the documentation for texlive-lualatex-truncate

%post -n texlive-lualatex-truncate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lualatex-truncate 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lualatex-truncate
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lualatex-truncate-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/lualatex-truncate/README.md
%{_texmfdistdir}/doc/lualatex/lualatex-truncate/lualatex-truncate-doc.pdf

%files -n texlive-lualatex-truncate
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/lualatex-truncate/lualatex-truncate.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lualatex-truncate-%{texlive_version}.%{texlive_noarch}.1.1svn48469-%{release}-zypper
%endif

%package -n texlive-lualibs
Version:        %{texlive_version}.%{texlive_noarch}.2.70svn53682
Release:        0
Summary:        Additional Lua functions for LuaTeX macro programmers
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lualibs-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source74:       lualibs.tar.xz
Source75:       lualibs.doc.tar.xz

%description -n texlive-lualibs
Lualibs is a collection of Lua modules useful for general
programming. The bundle is based on lua modules shipped with
ConTeXt, and made available in this bundle for use independent
of ConTeXt.

%package -n texlive-lualibs-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.70svn53682
Release:        0
Summary:        Documentation for texlive-lualibs
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lualibs-doc
This package includes the documentation for texlive-lualibs

%post -n texlive-lualibs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lualibs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lualibs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lualibs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/lualibs/LICENSE
%{_texmfdistdir}/doc/luatex/lualibs/NEWS
%{_texmfdistdir}/doc/luatex/lualibs/README.md
%{_texmfdistdir}/doc/luatex/lualibs/lualibs.pdf

%files -n texlive-lualibs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-basic-merged.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-basic.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-boolean.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-compat.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-dir.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-extended-merged.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-extended.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-file.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-function.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-gzip.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-io.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-lpeg.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-lua.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-math.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-md5.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-number.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-os.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-package.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-set.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-string.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-table.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-trac-inf.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-unicode.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-url.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-deb.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-dim.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-fil.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-jsn.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-lua.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-prs.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-sta.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-sto.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-str.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-tab.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs-util-tpl.lua
%{_texmfdistdir}/tex/luatex/lualibs/lualibs.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lualibs-%{texlive_version}.%{texlive_noarch}.2.70svn53682-%{release}-zypper
%endif

%package -n texlive-luamesh
Version:        %{texlive_version}.%{texlive_noarch}.0.0.51svn43814
Release:        0
Summary:        Computes and draws 2D Delaunay triangulation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luamesh-doc >= %{texlive_version}
Provides:       tex(luamesh.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source76:       luamesh.tar.xz
Source77:       luamesh.doc.tar.xz

%description -n texlive-luamesh
The package allows to compute and draw 2D Delaunay
triangulation. The algorithm is written with lua, and depending
upon the choice of the engine, the drawing is done by MetaPost
(with luamplib) or by TikZ. The Delaunay triangulation
algorithm is the Bowyer and Watson algorithm. Several macros
are provided to draw the global mesh, the set of points, or a
particular step of the algorithm.

%package -n texlive-luamesh-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.51svn43814
Release:        0
Summary:        Documentation for texlive-luamesh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luamesh-doc
This package includes the documentation for texlive-luamesh

%post -n texlive-luamesh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luamesh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luamesh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luamesh-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luamesh/README
%{_texmfdistdir}/doc/lualatex/luamesh/animation-crop.pdf
%{_texmfdistdir}/doc/lualatex/luamesh/biblio.bib
%{_texmfdistdir}/doc/lualatex/luamesh/dum.tex
%{_texmfdistdir}/doc/lualatex/luamesh/fond.mp
%{_texmfdistdir}/doc/lualatex/luamesh/fond.pdf
%{_texmfdistdir}/doc/lualatex/luamesh/lltxdoc.cls
%{_texmfdistdir}/doc/lualatex/luamesh/luamesh-doc.listing
%{_texmfdistdir}/doc/lualatex/luamesh/luamesh-doc.pdf
%{_texmfdistdir}/doc/lualatex/luamesh/luamesh-doc.tex
%{_texmfdistdir}/doc/lualatex/luamesh/luamesh-title.pdf
%{_texmfdistdir}/doc/lualatex/luamesh/maillage.geo
%{_texmfdistdir}/doc/lualatex/luamesh/maillage.msh
%{_texmfdistdir}/doc/lualatex/luamesh/mesh.txt
%{_texmfdistdir}/doc/lualatex/luamesh/meshgarde.txt

%files -n texlive-luamesh
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/luamesh/luamesh-polygon.lua
%{_texmfdistdir}/scripts/luamesh/luamesh-tex.lua
%{_texmfdistdir}/scripts/luamesh/luamesh.lua
%{_texmfdistdir}/tex/lualatex/luamesh/luamesh.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luamesh-%{texlive_version}.%{texlive_noarch}.0.0.51svn43814-%{release}-zypper
%endif

%package -n texlive-luamplib
Version:        %{texlive_version}.%{texlive_noarch}.2.20.5svn53904
Release:        0
Summary:        Use LuaTeX's built-in MetaPost interpreter
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luamplib-doc >= %{texlive_version}
Provides:       tex(luamplib.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source78:       luamplib.tar.xz
Source79:       luamplib.doc.tar.xz

%description -n texlive-luamplib
The package enables the user to specify MetaPost diagrams
(which may include colour specifications from the color or
xcolor packages) into a document, using LuaTeX's built-in
MetaPost library. The facility is only available in PDF mode.

%package -n texlive-luamplib-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.20.5svn53904
Release:        0
Summary:        Documentation for texlive-luamplib
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luamplib-doc
This package includes the documentation for texlive-luamplib

%post -n texlive-luamplib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luamplib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luamplib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luamplib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luamplib/NEWS
%{_texmfdistdir}/doc/luatex/luamplib/README
%{_texmfdistdir}/doc/luatex/luamplib/luamplib.pdf
%{_texmfdistdir}/doc/luatex/luamplib/test-luamplib-latex.tex
%{_texmfdistdir}/doc/luatex/luamplib/test-luamplib-plain.tex

%files -n texlive-luamplib
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/luamplib/luamplib.lua
%{_texmfdistdir}/tex/luatex/luamplib/luamplib.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luamplib-%{texlive_version}.%{texlive_noarch}.2.20.5svn53904-%{release}-zypper
%endif

%package -n texlive-luaotfload
Version:        %{texlive_version}.%{texlive_noarch}.3.12svn53652
Release:        0
Summary:        OpenType 'loader' for Plain TeX and LaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-lm >= %{texlive_version}
#!BuildIgnore: texlive-lm
Requires:       texlive-lualibs >= %{texlive_version}
#!BuildIgnore: texlive-lualibs
Requires(pre): texlive-luaotfload-bin >= %{texlive_version}
#!BuildIgnore: texlive-luaotfload-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luaotfload-doc >= %{texlive_version}
Provides:       tex(luaotfload-blacklist.cnf)
Provides:       tex(luaotfload.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source80:       luaotfload.tar.xz
Source81:       luaotfload.doc.tar.xz
Source82:       luaotfload_varfonts.dif

%description -n texlive-luaotfload
The package adopts the TrueType/OpenType Font loader code
provided in ConTeXt, and adapts it to use in Plain TeX and
LaTeX. It works under LuaLaTeX only.

%package -n texlive-luaotfload-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.12svn53652
Release:        0
Summary:        Documentation for texlive-luaotfload
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(luaotfload-tool.1)

%description -n texlive-luaotfload-doc
This package includes the documentation for texlive-luaotfload

%post -n texlive-luaotfload
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luaotfload 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luaotfload
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luaotfload-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luaotfload/COPYING
%{_texmfdistdir}/doc/luatex/luaotfload/NEWS
%{_texmfdistdir}/doc/luatex/luaotfload/README.md
%{_texmfdistdir}/doc/luatex/luaotfload/filegraph.pdf
%{_texmfdistdir}/doc/luatex/luaotfload/filegraph.tex
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload-conf.pdf
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload-latex.pdf
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload-latex.tex
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload-main.tex
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload-tool.pdf
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload-tool.rst
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload.conf.example
%{_texmfdistdir}/doc/luatex/luaotfload/luaotfload.conf.rst
%{_texmfdistdir}/doc/luatex/luaotfload/scripts-demo.pdf
%{_texmfdistdir}/doc/luatex/luaotfload/scripts-demo.tex
%{_texmfdistdir}/doc/luatex/luaotfload/shaper-demo-graphite.pdf
%{_texmfdistdir}/doc/luatex/luaotfload/shaper-demo-graphite.tex
%{_texmfdistdir}/doc/luatex/luaotfload/shaper-demo.pdf
%{_texmfdistdir}/doc/luatex/luaotfload/shaper-demo.tex
%{_mandir}/man1/luaotfload-tool.1*
%{_mandir}/man5/luaotfload.conf.5*

%files -n texlive-luaotfload
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/luaotfload/luaotfload-tool.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-2020-01-26.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-basics-chr.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-basics-gen.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-basics-nod.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-data-con.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-afk.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-cff.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-cid.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-con.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-def.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-dsp.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-imp-effects.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-imp-italics.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-imp-ligatures.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-imp-tex.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-ini.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-lua.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-map.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-ocl.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-one.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-onr.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-osd.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-ota.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-otc.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-oti.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-otj.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-otl.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-oto.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-otr.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-ots.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-ott.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-oup.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-ttf.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-font-vfc.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-def.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-enc.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-ext.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-gbn.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-lig.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-mis.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-syn.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-fonts-tfm.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-boolean.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-file.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-function.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-io.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-lpeg.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-lua.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-math.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-string.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-table.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-l-unicode.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-reference.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-util-fil.lua
%{_texmfdistdir}/tex/luatex/luaotfload/fontloader-util-str.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-auxiliary.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-blacklist.cnf
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-characters.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-colors.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-configuration.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-database.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-diagnostics.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-embolden.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-fallback.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-features.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-filelist.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-glyphlist.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-harf-define.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-harf-plug.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-init.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-letterspace.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-loaders.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-log.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-main.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-multiscript.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-notdef.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-parsers.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-resolvers.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-scripts.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-status.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-tounicode.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload-unicode.lua
%{_texmfdistdir}/tex/luatex/luaotfload/luaotfload.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luaotfload-%{texlive_version}.%{texlive_noarch}.3.12svn53652-%{release}-zypper
%endif

%package -n texlive-luapackageloader
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn54779
Release:        0
Summary:        Allow LuaTeX to load external Lua packages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luapackageloader-doc >= %{texlive_version}
Provides:       tex(luapackageloader.sty)
Requires:       tex(ifluatex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source83:       luapackageloader.tar.xz
Source84:       luapackageloader.doc.tar.xz

%description -n texlive-luapackageloader
This package allows LuaTeX to load packages from the default
package.path and package.cpath locations. This could be useful
to load external Lua modules, including modules installed via
LuaRocks. This package requires ifluatex.

%package -n texlive-luapackageloader-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn54779
Release:        0
Summary:        Documentation for texlive-luapackageloader
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luapackageloader-doc
This package includes the documentation for texlive-luapackageloader

%post -n texlive-luapackageloader
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luapackageloader 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luapackageloader
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luapackageloader-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luapackageloader/README.md
%{_texmfdistdir}/doc/luatex/luapackageloader/luapackageloader.pdf
%{_texmfdistdir}/doc/luatex/luapackageloader/luapackageloader.tex

%files -n texlive-luapackageloader
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/luapackageloader/luapackageloader.lua
%{_texmfdistdir}/tex/luatex/luapackageloader/luapackageloader.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luapackageloader-%{texlive_version}.%{texlive_noarch}.0.0.2svn54779-%{release}-zypper
%endif

%package -n texlive-luarandom
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn49419
Release:        0
Summary:        Create lists of random numbers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luarandom-doc >= %{texlive_version}
Provides:       tex(luarandom.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luacode.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source85:       luarandom.tar.xz
Source86:       luarandom.doc.tar.xz

%description -n texlive-luarandom
This package can create lists of random numbers for any given
interval [a;b]. It is possible to get lists with or without
multiple numbers. The random generator will be initialized by
the system time. The package can only be used with LuaLaTeX!

%package -n texlive-luarandom-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn49419
Release:        0
Summary:        Documentation for texlive-luarandom
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luarandom-doc
This package includes the documentation for texlive-luarandom

%post -n texlive-luarandom
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luarandom 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luarandom
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luarandom-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luarandom/Changes
%{_texmfdistdir}/doc/lualatex/luarandom/README
%{_texmfdistdir}/doc/lualatex/luarandom/luarandom-doc.pdf
%{_texmfdistdir}/doc/lualatex/luarandom/luarandom-doc.tex

%files -n texlive-luarandom
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luarandom/luarandom.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luarandom-%{texlive_version}.%{texlive_noarch}.0.0.01svn49419-%{release}-zypper
%endif

%package -n texlive-luasseq
Version:        %{texlive_version}.%{texlive_noarch}.svn37877
Release:        0
Summary:        Drawing spectral sequences in LuaLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luasseq-doc >= %{texlive_version}
Provides:       tex(luasseq.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pifont.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source87:       luasseq.tar.xz
Source88:       luasseq.doc.tar.xz

%description -n texlive-luasseq
The package is an update of the author's sseq package, for use
with LuaLaTeX. This version uses less memory, and operates
faster than the original; it also offers several enhancements.

%package -n texlive-luasseq-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn37877
Release:        0
Summary:        Documentation for texlive-luasseq
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luasseq-doc
This package includes the documentation for texlive-luasseq

%post -n texlive-luasseq
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luasseq 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luasseq
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luasseq-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luasseq/README
%{_texmfdistdir}/doc/lualatex/luasseq/luasseq.pdf

%files -n texlive-luasseq
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/luasseq/luasseq.lua
%{_texmfdistdir}/tex/lualatex/luasseq/luasseq.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luasseq-%{texlive_version}.%{texlive_noarch}.svn37877-%{release}-zypper
%endif

%package -n texlive-luatex
Version:        %{texlive_version}.%{texlive_noarch}.svn54610
Release:        0
Summary:        The LuaTeX engine
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-cm >= %{texlive_version}
Requires:       tex(load-unicode-data.tex)
Requires:       tex(luatexconfig.tex)
#!BuildIgnore: texlive-cm
Requires:       texlive-etex >= %{texlive_version}
#!BuildIgnore: texlive-etex
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires:       texlive-knuth-lib >= %{texlive_version}
#!BuildIgnore: texlive-knuth-lib
Requires(pre): texlive-luatex-bin >= %{texlive_version}
#!BuildIgnore: texlive-luatex-bin
Requires:       texlive-plain >= %{texlive_version}
#!BuildIgnore: texlive-plain
Requires:       texlive-tex-ini-files >= %{texlive_version}
#!BuildIgnore: texlive-tex-ini-files
Requires:       texlive-unicode-data >= %{texlive_version}
#!BuildIgnore: texlive-unicode-data
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(language.dat)
Requires(post): tex(language.def)
Requires(post): tex(language.dat.lua)
#!BuildIgnore:  tex(language.dat)
#!BuildIgnore:  tex(language.def)
#!BuildIgnore:  tex(language.dat.lua)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(language.dat)
Requires(postun): tex(language.def)
Requires(postun): tex(language.dat.lua)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luatex-doc >= %{texlive_version}
Requires(posttrans): texlive-cm >= %{texlive_version}
Requires(posttrans): texlive-etex >= %{texlive_version}
Requires(posttrans): texlive-hyph-utf8 >= %{texlive_version}
Requires(posttrans): texlive-hyphen-base >= %{texlive_version}
Requires(posttrans): texlive-manfnt >= %{texlive_version}
Requires(posttrans): tex(null.tex)
Provides:       tex(luatex-unicode-letters.tex)
Provides:       tex(luatexiniconfig.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source89:       luatex.tar.xz
Source90:       luatex.doc.tar.xz
Source91:       luatex_cnf.dif

%description -n texlive-luatex
LuaTeX is an extended version of pdfTeX using Lua as an
embedded scripting language. The LuaTeX project's main
objective is to provide an open and configurable variant of TeX
while at the same time offering downward compatibility. LuaTeX
uses Unicode (as UTF-8) as its default input encoding, and is
able to use modern (OpenType) fonts (for both text and
mathematics). It should be noted that LuaTeX is still under
development; its specification has been declared stable, but
absolute stability may not in practice be assumed. Source code
is available from ctan:/systems/texlive/Source/.

%package -n texlive-luatex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54610
Release:        0
Summary:        Documentation for texlive-luatex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(dviluatex.1)
Provides:       man(luatex.1)
Provides:       man(texlua.1)
Provides:       man(texluac.1)

%description -n texlive-luatex-doc
This package includes the documentation for texlive-luatex

%post -n texlive-luatex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.dviluatex
sed -ri 's/^\#\![[= =]]+dviluatex\b.*/dviluatex luatex language.def,language.dat.lua dviluatex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
> /var/run/texlive/run-fmtutil.luatex
sed -ri 's/^\#\![[= =]]+luatex\b.*/luatex luatex language.def,language.dat.lua luatex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :

%postun -n texlive-luatex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    sed -ri 's/^(dviluatex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/luatex/dviluatex.*
    sed -ri 's/^(luatex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/luatex/luatex.*
    exit 0
fi

%triggerin -n texlive-luatex -- texlive-cm
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-cm
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerin -n texlive-luatex -- texlive-etex
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-etex
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerin -n texlive-luatex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerin -n texlive-luatex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerin -n texlive-luatex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerin -n texlive-luatex -- texlive-plain
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-plain
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerin -n texlive-luatex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerin -n texlive-luatex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%triggerun -n texlive-luatex -- texlive-unicode-data
> /var/run/texlive/run-fmtutil.dviluatex
> /var/run/texlive/run-fmtutil.luatex

%posttrans -n texlive-luatex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luatex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/base/graphics/luaharfbuzz.pdf
%{_texmfdistdir}/doc/luatex/base/luatex-backend.tex
%{_texmfdistdir}/doc/luatex/base/luatex-callbacks.tex
%{_texmfdistdir}/doc/luatex/base/luatex-contents.tex
%{_texmfdistdir}/doc/luatex/base/luatex-enhancements.tex
%{_texmfdistdir}/doc/luatex/base/luatex-export-titlepage.tex
%{_texmfdistdir}/doc/luatex/base/luatex-firstpage.tex
%{_texmfdistdir}/doc/luatex/base/luatex-fontloader.tex
%{_texmfdistdir}/doc/luatex/base/luatex-fonts.tex
%{_texmfdistdir}/doc/luatex/base/luatex-graphics.tex
%{_texmfdistdir}/doc/luatex/base/luatex-harfbuzz.tex
%{_texmfdistdir}/doc/luatex/base/luatex-introduction.tex
%{_texmfdistdir}/doc/luatex/base/luatex-languages.tex
%{_texmfdistdir}/doc/luatex/base/luatex-logos.tex
%{_texmfdistdir}/doc/luatex/base/luatex-lua.tex
%{_texmfdistdir}/doc/luatex/base/luatex-math.tex
%{_texmfdistdir}/doc/luatex/base/luatex-modifications.tex
%{_texmfdistdir}/doc/luatex/base/luatex-nodes.tex
%{_texmfdistdir}/doc/luatex/base/luatex-preamble.tex
%{_texmfdistdir}/doc/luatex/base/luatex-registers.tex
%{_texmfdistdir}/doc/luatex/base/luatex-statistics.tex
%{_texmfdistdir}/doc/luatex/base/luatex-style.tex
%{_texmfdistdir}/doc/luatex/base/luatex-tex.tex
%{_texmfdistdir}/doc/luatex/base/luatex-titlepage.tex
%{_texmfdistdir}/doc/luatex/base/luatex.pdf
%{_texmfdistdir}/doc/luatex/base/luatex.tex
%{_mandir}/man1/dviluatex.1*
%{_mandir}/man1/luatex.1*
%{_mandir}/man1/texlua.1*
%{_mandir}/man1/texluac.1*

%files -n texlive-luatex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/config/luatex-unicode-letters.tex
%{_texmfdistdir}/tex/generic/config/luatexiniconfig.tex
%verify(link) %{_texmfdistdir}/web2c/texmfcnf.lua
%config(noreplace) %verify(not md5 mtime size) %{_texmfconfdir}/web2c/texmfcnf.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luatex-%{texlive_version}.%{texlive_noarch}.svn54610-%{release}-zypper
%endif

%package -n texlive-luatex85
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn41456
Release:        0
Summary:        PdfTeX aliases for LuaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luatex85-doc >= %{texlive_version}
Provides:       tex(luatex85.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source92:       luatex85.tar.xz
Source93:       luatex85.doc.tar.xz

%description -n texlive-luatex85
The package provides emulation of pdfTeX primitives for LuaTeX
v0.85+.

%package -n texlive-luatex85-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn41456
Release:        0
Summary:        Documentation for texlive-luatex85
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luatex85-doc
This package includes the documentation for texlive-luatex85

%post -n texlive-luatex85
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luatex85 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luatex85
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luatex85-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/luatex85/README.md
%{_texmfdistdir}/doc/generic/luatex85/luatex85.pdf

%files -n texlive-luatex85
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/luatex85/luatex85.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luatex85-%{texlive_version}.%{texlive_noarch}.1.4svn41456-%{release}-zypper
%endif

%package -n texlive-luatexbase
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn52663
Release:        0
Summary:        Basic resource management for LuaTeX code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-ctablestack >= %{texlive_version}
#!BuildIgnore: texlive-ctablestack
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luatexbase-doc >= %{texlive_version}
Provides:       tex(luatexbase-attr.sty)
Provides:       tex(luatexbase-cctb.sty)
Provides:       tex(luatexbase-compat.sty)
Provides:       tex(luatexbase-loader.sty)
Provides:       tex(luatexbase-mcb.sty)
Provides:       tex(luatexbase-modutils.sty)
Provides:       tex(luatexbase-regs.sty)
Provides:       tex(luatexbase.sty)
Requires:       tex(ctablestack.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source94:       luatexbase.tar.xz
Source95:       luatexbase.doc.tar.xz

%description -n texlive-luatexbase
The LaTeX kernel (LaTeX2e 2015/10/01 onward) builds in support
for LuaTeX functionality, also available as ltluatex.tex for
users of plain TeX and those with older LaTeX kernel
implementations. This support is based on ideas taken from the
original luatexbase package, but there are interface
differences. This 'stub' package provides a compatibility layer
to allow existing packages to upgrade smoothly to the new
support structure.

%package -n texlive-luatexbase-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn52663
Release:        0
Summary:        Documentation for texlive-luatexbase
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luatexbase-doc
This package includes the documentation for texlive-luatexbase

%post -n texlive-luatexbase
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luatexbase 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luatexbase
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luatexbase-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luatexbase/README.md
%{_texmfdistdir}/doc/luatex/luatexbase/luatexbase.pdf

%files -n texlive-luatexbase
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-attr.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-cctb.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-compat.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-loader.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-mcb.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-modutils.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase-regs.sty
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase.loader.lua
%{_texmfdistdir}/tex/luatex/luatexbase/luatexbase.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luatexbase-%{texlive_version}.%{texlive_noarch}.1.3svn52663-%{release}-zypper
%endif

%package -n texlive-luatexja
Version:        %{texlive_version}.%{texlive_noarch}.20200412.0svn54758
Release:        0
Summary:        Typeset Japanese with Lua(La)TeX
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-luatexbase >= %{texlive_version}
#!BuildIgnore: texlive-luatexbase
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luatexja-doc >= %{texlive_version}
Provides:       tex(lltjcore.sty)
Provides:       tex(lltjdefs.sty)
Provides:       tex(lltjext.sty)
Provides:       tex(lltjfont.sty)
Provides:       tex(lltjp-array.sty)
Provides:       tex(lltjp-fontspec.sty)
Provides:       tex(lltjp-footmisc.sty)
Provides:       tex(lltjp-geometry.sty)
Provides:       tex(lltjp-listings.sty)
Provides:       tex(lltjp-microtype.sty)
Provides:       tex(lltjp-preview.sty)
Provides:       tex(lltjp-siunitx.sty)
Provides:       tex(lltjp-stfloats.sty)
Provides:       tex(lltjp-tascmac.sty)
Provides:       tex(lltjp-unicode-math.sty)
Provides:       tex(lltjp-xunicode.sty)
Provides:       tex(ltj-base.sty)
Provides:       tex(ltj-latex.sty)
Provides:       tex(ltj-plain.sty)
Provides:       tex(ltjarticle.cls)
Provides:       tex(ltjbk10.clo)
Provides:       tex(ltjbk11.clo)
Provides:       tex(ltjbk12.clo)
Provides:       tex(ltjbook.cls)
Provides:       tex(ltjltxdoc.cls)
Provides:       tex(ltjreport.cls)
Provides:       tex(ltjsarticle.cls)
Provides:       tex(ltjsbook.cls)
Provides:       tex(ltjsize10.clo)
Provides:       tex(ltjsize11.clo)
Provides:       tex(ltjsize12.clo)
Provides:       tex(ltjskiyou.cls)
Provides:       tex(ltjspf.cls)
Provides:       tex(ltjsreport.cls)
Provides:       tex(ltjtarticle.cls)
Provides:       tex(ltjtbk10.clo)
Provides:       tex(ltjtbk11.clo)
Provides:       tex(ltjtbk12.clo)
Provides:       tex(ltjtbook.cls)
Provides:       tex(ltjtreport.cls)
Provides:       tex(ltjtsize10.clo)
Provides:       tex(ltjtsize11.clo)
Provides:       tex(ltjtsize12.clo)
Provides:       tex(luatexja-adjust.sty)
Provides:       tex(luatexja-ajmacros.sty)
Provides:       tex(luatexja-compat.sty)
Provides:       tex(luatexja-core.sty)
Provides:       tex(luatexja-fontspec-27c.sty)
Provides:       tex(luatexja-fontspec.sty)
Provides:       tex(luatexja-otf.sty)
Provides:       tex(luatexja-preset.sty)
Provides:       tex(luatexja-ruby.sty)
Provides:       tex(luatexja-zhfonts.sty)
Provides:       tex(luatexja.sty)
Requires:       tex(array.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(everyhook.sty)
Requires:       tex(everysel.sty)
Requires:       tex(expl3.sty)
Requires:       tex(filehook.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(jslogo.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(listings.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(ltxdoc.cls)
Requires:       tex(luaotfload.sty)
Requires:       tex(luatexbase-cctb.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(preview.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(stfloats.sty)
Requires:       tex(tascmac.sty)
Requires:       tex(tuenc.def)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source96:       luatexja.tar.xz
Source97:       luatexja.doc.tar.xz

%description -n texlive-luatexja
The package offers support for typesetting Japanese documents
with LuaTeX. Either of the Plain and LaTeX2e formats may be
used with the package.

%package -n texlive-luatexja-doc
Version:        %{texlive_version}.%{texlive_noarch}.20200412.0svn54758
Release:        0
Summary:        Documentation for texlive-luatexja
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-luatexja-doc:en;ja)

%description -n texlive-luatexja-doc
This package includes the documentation for texlive-luatexja

%post -n texlive-luatexja
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luatexja 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luatexja
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luatexja-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luatexja/COPYING
%{_texmfdistdir}/doc/luatex/luatexja/README
%{_texmfdistdir}/doc/luatex/luatexja/jfm-test.lua
%{_texmfdistdir}/doc/luatex/luatexja/jfm-ujisc33.lua
%{_texmfdistdir}/doc/luatex/luatexja/lltjp-geometry.pdf
%{_texmfdistdir}/doc/luatex/luatexja/lltjp-geometry.tex
%{_texmfdistdir}/doc/luatex/luatexja/ltjclasses.pdf
%{_texmfdistdir}/doc/luatex/luatexja/ltjltxdoc.pdf
%{_texmfdistdir}/doc/luatex/luatexja/ltjsclasses.pdf
%{_texmfdistdir}/doc/luatex/luatexja/luatexja-en.pdf
%{_texmfdistdir}/doc/luatex/luatexja/luatexja-ja.pdf
%{_texmfdistdir}/doc/luatex/luatexja/luatexja-ruby.pdf
%{_texmfdistdir}/doc/luatex/luatexja/luatexja-ruby.tex
%{_texmfdistdir}/doc/luatex/luatexja/luatexja.dtx
%{_texmfdistdir}/doc/luatex/luatexja/luatexja.ins

%files -n texlive-luatexja
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-adjust.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-ajmacros.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-fontspec-27c.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-fontspec.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-otf.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-preset.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-ruby.sty
%{_texmfdistdir}/tex/luatex/luatexja/addons/luatexja-zhfonts.sty
%{_texmfdistdir}/tex/luatex/luatexja/jfm-CCT.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-banjiao.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-jis.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-kaiming.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-min.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-mono.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-prop.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-propv.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-quanjiao.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-tmin.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-ujis.lua
%{_texmfdistdir}/tex/luatex/luatexja/jfm-ujisv.lua
%{_texmfdistdir}/tex/luatex/luatexja/lltjext.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-adjust.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-base.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-base.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-charrange.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-compat.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-debug.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-direction.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-inputbuf.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-ivd_aj1.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-jfmglue.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-jfont.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-jisx0208.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-kinsoku.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-latex.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-lineskip.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-lotf_aux.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-math.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-otf.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-plain.sty
%{_texmfdistdir}/tex/luatex/luatexja/ltj-pretreat.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-rmlgbm.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-ruby.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-setwidth.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-stack.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltj-unicode-ccfix.lua
%{_texmfdistdir}/tex/luatex/luatexja/ltjarticle.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjbk10.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjbk11.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjbk12.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjbook.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjltxdoc.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjreport.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjsarticle.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjsbook.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjsize10.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjsize11.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjsize12.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjskiyou.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjspf.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjsreport.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjtarticle.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjtbk10.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjtbk11.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjtbk12.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjtbook.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjtreport.cls
%{_texmfdistdir}/tex/luatex/luatexja/ltjtsize10.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjtsize11.clo
%{_texmfdistdir}/tex/luatex/luatexja/ltjtsize12.clo
%{_texmfdistdir}/tex/luatex/luatexja/luatexja-compat.sty
%{_texmfdistdir}/tex/luatex/luatexja/luatexja-core.sty
%{_texmfdistdir}/tex/luatex/luatexja/luatexja.lua
%{_texmfdistdir}/tex/luatex/luatexja/luatexja.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjcore.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjdefs.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjfont.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-array.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-fontspec.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-footmisc.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-geometry.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-listings.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-microtype.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-preview.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-siunitx.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-stfloats.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-tascmac.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-unicode-math.sty
%{_texmfdistdir}/tex/luatex/luatexja/patches/lltjp-xunicode.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luatexja-%{texlive_version}.%{texlive_noarch}.20200412.0svn54758-%{release}-zypper
%endif

%package -n texlive-luatexko
Version:        %{texlive_version}.%{texlive_noarch}.2.8svn54438
Release:        0
Summary:        Typeset Korean with Lua(La)TeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luatexko-doc >= %{texlive_version}
Provides:       tex(luatexko.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(everysel.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(kolabels-utf.sty)
Requires:       tex(konames-utf.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(luatexbase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source98:       luatexko.tar.xz
Source99:       luatexko.doc.tar.xz

%description -n texlive-luatexko
This is a Lua(La)TeX macro package that supports typesetting
Korean documents including Old Hangul texts. As LuaTeX has
opened up access to almost all the hidden routines of TeX
engine, users can obtain more beautiful outcome using this
package rather than other Hangul macros operating on other
engines. LuaTeX version 1.10+ and luaotfload version 2.96+ are
required for this package to run. This package also requires
the cjk-ko package for its full functionality.

%package -n texlive-luatexko-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.8svn54438
Release:        0
Summary:        Documentation for texlive-luatexko
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luatexko-doc
This package includes the documentation for texlive-luatexko

%post -n texlive-luatexko
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luatexko 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luatexko
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luatexko-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luatexko/ChangeLog
%{_texmfdistdir}/doc/luatex/luatexko/README
%{_texmfdistdir}/doc/luatex/luatexko/luatexko-doc.pdf
%{_texmfdistdir}/doc/luatex/luatexko/luatexko-doc.tex

%files -n texlive-luatexko
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/luatexko/luatexko-normalize.lua
%{_texmfdistdir}/tex/luatex/luatexko/luatexko-uhc2utf8.lua
%{_texmfdistdir}/tex/luatex/luatexko/luatexko.lua
%{_texmfdistdir}/tex/luatex/luatexko/luatexko.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luatexko-%{texlive_version}.%{texlive_noarch}.2.8svn54438-%{release}-zypper
%endif

%package -n texlive-luatextra
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn20747
Release:        0
Summary:        Additional macros for Plain TeX and LaTeX in LuaTeX
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luatextra-doc >= %{texlive_version}
Provides:       tex(luatextra.sty)
Requires:       tex(fixltx2e.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(metalogo.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source100:      luatextra.tar.xz
Source101:      luatextra.doc.tar.xz

%description -n texlive-luatextra
The package provides a coherent extended programming
environment for use with LuaTeX. It loads packages fontspec,
luatexbase and lualibs, and provides additional user-level
features and goodies. The package is under development, and its
specification may be expected to change.

%package -n texlive-luatextra-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn20747
Release:        0
Summary:        Documentation for texlive-luatextra
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luatextra-doc
This package includes the documentation for texlive-luatextra

%post -n texlive-luatextra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luatextra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luatextra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luatextra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luatextra/News
%{_texmfdistdir}/doc/lualatex/luatextra/README
%{_texmfdistdir}/doc/lualatex/luatextra/luatextra.pdf
%{_texmfdistdir}/doc/lualatex/luatextra/test.tex

%files -n texlive-luatextra
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luatextra/luatextra.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luatextra-%{texlive_version}.%{texlive_noarch}.1.0.1svn20747-%{release}-zypper
%endif

%package -n texlive-luatodonotes
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn53825
Release:        0
Summary:        Add editing annotations in a LuaLaTeX document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luatodonotes-doc >= %{texlive_version}
Provides:       tex(luatodonotes.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(luacode.sty)
Requires:       tex(soul.sty)
Requires:       tex(soulpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
Requires:       tex(zref-abspage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source102:      luatodonotes.tar.xz
Source103:      luatodonotes.doc.tar.xz

%description -n texlive-luatodonotes
The package allows the user to insert comments into a document
that suggest (for example) further editing that may be needed.
The comments are shown in the margins alongside the text;
different styles for the comments may be used; the styles are
selected using package options. The package is based on the
package todonotes, and depends heavily on Lua, so it can only
be used with LuaLaTeX.

%package -n texlive-luatodonotes-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn53825
Release:        0
Summary:        Documentation for texlive-luatodonotes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luatodonotes-doc
This package includes the documentation for texlive-luatodonotes

%post -n texlive-luatodonotes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luatodonotes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luatodonotes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luatodonotes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/luatodonotes/README.md
%{_texmfdistdir}/doc/lualatex/luatodonotes/luatodonotes.pdf

%files -n texlive-luatodonotes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/luatodonotes/inspect.lua
%{_texmfdistdir}/tex/lualatex/luatodonotes/luatodonotes.lua
%{_texmfdistdir}/tex/lualatex/luatodonotes/luatodonotes.sty
%{_texmfdistdir}/tex/lualatex/luatodonotes/path_line.lua
%{_texmfdistdir}/tex/lualatex/luatodonotes/path_point.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luatodonotes-%{texlive_version}.%{texlive_noarch}.0.0.5svn53825-%{release}-zypper
%endif

%package -n texlive-luavlna
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1fsvn52682
Release:        0
Summary:        Prevent line breaks after single letter words, units, or adademic titles
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luavlna-doc >= %{texlive_version}
Provides:       tex(luavlna.sty)
Provides:       tex(luavlna.tex)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source104:      luavlna.tar.xz
Source105:      luavlna.doc.tar.xz

%description -n texlive-luavlna
In some languages, like Czech or Polish, there should be no
single letter words at the end of a line, according to
typographical norms. This package handles such situations using
LuaTeX's callback mechanism. In doing this, the package can
detect languages used in the text and insert spaces only in
parts of the document where languages requiring this feature
are used. Another feature of this package is the inclusion of
non-breakable space after initials (like in personal names),
after or before academic degrees, and between numbers and
units. The package supports both plain LuaTeX and LuaLaTeX.
BTW: "vlna" is the Czech word for "wave" or "curl" and also
denotes the tilde which, in TeX, is used for "unbreakable
spaces".

%package -n texlive-luavlna-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1fsvn52682
Release:        0
Summary:        Documentation for texlive-luavlna
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luavlna-doc
This package includes the documentation for texlive-luavlna

%post -n texlive-luavlna
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luavlna 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luavlna
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luavlna-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luavlna/README.md
%{_texmfdistdir}/doc/luatex/luavlna/luavlna-doc.pdf
%{_texmfdistdir}/doc/luatex/luavlna/luavlna-doc.tex

%files -n texlive-luavlna
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/luavlna/luavlna-csplain-langs.lua
%{_texmfdistdir}/tex/luatex/luavlna/luavlna-langno.lua
%{_texmfdistdir}/tex/luatex/luavlna/luavlna-predegrees.lua
%{_texmfdistdir}/tex/luatex/luavlna/luavlna-presi.lua
%{_texmfdistdir}/tex/luatex/luavlna/luavlna-si.lua
%{_texmfdistdir}/tex/luatex/luavlna/luavlna-sufdegrees.lua
%{_texmfdistdir}/tex/luatex/luavlna/luavlna.4ht
%{_texmfdistdir}/tex/luatex/luavlna/luavlna.lua
%{_texmfdistdir}/tex/luatex/luavlna/luavlna.sty
%{_texmfdistdir}/tex/luatex/luavlna/luavlna.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luavlna-%{texlive_version}.%{texlive_noarch}.0.0.1fsvn52682-%{release}-zypper
%endif

%package -n texlive-luaxml
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1lsvn52137
Release:        0
Summary:        Lua library for reading and serialising XML files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-luaxml-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source106:      luaxml.tar.xz
Source107:      luaxml.doc.tar.xz

%description -n texlive-luaxml
LuaXML is pure lua library for reading and serializing of the
XML files. Current release is aimed mainly as support for the
odsfile package. The documentation was created by automatic
conversion of original documentation in the source code.

%package -n texlive-luaxml-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1lsvn52137
Release:        0
Summary:        Documentation for texlive-luaxml
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-luaxml-doc
This package includes the documentation for texlive-luaxml

%post -n texlive-luaxml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-luaxml 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-luaxml
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-luaxml-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/luaxml/README
%{_texmfdistdir}/doc/luatex/luaxml/luaxml.pdf
%{_texmfdistdir}/doc/luatex/luaxml/luaxml.tex

%files -n texlive-luaxml
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-cssquery.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-domobject.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-entities.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-mod-handler.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-mod-xml.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-namedentities.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-parse-query.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-pretty.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-stack.lua
%{_texmfdistdir}/tex/luatex/luaxml/luaxml-testxml.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-luaxml-%{texlive_version}.%{texlive_noarch}.0.0.1lsvn52137-%{release}-zypper
%endif

%package -n texlive-lwarp
Version:        %{texlive_version}.%{texlive_noarch}.0.0.83svn54586
Release:        0
Summary:        Converts LaTeX to HTML
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-lwarp-bin >= %{texlive_version}
#!BuildIgnore: texlive-lwarp-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lwarp-doc >= %{texlive_version}
Provides:       tex(lwarp-2in1.sty)
Provides:       tex(lwarp-2up.sty)
Provides:       tex(lwarp-CJK.sty)
Provides:       tex(lwarp-CJKutf8.sty)
Provides:       tex(lwarp-DotArrow.sty)
Provides:       tex(lwarp-SIunits.sty)
Provides:       tex(lwarp-a4.sty)
Provides:       tex(lwarp-a4wide.sty)
Provides:       tex(lwarp-a5comb.sty)
Provides:       tex(lwarp-abstract.sty)
Provides:       tex(lwarp-academicons.sty)
Provides:       tex(lwarp-accessibility.sty)
Provides:       tex(lwarp-accsupp.sty)
Provides:       tex(lwarp-acro.sty)
Provides:       tex(lwarp-acronym.sty)
Provides:       tex(lwarp-addlines.sty)
Provides:       tex(lwarp-adjmulticol.sty)
Provides:       tex(lwarp-afterpage.sty)
Provides:       tex(lwarp-algorithm2e.sty)
Provides:       tex(lwarp-algorithmicx.sty)
Provides:       tex(lwarp-alltt.sty)
Provides:       tex(lwarp-amsmath.sty)
Provides:       tex(lwarp-amsthm.sty)
Provides:       tex(lwarp-anonchap.sty)
Provides:       tex(lwarp-anysize.sty)
Provides:       tex(lwarp-appendix.sty)
Provides:       tex(lwarp-ar.sty)
Provides:       tex(lwarp-arabicfront.sty)
Provides:       tex(lwarp-array.sty)
Provides:       tex(lwarp-arydshln.sty)
Provides:       tex(lwarp-asymptote.sty)
Provides:       tex(lwarp-atbegshi.sty)
Provides:       tex(lwarp-attachfile.sty)
Provides:       tex(lwarp-attachfile2.sty)
Provides:       tex(lwarp-authblk.sty)
Provides:       tex(lwarp-autobreak.sty)
Provides:       tex(lwarp-autonum.sty)
Provides:       tex(lwarp-awesomebox.sty)
Provides:       tex(lwarp-axessibility.sty)
Provides:       tex(lwarp-axodraw2.sty)
Provides:       tex(lwarp-backnaur.sty)
Provides:       tex(lwarp-backref.sty)
Provides:       tex(lwarp-balance.sty)
Provides:       tex(lwarp-bbding.sty)
Provides:       tex(lwarp-biblatex.sty)
Provides:       tex(lwarp-bibunits.sty)
Provides:       tex(lwarp-bigdelim.sty)
Provides:       tex(lwarp-bigfoot.sty)
Provides:       tex(lwarp-bigstrut.sty)
Provides:       tex(lwarp-bitpattern.sty)
Provides:       tex(lwarp-blowup.sty)
Provides:       tex(lwarp-bm.sty)
Provides:       tex(lwarp-booklet.sty)
Provides:       tex(lwarp-bookmark.sty)
Provides:       tex(lwarp-booktabs.sty)
Provides:       tex(lwarp-bophook.sty)
Provides:       tex(lwarp-bounddvi.sty)
Provides:       tex(lwarp-boxedminipage2e.sty)
Provides:       tex(lwarp-braket.sty)
Provides:       tex(lwarp-breakurl.sty)
Provides:       tex(lwarp-breqn.sty)
Provides:       tex(lwarp-bsheaders.sty)
Provides:       tex(lwarp-bxpapersize.sty)
Provides:       tex(lwarp-bytefield.sty)
Provides:       tex(lwarp-cancel.sty)
Provides:       tex(lwarp-canoniclayout.sty)
Provides:       tex(lwarp-caption.sty)
Provides:       tex(lwarp-cases.sty)
Provides:       tex(lwarp-centernot.sty)
Provides:       tex(lwarp-changebar.sty)
Provides:       tex(lwarp-changelayout.sty)
Provides:       tex(lwarp-changepage.sty)
Provides:       tex(lwarp-changes.sty)
Provides:       tex(lwarp-chappg.sty)
Provides:       tex(lwarp-chapterbib.sty)
Provides:       tex(lwarp-chemfig.sty)
Provides:       tex(lwarp-chemformula.sty)
Provides:       tex(lwarp-chemgreek.sty)
Provides:       tex(lwarp-chemmacros.sty)
Provides:       tex(lwarp-chemnum.sty)
Provides:       tex(lwarp-chkfloat.sty)
Provides:       tex(lwarp-chngpage.sty)
Provides:       tex(lwarp-cite.sty)
Provides:       tex(lwarp-clrdblpg.sty)
Provides:       tex(lwarp-cmdtrack.sty)
Provides:       tex(lwarp-colonequals.sty)
Provides:       tex(lwarp-color.sty)
Provides:       tex(lwarp-colortbl.sty)
Provides:       tex(lwarp-common-multimedia.sty)
Provides:       tex(lwarp-continue.sty)
Provides:       tex(lwarp-copyrightbox.sty)
Provides:       tex(lwarp-crop.sty)
Provides:       tex(lwarp-ctable.sty)
Provides:       tex(lwarp-cuted.sty)
Provides:       tex(lwarp-cutwin.sty)
Provides:       tex(lwarp-dblfloatfix.sty)
Provides:       tex(lwarp-dblfnote.sty)
Provides:       tex(lwarp-dcolumn.sty)
Provides:       tex(lwarp-decimal.sty)
Provides:       tex(lwarp-diagbox.sty)
Provides:       tex(lwarp-dingbat.sty)
Provides:       tex(lwarp-dotlessi.sty)
Provides:       tex(lwarp-dprogress.sty)
Provides:       tex(lwarp-draftcopy.sty)
Provides:       tex(lwarp-draftfigure.sty)
Provides:       tex(lwarp-draftwatermark.sty)
Provides:       tex(lwarp-easy-todo.sty)
Provides:       tex(lwarp-ebook.sty)
Provides:       tex(lwarp-econometrics.sty)
Provides:       tex(lwarp-ed.sty)
Provides:       tex(lwarp-ellipsis.sty)
Provides:       tex(lwarp-embrac.sty)
Provides:       tex(lwarp-emptypage.sty)
Provides:       tex(lwarp-endfloat.sty)
Provides:       tex(lwarp-endheads.sty)
Provides:       tex(lwarp-endnotes.sty)
Provides:       tex(lwarp-engtlc.sty)
Provides:       tex(lwarp-enumerate.sty)
Provides:       tex(lwarp-enumitem.sty)
Provides:       tex(lwarp-epigraph.sty)
Provides:       tex(lwarp-epsfig.sty)
Provides:       tex(lwarp-epstopdf-base.sty)
Provides:       tex(lwarp-epstopdf.sty)
Provides:       tex(lwarp-eqlist.sty)
Provides:       tex(lwarp-eqparbox.sty)
Provides:       tex(lwarp-errata.sty)
Provides:       tex(lwarp-eso-pic.sty)
Provides:       tex(lwarp-etoc.sty)
Provides:       tex(lwarp-eurosym.sty)
Provides:       tex(lwarp-everypage.sty)
Provides:       tex(lwarp-everyshi.sty)
Provides:       tex(lwarp-extarrows.sty)
Provides:       tex(lwarp-extramarks.sty)
Provides:       tex(lwarp-fancybox.sty)
Provides:       tex(lwarp-fancyhdr.sty)
Provides:       tex(lwarp-fancyref.sty)
Provides:       tex(lwarp-fancytabs.sty)
Provides:       tex(lwarp-fancyvrb.sty)
Provides:       tex(lwarp-fewerfloatpages.sty)
Provides:       tex(lwarp-figcaps.sty)
Provides:       tex(lwarp-figsize.sty)
Provides:       tex(lwarp-fitbox.sty)
Provides:       tex(lwarp-fix2col.sty)
Provides:       tex(lwarp-fixme.sty)
Provides:       tex(lwarp-fixmetodonotes.sty)
Provides:       tex(lwarp-flafter.sty)
Provides:       tex(lwarp-flippdf.sty)
Provides:       tex(lwarp-float.sty)
Provides:       tex(lwarp-floatflt.sty)
Provides:       tex(lwarp-floatpag.sty)
Provides:       tex(lwarp-floatrow.sty)
Provides:       tex(lwarp-fltrace.sty)
Provides:       tex(lwarp-flushend.sty)
Provides:       tex(lwarp-fnbreak.sty)
Provides:       tex(lwarp-fncychap.sty)
Provides:       tex(lwarp-fnlineno.sty)
Provides:       tex(lwarp-fnpos.sty)
Provides:       tex(lwarp-fontawesome.sty)
Provides:       tex(lwarp-fontawesome5.sty)
Provides:       tex(lwarp-fontaxes.sty)
Provides:       tex(lwarp-fontenc.sty)
Provides:       tex(lwarp-footmisc.sty)
Provides:       tex(lwarp-footnote.sty)
Provides:       tex(lwarp-footnotebackref.sty)
Provides:       tex(lwarp-footnotehyper.sty)
Provides:       tex(lwarp-footnoterange.sty)
Provides:       tex(lwarp-footnpag.sty)
Provides:       tex(lwarp-foreign.sty)
Provides:       tex(lwarp-forest.sty)
Provides:       tex(lwarp-fouridx.sty)
Provides:       tex(lwarp-framed.sty)
Provides:       tex(lwarp-ftcap.sty)
Provides:       tex(lwarp-ftnright.sty)
Provides:       tex(lwarp-fullminipage.sty)
Provides:       tex(lwarp-fullpage.sty)
Provides:       tex(lwarp-fullwidth.sty)
Provides:       tex(lwarp-fwlw.sty)
Provides:       tex(lwarp-gensymb.sty)
Provides:       tex(lwarp-gentombow.sty)
Provides:       tex(lwarp-geometry.sty)
Provides:       tex(lwarp-ghsystem.sty)
Provides:       tex(lwarp-gloss.sty)
Provides:       tex(lwarp-glossaries.sty)
Provides:       tex(lwarp-gmeometric.sty)
Provides:       tex(lwarp-graphics.sty)
Provides:       tex(lwarp-graphicx.sty)
Provides:       tex(lwarp-grffile.sty)
Provides:       tex(lwarp-grid-system.sty)
Provides:       tex(lwarp-grid.sty)
Provides:       tex(lwarp-gridset.sty)
Provides:       tex(lwarp-hang.sty)
Provides:       tex(lwarp-hanging.sty)
Provides:       tex(lwarp-hhline.sty)
Provides:       tex(lwarp-hypbmsec.sty)
Provides:       tex(lwarp-hypcap.sty)
Provides:       tex(lwarp-hypdestopt.sty)
Provides:       tex(lwarp-hypernat.sty)
Provides:       tex(lwarp-hyperref.sty)
Provides:       tex(lwarp-hyperxmp.sty)
Provides:       tex(lwarp-hyphenat.sty)
Provides:       tex(lwarp-idxlayout.sty)
Provides:       tex(lwarp-ifoddpage.sty)
Provides:       tex(lwarp-imakeidx.sty)
Provides:       tex(lwarp-index.sty)
Provides:       tex(lwarp-inputtrc.sty)
Provides:       tex(lwarp-intopdf.sty)
Provides:       tex(lwarp-karnaugh-map.sty)
Provides:       tex(lwarp-keyfloat.sty)
Provides:       tex(lwarp-layaureo.sty)
Provides:       tex(lwarp-layout.sty)
Provides:       tex(lwarp-layouts.sty)
Provides:       tex(lwarp-leading.sty)
Provides:       tex(lwarp-leftidx.sty)
Provides:       tex(lwarp-letterspace.sty)
Provides:       tex(lwarp-lettrine.sty)
Provides:       tex(lwarp-lineno.sty)
Provides:       tex(lwarp-lips.sty)
Provides:       tex(lwarp-listings.sty)
Provides:       tex(lwarp-listliketab.sty)
Provides:       tex(lwarp-lltjext.sty)
Provides:       tex(lwarp-longtable.sty)
Provides:       tex(lwarp-lscape.sty)
Provides:       tex(lwarp-ltablex.sty)
Provides:       tex(lwarp-ltcaption.sty)
Provides:       tex(lwarp-ltxgrid.sty)
Provides:       tex(lwarp-ltxtable.sty)
Provides:       tex(lwarp-lua-check-hyphen.sty)
Provides:       tex(lwarp-lua-visual-debug.sty)
Provides:       tex(lwarp-luacolor.sty)
Provides:       tex(lwarp-luamplib.sty)
Provides:       tex(lwarp-luatexko.sty)
Provides:       tex(lwarp-luatodonotes.sty)
Provides:       tex(lwarp-lyluatex.sty)
Provides:       tex(lwarp-magaz.sty)
Provides:       tex(lwarp-makeidx.sty)
Provides:       tex(lwarp-manyfoot.sty)
Provides:       tex(lwarp-marginal.sty)
Provides:       tex(lwarp-marginfit.sty)
Provides:       tex(lwarp-marginfix.sty)
Provides:       tex(lwarp-marginnote.sty)
Provides:       tex(lwarp-marvosym.sty)
Provides:       tex(lwarp-mathcomp.sty)
Provides:       tex(lwarp-mathdots.sty)
Provides:       tex(lwarp-mathfixs.sty)
Provides:       tex(lwarp-mathtools.sty)
Provides:       tex(lwarp-mcaption.sty)
Provides:       tex(lwarp-mdframed.sty)
Provides:       tex(lwarp-media9.sty)
Provides:       tex(lwarp-memhfixc.sty)
Provides:       tex(lwarp-metalogo.sty)
Provides:       tex(lwarp-metalogox.sty)
Provides:       tex(lwarp-mhchem.sty)
Provides:       tex(lwarp-microtype.sty)
Provides:       tex(lwarp-midfloat.sty)
Provides:       tex(lwarp-midpage.sty)
Provides:       tex(lwarp-minibox.sty)
Provides:       tex(lwarp-minitoc.sty)
Provides:       tex(lwarp-mismath.sty)
Provides:       tex(lwarp-morefloats.sty)
Provides:       tex(lwarp-moreverb.sty)
Provides:       tex(lwarp-movie15.sty)
Provides:       tex(lwarp-mparhack.sty)
Provides:       tex(lwarp-multicap.sty)
Provides:       tex(lwarp-multicol.sty)
Provides:       tex(lwarp-multicolrule.sty)
Provides:       tex(lwarp-multimedia.sty)
Provides:       tex(lwarp-multiobjective.sty)
Provides:       tex(lwarp-multirow.sty)
Provides:       tex(lwarp-multitoc.sty)
Provides:       tex(lwarp-musicography.sty)
Provides:       tex(lwarp-nameauth.sty)
Provides:       tex(lwarp-nameref.sty)
Provides:       tex(lwarp-natbib.sty)
Provides:       tex(lwarp-nccfancyhdr.sty)
Provides:       tex(lwarp-nccfoots.sty)
Provides:       tex(lwarp-nccmath.sty)
Provides:       tex(lwarp-needspace.sty)
Provides:       tex(lwarp-nextpage.sty)
Provides:       tex(lwarp-nfssext-cfr.sty)
Provides:       tex(lwarp-nicefrac.sty)
Provides:       tex(lwarp-niceframe.sty)
Provides:       tex(lwarp-noitcrul.sty)
Provides:       tex(lwarp-nolbreaks.sty)
Provides:       tex(lwarp-nomencl.sty)
Provides:       tex(lwarp-nonfloat.sty)
Provides:       tex(lwarp-nonumonpart.sty)
Provides:       tex(lwarp-nopageno.sty)
Provides:       tex(lwarp-notes.sty)
Provides:       tex(lwarp-notespages.sty)
Provides:       tex(lwarp-nowidow.sty)
Provides:       tex(lwarp-ntheorem.sty)
Provides:       tex(lwarp-octave.sty)
Provides:       tex(lwarp-overpic.sty)
Provides:       tex(lwarp-pagegrid.sty)
Provides:       tex(lwarp-pagenote.sty)
Provides:       tex(lwarp-pagesel.sty)
Provides:       tex(lwarp-paralist.sty)
Provides:       tex(lwarp-parallel.sty)
Provides:       tex(lwarp-parcolumns.sty)
Provides:       tex(lwarp-parnotes.sty)
Provides:       tex(lwarp-parskip.sty)
Provides:       tex(lwarp-patch-komascript.sty)
Provides:       tex(lwarp-patch-memoir.sty)
Provides:       tex(lwarp-pbox.sty)
Provides:       tex(lwarp-pdfcol.sty)
Provides:       tex(lwarp-pdfcolfoot.sty)
Provides:       tex(lwarp-pdfcolmk.sty)
Provides:       tex(lwarp-pdfcolparallel.sty)
Provides:       tex(lwarp-pdfcolparcolumns.sty)
Provides:       tex(lwarp-pdfcomment.sty)
Provides:       tex(lwarp-pdfcrypt.sty)
Provides:       tex(lwarp-pdflscape.sty)
Provides:       tex(lwarp-pdfmarginpar.sty)
Provides:       tex(lwarp-pdfpages.sty)
Provides:       tex(lwarp-pdfprivacy.sty)
Provides:       tex(lwarp-pdfrender.sty)
Provides:       tex(lwarp-pdfsync.sty)
Provides:       tex(lwarp-pdftricks.sty)
Provides:       tex(lwarp-pdfx.sty)
Provides:       tex(lwarp-perpage.sty)
Provides:       tex(lwarp-pfnote.sty)
Provides:       tex(lwarp-phfqit.sty)
Provides:       tex(lwarp-physics.sty)
Provides:       tex(lwarp-physunits.sty)
Provides:       tex(lwarp-pifont.sty)
Provides:       tex(lwarp-placeins.sty)
Provides:       tex(lwarp-plarydshln.sty)
Provides:       tex(lwarp-plext.sty)
Provides:       tex(lwarp-plextarydshln.sty)
Provides:       tex(lwarp-plextcolorbl.sty)
Provides:       tex(lwarp-prelim2e.sty)
Provides:       tex(lwarp-prettyref.sty)
Provides:       tex(lwarp-preview.sty)
Provides:       tex(lwarp-psfrag.sty)
Provides:       tex(lwarp-psfragx.sty)
Provides:       tex(lwarp-pst-eps.sty)
Provides:       tex(lwarp-pstool.sty)
Provides:       tex(lwarp-pstricks.sty)
Provides:       tex(lwarp-pxatbegshi.sty)
Provides:       tex(lwarp-pxeveryshi.sty)
Provides:       tex(lwarp-pxftnright.sty)
Provides:       tex(lwarp-pxjahyper.sty)
Provides:       tex(lwarp-quotchap.sty)
Provides:       tex(lwarp-quoting.sty)
Provides:       tex(lwarp-ragged2e.sty)
Provides:       tex(lwarp-realscripts.sty)
Provides:       tex(lwarp-refcheck.sty)
Provides:       tex(lwarp-register.sty)
Provides:       tex(lwarp-relsize.sty)
Provides:       tex(lwarp-repeatindex.sty)
Provides:       tex(lwarp-resizegather.sty)
Provides:       tex(lwarp-returntogrid.sty)
Provides:       tex(lwarp-rmathbr.sty)
Provides:       tex(lwarp-rmpage.sty)
Provides:       tex(lwarp-romanbar.sty)
Provides:       tex(lwarp-romanbarpagenumber.sty)
Provides:       tex(lwarp-rotating.sty)
Provides:       tex(lwarp-rotfloat.sty)
Provides:       tex(lwarp-rviewport.sty)
Provides:       tex(lwarp-savetrees.sty)
Provides:       tex(lwarp-scalefnt.sty)
Provides:       tex(lwarp-schemata.sty)
Provides:       tex(lwarp-scrextend.sty)
Provides:       tex(lwarp-scrhack.sty)
Provides:       tex(lwarp-scrlayer-notecolumn.sty)
Provides:       tex(lwarp-scrlayer-scrpage.sty)
Provides:       tex(lwarp-scrlayer.sty)
Provides:       tex(lwarp-scrpage2.sty)
Provides:       tex(lwarp-section.sty)
Provides:       tex(lwarp-sectionbreak.sty)
Provides:       tex(lwarp-sectsty.sty)
Provides:       tex(lwarp-semantic-markup.sty)
Provides:       tex(lwarp-setspace.sty)
Provides:       tex(lwarp-shadow.sty)
Provides:       tex(lwarp-shapepar.sty)
Provides:       tex(lwarp-showidx.sty)
Provides:       tex(lwarp-showkeys.sty)
Provides:       tex(lwarp-showtags.sty)
Provides:       tex(lwarp-sidecap.sty)
Provides:       tex(lwarp-sidenotes.sty)
Provides:       tex(lwarp-siunitx.sty)
Provides:       tex(lwarp-slantsc.sty)
Provides:       tex(lwarp-slashed.sty)
Provides:       tex(lwarp-soul.sty)
Provides:       tex(lwarp-soulpos.sty)
Provides:       tex(lwarp-soulutf8.sty)
Provides:       tex(lwarp-splitidx.sty)
Provides:       tex(lwarp-srcltx.sty)
Provides:       tex(lwarp-srctex.sty)
Provides:       tex(lwarp-stabular.sty)
Provides:       tex(lwarp-stackengine.sty)
Provides:       tex(lwarp-stackrel.sty)
Provides:       tex(lwarp-statex2.sty)
Provides:       tex(lwarp-statmath.sty)
Provides:       tex(lwarp-steinmetz.sty)
Provides:       tex(lwarp-stfloats.sty)
Provides:       tex(lwarp-struktex.sty)
Provides:       tex(lwarp-subcaption.sty)
Provides:       tex(lwarp-subfig.sty)
Provides:       tex(lwarp-subfigure.sty)
Provides:       tex(lwarp-subsupscripts.sty)
Provides:       tex(lwarp-supertabular.sty)
Provides:       tex(lwarp-svg.sty)
Provides:       tex(lwarp-syntonly.sty)
Provides:       tex(lwarp-tabfigures.sty)
Provides:       tex(lwarp-tablefootnote.sty)
Provides:       tex(lwarp-tabls.sty)
Provides:       tex(lwarp-tabularx.sty)
Provides:       tex(lwarp-tabulary.sty)
Provides:       tex(lwarp-tagpdf.sty)
Provides:       tex(lwarp-tascmac.sty)
Provides:       tex(lwarp-textarea.sty)
Provides:       tex(lwarp-textcomp.sty)
Provides:       tex(lwarp-textfit.sty)
Provides:       tex(lwarp-textpos.sty)
Provides:       tex(lwarp-theorem.sty)
Provides:       tex(lwarp-thinsp.sty)
Provides:       tex(lwarp-threadcol.sty)
Provides:       tex(lwarp-threeparttable.sty)
Provides:       tex(lwarp-threeparttablex.sty)
Provides:       tex(lwarp-thumb.sty)
Provides:       tex(lwarp-thumbs.sty)
Provides:       tex(lwarp-tikz.sty)
Provides:       tex(lwarp-titleps.sty)
Provides:       tex(lwarp-titleref.sty)
Provides:       tex(lwarp-titlesec.sty)
Provides:       tex(lwarp-titletoc.sty)
Provides:       tex(lwarp-titling.sty)
Provides:       tex(lwarp-tocbasic.sty)
Provides:       tex(lwarp-tocbibind.sty)
Provides:       tex(lwarp-tocdata.sty)
Provides:       tex(lwarp-tocenter.sty)
Provides:       tex(lwarp-tocloft.sty)
Provides:       tex(lwarp-tocstyle.sty)
Provides:       tex(lwarp-todo.sty)
Provides:       tex(lwarp-todonotes.sty)
Provides:       tex(lwarp-topcapt.sty)
Provides:       tex(lwarp-tram.sty)
Provides:       tex(lwarp-transparent.sty)
Provides:       tex(lwarp-trimclip.sty)
Provides:       tex(lwarp-trivfloat.sty)
Provides:       tex(lwarp-truncate.sty)
Provides:       tex(lwarp-turnthepage.sty)
Provides:       tex(lwarp-twoup.sty)
Provides:       tex(lwarp-typearea.sty)
Provides:       tex(lwarp-typicons.sty)
Provides:       tex(lwarp-ulem.sty)
Provides:       tex(lwarp-umoline.sty)
Provides:       tex(lwarp-underscore.sty)
Provides:       tex(lwarp-unicode-math.sty)
Provides:       tex(lwarp-units.sty)
Provides:       tex(lwarp-unitsdef.sty)
Provides:       tex(lwarp-upref.sty)
Provides:       tex(lwarp-url.sty)
Provides:       tex(lwarp-uspace.sty)
Provides:       tex(lwarp-verse.sty)
Provides:       tex(lwarp-versonotes.sty)
Provides:       tex(lwarp-vertbars.sty)
Provides:       tex(lwarp-vmargin.sty)
Provides:       tex(lwarp-vowel.sty)
Provides:       tex(lwarp-vpe.sty)
Provides:       tex(lwarp-vwcol.sty)
Provides:       tex(lwarp-wallpaper.sty)
Provides:       tex(lwarp-watermark.sty)
Provides:       tex(lwarp-widetable.sty)
Provides:       tex(lwarp-widows-and-orphans.sty)
Provides:       tex(lwarp-witharrows.sty)
Provides:       tex(lwarp-wrapfig.sty)
Provides:       tex(lwarp-xbmks.sty)
Provides:       tex(lwarp-xcolor.sty)
Provides:       tex(lwarp-xechangebar.sty)
Provides:       tex(lwarp-xellipsis.sty)
Provides:       tex(lwarp-xetexko-vertical.sty)
Provides:       tex(lwarp-xfakebold.sty)
Provides:       tex(lwarp-xfrac.sty)
Provides:       tex(lwarp-xltabular.sty)
Provides:       tex(lwarp-xltxtra.sty)
Provides:       tex(lwarp-xmpincl.sty)
Provides:       tex(lwarp-xpiano.sty)
Provides:       tex(lwarp-xpinyin.sty)
Provides:       tex(lwarp-xr-hyper.sty)
Provides:       tex(lwarp-xr.sty)
Provides:       tex(lwarp-xtab.sty)
Provides:       tex(lwarp-xunicode.sty)
Provides:       tex(lwarp-xurl.sty)
Provides:       tex(lwarp-xy.sty)
Provides:       tex(lwarp-zhlineskip.sty)
Provides:       tex(lwarp-zwpagelayout.sty)
Provides:       tex(lwarp.sty)
Requires:       tex(accsupp.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(comment.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(everyhook.sty)
Requires:       tex(expl3.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(footnote.sty)
Requires:       tex(geometry.sty)
Requires:       tex(gettitlestring.sty)
Requires:       tex(graphics.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(longtable.sty)
Requires:       tex(ltablex.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(manyfoot.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(microtype.sty)
Requires:       tex(mtcoff.sty)
Requires:       tex(multicol.sty)
Requires:       tex(musicography.sty)
Requires:       tex(nccfoots.sty)
Requires:       tex(newfloat.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(parallel.sty)
Requires:       tex(parcolumns.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(perpage.sty)
Requires:       tex(printlen.sty)
Requires:       tex(realscripts.sty)
Requires:       tex(refcount.sty)
Requires:       tex(soul.sty)
Requires:       tex(soulutf8.sty)
Requires:       tex(subfig.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tagpdf.sty)
Requires:       tex(upquote.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source108:      lwarp.tar.xz
Source109:      lwarp.doc.tar.xz

%description -n texlive-lwarp
This package converts LaTeX to HTML by using LaTeX to process
the user's document and generate HTML tags. External utility
programs are only used for the final conversion of text and
images. Math may be represented by SVG files or MathJax.
Hundreds of LaTeX packages are supported, and their load order
is automatically verified. Documents may be produced by LaTeX,
LuaLaTeX, XeLaTeX, and by several CJK engines, classes, and
packages. A texlua script automates compilation, index,
glossary, and batch image processing, and also supports
latexmk. Configuration is semi-automatic at the first manual
compile. Support files are self-generated. Print and HTML
versions of each document may coexist. Assistance is provided
for HTML import into EPUB conversion software and word
processors. Requirements include the commonly-available Poppler
utilities, and Perl. Detailed installation instructions are
included for each of the major operating systems and TeX
distributions. A quick-start tutorial is provided.

%package -n texlive-lwarp-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.83svn54586
Release:        0
Summary:        Documentation for texlive-lwarp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lwarp-doc
This package includes the documentation for texlive-lwarp

%post -n texlive-lwarp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lwarp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lwarp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lwarp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/lwarp/README.txt
%{_texmfdistdir}/doc/latex/lwarp/lwarp.pdf
%{_texmfdistdir}/doc/latex/lwarp/lwarp_tutorial.txt

%files -n texlive-lwarp
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/lwarp/lwarpmk.lua
%{_texmfdistdir}/tex/latex/lwarp/lwarp-2in1.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-2up.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-CJK.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-CJKutf8.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-DotArrow.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-SIunits.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-a4.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-a4wide.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-a5comb.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-abstract.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-academicons.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-accessibility.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-accsupp.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-acro.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-acronym.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-addlines.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-adjmulticol.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-afterpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-algorithm2e.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-algorithmicx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-alltt.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-amsmath.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-amsthm.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-anonchap.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-anysize.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-appendix.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ar.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-arabicfront.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-array.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-arydshln.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-asymptote.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-atbegshi.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-attachfile.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-attachfile2.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-authblk.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-autobreak.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-autonum.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-awesomebox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-axessibility.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-axodraw2.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-backnaur.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-backref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-balance.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bbding.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-biblatex.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bibunits.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bigdelim.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bigfoot.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bigstrut.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bitpattern.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-blowup.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bm.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-booklet.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bookmark.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-booktabs.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bophook.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bounddvi.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-boxedminipage2e.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-braket.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-breakurl.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-breqn.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bsheaders.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bxpapersize.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-bytefield.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-cancel.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-canoniclayout.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-caption.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-cases.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-centernot.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-changebar.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-changelayout.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-changepage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-changes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chappg.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chapterbib.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chemfig.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chemformula.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chemgreek.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chemmacros.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chemnum.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chkfloat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-chngpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-cite.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-clrdblpg.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-cmdtrack.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-colonequals.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-color.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-colortbl.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-common-multimedia.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-continue.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-copyrightbox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-crop.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ctable.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-cuted.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-cutwin.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-dblfloatfix.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-dblfnote.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-dcolumn.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-decimal.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-diagbox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-dingbat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-dotlessi.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-dprogress.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-draftcopy.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-draftfigure.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-draftwatermark.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-easy-todo.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ebook.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-econometrics.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ed.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ellipsis.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-embrac.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-emptypage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-endfloat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-endheads.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-endnotes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-engtlc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-enumerate.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-enumitem.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-epigraph.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-epsfig.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-epstopdf-base.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-epstopdf.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-eqlist.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-eqparbox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-errata.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-eso-pic.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-etoc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-eurosym.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-everypage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-everyshi.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-extarrows.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-extramarks.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fancybox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fancyhdr.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fancyref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fancytabs.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fancyvrb.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fewerfloatpages.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-figcaps.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-figsize.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fitbox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fix2col.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fixme.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fixmetodonotes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-flafter.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-flippdf.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-float.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-floatflt.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-floatpag.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-floatrow.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fltrace.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-flushend.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fnbreak.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fncychap.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fnlineno.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fnpos.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fontawesome.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fontawesome5.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fontaxes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fontenc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-footmisc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-footnote.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-footnotebackref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-footnotehyper.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-footnoterange.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-footnpag.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-foreign.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-forest.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fouridx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-framed.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ftcap.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ftnright.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fullminipage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fullpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fullwidth.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-fwlw.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-gensymb.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-gentombow.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-geometry.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ghsystem.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-gloss.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-glossaries.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-gmeometric.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-graphics.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-graphicx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-grffile.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-grid-system.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-grid.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-gridset.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hang.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hanging.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hhline.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hypbmsec.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hypcap.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hypdestopt.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hypernat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hyperref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hyperxmp.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-hyphenat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-idxlayout.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ifoddpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-imakeidx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-index.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-inputtrc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-intopdf.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-karnaugh-map.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-keyfloat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-layaureo.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-layout.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-layouts.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-leading.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-leftidx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-letterspace.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lettrine.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lineno.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lips.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-listings.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-listliketab.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lltjext.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-longtable.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lscape.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ltablex.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ltcaption.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ltxgrid.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ltxtable.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lua-check-hyphen.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lua-visual-debug.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-luacolor.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-luamplib.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-luatexko.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-luatodonotes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-lyluatex.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-magaz.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-makeidx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-manyfoot.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-marginal.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-marginfit.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-marginfix.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-marginnote.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-marvosym.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mathcomp.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mathdots.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mathfixs.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mathtools.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mcaption.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mdframed.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-media9.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-memhfixc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-metalogo.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-metalogox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mhchem.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-microtype.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-midfloat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-midpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-minibox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-minitoc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mismath.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-morefloats.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-moreverb.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-movie15.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-mparhack.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-multicap.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-multicol.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-multicolrule.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-multimedia.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-multiobjective.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-multirow.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-multitoc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-musicography.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nameauth.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nameref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-natbib.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nccfancyhdr.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nccfoots.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nccmath.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-needspace.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nextpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nfssext-cfr.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nicefrac.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-niceframe.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-noitcrul.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nolbreaks.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nomencl.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nonfloat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nonumonpart.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nopageno.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-notes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-notespages.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-nowidow.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ntheorem.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-octave.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-overpic.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pagegrid.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pagenote.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pagesel.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-paralist.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-parallel.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-parcolumns.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-parnotes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-parskip.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-patch-komascript.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-patch-memoir.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pbox.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfcol.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfcolfoot.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfcolmk.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfcolparallel.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfcolparcolumns.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfcomment.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfcrypt.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdflscape.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfmarginpar.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfpages.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfprivacy.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfrender.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfsync.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdftricks.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pdfx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-perpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pfnote.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-phfqit.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-physics.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-physunits.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pifont.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-placeins.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-plarydshln.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-plext.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-plextarydshln.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-plextcolorbl.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-prelim2e.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-prettyref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-preview.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-psfrag.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-psfragx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pst-eps.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pstool.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pstricks.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pxatbegshi.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pxeveryshi.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pxftnright.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-pxjahyper.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-quotchap.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-quoting.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ragged2e.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-realscripts.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-refcheck.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-register.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-relsize.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-repeatindex.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-resizegather.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-returntogrid.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-rmathbr.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-rmpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-romanbar.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-romanbarpagenumber.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-rotating.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-rotfloat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-rviewport.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-savetrees.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-scalefnt.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-schemata.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-scrextend.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-scrhack.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-scrlayer-notecolumn.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-scrlayer-scrpage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-scrlayer.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-scrpage2.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-section.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-sectionbreak.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-sectsty.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-semantic-markup.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-setspace.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-shadow.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-shapepar.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-showidx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-showkeys.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-showtags.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-sidecap.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-sidenotes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-siunitx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-slantsc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-slashed.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-soul.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-soulpos.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-soulutf8.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-splitidx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-srcltx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-srctex.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-stabular.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-stackengine.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-stackrel.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-statex2.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-statmath.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-steinmetz.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-stfloats.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-struktex.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-subcaption.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-subfig.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-subfigure.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-subsupscripts.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-supertabular.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-svg.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-syntonly.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tabfigures.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tablefootnote.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tabls.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tabularx.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tabulary.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tagpdf.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tascmac.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-textarea.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-textcomp.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-textfit.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-textpos.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-theorem.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-thinsp.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-threadcol.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-threeparttable.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-threeparttablex.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-thumb.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-thumbs.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tikz.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-titleps.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-titleref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-titlesec.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-titletoc.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-titling.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tocbasic.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tocbibind.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tocdata.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tocenter.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tocloft.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tocstyle.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-todo.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-todonotes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-topcapt.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-tram.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-transparent.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-trimclip.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-trivfloat.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-truncate.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-turnthepage.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-twoup.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-typearea.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-typicons.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-ulem.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-umoline.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-underscore.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-unicode-math.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-units.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-unitsdef.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-upref.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-url.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-uspace.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-verse.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-versonotes.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-vertbars.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-vmargin.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-vowel.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-vpe.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-vwcol.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-wallpaper.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-watermark.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-widetable.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-widows-and-orphans.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-witharrows.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-wrapfig.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xbmks.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xcolor.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xechangebar.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xellipsis.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xetexko-vertical.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xfakebold.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xfrac.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xltabular.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xltxtra.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xmpincl.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xpiano.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xpinyin.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xr-hyper.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xr.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xtab.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xunicode.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xurl.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-xy.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-zhlineskip.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp-zwpagelayout.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp.sty
%{_texmfdistdir}/tex/latex/lwarp/lwarp_baseline_marker.eps
%{_texmfdistdir}/tex/latex/lwarp/lwarp_baseline_marker.png
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lwarp-%{texlive_version}.%{texlive_noarch}.0.0.83svn54586-%{release}-zypper
%endif

%package -n texlive-lxfonts
Version:        %{texlive_version}.%{texlive_noarch}.2.0bsvn32354
Release:        0
Summary:        Set of slide fonts based on CM
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-lxfonts-fonts >= %{texlive_version}
Recommends:     texlive-lxfonts-doc >= %{texlive_version}
Provides:       tex(lcmbsy8.tfm)
Provides:       tex(lcmex8.tfm)
Provides:       tex(lcmmi8.tfm)
Provides:       tex(lcmmib8.tfm)
Provides:       tex(lcmsy8.tfm)
Provides:       tex(leclb8.tfm)
Provides:       tex(lecli8.tfm)
Provides:       tex(leclo8.tfm)
Provides:       tex(leclq8.tfm)
Provides:       tex(lgrllcmss.fd)
Provides:       tex(lgrllcmtt.fd)
Provides:       tex(llasy8.tfm)
Provides:       tex(llasyb8.tfm)
Provides:       tex(llcmss8.tfm)
Provides:       tex(llcmssb8.tfm)
Provides:       tex(llcmssi8.tfm)
Provides:       tex(llcmsso8.tfm)
Provides:       tex(lmsam8.tfm)
Provides:       tex(lmsbm8.tfm)
Provides:       tex(ltclb8.tfm)
Provides:       tex(ltcli8.tfm)
Provides:       tex(ltclo8.tfm)
Provides:       tex(ltclq8.tfm)
Provides:       tex(lxfonts.map)
Provides:       tex(lxfonts.sty)
Provides:       tex(omlllcmm.fd)
Provides:       tex(omsllcmsy.fd)
Provides:       tex(omxllcmex.fd)
Provides:       tex(ot1llcmss.fd)
Provides:       tex(ot1llcmtt.fd)
Provides:       tex(t1llcmss.fd)
Provides:       tex(t1llcmtt.fd)
Provides:       tex(ts1llcmss.fd)
Provides:       tex(ulllasy.fd)
Provides:       tex(ulmsa.fd)
Provides:       tex(ulmsb.fd)
Requires:       tex(etoolbox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source110:      lxfonts.tar.xz
Source111:      lxfonts.doc.tar.xz

%description -n texlive-lxfonts
The bundle contains the traditional slides fonts revised to be
completely usable both as text fonts and mathematics fonts;
they are fully integrate with the new operators, letters,
symbols and extensible delimiter fonts, as well as with the AMS
fonts, all redone with the same stylistic parameters.

%package -n texlive-lxfonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0bsvn32354
Release:        0
Summary:        Documentation for texlive-lxfonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lxfonts-doc
This package includes the documentation for texlive-lxfonts


%package -n texlive-lxfonts-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.0bsvn32354
Release:        0
Summary:        Severed fonts for texlive-lxfonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-lxfonts-fonts
The  separated fonts package for texlive-lxfonts
%post -n texlive-lxfonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap lxfonts.map' >> /var/run/texlive/run-updmap

%postun -n texlive-lxfonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap lxfonts.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-lxfonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-lxfonts-fonts
%files -n texlive-lxfonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/lxfonts/LXfonts-demo.pdf
%{_texmfdistdir}/doc/fonts/lxfonts/LXfonts-demo.tex
%{_texmfdistdir}/doc/fonts/lxfonts/LXfonts.readme
%{_texmfdistdir}/doc/fonts/lxfonts/README
%{_texmfdistdir}/doc/fonts/lxfonts/lxfonts.pdf
%{_texmfdistdir}/doc/fonts/lxfonts/manifest.txt

%files -n texlive-lxfonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/lxfonts/lxfonts.map
%{_texmfdistdir}/fonts/source/public/lxfonts/lamsya.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lamsyb.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lasymbols.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbigacc.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbigdel.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbigop.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lbsymbols.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmbsy8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmex8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmmi8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmmib8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lcmsy8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/leclb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lecli8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/leclo8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/leclq8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lexroman.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lexslides.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llasy.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llasy8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llasyb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmss8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmssb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmssi8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/llcmsso8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmathex.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmathit.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmathsy.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmsam8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lmsbm8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lroman.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltclb8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltcli8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltclo8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltclq8.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/ltxsymb.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lxbbase.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lxbbold.mf
%{_texmfdistdir}/fonts/source/public/lxfonts/lxbcaps.mf
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmbsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmex8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmmib8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lcmsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/leclb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lecli8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/leclo8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/leclq8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llasy8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llasyb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmssb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/llcmsso8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lmsam8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/lmsbm8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltclb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltcli8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltclo8.tfm
%{_texmfdistdir}/fonts/tfm/public/lxfonts/ltclq8.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lcmbsy8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lcmex8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lcmmi8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lcmmib8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lcmsy8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/leclb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lecli8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/leclo8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/leclq8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/llasy8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/llasyb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/llcmss8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/llcmssb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/llcmssi8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/llcmsso8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lmsam8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/lmsbm8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/ltclb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/ltcli8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/ltclo8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/lxfonts/ltclq8.pfb
%{_texmfdistdir}/tex/latex/lxfonts/lgrllcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/lgrllcmtt.fd
%{_texmfdistdir}/tex/latex/lxfonts/lxfonts.sty
%{_texmfdistdir}/tex/latex/lxfonts/omlllcmm.fd
%{_texmfdistdir}/tex/latex/lxfonts/omsllcmsy.fd
%{_texmfdistdir}/tex/latex/lxfonts/omxllcmex.fd
%{_texmfdistdir}/tex/latex/lxfonts/ot1llcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/ot1llcmtt.fd
%{_texmfdistdir}/tex/latex/lxfonts/t1llcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/t1llcmtt.fd
%{_texmfdistdir}/tex/latex/lxfonts/ts1llcmss.fd
%{_texmfdistdir}/tex/latex/lxfonts/ulllasy.fd
%{_texmfdistdir}/tex/latex/lxfonts/ulmsa.fd
%{_texmfdistdir}/tex/latex/lxfonts/ulmsb.fd

%files -n texlive-lxfonts-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-lxfonts
%{_datadir}/fontconfig/conf.avail/58-texlive-lxfonts.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-lxfonts/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-lxfonts/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-lxfonts/fonts.scale
%{_datadir}/fonts/texlive-lxfonts/lcmbsy8.pfb
%{_datadir}/fonts/texlive-lxfonts/lcmex8.pfb
%{_datadir}/fonts/texlive-lxfonts/lcmmi8.pfb
%{_datadir}/fonts/texlive-lxfonts/lcmmib8.pfb
%{_datadir}/fonts/texlive-lxfonts/lcmsy8.pfb
%{_datadir}/fonts/texlive-lxfonts/leclb8.pfb
%{_datadir}/fonts/texlive-lxfonts/lecli8.pfb
%{_datadir}/fonts/texlive-lxfonts/leclo8.pfb
%{_datadir}/fonts/texlive-lxfonts/leclq8.pfb
%{_datadir}/fonts/texlive-lxfonts/llasy8.pfb
%{_datadir}/fonts/texlive-lxfonts/llasyb8.pfb
%{_datadir}/fonts/texlive-lxfonts/llcmss8.pfb
%{_datadir}/fonts/texlive-lxfonts/llcmssb8.pfb
%{_datadir}/fonts/texlive-lxfonts/llcmssi8.pfb
%{_datadir}/fonts/texlive-lxfonts/llcmsso8.pfb
%{_datadir}/fonts/texlive-lxfonts/lmsam8.pfb
%{_datadir}/fonts/texlive-lxfonts/lmsbm8.pfb
%{_datadir}/fonts/texlive-lxfonts/ltclb8.pfb
%{_datadir}/fonts/texlive-lxfonts/ltcli8.pfb
%{_datadir}/fonts/texlive-lxfonts/ltclo8.pfb
%{_datadir}/fonts/texlive-lxfonts/ltclq8.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lxfonts-fonts-%{texlive_version}.%{texlive_noarch}.2.0bsvn32354-%{release}-zypper
%endif

%package -n texlive-ly1
Version:        %{texlive_version}.%{texlive_noarch}.svn47848
Release:        0
Summary:        Support for LY1 LaTeX encoding
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ly1-doc >= %{texlive_version}
Provides:       tex(ly1enc.def)
Provides:       tex(ly1pag.fd)
Provides:       tex(ly1pbk.fd)
Provides:       tex(ly1pcr.fd)
Provides:       tex(ly1phv.fd)
Provides:       tex(ly1pnc.fd)
Provides:       tex(ly1ppl.fd)
Provides:       tex(ly1ptm.fd)
Provides:       tex(ly1pzc.fd)
Provides:       tex(pag8y.map)
Provides:       tex(pagd8y.tfm)
Provides:       tex(pagdo8y.tfm)
Provides:       tex(pagk8y.tfm)
Provides:       tex(pagko8y.tfm)
Provides:       tex(pbk8y.map)
Provides:       tex(pbkd8y.tfm)
Provides:       tex(pbkdi8y.tfm)
Provides:       tex(pbkdo8y.tfm)
Provides:       tex(pbkl8y.tfm)
Provides:       tex(pbkli8y.tfm)
Provides:       tex(pbklo8y.tfm)
Provides:       tex(pcr8y.map)
Provides:       tex(pcrb8y.tfm)
Provides:       tex(pcrbo8y.tfm)
Provides:       tex(pcrr8y.tfm)
Provides:       tex(pcrro8y.tfm)
Provides:       tex(phv8y.map)
Provides:       tex(phvb8y.tfm)
Provides:       tex(phvb8yn.tfm)
Provides:       tex(phvbo8y.tfm)
Provides:       tex(phvbo8yn.tfm)
Provides:       tex(phvr8y.tfm)
Provides:       tex(phvr8yn.tfm)
Provides:       tex(phvro8y.tfm)
Provides:       tex(phvro8yn.tfm)
Provides:       tex(pnc8y.map)
Provides:       tex(pncb8y.tfm)
Provides:       tex(pncbi8y.tfm)
Provides:       tex(pncbo8y.tfm)
Provides:       tex(pncr8y.tfm)
Provides:       tex(pncri8y.tfm)
Provides:       tex(pncro8y.tfm)
Provides:       tex(ppl8y.map)
Provides:       tex(pplb8y.tfm)
Provides:       tex(pplbi8y.tfm)
Provides:       tex(pplbo8y.tfm)
Provides:       tex(pplbu8y.tfm)
Provides:       tex(pplr8y.tfm)
Provides:       tex(pplr8yn.tfm)
Provides:       tex(pplri8y.tfm)
Provides:       tex(pplro8y.tfm)
Provides:       tex(pplrr8ye.tfm)
Provides:       tex(pplru8y.tfm)
Provides:       tex(ptm8y.map)
Provides:       tex(ptmb8y.tfm)
Provides:       tex(ptmbc8y.tfm)
Provides:       tex(ptmbc8y.vf)
Provides:       tex(ptmbi8y.tfm)
Provides:       tex(ptmbo8y.tfm)
Provides:       tex(ptmr8y.tfm)
Provides:       tex(ptmr8yn.tfm)
Provides:       tex(ptmrc8y.tfm)
Provides:       tex(ptmrc8y.vf)
Provides:       tex(ptmri8y.tfm)
Provides:       tex(ptmro8y.tfm)
Provides:       tex(ptmrr8ye.tfm)
Provides:       tex(pzc8y.map)
Provides:       tex(pzcmi8y.tfm)
Provides:       tex(texnansi.enc)
Provides:       tex(texnansi.sty)
Provides:       tex(texnansi.tex)
Requires:       tex(fontenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source112:      ly1.tar.xz
Source113:      ly1.doc.tar.xz

%description -n texlive-ly1
The Y&Y 'texnansi' (TeX and ANSI, for Microsoft interpretations
of ANSI standards) encoding lives on, even after the decease of
the company; it is known in the LaTeX scheme of things as LY1
encoding. This bundle includes metrics and LaTeX macros to use
the basic three (Times, Helvetica and Courier) Adobe Type 1
fonts in LaTeX using LY1 encoding.

%package -n texlive-ly1-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn47848
Release:        0
Summary:        Documentation for texlive-ly1
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ly1-doc
This package includes the documentation for texlive-ly1

%post -n texlive-ly1
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ly1 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ly1
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ly1-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/ly1/README

%files -n texlive-ly1
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/ly1/texnansi.enc
%{_texmfdistdir}/fonts/map/dvips/ly1/pag8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pbk8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pcr8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/phv8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pnc8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/ppl8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/ptm8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pzc8y.map
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagd8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagdo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagk8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagko8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkd8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkdi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkdo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkl8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkli8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbklo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvb8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvbo8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvr8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvro8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncbi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncri8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplbi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplbu8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplr8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplri8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplrr8ye.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplru8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmbc8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmbi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmr8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmrc8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmri8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmrr8ye.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pzcmi8y.tfm
%{_texmfdistdir}/fonts/vf/adobe/ly1/ptmbc8y.vf
%{_texmfdistdir}/fonts/vf/adobe/ly1/ptmrc8y.vf
%{_texmfdistdir}/tex/latex/ly1/ly1enc.def
%{_texmfdistdir}/tex/latex/ly1/ly1pag.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pbk.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pcr.fd
%{_texmfdistdir}/tex/latex/ly1/ly1phv.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pnc.fd
%{_texmfdistdir}/tex/latex/ly1/ly1ppl.fd
%{_texmfdistdir}/tex/latex/ly1/ly1ptm.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pzc.fd
%{_texmfdistdir}/tex/latex/ly1/texnansi.sty
%{_texmfdistdir}/tex/plain/ly1/texnansi.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ly1-%{texlive_version}.%{texlive_noarch}.svn47848-%{release}-zypper
%endif

%package -n texlive-lyluatex
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn51252
Release:        0
Summary:        Commands to include lilypond scores within a (Lua)LaTeX document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-lyluatex-doc >= %{texlive_version}
Provides:       tex(lyluatex.sty)
Requires:       tex(currfile.sty)
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(minibox.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source114:      lyluatex.tar.xz
Source115:      lyluatex.doc.tar.xz

%description -n texlive-lyluatex
This package provides macros for the inclusion of LilyPond
scores within LuaLaTeX. It calls LilyPond to compile scores,
then includes the produced files. Dependencies: currfile,
environ, graphicx, luaotfload, luatexbase, metalogo, minibox,
pdfpages, xkeyval.

%package -n texlive-lyluatex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn51252
Release:        0
Summary:        Documentation for texlive-lyluatex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-lyluatex-doc
This package includes the documentation for texlive-lyluatex

%post -n texlive-lyluatex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-lyluatex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-lyluatex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-lyluatex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/lyluatex/Contributors.md
%{_texmfdistdir}/doc/support/lyluatex/LICENSE
%{_texmfdistdir}/doc/support/lyluatex/README.md
%{_texmfdistdir}/doc/support/lyluatex/latexmkrc
%{_texmfdistdir}/doc/support/lyluatex/ly/eight-systems.ly
%{_texmfdistdir}/doc/support/lyluatex/ly/fonts.ly
%{_texmfdistdir}/doc/support/lyluatex/lyluatex.pdf
%{_texmfdistdir}/doc/support/lyluatex/lyluatex.tex
%{_texmfdistdir}/doc/support/lyluatex/lyluatexbase.cls
%{_texmfdistdir}/doc/support/lyluatex/lyluatexmanual.cls

%files -n texlive-lyluatex
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/lyluatex/lyluatex-lib.lua
%{_texmfdistdir}/scripts/lyluatex/lyluatex-options.lua
%{_texmfdistdir}/scripts/lyluatex/lyluatex.lua
%{_texmfdistdir}/tex/luatex/lyluatex/lyluatex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-lyluatex-%{texlive_version}.%{texlive_noarch}.1.0fsvn51252-%{release}-zypper
%endif

%package -n texlive-m-tx
Version:        %{texlive_version}.%{texlive_noarch}.0.0.63csvn52851
Release:        0
Summary:        A preprocessor for pmx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-m-tx-bin >= %{texlive_version}
#!BuildIgnore: texlive-m-tx-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-m-tx-doc >= %{texlive_version}
Provides:       tex(mtx.tex)
Provides:       tex(mtxlatex.sty)
Requires:       tex(etex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source116:      m-tx.tar.xz
Source117:      m-tx.doc.tar.xz

%description -n texlive-m-tx
M-Tx is a preprocessor to pmx, which is itself a preprocessor
to musixtex, a music typesetting system. The prime motivation
to the development of M-Tx was to provide lyrics for music to
be typeset. In fact, pmx now provides a lyrics interface, but
M-Tx continues in use by those who prefer its language.

%package -n texlive-m-tx-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.63csvn52851
Release:        0
Summary:        Documentation for texlive-m-tx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(prepmx.1)

%description -n texlive-m-tx-doc
This package includes the documentation for texlive-m-tx

%post -n texlive-m-tx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-m-tx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-m-tx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-m-tx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/m-tx/Makefile
%{_texmfdistdir}/doc/generic/m-tx/README
%{_texmfdistdir}/doc/generic/m-tx/README.documentation
%{_texmfdistdir}/doc/generic/m-tx/borup.mtx
%{_texmfdistdir}/doc/generic/m-tx/borup.pdf
%{_texmfdistdir}/doc/generic/m-tx/buildmtxdoc.lua
%{_texmfdistdir}/doc/generic/m-tx/buildzip.lua
%{_texmfdistdir}/doc/generic/m-tx/chord.mtx
%{_texmfdistdir}/doc/generic/m-tx/dertod.mtx
%{_texmfdistdir}/doc/generic/m-tx/dona.mtx
%{_texmfdistdir}/doc/generic/m-tx/dwoman.mta
%{_texmfdistdir}/doc/generic/m-tx/dwoman.mtb
%{_texmfdistdir}/doc/generic/m-tx/dwoman.mtx
%{_texmfdistdir}/doc/generic/m-tx/halleluja.ltx
%{_texmfdistdir}/doc/generic/m-tx/halleluja.pdf
%{_texmfdistdir}/doc/generic/m-tx/hallelujashort.ltx
%{_texmfdistdir}/doc/generic/m-tx/kanons.ltx
%{_texmfdistdir}/doc/generic/m-tx/kanons.pdf
%{_texmfdistdir}/doc/generic/m-tx/kroonhom.mtx
%{_texmfdistdir}/doc/generic/m-tx/loofnou.mtx
%{_texmfdistdir}/doc/generic/m-tx/lyrics.tex
%{_texmfdistdir}/doc/generic/m-tx/macro.mtx
%{_texmfdistdir}/doc/generic/m-tx/make-dvi
%{_texmfdistdir}/doc/generic/m-tx/make-pdf
%{_texmfdistdir}/doc/generic/m-tx/make-target
%{_texmfdistdir}/doc/generic/m-tx/melisma.mta
%{_texmfdistdir}/doc/generic/m-tx/melisma1.mtb
%{_texmfdistdir}/doc/generic/m-tx/melisma1.mtx
%{_texmfdistdir}/doc/generic/m-tx/melisma2.mtb
%{_texmfdistdir}/doc/generic/m-tx/melisma2.mtx
%{_texmfdistdir}/doc/generic/m-tx/melisma3.mtb
%{_texmfdistdir}/doc/generic/m-tx/melisma3.mtx
%{_texmfdistdir}/doc/generic/m-tx/melisma4.mtb
%{_texmfdistdir}/doc/generic/m-tx/melisma4.mtx
%{_texmfdistdir}/doc/generic/m-tx/melisma5.mtb
%{_texmfdistdir}/doc/generic/m-tx/melisma5.mtx
%{_texmfdistdir}/doc/generic/m-tx/melisma6.mtb
%{_texmfdistdir}/doc/generic/m-tx/melisma6.mtx
%{_texmfdistdir}/doc/generic/m-tx/meter.mtx
%{_texmfdistdir}/doc/generic/m-tx/mozart.mtx
%{_texmfdistdir}/doc/generic/m-tx/mozart0.mtx
%{_texmfdistdir}/doc/generic/m-tx/mtx-install.pdf
%{_texmfdistdir}/doc/generic/m-tx/mtx-install.tex
%{_texmfdistdir}/doc/generic/m-tx/mtxdoc.ltx
%{_texmfdistdir}/doc/generic/m-tx/mtxdoc.pdf
%{_texmfdistdir}/doc/generic/m-tx/mtxdoc.sty
%{_texmfdistdir}/doc/generic/m-tx/mtxindex.tex
%{_texmfdistdir}/doc/generic/m-tx/netfirst.mtx
%{_texmfdistdir}/doc/generic/m-tx/netsoos.mta
%{_texmfdistdir}/doc/generic/m-tx/netsoos1.mtb
%{_texmfdistdir}/doc/generic/m-tx/netsoos1.mtx
%{_texmfdistdir}/doc/generic/m-tx/netsoos2.mtb
%{_texmfdistdir}/doc/generic/m-tx/netsoos2.mtx
%{_texmfdistdir}/doc/generic/m-tx/notes.tex
%{_texmfdistdir}/doc/generic/m-tx/pdfcat
%{_texmfdistdir}/doc/generic/m-tx/prepmx.pdf
%{_texmfdistdir}/doc/generic/m-tx/psalm42.mtx
%{_texmfdistdir}/doc/generic/m-tx/sanctus.mtx
%{_texmfdistdir}/doc/generic/m-tx/title.mtx
%{_texmfdistdir}/doc/generic/m-tx/title1.mtx
%{_texmfdistdir}/doc/generic/m-tx/viva.mtx
%{_texmfdistdir}/doc/generic/m-tx/volta.mtx
%{_mandir}/man1/prepmx.1*

%files -n texlive-m-tx
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/m-tx/m-tx.lua
%{_texmfdistdir}/tex/generic/m-tx/mtx.tex
%{_texmfdistdir}/tex/latex/m-tx/mtxlatex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-m-tx-%{texlive_version}.%{texlive_noarch}.0.0.63csvn52851-%{release}-zypper
%endif

%package -n texlive-macros2e
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn46026
Release:        0
Summary:        A list of internal LaTeX2e macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-macros2e-doc >= %{texlive_version}
Provides:       tex(extlabels.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(zref-abspos.sty)
Requires:       tex(zref-user.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source118:      macros2e.tar.xz
Source119:      macros2e.doc.tar.xz

%description -n texlive-macros2e
This document lists the internal macros defined by the LaTeX2e
base files which can also be useful to package authors. The
macros are hyper-linked to their description in source2e. For
this to work both PDFs must be inside the same directory. This
document is not yet complete in content and format and may miss
some macros.

%package -n texlive-macros2e-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn46026
Release:        0
Summary:        Documentation for texlive-macros2e
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-macros2e-doc
This package includes the documentation for texlive-macros2e

%post -n texlive-macros2e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-macros2e 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-macros2e
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-macros2e-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/macros2e/Makefile
%{_texmfdistdir}/doc/latex/macros2e/README
%{_texmfdistdir}/doc/latex/macros2e/macros2e.pdf
%{_texmfdistdir}/doc/latex/macros2e/macros2e.tex

%files -n texlive-macros2e
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/macros2e/extlabels.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-macros2e-%{texlive_version}.%{texlive_noarch}.0.0.4asvn46026-%{release}-zypper
%endif

%package -n texlive-macroswap
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn31498
Release:        0
Summary:        Swap the definitions of two LaTeX macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-macroswap-doc >= %{texlive_version}
Provides:       tex(macroswap.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source120:      macroswap.tar.xz
Source121:      macroswap.doc.tar.xz

%description -n texlive-macroswap
The package provides simple utility methods to swap the meaning
(token expansion) of two macros by name.

%package -n texlive-macroswap-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn31498
Release:        0
Summary:        Documentation for texlive-macroswap
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-macroswap-doc
This package includes the documentation for texlive-macroswap

%post -n texlive-macroswap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-macroswap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-macroswap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-macroswap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/macroswap/Makefile
%{_texmfdistdir}/doc/latex/macroswap/README
%{_texmfdistdir}/doc/latex/macroswap/macroswap.pdf

%files -n texlive-macroswap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/macroswap/macroswap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-macroswap-%{texlive_version}.%{texlive_noarch}.1.1svn31498-%{release}-zypper
%endif

%package -n texlive-mafr
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Mathematics in accord with French usage
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mafr-doc >= %{texlive_version}
Provides:       tex(cours.cls)
Provides:       tex(fiche.cls)
Provides:       tex(mafr.sty)
Requires:       tex(a4wide.sty)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(fontenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source122:      mafr.tar.xz
Source123:      mafr.doc.tar.xz

%description -n texlive-mafr
The package provides settings and macros for typesetting
mathematics with LaTeX in compliance with French usage. It
comes with two document classes, 'fiche' and 'cours', useful to
create short high school documents such as tests or lessons.
The documentation is in French.

%package -n texlive-mafr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-mafr
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-mafr-doc:fr;en)

%description -n texlive-mafr-doc
This package includes the documentation for texlive-mafr

%post -n texlive-mafr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mafr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mafr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mafr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mafr/ALIRE
%{_texmfdistdir}/doc/latex/mafr/COPYING
%{_texmfdistdir}/doc/latex/mafr/README
%{_texmfdistdir}/doc/latex/mafr/docmafr.pdf
%{_texmfdistdir}/doc/latex/mafr/docmafr.tex
%{_texmfdistdir}/doc/latex/mafr/triangle.eps

%files -n texlive-mafr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mafr/cours.cls
%{_texmfdistdir}/tex/latex/mafr/fiche.cls
%{_texmfdistdir}/tex/latex/mafr/mafr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mafr-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-magaz
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn24694
Release:        0
Summary:        Magazine layout
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-magaz-doc >= %{texlive_version}
Provides:       tex(magaz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source124:      magaz.tar.xz
Source125:      magaz.doc.tar.xz

%description -n texlive-magaz
The current version does special formatting for the first line
of text in a paragraph. The package is part of a larger body of
tools which remain in preparation.

%package -n texlive-magaz-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn24694
Release:        0
Summary:        Documentation for texlive-magaz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-magaz-doc
This package includes the documentation for texlive-magaz

%post -n texlive-magaz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-magaz 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-magaz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-magaz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/magaz/magaz.pdf
%{_texmfdistdir}/doc/latex/magaz/magaz.tex

%files -n texlive-magaz
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/magaz/magaz.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-magaz-%{texlive_version}.%{texlive_noarch}.0.0.4svn24694-%{release}-zypper
%endif

%package -n texlive-magicnum
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn52983
Release:        0
Summary:        Access TeX systems' "magic numbers"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-magicnum-doc >= %{texlive_version}
Provides:       tex(magicnum.sty)
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source126:      magicnum.tar.xz
Source127:      magicnum.doc.tar.xz

%description -n texlive-magicnum
This package allows access to the various parameter values in
TeX (catcode values), e-TeX (group, if and node types, and
interaction mode), and LuaTeX (pdfliteral mode) by a
hierarchical name system.

%package -n texlive-magicnum-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn52983
Release:        0
Summary:        Documentation for texlive-magicnum
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-magicnum-doc
This package includes the documentation for texlive-magicnum

%post -n texlive-magicnum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-magicnum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-magicnum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-magicnum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/magicnum/README.md
%{_texmfdistdir}/doc/latex/magicnum/magicnum.pdf
%{_texmfdistdir}/doc/latex/magicnum/magicnum.txt

%files -n texlive-magicnum
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/magicnum/magicnum.lua
%{_texmfdistdir}/tex/generic/magicnum/magicnum.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-magicnum-%{texlive_version}.%{texlive_noarch}.1.7svn52983-%{release}-zypper
%endif

%package -n texlive-mailing
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Macros for mail merging
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mailing-doc >= %{texlive_version}
Provides:       tex(mailing.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source128:      mailing.tar.xz
Source129:      mailing.doc.tar.xz

%description -n texlive-mailing
This package is for use when sending a large number of letters,
all with the same body text. The package's \addressfile command
is used to specify who the letter is to be sent to; the body of
the \mailingtext command specifies the text of the letters,
possibly using macros defined in the \addressfile.

%package -n texlive-mailing-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-mailing
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mailing-doc
This package includes the documentation for texlive-mailing

%post -n texlive-mailing
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mailing 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mailing
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mailing-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mailing/mailing.pdf
%{_texmfdistdir}/doc/latex/mailing/manifest.txt

%files -n texlive-mailing
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mailing/mailing.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mailing-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-mailmerge
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Repeating text field substitution
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mailmerge-doc >= %{texlive_version}
Provides:       tex(mailmerge.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source130:      mailmerge.tar.xz
Source131:      mailmerge.doc.tar.xz

%description -n texlive-mailmerge
The package mailmerge provides an interface to produce text
from a template, where fields are replaced by actual data, as
in a database. The package may be used to produce several
letters from a template, certificates or other such documents.
It allows access to the entry number, number of entries and so
on.

%package -n texlive-mailmerge-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-mailmerge
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mailmerge-doc
This package includes the documentation for texlive-mailmerge

%post -n texlive-mailmerge
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mailmerge 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mailmerge
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mailmerge-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mailmerge/README
%{_texmfdistdir}/doc/latex/mailmerge/mailmerge.pdf

%files -n texlive-mailmerge
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mailmerge/mailmerge.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mailmerge-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-make4ht
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3esvn54080
Release:        0
Summary:        A build system for tex4ht
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-make4ht-bin >= %{texlive_version}
#!BuildIgnore: texlive-make4ht-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-make4ht-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source132:      make4ht.tar.xz
Source133:      make4ht.doc.tar.xz

%description -n texlive-make4ht
make4ht is a simple build system for tex4ht, a TeX to XML
converter. It provides a command line tool that drives the
conversion process. It also provides a library which can be
used to create customized conversion tools.

%package -n texlive-make4ht-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3esvn54080
Release:        0
Summary:        Documentation for texlive-make4ht
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-make4ht-doc
This package includes the documentation for texlive-make4ht

%post -n texlive-make4ht
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-make4ht 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-make4ht
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-make4ht-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/make4ht/README
%{_texmfdistdir}/doc/support/make4ht/changelog.tex
%{_texmfdistdir}/doc/support/make4ht/make4ht-doc.pdf
%{_texmfdistdir}/doc/support/make4ht/make4ht-doc.tex
%{_texmfdistdir}/doc/support/make4ht/readme.tex

%files -n texlive-make4ht
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-aeneas.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-booktabs.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-collapsetoc.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-fixinlines.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-idcolons.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-joincharacters.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-joincolors.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-mathmlfixes.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-odtimagesize.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-odtpartable.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-t4htlinks.lua
%{_texmfdistdir}/scripts/make4ht/domfilters/make4ht-tablerows.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-common_domfilters.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-common_filters.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-detect_engine.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-dvisvgm_hashes.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-join_colors.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-latexmk_build.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-mathjaxnode.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-odttemplate.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-preprocess_input.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-staticsite.lua
%{_texmfdistdir}/scripts/make4ht/extensions/make4ht-ext-tidy.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-cleanspan-nat.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-cleanspan.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-domfilter.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-entities-to-unicode.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-entities.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-filter.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-fix-links.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-fixligatures.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-hruletohr.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-mathjaxnode.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-odttemplate.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-staticsite.lua
%{_texmfdistdir}/scripts/make4ht/filters/make4ht-svg-height.lua
%{_texmfdistdir}/scripts/make4ht/formats/make4ht-docbook.lua
%{_texmfdistdir}/scripts/make4ht/formats/make4ht-html5.lua
%{_texmfdistdir}/scripts/make4ht/formats/make4ht-odt.lua
%{_texmfdistdir}/scripts/make4ht/formats/make4ht-tei.lua
%{_texmfdistdir}/scripts/make4ht/formats/make4ht-xhtml.lua
%{_texmfdistdir}/scripts/make4ht/lapp-mk4.lua
%{_texmfdistdir}/scripts/make4ht/make4ht
%{_texmfdistdir}/scripts/make4ht/make4ht-aeneas-config.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-config.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-dvireader.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-errorlogparser.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-filterlib.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-htlatex.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-indexing.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-lib.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-logging.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-odtfilter.lua
%{_texmfdistdir}/scripts/make4ht/make4ht-xtpipes.lua
%{_texmfdistdir}/scripts/make4ht/mkparams.lua
%{_texmfdistdir}/scripts/make4ht/mkutils.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-make4ht-%{texlive_version}.%{texlive_noarch}.0.0.3esvn54080-%{release}-zypper
%endif

%package -n texlive-makebarcode
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Print various kinds 2/5 and Code 39 bar codes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makebarcode-doc >= %{texlive_version}
Provides:       tex(makebarcode.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source134:      makebarcode.tar.xz
Source135:      makebarcode.doc.tar.xz

%description -n texlive-makebarcode
The package contains macros for printing various 2/5 bar codes
and Code 39 bar codes. The macros do not use fonts but create
the bar codes directly using vertical rules. It is therefore
possible to vary width to height ratio, ratio of thin and thick
bars. The package is therefore convenient for printing ITF bar
codes as well as bar codes for identification labels for HP
storage media.

%package -n texlive-makebarcode-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-makebarcode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makebarcode-doc
This package includes the documentation for texlive-makebarcode

%post -n texlive-makebarcode
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makebarcode 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makebarcode
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makebarcode-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makebarcode/License.txt
%{_texmfdistdir}/doc/latex/makebarcode/README
%{_texmfdistdir}/doc/latex/makebarcode/makebarcode.pdf
%{_texmfdistdir}/doc/latex/makebarcode/makebarcode.tex

%files -n texlive-makebarcode
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makebarcode/makebarcode.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makebarcode-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-makebase
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn41012
Release:        0
Summary:        Typeset counters in a different base
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makebase-doc >= %{texlive_version}
Provides:       tex(makebase.sty)
Requires:       tex(calc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source136:      makebase.tar.xz
Source137:      makebase.doc.tar.xz

%description -n texlive-makebase
This package typesets a LaTeX counter such as page in an
arbitrary base (default 16). It does not change font or
typeface. The package extends the functionality of the existing
hex LaTeX 2.09 package and provides documentation. However, the
author is not a mathematician, and suggestions for rewriting
the code are welcomed. Warning: this is alpha software and may
contain bugs. Please report problems to the author.

%package -n texlive-makebase-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn41012
Release:        0
Summary:        Documentation for texlive-makebase
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makebase-doc
This package includes the documentation for texlive-makebase

%post -n texlive-makebase
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makebase 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makebase
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makebase-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makebase/MANIFEST
%{_texmfdistdir}/doc/latex/makebase/README.md
%{_texmfdistdir}/doc/latex/makebase/makebase-test.tex
%{_texmfdistdir}/doc/latex/makebase/makebase.pdf

%files -n texlive-makebase
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makebase/makebase.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makebase-%{texlive_version}.%{texlive_noarch}.0.0.2svn41012-%{release}-zypper
%endif

%package -n texlive-makebox
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Defines a \makebox* command
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makebox-doc >= %{texlive_version}
Provides:       tex(makebox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source138:      makebox.tar.xz
Source139:      makebox.doc.tar.xz

%description -n texlive-makebox
Define a \makebox* command that does the same as a \makebox
command, except that the width is given by a sample text
instead of an explicit length measure.

%package -n texlive-makebox-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-makebox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makebox-doc
This package includes the documentation for texlive-makebox

%post -n texlive-makebox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makebox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makebox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makebox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makebox/ChangeLog
%{_texmfdistdir}/doc/latex/makebox/README
%{_texmfdistdir}/doc/latex/makebox/getversion.tex
%{_texmfdistdir}/doc/latex/makebox/makebox.pdf
%{_texmfdistdir}/doc/latex/makebox/makebox.xml
%{_texmfdistdir}/doc/latex/makebox/testmakebox.tex

%files -n texlive-makebox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makebox/makebox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makebox-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif

%package -n texlive-makecell
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1esvn15878
Release:        0
Summary:        Tabular column heads and multilined cells
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makecell-doc >= %{texlive_version}
Provides:       tex(makecell.sty)
Requires:       tex(array.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source140:      makecell.tar.xz
Source141:      makecell.doc.tar.xz

%description -n texlive-makecell
This package supports common layouts for tabular column heads
in whole documents, based on one-column tabular environment. In
addition, it can create multi-lined tabular cells. The Package
also offers: a macro which changes the vertical space around
all the cells in a tabular environment (similar to the function
of the tabls package, but using the facilities of the array)
macros for multirow cells, which use the facilities of the
multirow package; macros to number rows in tables, or to skip
cells; diagonally divided cells; horizontal lines in tabular
environments with defined thickness.

%package -n texlive-makecell-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1esvn15878
Release:        0
Summary:        Documentation for texlive-makecell
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-makecell-doc:ru;en)

%description -n texlive-makecell-doc
This package includes the documentation for texlive-makecell

%post -n texlive-makecell
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makecell 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makecell
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makecell-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makecell/README
%{_texmfdistdir}/doc/latex/makecell/makecell-rus.pdf
%{_texmfdistdir}/doc/latex/makecell/makecell-rus.tex
%{_texmfdistdir}/doc/latex/makecell/makecell.pdf

%files -n texlive-makecell
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makecell/makecell.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makecell-%{texlive_version}.%{texlive_noarch}.0.0.1esvn15878-%{release}-zypper
%endif

%package -n texlive-makecirc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A MetaPost library for drawing electrical circuit diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makecirc-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source142:      makecirc.tar.xz
Source143:      makecirc.doc.tar.xz

%description -n texlive-makecirc
MakeCirc is a MetaPost library that contains diverse symbols
for use in circuit diagrams. MakeCirc offers a high quality
tool, with a simple syntax. MakeCirc is completely integrated
with LaTeX documents and with other MetaPost drawing/graphic.
Its output is a PostScript file. MakeCirc only requires (La)TeX
and MetaPost to work.

%package -n texlive-makecirc-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-makecirc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-makecirc-doc:en;es)

%description -n texlive-makecirc-doc
This package includes the documentation for texlive-makecirc

%post -n texlive-makecirc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makecirc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makecirc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makecirc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/makecirc/MakeCirc-en.pdf
%{_texmfdistdir}/doc/metapost/makecirc/MakeCirc.pdf
%{_texmfdistdir}/doc/metapost/makecirc/README
%{_texmfdistdir}/doc/metapost/makecirc/ejemplos.pdf

%files -n texlive-makecirc
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/makecirc/ejemplos.mp
%{_texmfdistdir}/metapost/makecirc/latex.mp
%{_texmfdistdir}/metapost/makecirc/makecirc.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makecirc-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-makecmds
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        The new \makecommand command always (re)defines a command
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makecmds-doc >= %{texlive_version}
Provides:       tex(makecmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source144:      makecmds.tar.xz
Source145:      makecmds.doc.tar.xz

%description -n texlive-makecmds
The package provides a \makecommand command, which is like
\(re)newcommand except it always (re)defines a command. There
is also \makeenvironment and \provideenvironment for
environments.

%package -n texlive-makecmds-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-makecmds
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makecmds-doc
This package includes the documentation for texlive-makecmds

%post -n texlive-makecmds
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makecmds 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makecmds
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makecmds-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makecmds/README
%{_texmfdistdir}/doc/latex/makecmds/makecmds.pdf

%files -n texlive-makecmds
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makecmds/makecmds.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makecmds-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-makecookbook
Version:        %{texlive_version}.%{texlive_noarch}.0.0.85svn49311
Release:        0
Summary:        Make a Cookbook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source146:      makecookbook.doc.tar.xz

%description -n texlive-makecookbook
The makecookbook bundle contains the files needed to create a
nice quality family cookbook in a form ready to submit to most
print-on-demand companies. Modifiable choices have been made
regarding standard book features such as trim size, margins,
headers/footers, chapter heading formatting, front matter
(copyright page, table of contents, etc.) and back matter
(index). Commands and environments have been created to format
the food stories and recipes. The user will need to: supply
their own food stories and recipes(!), and install the needed
fonts. We assume a LuaTeX compile. Please note that no new
document class or package is included here. Rather, we provide
a modifiable preamble and a small number of other files that,
together, fully support creation of all of the internal pages
of a cookbook (i.e., everything except the cover art).
%post -n texlive-makecookbook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makecookbook 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makecookbook
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makecookbook
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/makecookbook/README.old
%{_texmfdistdir}/doc/lualatex/makecookbook/README.txt
%{_texmfdistdir}/doc/lualatex/makecookbook/makecookbook-doc.pdf
%{_texmfdistdir}/doc/lualatex/makecookbook/makecookbook-doc.tex
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/cb-idxstyle.ist
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/cb-lettrine.cfl
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/cb-preamble.tex
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/img/image-a.jpg
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/img/image-b.jpg
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/makecookbook.pdf
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/makecookbook.tex
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/tex/cb-chapterA.tex
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/tex/cb-chapterB.tex
%{_texmfdistdir}/doc/lualatex/makecookbook/mycookbook/tex/cb-frontmatter.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makecookbook-%{texlive_version}.%{texlive_noarch}.0.0.85svn49311-%{release}-zypper
%endif

%package -n texlive-makedtx
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn46702
Release:        0
Summary:        Perl script to help generate dtx and ins files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-makedtx-bin >= %{texlive_version}
#!BuildIgnore: texlive-makedtx-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makedtx-doc >= %{texlive_version}
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Provides:       tex(createdtx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source147:      makedtx.tar.xz
Source148:      makedtx.doc.tar.xz

%description -n texlive-makedtx
The makedtx bundle is provided to help LaTeX2e developers to
write the code and documentation in separate files, and then
combine them into a single .dtx file for distribution. It
automatically generates the character table, and also writes
the associated installation (.ins) script.

%package -n texlive-makedtx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn46702
Release:        0
Summary:        Documentation for texlive-makedtx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makedtx-doc
This package includes the documentation for texlive-makedtx

%post -n texlive-makedtx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makedtx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makedtx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makedtx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/makedtx/CHANGES.org
%{_texmfdistdir}/doc/support/makedtx/README.txt
%{_texmfdistdir}/doc/support/makedtx/latexmkrc.pl
%{_texmfdistdir}/doc/support/makedtx/makedtx-version.tex
%{_texmfdistdir}/doc/support/makedtx/makedtx.pdf

%files -n texlive-makedtx
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/makedtx/makedtx.pl
%{_texmfdistdir}/tex/latex/makedtx/createdtx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makedtx-%{texlive_version}.%{texlive_noarch}.1.2svn46702-%{release}-zypper
%endif

%package -n texlive-makeglos
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Include a glossary into a document
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makeglos-doc >= %{texlive_version}
Provides:       tex(makeglos.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source149:      makeglos.tar.xz
Source150:      makeglos.doc.tar.xz

%description -n texlive-makeglos
The package provides the means to include a glossary into a
document. The glossary is prepared by an external program, such
as xindy or makeindex, in the same way that an index is made.

%package -n texlive-makeglos-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-makeglos
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makeglos-doc
This package includes the documentation for texlive-makeglos

%post -n texlive-makeglos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makeglos 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makeglos
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makeglos-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makeglos/README
%{_texmfdistdir}/doc/latex/makeglos/makeglos.pdf
%{_texmfdistdir}/doc/latex/makeglos/makeglos.tex
%{_texmfdistdir}/doc/latex/makeglos/makeglos.xdy

%files -n texlive-makeglos
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makeglos/makeglos.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makeglos-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-makeindex
Version:        %{texlive_version}.%{texlive_noarch}.svn52851
Release:        0
Summary:        Makeindex development sources
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-makeindex-bin >= %{texlive_version}
#!BuildIgnore: texlive-makeindex-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makeindex-doc >= %{texlive_version}
Provides:       tex(idxmac.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source151:      makeindex.tar.xz
Source152:      makeindex.doc.tar.xz

%description -n texlive-makeindex
The package contains the development sources of makeindex, as
derived from the texlive subversion repository.

%package -n texlive-makeindex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn52851
Release:        0
Summary:        Documentation for texlive-makeindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(makeindex.1)
Provides:       man(mkindex.1)

%description -n texlive-makeindex-doc
This package includes the documentation for texlive-makeindex

%post -n texlive-makeindex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makeindex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makeindex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makeindex-doc
%defattr(-,root,root,755)
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_texmfdistdir}/doc/support/makeindex/doc-src.zip
%{_texmfdistdir}/doc/support/makeindex/ind.pdf
%{_texmfdistdir}/doc/support/makeindex/makeindex.pdf

%files -n texlive-makeindex
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/base/din.ist
%{_texmfdistdir}/makeindex/base/icase.ist
%{_texmfdistdir}/makeindex/base/latex.ist
%{_texmfdistdir}/makeindex/base/math.ist
%{_texmfdistdir}/makeindex/base/mkind.ist
%{_texmfdistdir}/makeindex/base/puncts.ist
%{_texmfdistdir}/makeindex/base/tex.ist
%{_texmfdistdir}/tex/plain/makeindex/idxmac.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makeindex-%{texlive_version}.%{texlive_noarch}.svn52851-%{release}-zypper
%endif

%package -n texlive-makeplot
Version:        %{texlive_version}.%{texlive_noarch}.1.0.6svn15878
Release:        0
Summary:        Easy plots from Matlab in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makeplot-doc >= %{texlive_version}
Provides:       tex(makeplot.sty)
Requires:       tex(fp.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source153:      makeplot.tar.xz
Source154:      makeplot.doc.tar.xz

%description -n texlive-makeplot
Existing approaches to create EPS files from Matlab (laprint,
mma2ltx, print -eps, etc.) aren't satisfactory; makeplot aims
to resolve this problem. Makeplot is a LaTeX package that uses
the pstricks pst-plot functions to plot data that it takes from
Matlab output files.

%package -n texlive-makeplot-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.6svn15878
Release:        0
Summary:        Documentation for texlive-makeplot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makeplot-doc
This package includes the documentation for texlive-makeplot

%post -n texlive-makeplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makeplot 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makeplot
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makeplot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makeplot/README
%{_texmfdistdir}/doc/latex/makeplot/data1.mat
%{_texmfdistdir}/doc/latex/makeplot/data2.mat
%{_texmfdistdir}/doc/latex/makeplot/makeplot.pdf
%{_texmfdistdir}/doc/latex/makeplot/mptest.tex

%files -n texlive-makeplot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makeplot/makeplot.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makeplot-%{texlive_version}.%{texlive_noarch}.1.0.6svn15878-%{release}-zypper
%endif

%package -n texlive-maker
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn44823
Release:        0
Summary:        Include Arduino or Processing code in LaTeX documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-maker-doc >= %{texlive_version}
Provides:       tex(maker.sty)
Requires:       tex(listings.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source155:      maker.tar.xz
Source156:      maker.doc.tar.xz

%description -n texlive-maker
The first version of the package allows to include Arduino or
Processing code using three different forms: writing the code
directly in the LaTeX document writing Arduino or Processing
commands in line with the text calling to Arduino or Processing
files All these options support the syntax highlighting of the
oficial IDE.

%package -n texlive-maker-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn44823
Release:        0
Summary:        Documentation for texlive-maker
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-maker-doc
This package includes the documentation for texlive-maker

%post -n texlive-maker
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-maker 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-maker
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-maker-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/maker/README
%{_texmfdistdir}/doc/latex/maker/README.TEXLIVE

%files -n texlive-maker
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/maker/maker.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-maker-%{texlive_version}.%{texlive_noarch}.1.0svn44823-%{release}-zypper
%endif

%package -n texlive-makerobust
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn52811
Release:        0
Summary:        Making a macro robust (legacy package)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makerobust-doc >= %{texlive_version}
Provides:       tex(makerobust.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source157:      makerobust.tar.xz
Source158:      makerobust.doc.tar.xz

%description -n texlive-makerobust
Heiko Oberdiek's makerobust package defined a command with name
\MakeRobustCommand that could be used to make fragile commands
robust. The LaTeX format has, since 2015, included a command
\MakeRobust with the same syntax and behaviour. Also by 2019,
almost all commands in LaTeX that may be used in a moving
argument are already robust. This package is now just a simple
one-liner defining the name \MakeRobustCommand as an alias for
\MakeRobust. This package should not be used in any new
documents.

%package -n texlive-makerobust-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn52811
Release:        0
Summary:        Documentation for texlive-makerobust
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-makerobust-doc:en)

%description -n texlive-makerobust-doc
This package includes the documentation for texlive-makerobust

%post -n texlive-makerobust
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makerobust 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makerobust
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makerobust-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makerobust/README.md
%{_texmfdistdir}/doc/latex/makerobust/makerobust.pdf
%{_texmfdistdir}/doc/latex/makerobust/makerobust.tex

%files -n texlive-makerobust
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makerobust/makerobust.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makerobust-%{texlive_version}.%{texlive_noarch}.2.0svn52811-%{release}-zypper
%endif

%package -n texlive-makeshape
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn28973
Release:        0
Summary:        Declare new PGF shapes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-makeshape-doc >= %{texlive_version}
Provides:       tex(makeshape.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source159:      makeshape.tar.xz
Source160:      makeshape.doc.tar.xz

%description -n texlive-makeshape
The package simplifies production of custom shapes with correct
anchor borders, in PGF/TikZ; the only requirement is a PGF path
describing the anchor border. The package also provides macros
that help with the management of shape parameters, and the
definition of anchor points.

%package -n texlive-makeshape-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn28973
Release:        0
Summary:        Documentation for texlive-makeshape
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-makeshape-doc
This package includes the documentation for texlive-makeshape

%post -n texlive-makeshape
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-makeshape 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-makeshape
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-makeshape-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/makeshape/README
%{_texmfdistdir}/doc/latex/makeshape/makeshape.pdf
%{_texmfdistdir}/doc/latex/makeshape/ontesting.pdf
%{_texmfdistdir}/doc/latex/makeshape/sampleshape.tex
%{_texmfdistdir}/doc/latex/makeshape/testsample.pdf
%{_texmfdistdir}/doc/latex/makeshape/testsample.tex

%files -n texlive-makeshape
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/makeshape/makeshape.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-makeshape-%{texlive_version}.%{texlive_noarch}.2.1svn28973-%{release}-zypper
%endif

%package -n texlive-mandi
Version:        %{texlive_version}.%{texlive_noarch}.2.7.5svn49720
Release:        0
Summary:        Macros for introductory physics and astronomy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mandi-doc >= %{texlive_version}
Provides:       tex(mandi.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(calligra.sty)
Requires:       tex(cancel.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(epstopdf.sty)
Requires:       tex(esint.sty)
Requires:       tex(esvect.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(extarrows.sty)
Requires:       tex(filehook.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(stackengine.sty)
Requires:       tex(suffix.sty)
Requires:       tex(tensor.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xargs.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source161:      mandi.tar.xz
Source162:      mandi.doc.tar.xz

%description -n texlive-mandi
The package contains commands for students and teachers of
introductory physics. Commands for physical quantities
intelligently handle SI units so the user need not do so. There
are other features that should make LaTeX easy for introductory
physics students.

%package -n texlive-mandi-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.7.5svn49720
Release:        0
Summary:        Documentation for texlive-mandi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mandi-doc
This package includes the documentation for texlive-mandi

%post -n texlive-mandi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mandi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mandi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mandi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mandi/README
%{_texmfdistdir}/doc/latex/mandi/mandi.pdf
%{_texmfdistdir}/doc/latex/mandi/vdemo.py

%files -n texlive-mandi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mandi/mandi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mandi-%{texlive_version}.%{texlive_noarch}.2.7.5svn49720-%{release}-zypper
%endif

%package -n texlive-manfnt
Version:        %{texlive_version}.%{texlive_noarch}.svn54684
Release:        0
Summary:        LaTeX support for the TeX book symbols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-manfnt-doc >= %{texlive_version}
Provides:       tex(manfnt.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source163:      manfnt.tar.xz
Source164:      manfnt.doc.tar.xz

%description -n texlive-manfnt
A LaTeX package for easy access to the symbols of the Knuth's
'manual' font, such as the Dangerous Bend and Manual-errata
Arrow.

%package -n texlive-manfnt-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54684
Release:        0
Summary:        Documentation for texlive-manfnt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-manfnt-doc
This package includes the documentation for texlive-manfnt

%post -n texlive-manfnt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-manfnt 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-manfnt
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-manfnt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/manfnt/manfnt.pdf

%files -n texlive-manfnt
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/manfnt/manfnt.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-manfnt-%{texlive_version}.%{texlive_noarch}.svn54684-%{release}-zypper
%endif

%package -n texlive-manfnt-font
Version:        %{texlive_version}.%{texlive_noarch}.svn45777
Release:        0
Summary:        Knuth's "manual" fonts
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-manfnt-font-fonts >= %{texlive_version}
Provides:       tex(manfnt.map)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source165:      manfnt-font.tar.xz

%description -n texlive-manfnt-font
Metafont (by Donald Knuth) and Adobe Type 1 (by Taco Hoekwater)
versions of the font containing the odd symbols Knuth uses in
his books. LaTeX support is available using the manfnt package

%package -n texlive-manfnt-font-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn45777
Release:        0
Summary:        Severed fonts for texlive-manfnt-font
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-manfnt-font-fonts
The  separated fonts package for texlive-manfnt-font
%post -n texlive-manfnt-font
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap manfnt.map' >> /var/run/texlive/run-updmap

%postun -n texlive-manfnt-font 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap manfnt.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-manfnt-font
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-manfnt-font-fonts
%files -n texlive-manfnt-font
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/hoekwater/manfnt-font/manfnt.afm
%{_texmfdistdir}/fonts/map/dvips/manfnt-font/manfnt.map
%verify(link) %{_texmfdistdir}/fonts/type1/hoekwater/manfnt-font/manfnt.pfb
%{_texmfdistdir}/fonts/type1/hoekwater/manfnt-font/manfnt.pfm

%files -n texlive-manfnt-font-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-manfnt-font
%{_datadir}/fontconfig/conf.avail/58-texlive-manfnt-font.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-manfnt-font/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-manfnt-font/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-manfnt-font/fonts.scale
%{_datadir}/fonts/texlive-manfnt-font/manfnt.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-manfnt-font-fonts-%{texlive_version}.%{texlive_noarch}.svn45777-%{release}-zypper
%endif

%package -n texlive-manuscript
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn36110
Release:        0
Summary:        Emulate look of a document typed on a typewriter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-manuscript-doc >= %{texlive_version}
Provides:       tex(manuscript.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fullpage.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(setspace.sty)
Requires:       tex(soul.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source166:      manuscript.tar.xz
Source167:      manuscript.doc.tar.xz

%description -n texlive-manuscript
This package is designed for those who have to submit
dissertations, etc., to institutions that still maintain the
typewriter is the summit of non-professional printing.

%package -n texlive-manuscript-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn36110
Release:        0
Summary:        Documentation for texlive-manuscript
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-manuscript-doc
This package includes the documentation for texlive-manuscript

%post -n texlive-manuscript
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-manuscript 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-manuscript
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-manuscript-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/manuscript/Makefile
%{_texmfdistdir}/doc/latex/manuscript/README
%{_texmfdistdir}/doc/latex/manuscript/manuscript.pdf

%files -n texlive-manuscript
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/manuscript/manuscript.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-manuscript-%{texlive_version}.%{texlive_noarch}.1.7svn36110-%{release}-zypper
%endif

%package -n texlive-manyind
Version:        %{texlive_version}.%{texlive_noarch}.svn49874
Release:        0
Summary:        Provides support for many indexes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-manyind-doc >= %{texlive_version}
Provides:       tex(manyind.sty)
Requires:       tex(makeidx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source168:      manyind.tar.xz
Source169:      manyind.doc.tar.xz

%description -n texlive-manyind
This package provides support for many indexes, leaving all the
bookkeeping to LaTeX and makeindex. No extra programs or files
are needed. One runs latex and makeindex as if there is just
one index. In the main file one puts commands like
\setindex{main} to steer the flow. Some features of makeindex
may no longer work.

%package -n texlive-manyind-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn49874
Release:        0
Summary:        Documentation for texlive-manyind
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-manyind-doc
This package includes the documentation for texlive-manyind

%post -n texlive-manyind
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-manyind 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-manyind
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-manyind-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/manyind/README.md
%{_texmfdistdir}/doc/latex/manyind/mind.html
%{_texmfdistdir}/doc/latex/manyind/mindsample.pdf
%{_texmfdistdir}/doc/latex/manyind/mindsample.tex

%files -n texlive-manyind
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/manyind/manyind.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-manyind-%{texlive_version}.%{texlive_noarch}.svn49874-%{release}-zypper
%endif

%package -n texlive-marcellus
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Marcellus fonts with LaTeX support
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-marcellus-fonts >= %{texlive_version}
Recommends:     texlive-marcellus-doc >= %{texlive_version}
Provides:       tex(LY1Marcellus-LF.fd)
Provides:       tex(LY1Marcellus-Sup.fd)
Provides:       tex(Marcellus-Regular-lf-ly1--base.tfm)
Provides:       tex(Marcellus-Regular-lf-ly1.tfm)
Provides:       tex(Marcellus-Regular-lf-ly1.vf)
Provides:       tex(Marcellus-Regular-lf-ot1.tfm)
Provides:       tex(Marcellus-Regular-lf-t1--base.tfm)
Provides:       tex(Marcellus-Regular-lf-t1.tfm)
Provides:       tex(Marcellus-Regular-lf-t1.vf)
Provides:       tex(Marcellus-Regular-lf-ts1--base.tfm)
Provides:       tex(Marcellus-Regular-lf-ts1.tfm)
Provides:       tex(Marcellus-Regular-lf-ts1.vf)
Provides:       tex(Marcellus-Regular-sup-ly1--base.tfm)
Provides:       tex(Marcellus-Regular-sup-ly1.tfm)
Provides:       tex(Marcellus-Regular-sup-ly1.vf)
Provides:       tex(Marcellus-Regular-sup-ot1.tfm)
Provides:       tex(Marcellus-Regular-sup-t1--base.tfm)
Provides:       tex(Marcellus-Regular-sup-t1.tfm)
Provides:       tex(Marcellus-Regular-sup-t1.vf)
Provides:       tex(MarcellusSmallCaps-lf-sc-ly1--base.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-ly1.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-ly1.vf)
Provides:       tex(MarcellusSmallCaps-lf-sc-ot1--base.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-ot1.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-ot1.vf)
Provides:       tex(MarcellusSmallCaps-lf-sc-t1--base.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-t1.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-t1.vf)
Provides:       tex(MarcellusSmallCaps-lf-sc-ts1--base.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-ts1.tfm)
Provides:       tex(MarcellusSmallCaps-lf-sc-ts1.vf)
Provides:       tex(MarcellusSmallCaps-sup-sc-ly1--base.tfm)
Provides:       tex(MarcellusSmallCaps-sup-sc-ly1.tfm)
Provides:       tex(MarcellusSmallCaps-sup-sc-ly1.vf)
Provides:       tex(MarcellusSmallCaps-sup-sc-ot1--base.tfm)
Provides:       tex(MarcellusSmallCaps-sup-sc-ot1.tfm)
Provides:       tex(MarcellusSmallCaps-sup-sc-ot1.vf)
Provides:       tex(MarcellusSmallCaps-sup-sc-t1--base.tfm)
Provides:       tex(MarcellusSmallCaps-sup-sc-t1.tfm)
Provides:       tex(MarcellusSmallCaps-sup-sc-t1.vf)
Provides:       tex(OT1Marcellus-LF.fd)
Provides:       tex(OT1Marcellus-Sup.fd)
Provides:       tex(T1Marcellus-LF.fd)
Provides:       tex(T1Marcellus-Sup.fd)
Provides:       tex(TS1Marcellus-LF.fd)
Provides:       tex(marcellus.map)
Provides:       tex(marcellus.sty)
Provides:       tex(mrcl_4cvize.enc)
Provides:       tex(mrcl_5ago63.enc)
Provides:       tex(mrcl_5az7w7.enc)
Provides:       tex(mrcl_cvodtw.enc)
Provides:       tex(mrcl_dfyae6.enc)
Provides:       tex(mrcl_hxcgcn.enc)
Provides:       tex(mrcl_l63c5y.enc)
Provides:       tex(mrcl_lo2l42.enc)
Provides:       tex(mrcl_mqz6jr.enc)
Provides:       tex(mrcl_oyecj6.enc)
Provides:       tex(mrcl_pp6sje.enc)
Provides:       tex(mrcl_rfafok.enc)
Provides:       tex(mrcl_rwr7kk.enc)
Provides:       tex(mrcl_tzgqbn.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source170:      marcellus.tar.xz
Source171:      marcellus.doc.tar.xz

%description -n texlive-marcellus
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Marcellus family of fonts, designed by Brian J.
Bonislawsky. Marcellus is a flared-serif family, inspired by
classic Roman inscription letterforms. There is currently just
a regular weight and small-caps. The regular weight will be
silently substituted for bold.

%package -n texlive-marcellus-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Documentation for texlive-marcellus
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-marcellus-doc
This package includes the documentation for texlive-marcellus


%package -n texlive-marcellus-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Severed fonts for texlive-marcellus
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-marcellus-fonts
The  separated fonts package for texlive-marcellus
%post -n texlive-marcellus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap marcellus.map' >> /var/run/texlive/run-updmap

%postun -n texlive-marcellus 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap marcellus.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-marcellus
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-marcellus-fonts
%files -n texlive-marcellus-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/marcellus/OFL.txt
%{_texmfdistdir}/doc/fonts/marcellus/README
%{_texmfdistdir}/doc/fonts/marcellus/marcellus-samples.pdf
%{_texmfdistdir}/doc/fonts/marcellus/marcellus-samples.tex

%files -n texlive-marcellus
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_4cvize.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_5ago63.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_5az7w7.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_cvodtw.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_dfyae6.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_hxcgcn.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_l63c5y.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_lo2l42.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_mqz6jr.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_oyecj6.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_pp6sje.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_rfafok.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_rwr7kk.enc
%{_texmfdistdir}/fonts/enc/dvips/marcellus/mrcl_tzgqbn.enc
%{_texmfdistdir}/fonts/map/dvips/marcellus/marcellus.map
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/Marcellus-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-lf-sc-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-sup-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-sup-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-sup-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-sup-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-sup-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/marcellus/MarcellusSmallCaps-sup-sc-t1.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/marcellus/Marcellus-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/marcellus/MarcellusSmallCaps.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/marcellus/Marcellus-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/marcellus/MarcellusSmallCaps.pfb
%{_texmfdistdir}/fonts/vf/public/marcellus/Marcellus-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/Marcellus-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/Marcellus-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/Marcellus-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/Marcellus-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/MarcellusSmallCaps-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/MarcellusSmallCaps-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/MarcellusSmallCaps-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/MarcellusSmallCaps-lf-sc-ts1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/MarcellusSmallCaps-sup-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/MarcellusSmallCaps-sup-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/marcellus/MarcellusSmallCaps-sup-sc-t1.vf
%{_texmfdistdir}/tex/latex/marcellus/LY1Marcellus-LF.fd
%{_texmfdistdir}/tex/latex/marcellus/LY1Marcellus-Sup.fd
%{_texmfdistdir}/tex/latex/marcellus/OT1Marcellus-LF.fd
%{_texmfdistdir}/tex/latex/marcellus/OT1Marcellus-Sup.fd
%{_texmfdistdir}/tex/latex/marcellus/T1Marcellus-LF.fd
%{_texmfdistdir}/tex/latex/marcellus/T1Marcellus-Sup.fd
%{_texmfdistdir}/tex/latex/marcellus/TS1Marcellus-LF.fd
%{_texmfdistdir}/tex/latex/marcellus/marcellus.sty

%files -n texlive-marcellus-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-marcellus
%{_datadir}/fontconfig/conf.avail/58-texlive-marcellus.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-marcellus.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-marcellus.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-marcellus/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-marcellus/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-marcellus/fonts.scale
%{_datadir}/fonts/texlive-marcellus/Marcellus-Regular.ttf
%{_datadir}/fonts/texlive-marcellus/MarcellusSmallCaps.ttf
%{_datadir}/fonts/texlive-marcellus/Marcellus-Regular.pfb
%{_datadir}/fonts/texlive-marcellus/MarcellusSmallCaps.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-marcellus-fonts-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif

%package -n texlive-margbib
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn15878
Release:        0
Summary:        Display bibitem tags in the margins
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-margbib-doc >= %{texlive_version}
Provides:       tex(margbib.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source172:      margbib.tar.xz
Source173:      margbib.doc.tar.xz

%description -n texlive-margbib
The package redefines the 'thebibliography' environment to
place the citation key into the margin.

%package -n texlive-margbib-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn15878
Release:        0
Summary:        Documentation for texlive-margbib
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-margbib-doc
This package includes the documentation for texlive-margbib

%post -n texlive-margbib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-margbib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-margbib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-margbib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/margbib/margbib.pdf

%files -n texlive-margbib
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/margbib/margbib.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-margbib-%{texlive_version}.%{texlive_noarch}.1.0csvn15878-%{release}-zypper
%endif

%package -n texlive-marginfit
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48281
Release:        0
Summary:        Improved margin notes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-marginfit-doc >= %{texlive_version}
Provides:       tex(marginfit.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source174:      marginfit.tar.xz
Source175:      marginfit.doc.tar.xz

%description -n texlive-marginfit
This package fixes various bugs with the margin paragraph
implementation of LaTeX. Those bugs include margin notes that
are attached to the wrong side as well as those that stick out
of the bottom of the page. This package provides a drop-in
replacement solution.

%package -n texlive-marginfit-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48281
Release:        0
Summary:        Documentation for texlive-marginfit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-marginfit-doc
This package includes the documentation for texlive-marginfit

%post -n texlive-marginfit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-marginfit 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-marginfit
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-marginfit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/marginfit/Makefile
%{_texmfdistdir}/doc/latex/marginfit/README
%{_texmfdistdir}/doc/latex/marginfit/marginfit.pdf

%files -n texlive-marginfit
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/marginfit/marginfit.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-marginfit-%{texlive_version}.%{texlive_noarch}.1.1svn48281-%{release}-zypper
%endif

%package -n texlive-marginfix
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn31598
Release:        0
Summary:        Patch \marginpar to avoid overfull margins
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-marginfix-doc >= %{texlive_version}
Provides:       tex(marginfix.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source176:      marginfix.tar.xz
Source177:      marginfix.doc.tar.xz

%description -n texlive-marginfix
Authors using LaTeX to typeset books with significant margin
material often run into the problem of long notes running off
the bottom of the page. A typical workaround is to insert
\vshift commands by hand, but this is a tedious process that is
invalidated when pagination changes. Another workaround is
memoir's \sidebar function, but this can be unsatisfying for
short textual notes, and standard marginpars cannot be mixed
with sidebars. This package implements a solution to make
marginpars "just work" by keeping a list of floating inserts
and arranging them intelligently in the output routine.

%package -n texlive-marginfix-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn31598
Release:        0
Summary:        Documentation for texlive-marginfix
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-marginfix-doc
This package includes the documentation for texlive-marginfix

%post -n texlive-marginfix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-marginfix 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-marginfix
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-marginfix-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/marginfix/README
%{_texmfdistdir}/doc/latex/marginfix/marginfix.pdf

%files -n texlive-marginfix
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/marginfix/marginfix.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-marginfix-%{texlive_version}.%{texlive_noarch}.1.1svn31598-%{release}-zypper
%endif

%package -n texlive-marginnote
Version:        %{texlive_version}.%{texlive_noarch}.1.4bsvn48383
Release:        0
Summary:        Notes in the margin, even where \marginpar fails
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-marginnote-doc >= %{texlive_version}
Provides:       tex(marginnote.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source178:      marginnote.tar.xz
Source179:      marginnote.doc.tar.xz

%description -n texlive-marginnote
This package provides the command \marginnote that may be used
instead of \marginpar at almost every place where \marginpar
cannot be used, e.g., inside floats, footnotes, or in frames
made with the framed package.

%package -n texlive-marginnote-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4bsvn48383
Release:        0
Summary:        Documentation for texlive-marginnote
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-marginnote-doc
This package includes the documentation for texlive-marginnote

%post -n texlive-marginnote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-marginnote 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-marginnote
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-marginnote-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/marginnote/README.txt
%{_texmfdistdir}/doc/latex/marginnote/marginnote.pdf

%files -n texlive-marginnote
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/marginnote/marginnote.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-marginnote-%{texlive_version}.%{texlive_noarch}.1.4bsvn48383-%{release}-zypper
%endif

%package -n texlive-markdown
Version:        %{texlive_version}.%{texlive_noarch}.2.8.2svn54482
Release:        0
Summary:        A package for converting and rendering markdown documents inside TeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-markdown-doc >= %{texlive_version}
Provides:       tex(markdown.sty)
Provides:       tex(markdown.tex)
Provides:       tex(t-markdown.tex)
Requires:       tex(csvsimple.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(gobble.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(paralist.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source180:      markdown.tar.xz
Source181:      markdown.doc.tar.xz

%description -n texlive-markdown
The package provides facilities for the conversion of markdown
markup to plain TeX. These are provided both in form of a Lua
module and in form of plain TeX, LaTeX, and ConTeXt macro
packages that enable the direct inclusion of markdown documents
inside TeX documents. Architecturally, the package consists of
the Lunamark Lua module by John MacFarlane, which was slimmed
down and rewritten for the needs of the package. Lunamark
provides speedy markdown parsing for the rest of the package.
On top of Lunamark sits code for the plain TeX, LaTeX, and
ConTeXt formats by Vit Novotny.

%package -n texlive-markdown-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.8.2svn54482
Release:        0
Summary:        Documentation for texlive-markdown
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-markdown-doc
This package includes the documentation for texlive-markdown

%post -n texlive-markdown
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-markdown 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-markdown
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-markdown-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/context/third/markdown/examples/context.tex
%{_texmfdistdir}/doc/context/third/markdown/examples/example.md
%{_texmfdistdir}/doc/context/third/markdown/examples/scientists.csv
%{_texmfdistdir}/doc/generic/markdown/README.md
%{_texmfdistdir}/doc/generic/markdown/markdown.css
%{_texmfdistdir}/doc/generic/markdown/markdown.html
%{_texmfdistdir}/doc/generic/markdown/markdown.md
%{_texmfdistdir}/doc/generic/markdown/markdown.pdf
%{_texmfdistdir}/doc/latex/markdown/examples/example.md
%{_texmfdistdir}/doc/latex/markdown/examples/latex.tex
%{_texmfdistdir}/doc/latex/markdown/examples/scientists.csv

%files -n texlive-markdown
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/markdown/markdown-cli.lua
%{_texmfdistdir}/tex/context/third/markdown/t-markdown.tex
%{_texmfdistdir}/tex/generic/markdown/markdown.tex
%{_texmfdistdir}/tex/latex/markdown/markdown.sty
%{_texmfdistdir}/tex/luatex/markdown/markdown.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-markdown-%{texlive_version}.%{texlive_noarch}.2.8.2svn54482-%{release}-zypper
%endif

%package -n texlive-marvosym
Version:        %{texlive_version}.%{texlive_noarch}.2.2asvn29349
Release:        0
Summary:        Martin Vogel's Symbols (marvosym) font
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-marvosym-fonts >= %{texlive_version}
Recommends:     texlive-marvosym-doc >= %{texlive_version}
Provides:       tex(marvosym.map)
Provides:       tex(marvosym.sty)
Provides:       tex(umvs.fd)
Provides:       tex(umvs.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source182:      marvosym.tar.xz
Source183:      marvosym.doc.tar.xz

%description -n texlive-marvosym
Martin Vogel's Symbol font (marvosym) contains the Euro
currency symbol as defined by the European commission, along
with symbols for structural engineering; symbols for steel
cross-sections; astronomy signs (sun, moon, planets); the 12
signs of the zodiac; scissor symbols; CE sign and others. The
package contains both the original TrueType font and the
derived Type 1 font, together with support files for TeX
(LaTeX).

%package -n texlive-marvosym-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2asvn29349
Release:        0
Summary:        Documentation for texlive-marvosym
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-marvosym-doc
This package includes the documentation for texlive-marvosym


%package -n texlive-marvosym-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.2asvn29349
Release:        0
Summary:        Severed fonts for texlive-marvosym
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-marvosym-fonts
The  separated fonts package for texlive-marvosym
%post -n texlive-marvosym
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap marvosym.map' >> /var/run/texlive/run-updmap

%postun -n texlive-marvosym 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap marvosym.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-marvosym
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-marvosym-fonts
%files -n texlive-marvosym-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/marvosym/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/marvosym/Makefile
%{_texmfdistdir}/doc/fonts/marvosym/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/marvosym/OFL.txt
%{_texmfdistdir}/doc/fonts/marvosym/README
%{_texmfdistdir}/doc/fonts/marvosym/marvodoc.pdf
%{_texmfdistdir}/doc/fonts/marvosym/marvodoc.tex
%{_texmfdistdir}/doc/fonts/marvosym/marvosym-doc.pdf
%{_texmfdistdir}/doc/fonts/marvosym/marvosym-doc.tex

%files -n texlive-marvosym
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/marvosym/marvosym.afm
%{_texmfdistdir}/fonts/map/dvips/marvosym/marvosym.map
%{_texmfdistdir}/fonts/tfm/public/marvosym/umvs.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/marvosym/marvosym.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/marvosym/marvosym.pfb
%{_texmfdistdir}/tex/latex/marvosym/marvosym.sty
%{_texmfdistdir}/tex/latex/marvosym/umvs.fd

%files -n texlive-marvosym-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-marvosym
%{_datadir}/fontconfig/conf.avail/58-texlive-marvosym.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-marvosym.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-marvosym.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-marvosym/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-marvosym/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-marvosym/fonts.scale
%{_datadir}/fonts/texlive-marvosym/marvosym.ttf
%{_datadir}/fonts/texlive-marvosym/marvosym.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-marvosym-fonts-%{texlive_version}.%{texlive_noarch}.2.2asvn29349-%{release}-zypper
%endif

%package -n texlive-matc3
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn29845
Release:        0
Summary:        Commands for MatematicaC3 textbooks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-matc3-doc >= %{texlive_version}
Provides:       tex(matc3.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source184:      matc3.tar.xz
Source185:      matc3.doc.tar.xz

%description -n texlive-matc3
The package provides support for the Matematica C3 project to
produce free mathematical text books for use in Italian high
schools.

%package -n texlive-matc3-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn29845
Release:        0
Summary:        Documentation for texlive-matc3
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-matc3-doc:it)

%description -n texlive-matc3-doc
This package includes the documentation for texlive-matc3

%post -n texlive-matc3
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-matc3 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-matc3
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-matc3-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/matc3/Makefile
%{_texmfdistdir}/doc/latex/matc3/README
%{_texmfdistdir}/doc/latex/matc3/matc3.pdf

%files -n texlive-matc3
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/matc3/matc3.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-matc3-%{texlive_version}.%{texlive_noarch}.1.0.1svn29845-%{release}-zypper
%endif

%package -n texlive-matc3mem
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn35773
Release:        0
Summary:        Class for MatematicaC3 textbooks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-matc3mem-doc >= %{texlive_version}
Provides:       tex(matc3mem.cls)
Requires:       tex(amsthm.sty)
Requires:       tex(shadethm.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source186:      matc3mem.tar.xz
Source187:      matc3mem.doc.tar.xz

%description -n texlive-matc3mem
The class is a development of memoir, with additions
(specifically, mathematical extensions) that provide support
for writing the books for the Matematica C3 project to produce
free mathematical textbooks for use in Italian high schools.

%package -n texlive-matc3mem-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn35773
Release:        0
Summary:        Documentation for texlive-matc3mem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-matc3mem-doc:it)

%description -n texlive-matc3mem-doc
This package includes the documentation for texlive-matc3mem

%post -n texlive-matc3mem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-matc3mem 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-matc3mem
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-matc3mem-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/matc3mem/Makefile
%{_texmfdistdir}/doc/latex/matc3mem/README
%{_texmfdistdir}/doc/latex/matc3mem/matc3mem.pdf

%files -n texlive-matc3mem
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/matc3mem/matc3mem.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-matc3mem-%{texlive_version}.%{texlive_noarch}.1.1svn35773-%{release}-zypper
%endif

%package -n texlive-match_parens
Version:        %{texlive_version}.%{texlive_noarch}.1.43svn36270
Release:        0
Summary:        Find mismatches of parentheses, braces, (angle) brackets, in texts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-match_parens-bin >= %{texlive_version}
#!BuildIgnore: texlive-match_parens-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-match_parens-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source188:      match_parens.tar.xz
Source189:      match_parens.doc.tar.xz

%description -n texlive-match_parens
Mismatches of parentheses, braces, (angle) brackets, especially
in TeX sources which may be rich in those, may be difficult to
trace. This little Ruby script helps you by writing your text
to standard output, after adding a left margin to your text,
which will normally be almost empty, but will clearly show any
mismatches.

%package -n texlive-match_parens-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.43svn36270
Release:        0
Summary:        Documentation for texlive-match_parens
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-match_parens-doc
This package includes the documentation for texlive-match_parens

%post -n texlive-match_parens
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-match_parens 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-match_parens
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-match_parens-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/match_parens/README
%{_texmfdistdir}/doc/support/match_parens/match_parens.pdf

%files -n texlive-match_parens
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/match_parens/match_parens
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-match_parens-%{texlive_version}.%{texlive_noarch}.1.43svn36270-%{release}-zypper
%endif

%package -n texlive-math-e
Version:        %{texlive_version}.%{texlive_noarch}.svn20062
Release:        0
Summary:        Examples from the book Typesetting Mathematics with LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source190:      math-e.doc.tar.xz

%description -n texlive-math-e
The bundle contains all the examples from the (English) book
"Typesetting Mathematics with LaTeX" (UIT Press, Cambridge,
2010). The examples are stand alone documents and may be
separately processed with LaTeX or pdfLaTeX.
%post -n texlive-math-e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-math-e 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-math-e
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-math-e
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/math-e/01-00-1.ltx
%{_texmfdistdir}/doc/latex/math-e/01-00-2.ltx
%{_texmfdistdir}/doc/latex/math-e/01-00-3.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-10.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-11.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-12.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-3.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-4.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-5.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-6.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-7.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-8.ltx
%{_texmfdistdir}/doc/latex/math-e/02-02-9.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-10.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-11.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-3.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-4.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-5.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-6.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-7.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-8.ltx
%{_texmfdistdir}/doc/latex/math-e/03-02-9.ltx
%{_texmfdistdir}/doc/latex/math-e/03-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/03-04-1.ltx
%{_texmfdistdir}/doc/latex/math-e/03-04-2.ltx
%{_texmfdistdir}/doc/latex/math-e/03-04-5.ltx
%{_texmfdistdir}/doc/latex/math-e/03-04-6.ltx
%{_texmfdistdir}/doc/latex/math-e/03-05-1.ltx
%{_texmfdistdir}/doc/latex/math-e/03-05-2.ltx
%{_texmfdistdir}/doc/latex/math-e/03-05-3.ltx
%{_texmfdistdir}/doc/latex/math-e/03-06-1.ltx
%{_texmfdistdir}/doc/latex/math-e/03-06-2.ltx
%{_texmfdistdir}/doc/latex/math-e/03-06-3.ltx
%{_texmfdistdir}/doc/latex/math-e/03-06-4.ltx
%{_texmfdistdir}/doc/latex/math-e/03-07-1.ltx
%{_texmfdistdir}/doc/latex/math-e/03-07-2.ltx
%{_texmfdistdir}/doc/latex/math-e/03-07-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-01-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-01-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-01-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-01-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-01-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-01-6.ltx
%{_texmfdistdir}/doc/latex/math-e/04-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-03-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-03-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-03-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-03-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-04-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-04-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-04-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-04-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-10.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-11.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-12.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-13.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-14.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-15.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-16.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-17.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-18.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-19.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-20.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-21.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-22.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-6.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-7.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-8.ltx
%{_texmfdistdir}/doc/latex/math-e/04-05-9.ltx
%{_texmfdistdir}/doc/latex/math-e/04-06-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-06-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-07-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-07-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-10.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-11.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-6.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-7.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-8.ltx
%{_texmfdistdir}/doc/latex/math-e/04-08-9.ltx
%{_texmfdistdir}/doc/latex/math-e/04-09-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-09-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-09-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-09-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-09-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-10-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-10-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-11-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-11-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-11-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-11-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-11-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-11-6.ltx
%{_texmfdistdir}/doc/latex/math-e/04-12-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-13-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-13-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-16-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-17-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-10.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-11.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-6.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-7.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-8.ltx
%{_texmfdistdir}/doc/latex/math-e/04-18-9.ltx
%{_texmfdistdir}/doc/latex/math-e/04-20-1.ltx
%{_texmfdistdir}/doc/latex/math-e/04-20-2.ltx
%{_texmfdistdir}/doc/latex/math-e/04-20-3.ltx
%{_texmfdistdir}/doc/latex/math-e/04-20-4.ltx
%{_texmfdistdir}/doc/latex/math-e/04-20-5.ltx
%{_texmfdistdir}/doc/latex/math-e/04-20-6.ltx
%{_texmfdistdir}/doc/latex/math-e/04-20-7.ltx
%{_texmfdistdir}/doc/latex/math-e/05-00-1.ltx
%{_texmfdistdir}/doc/latex/math-e/05-01-1.ltx
%{_texmfdistdir}/doc/latex/math-e/05-01-2.ltx
%{_texmfdistdir}/doc/latex/math-e/05-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/05-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/05-03-2.ltx
%{_texmfdistdir}/doc/latex/math-e/05-03-3.ltx
%{_texmfdistdir}/doc/latex/math-e/05-03-4.ltx
%{_texmfdistdir}/doc/latex/math-e/05-03-5.ltx
%{_texmfdistdir}/doc/latex/math-e/05-04-1.ltx
%{_texmfdistdir}/doc/latex/math-e/05-04-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-10.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-11.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-12.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-13.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-14.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-15.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-16.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-17.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-18.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-19.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-20.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-21.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-4.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-5.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-6.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-7.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-8.ltx
%{_texmfdistdir}/doc/latex/math-e/06-02-9.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-10.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-11.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-12.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-13.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-14.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-15.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-16.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-17.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-18.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-19.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-20.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-21.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-22.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-4.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-5.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-6.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-7.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-8.ltx
%{_texmfdistdir}/doc/latex/math-e/06-03-9.ltx
%{_texmfdistdir}/doc/latex/math-e/06-06-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-06-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-07-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-07-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-07-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-07-4.ltx
%{_texmfdistdir}/doc/latex/math-e/06-07-5.ltx
%{_texmfdistdir}/doc/latex/math-e/06-08-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-08-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-09-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-09-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-10-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-4.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-5.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-6.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-7.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-8.ltx
%{_texmfdistdir}/doc/latex/math-e/06-11-9.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-10.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-11.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-12.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-13.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-14.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-15.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-4.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-5.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-6.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-7.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-8.ltx
%{_texmfdistdir}/doc/latex/math-e/06-12-9.ltx
%{_texmfdistdir}/doc/latex/math-e/06-13-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-13-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-13-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-14-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-14-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-14-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-15-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-15-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-15-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-16-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-16-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-17-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-18-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-19-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-19-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-19-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-19-4.ltx
%{_texmfdistdir}/doc/latex/math-e/06-20-1.ltx
%{_texmfdistdir}/doc/latex/math-e/06-20-2.ltx
%{_texmfdistdir}/doc/latex/math-e/06-20-3.ltx
%{_texmfdistdir}/doc/latex/math-e/06-20-4.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-10.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-11.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-12.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-4.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-5.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-6.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-7.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-8.ltx
%{_texmfdistdir}/doc/latex/math-e/07-01-9.ltx
%{_texmfdistdir}/doc/latex/math-e/07-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-02-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-02-4.ltx
%{_texmfdistdir}/doc/latex/math-e/07-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-03-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-04-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-10.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-11.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-12.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-13.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-14.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-4.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-5.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-6.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-7.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-8.ltx
%{_texmfdistdir}/doc/latex/math-e/07-05-9.ltx
%{_texmfdistdir}/doc/latex/math-e/07-06-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-06-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-06-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-06-4.ltx
%{_texmfdistdir}/doc/latex/math-e/07-06-5.ltx
%{_texmfdistdir}/doc/latex/math-e/07-06-6.ltx
%{_texmfdistdir}/doc/latex/math-e/07-07-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-08-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-08-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-08-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-09-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-09-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-10-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-10-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-10-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-10-4.ltx
%{_texmfdistdir}/doc/latex/math-e/07-11-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-12-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-12-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-12-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-13-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-10.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-3.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-4.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-5.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-6.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-7.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-8.ltx
%{_texmfdistdir}/doc/latex/math-e/07-14-9.ltx
%{_texmfdistdir}/doc/latex/math-e/07-15-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-15-2.ltx
%{_texmfdistdir}/doc/latex/math-e/07-16-1.ltx
%{_texmfdistdir}/doc/latex/math-e/07-16-2.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-1.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-10.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-11.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-12.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-13.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-14.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-15.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-16.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-2.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-3.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-4.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-5.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-6.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-7.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-8.ltx
%{_texmfdistdir}/doc/latex/math-e/08-01-9.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-10.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-11.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-12.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-13.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-14.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-15.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-3.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-4.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-5.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-6.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-7.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-8.ltx
%{_texmfdistdir}/doc/latex/math-e/08-02-9.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-10.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-11.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-12.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-2.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-3.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-4.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-5.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-6.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-7.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-8.ltx
%{_texmfdistdir}/doc/latex/math-e/08-03-9.ltx
%{_texmfdistdir}/doc/latex/math-e/09-01-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-03-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-04-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-05-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-05-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-06-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-06-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-07-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-07-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-07-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-07-4.ltx
%{_texmfdistdir}/doc/latex/math-e/09-08-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-08-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-08-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-09-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-09-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-10-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-10-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-11-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-11-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-11-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-12-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-12-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-12-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-12-4.ltx
%{_texmfdistdir}/doc/latex/math-e/09-12-5.ltx
%{_texmfdistdir}/doc/latex/math-e/09-12-6.ltx
%{_texmfdistdir}/doc/latex/math-e/09-12-7.ltxps
%{_texmfdistdir}/doc/latex/math-e/09-13-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-13-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-14-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-15-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-15-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-15-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-4.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-5.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-6.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-7.ltx
%{_texmfdistdir}/doc/latex/math-e/09-16-8.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-10.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-11.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-12.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-13.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-14.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-4.ltx4
%{_texmfdistdir}/doc/latex/math-e/09-17-5.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-6.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-7.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-8.ltx
%{_texmfdistdir}/doc/latex/math-e/09-17-9.ltx
%{_texmfdistdir}/doc/latex/math-e/09-18-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-18-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-18-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-19-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-19-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-20-1.ltx
%{_texmfdistdir}/doc/latex/math-e/09-20-2.ltx
%{_texmfdistdir}/doc/latex/math-e/09-20-3.ltx
%{_texmfdistdir}/doc/latex/math-e/09-20-4.ltx
%{_texmfdistdir}/doc/latex/math-e/09-20-5.ltx
%{_texmfdistdir}/doc/latex/math-e/10-01-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-01-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-01-3.ltx
%{_texmfdistdir}/doc/latex/math-e/10-01-4.ltxps
%{_texmfdistdir}/doc/latex/math-e/10-01-5.ltxps
%{_texmfdistdir}/doc/latex/math-e/10-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-03-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-03-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-03-3.ltx
%{_texmfdistdir}/doc/latex/math-e/10-03-4.ltx
%{_texmfdistdir}/doc/latex/math-e/10-03-5.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-3.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-4.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-5.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-6.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-7.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-8.ltx
%{_texmfdistdir}/doc/latex/math-e/10-04-9.ltx
%{_texmfdistdir}/doc/latex/math-e/10-05-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-05-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-06-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-06-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-06-3.ltx
%{_texmfdistdir}/doc/latex/math-e/10-06-4.ltx
%{_texmfdistdir}/doc/latex/math-e/10-07-1.ltx2
%{_texmfdistdir}/doc/latex/math-e/10-07-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-07-3.ltx
%{_texmfdistdir}/doc/latex/math-e/10-07-4.ltx
%{_texmfdistdir}/doc/latex/math-e/10-07-5.ltx
%{_texmfdistdir}/doc/latex/math-e/10-07-6.ltx
%{_texmfdistdir}/doc/latex/math-e/10-07-7.ltx
%{_texmfdistdir}/doc/latex/math-e/10-08-1.ltxps
%{_texmfdistdir}/doc/latex/math-e/10-09-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-10.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-11.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-12.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-13.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-3.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-4.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-5.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-6.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-7.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-8.ltx
%{_texmfdistdir}/doc/latex/math-e/10-09-9.ltx
%{_texmfdistdir}/doc/latex/math-e/10-10-1.ltx
%{_texmfdistdir}/doc/latex/math-e/10-10-2.ltx
%{_texmfdistdir}/doc/latex/math-e/10-10-3.ltx
%{_texmfdistdir}/doc/latex/math-e/10-10-4.ltx
%{_texmfdistdir}/doc/latex/math-e/10-10-5.ltx
%{_texmfdistdir}/doc/latex/math-e/10-10-6.ltx
%{_texmfdistdir}/doc/latex/math-e/10-10-7.ltx
%{_texmfdistdir}/doc/latex/math-e/11-01-1.ltx
%{_texmfdistdir}/doc/latex/math-e/11-01-2.ltx
%{_texmfdistdir}/doc/latex/math-e/11-01-3.ltx
%{_texmfdistdir}/doc/latex/math-e/11-01-4.ltx
%{_texmfdistdir}/doc/latex/math-e/11-01-5.ltx
%{_texmfdistdir}/doc/latex/math-e/11-01-6.ltx
%{_texmfdistdir}/doc/latex/math-e/11-01-7.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-1.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-10.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-11.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-12.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-13.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-14.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-15.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-16.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-17.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-18.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-19.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-2.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-20.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-21.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-22.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-23.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-24.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-25.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-26.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-3.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-4.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-5.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-6.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-7.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-8.ltx
%{_texmfdistdir}/doc/latex/math-e/11-02-9.ltx
%{_texmfdistdir}/doc/latex/math-e/README
%{_texmfdistdir}/doc/latex/math-e/exaarticle.cls
%{_texmfdistdir}/doc/latex/math-e/exaarticle2.cls
%{_texmfdistdir}/doc/latex/math-e/exaartplain.cls
%{_texmfdistdir}/doc/latex/math-e/exareport.cls
%{_texmfdistdir}/doc/latex/math-e/exasymbol.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-math-e-%{texlive_version}.%{texlive_noarch}.svn20062-%{release}-zypper
%endif

%package -n texlive-math-into-latex-4
Version:        %{texlive_version}.%{texlive_noarch}.svn44131
Release:        0
Summary:        Samples from Math into LaTeX, 4th Edition
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source191:      math-into-latex-4.doc.tar.xz

%description -n texlive-math-into-latex-4
Samples for the book `(More) Math into LaTeX', 4th edition. In
addition, there are two excerpts from the book: A Short Course
to help you get started quickly with LaTeX, including detailed
instructions on how to install LaTeX on a PC or a Mac; Math and
Text Symbol Tables.
%post -n texlive-math-into-latex-4
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-math-into-latex-4 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-math-into-latex-4
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-math-into-latex-4
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/math-into-latex-4/README
%{_texmfdistdir}/doc/latex/math-into-latex-4/README.TEXLIVE
%{_texmfdistdir}/doc/latex/math-into-latex-4/amsart.tpl
%{_texmfdistdir}/doc/latex/math-into-latex-4/amsproc.template
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer1.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer1.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer10.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer10.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer2.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer2.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer3.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer3.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer4.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer4.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer5.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer5.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6block.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6block.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6mod.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6mod.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6mod2.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer6mod2.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer7.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer7.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer8.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer8.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer9.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/babybeamer9.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-1.eps
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-1.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-2.eps
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-2.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-3.eps
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-3.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-4.eps
%{_texmfdistdir}/doc/latex/math-into-latex-4/basem3-4.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/beamerstructure1.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/beamerstructure1.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/beamerstructure2.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/beamerstructure2.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/bibl.tpl
%{_texmfdistdir}/doc/latex/math-into-latex-4/cleardoublepage.sty
%{_texmfdistdir}/doc/latex/math-into-latex-4/cube.eps
%{_texmfdistdir}/doc/latex/math-into-latex-4/cube.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/fonttbl.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/german.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/gg.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/gg2.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/ggamsart.tpl
%{_texmfdistdir}/doc/latex/math-into-latex-4/gratzer
%{_texmfdistdir}/doc/latex/math-into-latex-4/inbibl.tpl
%{_texmfdistdir}/doc/latex/math-into-latex-4/intrart.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/intrarti.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/intropres.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/legacy-article.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/letter.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/math.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/mathb.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/newlattice.sty
%{_texmfdistdir}/doc/latex/math-into-latex-4/notation.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/note1.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/note1b.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/note2.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/noteslug.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/products.eps
%{_texmfdistdir}/doc/latex/math-into-latex-4/products.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/quickbeamer.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/quickbeamer.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/quickbeamer1.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/quickbeamer1.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/quickbeamer2.pdf
%{_texmfdistdir}/doc/latex/math-into-latex-4/quickbeamer2.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/sampart-ref.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/sampart.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/sampartb.bib
%{_texmfdistdir}/doc/latex/math-into-latex-4/sampartb.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/sampartu.tex
%{_texmfdistdir}/doc/latex/math-into-latex-4/sample.cls
%{_texmfdistdir}/doc/latex/math-into-latex-4/template.bib
%{_texmfdistdir}/doc/latex/math-into-latex-4/topmat.tpl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-math-into-latex-4-%{texlive_version}.%{texlive_noarch}.svn44131-%{release}-zypper
%endif

%package -n texlive-mathabx
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Three series of mathematical symbols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathabx-doc >= %{texlive_version}
Provides:       tex(matha10.tfm)
Provides:       tex(matha12.tfm)
Provides:       tex(matha5.tfm)
Provides:       tex(matha6.tfm)
Provides:       tex(matha7.tfm)
Provides:       tex(matha8.tfm)
Provides:       tex(matha9.tfm)
Provides:       tex(mathabx.sty)
Provides:       tex(mathabx.tex)
Provides:       tex(mathastrotest10.tfm)
Provides:       tex(mathb10.tfm)
Provides:       tex(mathb12.tfm)
Provides:       tex(mathb5.tfm)
Provides:       tex(mathb6.tfm)
Provides:       tex(mathb7.tfm)
Provides:       tex(mathb8.tfm)
Provides:       tex(mathb9.tfm)
Provides:       tex(mathc10.tfm)
Provides:       tex(mathu10.tfm)
Provides:       tex(mathux10.tfm)
Provides:       tex(mathx10.tfm)
Provides:       tex(mathx12.tfm)
Provides:       tex(mathx5.tfm)
Provides:       tex(mathx6.tfm)
Provides:       tex(mathx7.tfm)
Provides:       tex(mathx8.tfm)
Provides:       tex(mathx9.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source192:      mathabx.tar.xz
Source193:      mathabx.doc.tar.xz

%description -n texlive-mathabx
Mathabx is a set of 3 mathematical symbols font series: matha,
mathb and mathx. They are defined by Metafont code and should
be of reasonable quality (bitmap output). Things change from
time to time, so there is no claim of stability (encoding,
metrics, design). The package includes Plain TeX and LaTeX
support macros. A version of the fonts, in Adobe Type 1 format,
is also available.

%package -n texlive-mathabx-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-mathabx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathabx-doc
This package includes the documentation for texlive-mathabx

%post -n texlive-mathabx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathabx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathabx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathabx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/mathabx/README
%{_texmfdistdir}/doc/fonts/mathabx/mathtest.pdf
%{_texmfdistdir}/doc/fonts/mathabx/mathtest.tex
%{_texmfdistdir}/doc/fonts/mathabx/testmac.tex

%files -n texlive-mathabx
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/mathabx/matha10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha12.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha5.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha6.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha7.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha8.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matha9.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathacnt.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathadrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/matharrw.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathastr.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathastrotest10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathastrotestdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathasym.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb12.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb5.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb6.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb7.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb8.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathb9.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbase.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbdel.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbigs.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathbsym.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathc10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathcall.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathcallgreek.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathcdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathfine.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathgrey.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathhbrw.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathineq.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathltlk.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathmbcb.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathprmt.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathsmsy.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathsubs.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathsymb.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathu10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathudrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathusym.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathux10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathuxdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx10.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx12.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx5.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx6.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx7.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx8.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathx9.mf
%{_texmfdistdir}/fonts/source/public/mathabx/mathxdrv.mf
%{_texmfdistdir}/fonts/source/public/mathabx/maydigit.mf
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha12.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/matha9.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathastrotest10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb12.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathb9.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathc10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathu10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathux10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx10.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx12.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathabx/mathx9.tfm
%{_texmfdistdir}/tex/generic/mathabx/mathabx.dcl
%{_texmfdistdir}/tex/generic/mathabx/mathabx.sty
%{_texmfdistdir}/tex/generic/mathabx/mathabx.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathabx-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-mathabx-type1
Version:        %{texlive_version}.%{texlive_noarch}.svn21129
Release:        0
Summary:        Outline version of the mathabx fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-mathabx >= %{texlive_version}
#!BuildIgnore: texlive-mathabx
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-mathabx-type1-fonts >= %{texlive_version}
Recommends:     texlive-mathabx-type1-doc >= %{texlive_version}
Provides:       tex(mathabx.map)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source194:      mathabx-type1.tar.xz
Source195:      mathabx-type1.doc.tar.xz

%description -n texlive-mathabx-type1
This is an Adobe Type 1 outline version of the mathabx fonts.

%package -n texlive-mathabx-type1-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn21129
Release:        0
Summary:        Documentation for texlive-mathabx-type1
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathabx-type1-doc
This package includes the documentation for texlive-mathabx-type1


%package -n texlive-mathabx-type1-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn21129
Release:        0
Summary:        Severed fonts for texlive-mathabx-type1
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-mathabx-type1-fonts
The  separated fonts package for texlive-mathabx-type1
%post -n texlive-mathabx-type1
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap mathabx.map' >> /var/run/texlive/run-updmap

%postun -n texlive-mathabx-type1 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap mathabx.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-mathabx-type1
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-mathabx-type1-fonts
%files -n texlive-mathabx-type1-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/mathabx-type1/README

%files -n texlive-mathabx-type1
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/mathabx-type1/mathabx.map
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/matha9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathastrotest10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathb9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathu10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathux10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathabx-type1/mathx9.pfb

%files -n texlive-mathabx-type1-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-mathabx-type1
%{_datadir}/fontconfig/conf.avail/58-texlive-mathabx-type1.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathabx-type1/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathabx-type1/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathabx-type1/fonts.scale
%{_datadir}/fonts/texlive-mathabx-type1/matha10.pfb
%{_datadir}/fonts/texlive-mathabx-type1/matha12.pfb
%{_datadir}/fonts/texlive-mathabx-type1/matha5.pfb
%{_datadir}/fonts/texlive-mathabx-type1/matha6.pfb
%{_datadir}/fonts/texlive-mathabx-type1/matha7.pfb
%{_datadir}/fonts/texlive-mathabx-type1/matha8.pfb
%{_datadir}/fonts/texlive-mathabx-type1/matha9.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathastrotest10.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathb10.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathb12.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathb5.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathb6.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathb7.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathb8.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathb9.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathc10.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathu10.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathux10.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathx10.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathx12.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathx5.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathx6.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathx7.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathx8.pfb
%{_datadir}/fonts/texlive-mathabx-type1/mathx9.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathabx-type1-fonts-%{texlive_version}.%{texlive_noarch}.svn21129-%{release}-zypper
%endif

%package -n texlive-mathalpha
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn52305
Release:        0
Summary:        General package for loading maths alphabets in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathalpha-doc >= %{texlive_version}
Provides:       tex(mathalfa.sty)
Provides:       tex(mathalpha.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source196:      mathalpha.tar.xz
Source197:      mathalpha.doc.tar.xz

%description -n texlive-mathalpha
Package mathalfa was renamed to mathalpha. For backward
compatibility the old name will continue to be recognized in
LaTeX documents. The package provides means of loading maths
alphabets (such as are normally addressed via macros \mathcal,
\mathbb, \mathfrak and \mathscr), offering various features
normally missing in existing packages for this job.

%package -n texlive-mathalpha-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn52305
Release:        0
Summary:        Documentation for texlive-mathalpha
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathalpha-doc
This package includes the documentation for texlive-mathalpha

%post -n texlive-mathalpha
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathalpha 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathalpha
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathalpha-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathalpha/README
%{_texmfdistdir}/doc/latex/mathalpha/mathalpha-doc.pdf
%{_texmfdistdir}/doc/latex/mathalpha/mathalpha-doc.tex

%files -n texlive-mathalpha
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathalpha/mathalfa.sty
%{_texmfdistdir}/tex/latex/mathalpha/mathalpha.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathalpha-%{texlive_version}.%{texlive_noarch}.1.13svn52305-%{release}-zypper
%endif

%package -n texlive-mathastext
Version:        %{texlive_version}.%{texlive_noarch}.1.3wsvn52840
Release:        0
Summary:        Use the text font in maths mode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathastext-doc >= %{texlive_version}
Provides:       tex(mathastext.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source198:      mathastext.tar.xz
Source199:      mathastext.doc.tar.xz

%description -n texlive-mathastext
The package uses a text font (usually the document's text font)
for the letters of the Latin alphabet needed when typesetting
mathematics. (Optionally, other characters in the font may also
be used). This facility makes possible (for a document with
simple mathematics) a far wider choice of text font, with
little worry that no specially designed accompanying maths
fonts are available. The package also offers a simple mechanism
for using many different choices of (text hence, now, maths)
font in the same document. Of course, using one font for two
purposes helps produce smaller PDF files. The package, if
running under LuaTeX, requires the TeX live 2013 distribution
(or later).

%package -n texlive-mathastext-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3wsvn52840
Release:        0
Summary:        Documentation for texlive-mathastext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathastext-doc
This package includes the documentation for texlive-mathastext

%post -n texlive-mathastext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathastext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathastext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathastext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathastext/ChangeLog.md
%{_texmfdistdir}/doc/latex/mathastext/INSTALL.txt
%{_texmfdistdir}/doc/latex/mathastext/README.md
%{_texmfdistdir}/doc/latex/mathastext/mathastext.pdf
%{_texmfdistdir}/doc/latex/mathastext/mathastext.tex
%{_texmfdistdir}/doc/latex/mathastext/mathastexttestalphabets.pdf
%{_texmfdistdir}/doc/latex/mathastext/mathastexttestalphabets.tex
%{_texmfdistdir}/doc/latex/mathastext/mathastexttestmathversions.tex
%{_texmfdistdir}/doc/latex/mathastext/mathastexttestunicodelinux.tex
%{_texmfdistdir}/doc/latex/mathastext/mathastexttestunicodemacos.tex

%files -n texlive-mathastext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathastext/mathastext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathastext-%{texlive_version}.%{texlive_noarch}.1.3wsvn52840-%{release}-zypper
%endif

%package -n texlive-mathcommand
Version:        %{texlive_version}.%{texlive_noarch}.1.03svn53044
Release:        0
Summary:        \newcommand-like commands for defining math macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathcommand-doc >= %{texlive_version}
Provides:       tex(mathcommand.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source200:      mathcommand.tar.xz
Source201:      mathcommand.doc.tar.xz

%description -n texlive-mathcommand
This package provides functionalities for defining macros that
have different behaviors depending on whether in math or text
mode, that absorb Primes, Indices and Exponents (PIE) as extra
parameters usable in the code; and it offers some iteration
facilities for defining macros with similar code. The primary
objective of this package is to be used together with the
knowledge package for a proper handling of mathematical
notations.

%package -n texlive-mathcommand-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.03svn53044
Release:        0
Summary:        Documentation for texlive-mathcommand
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathcommand-doc
This package includes the documentation for texlive-mathcommand

%post -n texlive-mathcommand
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathcommand 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathcommand
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathcommand-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathcommand/README.md
%{_texmfdistdir}/doc/latex/mathcommand/makefile
%{_texmfdistdir}/doc/latex/mathcommand/mathcommand.pdf

%files -n texlive-mathcommand
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathcommand/mathcommand.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathcommand-%{texlive_version}.%{texlive_noarch}.1.03svn53044-%{release}-zypper
%endif

%package -n texlive-mathcomp
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1fsvn15878
Release:        0
Summary:        Text symbols in maths mode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathcomp-doc >= %{texlive_version}
Provides:       tex(mathcomp.sty)
Requires:       tex(textcomp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source202:      mathcomp.tar.xz
Source203:      mathcomp.doc.tar.xz

%description -n texlive-mathcomp
A package which provides access to some interesting characters
of the Text Companion fonts (TS1 encoding) in maths mode.

%package -n texlive-mathcomp-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1fsvn15878
Release:        0
Summary:        Documentation for texlive-mathcomp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathcomp-doc
This package includes the documentation for texlive-mathcomp

%post -n texlive-mathcomp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathcomp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathcomp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathcomp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathcomp/mathcomp.pdf

%files -n texlive-mathcomp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathcomp/mathcomp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathcomp-%{texlive_version}.%{texlive_noarch}.0.0.1fsvn15878-%{release}-zypper
%endif

%package -n texlive-mathdesign
Version:        %{texlive_version}.%{texlive_noarch}.2.31svn31639
Release:        0
Summary:        Mathematical fonts to fit with particular text fonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-mathdesign-fonts >= %{texlive_version}
Recommends:     texlive-mathdesign-doc >= %{texlive_version}
Requires:       tex(texnansi.enc)
Provides:       tex(a_2dncez.enc)
Provides:       tex(a_2rwgaw.enc)
Provides:       tex(a_42s2zl.enc)
Provides:       tex(a_45o73x.enc)
Provides:       tex(a_4b5i6w.enc)
Provides:       tex(a_57soyv.enc)
Provides:       tex(a_csqf63.enc)
Provides:       tex(a_e65dz6.enc)
Provides:       tex(a_g2masa.enc)
Provides:       tex(a_g47ck7.enc)
Provides:       tex(a_ipzj2o.enc)
Provides:       tex(a_kld4uc.enc)
Provides:       tex(a_mdpn2k.enc)
Provides:       tex(a_n2elaj.enc)
Provides:       tex(a_oxfbe4.enc)
Provides:       tex(a_py5znv.enc)
Provides:       tex(a_qnfjtt.enc)
Provides:       tex(a_qzg4u4.enc)
Provides:       tex(a_r2nxhw.enc)
Provides:       tex(a_rl4tn2.enc)
Provides:       tex(a_rxz3ga.enc)
Provides:       tex(a_telfo7.enc)
Provides:       tex(a_uwwzqd.enc)
Provides:       tex(a_yezm6g.enc)
Provides:       tex(bchb8a.tfm)
Provides:       tex(bchbc8a.tfm)
Provides:       tex(bchbc8y.tfm)
Provides:       tex(bchbi8a.tfm)
Provides:       tex(bchr8a.tfm)
Provides:       tex(bchrc8a.tfm)
Provides:       tex(bchrc8y.tfm)
Provides:       tex(bchri8a.tfm)
Provides:       tex(mathdesign.sty)
Provides:       tex(md-chb7m.tfm)
Provides:       tex(md-chb7t.tfm)
Provides:       tex(md-chb7v.tfm)
Provides:       tex(md-chb7y.tfm)
Provides:       tex(md-chb8c.tfm)
Provides:       tex(md-chb8t.tfm)
Provides:       tex(md-chb8y.tfm)
Provides:       tex(md-chbc8y.tfm)
Provides:       tex(md-chbi7m.tfm)
Provides:       tex(md-chbi7t.tfm)
Provides:       tex(md-chbi8c.tfm)
Provides:       tex(md-chbi8t.tfm)
Provides:       tex(md-chbi8y.tfm)
Provides:       tex(md-chbma.tfm)
Provides:       tex(md-chbmb.tfm)
Provides:       tex(md-chbo7t.tfm)
Provides:       tex(md-chbo8c.tfm)
Provides:       tex(md-chbo8t.tfm)
Provides:       tex(md-chbo8y.tfm)
Provides:       tex(md-chboc8y.tfm)
Provides:       tex(md-chr7m.tfm)
Provides:       tex(md-chr7t.tfm)
Provides:       tex(md-chr7v.tfm)
Provides:       tex(md-chr7y.tfm)
Provides:       tex(md-chr8c.tfm)
Provides:       tex(md-chr8t.tfm)
Provides:       tex(md-chr8y.tfm)
Provides:       tex(md-chrc8y.tfm)
Provides:       tex(md-chree.tfm)
Provides:       tex(md-chri7m.tfm)
Provides:       tex(md-chri7t.tfm)
Provides:       tex(md-chri8c.tfm)
Provides:       tex(md-chri8t.tfm)
Provides:       tex(md-chri8y.tfm)
Provides:       tex(md-chrma.tfm)
Provides:       tex(md-chrmb.tfm)
Provides:       tex(md-chro7t.tfm)
Provides:       tex(md-chro8c.tfm)
Provides:       tex(md-chro8t.tfm)
Provides:       tex(md-chro8y.tfm)
Provides:       tex(md-chroc8y.tfm)
Provides:       tex(md-cib7m.tfm)
Provides:       tex(md-cib7t.tfm)
Provides:       tex(md-cib7v.tfm)
Provides:       tex(md-cib7y.tfm)
Provides:       tex(md-cib8c.tfm)
Provides:       tex(md-cib8t.tfm)
Provides:       tex(md-cibee.tfm)
Provides:       tex(md-cibi7m.tfm)
Provides:       tex(md-cibi7t.tfm)
Provides:       tex(md-cibi8c.tfm)
Provides:       tex(md-cibi8t.tfm)
Provides:       tex(md-cibma.tfm)
Provides:       tex(md-cibmb.tfm)
Provides:       tex(md-cir7m.tfm)
Provides:       tex(md-cir7t.tfm)
Provides:       tex(md-cir7v.tfm)
Provides:       tex(md-cir7y.tfm)
Provides:       tex(md-cir8c.tfm)
Provides:       tex(md-cir8t.tfm)
Provides:       tex(md-ciree.tfm)
Provides:       tex(md-ciri7m.tfm)
Provides:       tex(md-ciri7t.tfm)
Provides:       tex(md-ciri8c.tfm)
Provides:       tex(md-ciri8t.tfm)
Provides:       tex(md-cirma.tfm)
Provides:       tex(md-cirmb.tfm)
Provides:       tex(md-gdr7m.tfm)
Provides:       tex(md-gdr7t.tfm)
Provides:       tex(md-gdr7v.tfm)
Provides:       tex(md-gdr7y.tfm)
Provides:       tex(md-gdr8c.tfm)
Provides:       tex(md-gdr8t.tfm)
Provides:       tex(md-gdree.tfm)
Provides:       tex(md-gdri7m.tfm)
Provides:       tex(md-gdri7t.tfm)
Provides:       tex(md-gdri8c.tfm)
Provides:       tex(md-gdri8t.tfm)
Provides:       tex(md-gdrma.tfm)
Provides:       tex(md-gdrmb.tfm)
Provides:       tex(md-gds7m.tfm)
Provides:       tex(md-gds7t.tfm)
Provides:       tex(md-gds7v.tfm)
Provides:       tex(md-gds7y.tfm)
Provides:       tex(md-gds8c.tfm)
Provides:       tex(md-gds8t.tfm)
Provides:       tex(md-gdsi7m.tfm)
Provides:       tex(md-gdsi7t.tfm)
Provides:       tex(md-gdsi8c.tfm)
Provides:       tex(md-gdsi8t.tfm)
Provides:       tex(md-gdsma.tfm)
Provides:       tex(md-gdsmb.tfm)
Provides:       tex(md-gmm7m.tfm)
Provides:       tex(md-gmm7t.tfm)
Provides:       tex(md-gmm7v.tfm)
Provides:       tex(md-gmm7y.tfm)
Provides:       tex(md-gmm8c.tfm)
Provides:       tex(md-gmm8t.tfm)
Provides:       tex(md-gmm8y.tfm)
Provides:       tex(md-gmmi7m.tfm)
Provides:       tex(md-gmmi7t.tfm)
Provides:       tex(md-gmmi8c.tfm)
Provides:       tex(md-gmmi8t.tfm)
Provides:       tex(md-gmmi8y.tfm)
Provides:       tex(md-gmmma.tfm)
Provides:       tex(md-gmmmb.tfm)
Provides:       tex(md-gmmo7t.tfm)
Provides:       tex(md-gmmo8c.tfm)
Provides:       tex(md-gmmo8t.tfm)
Provides:       tex(md-gmmo8y.tfm)
Provides:       tex(md-gmr7m.tfm)
Provides:       tex(md-gmr7t.tfm)
Provides:       tex(md-gmr7v.tfm)
Provides:       tex(md-gmr7y.tfm)
Provides:       tex(md-gmr8c.tfm)
Provides:       tex(md-gmr8t.tfm)
Provides:       tex(md-gmr8y.tfm)
Provides:       tex(md-gmree.tfm)
Provides:       tex(md-gmri7m.tfm)
Provides:       tex(md-gmri7t.tfm)
Provides:       tex(md-gmri8c.tfm)
Provides:       tex(md-gmri8t.tfm)
Provides:       tex(md-gmri8y.tfm)
Provides:       tex(md-gmrma.tfm)
Provides:       tex(md-gmrmb.tfm)
Provides:       tex(md-gmro7t.tfm)
Provides:       tex(md-gmro8c.tfm)
Provides:       tex(md-gmro8t.tfm)
Provides:       tex(md-gmro8y.tfm)
Provides:       tex(md-grbb7m.tfm)
Provides:       tex(md-grbbi7m.tfm)
Provides:       tex(md-grbr7m.tfm)
Provides:       tex(md-grbri7m.tfm)
Provides:       tex(md-grdb7m.tfm)
Provides:       tex(md-grdbi7m.tfm)
Provides:       tex(md-grdr7m.tfm)
Provides:       tex(md-grdri7m.tfm)
Provides:       tex(md-usr7m.tfm)
Provides:       tex(md-usr7t.tfm)
Provides:       tex(md-usr7t5.tfm)
Provides:       tex(md-usr7t6.tfm)
Provides:       tex(md-usr7t7.tfm)
Provides:       tex(md-usr7t8.tfm)
Provides:       tex(md-usr7t9.tfm)
Provides:       tex(md-usr7v.tfm)
Provides:       tex(md-usr7y.tfm)
Provides:       tex(md-usr8c.tfm)
Provides:       tex(md-usr8t.tfm)
Provides:       tex(md-usree.tfm)
Provides:       tex(md-usri7m.tfm)
Provides:       tex(md-usri7t.tfm)
Provides:       tex(md-usri7t5.tfm)
Provides:       tex(md-usri7t6.tfm)
Provides:       tex(md-usri7t7.tfm)
Provides:       tex(md-usri7t8.tfm)
Provides:       tex(md-usri7t9.tfm)
Provides:       tex(md-usri8c.tfm)
Provides:       tex(md-usri8t.tfm)
Provides:       tex(md-usrma.tfm)
Provides:       tex(md-usrmb.tfm)
Provides:       tex(md-uss7m.tfm)
Provides:       tex(md-uss7t.tfm)
Provides:       tex(md-uss7v.tfm)
Provides:       tex(md-uss7y.tfm)
Provides:       tex(md-uss8c.tfm)
Provides:       tex(md-uss8t.tfm)
Provides:       tex(md-ussi7m.tfm)
Provides:       tex(md-ussi7t.tfm)
Provides:       tex(md-ussi8c.tfm)
Provides:       tex(md-ussi8t.tfm)
Provides:       tex(md-ussma.tfm)
Provides:       tex(md-ussmb.tfm)
Provides:       tex(md-utb7m.tfm)
Provides:       tex(md-utb7t.tfm)
Provides:       tex(md-utb7v.tfm)
Provides:       tex(md-utb7y.tfm)
Provides:       tex(md-utb8c.tfm)
Provides:       tex(md-utb8t.tfm)
Provides:       tex(md-utb8y.tfm)
Provides:       tex(md-utbee.tfm)
Provides:       tex(md-utbi7m.tfm)
Provides:       tex(md-utbi7t.tfm)
Provides:       tex(md-utbi8c.tfm)
Provides:       tex(md-utbi8t.tfm)
Provides:       tex(md-utbi8y.tfm)
Provides:       tex(md-utbma.tfm)
Provides:       tex(md-utbmb.tfm)
Provides:       tex(md-utbo7t.tfm)
Provides:       tex(md-utbo8c.tfm)
Provides:       tex(md-utbo8t.tfm)
Provides:       tex(md-utbo8y.tfm)
Provides:       tex(md-utr7m.tfm)
Provides:       tex(md-utr7t.tfm)
Provides:       tex(md-utr7v.tfm)
Provides:       tex(md-utr7y.tfm)
Provides:       tex(md-utr8c.tfm)
Provides:       tex(md-utr8t.tfm)
Provides:       tex(md-utr8y.tfm)
Provides:       tex(md-utree.tfm)
Provides:       tex(md-utri7m.tfm)
Provides:       tex(md-utri7t.tfm)
Provides:       tex(md-utri8c.tfm)
Provides:       tex(md-utri8t.tfm)
Provides:       tex(md-utri8y.tfm)
Provides:       tex(md-utrma.tfm)
Provides:       tex(md-utrmb.tfm)
Provides:       tex(md-utro7t.tfm)
Provides:       tex(md-utro8c.tfm)
Provides:       tex(md-utro8t.tfm)
Provides:       tex(md-utro8y.tfm)
Provides:       tex(md8x.enc)
Provides:       tex(mdacmr.fd)
Provides:       tex(mdamdbch.fd)
Provides:       tex(mdamdici.fd)
Provides:       tex(mdamdpgd.fd)
Provides:       tex(mdamdpus.fd)
Provides:       tex(mdamdput.fd)
Provides:       tex(mdamdugm.fd)
Provides:       tex(mdbch.cfg)
Provides:       tex(mdbch.map)
Provides:       tex(mdbch.sty)
Provides:       tex(mdbchb7m.tfm)
Provides:       tex(mdbchb7m.vf)
Provides:       tex(mdbchb7t.tfm)
Provides:       tex(mdbchb7t.vf)
Provides:       tex(mdbchb7v.tfm)
Provides:       tex(mdbchb7v.vf)
Provides:       tex(mdbchb7y.tfm)
Provides:       tex(mdbchb7y.vf)
Provides:       tex(mdbchb8c.tfm)
Provides:       tex(mdbchb8c.vf)
Provides:       tex(mdbchb8t.tfm)
Provides:       tex(mdbchb8t.vf)
Provides:       tex(mdbchbc8t.tfm)
Provides:       tex(mdbchbc8t.vf)
Provides:       tex(mdbchbfc8t.tfm)
Provides:       tex(mdbchbfc8t.vf)
Provides:       tex(mdbchbi7m.tfm)
Provides:       tex(mdbchbi7m.vf)
Provides:       tex(mdbchbi7t.tfm)
Provides:       tex(mdbchbi7t.vf)
Provides:       tex(mdbchbi8c.tfm)
Provides:       tex(mdbchbi8c.vf)
Provides:       tex(mdbchbi8t.tfm)
Provides:       tex(mdbchbi8t.vf)
Provides:       tex(mdbchbifc8t.tfm)
Provides:       tex(mdbchbifc8t.vf)
Provides:       tex(mdbchbma.tfm)
Provides:       tex(mdbchbma.vf)
Provides:       tex(mdbchbmb.tfm)
Provides:       tex(mdbchbmb.vf)
Provides:       tex(mdbchbo7t.tfm)
Provides:       tex(mdbchbo7t.vf)
Provides:       tex(mdbchbo8c.tfm)
Provides:       tex(mdbchbo8c.vf)
Provides:       tex(mdbchbo8t.tfm)
Provides:       tex(mdbchbo8t.vf)
Provides:       tex(mdbchbofc8t.tfm)
Provides:       tex(mdbchbofc8t.vf)
Provides:       tex(mdbchr7m.tfm)
Provides:       tex(mdbchr7m.vf)
Provides:       tex(mdbchr7t.tfm)
Provides:       tex(mdbchr7t.vf)
Provides:       tex(mdbchr7v.tfm)
Provides:       tex(mdbchr7v.vf)
Provides:       tex(mdbchr7y.tfm)
Provides:       tex(mdbchr7y.vf)
Provides:       tex(mdbchr8c.tfm)
Provides:       tex(mdbchr8c.vf)
Provides:       tex(mdbchr8t.tfm)
Provides:       tex(mdbchr8t.vf)
Provides:       tex(mdbchrc8t.tfm)
Provides:       tex(mdbchrc8t.vf)
Provides:       tex(mdbchrfc8t.tfm)
Provides:       tex(mdbchrfc8t.vf)
Provides:       tex(mdbchri7m.tfm)
Provides:       tex(mdbchri7m.vf)
Provides:       tex(mdbchri7t.tfm)
Provides:       tex(mdbchri7t.vf)
Provides:       tex(mdbchri8c.tfm)
Provides:       tex(mdbchri8c.vf)
Provides:       tex(mdbchri8t.tfm)
Provides:       tex(mdbchri8t.vf)
Provides:       tex(mdbchrifc8t.tfm)
Provides:       tex(mdbchrifc8t.vf)
Provides:       tex(mdbchrma.tfm)
Provides:       tex(mdbchrma.vf)
Provides:       tex(mdbchrmb.tfm)
Provides:       tex(mdbchrmb.vf)
Provides:       tex(mdbchro7t.tfm)
Provides:       tex(mdbchro7t.vf)
Provides:       tex(mdbchro8c.tfm)
Provides:       tex(mdbchro8c.vf)
Provides:       tex(mdbchro8t.tfm)
Provides:       tex(mdbchro8t.vf)
Provides:       tex(mdbchrofc8t.tfm)
Provides:       tex(mdbchrofc8t.vf)
Provides:       tex(mdbcmr.fd)
Provides:       tex(mdbmdbch.fd)
Provides:       tex(mdbmdici.fd)
Provides:       tex(mdbmdpgd.fd)
Provides:       tex(mdbmdpus.fd)
Provides:       tex(mdbmdput.fd)
Provides:       tex(mdbmdugm.fd)
Provides:       tex(mdfont.def)
Provides:       tex(mdgrbCb7m.tfm)
Provides:       tex(mdgrbCb7m.vf)
Provides:       tex(mdgrbCbi7m.tfm)
Provides:       tex(mdgrbCbi7m.vf)
Provides:       tex(mdgrbCr7m.tfm)
Provides:       tex(mdgrbCr7m.vf)
Provides:       tex(mdgrbCri7m.tfm)
Provides:       tex(mdgrbCri7m.vf)
Provides:       tex(mdgrbb7m.tfm)
Provides:       tex(mdgrbb7m.vf)
Provides:       tex(mdgrbbi7m.tfm)
Provides:       tex(mdgrbbi7m.vf)
Provides:       tex(mdgrbr7m.tfm)
Provides:       tex(mdgrbr7m.vf)
Provides:       tex(mdgrbri7m.tfm)
Provides:       tex(mdgrbri7m.vf)
Provides:       tex(mdgrdCb7m.tfm)
Provides:       tex(mdgrdCb7m.vf)
Provides:       tex(mdgrdCbi7m.tfm)
Provides:       tex(mdgrdCbi7m.vf)
Provides:       tex(mdgrdCri7m.tfm)
Provides:       tex(mdgrdCri7m.vf)
Provides:       tex(mdgrdb7m.tfm)
Provides:       tex(mdgrdb7m.vf)
Provides:       tex(mdgrdbi7m.tfm)
Provides:       tex(mdgrdbi7m.vf)
Provides:       tex(mdgrdr7m.tfm)
Provides:       tex(mdgrdr7m.vf)
Provides:       tex(mdgrdrC7m.tfm)
Provides:       tex(mdgrdrC7m.vf)
Provides:       tex(mdgrdri7m.tfm)
Provides:       tex(mdgrdri7m.vf)
Provides:       tex(mdgreek.map)
Provides:       tex(mdici.cfg)
Provides:       tex(mdici.map)
Provides:       tex(mdici.sty)
Provides:       tex(mdicib7m.tfm)
Provides:       tex(mdicib7m.vf)
Provides:       tex(mdicib7t.tfm)
Provides:       tex(mdicib7t.vf)
Provides:       tex(mdicib7v.tfm)
Provides:       tex(mdicib7v.vf)
Provides:       tex(mdicib7y.tfm)
Provides:       tex(mdicib7y.vf)
Provides:       tex(mdicib8c.tfm)
Provides:       tex(mdicib8c.vf)
Provides:       tex(mdicib8t.tfm)
Provides:       tex(mdicib8t.vf)
Provides:       tex(mdicibc8c.tfm)
Provides:       tex(mdicibc8c.vf)
Provides:       tex(mdicibc8t.tfm)
Provides:       tex(mdicibc8t.vf)
Provides:       tex(mdicibfc8t.tfm)
Provides:       tex(mdicibfc8t.vf)
Provides:       tex(mdicibi7m.tfm)
Provides:       tex(mdicibi7m.vf)
Provides:       tex(mdicibi7t.tfm)
Provides:       tex(mdicibi7t.vf)
Provides:       tex(mdicibi8c.tfm)
Provides:       tex(mdicibi8c.vf)
Provides:       tex(mdicibi8t.tfm)
Provides:       tex(mdicibi8t.vf)
Provides:       tex(mdicibic8c.tfm)
Provides:       tex(mdicibic8c.vf)
Provides:       tex(mdicibic8t.tfm)
Provides:       tex(mdicibic8t.vf)
Provides:       tex(mdicibifc8t.tfm)
Provides:       tex(mdicibifc8t.vf)
Provides:       tex(mdicibiu7m.vf)
Provides:       tex(mdicibma.tfm)
Provides:       tex(mdicibma.vf)
Provides:       tex(mdicibmb.tfm)
Provides:       tex(mdicibmb.vf)
Provides:       tex(mdicibui7m.vf)
Provides:       tex(mdicic8c.tfm)
Provides:       tex(mdicic8c.vf)
Provides:       tex(mdicic8t.tfm)
Provides:       tex(mdicic8t.vf)
Provides:       tex(mdicicc8c.tfm)
Provides:       tex(mdicicc8c.vf)
Provides:       tex(mdicicc8t.tfm)
Provides:       tex(mdicicc8t.vf)
Provides:       tex(mdicicfc8t.tfm)
Provides:       tex(mdicicfc8t.vf)
Provides:       tex(mdicici8c.tfm)
Provides:       tex(mdicici8c.vf)
Provides:       tex(mdicici8t.tfm)
Provides:       tex(mdicici8t.vf)
Provides:       tex(mdicicic8c.tfm)
Provides:       tex(mdicicic8c.vf)
Provides:       tex(mdicicic8t.tfm)
Provides:       tex(mdicicic8t.vf)
Provides:       tex(mdicicifc8t.tfm)
Provides:       tex(mdicicifc8t.vf)
Provides:       tex(mdicir7m.tfm)
Provides:       tex(mdicir7m.vf)
Provides:       tex(mdicir7t.tfm)
Provides:       tex(mdicir7t.vf)
Provides:       tex(mdicir7v.tfm)
Provides:       tex(mdicir7v.vf)
Provides:       tex(mdicir7y.tfm)
Provides:       tex(mdicir7y.vf)
Provides:       tex(mdicir8c.tfm)
Provides:       tex(mdicir8c.vf)
Provides:       tex(mdicir8t.tfm)
Provides:       tex(mdicir8t.vf)
Provides:       tex(mdicirc8c.tfm)
Provides:       tex(mdicirc8c.vf)
Provides:       tex(mdicirc8t.tfm)
Provides:       tex(mdicirc8t.vf)
Provides:       tex(mdicirfc8t.tfm)
Provides:       tex(mdicirfc8t.vf)
Provides:       tex(mdiciri7m.tfm)
Provides:       tex(mdiciri7m.vf)
Provides:       tex(mdiciri7t.tfm)
Provides:       tex(mdiciri7t.vf)
Provides:       tex(mdiciri8c.tfm)
Provides:       tex(mdiciri8c.vf)
Provides:       tex(mdiciri8t.tfm)
Provides:       tex(mdiciri8t.vf)
Provides:       tex(mdiciric8c.tfm)
Provides:       tex(mdiciric8c.vf)
Provides:       tex(mdiciric8t.tfm)
Provides:       tex(mdiciric8t.vf)
Provides:       tex(mdicirifc8t.tfm)
Provides:       tex(mdicirifc8t.vf)
Provides:       tex(mdiciriu7m.vf)
Provides:       tex(mdicirma.tfm)
Provides:       tex(mdicirma.vf)
Provides:       tex(mdicirmb.tfm)
Provides:       tex(mdicirmb.vf)
Provides:       tex(mdicirui7m.vf)
Provides:       tex(mdpgd.cfg)
Provides:       tex(mdpgd.map)
Provides:       tex(mdpgd.sty)
Provides:       tex(mdpgdb8c.tfm)
Provides:       tex(mdpgdb8c.vf)
Provides:       tex(mdpgdb8t.tfm)
Provides:       tex(mdpgdb8t.vf)
Provides:       tex(mdpgdbc8c.tfm)
Provides:       tex(mdpgdbc8c.vf)
Provides:       tex(mdpgdbc8t.tfm)
Provides:       tex(mdpgdbc8t.vf)
Provides:       tex(mdpgdbfc8t.tfm)
Provides:       tex(mdpgdbfc8t.vf)
Provides:       tex(mdpgdbi8c.tfm)
Provides:       tex(mdpgdbi8c.vf)
Provides:       tex(mdpgdbi8t.tfm)
Provides:       tex(mdpgdbi8t.vf)
Provides:       tex(mdpgdbic8c.tfm)
Provides:       tex(mdpgdbic8c.vf)
Provides:       tex(mdpgdbic8t.tfm)
Provides:       tex(mdpgdbic8t.vf)
Provides:       tex(mdpgdbifc8t.tfm)
Provides:       tex(mdpgdbifc8t.vf)
Provides:       tex(mdpgdr7m.tfm)
Provides:       tex(mdpgdr7m.vf)
Provides:       tex(mdpgdr7t.tfm)
Provides:       tex(mdpgdr7t.vf)
Provides:       tex(mdpgdr7v.tfm)
Provides:       tex(mdpgdr7v.vf)
Provides:       tex(mdpgdr7y.tfm)
Provides:       tex(mdpgdr7y.vf)
Provides:       tex(mdpgdr8c.tfm)
Provides:       tex(mdpgdr8c.vf)
Provides:       tex(mdpgdr8t.tfm)
Provides:       tex(mdpgdr8t.vf)
Provides:       tex(mdpgdrc8c.tfm)
Provides:       tex(mdpgdrc8c.vf)
Provides:       tex(mdpgdrc8t.tfm)
Provides:       tex(mdpgdrc8t.vf)
Provides:       tex(mdpgdrfc8t.tfm)
Provides:       tex(mdpgdrfc8t.vf)
Provides:       tex(mdpgdri7m.tfm)
Provides:       tex(mdpgdri7m.vf)
Provides:       tex(mdpgdri7t.tfm)
Provides:       tex(mdpgdri7t.vf)
Provides:       tex(mdpgdri8c.tfm)
Provides:       tex(mdpgdri8c.vf)
Provides:       tex(mdpgdri8t.tfm)
Provides:       tex(mdpgdri8t.vf)
Provides:       tex(mdpgdric8c.tfm)
Provides:       tex(mdpgdric8c.vf)
Provides:       tex(mdpgdric8t.tfm)
Provides:       tex(mdpgdric8t.vf)
Provides:       tex(mdpgdrifc8t.tfm)
Provides:       tex(mdpgdrifc8t.vf)
Provides:       tex(mdpgdrma.tfm)
Provides:       tex(mdpgdrma.vf)
Provides:       tex(mdpgdrmb.tfm)
Provides:       tex(mdpgdrmb.vf)
Provides:       tex(mdpgds7m.tfm)
Provides:       tex(mdpgds7m.vf)
Provides:       tex(mdpgds7t.tfm)
Provides:       tex(mdpgds7t.vf)
Provides:       tex(mdpgds7v.tfm)
Provides:       tex(mdpgds7v.vf)
Provides:       tex(mdpgds7y.tfm)
Provides:       tex(mdpgds7y.vf)
Provides:       tex(mdpgds8c.tfm)
Provides:       tex(mdpgds8c.vf)
Provides:       tex(mdpgds8t.tfm)
Provides:       tex(mdpgds8t.vf)
Provides:       tex(mdpgdsc8c.tfm)
Provides:       tex(mdpgdsc8c.vf)
Provides:       tex(mdpgdsc8t.tfm)
Provides:       tex(mdpgdsc8t.vf)
Provides:       tex(mdpgdsfc8t.tfm)
Provides:       tex(mdpgdsfc8t.vf)
Provides:       tex(mdpgdsi7m.tfm)
Provides:       tex(mdpgdsi7m.vf)
Provides:       tex(mdpgdsi7t.tfm)
Provides:       tex(mdpgdsi7t.vf)
Provides:       tex(mdpgdsi8c.tfm)
Provides:       tex(mdpgdsi8c.vf)
Provides:       tex(mdpgdsi8t.tfm)
Provides:       tex(mdpgdsi8t.vf)
Provides:       tex(mdpgdsic8c.tfm)
Provides:       tex(mdpgdsic8c.vf)
Provides:       tex(mdpgdsic8t.tfm)
Provides:       tex(mdpgdsic8t.vf)
Provides:       tex(mdpgdsifc8t.tfm)
Provides:       tex(mdpgdsifc8t.vf)
Provides:       tex(mdpgdsma.tfm)
Provides:       tex(mdpgdsma.vf)
Provides:       tex(mdpgdsmb.tfm)
Provides:       tex(mdpgdsmb.vf)
Provides:       tex(mdpus.cfg)
Provides:       tex(mdpus.map)
Provides:       tex(mdpus.sty)
Provides:       tex(mdpusb8c.tfm)
Provides:       tex(mdpusb8c.vf)
Provides:       tex(mdpusb8t.tfm)
Provides:       tex(mdpusb8t.vf)
Provides:       tex(mdpusbc8c.tfm)
Provides:       tex(mdpusbc8c.vf)
Provides:       tex(mdpusbc8t.tfm)
Provides:       tex(mdpusbc8t.vf)
Provides:       tex(mdpusbfc8t.tfm)
Provides:       tex(mdpusbfc8t.vf)
Provides:       tex(mdpusbi8c.tfm)
Provides:       tex(mdpusbi8c.vf)
Provides:       tex(mdpusbi8t.tfm)
Provides:       tex(mdpusbi8t.vf)
Provides:       tex(mdpusbic8c.tfm)
Provides:       tex(mdpusbic8c.vf)
Provides:       tex(mdpusbic8t.tfm)
Provides:       tex(mdpusbic8t.vf)
Provides:       tex(mdpusbifc8t.tfm)
Provides:       tex(mdpusbifc8t.vf)
Provides:       tex(mdpusr7m.tfm)
Provides:       tex(mdpusr7m.vf)
Provides:       tex(mdpusr7t.tfm)
Provides:       tex(mdpusr7t.vf)
Provides:       tex(mdpusr7v.tfm)
Provides:       tex(mdpusr7v.vf)
Provides:       tex(mdpusr7y.tfm)
Provides:       tex(mdpusr7y.vf)
Provides:       tex(mdpusr8c.tfm)
Provides:       tex(mdpusr8c.vf)
Provides:       tex(mdpusr8t.tfm)
Provides:       tex(mdpusr8t.vf)
Provides:       tex(mdpusrc8c.tfm)
Provides:       tex(mdpusrc8c.vf)
Provides:       tex(mdpusrc8t.tfm)
Provides:       tex(mdpusrc8t.vf)
Provides:       tex(mdpusrfc8t.tfm)
Provides:       tex(mdpusrfc8t.vf)
Provides:       tex(mdpusri7m.tfm)
Provides:       tex(mdpusri7m.vf)
Provides:       tex(mdpusri7t.tfm)
Provides:       tex(mdpusri7t.vf)
Provides:       tex(mdpusri8c.tfm)
Provides:       tex(mdpusri8c.vf)
Provides:       tex(mdpusri8t.tfm)
Provides:       tex(mdpusri8t.vf)
Provides:       tex(mdpusric8c.tfm)
Provides:       tex(mdpusric8c.vf)
Provides:       tex(mdpusric8t.tfm)
Provides:       tex(mdpusric8t.vf)
Provides:       tex(mdpusrifc8t.tfm)
Provides:       tex(mdpusrifc8t.vf)
Provides:       tex(mdpusrma.tfm)
Provides:       tex(mdpusrma.vf)
Provides:       tex(mdpusrmb.tfm)
Provides:       tex(mdpusrmb.vf)
Provides:       tex(mdpuss7m.tfm)
Provides:       tex(mdpuss7m.vf)
Provides:       tex(mdpuss7t.tfm)
Provides:       tex(mdpuss7t.vf)
Provides:       tex(mdpuss7v.tfm)
Provides:       tex(mdpuss7v.vf)
Provides:       tex(mdpuss7y.tfm)
Provides:       tex(mdpuss7y.vf)
Provides:       tex(mdpuss8c.tfm)
Provides:       tex(mdpuss8c.vf)
Provides:       tex(mdpuss8t.tfm)
Provides:       tex(mdpuss8t.vf)
Provides:       tex(mdpussc8c.tfm)
Provides:       tex(mdpussc8c.vf)
Provides:       tex(mdpussc8t.tfm)
Provides:       tex(mdpussc8t.vf)
Provides:       tex(mdpussfc8t.tfm)
Provides:       tex(mdpussfc8t.vf)
Provides:       tex(mdpussi7m.tfm)
Provides:       tex(mdpussi7m.vf)
Provides:       tex(mdpussi7t.tfm)
Provides:       tex(mdpussi7t.vf)
Provides:       tex(mdpussi8c.tfm)
Provides:       tex(mdpussi8c.vf)
Provides:       tex(mdpussi8t.tfm)
Provides:       tex(mdpussi8t.vf)
Provides:       tex(mdpussic8c.tfm)
Provides:       tex(mdpussic8c.vf)
Provides:       tex(mdpussic8t.tfm)
Provides:       tex(mdpussic8t.vf)
Provides:       tex(mdpussifc8t.tfm)
Provides:       tex(mdpussifc8t.vf)
Provides:       tex(mdpussma.tfm)
Provides:       tex(mdpussma.vf)
Provides:       tex(mdpussmb.tfm)
Provides:       tex(mdpussmb.vf)
Provides:       tex(mdput.cfg)
Provides:       tex(mdput.map)
Provides:       tex(mdput.sty)
Provides:       tex(mdputb7m.tfm)
Provides:       tex(mdputb7m.vf)
Provides:       tex(mdputb7t.tfm)
Provides:       tex(mdputb7t.vf)
Provides:       tex(mdputb7v.tfm)
Provides:       tex(mdputb7v.vf)
Provides:       tex(mdputb7y.tfm)
Provides:       tex(mdputb7y.vf)
Provides:       tex(mdputb8c.tfm)
Provides:       tex(mdputb8c.vf)
Provides:       tex(mdputb8t.tfm)
Provides:       tex(mdputb8t.vf)
Provides:       tex(mdputbc8t.tfm)
Provides:       tex(mdputbc8t.vf)
Provides:       tex(mdputbfc8t.tfm)
Provides:       tex(mdputbfc8t.vf)
Provides:       tex(mdputbi7m.tfm)
Provides:       tex(mdputbi7m.vf)
Provides:       tex(mdputbi7t.tfm)
Provides:       tex(mdputbi7t.vf)
Provides:       tex(mdputbi8c.tfm)
Provides:       tex(mdputbi8c.vf)
Provides:       tex(mdputbi8t.tfm)
Provides:       tex(mdputbi8t.vf)
Provides:       tex(mdputbifc8t.tfm)
Provides:       tex(mdputbifc8t.vf)
Provides:       tex(mdputbma.tfm)
Provides:       tex(mdputbma.vf)
Provides:       tex(mdputbmb.tfm)
Provides:       tex(mdputbmb.vf)
Provides:       tex(mdputbo7t.tfm)
Provides:       tex(mdputbo7t.vf)
Provides:       tex(mdputbo8c.tfm)
Provides:       tex(mdputbo8c.vf)
Provides:       tex(mdputbo8t.tfm)
Provides:       tex(mdputbo8t.vf)
Provides:       tex(mdputbofc8t.tfm)
Provides:       tex(mdputbofc8t.vf)
Provides:       tex(mdputr7m.tfm)
Provides:       tex(mdputr7m.vf)
Provides:       tex(mdputr7t.tfm)
Provides:       tex(mdputr7t.vf)
Provides:       tex(mdputr7v.tfm)
Provides:       tex(mdputr7v.vf)
Provides:       tex(mdputr7y.tfm)
Provides:       tex(mdputr7y.vf)
Provides:       tex(mdputr8c.tfm)
Provides:       tex(mdputr8c.vf)
Provides:       tex(mdputr8t.tfm)
Provides:       tex(mdputr8t.vf)
Provides:       tex(mdputrc8t.tfm)
Provides:       tex(mdputrc8t.vf)
Provides:       tex(mdputrfc8t.tfm)
Provides:       tex(mdputrfc8t.vf)
Provides:       tex(mdputri7m.tfm)
Provides:       tex(mdputri7m.vf)
Provides:       tex(mdputri7t.tfm)
Provides:       tex(mdputri7t.vf)
Provides:       tex(mdputri8c.tfm)
Provides:       tex(mdputri8c.vf)
Provides:       tex(mdputri8t.tfm)
Provides:       tex(mdputri8t.vf)
Provides:       tex(mdputrifc8t.tfm)
Provides:       tex(mdputrifc8t.vf)
Provides:       tex(mdputrma.tfm)
Provides:       tex(mdputrma.vf)
Provides:       tex(mdputrmb.tfm)
Provides:       tex(mdputrmb.vf)
Provides:       tex(mdputro7t.tfm)
Provides:       tex(mdputro7t.vf)
Provides:       tex(mdputro8c.tfm)
Provides:       tex(mdputro8c.vf)
Provides:       tex(mdputro8t.tfm)
Provides:       tex(mdputro8t.vf)
Provides:       tex(mdputrofc8t.tfm)
Provides:       tex(mdputrofc8t.vf)
Provides:       tex(mdsffont.def)
Provides:       tex(mdttfont.def)
Provides:       tex(mdugm.cfg)
Provides:       tex(mdugm.map)
Provides:       tex(mdugm.sty)
Provides:       tex(mdugmm7m.tfm)
Provides:       tex(mdugmm7m.vf)
Provides:       tex(mdugmm7t.tfm)
Provides:       tex(mdugmm7t.vf)
Provides:       tex(mdugmm7v.tfm)
Provides:       tex(mdugmm7v.vf)
Provides:       tex(mdugmm7y.tfm)
Provides:       tex(mdugmm7y.vf)
Provides:       tex(mdugmm8c.tfm)
Provides:       tex(mdugmm8c.vf)
Provides:       tex(mdugmm8t.tfm)
Provides:       tex(mdugmm8t.vf)
Provides:       tex(mdugmmfc8t.tfm)
Provides:       tex(mdugmmfc8t.vf)
Provides:       tex(mdugmmi7m.tfm)
Provides:       tex(mdugmmi7m.vf)
Provides:       tex(mdugmmi7t.tfm)
Provides:       tex(mdugmmi7t.vf)
Provides:       tex(mdugmmi8c.tfm)
Provides:       tex(mdugmmi8c.vf)
Provides:       tex(mdugmmi8t.tfm)
Provides:       tex(mdugmmi8t.vf)
Provides:       tex(mdugmmifc8t.tfm)
Provides:       tex(mdugmmifc8t.vf)
Provides:       tex(mdugmmma.tfm)
Provides:       tex(mdugmmma.vf)
Provides:       tex(mdugmmmb.tfm)
Provides:       tex(mdugmmmb.vf)
Provides:       tex(mdugmmo7t.tfm)
Provides:       tex(mdugmmo7t.vf)
Provides:       tex(mdugmmo8c.tfm)
Provides:       tex(mdugmmo8c.vf)
Provides:       tex(mdugmmo8t.tfm)
Provides:       tex(mdugmmo8t.vf)
Provides:       tex(mdugmmofc8t.tfm)
Provides:       tex(mdugmmofc8t.vf)
Provides:       tex(mdugmr7m.tfm)
Provides:       tex(mdugmr7m.vf)
Provides:       tex(mdugmr7t.tfm)
Provides:       tex(mdugmr7t.vf)
Provides:       tex(mdugmr7v.tfm)
Provides:       tex(mdugmr7v.vf)
Provides:       tex(mdugmr7y.tfm)
Provides:       tex(mdugmr7y.vf)
Provides:       tex(mdugmr8c.tfm)
Provides:       tex(mdugmr8c.vf)
Provides:       tex(mdugmr8t.tfm)
Provides:       tex(mdugmr8t.vf)
Provides:       tex(mdugmrfc8t.tfm)
Provides:       tex(mdugmrfc8t.vf)
Provides:       tex(mdugmri7m.tfm)
Provides:       tex(mdugmri7m.vf)
Provides:       tex(mdugmri7t.tfm)
Provides:       tex(mdugmri7t.vf)
Provides:       tex(mdugmri8c.tfm)
Provides:       tex(mdugmri8c.vf)
Provides:       tex(mdugmri8t.tfm)
Provides:       tex(mdugmri8t.vf)
Provides:       tex(mdugmrifc8t.tfm)
Provides:       tex(mdugmrifc8t.vf)
Provides:       tex(mdugmrma.tfm)
Provides:       tex(mdugmrma.vf)
Provides:       tex(mdugmrmb.tfm)
Provides:       tex(mdugmrmb.vf)
Provides:       tex(mdugmro7t.tfm)
Provides:       tex(mdugmro7t.vf)
Provides:       tex(mdugmro8c.tfm)
Provides:       tex(mdugmro8c.vf)
Provides:       tex(mdugmro8t.tfm)
Provides:       tex(mdugmro8t.vf)
Provides:       tex(mdugmrofc8t.tfm)
Provides:       tex(mdugmrofc8t.vf)
Provides:       tex(mdwcib7m.tfm)
Provides:       tex(mdwcib7y.tfm)
Provides:       tex(mdwcib8t.tfm)
Provides:       tex(mdwcibc8t.tfm)
Provides:       tex(mdwcibi7m.tfm)
Provides:       tex(mdwcibi7y.tfm)
Provides:       tex(mdwcibi8t.tfm)
Provides:       tex(mdwcibic8t.tfm)
Provides:       tex(mdwcic7m.tfm)
Provides:       tex(mdwcic7y.tfm)
Provides:       tex(mdwcic8t.tfm)
Provides:       tex(mdwcicc8t.tfm)
Provides:       tex(mdwcici7m.tfm)
Provides:       tex(mdwcici7y.tfm)
Provides:       tex(mdwcici8t.tfm)
Provides:       tex(mdwcicic8t.tfm)
Provides:       tex(mdwcir7m.tfm)
Provides:       tex(mdwcir7y.tfm)
Provides:       tex(mdwcir8t.tfm)
Provides:       tex(mdwcirc8t.tfm)
Provides:       tex(mdwciri7m.tfm)
Provides:       tex(mdwciri7y.tfm)
Provides:       tex(mdwciri8t.tfm)
Provides:       tex(mdwciric8t.tfm)
Provides:       tex(mdwgdb7m.tfm)
Provides:       tex(mdwgdb7y.tfm)
Provides:       tex(mdwgdb8t.tfm)
Provides:       tex(mdwgdbc8t.tfm)
Provides:       tex(mdwgdbi7m.tfm)
Provides:       tex(mdwgdbi7y.tfm)
Provides:       tex(mdwgdbi8t.tfm)
Provides:       tex(mdwgdbic8t.tfm)
Provides:       tex(mdwgdr7m.tfm)
Provides:       tex(mdwgdr7y.tfm)
Provides:       tex(mdwgdr8t.tfm)
Provides:       tex(mdwgdrc8t.tfm)
Provides:       tex(mdwgdri7m.tfm)
Provides:       tex(mdwgdri7y.tfm)
Provides:       tex(mdwgdri8t.tfm)
Provides:       tex(mdwgdric8t.tfm)
Provides:       tex(mdwgds7m.tfm)
Provides:       tex(mdwgds7y.tfm)
Provides:       tex(mdwgds8t.tfm)
Provides:       tex(mdwgdsc8t.tfm)
Provides:       tex(mdwgdsi7m.tfm)
Provides:       tex(mdwgdsi7y.tfm)
Provides:       tex(mdwgdsi8t.tfm)
Provides:       tex(mdwgdsic8t.tfm)
Provides:       tex(mdwusb7m.tfm)
Provides:       tex(mdwusb7y.tfm)
Provides:       tex(mdwusb8t.tfm)
Provides:       tex(mdwusbc8t.tfm)
Provides:       tex(mdwusbi7m.tfm)
Provides:       tex(mdwusbi7y.tfm)
Provides:       tex(mdwusbi8t.tfm)
Provides:       tex(mdwusbic8t.tfm)
Provides:       tex(mdwusr7m.tfm)
Provides:       tex(mdwusr7y.tfm)
Provides:       tex(mdwusr8t.tfm)
Provides:       tex(mdwusrc8t.tfm)
Provides:       tex(mdwusri7m.tfm)
Provides:       tex(mdwusri7y.tfm)
Provides:       tex(mdwusri8t.tfm)
Provides:       tex(mdwusric8t.tfm)
Provides:       tex(mdwuss7m.tfm)
Provides:       tex(mdwuss7y.tfm)
Provides:       tex(mdwuss8t.tfm)
Provides:       tex(mdwussc8t.tfm)
Provides:       tex(mdwussi7m.tfm)
Provides:       tex(mdwussi7y.tfm)
Provides:       tex(mdwussi8t.tfm)
Provides:       tex(mdwussic8t.tfm)
Provides:       tex(mdxcib7t.tfm)
Provides:       tex(mdxcib7y.tfm)
Provides:       tex(mdxcib7y.vf)
Provides:       tex(mdxcib8t.tfm)
Provides:       tex(mdxcib8t.vf)
Provides:       tex(mdxcibc8t.tfm)
Provides:       tex(mdxcibc8t.vf)
Provides:       tex(mdxcibi7t.tfm)
Provides:       tex(mdxcibi7y.tfm)
Provides:       tex(mdxcibi7y.vf)
Provides:       tex(mdxcibi8t.tfm)
Provides:       tex(mdxcibi8t.vf)
Provides:       tex(mdxcibic8t.tfm)
Provides:       tex(mdxcibic8t.vf)
Provides:       tex(mdxcic7t.tfm)
Provides:       tex(mdxcic7y.tfm)
Provides:       tex(mdxcic7y.vf)
Provides:       tex(mdxcic8t.tfm)
Provides:       tex(mdxcic8t.vf)
Provides:       tex(mdxcicc8t.tfm)
Provides:       tex(mdxcicc8t.vf)
Provides:       tex(mdxcici7t.tfm)
Provides:       tex(mdxcici7y.tfm)
Provides:       tex(mdxcici7y.vf)
Provides:       tex(mdxcici8t.tfm)
Provides:       tex(mdxcici8t.vf)
Provides:       tex(mdxcicic8t.tfm)
Provides:       tex(mdxcicic8t.vf)
Provides:       tex(mdxcir7t.tfm)
Provides:       tex(mdxcir7y.tfm)
Provides:       tex(mdxcir7y.vf)
Provides:       tex(mdxcir8t.tfm)
Provides:       tex(mdxcir8t.vf)
Provides:       tex(mdxcirc8t.tfm)
Provides:       tex(mdxcirc8t.vf)
Provides:       tex(mdxciri7t.tfm)
Provides:       tex(mdxciri7y.tfm)
Provides:       tex(mdxciri7y.vf)
Provides:       tex(mdxciri8t.tfm)
Provides:       tex(mdxciri8t.vf)
Provides:       tex(mdxciric8t.tfm)
Provides:       tex(mdxciric8t.vf)
Provides:       tex(mdxgdb7t.tfm)
Provides:       tex(mdxgdb7y.tfm)
Provides:       tex(mdxgdb7y.vf)
Provides:       tex(mdxgdb8t.tfm)
Provides:       tex(mdxgdb8t.vf)
Provides:       tex(mdxgdbc8t.tfm)
Provides:       tex(mdxgdbc8t.vf)
Provides:       tex(mdxgdbi7t.tfm)
Provides:       tex(mdxgdbi7y.tfm)
Provides:       tex(mdxgdbi7y.vf)
Provides:       tex(mdxgdbi8t.tfm)
Provides:       tex(mdxgdbi8t.vf)
Provides:       tex(mdxgdbic8t.tfm)
Provides:       tex(mdxgdbic8t.vf)
Provides:       tex(mdxgdr7t.tfm)
Provides:       tex(mdxgdr7y.tfm)
Provides:       tex(mdxgdr7y.vf)
Provides:       tex(mdxgdr8t.tfm)
Provides:       tex(mdxgdr8t.vf)
Provides:       tex(mdxgdrc8t.tfm)
Provides:       tex(mdxgdrc8t.vf)
Provides:       tex(mdxgdri7t.tfm)
Provides:       tex(mdxgdri7y.tfm)
Provides:       tex(mdxgdri7y.vf)
Provides:       tex(mdxgdri8t.tfm)
Provides:       tex(mdxgdri8t.vf)
Provides:       tex(mdxgdric8t.tfm)
Provides:       tex(mdxgdric8t.vf)
Provides:       tex(mdxgds7t.tfm)
Provides:       tex(mdxgds7y.tfm)
Provides:       tex(mdxgds7y.vf)
Provides:       tex(mdxgds8t.tfm)
Provides:       tex(mdxgds8t.vf)
Provides:       tex(mdxgdsc8t.tfm)
Provides:       tex(mdxgdsc8t.vf)
Provides:       tex(mdxgdsi7t.tfm)
Provides:       tex(mdxgdsi7y.tfm)
Provides:       tex(mdxgdsi7y.vf)
Provides:       tex(mdxgdsi8t.tfm)
Provides:       tex(mdxgdsi8t.vf)
Provides:       tex(mdxgdsic8t.tfm)
Provides:       tex(mdxgdsic8t.vf)
Provides:       tex(mdxusb7t.tfm)
Provides:       tex(mdxusb7y.tfm)
Provides:       tex(mdxusb7y.vf)
Provides:       tex(mdxusb8t.tfm)
Provides:       tex(mdxusb8t.vf)
Provides:       tex(mdxusbc8t.tfm)
Provides:       tex(mdxusbc8t.vf)
Provides:       tex(mdxusbi7t.tfm)
Provides:       tex(mdxusbi7y.tfm)
Provides:       tex(mdxusbi7y.vf)
Provides:       tex(mdxusbi8t.tfm)
Provides:       tex(mdxusbi8t.vf)
Provides:       tex(mdxusbic8t.tfm)
Provides:       tex(mdxusbic8t.vf)
Provides:       tex(mdxusr7t.tfm)
Provides:       tex(mdxusr7y.tfm)
Provides:       tex(mdxusr7y.vf)
Provides:       tex(mdxusr8t.tfm)
Provides:       tex(mdxusr8t.vf)
Provides:       tex(mdxusrc8t.tfm)
Provides:       tex(mdxusrc8t.vf)
Provides:       tex(mdxusri7t.tfm)
Provides:       tex(mdxusri7y.tfm)
Provides:       tex(mdxusri7y.vf)
Provides:       tex(mdxusri8t.tfm)
Provides:       tex(mdxusri8t.vf)
Provides:       tex(mdxusric8t.tfm)
Provides:       tex(mdxusric8t.vf)
Provides:       tex(mdxuss7t.tfm)
Provides:       tex(mdxuss7y.tfm)
Provides:       tex(mdxuss7y.vf)
Provides:       tex(mdxuss8t.tfm)
Provides:       tex(mdxuss8t.vf)
Provides:       tex(mdxussc8t.tfm)
Provides:       tex(mdxussc8t.vf)
Provides:       tex(mdxussi7t.tfm)
Provides:       tex(mdxussi7y.tfm)
Provides:       tex(mdxussi7y.vf)
Provides:       tex(mdxussi8t.tfm)
Provides:       tex(mdxussi8t.vf)
Provides:       tex(mdxussic8t.tfm)
Provides:       tex(mdxussic8t.vf)
Provides:       tex(omlmdbch.fd)
Provides:       tex(omlmdgrb.fd)
Provides:       tex(omlmdgrbc.fd)
Provides:       tex(omlmdgrd.fd)
Provides:       tex(omlmdgrdc.fd)
Provides:       tex(omlmdici.fd)
Provides:       tex(omlmdpgd.fd)
Provides:       tex(omlmdpus.fd)
Provides:       tex(omlmdput.fd)
Provides:       tex(omlmdugm.fd)
Provides:       tex(omsmdbch.fd)
Provides:       tex(omsmdici.fd)
Provides:       tex(omsmdpgd.fd)
Provides:       tex(omsmdpus.fd)
Provides:       tex(omsmdput.fd)
Provides:       tex(omsmdugm.fd)
Provides:       tex(omxmdbch.fd)
Provides:       tex(omxmdici.fd)
Provides:       tex(omxmdpgd.fd)
Provides:       tex(omxmdpus.fd)
Provides:       tex(omxmdput.fd)
Provides:       tex(omxmdugm.fd)
Provides:       tex(ot1mdbch.fd)
Provides:       tex(ot1mdici.fd)
Provides:       tex(ot1mdpgd.fd)
Provides:       tex(ot1mdpus.fd)
Provides:       tex(ot1mdput.fd)
Provides:       tex(ot1mdugm.fd)
Provides:       tex(putb8a.tfm)
Provides:       tex(putb8x.tfm)
Provides:       tex(putbi8a.tfm)
Provides:       tex(putr8a.tfm)
Provides:       tex(putr8x.tfm)
Provides:       tex(putri8a.tfm)
Provides:       tex(t1mdbch.fd)
Provides:       tex(t1mdici.fd)
Provides:       tex(t1mdpgd.fd)
Provides:       tex(t1mdpus.fd)
Provides:       tex(t1mdput.fd)
Provides:       tex(t1mdugm.fd)
Provides:       tex(ts1mdbch.fd)
Provides:       tex(ts1mdici.fd)
Provides:       tex(ts1mdpgd.fd)
Provides:       tex(ts1mdpus.fd)
Provides:       tex(ts1mdput.fd)
Provides:       tex(ts1mdugm.fd)
Provides:       tex(ugmm8a.tfm)
Provides:       tex(ugmmi8a.tfm)
Provides:       tex(ugmr8a.tfm)
Provides:       tex(ugmri8a.tfm)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source204:      mathdesign.tar.xz
Source205:      mathdesign.doc.tar.xz

%description -n texlive-mathdesign
The Math Design project offers free mathematical fonts that
match with existing text fonts. To date, three free font
families are available: Adobe Utopia, URW Garamond and
Bitstream Charter. Three commercial fonts are also supported:
Adobe Garamond Pro, Adobe UtopiaStd and ITC Charter. Mathdesign
covers the whole LaTeX glyph set, including AMS symbols and
some extra. Both roman and bold versions of these symbols can
be used. Moreover you can choose between three greek fonts (two
of them created by the Greek Font Society).

%package -n texlive-mathdesign-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.31svn31639
Release:        0
Summary:        Documentation for texlive-mathdesign
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathdesign-doc
This package includes the documentation for texlive-mathdesign


%package -n texlive-mathdesign-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.31svn31639
Release:        0
Summary:        Severed fonts for texlive-mathdesign
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-mathdesign-fonts
The  separated fonts package for texlive-mathdesign
%post -n texlive-mathdesign
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap mdbch.map' >> /var/run/texlive/run-updmap
echo 'addMap mdgreek.map' >> /var/run/texlive/run-updmap
echo 'addMap mdici.map' >> /var/run/texlive/run-updmap
echo 'addMap mdpgd.map' >> /var/run/texlive/run-updmap
echo 'addMap mdpus.map' >> /var/run/texlive/run-updmap
echo 'addMap mdput.map' >> /var/run/texlive/run-updmap
echo 'addMap mdugm.map' >> /var/run/texlive/run-updmap

%postun -n texlive-mathdesign 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap mdbch.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap mdgreek.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap mdici.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap mdpgd.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap mdpus.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap mdput.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap mdugm.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-mathdesign
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-mathdesign-fonts
%files -n texlive-mathdesign-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/mathdesign/MD-Adobe-Adobe-Garamond-Pro-example.tex
%{_texmfdistdir}/doc/fonts/mathdesign/MD-Adobe-Utopia-Std-example.tex
%{_texmfdistdir}/doc/fonts/mathdesign/MD-Adobe-Utopia-example.pdf
%{_texmfdistdir}/doc/fonts/mathdesign/MD-Adobe-Utopia-example.tex
%{_texmfdistdir}/doc/fonts/mathdesign/MD-Bitstream-Bitstream-Charter-example.pdf
%{_texmfdistdir}/doc/fonts/mathdesign/MD-Bitstream-Bitstream-Charter-example.tex
%{_texmfdistdir}/doc/fonts/mathdesign/MD-itc-Charter-ITC-Std-example.tex
%{_texmfdistdir}/doc/fonts/mathdesign/MD-urw-GaramondNo8-example.tex
%{_texmfdistdir}/doc/fonts/mathdesign/README
%{_texmfdistdir}/doc/fonts/mathdesign/mathdesign-doc.pdf
%{_texmfdistdir}/doc/fonts/mathdesign/mathdesign-doc.tex

%files -n texlive-mathdesign
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/mathdesign/config.mdbch
%{_texmfdistdir}/dvips/mathdesign/config.mdici
%{_texmfdistdir}/dvips/mathdesign/config.mdpgd
%{_texmfdistdir}/dvips/mathdesign/config.mdpus
%{_texmfdistdir}/dvips/mathdesign/config.mdput
%{_texmfdistdir}/dvips/mathdesign/config.mdugm
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_2dncez.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_2rwgaw.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_42s2zl.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_45o73x.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_4b5i6w.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_57soyv.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_csqf63.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_e65dz6.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_g2masa.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_g47ck7.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_ipzj2o.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_kld4uc.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_mdpn2k.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_n2elaj.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_oxfbe4.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_py5znv.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_qnfjtt.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_qzg4u4.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_r2nxhw.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_rl4tn2.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_rxz3ga.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_telfo7.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_uwwzqd.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/a_yezm6g.enc
%{_texmfdistdir}/fonts/enc/dvips/mathdesign/md8x.enc
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdbch.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdgreek.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdici.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdpgd.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdpus.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdput.map
%{_texmfdistdir}/fonts/map/dvips/mathdesign/mdugm.map
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchbc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchbc8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchrc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchrc8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/bchri8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chb7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chb8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbc8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbi8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chbo8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chboc8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chr8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chrc8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chree.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chri8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chro7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chro8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/md-chroc8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchb7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchbofc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchro7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdbch/mdbchrofc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grbb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grbbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grbr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grbri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grdb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grdbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grdr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/md-grdri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbCb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbCbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbCr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbCri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrbri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdCb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdCbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdCri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdrC7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdgreek/mdgrdri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cib7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cib7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cib7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cib7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cib8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cib8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cibee.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cibi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cibi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cibi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cibi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cibma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cibmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cir7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cir7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cir7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cir7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cir8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cir8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-ciree.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-ciri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-ciri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-ciri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-ciri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cirma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/md-cirmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicib7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicib7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicib7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicib7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicib8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicib8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibic8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicibmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicic8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicicc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicicc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicicfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicici8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicici8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicicic8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicicic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicicifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicir7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicir7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicir7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicir7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicir8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicir8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicirc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicirc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicirfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdiciri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdiciri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdiciri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdiciri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdiciric8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdiciric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicirifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicirma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdicirmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcib7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcib7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcib8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcibc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcibi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcibi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcibi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcibic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcic7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcic7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcicc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcici7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcici7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcici8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcicic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcir7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcir7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcir8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwcirc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwciri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwciri7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwciri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdwciric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcib7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcib7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcib8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcibc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcibi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcibi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcibi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcibic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcic7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcic7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcicc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcici7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcici7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcici8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcicic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcir7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcir7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcir8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxcirc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxciri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxciri7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxciri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdici/mdxciric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdree.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gds7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gds7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gds7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gds7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gds8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gds8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdsi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdsi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdsi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdsi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdsma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/md-gdsmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbic8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdbifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdrc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdric8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgds7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgds7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgds7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgds7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgds8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgds8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsic8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdpgdsmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdbi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdbic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdri7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgds7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgds7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgds8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdsc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdsi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdsi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdsi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdwgdsic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdbi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdbic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdri7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgds7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgds7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgds8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdsc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdsi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdsi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdsi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpgd/mdxgdsic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7t5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7t6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7t7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7t8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7t9.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usree.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri7t5.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri7t6.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri7t7.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri7t8.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri7t9.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-usrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-uss7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-uss7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-uss7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-uss7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-uss8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-uss8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-ussi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-ussi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-ussi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-ussi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-ussma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/md-ussmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbic8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusbifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusrc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusric8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpusrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpuss7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpuss7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpuss7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpuss7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpuss8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpuss8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussc8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussic8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdpussmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusbi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusbic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusri7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwusric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwuss7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwuss7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwuss8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwussc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwussi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwussi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwussi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdwussic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusbi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusbic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusri7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxusric8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxuss7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxuss7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxuss8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxussc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxussi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxussi7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxussi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdpus/mdxussic8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utb7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utb8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbee.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbi8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utbo8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utr8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utree.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utri8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utro7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/md-utro8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputb7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputbofc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputro7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/mdputrofc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/putb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/putb8x.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/putbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/putr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/putr8x.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdput/putri8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmm7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmm7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmm7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmm7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmm8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmm8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmm8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmi8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmmo8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmr8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmree.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmri8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmro7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/md-gmro8y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmm7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmm7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmm7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmm7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmm8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmm8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmi7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmo7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmmofc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmr7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmrfc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmri7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmrifc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmrma.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmrmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmro7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/mdugmrofc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/ugmm8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/ugmmi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/ugmr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/mathdesign/mdugm/ugmri8a.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chb7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chb7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chb7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chb7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chb8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chb8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chbi7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chbi7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chbi8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chbi8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chbma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chbmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chr7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chr7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chr7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chr7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chr8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chr8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chree.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chri7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chri7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chri8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chri8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chrma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/md-chrmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/UtopiaStd-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cib7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cib7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cib7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cib7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cib8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cib8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cibee.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cibi7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cibi7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cibi8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cibi8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cibma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cibmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cir7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cir7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cir7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cir7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cir8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cir8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-ciree.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-ciri7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-ciri7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-ciri8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-ciri8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cirma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/md-cirmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdr7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdr7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdr7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdr7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdr8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdr8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdree.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdri7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdri7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdri8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdri8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdrma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdrmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gds7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gds7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gds7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gds7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gds8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gds8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdsi7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdsi7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdsi8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdsi8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdsma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-gdsmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/md-utrma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7t5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7t6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7t7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7t8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7t9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usr8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usree.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri7t5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri7t6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri7t7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri7t8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri7t9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usri8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usrma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-usrmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-uss7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-uss7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-uss7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-uss7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-uss8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-uss8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-ussi7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-ussi7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-ussi8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-ussi8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-ussma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/md-ussmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utb7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utb7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utb7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utb7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utb8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utb8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utbee.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utbi7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utbi7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utbi8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utbi8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utbma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utbmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utr7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utr7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utr7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utr7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utr8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utr8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utree.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utri7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utri7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utri8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utri8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utrma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/md-utrmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmm7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmm7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmm7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmm7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmm8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmm8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmmi7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmmi7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmmi8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmmi8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmmma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmmmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmr7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmr7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmr7v.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmr7y.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmr8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmr8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmree.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmri7m.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmri7t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmri8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmri8t.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmrma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/md-gmrmb.pfb
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchb7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchb7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchb7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchb8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchb8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbi7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbo7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbo8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbo8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchbofc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchr7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchr7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchr7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchr8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchr8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchrc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchrfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchri7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchri8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchrifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchrma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchrmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchro7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchro8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchro8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdbch/mdbchrofc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbCb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbCbi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbCr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbCri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbbi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrbri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdCb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdCbi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdCri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdbi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdrC7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdgreek/mdgrdri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicib7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicib7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicib7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicib7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicib8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicib8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibi7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibic8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibiu7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicibui7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicic8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicicc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicicc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicicfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicici8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicici8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicicic8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicicic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicicifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicir7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicir7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicir7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicir7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicir8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicir8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicirc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicirc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicirfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdiciri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdiciri7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdiciri8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdiciri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdiciric8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdiciric8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicirifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdiciriu7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicirma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicirmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdicirui7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcib7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcib8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcibc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcibi7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcibi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcibic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcic7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcicc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcici7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcici8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcicic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcir7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcir8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxcirc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxciri7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxciri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdici/mdxciric8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdb8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdb8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbic8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdbifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdr7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdr7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdr7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdr8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdr8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdrc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdrc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdrfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdri7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdri8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdric8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdric8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdrifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdrma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdrmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgds7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgds7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgds7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgds7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgds8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgds8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsi7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsic8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdpgdsmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdb7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdb8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdbc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdbi7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdbi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdbic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdr7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdr8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdrc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdri7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdric8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgds7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgds8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdsc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdsi7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdsi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpgd/mdxgdsic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusb8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusb8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbic8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusbifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusr7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusr7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusr7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusr8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusr8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusrc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusrc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusrfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusri7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusri8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusric8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusric8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusrifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusrma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpusrmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpuss7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpuss7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpuss7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpuss7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpuss8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpuss8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussc8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussi7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussic8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdpussmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusb7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusb8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusbc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusbi7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusbi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusbic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusr7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusr8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusrc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusri7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxusric8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxuss7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxuss8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxussc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxussi7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxussi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdpus/mdxussic8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputb7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputb7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputb7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputb8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputb8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbi7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbo7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbo8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbo8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputbofc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputr7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputr7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputr7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputr8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputr8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputrc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputrfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputri7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputri8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputrifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputrma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputrmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputro7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputro8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputro8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdput/mdputrofc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmm7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmm7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmm7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmm7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmm8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmm8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmi7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmi7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmi8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmi8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmo7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmo8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmo8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmmofc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmr7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmr7v.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmr7y.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmr8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmr8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmrfc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmri7m.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmri7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmri8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmri8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmrifc8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmrma.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmrmb.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmro7t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmro8c.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmro8t.vf
%{_texmfdistdir}/fonts/vf/public/mathdesign/mdugm/mdugmrofc8t.vf
%{_texmfdistdir}/tex/latex/mathdesign/mathdesign.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdacmr.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdamdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdbch.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdbch.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/mdbmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/omlmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/omsmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/omxmdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/ot1mdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/t1mdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbch/ts1mdbch.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdbcmr.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdfont.def
%{_texmfdistdir}/tex/latex/mathdesign/mdici/mdamdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdici/mdbmdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdici/mdici.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdici/mdici.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdici/omlmdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdici/omsmdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdici/omxmdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdici/ot1mdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdici/t1mdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdici/ts1mdici.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/mdamdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/mdbmdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/mdpgd.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/mdpgd.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/omlmdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/omsmdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/omxmdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/ot1mdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/t1mdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpgd/ts1mdpgd.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/mdamdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/mdbmdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/mdpus.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/mdpus.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/omlmdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/omsmdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/omxmdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/ot1mdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/t1mdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdpus/ts1mdpus.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdamdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdbmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdput.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdput/mdput.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdput/omlmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/omsmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/omxmdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/ot1mdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/t1mdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdput/ts1mdput.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdsffont.def
%{_texmfdistdir}/tex/latex/mathdesign/mdttfont.def
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdamdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdbmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdugm.cfg
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/mdugm.sty
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/omlmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/omsmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/omxmdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/ot1mdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/t1mdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/mdugm/ts1mdugm.fd
%{_texmfdistdir}/tex/latex/mathdesign/omlmdgrb.fd
%{_texmfdistdir}/tex/latex/mathdesign/omlmdgrbc.fd
%{_texmfdistdir}/tex/latex/mathdesign/omlmdgrd.fd
%{_texmfdistdir}/tex/latex/mathdesign/omlmdgrdc.fd

%files -n texlive-mathdesign-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-mathdesign
%{_datadir}/fontconfig/conf.avail/58-texlive-mathdesign.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathdesign/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathdesign/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathdesign/fonts.scale
%{_datadir}/fonts/texlive-mathdesign/md-chb7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chb7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chb7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chb7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chb8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chb8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chbi7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chbi7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chbi8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chbi8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chbma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chbmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chr7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chr7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chr7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chr7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chr8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chr8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chree.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chri7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chri7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chri8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chri8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chrma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-chrmb.pfb
%{_datadir}/fonts/texlive-mathdesign/UtopiaStd-Regular.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cib7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cib7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cib7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cib7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cib8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cib8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cibee.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cibi7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cibi7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cibi8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cibi8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cibma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cibmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cir7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cir7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cir7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cir7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cir8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cir8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ciree.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ciri7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ciri7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ciri8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ciri8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cirma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-cirmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdr7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdr7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdr7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdr7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdr8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdr8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdree.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdri7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdri7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdri8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdri8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdrma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdrmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gds7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gds7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gds7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gds7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gds8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gds8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdsi7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdsi7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdsi8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdsi8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdsma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gdsmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utrma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7t5.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7t6.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7t7.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7t8.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7t9.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usr8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usree.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri7t5.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri7t6.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri7t7.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri7t8.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri7t9.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usri8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usrma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-usrmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-uss7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-uss7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-uss7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-uss7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-uss8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-uss8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ussi7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ussi7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ussi8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ussi8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ussma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-ussmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utb7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utb7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utb7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utb7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utb8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utb8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utbee.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utbi7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utbi7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utbi8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utbi8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utbma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utbmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utr7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utr7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utr7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utr7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utr8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utr8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utree.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utri7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utri7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utri8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utri8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utrma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-utrmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmm7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmm7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmm7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmm7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmm8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmm8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmmi7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmmi7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmmi8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmmi8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmmma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmmmb.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmr7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmr7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmr7v.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmr7y.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmr8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmr8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmree.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmri7m.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmri7t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmri8c.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmri8t.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmrma.pfb
%{_datadir}/fonts/texlive-mathdesign/md-gmrmb.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathdesign-fonts-%{texlive_version}.%{texlive_noarch}.2.31svn31639-%{release}-zypper
%endif

%package -n texlive-mathdots
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn34301
Release:        0
Summary:        Commands to produce dots in math that respect font size
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathdots-doc >= %{texlive_version}
Provides:       tex(mathdots.sty)
Provides:       tex(mathdots.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source206:      mathdots.tar.xz
Source207:      mathdots.doc.tar.xz

%description -n texlive-mathdots
Redefines \ddots and \vdots, and defines \iddots. The dots
produced by \iddots slant in the opposite direction to \ddots.
All the commands are designed to change size appropriately in
scripts, as well as in response to LaTeX size changing
commands. The commands may also be used in plain TeX.

%package -n texlive-mathdots-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn34301
Release:        0
Summary:        Documentation for texlive-mathdots
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathdots-doc
This package includes the documentation for texlive-mathdots

%post -n texlive-mathdots
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathdots 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathdots
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathdots-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/mathdots/README
%{_texmfdistdir}/doc/generic/mathdots/mathdots.pdf
%{_texmfdistdir}/doc/generic/mathdots/mdotest.pdf
%{_texmfdistdir}/doc/generic/mathdots/mdotest.tex
%{_texmfdistdir}/doc/generic/mathdots/plmdotest.tex

%files -n texlive-mathdots
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/mathdots/mathdots.sty
%{_texmfdistdir}/tex/generic/mathdots/mathdots.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathdots-%{texlive_version}.%{texlive_noarch}.0.0.9svn34301-%{release}-zypper
%endif

%package -n texlive-mathexam
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn15878
Release:        0
Summary:        Package for typesetting exams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathexam-doc >= %{texlive_version}
Provides:       tex(mathexam.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lastpage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source208:      mathexam.tar.xz
Source209:      mathexam.doc.tar.xz

%description -n texlive-mathexam
The package can help you typeset exams (mostly in mathematics
and related disciplines where students are required to show
their calculations followed by one or more short answers). It
provides commands for inclusion of space for calculations, as
well as commands for automatic creation of "answer spaces". In
addition, the package will automatically create page headers
and footers, and will let you include instructions and space
for students to put their name.

%package -n texlive-mathexam-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn15878
Release:        0
Summary:        Documentation for texlive-mathexam
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathexam-doc
This package includes the documentation for texlive-mathexam

%post -n texlive-mathexam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathexam 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathexam
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathexam-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathexam/README
%{_texmfdistdir}/doc/latex/mathexam/mathexam.pdf
%{_texmfdistdir}/doc/latex/mathexam/sample.pdf
%{_texmfdistdir}/doc/latex/mathexam/sample.tex

%files -n texlive-mathexam
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathexam/mathexam.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathexam-%{texlive_version}.%{texlive_noarch}.1.00svn15878-%{release}-zypper
%endif

%package -n texlive-mathfam256
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn53519
Release:        0
Summary:        Extend math family up to 256 for pLaTeX/upLaTeX/Lamed
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathfam256-doc >= %{texlive_version}
Provides:       tex(mathfam256.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source210:      mathfam256.tar.xz
Source211:      mathfam256.doc.tar.xz

%description -n texlive-mathfam256
This package increases the upper limit of math symbols up to
256, using \omath... primitives. These primitives were
originally introduced in Omega and are currently available in
the following formats: pLaTeX (runs on e-pTeX), upLaTeX (runs
on e-upTeX), Lamed (runs on Aleph, successor of Omega).

%package -n texlive-mathfam256-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn53519
Release:        0
Summary:        Documentation for texlive-mathfam256
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathfam256-doc
This package includes the documentation for texlive-mathfam256

%post -n texlive-mathfam256
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathfam256 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathfam256
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathfam256-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathfam256/LICENSE
%{_texmfdistdir}/doc/latex/mathfam256/README.md
%{_texmfdistdir}/doc/latex/mathfam256/mathfam256.pdf
%{_texmfdistdir}/doc/latex/mathfam256/mathfam256.tex

%files -n texlive-mathfam256
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathfam256/mathfam256.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathfam256-%{texlive_version}.%{texlive_noarch}.0.0.5svn53519-%{release}-zypper
%endif

%package -n texlive-mathfixs
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn49547
Release:        0
Summary:        Fix various layout issues in math mode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathfixs-doc >= %{texlive_version}
Provides:       tex(mathfixs.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source212:      mathfixs.tar.xz
Source213:      mathfixs.doc.tar.xz

%description -n texlive-mathfixs
This is a LaTeX2e package to fix some odd behaviour in math
mode such as spacing around fractions and roots, math symbols
within bold text as well as capital Greek letters. It also adds
some related macros.

%package -n texlive-mathfixs-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn49547
Release:        0
Summary:        Documentation for texlive-mathfixs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathfixs-doc
This package includes the documentation for texlive-mathfixs

%post -n texlive-mathfixs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathfixs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathfixs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathfixs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathfixs/README.txt
%{_texmfdistdir}/doc/latex/mathfixs/mafxsamp.tex
%{_texmfdistdir}/doc/latex/mathfixs/mathfixs.pdf

%files -n texlive-mathfixs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathfixs/mathfixs.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathfixs-%{texlive_version}.%{texlive_noarch}.1.01svn49547-%{release}-zypper
%endif

%package -n texlive-mathfont
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn53035
Release:        0
Summary:        Use TrueType and OpenType fonts in math mode
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathfont-doc >= %{texlive_version}
Provides:       tex(mathfont.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(fontspec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source214:      mathfont.tar.xz
Source215:      mathfont.doc.tar.xz

%description -n texlive-mathfont
This package provides a flexible interface for changing the
font of math mode characters. The package allows the user to
specify a default unicode font for each of six basic classes of
Latin and Greek characters, and it provides additional support
for unicode alphanumeric symbols. Crucially, mathfont is
compatible with both LuaLaTeX and XeLaTeX, and it provides
several font-loading commands that allow the user to change
fonts locally or for individual symbols within math mode.

%package -n texlive-mathfont-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn53035
Release:        0
Summary:        Documentation for texlive-mathfont
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathfont-doc
This package includes the documentation for texlive-mathfont

%post -n texlive-mathfont
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathfont 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathfont
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathfont-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathfont/README.txt
%{_texmfdistdir}/doc/latex/mathfont/mathfont_code.pdf
%{_texmfdistdir}/doc/latex/mathfont/mathfont_doc_patch.tex
%{_texmfdistdir}/doc/latex/mathfont/mathfont_heading.tex
%{_texmfdistdir}/doc/latex/mathfont/mathfont_index_warning.tex
%{_texmfdistdir}/doc/latex/mathfont/mathfont_symbol_list.pdf
%{_texmfdistdir}/doc/latex/mathfont/mathfont_symbol_list.tex
%{_texmfdistdir}/doc/latex/mathfont/mathfont_user_guide.pdf
%{_texmfdistdir}/doc/latex/mathfont/mathfont_user_guide.tex

%files -n texlive-mathfont
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathfont/mathfont.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathfont-%{texlive_version}.%{texlive_noarch}.1.6svn53035-%{release}-zypper
%endif

%package -n texlive-mathlig
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54244
Release:        0
Summary:        Define maths "ligatures"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(mathlig.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source216:      mathlig.tar.xz

%description -n texlive-mathlig
The package defines character sequences that "behave like"
ligatures, in maths mode. Example definitions (chosen to show
the package's flexibility, are: \mathlig{->}{\rightarrow}
\mathlig{<-}{\leftarrow} \mathlig{<->}{\leftrightarrow}
%post -n texlive-mathlig
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathlig 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathlig
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathlig
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/mathlig/mathlig.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathlig-%{texlive_version}.%{texlive_noarch}.1.0svn54244-%{release}-zypper
%endif

%package -n texlive-mathpartir
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn39864
Release:        0
Summary:        Typesetting sequences of math formulas, e.g. type inference rules
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathpartir-doc >= %{texlive_version}
Provides:       tex(mathpartir.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source217:      mathpartir.tar.xz
Source218:      mathpartir.doc.tar.xz

%description -n texlive-mathpartir
The package provides macros for typesetting math formulas in
mixed horizontal and vertical mode, automatically as best fit.
It provides an environment mathpar that behaves much as a loose
centered paragraph where words are math formulas, and spaces
between them are larger and adjustable. It also provides a
macro \inferrule for typeseting fractions where both the
numerator and denominator may be sequences of formulas that
will be also typeset in a similar way. It can typically be used
for typeseting sets of type inference rules or typing
derivations. A macro inferrule for typesetting type inference
rules.

%package -n texlive-mathpartir-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn39864
Release:        0
Summary:        Documentation for texlive-mathpartir
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathpartir-doc
This package includes the documentation for texlive-mathpartir

%post -n texlive-mathpartir
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathpartir 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathpartir
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathpartir-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathpartir/COPYING
%{_texmfdistdir}/doc/latex/mathpartir/README
%{_texmfdistdir}/doc/latex/mathpartir/mathpartir.pdf

%files -n texlive-mathpartir
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathpartir/mathpartir.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathpartir-%{texlive_version}.%{texlive_noarch}.1.3.2svn39864-%{release}-zypper
%endif

%package -n texlive-mathpazo
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn52663
Release:        0
Summary:        Fonts to typeset mathematics to match Palatino
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-fpl >= %{texlive_version}
#!BuildIgnore: texlive-fpl
Requires:       texlive-palatino >= %{texlive_version}
#!BuildIgnore: texlive-palatino
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-mathpazo-fonts >= %{texlive_version}
Recommends:     texlive-mathpazo-doc >= %{texlive_version}
Provides:       tex(fplmb.tfm)
Provides:       tex(fplmbb.tfm)
Provides:       tex(fplmbi.tfm)
Provides:       tex(fplmr.tfm)
Provides:       tex(fplmri.tfm)
Provides:       tex(zplmb7m.tfm)
Provides:       tex(zplmb7m.vf)
Provides:       tex(zplmb7t.tfm)
Provides:       tex(zplmb7t.vf)
Provides:       tex(zplmb7y.tfm)
Provides:       tex(zplmb7y.vf)
Provides:       tex(zplmr7m.tfm)
Provides:       tex(zplmr7m.vf)
Provides:       tex(zplmr7t.tfm)
Provides:       tex(zplmr7t.vf)
Provides:       tex(zplmr7v.tfm)
Provides:       tex(zplmr7v.vf)
Provides:       tex(zplmr7y.tfm)
Provides:       tex(zplmr7y.vf)
Requires:       tex(cmbsy10.tfm)
Requires:       tex(cmbx10.tfm)
Requires:       tex(cmex10.tfm)
Requires:       tex(cmmi10.tfm)
Requires:       tex(cmmib10.tfm)
Requires:       tex(cmr10.tfm)
Requires:       tex(cmsy10.tfm)
Requires:       tex(pplb8r.tfm)
Requires:       tex(pplbi8r.tfm)
Requires:       tex(pplr8r.tfm)
Requires:       tex(pplri8r.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source219:      mathpazo.tar.xz
Source220:      mathpazo.doc.tar.xz

%description -n texlive-mathpazo
The Pazo Math fonts are a family of PostScript fonts suitable
for typesetting mathematics in combination with the Palatino
family of text fonts. The Pazo Math family is made up of five
fonts provided in Adobe Type 1 format (PazoMath,
PazoMath-Italic, PazoMath-Bold, PazoMath-BoldItalic, and
PazoMathBlackboardBold). These contain, in designs that match
Palatino, glyphs that are usually not available in Palatino and
for which Computer Modern looks odd when combined with
Palatino. These glyphs include the uppercase Greek alphabet in
upright and slanted shapes in regular and bold weights, the
lowercase Greek alphabet in slanted shape in regular and bold
weights, several mathematical glyphs (partialdiff, summation,
product, coproduct, emptyset, infinity, and proportional) in
regular and bold weights, other glyphs (Euro and dotlessj) in
upright and slanted shapes in regular and bold weights, and the
uppercase letters commonly used to represent various number
sets (C, I, N, Q, R, and Z) in blackboard bold. LaTeX macro
support (using package mathpazo.sty) is provided in psnfss (a
required part of any LaTeX distribution).

%package -n texlive-mathpazo-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn52663
Release:        0
Summary:        Documentation for texlive-mathpazo
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathpazo-doc
This package includes the documentation for texlive-mathpazo


%package -n texlive-mathpazo-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn52663
Release:        0
Summary:        Severed fonts for texlive-mathpazo
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-mathpazo-fonts
The  separated fonts package for texlive-mathpazo
%post -n texlive-mathpazo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathpazo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathpazo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-mathpazo-fonts
%files -n texlive-mathpazo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathpazo/README.txt
%{_texmfdistdir}/doc/latex/mathpazo/gpl.txt
%{_texmfdistdir}/doc/latex/mathpazo/mapfplm.tex
%{_texmfdistdir}/doc/latex/mathpazo/mapppl.tex
%{_texmfdistdir}/doc/latex/mathpazo/mapzplm.tex
%{_texmfdistdir}/doc/latex/mathpazo/pazofnst.tex
%{_texmfdistdir}/doc/latex/mathpazo/pazotest.pdf

%files -n texlive-mathpazo
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmb.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmbb.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmbi.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmr.afm
%{_texmfdistdir}/fonts/afm/public/mathpazo/fplmri.afm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmbb.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmr.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/fplmri.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmb7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmb7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmb7y.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7m.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7v.tfm
%{_texmfdistdir}/fonts/tfm/public/mathpazo/zplmr7y.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathpazo/fplmb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathpazo/fplmbb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathpazo/fplmbi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathpazo/fplmr.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mathpazo/fplmri.pfb
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmb7m.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmb7t.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmb7y.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7m.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7t.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7v.vf
%{_texmfdistdir}/fonts/vf/public/mathpazo/zplmr7y.vf

%files -n texlive-mathpazo-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-mathpazo
%{_datadir}/fontconfig/conf.avail/58-texlive-mathpazo.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathpazo/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathpazo/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mathpazo/fonts.scale
%{_datadir}/fonts/texlive-mathpazo/fplmb.pfb
%{_datadir}/fonts/texlive-mathpazo/fplmbb.pfb
%{_datadir}/fonts/texlive-mathpazo/fplmbi.pfb
%{_datadir}/fonts/texlive-mathpazo/fplmr.pfb
%{_datadir}/fonts/texlive-mathpazo/fplmri.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathpazo-fonts-%{texlive_version}.%{texlive_noarch}.1.003svn52663-%{release}-zypper
%endif

%package -n texlive-mathpunctspace
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46754
Release:        0
Summary:        Control the space after punctuation in math expressions
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathpunctspace-doc >= %{texlive_version}
Provides:       tex(mathpunctspace.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source221:      mathpunctspace.tar.xz
Source222:      mathpunctspace.doc.tar.xz

%description -n texlive-mathpunctspace
This package provides a mechanism to control the space after
commas and semicolons in mathematical expressions.

%package -n texlive-mathpunctspace-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46754
Release:        0
Summary:        Documentation for texlive-mathpunctspace
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathpunctspace-doc
This package includes the documentation for texlive-mathpunctspace

%post -n texlive-mathpunctspace
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathpunctspace 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathpunctspace
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathpunctspace-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathpunctspace/README.md
%{_texmfdistdir}/doc/latex/mathpunctspace/comma0mu-semicolonnat-colonnat.pdf
%{_texmfdistdir}/doc/latex/mathpunctspace/comma10mu-semicolon20mu-colon30mu.pdf
%{_texmfdistdir}/doc/latex/mathpunctspace/comma5pt-semicolon5pt-colon5pt.pdf
%{_texmfdistdir}/doc/latex/mathpunctspace/latexorg.pdf
%{_texmfdistdir}/doc/latex/mathpunctspace/mathpunctspace.pdf
%{_texmfdistdir}/doc/latex/mathpunctspace/mathpunctspace.tex

%files -n texlive-mathpunctspace
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathpunctspace/mathpunctspace.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathpunctspace-%{texlive_version}.%{texlive_noarch}.1.1svn46754-%{release}-zypper
%endif

%package -n texlive-maths-symbols
Version:        %{texlive_version}.%{texlive_noarch}.3.4svn37763
Release:        0
Summary:        Summary of mathematical symbols available in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source223:      maths-symbols.doc.tar.xz

%description -n texlive-maths-symbols
A predecessor of the comprehensive symbols list, covering
mathematical symbols available in standard LaTeX (including the
AMS symbols, if available at compile time).
%post -n texlive-maths-symbols
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-maths-symbols 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-maths-symbols
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-maths-symbols
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/maths-symbols/README
%{_texmfdistdir}/doc/latex/maths-symbols/maths-symbols.pdf
%{_texmfdistdir}/doc/latex/maths-symbols/maths-symbols.tex
%{_texmfdistdir}/doc/latex/maths-symbols/scriptfonts.pdf
%{_texmfdistdir}/doc/latex/maths-symbols/scriptfonts.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-maths-symbols-%{texlive_version}.%{texlive_noarch}.3.4svn37763-%{release}-zypper
%endif

%package -n texlive-mathspec
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2bsvn42773
Release:        0
Summary:        Specify arbitrary fonts for mathematics in XeTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathspec-doc >= %{texlive_version}
Provides:       tex(mathspec.sty)
Requires:       tex(MnSymbol.sty)
Requires:       tex(amstext.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source224:      mathspec.tar.xz
Source225:      mathspec.doc.tar.xz

%description -n texlive-mathspec
The mathspec package provides an interface to typeset
mathematics in XeLaTeX with arbitrary text fonts using fontspec
as a backend. The package is under development and later
versions might to be incompatible with this version, as this
version is incompatible with earlier versions. The package
requires at least version 0.9995 of XeTeX.

%package -n texlive-mathspec-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2bsvn42773
Release:        0
Summary:        Documentation for texlive-mathspec
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathspec-doc
This package includes the documentation for texlive-mathspec

%post -n texlive-mathspec
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathspec 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathspec
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathspec-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/mathspec/README.txt
%{_texmfdistdir}/doc/xelatex/mathspec/mathspec.pdf
%{_texmfdistdir}/doc/xelatex/mathspec/mathspec.tex

%files -n texlive-mathspec
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/mathspec/mathspec.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathspec-%{texlive_version}.%{texlive_noarch}.0.0.2bsvn42773-%{release}-zypper
%endif

%package -n texlive-mathspic
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn31957
Release:        0
Summary:        A Perl filter program for use with PiCTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-mathspic-bin >= %{texlive_version}
#!BuildIgnore: texlive-mathspic-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathspic-doc >= %{texlive_version}
Requires:       perl(Math::Trig)
#!BuildIgnore:  perl(Math::Trig)
Requires:       perl(constant)
#!BuildIgnore:  perl(constant)
Provides:       tex(mathspic.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source226:      mathspic.tar.xz
Source227:      mathspic.doc.tar.xz

%description -n texlive-mathspic
MathsPIC(Perl) is a development of the earlier MathsPIC(DOS)
program, now implemented as a Perl script, being much more
portable than the earlier program. MathsPIC parses a plain text
input file and generates a plain text output-file containing
commands for drawing a diagram. Version 1.0 produces output
containing PiCTeX and (La)TeX commands, which may then be
processed by plain TeX or LaTeX in the usual way. MathsPIC also
outputs a comprehensive log-file. MathsPIC facilitates creating
figures using PiCTeX by providing an environment for
manipulating named points and also allows the use of variables
and maths (advance, multiply, and divide)--in short--it takes
the pain out of PiCTeX. Both the original DOS version and the
new Perl version are available.

%package -n texlive-mathspic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn31957
Release:        0
Summary:        Documentation for texlive-mathspic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(mathspic.1)

%description -n texlive-mathspic-doc
This package includes the documentation for texlive-mathspic

%post -n texlive-mathspic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathspic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathspic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathspic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathspic/HELP.txt
%{_texmfdistdir}/doc/latex/mathspic/README.txt
%{_texmfdistdir}/doc/latex/mathspic/grabtexdata.tex
%{_texmfdistdir}/doc/latex/mathspic/mathsPICfigures.zip
%{_texmfdistdir}/doc/latex/mathspic/mathsPICmanual.pdf
%{_texmfdistdir}/doc/latex/mathspic/mathsPICmanual.zip
%{_texmfdistdir}/doc/latex/mathspic/mathspic.lib
%{_texmfdistdir}/doc/latex/mathspic/mathspic.sh
%{_texmfdistdir}/doc/latex/mathspic/sourcecode113.html
%{_texmfdistdir}/doc/latex/mathspic/sourcecode113.nw
%{_texmfdistdir}/doc/latex/mathspic/sourcecode113.pdf
%{_mandir}/man1/mathspic.1*

%files -n texlive-mathspic
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/mathspic/mathspic.pl
%{_texmfdistdir}/tex/latex/mathspic/mathspic.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathspic-%{texlive_version}.%{texlive_noarch}.1.13svn31957-%{release}-zypper
%endif

%package -n texlive-mathtools
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn54516
Release:        0
Summary:        Mathematical tools to use with amsmath
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mathtools-doc >= %{texlive_version}
Provides:       tex(empheq.sty)
Provides:       tex(mathtools.sty)
Provides:       tex(mhsetup.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source228:      mathtools.tar.xz
Source229:      mathtools.doc.tar.xz

%description -n texlive-mathtools
Mathtools provides a series of packages designed to enhance the
appearance of documents containing a lot of mathematics. The
main backbone is amsmath, so those unfamiliar with this
required part of the LaTeX system will probably not find the
packages very useful. Mathtools provides many useful tools for
mathematical typesetting. It is based on amsmath and fixes
various deficiencies of amsmath and standard LaTeX. It
provides Extensible symbols, such as brackets, arrows,
harpoons, etc.; Various symbols such as \coloneqq (:=); Easy
creation of new tag forms; Showing equation numbers only for
referenced equations; Extensible arrows, harpoons and
hookarrows; Starred versions of the amsmath matrix environments
for specifying the column alignment; More building blocks:
multlined, cases-like environments, new gathered environments;
Maths versions of \makebox, \llap, \rlap etc.; Cramped math
styles; and more... Mathtools requires mhsetup.

%package -n texlive-mathtools-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn54516
Release:        0
Summary:        Documentation for texlive-mathtools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mathtools-doc
This package includes the documentation for texlive-mathtools

%post -n texlive-mathtools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mathtools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mathtools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mathtools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mathtools/README.md
%{_texmfdistdir}/doc/latex/mathtools/empheq.pdf
%{_texmfdistdir}/doc/latex/mathtools/mathtools.pdf
%{_texmfdistdir}/doc/latex/mathtools/mhsetup.pdf

%files -n texlive-mathtools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mathtools/empheq.sty
%{_texmfdistdir}/tex/latex/mathtools/mathtools.sty
%{_texmfdistdir}/tex/latex/mathtools/mhsetup.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mathtools-%{texlive_version}.%{texlive_noarch}.1.24svn54516-%{release}-zypper
%endif

%package -n texlive-matlab-prettifier
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn34323
Release:        0
Summary:        Pretty-print Matlab source code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-matlab-prettifier-doc >= %{texlive_version}
Provides:       tex(matlab-prettifier.sty)
Requires:       tex(listings.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source230:      matlab-prettifier.tar.xz
Source231:      matlab-prettifier.doc.tar.xz

%description -n texlive-matlab-prettifier
The package extends the facilities of the listings package, to
pretty-print Matlab and Octave source code. (Note that support
of Octave syntax is not complete.)

%package -n texlive-matlab-prettifier-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn34323
Release:        0
Summary:        Documentation for texlive-matlab-prettifier
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-matlab-prettifier-doc
This package includes the documentation for texlive-matlab-prettifier

%post -n texlive-matlab-prettifier
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-matlab-prettifier 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-matlab-prettifier
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-matlab-prettifier-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/matlab-prettifier/README
%{_texmfdistdir}/doc/latex/matlab-prettifier/matlab-prettifier.pdf

%files -n texlive-matlab-prettifier
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/matlab-prettifier/matlab-prettifier.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-matlab-prettifier-%{texlive_version}.%{texlive_noarch}.0.0.3svn34323-%{release}-zypper
%endif

%package -n texlive-matrix-skeleton
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        A PGF/TikZ library that simplifies working with multiple matrix nodes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-matrix-skeleton-doc >= %{texlive_version}
Provides:       tex(pgflibrarymatrix.skeleton.code.tex)
Provides:       tex(tikzlibrarymatrix.skeleton.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source232:      matrix-skeleton.tar.xz
Source233:      matrix-skeleton.doc.tar.xz

%description -n texlive-matrix-skeleton
The package provides a PGF/TikZ library that simplifies working
with multiple matrix nodes. To do so, it correctly aligns
groups of nodes with the content of the whole matrix.
Furthermore, matrix.skeleton provides rows and columns for easy
styling.

%package -n texlive-matrix-skeleton-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Documentation for texlive-matrix-skeleton
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-matrix-skeleton-doc
This package includes the documentation for texlive-matrix-skeleton

%post -n texlive-matrix-skeleton
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-matrix-skeleton 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-matrix-skeleton
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-matrix-skeleton-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/matrix-skeleton/LICENSE
%{_texmfdistdir}/doc/latex/matrix-skeleton/README.md
%{_texmfdistdir}/doc/latex/matrix-skeleton/example.pdf
%{_texmfdistdir}/doc/latex/matrix-skeleton/example.tex
%{_texmfdistdir}/doc/latex/matrix-skeleton/manual.pdf
%{_texmfdistdir}/doc/latex/matrix-skeleton/manual.tex

%files -n texlive-matrix-skeleton
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/matrix-skeleton/pgflibrarymatrix.skeleton.code.tex
%{_texmfdistdir}/tex/latex/matrix-skeleton/tikzlibrarymatrix.skeleton.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-matrix-skeleton-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif

%package -n texlive-mattens
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn17582
Release:        0
Summary:        Matrices/tensor typesetting
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mattens-doc >= %{texlive_version}
Provides:       tex(mattens.sty)
Requires:       tex(amsmath.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source234:      mattens.tar.xz
Source235:      mattens.doc.tar.xz

%description -n texlive-mattens
The mattens package contains the definitions to typeset
matrices, vectors and tensors as used in the engineering
community for the representation of common vectors and tensors
such as forces, velocities, moments of inertia, etc.

%package -n texlive-mattens-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn17582
Release:        0
Summary:        Documentation for texlive-mattens
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mattens-doc
This package includes the documentation for texlive-mattens

%post -n texlive-mattens
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mattens 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mattens
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mattens-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mattens/README
%{_texmfdistdir}/doc/latex/mattens/mattens.pdf
%{_texmfdistdir}/doc/latex/mattens/mattens_sample.pdf
%{_texmfdistdir}/doc/latex/mattens/mattens_sample_src.zip

%files -n texlive-mattens
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mattens/mattens.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mattens-%{texlive_version}.%{texlive_noarch}.1.3svn17582-%{release}-zypper
%endif

%package -n texlive-maybemath
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Make math bold or italic according to context
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-maybemath-doc >= %{texlive_version}
Provides:       tex(maybemath.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(bm.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source236:      maybemath.tar.xz
Source237:      maybemath.doc.tar.xz

%description -n texlive-maybemath
The \maybebm and \maybeit macros can be used in maths
expressions to make the arguments typeset as bold or italic
respectively if the surrounding context is appropriate. They
are useful for writing user macros for use in general contexts.
\maybebm is especially appropriate when section titles contain
math expressions, since the title will appear bold but the
header and table of contents usually replicate the title in
normal width. It uses the bm package to make things bold
\maybeit performs a similar role to \mathrm{} but the maths
expression will be italicised if the surrounding text is.
\maybeitsubscript is provided to shift subscripts to the left
if the expression is italicised.

%package -n texlive-maybemath-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-maybemath
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-maybemath-doc
This package includes the documentation for texlive-maybemath

%post -n texlive-maybemath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-maybemath 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-maybemath
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-maybemath-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/maybemath/README
%{_texmfdistdir}/doc/latex/maybemath/maybemath.pdf
%{_texmfdistdir}/doc/latex/maybemath/maybemath.tex

%files -n texlive-maybemath
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/maybemath/maybemath.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-maybemath-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-mcaption
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Put captions in the margin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mcaption-doc >= %{texlive_version}
Provides:       tex(mcaption.sty)
Requires:       tex(changepage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source238:      mcaption.tar.xz
Source239:      mcaption.doc.tar.xz

%description -n texlive-mcaption
The mcaption package provides an mcaption environment which
puts figure or table captions in the margin. The package works
with the standard classes and with the KOMA-Script document
classes scrartcl, scrreprt and scrbook. The package requires
the changepage package.

%package -n texlive-mcaption-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Documentation for texlive-mcaption
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mcaption-doc
This package includes the documentation for texlive-mcaption

%post -n texlive-mcaption
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mcaption 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mcaption
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mcaption-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mcaption/CHANGES
%{_texmfdistdir}/doc/latex/mcaption/README
%{_texmfdistdir}/doc/latex/mcaption/example.tex
%{_texmfdistdir}/doc/latex/mcaption/mcaption.pdf

%files -n texlive-mcaption
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mcaption/mcaption.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mcaption-%{texlive_version}.%{texlive_noarch}.3.0svn15878-%{release}-zypper
%endif

%package -n texlive-mceinleger
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Creating covers for music cassettes
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mceinleger-doc >= %{texlive_version}
Provides:       tex(mceinleger.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source240:      mceinleger.tar.xz
Source241:      mceinleger.doc.tar.xz

%description -n texlive-mceinleger
A package for creating MC-covers on your own. It allows the
creation of simple covers as well as covers with an additional
page for more information about the cassette (table of contents
e.g.). The rotating package is required.

%package -n texlive-mceinleger-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-mceinleger
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mceinleger-doc
This package includes the documentation for texlive-mceinleger

%post -n texlive-mceinleger
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mceinleger 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mceinleger
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mceinleger-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mceinleger/mceinleger.pdf
%{_texmfdistdir}/doc/latex/mceinleger/mceinleger.tex

%files -n texlive-mceinleger
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mceinleger/mceinleger.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mceinleger-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-mcexam
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn46155
Release:        0
Summary:        Create randomized Multiple Choice questions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mcexam-doc >= %{texlive_version}
Provides:       tex(mcexam.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(longtable.sty)
Requires:       tex(newfile.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source242:      mcexam.tar.xz
Source243:      mcexam.doc.tar.xz

%description -n texlive-mcexam
This LaTeX package automatically randomly permutes the order of
questions as well as the answer options in different versions
of a multiple choice exam/test. Next to the exam versions
themselves, the package also allows printing a concept version
of the exam, a key table with the correct answers or points,
and a document with solutions and explanations per exam
version. The package also allows writing an R code which
processes the results of the exam and calculates the grades.
The following other LaTeX packages are required: enumitem,
environ, etoolbox, longtable, newfile, pgffor (from the
PGF/TikZ bundle), xkeyval, and xstring.

%package -n texlive-mcexam-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn46155
Release:        0
Summary:        Documentation for texlive-mcexam
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mcexam-doc
This package includes the documentation for texlive-mcexam

%post -n texlive-mcexam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mcexam 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mcexam
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mcexam-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mcexam/README.md
%{_texmfdistdir}/doc/latex/mcexam/mcexam.pdf
%{_texmfdistdir}/doc/latex/mcexam/mcexam.tex
%{_texmfdistdir}/doc/latex/mcexam/mcexam_example.r
%{_texmfdistdir}/doc/latex/mcexam/mcexam_example.tex

%files -n texlive-mcexam
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mcexam/mcexam.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mcexam-%{texlive_version}.%{texlive_noarch}.0.0.4svn46155-%{release}-zypper
%endif

%package -n texlive-mcf2graph
Version:        %{texlive_version}.%{texlive_noarch}.4.48svn53550
Release:        0
Summary:        Draw chemical structure diagrams with Metafont/MetaPost
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mcf2graph-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source244:      mcf2graph.tar.xz
Source245:      mcf2graph.doc.tar.xz

%description -n texlive-mcf2graph
The Molecular Coding Format (MCF) is a linear notation for
describing chemical structure diagrams. This package converts
MCF to graphic files using Metafont / MetaPost.

%package -n texlive-mcf2graph-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.48svn53550
Release:        0
Summary:        Documentation for texlive-mcf2graph
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mcf2graph-doc
This package includes the documentation for texlive-mcf2graph

%post -n texlive-mcf2graph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mcf2graph 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mcf2graph
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mcf2graph-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/mcf2graph/CHANGELOG
%{_texmfdistdir}/doc/metapost/mcf2graph/README
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_exa_soc.mf
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_example.pdf
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_example.tex
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_man_soc-064.mps
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_man_soc.mf
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_manual.pdf
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_manual.tex
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_mplib_exa.pdf
%{_texmfdistdir}/doc/metapost/mcf2graph/mcf_mplib_exa.tex

%files -n texlive-mcf2graph
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/mcf2graph/mcf2graph.mf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mcf2graph-%{texlive_version}.%{texlive_noarch}.4.48svn53550-%{release}-zypper
%endif

%package -n texlive-mcite
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn18173
Release:        0
Summary:        Multiple items in a single citation
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mcite-doc >= %{texlive_version}
Provides:       tex(mcite.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source246:      mcite.tar.xz
Source247:      mcite.doc.tar.xz

%description -n texlive-mcite
The mcite package allows the user to collapse multiple
citations into one, as is customary in physics journals. The
package requires a customised BibTeX style for its work; the
documentation explains how to do that customisation.

%package -n texlive-mcite-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn18173
Release:        0
Summary:        Documentation for texlive-mcite
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mcite-doc
This package includes the documentation for texlive-mcite

%post -n texlive-mcite
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mcite 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mcite
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mcite-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mcite/COPYING
%{_texmfdistdir}/doc/latex/mcite/README
%{_texmfdistdir}/doc/latex/mcite/mcite.bib
%{_texmfdistdir}/doc/latex/mcite/mcite.pdf

%files -n texlive-mcite
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mcite/mcite.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mcite-%{texlive_version}.%{texlive_noarch}.1.6svn18173-%{release}-zypper
%endif

%package -n texlive-mciteplus
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn31648
Release:        0
Summary:        Enhanced multiple citations
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mciteplus-doc >= %{texlive_version}
Provides:       tex(mciteplus.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source248:      mciteplus.tar.xz
Source249:      mciteplus.doc.tar.xz

%description -n texlive-mciteplus
The mciteplus LaTeX package is an enhanced reimplementation of
Thorsten Ohl's mcite package which provides support for the
grouping of multiple citations together as is often done in
physics journals. An extensive set of features provide for
other applications such as reference sublisting.

%package -n texlive-mciteplus-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn31648
Release:        0
Summary:        Documentation for texlive-mciteplus
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mciteplus-doc
This package includes the documentation for texlive-mciteplus

%post -n texlive-mciteplus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mciteplus 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mciteplus
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mciteplus-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mciteplus/README
%{_texmfdistdir}/doc/latex/mciteplus/changelog.txt
%{_texmfdistdir}/doc/latex/mciteplus/mciteplus_code.txt
%{_texmfdistdir}/doc/latex/mciteplus/mciteplus_doc.pdf
%{_texmfdistdir}/doc/latex/mciteplus/mciteplus_doc.tex

%files -n texlive-mciteplus
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/mciteplus/IEEEtranM.bst
%{_texmfdistdir}/bibtex/bst/mciteplus/IEEEtranMN.bst
%{_texmfdistdir}/bibtex/bst/mciteplus/apsrevM.bst
%{_texmfdistdir}/bibtex/bst/mciteplus/apsrmpM.bst
%{_texmfdistdir}/tex/latex/mciteplus/mciteplus.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mciteplus-%{texlive_version}.%{texlive_noarch}.1.2svn31648-%{release}-zypper
%endif

%package -n texlive-mcmthesis
Version:        %{texlive_version}.%{texlive_noarch}.6.3svn53513
Release:        0
Summary:        Template designed for MCM/ICM
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mcmthesis-doc >= %{texlive_version}
Provides:       tex(mcmthesis.cls)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(appendix.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(berasans.sty)
Requires:       tex(bm.sty)
Requires:       tex(bmpsize.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(environ.sty)
Requires:       tex(epstopdf.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(flafter.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hhline.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(multirow.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pifont.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source250:      mcmthesis.tar.xz
Source251:      mcmthesis.doc.tar.xz

%description -n texlive-mcmthesis
The package offers a template for MCM (The Mathematical Contest
in Modeling) and ICM (The Interdisciplinary Contest in
Modeling) for typesetting the submitted paper.

%package -n texlive-mcmthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.6.3svn53513
Release:        0
Summary:        Documentation for texlive-mcmthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mcmthesis-doc
This package includes the documentation for texlive-mcmthesis

%post -n texlive-mcmthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mcmthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mcmthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mcmthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mcmthesis/LICENSE
%{_texmfdistdir}/doc/latex/mcmthesis/LICENSE.tex
%{_texmfdistdir}/doc/latex/mcmthesis/README.md
%{_texmfdistdir}/doc/latex/mcmthesis/README.tex
%{_texmfdistdir}/doc/latex/mcmthesis/code/mcmthesis-matlab1.m
%{_texmfdistdir}/doc/latex/mcmthesis/code/mcmthesis-sudoku.cpp
%{_texmfdistdir}/doc/latex/mcmthesis/figures/example-image-a.pdf
%{_texmfdistdir}/doc/latex/mcmthesis/figures/example-image-b.pdf
%{_texmfdistdir}/doc/latex/mcmthesis/figures/example-image-c.pdf
%{_texmfdistdir}/doc/latex/mcmthesis/figures/mcmthesis-logo.pdf
%{_texmfdistdir}/doc/latex/mcmthesis/mcmthesis-demo.pdf
%{_texmfdistdir}/doc/latex/mcmthesis/mcmthesis-demo.tex
%{_texmfdistdir}/doc/latex/mcmthesis/mcmthesis.pdf

%files -n texlive-mcmthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mcmthesis/mcmthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mcmthesis-%{texlive_version}.%{texlive_noarch}.6.3svn53513-%{release}-zypper
%endif

%package -n texlive-mdframed
Version:        %{texlive_version}.%{texlive_noarch}.1.9bsvn31075
Release:        0
Summary:        Framed environments that can split at page boundaries
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mdframed-doc >= %{texlive_version}
Provides:       tex(ltxmdf.cls)
Provides:       tex(mdframed.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(beramono.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(color.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hypdoc.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kantlipsum.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(listings.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multicol.sty)
Requires:       tex(needspace.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(scrpage2.sty)
Requires:       tex(selinput.sty)
Requires:       tex(showframe.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
Requires:       tex(zref-abspage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source252:      mdframed.tar.xz
Source253:      mdframed.doc.tar.xz

%description -n texlive-mdframed
The package develops the facilities of framed in providing
breakable framed and coloured boxes. The user may instruct the
package to perform its operations using default LaTeX commands,
PStricks or TikZ.

%package -n texlive-mdframed-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9bsvn31075
Release:        0
Summary:        Documentation for texlive-mdframed
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mdframed-doc
This package includes the documentation for texlive-mdframed

%post -n texlive-mdframed
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mdframed 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mdframed
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mdframed-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mdframed/README.txt
%{_texmfdistdir}/doc/latex/mdframed/ctan-lion.png
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-default.pdf
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-default.tex
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-pstricks.pdf
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-pstricks.tex
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-texsx.pdf
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-texsx.tex
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-tikz.pdf
%{_texmfdistdir}/doc/latex/mdframed/mdframed-example-tikz.tex
%{_texmfdistdir}/doc/latex/mdframed/mdframed.pdf

%files -n texlive-mdframed
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mdframed/ltxmdf.cls
%{_texmfdistdir}/tex/latex/mdframed/md-frame-0.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-1.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-2.mdf
%{_texmfdistdir}/tex/latex/mdframed/md-frame-3.mdf
%{_texmfdistdir}/tex/latex/mdframed/mdframed.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mdframed-%{texlive_version}.%{texlive_noarch}.1.9bsvn31075-%{release}-zypper
%endif

%package -n texlive-mdputu
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn20298
Release:        0
Summary:        Upright digits in Adobe Utopia Italic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mdputu-doc >= %{texlive_version}
Provides:       tex(mdputu.sty)
Provides:       tex(mdputubi7t.tfm)
Provides:       tex(mdputubi7t.vf)
Provides:       tex(mdputubi8t.tfm)
Provides:       tex(mdputubi8t.vf)
Provides:       tex(mdputuri7t.tfm)
Provides:       tex(mdputuri7t.vf)
Provides:       tex(mdputuri8t.tfm)
Provides:       tex(mdputuri8t.vf)
Provides:       tex(ot1mdputu.fd)
Provides:       tex(t1mdputu.fd)
Requires:       tex(mdputb7t.tfm)
Requires:       tex(mdputb8t.tfm)
Requires:       tex(mdputbi7t.tfm)
Requires:       tex(mdputbi8t.tfm)
Requires:       tex(mdputr7t.tfm)
Requires:       tex(mdputr8t.tfm)
Requires:       tex(mdputri7t.tfm)
Requires:       tex(mdputri8t.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source254:      mdputu.tar.xz
Source255:      mdputu.doc.tar.xz

%description -n texlive-mdputu
The Annals of Mathematics uses italics for theorems. However,
slanted digits and parentheses look disturbing when surrounded
by (upright) mathematics. This package provides virtual fonts
with italics and upright digits and punctuation, as an
extension to Mathdesign's Utopia bundle.

%package -n texlive-mdputu-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn20298
Release:        0
Summary:        Documentation for texlive-mdputu
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mdputu-doc
This package includes the documentation for texlive-mdputu

%post -n texlive-mdputu
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mdputu 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mdputu
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mdputu-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mdputu/README
%{_texmfdistdir}/doc/latex/mdputu/mdputu.dtx
%{_texmfdistdir}/doc/latex/mdputu/mdputu.ins
%{_texmfdistdir}/doc/latex/mdputu/mdputu.pdf
%{_texmfdistdir}/doc/latex/mdputu/sample.pdf
%{_texmfdistdir}/doc/latex/mdputu/sample.tex

%files -n texlive-mdputu
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputubi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputubi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputuri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputuri8t.tfm
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputubi7t.vf
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputubi8t.vf
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputuri7t.vf
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputuri8t.vf
%{_texmfdistdir}/tex/latex/mdputu/mdputu.sty
%{_texmfdistdir}/tex/latex/mdputu/ot1mdputu.fd
%{_texmfdistdir}/tex/latex/mdputu/t1mdputu.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mdputu-%{texlive_version}.%{texlive_noarch}.1.2svn20298-%{release}-zypper
%endif

%package -n texlive-mdsymbol
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn28399
Release:        0
Summary:        Symbol fonts to match Adobe Myriad Pro
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-mdsymbol-fonts >= %{texlive_version}
Recommends:     texlive-mdsymbol-doc >= %{texlive_version}
Provides:       tex(MdSymbolA-Bold.tfm)
Provides:       tex(MdSymbolA-Light.tfm)
Provides:       tex(MdSymbolA-Regular.tfm)
Provides:       tex(MdSymbolA-Semibold.tfm)
Provides:       tex(MdSymbolB-Bold.tfm)
Provides:       tex(MdSymbolB-Light.tfm)
Provides:       tex(MdSymbolB-Regular.tfm)
Provides:       tex(MdSymbolB-Semibold.tfm)
Provides:       tex(MdSymbolC-Bold.tfm)
Provides:       tex(MdSymbolC-Light.tfm)
Provides:       tex(MdSymbolC-Regular.tfm)
Provides:       tex(MdSymbolC-Semibold.tfm)
Provides:       tex(MdSymbolD-Bold.tfm)
Provides:       tex(MdSymbolD-Light.tfm)
Provides:       tex(MdSymbolD-Regular.tfm)
Provides:       tex(MdSymbolD-Semibold.tfm)
Provides:       tex(MdSymbolE-Bold.tfm)
Provides:       tex(MdSymbolE-Light.tfm)
Provides:       tex(MdSymbolE-Regular.tfm)
Provides:       tex(MdSymbolE-Semibold.tfm)
Provides:       tex(MdSymbolF-Bold.tfm)
Provides:       tex(MdSymbolF-Light.tfm)
Provides:       tex(MdSymbolF-Regular.tfm)
Provides:       tex(MdSymbolF-Semibold.tfm)
Provides:       tex(mdsymbol-a.enc)
Provides:       tex(mdsymbol-b.enc)
Provides:       tex(mdsymbol-c.enc)
Provides:       tex(mdsymbol-d.enc)
Provides:       tex(mdsymbol-e.enc)
Provides:       tex(mdsymbol-f.enc)
Provides:       tex(mdsymbol.map)
Provides:       tex(mdsymbol.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fltpoint.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source256:      mdsymbol.tar.xz
Source257:      mdsymbol.doc.tar.xz

%description -n texlive-mdsymbol
The package provides a font of mathematical symbols, MyriadPro
The font is designed as a companion to Adobe Myriad Pro, but it
might also fit well with other contemporary typefaces.

%package -n texlive-mdsymbol-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn28399
Release:        0
Summary:        Documentation for texlive-mdsymbol
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mdsymbol-doc
This package includes the documentation for texlive-mdsymbol


%package -n texlive-mdsymbol-fonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn28399
Release:        0
Summary:        Severed fonts for texlive-mdsymbol
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-mdsymbol-fonts
The  separated fonts package for texlive-mdsymbol
%post -n texlive-mdsymbol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap mdsymbol.map' >> /var/run/texlive/run-updmap

%postun -n texlive-mdsymbol 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap mdsymbol.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-mdsymbol
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-mdsymbol-fonts
%files -n texlive-mdsymbol-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/mdsymbol/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/mdsymbol/OFL.txt
%{_texmfdistdir}/doc/latex/mdsymbol/mdsymbol.pdf

%files -n texlive-mdsymbol
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-a.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-b.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-c.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-d.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-e.enc
%{_texmfdistdir}/fonts/enc/dvips/mdsymbol/mdsymbol-f.enc
%{_texmfdistdir}/fonts/map/dvips/mdsymbol/mdsymbol.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/mdsymbol/MdSymbol-Semibold.otf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolA.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolB.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolC.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolD.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolE.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Bold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Light.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Regular.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF-Semibold.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/MdSymbolF.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdaccents.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdarrows.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdbase.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mddelims.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdgeometric.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdoperators.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdrelations.mf
%{_texmfdistdir}/fonts/source/public/mdsymbol/mdturnstile.mf
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolA-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolB-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolC-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolD-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolE-Semibold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Light.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/mdsymbol/MdSymbolF-Semibold.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolA-Semibold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolB-Semibold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolC-Semibold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolD-Semibold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolE-Semibold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Light.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/mdsymbol/MdSymbolF-Semibold.pfb
%{_texmfdistdir}/tex/latex/mdsymbol/mdsymbol.sty

%files -n texlive-mdsymbol-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-mdsymbol
%{_datadir}/fontconfig/conf.avail/58-texlive-mdsymbol.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-mdsymbol.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-mdsymbol.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mdsymbol/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mdsymbol/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-mdsymbol/fonts.scale
%{_datadir}/fonts/texlive-mdsymbol/MdSymbol-Bold.otf
%{_datadir}/fonts/texlive-mdsymbol/MdSymbol-Light.otf
%{_datadir}/fonts/texlive-mdsymbol/MdSymbol-Regular.otf
%{_datadir}/fonts/texlive-mdsymbol/MdSymbol-Semibold.otf
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolA-Bold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolA-Light.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolA-Regular.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolA-Semibold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolB-Bold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolB-Light.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolB-Regular.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolB-Semibold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolC-Bold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolC-Light.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolC-Regular.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolC-Semibold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolD-Bold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolD-Light.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolD-Regular.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolD-Semibold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolE-Bold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolE-Light.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolE-Regular.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolE-Semibold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolF-Bold.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolF-Light.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolF-Regular.pfb
%{_datadir}/fonts/texlive-mdsymbol/MdSymbolF-Semibold.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mdsymbol-fonts-%{texlive_version}.%{texlive_noarch}.0.0.5svn28399-%{release}-zypper
%endif

%package -n texlive-mdwtools
Version:        %{texlive_version}.%{texlive_noarch}.1.05.4svn15878
Release:        0
Summary:        Miscellaneous tools by Mark Wooding
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mdwtools-doc >= %{texlive_version}
Provides:       tex(at.sty)
Provides:       tex(cmtt.sty)
Provides:       tex(doafter.sty)
Provides:       tex(footnote.sty)
Provides:       tex(mTTcmtt.fd)
Provides:       tex(mTTenc.def)
Provides:       tex(mathenv.sty)
Provides:       tex(mdwlist.sty)
Provides:       tex(mdwmath.sty)
Provides:       tex(mdwtab.sty)
Provides:       tex(sverb.sty)
Provides:       tex(syntax.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source258:      mdwtools.tar.xz
Source259:      mdwtools.doc.tar.xz

%description -n texlive-mdwtools
This collection of tools includes: support for short commands
starting with @, macros to sanitise the OT1 encoding of the
cmtt fonts; a 'do after' command; improved footnote support;
mathenv for various alignment in maths; list handling; mdwmath
which adds some minor changes to LaTeX maths; a rewrite of
LaTeX's tabular and array environments; verbatim handling; and
syntax diagrams.

%package -n texlive-mdwtools-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05.4svn15878
Release:        0
Summary:        Documentation for texlive-mdwtools
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mdwtools-doc
This package includes the documentation for texlive-mdwtools

%post -n texlive-mdwtools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mdwtools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mdwtools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mdwtools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mdwtools/COPYING
%{_texmfdistdir}/doc/latex/mdwtools/README
%{_texmfdistdir}/doc/latex/mdwtools/at.pdf
%{_texmfdistdir}/doc/latex/mdwtools/cmtt.pdf
%{_texmfdistdir}/doc/latex/mdwtools/doafter.pdf
%{_texmfdistdir}/doc/latex/mdwtools/doafter.tex
%{_texmfdistdir}/doc/latex/mdwtools/footnote.pdf
%{_texmfdistdir}/doc/latex/mdwtools/gpl.tex
%{_texmfdistdir}/doc/latex/mdwtools/mathenv.tex
%{_texmfdistdir}/doc/latex/mdwtools/mdwlist.pdf
%{_texmfdistdir}/doc/latex/mdwtools/mdwmath.pdf
%{_texmfdistdir}/doc/latex/mdwtools/mdwtab.pdf
%{_texmfdistdir}/doc/latex/mdwtools/mdwtools.tex
%{_texmfdistdir}/doc/latex/mdwtools/sverb.pdf
%{_texmfdistdir}/doc/latex/mdwtools/syntax.pdf

%files -n texlive-mdwtools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mdwtools/at.sty
%{_texmfdistdir}/tex/latex/mdwtools/cmtt.sty
%{_texmfdistdir}/tex/latex/mdwtools/doafter.sty
%{_texmfdistdir}/tex/latex/mdwtools/footnote.sty
%{_texmfdistdir}/tex/latex/mdwtools/mTTcmtt.fd
%{_texmfdistdir}/tex/latex/mdwtools/mTTenc.def
%{_texmfdistdir}/tex/latex/mdwtools/mathenv.sty
%{_texmfdistdir}/tex/latex/mdwtools/mdwlist.sty
%{_texmfdistdir}/tex/latex/mdwtools/mdwmath.sty
%{_texmfdistdir}/tex/latex/mdwtools/mdwtab.sty
%{_texmfdistdir}/tex/latex/mdwtools/sverb.sty
%{_texmfdistdir}/tex/latex/mdwtools/syntax.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mdwtools-%{texlive_version}.%{texlive_noarch}.1.05.4svn15878-%{release}-zypper
%endif

%package -n texlive-media4svg
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn54773
Release:        0
Summary:        Multimedia inclusion for the dvisvgm backend
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-media4svg-doc >= %{texlive_version}
Provides:       tex(media4svg.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(expl3.sty)
Requires:       tex(iftex.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source260:      media4svg.tar.xz
Source261:      media4svg.doc.tar.xz

%description -n texlive-media4svg
This package implements an interface for embedding video and
audio files in SVG (Scalable Vector Graphics) output. SVG with
embedded media is very portable, as it is supported by all
modern Web browsers across a variety of operating systems and
platforms, including portable devices. All DVI producing TeX
engines can be used. The dvisvgm utility, which is part of all
major TeX distributions, converts the intermediate DVI to SVG.
By default, media files are embedded into the SVG output to
make self-sufficient SVG files. The package depends on iftex,
expl3, l3keys2e, xparse, and atbegshi.

%package -n texlive-media4svg-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn54773
Release:        0
Summary:        Documentation for texlive-media4svg
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-media4svg-doc
This package includes the documentation for texlive-media4svg

%post -n texlive-media4svg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-media4svg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-media4svg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-media4svg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/media4svg/ChangeLog
%{_texmfdistdir}/doc/latex/media4svg/README.txt
%{_texmfdistdir}/doc/latex/media4svg/example/beamer-example-1.svg
%{_texmfdistdir}/doc/latex/media4svg/example/beamer-example-2.svg
%{_texmfdistdir}/doc/latex/media4svg/example/beamer-example-3.svg
%{_texmfdistdir}/doc/latex/media4svg/example/beamer-example-4.svg
%{_texmfdistdir}/doc/latex/media4svg/example/beamer-example.tex

%files -n texlive-media4svg
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/media4svg/media4svg.lua
%{_texmfdistdir}/tex/latex/media4svg/media4svg.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-media4svg-%{texlive_version}.%{texlive_noarch}.0.0.4svn54773-%{release}-zypper
%endif

%package -n texlive-media9
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn54554
Release:        0
Summary:        Multimedia inclusion package with Adobe Reader-9/X compatibility
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-media9-doc >= %{texlive_version}
Provides:       tex(media9.sty)
Provides:       tex(pdfbase.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(ocgbase.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source262:      media9.tar.xz
Source263:      media9.doc.tar.xz

%description -n texlive-media9
The package provides an interface to embed interactive Flash
(SWF) and 3D objects (Adobe U3D & PRC), as well as video and
sound files or streams in the popular MP4, FLV and MP3 formats
into PDF documents with Acrobat-9/X compatibility. Playback of
multimedia files uses the built-in Flash Player of Adobe Reader
and does, therefore, not depend on external plug-ins. Flash
Player supports the efficient H.264 codec for video
compression. The package is based on the RichMedia Annotation,
an Adobe addition to the PDF specification. It replaces the now
obsolete movie15 package.

%package -n texlive-media9-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn54554
Release:        0
Summary:        Documentation for texlive-media9
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-media9-doc
This package includes the documentation for texlive-media9

%post -n texlive-media9
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-media9 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-media9
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-media9-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/media9/ChangeLog
%{_texmfdistdir}/doc/latex/media9/README.txt
%{_texmfdistdir}/doc/latex/media9/media9.pdf

%files -n texlive-media9
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/media9/javascript/3Dmenu.js
%{_texmfdistdir}/tex/latex/media9/javascript/3Dspintool.js
%{_texmfdistdir}/tex/latex/media9/javascript/animation.js
%{_texmfdistdir}/tex/latex/media9/javascript/asylabels.js
%{_texmfdistdir}/tex/latex/media9/media9.sty
%{_texmfdistdir}/tex/latex/media9/pdfbase.sty
%{_texmfdistdir}/tex/latex/media9/players/APlayer.swf
%{_texmfdistdir}/tex/latex/media9/players/APlayer9.swf
%{_texmfdistdir}/tex/latex/media9/players/SlideShow.swf
%{_texmfdistdir}/tex/latex/media9/players/StrobeMediaPlayback.swf
%{_texmfdistdir}/tex/latex/media9/players/VPlayer.swf
%{_texmfdistdir}/tex/latex/media9/players/VPlayer9.swf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-media9-%{texlive_version}.%{texlive_noarch}.1.10svn54554-%{release}-zypper
%endif

%package -n texlive-medstarbeamer
Version:        %{texlive_version}.%{texlive_noarch}.svn38828
Release:        0
Summary:        Beamer document class for MedStar Health Research Institute
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-medstarbeamer-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeMedStarColors.sty)
Provides:       tex(medstarbeamer.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(anysize.sty)
Requires:       tex(background.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cancel.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pgf.sty)
Requires:       tex(soul.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source264:      medstarbeamer.tar.xz
Source265:      medstarbeamer.doc.tar.xz

%description -n texlive-medstarbeamer
This is a beamer template for MedStar Health presentations. It
includes sample presentations using both .tex files and .rnw
files. The document class is obviously compatible with both.
The advantage of the .rnw file is that it can be used with
knitr such that you can weave your R code with your
presentation.

%package -n texlive-medstarbeamer-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn38828
Release:        0
Summary:        Documentation for texlive-medstarbeamer
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-medstarbeamer-doc
This package includes the documentation for texlive-medstarbeamer

%post -n texlive-medstarbeamer
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-medstarbeamer 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-medstarbeamer
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-medstarbeamer-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/medstarbeamer/README.txt
%{_texmfdistdir}/doc/latex/medstarbeamer/example.tex

%files -n texlive-medstarbeamer
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/medstarbeamer/beamercolorthemeMedStarColors.sty
%{_texmfdistdir}/tex/latex/medstarbeamer/medstarbeamer.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-medstarbeamer-%{texlive_version}.%{texlive_noarch}.svn38828-%{release}-zypper
%endif

%package -n texlive-meetingmins
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn31878
Release:        0
Summary:        Format written minutes of meetings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-meetingmins-doc >= %{texlive_version}
Provides:       tex(meetingmins.cls)
Requires:       tex(article.cls)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathabx.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source266:      meetingmins.tar.xz
Source267:      meetingmins.doc.tar.xz

%description -n texlive-meetingmins
The class allows formatting of meeting minutes using \section
commands (which provide hierarchical structure). An agenda can
also be produced for distribution prior to the meeting, with
user-selected portions suppressed from printing.

%package -n texlive-meetingmins-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn31878
Release:        0
Summary:        Documentation for texlive-meetingmins
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-meetingmins-doc
This package includes the documentation for texlive-meetingmins

%post -n texlive-meetingmins
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-meetingmins 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-meetingmins
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-meetingmins-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/meetingmins/README
%{_texmfdistdir}/doc/latex/meetingmins/meetingmins.pdf
%{_texmfdistdir}/doc/latex/meetingmins/samples/agenda.pdf
%{_texmfdistdir}/doc/latex/meetingmins/samples/agenda.tex
%{_texmfdistdir}/doc/latex/meetingmins/samples/chair.pdf
%{_texmfdistdir}/doc/latex/meetingmins/samples/chair.tex
%{_texmfdistdir}/doc/latex/meetingmins/samples/department.min
%{_texmfdistdir}/doc/latex/meetingmins/samples/minutes.pdf
%{_texmfdistdir}/doc/latex/meetingmins/samples/minutes.tex

%files -n texlive-meetingmins
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/meetingmins/meetingmins.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-meetingmins-%{texlive_version}.%{texlive_noarch}.1.6svn31878-%{release}-zypper
%endif

%package -n texlive-memdesign
Version:        %{texlive_version}.%{texlive_noarch}.svn48664
Release:        0
Summary:        Notes on book design
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source268:      memdesign.doc.tar.xz

%description -n texlive-memdesign
"A Few Notes on Book Design" provides an introduction to the
business of book design. It is an extended version of what used
to be the first part of the memoir users' manual. Please note
that the compiled copy, supplied in the package, uses
commercial fonts; the README file contains instructions on how
to compile the document without these fonts.
%post -n texlive-memdesign
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-memdesign 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-memdesign
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-memdesign
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/memdesign/README
%{_texmfdistdir}/doc/fonts/memdesign/memdesign.pdf
%{_texmfdistdir}/doc/fonts/memdesign/memdesign.tex
%{_texmfdistdir}/doc/fonts/memdesign/memetc.bib
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-memdesign-%{texlive_version}.%{texlive_noarch}.svn48664-%{release}-zypper
%endif

%package -n texlive-memexsupp
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Experimental memoir support
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-memexsupp-doc >= %{texlive_version}
Provides:       tex(memexsupp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source269:      memexsupp.tar.xz
Source270:      memexsupp.doc.tar.xz

%description -n texlive-memexsupp
A package of code proposed as supporting material for memoir.
The package is intended as a test bed for such code, which may
in the fullness of time be adopted into the main memoir
release.

%package -n texlive-memexsupp-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-memexsupp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-memexsupp-doc
This package includes the documentation for texlive-memexsupp

%post -n texlive-memexsupp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-memexsupp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-memexsupp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-memexsupp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/memexsupp/README
%{_texmfdistdir}/doc/latex/memexsupp/memexsupp.pdf
%{_texmfdistdir}/doc/latex/memexsupp/memexsupp.tex

%files -n texlive-memexsupp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/memexsupp/memexsupp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-memexsupp-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif

%package -n texlive-memoir
Version:        %{texlive_version}.%{texlive_noarch}.3.7ksvn54554
Release:        0
Summary:        Typeset fiction, non-fiction and mathematical books
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-memoir-doc >= %{texlive_version}
Provides:       tex(mem10.clo)
Provides:       tex(mem11.clo)
Provides:       tex(mem12.clo)
Provides:       tex(mem14.clo)
Provides:       tex(mem17.clo)
Provides:       tex(mem20.clo)
Provides:       tex(mem25.clo)
Provides:       tex(mem30.clo)
Provides:       tex(mem36.clo)
Provides:       tex(mem48.clo)
Provides:       tex(mem60.clo)
Provides:       tex(mem9.clo)
Provides:       tex(memhfixc.sty)
Provides:       tex(memoir.cls)
Requires:       tex(array.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(delarray.sty)
Requires:       tex(etex.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(iftex.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source271:      memoir.tar.xz
Source272:      memoir.doc.tar.xz

%description -n texlive-memoir
The memoir class is for typesetting poetry, fiction,
non-fiction, and mathematical works. Permissible document
'base' font sizes range from 9 to 60pt. There is a range of
page-styles and well over a dozen chapter-styles to choose
from, as well as methods for specifying your own layouts and
designs. The class also provides the functionality of over
thirty of the more popular packages, thus simplifying document
sources. Users who wish to use the hyperref package, in a
document written with the memoir class, should also use the
memhfixc package (part of this bundle). Note, however, that any
current version of hyperref actually loads the package
automatically if it detects that it is running under memoir.

%package -n texlive-memoir-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.7ksvn54554
Release:        0
Summary:        Documentation for texlive-memoir
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-memoir-doc
This package includes the documentation for texlive-memoir

%post -n texlive-memoir
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-memoir 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-memoir
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-memoir-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/memoir/Makeidxglo
%{_texmfdistdir}/doc/latex/memoir/README
%{_texmfdistdir}/doc/latex/memoir/anvil2.mps
%{_texmfdistdir}/doc/latex/memoir/memfonts.sty
%{_texmfdistdir}/doc/latex/memoir/memlays.sty
%{_texmfdistdir}/doc/latex/memoir/memman.gst
%{_texmfdistdir}/doc/latex/memoir/memman.ist
%{_texmfdistdir}/doc/latex/memoir/memman.pdf
%{_texmfdistdir}/doc/latex/memoir/memman.tex
%{_texmfdistdir}/doc/latex/memoir/memnoidxnum.tex
%{_texmfdistdir}/doc/latex/memoir/memsty.sty
%{_texmfdistdir}/doc/latex/memoir/setpage-example.pdf
%{_texmfdistdir}/doc/latex/memoir/titlepages.sty
%{_texmfdistdir}/doc/latex/memoir/trims-example.tex

%files -n texlive-memoir
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/memoir/basic.gst
%{_texmfdistdir}/tex/latex/memoir/mem10.clo
%{_texmfdistdir}/tex/latex/memoir/mem11.clo
%{_texmfdistdir}/tex/latex/memoir/mem12.clo
%{_texmfdistdir}/tex/latex/memoir/mem14.clo
%{_texmfdistdir}/tex/latex/memoir/mem17.clo
%{_texmfdistdir}/tex/latex/memoir/mem20.clo
%{_texmfdistdir}/tex/latex/memoir/mem25.clo
%{_texmfdistdir}/tex/latex/memoir/mem30.clo
%{_texmfdistdir}/tex/latex/memoir/mem36.clo
%{_texmfdistdir}/tex/latex/memoir/mem48.clo
%{_texmfdistdir}/tex/latex/memoir/mem60.clo
%{_texmfdistdir}/tex/latex/memoir/mem9.clo
%{_texmfdistdir}/tex/latex/memoir/memhfixc.sty
%{_texmfdistdir}/tex/latex/memoir/memoir.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-memoir-%{texlive_version}.%{texlive_noarch}.3.7ksvn54554-%{release}-zypper
%endif

%package -n texlive-memory
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn30452
Release:        0
Summary:        Containers for data in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-memory-doc >= %{texlive_version}
Provides:       tex(memory.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source273:      memory.tar.xz
Source274:      memory.doc.tar.xz

%description -n texlive-memory
The package allows the user to declare single object or array
containers.

%package -n texlive-memory-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn30452
Release:        0
Summary:        Documentation for texlive-memory
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-memory-doc
This package includes the documentation for texlive-memory

%post -n texlive-memory
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-memory 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-memory
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-memory-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/memory/README
%{_texmfdistdir}/doc/latex/memory/memory.pdf

%files -n texlive-memory
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/memory/memory.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-memory-%{texlive_version}.%{texlive_noarch}.1.2svn30452-%{release}-zypper
%endif

%package -n texlive-memorygraphs
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn49631
Release:        0
Summary:        TikZ styles to typeset graphs of program memory
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-memorygraphs-doc >= %{texlive_version}
Provides:       tex(memorygraphs.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source275:      memorygraphs.tar.xz
Source276:      memorygraphs.doc.tar.xz

%description -n texlive-memorygraphs
This package defines some TikZ styles and adds anchors to
existing styles that ease the declaration of "memory graphs".
It is intended for graphs that represent the memory of a
computer program during its execution.

%package -n texlive-memorygraphs-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn49631
Release:        0
Summary:        Documentation for texlive-memorygraphs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-memorygraphs-doc
This package includes the documentation for texlive-memorygraphs

%post -n texlive-memorygraphs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-memorygraphs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-memorygraphs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-memorygraphs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/memorygraphs/README.md
%{_texmfdistdir}/doc/latex/memorygraphs/memorygraphs.pdf
%{_texmfdistdir}/doc/latex/memorygraphs/memorygraphs.tex

%files -n texlive-memorygraphs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/memorygraphs/memorygraphs.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-memorygraphs-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn49631-%{release}-zypper
%endif

%package -n texlive-mendex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50268
Release:        0
Summary:        Documentation for Mendex index processor
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mendex-doc-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source277:      mendex-doc.source.tar.xz
Source278:      mendex-doc.doc.tar.xz

%description -n texlive-mendex-doc
This package provides documentation for Mendex (Japanese index
processor). The source code of the program is not included, it
can be obtained from TeX Live subversion repository.

%package -n texlive-mendex-doc-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn50268
Release:        0
Summary:        Documentation for texlive-mendex-doc
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-mendex-doc-doc:ja)

%description -n texlive-mendex-doc-doc
This package includes the documentation for texlive-mendex-doc

%post -n texlive-mendex-doc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mendex-doc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mendex-doc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mendex-doc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/mendex-doc/LICENSE
%{_texmfdistdir}/doc/support/mendex-doc/README.md
%{_texmfdistdir}/doc/support/mendex-doc/mendex.pdf
%{_texmfdistdir}/doc/support/mendex-doc/mendex.tex

%files -n texlive-mendex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/source/latex/mendex-doc/Makefile
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mendex-doc-%{texlive_version}.%{texlive_noarch}.svn50268-%{release}-zypper
%endif

%package -n texlive-mensa-tex
Version:        %{texlive_version}.%{texlive_noarch}.svn45997
Release:        0
Summary:        Typeset simple school cafeteria menus
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mensa-tex-doc >= %{texlive_version}
Provides:       tex(mensa-tex.cls)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(datetime2-calc.sty)
Requires:       tex(datetime2.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source279:      mensa-tex.tar.xz
Source280:      mensa-tex.doc.tar.xz

%description -n texlive-mensa-tex
This package provides a flexible LaTeX2e class for typesetting
school cafeteria menus consisting of two lunches (with
dessert), and dinner. It supports two different layouts: The
first layout is optimized for printing the menu on A4 paper.
The second layout is optimized for smartphone screens and uses
one (A6 sized) page per day. Supported localizations are
English (GB/US) and German. A way of defining additional
localizations is described in the documentation. The package
requires array, colortbl, datetime2, datetime2-calc, geometry,
graphicx, lmodern, textcomp, and xcolor.

%package -n texlive-mensa-tex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn45997
Release:        0
Summary:        Documentation for texlive-mensa-tex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mensa-tex-doc
This package includes the documentation for texlive-mensa-tex

%post -n texlive-mensa-tex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mensa-tex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mensa-tex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mensa-tex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mensa-tex/README.md
%{_texmfdistdir}/doc/latex/mensa-tex/doc/cafe-logo.png
%{_texmfdistdir}/doc/latex/mensa-tex/doc/mensa-tex-doc.pdf
%{_texmfdistdir}/doc/latex/mensa-tex/doc/mensa-tex-doc.tex
%{_texmfdistdir}/doc/latex/mensa-tex/doc/mensa-tex-example.pdf
%{_texmfdistdir}/doc/latex/mensa-tex/doc/mensa-tex-example.tex

%files -n texlive-mensa-tex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mensa-tex/mensa-tex.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mensa-tex-%{texlive_version}.%{texlive_noarch}.svn45997-%{release}-zypper
%endif

%package -n texlive-mentis
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        A basis for books to be published by Mentis publishers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-mentis-doc >= %{texlive_version}
Provides:       tex(mentis.cls)
Requires:       tex(babel.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(jurabib.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multicol.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(relsize.sty)
Requires:       tex(scrpage2.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source281:      mentis.tar.xz
Source282:      mentis.doc.tar.xz

%description -n texlive-mentis
This LaTeX class loads scrbook and provides changes necessary
for publishing at Mentis publishers in Paderborn, Germany. It
is not an official Mentis class, merely one developed by an
author in close co-operation with Mentis.

%package -n texlive-mentis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Documentation for texlive-mentis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-mentis-doc
This package includes the documentation for texlive-mentis

%post -n texlive-mentis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-mentis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-mentis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-mentis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/mentis/README
%{_texmfdistdir}/doc/latex/mentis/mentis.pdf

%files -n texlive-mentis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/mentis/mentis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-mentis-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif

%prep
%setup -q -c -T

%build

%install
    rm -rf %{buildroot}
    mkdir -p %{buildroot}%{_texmfdistdir}
    mkdir -p %{buildroot}%{_texmfmaindir}/tlpkg/tlpostcode
    mkdir -p %{buildroot}%{_datadir}/texlive/tlpkg
    mkdir -p %{buildroot}/var/adm/update-scripts
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf-dist
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf
    ln -sf ../../../share/texmf/tlpkg/tlpostcode \
                                    %{buildroot}%{_datadir}/texlive/tlpkg/tlpostcode
    ln -sf tlpkg/tlpostcode         %{buildroot}%{_texmfmaindir}/tlpostcode
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lshort-slovak-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lshort-slovenian-%{texlive_version}.%{texlive_noarch}.4.20svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lshort-spanish-%{texlive_version}.%{texlive_noarch}.0.0.5svn35050-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lshort-thai-%{texlive_version}.%{texlive_noarch}.1.32svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lshort-turkish-%{texlive_version}.%{texlive_noarch}.4.20svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lshort-ukr-%{texlive_version}.%{texlive_noarch}.4.00svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lshort-vietnamese-%{texlive_version}.%{texlive_noarch}.4.00svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lstaddons-%{texlive_version}.%{texlive_noarch}.0.0.1svn26196-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lstbayes-%{texlive_version}.%{texlive_noarch}.svn48160-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lstfiracode-%{texlive_version}.%{texlive_noarch}.0.0.1csvn49503-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lt3graph-%{texlive_version}.%{texlive_noarch}.0.0.1.9svn45913-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltablex-%{texlive_version}.%{texlive_noarch}.1.1svn34923-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltabptch-%{texlive_version}.%{texlive_noarch}.1.74dsvn17533-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltb2bib-%{texlive_version}.%{texlive_noarch}.0.0.01svn43746-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxcmds-%{texlive_version}.%{texlive_noarch}.1.24svn53165-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxdockit-%{texlive_version}.%{texlive_noarch}.1.2dsvn21869-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxfileinfo-%{texlive_version}.%{texlive_noarch}.2.04svn38663-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxguidex-%{texlive_version}.%{texlive_noarch}.0.0.2.0svn50992-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltximg-%{texlive_version}.%{texlive_noarch}.1.7svn51951-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/ltximg/ltximg.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxkeys-%{texlive_version}.%{texlive_noarch}.0.0.0.3csvn28332-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxmisc-%{texlive_version}.%{texlive_noarch}.svn21927-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxnew-%{texlive_version}.%{texlive_noarch}.1.3svn21586-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ltxtools-%{texlive_version}.%{texlive_noarch}.0.0.0.1asvn24897-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lua-alt-getopt-%{texlive_version}.%{texlive_noarch}.0.0.7.0svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/lua-alt-getopt/alt_getopt.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/texlua
		.
		w
		q
	EOF
    done
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/support/lua-alt-getopt/alt_getopt \
	       %{_texmfdistdir}/doc/support/lua-alt-getopt/tests/test.sh
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/support/lua-alt-getopt/alt_getopt
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lua-check-hyphen-%{texlive_version}.%{texlive_noarch}.0.0.7asvn47527-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lua-uca-%{texlive_version}.%{texlive_noarch}.0.0.1svn54550-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lua-ul-%{texlive_version}.%{texlive_noarch}.0.0.0.4svn54690-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lua-visual-debug-%{texlive_version}.%{texlive_noarch}.0.0.7svn49634-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luabibentry-%{texlive_version}.%{texlive_noarch}.0.0.1asvn31783-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luabidi-%{texlive_version}.%{texlive_noarch}.0.0.5svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luacode-%{texlive_version}.%{texlive_noarch}.1.2asvn25193-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luacolor-%{texlive_version}.%{texlive_noarch}.1.15svn53933-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luahbtex-%{texlive_version}.%{texlive_noarch}.svn54498-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luahyphenrules-%{texlive_version}.%{texlive_noarch}.1.0svn42670-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luaimageembed-%{texlive_version}.%{texlive_noarch}.0.0.1svn50788-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luaindex-%{texlive_version}.%{texlive_noarch}.0.0.1bsvn25882-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/luaindex/luaindex.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/texlua
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luainputenc-%{texlive_version}.%{texlive_noarch}.0.0.973svn20491-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luaintro-%{texlive_version}.%{texlive_noarch}.0.0.03svn35490-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/luatex/luaintro/01-02-7.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/02-01-4.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/02-01-5.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/02-02-6.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/03-08-3.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/03-11-1.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/06-11-1.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/06-11-2.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/06-11-7.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/06-11-8.sh \
	       %{_texmfdistdir}/doc/luatex/luaintro/06-11-9.sh
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luajittex-%{texlive_version}.%{texlive_noarch}.svn54498-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lualatex-doc-%{texlive_version}.%{texlive_noarch}.svn30473-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lualatex-doc-de-%{texlive_version}.%{texlive_noarch}.1.0svn30474-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lualatex-math-%{texlive_version}.%{texlive_noarch}.1.8svn52663-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lualatex-truncate-%{texlive_version}.%{texlive_noarch}.1.1svn48469-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lualibs-%{texlive_version}.%{texlive_noarch}.2.70svn53682-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/tex/luatex/lualibs/lualibs-compat.lua
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/tex/luatex/lualibs/lualibs-compat.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luamesh-%{texlive_version}.%{texlive_noarch}.0.0.51svn43814-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/luamesh/luamesh-polygon.lua \
	       %{_texmfdistdir}/scripts/luamesh/luamesh-tex.lua \
	       %{_texmfdistdir}/scripts/luamesh/luamesh.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/texlua
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luamplib-%{texlive_version}.%{texlive_noarch}.2.20.5svn53904-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luaotfload-%{texlive_version}.%{texlive_noarch}.3.12svn53652-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive
    pushd %{buildroot}%{_datadir}/texlive/texmf-dist
	patch --reject-format=unified --quoting-style=literal -f -p1 -F0 -T < %{S:82}
    popd
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/luaotfload/luaotfload-tool.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luapackageloader-%{texlive_version}.%{texlive_noarch}.0.0.2svn54779-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luarandom-%{texlive_version}.%{texlive_noarch}.0.0.01svn49419-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luasseq-%{texlive_version}.%{texlive_noarch}.svn37877-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/luasseq/luasseq.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/texlua
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luatex-%{texlive_version}.%{texlive_noarch}.svn54610-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive
    pushd %{buildroot}%{_datadir}/texlive/texmf-dist
	patch --reject-format=unified --quoting-style=literal -f -p1 -F0 -T < %{S:91}
    popd
    # Move configuration files
    mkdir -p %{buildroot}%{_texmfconfdir}/web2c
    mv -f  %{buildroot}%{_texmfdistdir}/web2c/texmfcnf.lua %{buildroot}%{_texmfconfdir}/web2c/
    rm -f  %{buildroot}%{_texmfdistdir}/web2c/texmfcnf.lua
    ln -sf %{_texmfconfdir}/web2c/texmfcnf.lua %{buildroot}%{_texmfdistdir}/web2c/texmfcnf.lua
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luatex85-%{texlive_version}.%{texlive_noarch}.1.4svn41456-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luatexbase-%{texlive_version}.%{texlive_noarch}.1.3svn52663-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luatexja-%{texlive_version}.%{texlive_noarch}.20200412.0svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luatexko-%{texlive_version}.%{texlive_noarch}.2.8svn54438-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luatextra-%{texlive_version}.%{texlive_noarch}.1.0.1svn20747-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luatodonotes-%{texlive_version}.%{texlive_noarch}.0.0.5svn53825-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luavlna-%{texlive_version}.%{texlive_noarch}.0.0.1fsvn52682-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-luaxml-%{texlive_version}.%{texlive_noarch}.0.0.1lsvn52137-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/tex/luatex/luaxml/luaxml-testxml.lua
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lwarp-%{texlive_version}.%{texlive_noarch}.0.0.83svn54586-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/lwarp/lwarpmk.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lxfonts-fonts-%{texlive_version}.%{texlive_noarch}.2.0bsvn32354-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-lxfonts
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/lxfonts/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-lxfonts
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-lxfonts/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-lxfonts/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-lxfonts/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-lxfonts/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-lxfonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-lxfonts    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-lxfonts/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ly1-%{texlive_version}.%{texlive_noarch}.svn47848-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-lyluatex-%{texlive_version}.%{texlive_noarch}.1.0fsvn51252-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/lyluatex/lyluatex-lib.lua \
	       %{_texmfdistdir}/scripts/lyluatex/lyluatex-options.lua \
	       %{_texmfdistdir}/scripts/lyluatex/lyluatex.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/texlua
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-m-tx-%{texlive_version}.%{texlive_noarch}.0.0.63csvn52851-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/doc/generic/m-tx/buildzip.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/texlua
		.
		w
		q
	EOF
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/m-tx/m-tx.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-macros2e-%{texlive_version}.%{texlive_noarch}.0.0.4asvn46026-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-macroswap-%{texlive_version}.%{texlive_noarch}.1.1svn31498-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mafr-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-magaz-%{texlive_version}.%{texlive_noarch}.0.0.4svn24694-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-magicnum-%{texlive_version}.%{texlive_noarch}.1.7svn52983-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mailing-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mailmerge-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-make4ht-%{texlive_version}.%{texlive_noarch}.0.0.3esvn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/make4ht/lapp-mk4.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-aeneas-config.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-config.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-dvireader.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-errorlogparser.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-filterlib.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-htlatex.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-indexing.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-lib.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-logging.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-odtfilter.lua \
	       %{_texmfdistdir}/scripts/make4ht/make4ht-xtpipes.lua \
	       %{_texmfdistdir}/scripts/make4ht/mkparams.lua \
	       %{_texmfdistdir}/scripts/make4ht/mkutils.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/texlua
		.
		w
		q
	EOF
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/make4ht/make4ht
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makebarcode-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makebase-%{texlive_version}.%{texlive_noarch}.0.0.2svn41012-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makebox-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makecell-%{texlive_version}.%{texlive_noarch}.0.0.1esvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makecirc-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makecmds-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makecookbook-%{texlive_version}.%{texlive_noarch}.0.0.85svn49311-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makedtx-%{texlive_version}.%{texlive_noarch}.1.2svn46702-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makeglos-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makeindex-%{texlive_version}.%{texlive_noarch}.svn52851-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makeplot-%{texlive_version}.%{texlive_noarch}.1.0.6svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-maker-%{texlive_version}.%{texlive_noarch}.1.0svn44823-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makerobust-%{texlive_version}.%{texlive_noarch}.2.0svn52811-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-makeshape-%{texlive_version}.%{texlive_noarch}.2.1svn28973-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mandi-%{texlive_version}.%{texlive_noarch}.2.7.5svn49720-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-manfnt-%{texlive_version}.%{texlive_noarch}.svn54684-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-manfnt-font-fonts-%{texlive_version}.%{texlive_noarch}.svn45777-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-manfnt-font
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/hoekwater/manfnt-font/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-manfnt-font
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-manfnt-font/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-manfnt-font/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-manfnt-font/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-manfnt-font/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-manfnt-font.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-manfnt-font    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-manfnt-font/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-manuscript-%{texlive_version}.%{texlive_noarch}.1.7svn36110-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-manyind-%{texlive_version}.%{texlive_noarch}.svn49874-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-marcellus-fonts-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-marcellus
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/marcellus/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/marcellus/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-marcellus
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-marcellus/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-marcellus/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-marcellus/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-marcellus/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-marcellus.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-marcellus    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-marcellus/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-marcellus.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-marcellus/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-marcellus.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-marcellus.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-margbib-%{texlive_version}.%{texlive_noarch}.1.0csvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-marginfit-%{texlive_version}.%{texlive_noarch}.1.1svn48281-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-marginfix-%{texlive_version}.%{texlive_noarch}.1.1svn31598-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-marginnote-%{texlive_version}.%{texlive_noarch}.1.4bsvn48383-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-markdown-%{texlive_version}.%{texlive_noarch}.2.8.2svn54482-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-marvosym-fonts-%{texlive_version}.%{texlive_noarch}.2.2asvn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-marvosym
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/marvosym/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/marvosym/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-marvosym
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-marvosym/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-marvosym/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-marvosym/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-marvosym/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-marvosym.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-marvosym    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-marvosym/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-marvosym.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-marvosym/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-marvosym.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-marvosym.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-matc3-%{texlive_version}.%{texlive_noarch}.1.0.1svn29845-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-matc3mem-%{texlive_version}.%{texlive_noarch}.1.1svn35773-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-match_parens-%{texlive_version}.%{texlive_noarch}.1.43svn36270-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/match_parens/match_parens
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-math-e-%{texlive_version}.%{texlive_noarch}.svn20062-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-math-into-latex-4-%{texlive_version}.%{texlive_noarch}.svn44131-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathabx-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathabx-type1-fonts-%{texlive_version}.%{texlive_noarch}.svn21129-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-mathabx-type1
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathabx-type1/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-mathabx-type1
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-mathabx-type1/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-mathabx-type1/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mathabx-type1/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mathabx-type1/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-mathabx-type1.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-mathabx-type1    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-mathabx-type1/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathalpha-%{texlive_version}.%{texlive_noarch}.1.13svn52305-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathastext-%{texlive_version}.%{texlive_noarch}.1.3wsvn52840-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathcommand-%{texlive_version}.%{texlive_noarch}.1.03svn53044-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathcomp-%{texlive_version}.%{texlive_noarch}.0.0.1fsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathdesign-fonts-%{texlive_version}.%{texlive_noarch}.2.31svn31639-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-mathdesign
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathdesign/mdbch/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathdesign/mdici/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathdesign/mdpgd/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathdesign/mdpus/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathdesign/mdput/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathdesign/mdugm/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-mathdesign
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-mathdesign/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-mathdesign/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mathdesign/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mathdesign/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-mathdesign.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-mathdesign    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-mathdesign/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathdots-%{texlive_version}.%{texlive_noarch}.0.0.9svn34301-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathexam-%{texlive_version}.%{texlive_noarch}.1.00svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathfam256-%{texlive_version}.%{texlive_noarch}.0.0.5svn53519-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathfixs-%{texlive_version}.%{texlive_noarch}.1.01svn49547-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathfont-%{texlive_version}.%{texlive_noarch}.1.6svn53035-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathlig-%{texlive_version}.%{texlive_noarch}.1.0svn54244-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathpartir-%{texlive_version}.%{texlive_noarch}.1.3.2svn39864-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathpazo-fonts-%{texlive_version}.%{texlive_noarch}.1.003svn52663-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-mathpazo
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/mathpazo/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-mathpazo
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-mathpazo/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-mathpazo/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mathpazo/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mathpazo/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-mathpazo.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-mathpazo    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-mathpazo/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathpunctspace-%{texlive_version}.%{texlive_noarch}.1.1svn46754-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-maths-symbols-%{texlive_version}.%{texlive_noarch}.3.4svn37763-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathspec-%{texlive_version}.%{texlive_noarch}.0.0.2bsvn42773-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathspic-%{texlive_version}.%{texlive_noarch}.1.13svn31957-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/mathspic/MATHSPIC.BAT
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mathtools-%{texlive_version}.%{texlive_noarch}.1.24svn54516-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-matlab-prettifier-%{texlive_version}.%{texlive_noarch}.0.0.3svn34323-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-matrix-skeleton-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mattens-%{texlive_version}.%{texlive_noarch}.1.3svn17582-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-maybemath-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mcaption-%{texlive_version}.%{texlive_noarch}.3.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mceinleger-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mcexam-%{texlive_version}.%{texlive_noarch}.0.0.4svn46155-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mcf2graph-%{texlive_version}.%{texlive_noarch}.4.48svn53550-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mcite-%{texlive_version}.%{texlive_noarch}.1.6svn18173-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mciteplus-%{texlive_version}.%{texlive_noarch}.1.2svn31648-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mcmthesis-%{texlive_version}.%{texlive_noarch}.6.3svn53513-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mdframed-%{texlive_version}.%{texlive_noarch}.1.9bsvn31075-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mdputu-%{texlive_version}.%{texlive_noarch}.1.2svn20298-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mdsymbol-fonts-%{texlive_version}.%{texlive_noarch}.0.0.5svn28399-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-mdsymbol
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/mdsymbol/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/mdsymbol/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-mdsymbol
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-mdsymbol/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-mdsymbol/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mdsymbol/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-mdsymbol/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-mdsymbol.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-mdsymbol    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-mdsymbol/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-mdsymbol.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-mdsymbol/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-mdsymbol.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-mdsymbol.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mdwtools-%{texlive_version}.%{texlive_noarch}.1.05.4svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-media4svg-%{texlive_version}.%{texlive_noarch}.0.0.4svn54773-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/tex/latex/media4svg/media4svg.lua
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-media9-%{texlive_version}.%{texlive_noarch}.1.10svn54554-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-medstarbeamer-%{texlive_version}.%{texlive_noarch}.svn38828-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-meetingmins-%{texlive_version}.%{texlive_noarch}.1.6svn31878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-memdesign-%{texlive_version}.%{texlive_noarch}.svn48664-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-memexsupp-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-memoir-%{texlive_version}.%{texlive_noarch}.3.7ksvn54554-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-memory-%{texlive_version}.%{texlive_noarch}.1.2svn30452-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-memorygraphs-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn49631-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mendex-doc-%{texlive_version}.%{texlive_noarch}.svn50268-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:277} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:278} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mensa-tex-%{texlive_version}.%{texlive_noarch}.svn45997-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:279} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:280} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-mentis-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:281} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:282} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove this
    rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
    rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
    rm -v  %{buildroot}%{_datadir}/texlive/texmf
    rm -v  %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -v  %{buildroot}%{_texmfmaindir}/tlpostcode
    rm -vr %{buildroot}%{_datadir}/texlive
    # Handle manual pages
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/man*/*.pdf
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/man*/*.pdf
    for path in %{buildroot}%{_texmfmaindir}/doc/man/man? \
               %{buildroot}%{_texmfdistdir}/doc/man/man?
    do
        test -d "$path" || continue
        sec=${path##*/}
        mkdir -p %{buildroot}%{_mandir}/${sec}
        for page in ${path}/*.*
        do
            test -e "$page" || continue
            mv -f $page %{buildroot}%{_mandir}/${sec}/
        done
    done
    rm -rf %{buildroot}%{_texmfmaindir}/doc/man
    rm -rf %{buildroot}%{_texmfdistdir}/doc/man
    find %{buildroot}%{_texmfmaindir}/ %{buildroot}%{_texmfdistdir}/ \
        -type f -a -perm /g+w,o+w | xargs --no-run-if-empty chmod g-w,o-w

%changelog
