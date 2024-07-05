#
# spec file for package texlive-specs-c.spec
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
##### WARNING: Please do not edit this auto generated spec file.
#

%define texlive_version  2024
%define texlive_previous 2022
%define texlive_release  20240311
%define texlive_noarch   216
%define biber_version    2.19

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

%if ! %{defined python3_bin_suffix}
%global python3_bin_suffix 3
%endif

Name:           texlive-specs-c
Version:        2024
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  mkfontdir
BuildRequires:  mkfontscale
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xorg-x11-fonts-core
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for c
License:        Artistic-2.0 and GPL-2.0-or-later and BSD-3-Clause and GPL-2.0-or-later and LPPL-1.0 and SUSE-Public-Domain and SUSE-TeX
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Group:          Productivity/Publishing/TeX/Base
Source0:        texlive-specs-c-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-bbding
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn17186
Release:        0
License:        LPPL-1.0
Summary:        A symbol (dingbat) font and LaTeX macros for its use
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bbding-doc >= %{texlive_version}
Provides:       tex(Uding.fd)
Provides:       tex(bbding.sty)
Provides:       tex(bbding10.tfm)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source1:        bbding.tar.xz
Source2:        bbding.doc.tar.xz

%description -n texlive-bbding
A symbol font (distributed as Metafont source) that contains
many of the symbols of the Zapf dingbats set, together with an
NFSS interface for using the font. An Adobe Type 1 version of
the fonts is available in the niceframe fonts bundle.

%package -n texlive-bbding-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn17186
Release:        0
Summary:        Documentation for texlive-bbding
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bbding and texlive-alldocumentation)

%description -n texlive-bbding-doc
This package includes the documentation for texlive-bbding

%post -n texlive-bbding
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bbding
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bbding
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bbding-doc
%{_texmfdistdir}/doc/latex/bbding/README
%{_texmfdistdir}/doc/latex/bbding/bbding.pdf
%{_texmfdistdir}/doc/latex/bbding/bbding10.org

%files -n texlive-bbding
%{_texmfdistdir}/fonts/source/public/bbding/bbding10.mf
%{_texmfdistdir}/fonts/tfm/public/bbding/bbding10.tfm
%{_texmfdistdir}/tex/latex/bbding/Uding.fd
%{_texmfdistdir}/tex/latex/bbding/bbding.sty

%package -n texlive-bbm
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        "Blackboard-style" cm fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bbm-doc >= %{texlive_version}
Provides:       tex(bbm10.tfm)
Provides:       tex(bbm12.tfm)
Provides:       tex(bbm17.tfm)
Provides:       tex(bbm5.tfm)
Provides:       tex(bbm6.tfm)
Provides:       tex(bbm7.tfm)
Provides:       tex(bbm8.tfm)
Provides:       tex(bbm9.tfm)
Provides:       tex(bbmb10.tfm)
Provides:       tex(bbmbx10.tfm)
Provides:       tex(bbmbx12.tfm)
Provides:       tex(bbmbx5.tfm)
Provides:       tex(bbmbx6.tfm)
Provides:       tex(bbmbx7.tfm)
Provides:       tex(bbmbx8.tfm)
Provides:       tex(bbmbx9.tfm)
Provides:       tex(bbmbxsl10.tfm)
Provides:       tex(bbmdunh10.tfm)
Provides:       tex(bbmfib8.tfm)
Provides:       tex(bbmfxib8.tfm)
Provides:       tex(bbmsl10.tfm)
Provides:       tex(bbmsl12.tfm)
Provides:       tex(bbmsl8.tfm)
Provides:       tex(bbmsl9.tfm)
Provides:       tex(bbmss10.tfm)
Provides:       tex(bbmss12.tfm)
Provides:       tex(bbmss17.tfm)
Provides:       tex(bbmss8.tfm)
Provides:       tex(bbmss9.tfm)
Provides:       tex(bbmssbx10.tfm)
Provides:       tex(bbmssdc10.tfm)
Provides:       tex(bbmssi10.tfm)
Provides:       tex(bbmssi12.tfm)
Provides:       tex(bbmssi17.tfm)
Provides:       tex(bbmssi8.tfm)
Provides:       tex(bbmssi9.tfm)
Provides:       tex(bbmssq8.tfm)
Provides:       tex(bbmssqi8.tfm)
Provides:       tex(bbmtt10.tfm)
Provides:       tex(bbmtt12.tfm)
Provides:       tex(bbmtt8.tfm)
Provides:       tex(bbmtt9.tfm)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source3:        bbm.tar.xz
Source4:        bbm.doc.tar.xz

%description -n texlive-bbm
Blackboard variants of Computer Modern fonts. The fonts are
distributed as Metafont source (only); LaTeX support is
available with the bbm-macros package. The Sauter font package
has Metafont parameter source files for building the fonts at
more sizes than you could reasonably imagine. A sample of these
fonts appears in the blackboard bold sampler.

%package -n texlive-bbm-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-bbm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bbm and texlive-alldocumentation)

%description -n texlive-bbm-doc
This package includes the documentation for texlive-bbm

%post -n texlive-bbm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bbm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bbm
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bbm-doc
%{_texmfdistdir}/doc/fonts/bbm/README
%{_texmfdistdir}/doc/fonts/bbm/gfbatch.batch
%{_texmfdistdir}/doc/fonts/bbm/mfbatch.batch
%{_texmfdistdir}/doc/fonts/bbm/test.tex

%files -n texlive-bbm
%{_texmfdistdir}/fonts/source/public/bbm/bbm10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm17.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm5.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm6.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm7.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbm9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmb10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx5.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx6.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx7.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbx9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmbxsl10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmdunh10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmfib8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmfxib8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbminch.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsl9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmsltt10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss17.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmss9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssbx10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssdc10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi17.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssi9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssq8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmssqi8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt10.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt12.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt8.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmtt9.mf
%{_texmfdistdir}/fonts/source/public/bbm/bbmvtt10.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbbase.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbord.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbordl.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbordsp.mf
%{_texmfdistdir}/fonts/source/public/bbm/blbordu.mf
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm5.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm6.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm7.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbm9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmdunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmfxib8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbm/bbmtt9.tfm

%package -n texlive-bbm-macros
Version:        %{texlive_version}.%{texlive_noarch}.svn17224
Release:        0
License:        LPPL-1.0
Summary:        LaTeX support for "blackboard-style" cm fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bbm-macros-doc >= %{texlive_version}
Provides:       tex(bbm.sty)
Provides:       tex(ubbm.fd)
Provides:       tex(ubbmss.fd)
Provides:       tex(ubbmtt.fd)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source5:        bbm-macros.tar.xz
Source6:        bbm-macros.doc.tar.xz

%description -n texlive-bbm-macros
Provides LaTeX support for Blackboard variants of Computer
Modern fonts. Declares a font family bbm so you can in
principle write running text in blackboard bold, and lots of
math alphabets for using the fonts within maths.

%package -n texlive-bbm-macros-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17224
Release:        0
Summary:        Documentation for texlive-bbm-macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bbm-macros and texlive-alldocumentation)

%description -n texlive-bbm-macros-doc
This package includes the documentation for texlive-bbm-macros

%post -n texlive-bbm-macros
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bbm-macros
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bbm-macros
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bbm-macros-doc
%{_texmfdistdir}/doc/latex/bbm-macros/README
%{_texmfdistdir}/doc/latex/bbm-macros/bbm.pdf

%files -n texlive-bbm-macros
%{_texmfdistdir}/tex/latex/bbm-macros/bbm.sty
%{_texmfdistdir}/tex/latex/bbm-macros/ubbm.fd
%{_texmfdistdir}/tex/latex/bbm-macros/ubbmss.fd
%{_texmfdistdir}/tex/latex/bbm-macros/ubbmtt.fd

%package -n texlive-bbold
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn17187
Release:        0
License:        BSD-3-Clause
Summary:        Sans serif blackboard bold
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bbold-doc >= %{texlive_version}
Provides:       tex(Ubbold.fd)
Provides:       tex(bbold.sty)
Provides:       tex(bbold10.tfm)
Provides:       tex(bbold12.tfm)
Provides:       tex(bbold17.tfm)
Provides:       tex(bbold5.tfm)
Provides:       tex(bbold6.tfm)
Provides:       tex(bbold7.tfm)
Provides:       tex(bbold8.tfm)
Provides:       tex(bbold9.tfm)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source7:        bbold.tar.xz
Source8:        bbold.doc.tar.xz
Source9:        bbold_bbold11.dif

%description -n texlive-bbold
A geometric sans serif blackboard bold font, for use in
mathematics; Metafont sources are provided, as well as macros
for use with LaTeX. The Sauter font package has Metafont
parameter source files for building the fonts at more sizes
than you could reasonably imagine. See the blackboard sampler
for a feel for the font's appearance.

%package -n texlive-bbold-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn17187
Release:        0
Summary:        Documentation for texlive-bbold
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bbold and texlive-alldocumentation)

%description -n texlive-bbold-doc
This package includes the documentation for texlive-bbold

%post -n texlive-bbold
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bbold
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bbold
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bbold-doc
%{_texmfdistdir}/doc/latex/bbold/INSTALL
%{_texmfdistdir}/doc/latex/bbold/README
%{_texmfdistdir}/doc/latex/bbold/bbold.pdf

%files -n texlive-bbold
%{_texmfdistdir}/fonts/source/public/bbold/bbbase.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbgreekl.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbgreeku.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbligs.mf
%{_texmfdistdir}/fonts/source/public/bbold/bblower.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbnum.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold10.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold12.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold17.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold5.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold6.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold7.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold8.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold9.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbparams.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbpunc.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbupper.mf
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold5.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold6.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold7.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold9.tfm
%{_texmfdistdir}/tex/latex/bbold/Ubbold.fd
%{_texmfdistdir}/tex/latex/bbold/bbold.sty
%{_texmfdistdir}/fonts/source/public/bbold/bbold11.mf

%package -n texlive-bbold-type1
Version:        %{texlive_version}.%{texlive_noarch}.svn33143
Release:        0
License:        LPPL-1.0
Summary:        An Adobe Type 1 format version of the bbold font
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Requires:       texlive-bbold-type1-fonts >= %{texlive_version}
Suggests:       texlive-bbold-type1-doc >= %{texlive_version}
Provides:       tex(bbold.map)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source10:       bbold-type1.tar.xz
Source11:       bbold-type1.doc.tar.xz

%description -n texlive-bbold-type1
The files offer an Adobe Type 1 format version of the 5pt, 7pt
and 10pt versions of the bbold fonts. The distribution also
includes a map file, for use when incorporating the fonts into
TeX documents; the macros provided with the original Metafont
version of the font serve for the scaleable version, too. The
fonts were produced to be part of the TeX distribution from
Y&Y; they were generously donated to the TeX Users Group when
Y&Y closed its doors as a business.

%package -n texlive-bbold-type1-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn33143
Release:        0
Summary:        Documentation for texlive-bbold-type1
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bbold-type1 and texlive-alldocumentation)

%description -n texlive-bbold-type1-doc
This package includes the documentation for texlive-bbold-type1

%package -n texlive-bbold-type1-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn33143
Release:        0
Summary:        Severed fonts for texlive-bbold-type1
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

%description -n texlive-bbold-type1-fonts
The  separated fonts package for texlive-bbold-type1

%post -n texlive-bbold-type1
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap bbold.map' >> /var/run/texlive/run-updmap

%postun -n texlive-bbold-type1
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap bbold.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-bbold-type1
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-bbold-type1-fonts

%files -n texlive-bbold-type1-doc
%{_texmfdistdir}/doc/fonts/bbold-type1/README
%{_texmfdistdir}/doc/fonts/bbold-type1/test.pdf
%{_texmfdistdir}/doc/fonts/bbold-type1/test.tex

%files -n texlive-bbold-type1
%{_texmfdistdir}/fonts/afm/public/bbold-type1/bbold10.afm
%{_texmfdistdir}/fonts/afm/public/bbold-type1/bbold5.afm
%{_texmfdistdir}/fonts/afm/public/bbold-type1/bbold7.afm
%{_texmfdistdir}/fonts/map/dvips/bbold-type1/bbold.map
%verify(link) %{_texmfdistdir}/fonts/type1/public/bbold-type1/bbold10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bbold-type1/bbold5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bbold-type1/bbold7.pfb

%files -n texlive-bbold-type1-fonts
%dir %{_datadir}/fonts/texlive-bbold-type1
%{_datadir}/fontconfig/conf.avail/58-texlive-bbold-type1.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bbold-type1/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bbold-type1/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bbold-type1/fonts.scale
%{_datadir}/fonts/texlive-bbold-type1/bbold10.pfb
%{_datadir}/fonts/texlive-bbold-type1/bbold5.pfb
%{_datadir}/fonts/texlive-bbold-type1/bbold7.pfb

%package -n texlive-bboldx
Version:        %{texlive_version}.%{texlive_noarch}.1.032svn65424
Release:        0
License:        LPPL-1.0
Summary:        Extension of the bbold package with a Blackboard Bold alphabet
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Requires:       texlive-bboldx-fonts >= %{texlive_version}
Suggests:       texlive-bboldx-doc >= %{texlive_version}
Provides:       tex(BBOLDX-Bold.tfm)
Provides:       tex(BBOLDX-Regular.tfm)
Provides:       tex(BBOLDX-Thin.tfm)
Provides:       tex(Ubboldx.fd)
Provides:       tex(bboldx.enc)
Provides:       tex(bboldx.map)
Provides:       tex(bboldx.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source12:       bboldx.tar.xz
Source13:       bboldx.doc.tar.xz

%description -n texlive-bboldx
Extension of bbold to a package with three weights, of which
the original is considered as light and the additions as
regular and bold.

%package -n texlive-bboldx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.032svn65424
Release:        0
Summary:        Documentation for texlive-bboldx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bboldx and texlive-alldocumentation)

%description -n texlive-bboldx-doc
This package includes the documentation for texlive-bboldx

%package -n texlive-bboldx-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.032svn65424
Release:        0
Summary:        Severed fonts for texlive-bboldx
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

%description -n texlive-bboldx-fonts
The  separated fonts package for texlive-bboldx

%post -n texlive-bboldx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap bboldx.map' >> /var/run/texlive/run-updmap

%postun -n texlive-bboldx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap bboldx.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-bboldx
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-bboldx-fonts

%files -n texlive-bboldx-doc
%{_texmfdistdir}/doc/fonts/bboldx/Bboldx-doc.pdf
%{_texmfdistdir}/doc/fonts/bboldx/Bboldx-doc.tex
%{_texmfdistdir}/doc/fonts/bboldx/README

%files -n texlive-bboldx
%{_texmfdistdir}/fonts/afm/public/bboldx/BBOLDX-Bold.afm
%{_texmfdistdir}/fonts/afm/public/bboldx/BBOLDX-Regular.afm
%{_texmfdistdir}/fonts/afm/public/bboldx/BBOLDX-Thin.afm
%{_texmfdistdir}/fonts/enc/dvips/bboldx/bboldx.enc
%{_texmfdistdir}/fonts/map/dvips/bboldx/bboldx.map
%{_texmfdistdir}/fonts/tfm/public/bboldx/BBOLDX-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/bboldx/BBOLDX-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/bboldx/BBOLDX-Thin.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/bboldx/BBOLDX-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bboldx/BBOLDX-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bboldx/BBOLDX-Thin.pfb
%{_texmfdistdir}/tex/latex/bboldx/Ubboldx.fd
%{_texmfdistdir}/tex/latex/bboldx/bboldx.sty

%files -n texlive-bboldx-fonts
%dir %{_datadir}/fonts/texlive-bboldx
%{_datadir}/fontconfig/conf.avail/58-texlive-bboldx.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bboldx/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bboldx/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bboldx/fonts.scale
%{_datadir}/fonts/texlive-bboldx/BBOLDX-Bold.pfb
%{_datadir}/fonts/texlive-bboldx/BBOLDX-Regular.pfb
%{_datadir}/fonts/texlive-bboldx/BBOLDX-Thin.pfb

%package -n texlive-bchart
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.3svn43928
Release:        0
License:        LPPL-1.0
Summary:        Draw simple bar charts in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bchart-doc >= %{texlive_version}
Provides:       tex(bchart.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source14:       bchart.tar.xz
Source15:       bchart.doc.tar.xz

%description -n texlive-bchart
The package provides horizontal bar charts, drawn using TikZ on
a numeric X-axis. The focus of the package is simplicity and
aesthetics.

%package -n texlive-bchart-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.3svn43928
Release:        0
Summary:        Documentation for texlive-bchart
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bchart and texlive-alldocumentation)

%description -n texlive-bchart-doc
This package includes the documentation for texlive-bchart

%post -n texlive-bchart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bchart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bchart
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bchart-doc
%{_texmfdistdir}/doc/latex/bchart/CHANGES.txt
%{_texmfdistdir}/doc/latex/bchart/LICENSE.txt
%{_texmfdistdir}/doc/latex/bchart/README.md
%{_texmfdistdir}/doc/latex/bchart/bchart.pdf
%{_texmfdistdir}/doc/latex/bchart/bchart.tex

%files -n texlive-bchart
%{_texmfdistdir}/tex/latex/bchart/bchart.sty

%package -n texlive-bclogo
Version:        %{texlive_version}.%{texlive_noarch}.3.15svn69578
Release:        0
License:        LPPL-1.0
Summary:        Creating colourful boxes with logos
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bclogo-doc >= %{texlive_version}
Provides:       tex(bclogo.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(pst-blur.sty)
Requires:       tex(pst-coil.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source16:       bclogo.tar.xz
Source17:       bclogo.doc.tar.xz

%description -n texlive-bclogo
The package facilitates the creation of colorful boxes with a
title and logo. It may use either TikZ or PSTricks as graphics
engine.

%package -n texlive-bclogo-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.15svn69578
Release:        0
Summary:        Documentation for texlive-bclogo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bclogo and texlive-alldocumentation)
Provides:       locale(texlive-bclogo-doc:fr)

%description -n texlive-bclogo-doc
This package includes the documentation for texlive-bclogo

%post -n texlive-bclogo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bclogo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bclogo
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bclogo-doc
%{_texmfdistdir}/doc/latex/bclogo/LICENSE
%{_texmfdistdir}/doc/latex/bclogo/README.md
%{_texmfdistdir}/doc/latex/bclogo/bclogo-doc.pdf
%{_texmfdistdir}/doc/latex/bclogo/bclogo-doc.tex
%{_texmfdistdir}/doc/latex/bclogo/bclogo.pdf
%{_texmfdistdir}/doc/latex/bclogo/brace.mps
%{_texmfdistdir}/doc/latex/bclogo/fond.pdf
%{_texmfdistdir}/doc/latex/bclogo/losanges.mps
%{_texmfdistdir}/doc/latex/bclogo/spir.mps
%{_texmfdistdir}/doc/latex/bclogo/syracuse-crop.pdf
%{_texmfdistdir}/doc/latex/bclogo/syracuse.pdf
%{_texmfdistdir}/doc/latex/bclogo/syracuse.tex
%{_texmfdistdir}/doc/latex/bclogo/toto.txt

%files -n texlive-bclogo
%{_texmfdistdir}/metapost/bclogo/bc-attention.mp
%{_texmfdistdir}/metapost/bclogo/bc-aux-301.mp
%{_texmfdistdir}/metapost/bclogo/bc-bombe.mp
%{_texmfdistdir}/metapost/bclogo/bc-book.mp
%{_texmfdistdir}/metapost/bclogo/bc-calendrier.mp
%{_texmfdistdir}/metapost/bclogo/bc-cle.mp
%{_texmfdistdir}/metapost/bclogo/bc-clefa.mp
%{_texmfdistdir}/metapost/bclogo/bc-clesol.mp
%{_texmfdistdir}/metapost/bclogo/bc-coeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-crayon.mp
%{_texmfdistdir}/metapost/bclogo/bc-cube.mp
%{_texmfdistdir}/metapost/bclogo/bc-dallemagne.mp
%{_texmfdistdir}/metapost/bclogo/bc-danger.mp
%{_texmfdistdir}/metapost/bclogo/bc-dautriche.mp
%{_texmfdistdir}/metapost/bclogo/bc-dbelgique.mp
%{_texmfdistdir}/metapost/bclogo/bc-dbulgarie.mp
%{_texmfdistdir}/metapost/bclogo/bc-dfrance.mp
%{_texmfdistdir}/metapost/bclogo/bc-ditalie.mp
%{_texmfdistdir}/metapost/bclogo/bc-dluxembourg.mp
%{_texmfdistdir}/metapost/bclogo/bc-dodecaedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-dpaysbas.mp
%{_texmfdistdir}/metapost/bclogo/bc-dz.mp
%{_texmfdistdir}/metapost/bclogo/bc-eclaircie.mp
%{_texmfdistdir}/metapost/bclogo/bc-etoile.mp
%{_texmfdistdir}/metapost/bclogo/bc-femme.mp
%{_texmfdistdir}/metapost/bclogo/bc-feujaune.mp
%{_texmfdistdir}/metapost/bclogo/bc-feurouge.mp
%{_texmfdistdir}/metapost/bclogo/bc-feutricolore.mp
%{_texmfdistdir}/metapost/bclogo/bc-feuvert.mp
%{_texmfdistdir}/metapost/bclogo/bc-fleur.mp
%{_texmfdistdir}/metapost/bclogo/bc-homme.mp
%{_texmfdistdir}/metapost/bclogo/bc-horloge.mp
%{_texmfdistdir}/metapost/bclogo/bc-icosaedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-info.mp
%{_texmfdistdir}/metapost/bclogo/bc-inter.mp
%{_texmfdistdir}/metapost/bclogo/bc-interdit.mp
%{_texmfdistdir}/metapost/bclogo/bc-lampe.mp
%{_texmfdistdir}/metapost/bclogo/bc-loupe.mp
%{_texmfdistdir}/metapost/bclogo/bc-neige.mp
%{_texmfdistdir}/metapost/bclogo/bc-note.mp
%{_texmfdistdir}/metapost/bclogo/bc-nucleaire.mp
%{_texmfdistdir}/metapost/bclogo/bc-octaedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-oeil.mp
%{_texmfdistdir}/metapost/bclogo/bc-orne.mp
%{_texmfdistdir}/metapost/bclogo/bc-ours.mp
%{_texmfdistdir}/metapost/bclogo/bc-outil.mp
%{_texmfdistdir}/metapost/bclogo/bc-peaceandlove.mp
%{_texmfdistdir}/metapost/bclogo/bc-pluie.mp
%{_texmfdistdir}/metapost/bclogo/bc-plume.mp
%{_texmfdistdir}/metapost/bclogo/bc-poisson.mp
%{_texmfdistdir}/metapost/bclogo/bc-recyclage.mp
%{_texmfdistdir}/metapost/bclogo/bc-rosevents.mp
%{_texmfdistdir}/metapost/bclogo/bc-smiley-bonnehumeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-smiley-mauvaisehumeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-soleil.mp
%{_texmfdistdir}/metapost/bclogo/bc-stop.mp
%{_texmfdistdir}/metapost/bclogo/bc-takecare.mp
%{_texmfdistdir}/metapost/bclogo/bc-tetraedre.mp
%{_texmfdistdir}/metapost/bclogo/bc-trefle.mp
%{_texmfdistdir}/metapost/bclogo/bc-trombone.mp
%{_texmfdistdir}/metapost/bclogo/bc-valetcoeur.mp
%{_texmfdistdir}/metapost/bclogo/bc-velo.mp
%{_texmfdistdir}/metapost/bclogo/bc-yin.mp
%{_texmfdistdir}/metapost/bclogo/brace.mp
%{_texmfdistdir}/metapost/bclogo/losanges.mp
%{_texmfdistdir}/metapost/bclogo/spir.mp
%{_texmfdistdir}/tex/latex/bclogo/bc-attention.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-aux-301.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-bombe.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-book.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-calendrier.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-cle.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-clefa.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-clesol.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-coeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-crayon.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-cube.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dallemagne.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-danger.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dautriche.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dbelgique.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dbulgarie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dfrance.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-ditalie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dluxembourg.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dodecaedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dpaysbas.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-dz.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-eclaircie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-etoile.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-femme.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feujaune.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feurouge.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feutricolore.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-feuvert.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-fleur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-homme.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-horloge.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-icosaedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-info.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-inter.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-interdit.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-lampe.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-loupe.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-neige.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-note.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-nucleaire.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-octaedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-oeil.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-orne.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-ours.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-outil.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-peaceandlove.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-pluie.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-plume.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-poisson.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-recyclage.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-rosevents.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-smiley-bonnehumeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-smiley-mauvaisehumeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-soleil.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-stop.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-takecare.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-tetraedre.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-trefle.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-trombone.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-valetcoeur.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-velo.mps
%{_texmfdistdir}/tex/latex/bclogo/bc-yin.mps
%{_texmfdistdir}/tex/latex/bclogo/bclogo.sty

%package -n texlive-beamer
Version:        %{texlive_version}.%{texlive_noarch}.3.71svn69316
Release:        0
License:        LPPL-1.0
Summary:        A LaTeX class for producing presentations and slides
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-amscls >= %{texlive_version}
#!BuildIgnore: texlive-amscls
Requires:       texlive-amsfonts >= %{texlive_version}
#!BuildIgnore: texlive-amsfonts
Requires:       texlive-amsmath >= %{texlive_version}
#!BuildIgnore: texlive-amsmath
Requires:       texlive-atbegshi >= %{texlive_version}
#!BuildIgnore: texlive-atbegshi
Requires:       texlive-etoolbox >= %{texlive_version}
#!BuildIgnore: texlive-etoolbox
Requires:       texlive-geometry >= %{texlive_version}
#!BuildIgnore: texlive-geometry
Requires:       texlive-hyperref >= %{texlive_version}
#!BuildIgnore: texlive-hyperref
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires:       texlive-translator >= %{texlive_version}
#!BuildIgnore: texlive-translator
Requires:       texlive-xcolor >= %{texlive_version}
#!BuildIgnore: texlive-xcolor
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamer-doc >= %{texlive_version}
Provides:       tex(beamer.cls)
Provides:       tex(beamerarticle.sty)
Provides:       tex(beamerbasearticle.sty)
Provides:       tex(beamerbaseauxtemplates.sty)
Provides:       tex(beamerbaseboxes.sty)
Provides:       tex(beamerbasecolor.sty)
Provides:       tex(beamerbasecompatibility.sty)
Provides:       tex(beamerbasedecode.sty)
Provides:       tex(beamerbasefont.sty)
Provides:       tex(beamerbaseframe.sty)
Provides:       tex(beamerbaseframecomponents.sty)
Provides:       tex(beamerbaseframesize.sty)
Provides:       tex(beamerbaselocalstructure.sty)
Provides:       tex(beamerbasemisc.sty)
Provides:       tex(beamerbasemodes.sty)
Provides:       tex(beamerbasenavigation.sty)
Provides:       tex(beamerbasenavigationsymbols.tex)
Provides:       tex(beamerbasenotes.sty)
Provides:       tex(beamerbaseoptions.sty)
Provides:       tex(beamerbaseoverlay.sty)
Provides:       tex(beamerbaserequires.sty)
Provides:       tex(beamerbasesection.sty)
Provides:       tex(beamerbasetemplates.sty)
Provides:       tex(beamerbasethemes.sty)
Provides:       tex(beamerbasetheorems.sty)
Provides:       tex(beamerbasetitle.sty)
Provides:       tex(beamerbasetoc.sty)
Provides:       tex(beamerbasetranslator.sty)
Provides:       tex(beamerbasetwoscreens.sty)
Provides:       tex(beamerbaseverbatim.sty)
Provides:       tex(beamercolorthemealbatross.sty)
Provides:       tex(beamercolorthemebeaver.sty)
Provides:       tex(beamercolorthemebeetle.sty)
Provides:       tex(beamercolorthemecrane.sty)
Provides:       tex(beamercolorthemedefault.sty)
Provides:       tex(beamercolorthemedolphin.sty)
Provides:       tex(beamercolorthemedove.sty)
Provides:       tex(beamercolorthemefly.sty)
Provides:       tex(beamercolorthemelily.sty)
Provides:       tex(beamercolorthememonarca.sty)
Provides:       tex(beamercolorthemeorchid.sty)
Provides:       tex(beamercolorthemerose.sty)
Provides:       tex(beamercolorthemeseagull.sty)
Provides:       tex(beamercolorthemeseahorse.sty)
Provides:       tex(beamercolorthemesidebartab.sty)
Provides:       tex(beamercolorthemespruce.sty)
Provides:       tex(beamercolorthemestructure.sty)
Provides:       tex(beamercolorthemewhale.sty)
Provides:       tex(beamercolorthemewolverine.sty)
Provides:       tex(beamerfoils.sty)
Provides:       tex(beamerfontthemedefault.sty)
Provides:       tex(beamerfontthemeprofessionalfonts.sty)
Provides:       tex(beamerfontthemeserif.sty)
Provides:       tex(beamerfontthemestructurebold.sty)
Provides:       tex(beamerfontthemestructureitalicserif.sty)
Provides:       tex(beamerfontthemestructuresmallcapsserif.sty)
Provides:       tex(beamericonarticle.tex)
Provides:       tex(beamericonbook.tex)
Provides:       tex(beamerinnerthemecircles.sty)
Provides:       tex(beamerinnerthemedefault.sty)
Provides:       tex(beamerinnerthemeinmargin.sty)
Provides:       tex(beamerinnerthemerectangles.sty)
Provides:       tex(beamerinnerthemerounded.sty)
Provides:       tex(beamerouterthemedefault.sty)
Provides:       tex(beamerouterthemeinfolines.sty)
Provides:       tex(beamerouterthememiniframes.sty)
Provides:       tex(beamerouterthemeshadow.sty)
Provides:       tex(beamerouterthemesidebar.sty)
Provides:       tex(beamerouterthemesmoothbars.sty)
Provides:       tex(beamerouterthemesmoothtree.sty)
Provides:       tex(beamerouterthemesplit.sty)
Provides:       tex(beamerouterthemetree.sty)
Provides:       tex(beamerpatchparalist.sty)
Provides:       tex(beamerprosper.sty)
Provides:       tex(beamerseminar.sty)
Provides:       tex(beamertexpower.sty)
Provides:       tex(beamerthemeAnnArbor.sty)
Provides:       tex(beamerthemeAntibes.sty)
Provides:       tex(beamerthemeBergen.sty)
Provides:       tex(beamerthemeBerkeley.sty)
Provides:       tex(beamerthemeBerlin.sty)
Provides:       tex(beamerthemeBoadilla.sty)
Provides:       tex(beamerthemeCambridgeUS.sty)
Provides:       tex(beamerthemeCopenhagen.sty)
Provides:       tex(beamerthemeDarmstadt.sty)
Provides:       tex(beamerthemeDresden.sty)
Provides:       tex(beamerthemeEastLansing.sty)
Provides:       tex(beamerthemeFrankfurt.sty)
Provides:       tex(beamerthemeGoettingen.sty)
Provides:       tex(beamerthemeHannover.sty)
Provides:       tex(beamerthemeIlmenau.sty)
Provides:       tex(beamerthemeJuanLesPins.sty)
Provides:       tex(beamerthemeLuebeck.sty)
Provides:       tex(beamerthemeMadrid.sty)
Provides:       tex(beamerthemeMalmoe.sty)
Provides:       tex(beamerthemeMarburg.sty)
Provides:       tex(beamerthemeMontpellier.sty)
Provides:       tex(beamerthemePaloAlto.sty)
Provides:       tex(beamerthemePittsburgh.sty)
Provides:       tex(beamerthemeRochester.sty)
Provides:       tex(beamerthemeSingapore.sty)
Provides:       tex(beamerthemeSzeged.sty)
Provides:       tex(beamerthemeWarsaw.sty)
Provides:       tex(beamerthemebars.sty)
Provides:       tex(beamerthemeboxes.sty)
Provides:       tex(beamerthemeclassic.sty)
Provides:       tex(beamerthemecompatibility.sty)
Provides:       tex(beamerthemedefault.sty)
Provides:       tex(beamerthemelined.sty)
Provides:       tex(beamerthemeplain.sty)
Provides:       tex(beamerthemeshadow.sty)
Provides:       tex(beamerthemesidebar.sty)
Provides:       tex(beamerthemesplit.sty)
Provides:       tex(beamerthemetree.sty)
Provides:       tex(multimedia.sty)
Provides:       tex(multimediasymbols.sty)
Provides:       tex(xmpmulti.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfcore.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(pgfpages.sty)
Requires:       tex(sansmathaccent.sty)
Requires:       tex(translator.sty)
Requires:       tex(ucs.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xxcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source18:       beamer.tar.xz
Source19:       beamer.doc.tar.xz

%description -n texlive-beamer
The beamer LaTeX class can be used for producing slides. The
class works in both PostScript and direct PDF output modes,
using the pgf graphics system for visual effects. Content is
created in the frame environment, and each frame can be made up
of a number of slides using a simple notation for specifying
material to appear on each slide within a frame. Short versions
of title, authors, institute can also be specified as optional
parameters. Whole frame graphics are supported by plain frames.
The class supports figure and table environments, transparency
effects, varying slide transitions and animations. Beamer also
provides compatibility with other packages like prosper. The
package now incorporates the functionality of the former
translator package, which is used for customising the package
for use in other language environments. Beamer depends on the
following other packages: atbegshi, etoolbox, hyperref, ifpdf,
pgf, and translator.

%package -n texlive-beamer-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.71svn69316
Release:        0
Summary:        Documentation for texlive-beamer
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamer and texlive-alldocumentation)

%description -n texlive-beamer-doc
This package includes the documentation for texlive-beamer

%post -n texlive-beamer
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamer
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamer
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamer-doc
%{_texmfdistdir}/doc/latex/beamer/AUTHORS.md
%{_texmfdistdir}/doc/latex/beamer/CHANGELOG.md
%{_texmfdistdir}/doc/latex/beamer/LICENSE.md
%{_texmfdistdir}/doc/latex/beamer/README.md
%{_texmfdistdir}/doc/latex/beamer/beamercolorthemeexample.tex
%{_texmfdistdir}/doc/latex/beamer/beamerexample-conference-talk.pdf
%{_texmfdistdir}/doc/latex/beamer/beamerexample-lecture-beamer-version.pdf
%{_texmfdistdir}/doc/latex/beamer/beamerexample-lecture-print-version.pdf
%{_texmfdistdir}/doc/latex/beamer/beamerfontthemeexample.tex
%{_texmfdistdir}/doc/latex/beamer/beamerinnerthemeexample.tex
%{_texmfdistdir}/doc/latex/beamer/beamerlogo.pdf
%{_texmfdistdir}/doc/latex/beamer/beamerouterthemeexample.tex
%{_texmfdistdir}/doc/latex/beamer/beamerthemeexample.tex
%{_texmfdistdir}/doc/latex/beamer/beamerthemeexamplebase.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-animations.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-color.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-compatibility.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-elements.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-emulation.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-fonts.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-frames.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-globalstructure.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-graphics.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-guidelines.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-installation.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-interaction.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-introduction.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-license.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-localstructure.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-macros.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-nonpresentation.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-notes.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-overlays.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-solutions.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-themes.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-transparencies.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-tricks.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-tutorial.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-twoscreens.tex
%{_texmfdistdir}/doc/latex/beamer/beamerug-workflow.tex
%{_texmfdistdir}/doc/latex/beamer/beameruserguide.pdf
%{_texmfdistdir}/doc/latex/beamer/beameruserguide.tex
%{_texmfdistdir}/doc/latex/beamer/emulation-examples/beamerexample-foils.tex
%{_texmfdistdir}/doc/latex/beamer/emulation-examples/beamerexample-prosper.tex
%{_texmfdistdir}/doc/latex/beamer/emulation-examples/beamerexample-seminar.tex
%{_texmfdistdir}/doc/latex/beamer/emulation-examples/beamerexample-texpower.tex
%{_texmfdistdir}/doc/latex/beamer/examples/a-conference-talk/beamerexample-conference-talk.tex
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-beamer-version.tex
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-body.tex
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-logo.pdf
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic1.jpg
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic2.jpg
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic3.jpg
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic4.jpg
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic5.jpg
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-pic6.jpg
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-print-version.tex
%{_texmfdistdir}/doc/latex/beamer/examples/a-lecture/beamerexample-lecture-style.tex
%{_texmfdistdir}/doc/latex/beamer/licenses/fdl.txt
%{_texmfdistdir}/doc/latex/beamer/licenses/gpl-2.0.txt
%{_texmfdistdir}/doc/latex/beamer/licenses/lppl-1-3c.txt
%{_texmfdistdir}/doc/latex/beamer/licenses/manifest-code.txt
%{_texmfdistdir}/doc/latex/beamer/licenses/manifest-documentation.txt
%{_texmfdistdir}/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.de.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.en.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/conference-talks/conference-ornate-20min.fr.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.de.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.en.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/generic-talks/generic-ornate-15min-45min.fr.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.de.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.en.tex
%{_texmfdistdir}/doc/latex/beamer/solutions/short-talks/speaker_introduction-ornate-2min.fr.tex

%files -n texlive-beamer
%{_texmfdistdir}/tex/latex/beamer/beamer.cls
%{_texmfdistdir}/tex/latex/beamer/beamerarticle.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasearticle.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseauxtemplates.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseboxes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasecolor.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasecompatibility.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasedecode.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasefont.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseframe.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseframecomponents.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseframesize.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaselocalstructure.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasemisc.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasemodes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasenavigation.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasenavigationsymbols.tex
%{_texmfdistdir}/tex/latex/beamer/beamerbasenotes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseoptions.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseoverlay.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaserequires.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasesection.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetemplates.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasethemes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetheorems.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetitle.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetoc.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetranslator.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbasetwoscreens.sty
%{_texmfdistdir}/tex/latex/beamer/beamerbaseverbatim.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemealbatross.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemebeaver.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemebeetle.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemecrane.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemedolphin.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemedove.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemefly.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemelily.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthememonarca.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemeorchid.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemerose.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemeseagull.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemeseahorse.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemesidebartab.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemespruce.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemestructure.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemewhale.sty
%{_texmfdistdir}/tex/latex/beamer/beamercolorthemewolverine.sty
%{_texmfdistdir}/tex/latex/beamer/beamerfoils.sty
%{_texmfdistdir}/tex/latex/beamer/beamerfontthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/beamerfontthemeprofessionalfonts.sty
%{_texmfdistdir}/tex/latex/beamer/beamerfontthemeserif.sty
%{_texmfdistdir}/tex/latex/beamer/beamerfontthemestructurebold.sty
%{_texmfdistdir}/tex/latex/beamer/beamerfontthemestructureitalicserif.sty
%{_texmfdistdir}/tex/latex/beamer/beamerfontthemestructuresmallcapsserif.sty
%{_texmfdistdir}/tex/latex/beamer/beamericonarticle.20.eps
%{_texmfdistdir}/tex/latex/beamer/beamericonarticle.20.pdf
%{_texmfdistdir}/tex/latex/beamer/beamericonarticle.eps
%{_texmfdistdir}/tex/latex/beamer/beamericonarticle.pdf
%{_texmfdistdir}/tex/latex/beamer/beamericonarticle.tex
%{_texmfdistdir}/tex/latex/beamer/beamericonbook.20.eps
%{_texmfdistdir}/tex/latex/beamer/beamericonbook.20.pdf
%{_texmfdistdir}/tex/latex/beamer/beamericonbook.eps
%{_texmfdistdir}/tex/latex/beamer/beamericonbook.pdf
%{_texmfdistdir}/tex/latex/beamer/beamericonbook.tex
%{_texmfdistdir}/tex/latex/beamer/beamericononline.20.eps
%{_texmfdistdir}/tex/latex/beamer/beamericononline.20.pdf
%{_texmfdistdir}/tex/latex/beamer/beamericononline.eps
%{_texmfdistdir}/tex/latex/beamer/beamericononline.pdf
%{_texmfdistdir}/tex/latex/beamer/beamerinnerthemecircles.sty
%{_texmfdistdir}/tex/latex/beamer/beamerinnerthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/beamerinnerthemeinmargin.sty
%{_texmfdistdir}/tex/latex/beamer/beamerinnerthemerectangles.sty
%{_texmfdistdir}/tex/latex/beamer/beamerinnerthemerounded.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemeinfolines.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthememiniframes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemeshadow.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemesidebar.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemesmoothbars.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemesmoothtree.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemesplit.sty
%{_texmfdistdir}/tex/latex/beamer/beamerouterthemetree.sty
%{_texmfdistdir}/tex/latex/beamer/beamerpatchparalist.sty
%{_texmfdistdir}/tex/latex/beamer/beamerprosper.sty
%{_texmfdistdir}/tex/latex/beamer/beamerseminar.sty
%{_texmfdistdir}/tex/latex/beamer/beamertexpower.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeAnnArbor.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeAntibes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeBergen.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeBerkeley.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeBerlin.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeBoadilla.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeCambridgeUS.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeCopenhagen.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeDarmstadt.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeDresden.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeEastLansing.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeFrankfurt.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeGoettingen.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeHannover.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeIlmenau.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeJuanLesPins.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeLuebeck.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeMadrid.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeMalmoe.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeMarburg.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeMontpellier.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemePaloAlto.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemePittsburgh.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeRochester.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeSingapore.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeSzeged.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeWarsaw.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemebars.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeboxes.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeclassic.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemecompatibility.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemedefault.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemelined.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeplain.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemeshadow.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemesidebar.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemesplit.sty
%{_texmfdistdir}/tex/latex/beamer/beamerthemetree.sty
%{_texmfdistdir}/tex/latex/beamer/multimedia.sty
%{_texmfdistdir}/tex/latex/beamer/multimediasymbols.sty
%{_texmfdistdir}/tex/latex/beamer/xmpmulti.sty

%package -n texlive-beamer-fuberlin
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02bsvn63161
Release:        0
License:        LPPL-1.0
Summary:        Beamer, using the style of FU Berlin
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamer-fuberlin-doc >= %{texlive_version}
Provides:       tex(FUbeamer.cls)
Provides:       tex(beamercolorthemeBerlinFU.sty)
Provides:       tex(beamerfontthemeBerlinFU.sty)
Provides:       tex(beamerouterthemeBerlinFU.sty)
Provides:       tex(beamerthemeBerlinFU.sty)
Requires:       tex(babel.sty)
Requires:       tex(beamer.cls)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx-psmin.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source20:       beamer-fuberlin.tar.xz
Source21:       beamer-fuberlin.doc.tar.xz

%description -n texlive-beamer-fuberlin
The bundle provides a beamer-derived class and a theme style
file for the corporate design of the Free University in Berlin.
Users may use the class itself (FUbeamer) or use the theme in
the usual way with \usetheme{BerlinFU}. Examples of using both
the class and the theme are provided; the PDF is visually
identical, so the catalogue only lists one; the sources of the
examples do of course differ.

%package -n texlive-beamer-fuberlin-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02bsvn63161
Release:        0
Summary:        Documentation for texlive-beamer-fuberlin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamer-fuberlin and texlive-alldocumentation)

%description -n texlive-beamer-fuberlin-doc
This package includes the documentation for texlive-beamer-fuberlin

%post -n texlive-beamer-fuberlin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamer-fuberlin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamer-fuberlin
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamer-fuberlin-doc
%{_texmfdistdir}/doc/latex/beamer-fuberlin/Changes
%{_texmfdistdir}/doc/latex/beamer-fuberlin/README
%{_texmfdistdir}/doc/latex/beamer-fuberlin/README.doc
%{_texmfdistdir}/doc/latex/beamer-fuberlin/exampleClass.pdf
%{_texmfdistdir}/doc/latex/beamer-fuberlin/exampleClass.tex
%{_texmfdistdir}/doc/latex/beamer-fuberlin/exampleTheme.pdf
%{_texmfdistdir}/doc/latex/beamer-fuberlin/exampleTheme.tex

%files -n texlive-beamer-fuberlin
%{_texmfdistdir}/tex/latex/beamer-fuberlin/FUbeamer.cls
%{_texmfdistdir}/tex/latex/beamer-fuberlin/beamercolorthemeBerlinFU.sty
%{_texmfdistdir}/tex/latex/beamer-fuberlin/beamerfontthemeBerlinFU.sty
%{_texmfdistdir}/tex/latex/beamer-fuberlin/beamerouterthemeBerlinFU.sty
%{_texmfdistdir}/tex/latex/beamer-fuberlin/beamerthemeBerlinFU.sty

%package -n texlive-beamer-rl
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn69254
Release:        0
License:        LPPL-1.0
Summary:        Right to left presentation with beamer and babel
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamer-rl-doc >= %{texlive_version}
Provides:       tex(beamer-rl.cls)
Provides:       tex(pgfpages-rl.sty)
Requires:       tex(babel.sty)
Requires:       tex(beamer.cls)
Requires:       tex(ifluatex.sty)
Requires:       tex(pgfpages.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source22:       beamer-rl.tar.xz
Source23:       beamer-rl.doc.tar.xz

%description -n texlive-beamer-rl
This class provides patches of some beamer templates and
commands for presentation from right to left. It requires Babel
with the LuaTeX engine.

%package -n texlive-beamer-rl-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn69254
Release:        0
Summary:        Documentation for texlive-beamer-rl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamer-rl and texlive-alldocumentation)
Provides:       locale(texlive-beamer-rl-doc:ar;en)

%description -n texlive-beamer-rl-doc
This package includes the documentation for texlive-beamer-rl

%post -n texlive-beamer-rl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamer-rl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamer-rl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamer-rl-doc
%{_texmfdistdir}/doc/lualatex/beamer-rl/Example-of-use-ar.pdf
%{_texmfdistdir}/doc/lualatex/beamer-rl/Example-of-use-ar.tex
%{_texmfdistdir}/doc/lualatex/beamer-rl/Example-of-use-en.pdf
%{_texmfdistdir}/doc/lualatex/beamer-rl/Example-of-use-en.tex
%{_texmfdistdir}/doc/lualatex/beamer-rl/README.txt

%files -n texlive-beamer-rl
%{_texmfdistdir}/tex/lualatex/beamer-rl/beamer-rl.cls
%{_texmfdistdir}/tex/lualatex/beamer-rl/pgfpages-rl.sty
%{_texmfdistdir}/tex/lualatex/beamer-rl/translator-basic-dictionary-Arabic.dict
%{_texmfdistdir}/tex/lualatex/beamer-rl/translator-bibliography-dictionary-Arabic.dict
%{_texmfdistdir}/tex/lualatex/beamer-rl/translator-environment-dictionary-Arabic.dict
%{_texmfdistdir}/tex/lualatex/beamer-rl/translator-numbers-dictionary-Arabic.dict
%{_texmfdistdir}/tex/lualatex/beamer-rl/translator-theorem-dictionary-Arabic.dict

%package -n texlive-beamer-tut-pt
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        An introduction to the Beamer class, in Portuguese
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source24:       beamer-tut-pt.doc.tar.xz

%description -n texlive-beamer-tut-pt
The beamer-tut-pt package

%post -n texlive-beamer-tut-pt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamer-tut-pt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamer-tut-pt
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamer-tut-pt
%{_texmfdistdir}/doc/latex/beamer-tut-pt/AnnArbor1.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/AnnArbor2.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/CambridgeUS1.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/CambridgeUS2.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/LEIAME
%{_texmfdistdir}/doc/latex/beamer-tut-pt/README
%{_texmfdistdir}/doc/latex/beamer-tut-pt/anim1.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/anim2.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/anim3.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/anim4.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/automato1.jpg
%{_texmfdistdir}/doc/latex/beamer-tut-pt/automato2.jpg
%{_texmfdistdir}/doc/latex/beamer-tut-pt/automato3.jpg
%{_texmfdistdir}/doc/latex/beamer-tut-pt/automato4.jpg
%{_texmfdistdir}/doc/latex/beamer-tut-pt/automato5.jpg
%{_texmfdistdir}/doc/latex/beamer-tut-pt/berkeley1.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/berkeley2.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/blocos.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/boadilla1.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/boadilla2.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/exemplo.tex
%{_texmfdistdir}/doc/latex/beamer-tut-pt/madrid1.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/madrid2.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/montpellier1.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/montpellier2.ps
%{_texmfdistdir}/doc/latex/beamer-tut-pt/tutorialbeamer.pdf
%{_texmfdistdir}/doc/latex/beamer-tut-pt/tutorialbeamer.tex
%{_texmfdistdir}/doc/latex/beamer-tut-pt/ufpellogo.jpg

%package -n texlive-beamer-verona
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn39180
Release:        0
License:        LPPL-1.0
Summary:        A theme for the beamer class
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamer-verona-doc >= %{texlive_version}
Provides:       tex(beamerthemeVerona.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source25:       beamer-verona.tar.xz
Source26:       beamer-verona.doc.tar.xz

%description -n texlive-beamer-verona
This package provides the 'Verona' theme for the beamer class
by Till Tantau.

%package -n texlive-beamer-verona-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn39180
Release:        0
Summary:        Documentation for texlive-beamer-verona
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamer-verona and texlive-alldocumentation)

%description -n texlive-beamer-verona-doc
This package includes the documentation for texlive-beamer-verona

%post -n texlive-beamer-verona
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamer-verona
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamer-verona
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamer-verona-doc
%{_texmfdistdir}/doc/latex/beamer-verona/README.md
%{_texmfdistdir}/doc/latex/beamer-verona/beamer-verona-default.pdf
%{_texmfdistdir}/doc/latex/beamer-verona/beamer-verona-default.tex
%{_texmfdistdir}/doc/latex/beamer-verona/beamer-verona-sidebar.pdf
%{_texmfdistdir}/doc/latex/beamer-verona/beamer-verona-sidebar.tex
%{_texmfdistdir}/doc/latex/beamer-verona/beamer-verona.pdf
%{_texmfdistdir}/doc/latex/beamer-verona/plato-aristotle.jpg

%files -n texlive-beamer-verona
%{_texmfdistdir}/tex/latex/beamer-verona/beamerthemeVerona.sty

%package -n texlive-beamer2thesis
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn27539
Release:        0
License:        LPPL-1.0
Summary:        Thesis presentations using beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamer2thesis-doc >= %{texlive_version}
Provides:       tex(beamercolorthemetorinoth.sty)
Provides:       tex(beamerfontthemetorinoth.sty)
Provides:       tex(beamerinnerthemetorinoth.sty)
Provides:       tex(beamerouterthemetorinoth.sty)
Provides:       tex(beamerthemeTorinoTh.sty)
Requires:       tex(babel.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(pifont.sty)
Requires:       tex(polyglossia.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source27:       beamer2thesis.tar.xz
Source28:       beamer2thesis.doc.tar.xz

%description -n texlive-beamer2thesis
The package specifies a beamer theme for presenting a thesis.

%package -n texlive-beamer2thesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn27539
Release:        0
Summary:        Documentation for texlive-beamer2thesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamer2thesis and texlive-alldocumentation)
Provides:       locale(texlive-beamer2thesis-doc:en;it)

%description -n texlive-beamer2thesis-doc
This package includes the documentation for texlive-beamer2thesis

%post -n texlive-beamer2thesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamer2thesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamer2thesis
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamer2thesis-doc
%{_texmfdistdir}/doc/latex/beamer2thesis/README
%{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis.pdf
%{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis.tex
%{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis_ita.pdf
%{_texmfdistdir}/doc/latex/beamer2thesis/beamer2thesis_ita.tex
%{_texmfdistdir}/doc/latex/beamer2thesis/content_end.tex
%{_texmfdistdir}/doc/latex/beamer2thesis/content_end_ita.tex
%{_texmfdistdir}/doc/latex/beamer2thesis/content_initial.tex
%{_texmfdistdir}/doc/latex/beamer2thesis/content_initial_ita.tex
%{_texmfdistdir}/doc/latex/beamer2thesis/license

%files -n texlive-beamer2thesis
%{_texmfdistdir}/tex/latex/beamer2thesis/beamer2thesis.jpg
%{_texmfdistdir}/tex/latex/beamer2thesis/beamercolorthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerfontthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerinnerthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerouterthemetorinoth.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/beamerthemeTorinoTh.sty
%{_texmfdistdir}/tex/latex/beamer2thesis/logopolito.jpg

%package -n texlive-beamerappendixnote
Version:        %{texlive_version}.%{texlive_noarch}.1.2.0svn55732
Release:        0
License:        LPPL-1.0
Summary:        Create notes on appendix frames in beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerappendixnote-doc >= %{texlive_version}
Provides:       tex(beamerappendixnote.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source29:       beamerappendixnote.tar.xz
Source30:       beamerappendixnote.doc.tar.xz

%description -n texlive-beamerappendixnote
This package introduces the \appxnote command, which puts the
note's content on a separate beamer frame shown by the command
\printappxnotes. It also creates interactive buttons to move
back and forth between the two frames.

%package -n texlive-beamerappendixnote-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2.0svn55732
Release:        0
Summary:        Documentation for texlive-beamerappendixnote
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerappendixnote and texlive-alldocumentation)

%description -n texlive-beamerappendixnote-doc
This package includes the documentation for texlive-beamerappendixnote

%post -n texlive-beamerappendixnote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerappendixnote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerappendixnote
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerappendixnote-doc
%{_texmfdistdir}/doc/latex/beamerappendixnote/README.md
%{_texmfdistdir}/doc/latex/beamerappendixnote/beamerappendixnote.pdf
%{_texmfdistdir}/doc/latex/beamerappendixnote/build.sh
%{_texmfdistdir}/doc/latex/beamerappendixnote/example-backtop.pdf
%{_texmfdistdir}/doc/latex/beamerappendixnote/example-backtop.tex
%{_texmfdistdir}/doc/latex/beamerappendixnote/example-basic.pdf
%{_texmfdistdir}/doc/latex/beamerappendixnote/example-basic.tex
%{_texmfdistdir}/doc/latex/beamerappendixnote/example-longnote.pdf
%{_texmfdistdir}/doc/latex/beamerappendixnote/example-longnote.tex

%files -n texlive-beamerappendixnote
%{_texmfdistdir}/tex/latex/beamerappendixnote/beamerappendixnote.sty

%package -n texlive-beameraudience
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn23427
Release:        0
License:        LPPL-1.0
Summary:        Assembling beamer frames according to audience
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beameraudience-doc >= %{texlive_version}
Provides:       tex(beameraudience.sty)
Requires:       tex(cprotect.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source31:       beameraudience.tar.xz
Source32:       beameraudience.doc.tar.xz

%description -n texlive-beameraudience
The Beamer Audience package provides macros to easily assemble
frames according to different audiences. It enables to pick up
the frames for a specific audience while leaving their order
according to a logical structure in the LaTeX source.

%package -n texlive-beameraudience-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn23427
Release:        0
Summary:        Documentation for texlive-beameraudience
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beameraudience and texlive-alldocumentation)

%description -n texlive-beameraudience-doc
This package includes the documentation for texlive-beameraudience

%post -n texlive-beameraudience
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beameraudience
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beameraudience
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beameraudience-doc
%{_texmfdistdir}/doc/latex/beameraudience/README

%files -n texlive-beameraudience
%{_texmfdistdir}/tex/latex/beameraudience/beameraudience.sty

%package -n texlive-beamerauxtheme
Version:        %{texlive_version}.%{texlive_noarch}.1.02asvn56087
Release:        0
License:        LPPL-1.0
Summary:        Supplementary outer and inner themes for beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerauxtheme-doc >= %{texlive_version}
Provides:       tex(beamerinnerthemesimplelines.sty)
Provides:       tex(beamerouterthemesidebarwithminiframes.sty)
Provides:       tex(beamerouterthemesplitwithminiframes.sty)
Provides:       tex(beamerouterthemetwolines.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source33:       beamerauxtheme.tar.xz
Source34:       beamerauxtheme.doc.tar.xz

%description -n texlive-beamerauxtheme
This bundle provides a collection of inner and outer themes as
supplements to the default themes in the beamer distribution.
These themes can be used in combination with existing inner,
outer, and color themes.

%package -n texlive-beamerauxtheme-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02asvn56087
Release:        0
Summary:        Documentation for texlive-beamerauxtheme
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerauxtheme and texlive-alldocumentation)

%description -n texlive-beamerauxtheme-doc
This package includes the documentation for texlive-beamerauxtheme

%post -n texlive-beamerauxtheme
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerauxtheme
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerauxtheme
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerauxtheme-doc
%{_texmfdistdir}/doc/latex/beamerauxtheme/LICENSE
%{_texmfdistdir}/doc/latex/beamerauxtheme/README.md
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-content.ltx
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-inner-simplelines.pdf
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-inner-simplelines.tex
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-outer-sidebarwithminiframes.pdf
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-outer-sidebarwithminiframes.tex
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-outer-splitwithminiframes.pdf
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-outer-splitwithminiframes.tex
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-outer-twolines.pdf
%{_texmfdistdir}/doc/latex/beamerauxtheme/example-outer-twolines.tex

%files -n texlive-beamerauxtheme
%{_texmfdistdir}/tex/latex/beamerauxtheme/beamerinnerthemesimplelines.sty
%{_texmfdistdir}/tex/latex/beamerauxtheme/beamerouterthemesidebarwithminiframes.sty
%{_texmfdistdir}/tex/latex/beamerauxtheme/beamerouterthemesplitwithminiframes.sty
%{_texmfdistdir}/tex/latex/beamerauxtheme/beamerouterthemetwolines.sty

%package -n texlive-beamercolorthemeowl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn40105
Release:        0
License:        LPPL-1.0
Summary:        A flexible beamer color theme to maximize visibility
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamercolorthemeowl-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeowl.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source35:       beamercolorthemeowl.tar.xz
Source36:       beamercolorthemeowl.doc.tar.xz

%description -n texlive-beamercolorthemeowl
This package provides a flexible dark or light colour theme
designed for maximum readability in environments where most
themes fall flat. Main features: Dark color theme for
presenting in low-light conditions. Optional light color theme
for presenting in bright ambient light. Redefines color names
"red", "green", "blue", "yellow" to values that are visible
when displayed by certain projectors, particularly those with a
very bright green channel and dim red and blue channels. This
behaviour can be optionally disabled, with the provided colours
also available as "OwlRed", "OwlGreen", etc.

%package -n texlive-beamercolorthemeowl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn40105
Release:        0
Summary:        Documentation for texlive-beamercolorthemeowl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamercolorthemeowl and texlive-alldocumentation)

%description -n texlive-beamercolorthemeowl-doc
This package includes the documentation for texlive-beamercolorthemeowl

%post -n texlive-beamercolorthemeowl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamercolorthemeowl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamercolorthemeowl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamercolorthemeowl-doc
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/Makefile
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/README.md
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/beamercolorthemeowl.pdf
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Hannover-dark/Hannover-owl-1.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Hannover-dark/Hannover-owl-2.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Hannover-light/Hannover-owl-1.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Hannover-light/Hannover-owl-2.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Pittsburgh-dark/Pittsburgh-owl-1.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Pittsburgh-dark/Pittsburgh-owl-2.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Pittsburgh-light/Pittsburgh-owl-1.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/Pittsburgh-light/Pittsburgh-owl-2.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/colours.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/metropolis-dark/metropolis-owl-1.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/metropolis-dark/metropolis-owl-2.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/metropolis-light/metropolis-owl-1.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/metropolis-light/metropolis-owl-2.png
%{_texmfdistdir}/doc/latex/beamercolorthemeowl/ex/readme.jpg

%files -n texlive-beamercolorthemeowl
%{_texmfdistdir}/tex/latex/beamercolorthemeowl/beamercolorthemeowl.sty

%package -n texlive-beamerdarkthemes
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.1svn55117
Release:        0
License:        LPPL-1.0
Summary:        Dark color themes for beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerdarkthemes-doc >= %{texlive_version}
Provides:       tex(beamercolorthemecormorant.sty)
Provides:       tex(beamercolorthemefrigatebird.sty)
Provides:       tex(beamercolorthememagpie.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source37:       beamerdarkthemes.tar.xz
Source38:       beamerdarkthemes.doc.tar.xz

%description -n texlive-beamerdarkthemes
A package with three dark color themes for beamer, designed for
presentations with pictures and/or for bright rooms without
screen. These themes mix one dominant foreground colour and a
black background. Cormorant stands for green, frigatebird for
red and magpie for blue.

%package -n texlive-beamerdarkthemes-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.1svn55117
Release:        0
Summary:        Documentation for texlive-beamerdarkthemes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerdarkthemes and texlive-alldocumentation)

%description -n texlive-beamerdarkthemes-doc
This package includes the documentation for texlive-beamerdarkthemes

%post -n texlive-beamerdarkthemes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerdarkthemes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerdarkthemes
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerdarkthemes-doc
%{_texmfdistdir}/doc/latex/beamerdarkthemes/README
%{_texmfdistdir}/doc/latex/beamerdarkthemes/beamerdarkthemesuserguide.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/beamerdarkthemesuserguide.tex
%{_texmfdistdir}/doc/latex/beamerdarkthemes/ccby.png
%{_texmfdistdir}/doc/latex/beamerdarkthemes/cormorantexampledefault.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/cormorantexampleinfolines.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/cormorantexamplesidebar.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/cormorantexampletree.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/dahut.jpg
%{_texmfdistdir}/doc/latex/beamerdarkthemes/example.tex
%{_texmfdistdir}/doc/latex/beamerdarkthemes/frigatebirdexampledefault.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/frigatebirdexampleinfolines.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/frigatebirdexamplesidebar.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/frigatebirdexampletree.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/img_5630.jpg
%{_texmfdistdir}/doc/latex/beamerdarkthemes/magpieexampledefault.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/magpieexampleinfolines.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/magpieexamplesidebar.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/magpieexampletree.pdf
%{_texmfdistdir}/doc/latex/beamerdarkthemes/makecormorant.sh
%{_texmfdistdir}/doc/latex/beamerdarkthemes/makeexamples.sh
%{_texmfdistdir}/doc/latex/beamerdarkthemes/makemagpie.sh

%files -n texlive-beamerdarkthemes
%{_texmfdistdir}/tex/latex/beamerdarkthemes/beamercolorthemecormorant.sty
%{_texmfdistdir}/tex/latex/beamerdarkthemes/beamercolorthemefrigatebird.sty
%{_texmfdistdir}/tex/latex/beamerdarkthemes/beamercolorthememagpie.sty

%package -n texlive-beamerposter
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn54512
Release:        0
License:        LPPL-1.0
Summary:        Extend beamer and a0poster for custom sized posters
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerposter-doc >= %{texlive_version}
Provides:       tex(beamerposter.sty)
Provides:       tex(beamerthemeAachen.sty)
Provides:       tex(beamerthemeI6dv.sty)
Provides:       tex(beamerthemeI6pd.sty)
Provides:       tex(beamerthemeI6pd2.sty)
Provides:       tex(beamerthemeI6td.sty)
Provides:       tex(beamerthemeZH.sty)
Requires:       tex(fp.sty)
Requires:       tex(tangocolors.sty)
Requires:       tex(type1cm.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source39:       beamerposter.tar.xz
Source40:       beamerposter.doc.tar.xz

%description -n texlive-beamerposter
The package enables the user to use beamer style operations on
a canvas of the sizes provided by a0poster; font scaling is
available (using packages such as type1cm if necessary). In
addition, the package allows the user to benefit from the nice
colour box handling and alignment provided by the beamer class
(for example, with rounded corners and shadows). Good looking
posters may be created very rapidly. Features include: scalable
fonts using the fp and type1cm packages; posters in A-series
sizes, and custom sizes like double A0 are possible; still
applicable to custom beamer slides, e.g. 16:9 slides for a
wide-screen (i.e. 1.78 aspect ratio); orientation may be
portrait or landscape; a 'debug mode' is provided.

%package -n texlive-beamerposter-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.13svn54512
Release:        0
Summary:        Documentation for texlive-beamerposter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerposter and texlive-alldocumentation)

%description -n texlive-beamerposter-doc
This package includes the documentation for texlive-beamerposter

%post -n texlive-beamerposter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerposter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerposter
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerposter-doc
%{_texmfdistdir}/doc/latex/beamerposter/README
%{_texmfdistdir}/doc/latex/beamerposter/beamerposter.pdf
%{_texmfdistdir}/doc/latex/beamerposter/beamerposter.tex
%{_texmfdistdir}/doc/latex/beamerposter/example.tex

%files -n texlive-beamerposter
%{_texmfdistdir}/tex/latex/beamerposter/beamerposter.sty
%{_texmfdistdir}/tex/latex/beamerposter/beamerthemeAachen.sty
%{_texmfdistdir}/tex/latex/beamerposter/beamerthemeI6dv.sty
%{_texmfdistdir}/tex/latex/beamerposter/beamerthemeI6pd.sty
%{_texmfdistdir}/tex/latex/beamerposter/beamerthemeI6pd2.sty
%{_texmfdistdir}/tex/latex/beamerposter/beamerthemeI6td.sty
%{_texmfdistdir}/tex/latex/beamerposter/beamerthemeZH.sty

%package -n texlive-beamersubframe
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn23510
Release:        0
License:        LPPL-1.0
Summary:        Reorder frames in the PDF file
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamersubframe-doc >= %{texlive_version}
Provides:       tex(beamersubframe.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source41:       beamersubframe.tar.xz
Source42:       beamersubframe.doc.tar.xz

%description -n texlive-beamersubframe
The package provides a method to reorder frames in the PDF file
without reordering the source. Its principal use is to embed or
append frames with details on some subject. The author
describes the package as "experimental".

%package -n texlive-beamersubframe-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn23510
Release:        0
Summary:        Documentation for texlive-beamersubframe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamersubframe and texlive-alldocumentation)

%description -n texlive-beamersubframe-doc
This package includes the documentation for texlive-beamersubframe

%post -n texlive-beamersubframe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamersubframe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamersubframe
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamersubframe-doc
%{_texmfdistdir}/doc/latex/beamersubframe/README
%{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-append.pdf
%{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-append.svg
%{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-embed.pdf
%{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-embed.svg
%{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe.pdf
%{_texmfdistdir}/doc/latex/beamersubframe/bsf-example.tex

%files -n texlive-beamersubframe
%{_texmfdistdir}/tex/latex/beamersubframe/beamersubframe.sty

%package -n texlive-beamerswitch
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn64182
Release:        0
License:        LPPL-1.0
Summary:        Convenient mode selection in Beamer documents
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerswitch-doc >= %{texlive_version}
Provides:       tex(beamerswitch.cls)
Requires:       tex(beamer.cls)
Requires:       tex(beamerarticle.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(iftex.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfpages.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xkvltxp.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source43:       beamerswitch.tar.xz
Source44:       beamerswitch.doc.tar.xz

%description -n texlive-beamerswitch
This class is a wrapper around the beamer class to make it
easier to use the same document to generate the different forms
of the presentation: the slides themselves, an abbreviated
slide set for transparencies or online reference, an n-up
handout version (various layouts are provided), and a
transcript or set of notes using the article class. The class
provides a variety of handout layouts, and allows the mode to
be chosen from the command line (without changing the document
itself).

%package -n texlive-beamerswitch-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn64182
Release:        0
Summary:        Documentation for texlive-beamerswitch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerswitch and texlive-alldocumentation)

%description -n texlive-beamerswitch-doc
This package includes the documentation for texlive-beamerswitch

%post -n texlive-beamerswitch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerswitch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerswitch
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerswitch-doc
%{_texmfdistdir}/doc/latex/beamerswitch/README.md
%{_texmfdistdir}/doc/latex/beamerswitch/beamerswitch-example-article.pdf
%{_texmfdistdir}/doc/latex/beamerswitch/beamerswitch-example-handout.pdf
%{_texmfdistdir}/doc/latex/beamerswitch/beamerswitch-example-trans.pdf
%{_texmfdistdir}/doc/latex/beamerswitch/beamerswitch-example.pdf
%{_texmfdistdir}/doc/latex/beamerswitch/beamerswitch-example.tex
%{_texmfdistdir}/doc/latex/beamerswitch/beamerswitch.pdf

%files -n texlive-beamerswitch
%{_texmfdistdir}/tex/latex/beamerswitch/beamerswitch.cls

%package -n texlive-beamertheme-arguelles
Version:        %{texlive_version}.%{texlive_noarch}.2.4.0svn70200
Release:        0
License:        LPPL-1.0
Summary:        Simple, typographic beamer theme
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-arguelles-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeArguelles.sty)
Provides:       tex(beamerfontthemeArguelles.sty)
Provides:       tex(beamerinnerthemeArguelles.sty)
Provides:       tex(beamerouterthemeArguelles.sty)
Provides:       tex(beamerthemeArguelles.sty)
Requires:       tex(Alegreya.sty)
Requires:       tex(AlegreyaSans.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(eulervm.sty)
Requires:       tex(fontawesome5.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(mathalpha.sty)
Requires:       tex(microtype.sty)
Requires:       tex(opencolor.sty)
Requires:       tex(parskip.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source45:       beamertheme-arguelles.tar.xz
Source46:       beamertheme-arguelles.doc.tar.xz

%description -n texlive-beamertheme-arguelles
Arguelles is a beamer theme that helps you create beautiful
presentations. It aims for simplicity and readability by
following best practices of graphic design. The layout is
elegant but subtle, so as to keep the audience's attention on
your content. This is brought to life by Alegreya, one of the
53 Fonts of the Decade selected by the Association
Typographique Internationale (2011).

%package -n texlive-beamertheme-arguelles-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4.0svn70200
Release:        0
Summary:        Documentation for texlive-beamertheme-arguelles
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-arguelles and texlive-alldocumentation)

%description -n texlive-beamertheme-arguelles-doc
This package includes the documentation for texlive-beamertheme-arguelles

%post -n texlive-beamertheme-arguelles
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-arguelles
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-arguelles
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-arguelles-doc
%{_texmfdistdir}/doc/latex/beamertheme-arguelles/LICENSE
%{_texmfdistdir}/doc/latex/beamertheme-arguelles/README.md
%{_texmfdistdir}/doc/latex/beamertheme-arguelles/demo/demo-arguelles.gif
%{_texmfdistdir}/doc/latex/beamertheme-arguelles/demo/demo-arguelles.pdf
%{_texmfdistdir}/doc/latex/beamertheme-arguelles/demo/demo-arguelles.png
%{_texmfdistdir}/doc/latex/beamertheme-arguelles/demo/demo-arguelles.tex

%files -n texlive-beamertheme-arguelles
%{_texmfdistdir}/tex/latex/beamertheme-arguelles/beamercolorthemeArguelles.sty
%{_texmfdistdir}/tex/latex/beamertheme-arguelles/beamerfontthemeArguelles.sty
%{_texmfdistdir}/tex/latex/beamertheme-arguelles/beamerinnerthemeArguelles.sty
%{_texmfdistdir}/tex/latex/beamertheme-arguelles/beamerouterthemeArguelles.sty
%{_texmfdistdir}/tex/latex/beamertheme-arguelles/beamerthemeArguelles.sty

%package -n texlive-beamertheme-cuerna
Version:        %{texlive_version}.%{texlive_noarch}.svn42161
Release:        0
License:        LPPL-1.0
Summary:        A beamer theme with 4 colour palettes
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-cuerna-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeCuerna.sty)
Provides:       tex(beamercolorthemebluesimplex.sty)
Provides:       tex(beamercolorthemebrick.sty)
Provides:       tex(beamercolorthemelettuce.sty)
Provides:       tex(beamerinnerthemeCuerna.sty)
Provides:       tex(beamerouterthemeCuerna.sty)
Provides:       tex(beamerthemeCuerna.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source47:       beamertheme-cuerna.tar.xz
Source48:       beamertheme-cuerna.doc.tar.xz

%description -n texlive-beamertheme-cuerna
The package contains a theme for Beamer which is referenced as
"Cuerna" inside beamer and has four basic colour themes. The
title page shows rectangles that represent the Fibonacci
sequence, and spiral is drawn on top of the rectangles. Besides
that the rest of the graphic elements in the slides are scarce
to keep it clean

%package -n texlive-beamertheme-cuerna-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn42161
Release:        0
Summary:        Documentation for texlive-beamertheme-cuerna
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-cuerna and texlive-alldocumentation)

%description -n texlive-beamertheme-cuerna-doc
This package includes the documentation for texlive-beamertheme-cuerna

%post -n texlive-beamertheme-cuerna
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-cuerna
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-cuerna
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-cuerna-doc
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/README
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/beamertheme-cuerna.pdf
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/pictures/bluesimplex.png
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/pictures/bluesimplexexample.pdf
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/pictures/brickexample.pdf
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/pictures/defaultexample.pdf
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/pictures/lettuceexample.pdf
%{_texmfdistdir}/doc/latex/beamertheme-cuerna/template.tex

%files -n texlive-beamertheme-cuerna
%{_texmfdistdir}/tex/latex/beamertheme-cuerna/beamercolorthemeCuerna.sty
%{_texmfdistdir}/tex/latex/beamertheme-cuerna/beamercolorthemebluesimplex.sty
%{_texmfdistdir}/tex/latex/beamertheme-cuerna/beamercolorthemebrick.sty
%{_texmfdistdir}/tex/latex/beamertheme-cuerna/beamercolorthemelettuce.sty
%{_texmfdistdir}/tex/latex/beamertheme-cuerna/beamerinnerthemeCuerna.sty
%{_texmfdistdir}/tex/latex/beamertheme-cuerna/beamerouterthemeCuerna.sty
%{_texmfdistdir}/tex/latex/beamertheme-cuerna/beamerthemeCuerna.sty

%package -n texlive-beamertheme-detlevcm
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn39048
Release:        0
License:        GPL-2.0-or-later
Summary:        A beamer theme designed for use in the University of Leeds
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-detlevcm-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeETII.sty)
Provides:       tex(beamerfontthemeDetlevCM.sty)
Provides:       tex(beamerouterthemeDetlevCM.sty)
Provides:       tex(beamerthemeDetlevCM.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source49:       beamertheme-detlevcm.tar.xz
Source50:       beamertheme-detlevcm.doc.tar.xz

%description -n texlive-beamertheme-detlevcm
The bundle provides a simple theme that has been used in the
author's department.

%package -n texlive-beamertheme-detlevcm-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn39048
Release:        0
Summary:        Documentation for texlive-beamertheme-detlevcm
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-detlevcm and texlive-alldocumentation)

%description -n texlive-beamertheme-detlevcm-doc
This package includes the documentation for texlive-beamertheme-detlevcm

%post -n texlive-beamertheme-detlevcm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-detlevcm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-detlevcm
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-detlevcm-doc
%{_texmfdistdir}/doc/latex/beamertheme-detlevcm/FS-img1.png
%{_texmfdistdir}/doc/latex/beamertheme-detlevcm/FS-img2.png
%{_texmfdistdir}/doc/latex/beamertheme-detlevcm/FS-img3.png
%{_texmfdistdir}/doc/latex/beamertheme-detlevcm/LogoTop.png
%{_texmfdistdir}/doc/latex/beamertheme-detlevcm/README.txt
%{_texmfdistdir}/doc/latex/beamertheme-detlevcm/beamertheme-detlevcm.pdf
%{_texmfdistdir}/doc/latex/beamertheme-detlevcm/beamertheme-detlevcm.tex

%files -n texlive-beamertheme-detlevcm
%{_texmfdistdir}/tex/latex/beamertheme-detlevcm/beamercolorthemeETII.sty
%{_texmfdistdir}/tex/latex/beamertheme-detlevcm/beamerfontthemeDetlevCM.sty
%{_texmfdistdir}/tex/latex/beamertheme-detlevcm/beamerouterthemeDetlevCM.sty
%{_texmfdistdir}/tex/latex/beamertheme-detlevcm/beamerthemeDetlevCM.sty

%package -n texlive-beamertheme-epyt
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41404
Release:        0
License:        LPPL-1.0
Summary:        A simple and clean theme for LaTeX beamer class
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-epyt-doc >= %{texlive_version}
Provides:       tex(beamerthemeepyt.sty)
Requires:       tex(arev.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source51:       beamertheme-epyt.tar.xz
Source52:       beamertheme-epyt.doc.tar.xz

%description -n texlive-beamertheme-epyt
This package provides a simple but nice theme for Beamer, with
the following features: simple structure: with page numbers at
footer, no head bar and side bar simple templates: displaying
theorems with traditional inline style simple colors: using
only several foreground and background colors

%package -n texlive-beamertheme-epyt-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41404
Release:        0
Summary:        Documentation for texlive-beamertheme-epyt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-epyt and texlive-alldocumentation)
Provides:       locale(texlive-beamertheme-epyt-doc:zh)

%description -n texlive-beamertheme-epyt-doc
This package includes the documentation for texlive-beamertheme-epyt

%post -n texlive-beamertheme-epyt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-epyt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-epyt
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-epyt-doc
%{_texmfdistdir}/doc/latex/beamertheme-epyt/README
%{_texmfdistdir}/doc/latex/beamertheme-epyt/epyt-demo-cn.pdf
%{_texmfdistdir}/doc/latex/beamertheme-epyt/epyt-demo-cn.tex
%{_texmfdistdir}/doc/latex/beamertheme-epyt/epyt-demo.pdf
%{_texmfdistdir}/doc/latex/beamertheme-epyt/epyt-demo.tex

%files -n texlive-beamertheme-epyt
%{_texmfdistdir}/tex/latex/beamertheme-epyt/beamerthemeepyt.sty

%package -n texlive-beamertheme-focus
Version:        %{texlive_version}.%{texlive_noarch}.3.4.0svn69742
Release:        0
License:        GPL-2.0-or-later
Summary:        A minimalist presentation theme for LaTeX Beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-focus-doc >= %{texlive_version}
Provides:       tex(beamercolorthemefocus.sty)
Provides:       tex(beamerfontthemefocus.sty)
Provides:       tex(beamerinnerthemefocus.sty)
Provides:       tex(beamerouterthemefocus.sty)
Provides:       tex(beamerthemefocus.sty)
Requires:       tex(FiraMono.sty)
Requires:       tex(FiraSans.sty)
Requires:       tex(appendixnumberbeamer.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(firamath-otf.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source53:       beamertheme-focus.tar.xz
Source54:       beamertheme-focus.doc.tar.xz

%description -n texlive-beamertheme-focus
A presentation theme for LaTeX Beamer that aims at a clean and
minimalist design, so to minimize distractions and put the
focus directly on the content.

%package -n texlive-beamertheme-focus-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.4.0svn69742
Release:        0
Summary:        Documentation for texlive-beamertheme-focus
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-focus and texlive-alldocumentation)

%description -n texlive-beamertheme-focus-doc
This package includes the documentation for texlive-beamertheme-focus

%post -n texlive-beamertheme-focus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-focus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-focus
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-focus-doc
%{_texmfdistdir}/doc/latex/beamertheme-focus/CHANGELOG.md
%{_texmfdistdir}/doc/latex/beamertheme-focus/LICENSE.md
%{_texmfdistdir}/doc/latex/beamertheme-focus/README.md
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo.pdf
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo.tex
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo/demo-appendix.jpg
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo/demo-focus.jpg
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo/demo-references.jpg
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo/demo-subsectionpage.jpg
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo/demo-titlepage-color.jpg
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo/demo-titlepage.jpg
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo/demo-typeset.jpg
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-demo_bibliography.bib
%{_texmfdistdir}/doc/latex/beamertheme-focus/focus-logo.pdf

%files -n texlive-beamertheme-focus
%{_texmfdistdir}/tex/latex/beamertheme-focus/beamercolorthemefocus.sty
%{_texmfdistdir}/tex/latex/beamertheme-focus/beamerfontthemefocus.sty
%{_texmfdistdir}/tex/latex/beamertheme-focus/beamerinnerthemefocus.sty
%{_texmfdistdir}/tex/latex/beamertheme-focus/beamerouterthemefocus.sty
%{_texmfdistdir}/tex/latex/beamertheme-focus/beamerthemefocus.sty

%package -n texlive-beamertheme-light
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49867
Release:        0
License:        GPL-2.0-or-later
Summary:        A minimal beamer style
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-light-doc >= %{texlive_version}
Provides:       tex(beamertheme-light.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source55:       beamertheme-light.tar.xz
Source56:       beamertheme-light.doc.tar.xz

%description -n texlive-beamertheme-light
The LaTeX package beamertheme-light provides an aesthetic and
minimal beamer style by redefining colors and fonts.

%package -n texlive-beamertheme-light-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49867
Release:        0
Summary:        Documentation for texlive-beamertheme-light
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-light and texlive-alldocumentation)

%description -n texlive-beamertheme-light-doc
This package includes the documentation for texlive-beamertheme-light

%post -n texlive-beamertheme-light
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-light
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-light
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-light-doc
%{_texmfdistdir}/doc/latex/beamertheme-light/README
%{_texmfdistdir}/doc/latex/beamertheme-light/beamertheme-light-example.pdf
%{_texmfdistdir}/doc/latex/beamertheme-light/beamertheme-light-example.tex

%files -n texlive-beamertheme-light
%{_texmfdistdir}/tex/latex/beamertheme-light/beamertheme-light.sty

%package -n texlive-beamertheme-metropolis
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn43031
Release:        0
License:        LPPL-1.0
Summary:        A modern LaTeX beamer theme
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-metropolis-doc >= %{texlive_version}
Provides:       tex(beamercolorthememetropolis-highcontrast.sty)
Provides:       tex(beamercolorthememetropolis.sty)
Provides:       tex(beamerfontthememetropolis.sty)
Provides:       tex(beamerinnerthememetropolis.sty)
Provides:       tex(beamerouterthememetropolis.sty)
Provides:       tex(beamerthememetropolis.sty)
Provides:       tex(pgfplotsthemetol.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source57:       beamertheme-metropolis.tar.xz
Source58:       beamertheme-metropolis.doc.tar.xz

%description -n texlive-beamertheme-metropolis
The package provides a simple, modern Beamer theme for anyone
to use. It tries to minimize noise and maximize space for
content.

%package -n texlive-beamertheme-metropolis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn43031
Release:        0
Summary:        Documentation for texlive-beamertheme-metropolis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-metropolis and texlive-alldocumentation)

%description -n texlive-beamertheme-metropolis-doc
This package includes the documentation for texlive-beamertheme-metropolis

%post -n texlive-beamertheme-metropolis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-metropolis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-metropolis
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-metropolis-doc
%{_texmfdistdir}/doc/latex/beamertheme-metropolis/README.md
%{_texmfdistdir}/doc/latex/beamertheme-metropolis/demo.bib
%{_texmfdistdir}/doc/latex/beamertheme-metropolis/demo.pdf
%{_texmfdistdir}/doc/latex/beamertheme-metropolis/demo.tex
%{_texmfdistdir}/doc/latex/beamertheme-metropolis/metropolistheme.pdf

%files -n texlive-beamertheme-metropolis
%{_texmfdistdir}/tex/latex/beamertheme-metropolis/beamercolorthememetropolis-highcontrast.sty
%{_texmfdistdir}/tex/latex/beamertheme-metropolis/beamercolorthememetropolis.sty
%{_texmfdistdir}/tex/latex/beamertheme-metropolis/beamerfontthememetropolis.sty
%{_texmfdistdir}/tex/latex/beamertheme-metropolis/beamerinnerthememetropolis.sty
%{_texmfdistdir}/tex/latex/beamertheme-metropolis/beamerouterthememetropolis.sty
%{_texmfdistdir}/tex/latex/beamertheme-metropolis/beamerthememetropolis.sty
%{_texmfdistdir}/tex/latex/beamertheme-metropolis/pgfplotsthemetol.sty

%package -n texlive-beamertheme-npbt
Version:        %{texlive_version}.%{texlive_noarch}.4.1svn54512
Release:        0
License:        GPL-2.0-or-later
Summary:        A collection of LaTeX beamer themes
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-npbt-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeNPBT_EUFOM.sty)
Provides:       tex(beamercolorthemeNPBT_FOM.sty)
Provides:       tex(beamercolorthemeNPBT_FOM_ifes.sty)
Provides:       tex(beamercolorthemeNPBT_SC.sty)
Provides:       tex(beamerouterthemeNPBT_FOM.sty)
Provides:       tex(beamerouterthemeNPBT_FOM_ifes.sty)
Provides:       tex(beamerthemeNPBT.sty)
Requires:       tex(array.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source59:       beamertheme-npbt.tar.xz
Source60:       beamertheme-npbt.doc.tar.xz

%description -n texlive-beamertheme-npbt
"NPBT" stands for "Norman's Pandoc Beamer Themes". Currently
the following themes are supported: Sefiroth Consulting: A
private (demonstration) theme. FOM: The layout of Hochschule
FOM. FOM ifes: The layout of Hochschule FOM, Institut fur
Empirie & Statistik. eufom: The layout of eufom.

%package -n texlive-beamertheme-npbt-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.1svn54512
Release:        0
Summary:        Documentation for texlive-beamertheme-npbt
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-npbt and texlive-alldocumentation)

%description -n texlive-beamertheme-npbt-doc
This package includes the documentation for texlive-beamertheme-npbt

%post -n texlive-beamertheme-npbt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-npbt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-npbt
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-npbt-doc
%{_texmfdistdir}/doc/latex/beamertheme-npbt/LICENSE
%{_texmfdistdir}/doc/latex/beamertheme-npbt/README
%{_texmfdistdir}/doc/latex/beamertheme-npbt/example/NPBT_exsamle.pdf
%{_texmfdistdir}/doc/latex/beamertheme-npbt/example/NPBT_exsamle.tex
%{_texmfdistdir}/doc/latex/beamertheme-npbt/header.tex

%files -n texlive-beamertheme-npbt
%{_texmfdistdir}/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_EUFOM.sty
%{_texmfdistdir}/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_FOM.sty
%{_texmfdistdir}/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_FOM_ifes.sty
%{_texmfdistdir}/tex/latex/beamertheme-npbt/beamercolorthemeNPBT_SC.sty
%{_texmfdistdir}/tex/latex/beamertheme-npbt/beamerouterthemeNPBT_FOM.sty
%{_texmfdistdir}/tex/latex/beamertheme-npbt/beamerouterthemeNPBT_FOM_ifes.sty
%{_texmfdistdir}/tex/latex/beamertheme-npbt/beamerthemeNPBT.sty
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/LICENSE.md
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_background.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_frametitlebackground.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_backgound.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_frametitlebackgound.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_linie.pdf
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_ifes_logo.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_linie.pdf
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_FOM_logo.pdf
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_SC_background.jpg
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_SC_logo.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_eufom_backgound.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_eufom_frametitlebackgound.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_eufom_linie.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/NPBT_eufom_logo.png
%{_texmfdistdir}/tex/latex/beamertheme-npbt/images/lNPBT_SC_linie.png

%package -n texlive-beamertheme-phnompenh
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn39100
Release:        0
License:        GPL-2.0-or-later
Summary:        A simple beamer theme
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-phnompenh-doc >= %{texlive_version}
Provides:       tex(beamerthemePhnomPenh.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source61:       beamertheme-phnompenh.tar.xz
Source62:       beamertheme-phnompenh.doc.tar.xz

%description -n texlive-beamertheme-phnompenh
The package provides a simple theme, similar to some others,
but designed to be attractive.

%package -n texlive-beamertheme-phnompenh-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn39100
Release:        0
Summary:        Documentation for texlive-beamertheme-phnompenh
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-phnompenh and texlive-alldocumentation)

%description -n texlive-beamertheme-phnompenh-doc
This package includes the documentation for texlive-beamertheme-phnompenh

%post -n texlive-beamertheme-phnompenh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-phnompenh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-phnompenh
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-phnompenh-doc
%{_texmfdistdir}/doc/latex/beamertheme-phnompenh/README
%{_texmfdistdir}/doc/latex/beamertheme-phnompenh/beamerthemePhnomPenh.pdf
%{_texmfdistdir}/doc/latex/beamertheme-phnompenh/beamerthemePhnomPenh.tex

%files -n texlive-beamertheme-phnompenh
%{_texmfdistdir}/tex/latex/beamertheme-phnompenh/beamerthemePhnomPenh.sty

%package -n texlive-beamertheme-pure-minimalistic
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn56934
Release:        0
License:        GPL-2.0-or-later
Summary:        A minimalistic presentation theme for LaTeX Beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-pure-minimalistic-doc >= %{texlive_version}
Provides:       tex(beamercolorthemepureminimalistic.sty)
Provides:       tex(beamerfontthemepureminimalistic.sty)
Provides:       tex(beamerinnerthemepureminimalistic.sty)
Provides:       tex(beamerouterthemepureminimalistic.sty)
Provides:       tex(beamerthemepureminimalistic.sty)
Requires:       tex(FiraMono.sty)
Requires:       tex(FiraSans.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(noto.sty)
Requires:       tex(silence.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source63:       beamertheme-pure-minimalistic.tar.xz
Source64:       beamertheme-pure-minimalistic.doc.tar.xz

%description -n texlive-beamertheme-pure-minimalistic
The main features of this minimalistic Beamer theme are: Easily
use own logos. Customizable. Looks good in a 4:3 and 16:9
aspect ratio, without the need to change anything. Provides an
environment for vertically-spaced items. Provides light and
dark mode. Is designed to be purely minimalistic without any
distractions.

%package -n texlive-beamertheme-pure-minimalistic-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn56934
Release:        0
Summary:        Documentation for texlive-beamertheme-pure-minimalistic
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-pure-minimalistic and texlive-alldocumentation)

%description -n texlive-beamertheme-pure-minimalistic-doc
This package includes the documentation for texlive-beamertheme-pure-minimalistic

%post -n texlive-beamertheme-pure-minimalistic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-pure-minimalistic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-pure-minimalistic
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-pure-minimalistic-doc
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/LICENSE
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/README.md
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/beamertheme-pure-minimalistic-demo.pdf
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/beamertheme-pure-minimalistic-demo.tex
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/demo_bib.bib
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/logos/header_logo.png
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/logos/header_logo_darkmode.png
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/logos/institute_logo.png
%{_texmfdistdir}/doc/latex/beamertheme-pure-minimalistic/logos/institute_logo_darkmode.png

%files -n texlive-beamertheme-pure-minimalistic
%{_texmfdistdir}/tex/latex/beamertheme-pure-minimalistic/beamercolorthemepureminimalistic.sty
%{_texmfdistdir}/tex/latex/beamertheme-pure-minimalistic/beamerfontthemepureminimalistic.sty
%{_texmfdistdir}/tex/latex/beamertheme-pure-minimalistic/beamerinnerthemepureminimalistic.sty
%{_texmfdistdir}/tex/latex/beamertheme-pure-minimalistic/beamerouterthemepureminimalistic.sty
%{_texmfdistdir}/tex/latex/beamertheme-pure-minimalistic/beamerthemepureminimalistic.sty

%package -n texlive-beamertheme-rainbow
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn67542
Release:        0
License:        LPPL-1.0
Summary:        A beamer colour theme which alternates theme colours on every frame
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-rainbow-doc >= %{texlive_version}
Provides:       tex(beamercolorthemerainbow.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source65:       beamertheme-rainbow.tar.xz
Source66:       beamertheme-rainbow.doc.tar.xz

%description -n texlive-beamertheme-rainbow
This package provides a beamer colour theme which alternates
theme colours on every frame.

%package -n texlive-beamertheme-rainbow-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn67542
Release:        0
Summary:        Documentation for texlive-beamertheme-rainbow
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-rainbow and texlive-alldocumentation)

%description -n texlive-beamertheme-rainbow-doc
This package includes the documentation for texlive-beamertheme-rainbow

%post -n texlive-beamertheme-rainbow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-rainbow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-rainbow
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-rainbow-doc
%{_texmfdistdir}/doc/latex/beamertheme-rainbow/README.md
%{_texmfdistdir}/doc/latex/beamertheme-rainbow/beamertheme-rainbow-doc.pdf
%{_texmfdistdir}/doc/latex/beamertheme-rainbow/beamertheme-rainbow-doc.tex

%files -n texlive-beamertheme-rainbow
%{_texmfdistdir}/tex/latex/beamertheme-rainbow/beamercolorthemerainbow.sty

%package -n texlive-beamertheme-saintpetersburg
Version:        %{texlive_version}.%{texlive_noarch}.svn45877
Release:        0
License:        LPPL-1.0
Summary:        A beamer theme that incorporates colours and fonts of Saint Petersburg State University
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-saintpetersburg-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeSaintPetersburg.sty)
Provides:       tex(beamerfontthemeSaintPetersburg.sty)
Provides:       tex(beamerthemeSaintPetersburg.sty)
Requires:       tex(FiraMono.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(opensans.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source67:       beamertheme-saintpetersburg.tar.xz
Source68:       beamertheme-saintpetersburg.doc.tar.xz

%description -n texlive-beamertheme-saintpetersburg
This minimalistic beamer theme incorporates Saint Petersburg
State University colours and fonts. It is suitable for both
presentations and posters.

%package -n texlive-beamertheme-saintpetersburg-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn45877
Release:        0
Summary:        Documentation for texlive-beamertheme-saintpetersburg
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-saintpetersburg and texlive-alldocumentation)

%description -n texlive-beamertheme-saintpetersburg-doc
This package includes the documentation for texlive-beamertheme-saintpetersburg

%post -n texlive-beamertheme-saintpetersburg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-saintpetersburg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-saintpetersburg
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-saintpetersburg-doc
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/README.md
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/SaintPetersburg.pdf
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/example.pdf
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/example.tex
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/propagating-elevation.eps
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/propagating-wave-height-x.eps
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/propagating-wave-length-x.eps
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/propagating-wave-period.eps
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/standing-elevation.eps
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/standing-wave-height-x.eps
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/standing-wave-length-x.eps
%{_texmfdistdir}/doc/latex/beamertheme-saintpetersburg/figures/standing-wave-period.eps

%files -n texlive-beamertheme-saintpetersburg
%{_texmfdistdir}/tex/latex/beamertheme-saintpetersburg/beamercolorthemeSaintPetersburg.sty
%{_texmfdistdir}/tex/latex/beamertheme-saintpetersburg/beamerfontthemeSaintPetersburg.sty
%{_texmfdistdir}/tex/latex/beamertheme-saintpetersburg/beamerthemeSaintPetersburg.sty

%package -n texlive-beamertheme-simpledarkblue
Version:        %{texlive_version}.%{texlive_noarch}.svn60061
Release:        0
License:        SUSE-Public-Domain
Summary:        Template for a simple presentation
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-simpledarkblue-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeSimpleDarkBlue.sty)
Provides:       tex(beamerfontthemeSimpleDarkBlue.sty)
Provides:       tex(beamerthemeSimpleDarkBlue.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source69:       beamertheme-simpledarkblue.tar.xz
Source70:       beamertheme-simpledarkblue.doc.tar.xz

%description -n texlive-beamertheme-simpledarkblue
This is a simple but nice theme for Beamer. Features: simple
structure: with page numbers in footer, no side bar, simple
colors: using only several foreground and background colors.

%package -n texlive-beamertheme-simpledarkblue-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn60061
Release:        0
Summary:        Documentation for texlive-beamertheme-simpledarkblue
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-simpledarkblue and texlive-alldocumentation)

%description -n texlive-beamertheme-simpledarkblue-doc
This package includes the documentation for texlive-beamertheme-simpledarkblue

%post -n texlive-beamertheme-simpledarkblue
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-simpledarkblue
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-simpledarkblue
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-simpledarkblue-doc
%{_texmfdistdir}/doc/latex/beamertheme-simpledarkblue/LICENSE
%{_texmfdistdir}/doc/latex/beamertheme-simpledarkblue/README.md
%{_texmfdistdir}/doc/latex/beamertheme-simpledarkblue/beamertheme-simpledarkblue-sample.pdf
%{_texmfdistdir}/doc/latex/beamertheme-simpledarkblue/beamertheme-simpledarkblue-sample.tex

%files -n texlive-beamertheme-simpledarkblue
%{_texmfdistdir}/tex/latex/beamertheme-simpledarkblue/beamercolorthemeSimpleDarkBlue.sty
%{_texmfdistdir}/tex/latex/beamertheme-simpledarkblue/beamerfontthemeSimpleDarkBlue.sty
%{_texmfdistdir}/tex/latex/beamertheme-simpledarkblue/beamerthemeSimpleDarkBlue.sty

%package -n texlive-beamertheme-simpleplus
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn64770
Release:        0
License:        SUSE-Public-Domain
Summary:        A simple and clean theme for LaTeX beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-simpleplus-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeSimplePlus.sty)
Provides:       tex(beamerfontthemeSimplePlus.sty)
Provides:       tex(beamerinnerthemeSimplePlus.sty)
Provides:       tex(beamerthemeSimplePlus.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source71:       beamertheme-simpleplus.tar.xz
Source72:       beamertheme-simpleplus.doc.tar.xz

%description -n texlive-beamertheme-simpleplus
This package provides a simple and clean theme for LaTeX
Beamer. It can be used for academic and scientific
presentations.

%package -n texlive-beamertheme-simpleplus-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn64770
Release:        0
Summary:        Documentation for texlive-beamertheme-simpleplus
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-simpleplus and texlive-alldocumentation)

%description -n texlive-beamertheme-simpleplus-doc
This package includes the documentation for texlive-beamertheme-simpleplus

%post -n texlive-beamertheme-simpleplus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-simpleplus
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-simpleplus
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-simpleplus-doc
%{_texmfdistdir}/doc/latex/beamertheme-simpleplus/LICENSE
%{_texmfdistdir}/doc/latex/beamertheme-simpleplus/README.md
%{_texmfdistdir}/doc/latex/beamertheme-simpleplus/beamertheme-simpleplus-sample.pdf
%{_texmfdistdir}/doc/latex/beamertheme-simpleplus/beamertheme-simpleplus-sample.tex

%files -n texlive-beamertheme-simpleplus
%{_texmfdistdir}/tex/latex/beamertheme-simpleplus/beamercolorthemeSimplePlus.sty
%{_texmfdistdir}/tex/latex/beamertheme-simpleplus/beamerfontthemeSimplePlus.sty
%{_texmfdistdir}/tex/latex/beamertheme-simpleplus/beamerinnerthemeSimplePlus.sty
%{_texmfdistdir}/tex/latex/beamertheme-simpleplus/beamerthemeSimplePlus.sty

%package -n texlive-beamertheme-tcolorbox
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn67000
Release:        0
License:        LPPL-1.0
Summary:        A beamer inner theme which reproduces standard beamer blocks using tcolorboxes
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-tcolorbox-doc >= %{texlive_version}
Provides:       tex(beamerinnerthemetcolorbox.sty)
Requires:       tex(tcolorbox.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source73:       beamertheme-tcolorbox.tar.xz
Source74:       beamertheme-tcolorbox.doc.tar.xz

%description -n texlive-beamertheme-tcolorbox
This package provides an inner theme for beamer which
reproduces standard beamer blocks using tcolorboxes. The look
and feel (rounded/sharp corners, shadows and colours) will
automatically adapt to which other themes are loaded.

%package -n texlive-beamertheme-tcolorbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn67000
Release:        0
Summary:        Documentation for texlive-beamertheme-tcolorbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-tcolorbox and texlive-alldocumentation)

%description -n texlive-beamertheme-tcolorbox-doc
This package includes the documentation for texlive-beamertheme-tcolorbox

%post -n texlive-beamertheme-tcolorbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-tcolorbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-tcolorbox
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-tcolorbox-doc
%{_texmfdistdir}/doc/latex/beamertheme-tcolorbox/README.md
%{_texmfdistdir}/doc/latex/beamertheme-tcolorbox/beamertheme-tcolorbox-doc.pdf
%{_texmfdistdir}/doc/latex/beamertheme-tcolorbox/beamertheme-tcolorbox-doc.tex

%files -n texlive-beamertheme-tcolorbox
%{_texmfdistdir}/tex/latex/beamertheme-tcolorbox/beamerinnerthemetcolorbox.sty

%package -n texlive-beamertheme-trigon
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn65985
Release:        0
License:        LPPL-1.0
Summary:        A modern, elegant, and versatile theme for Beamer
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-trigon-doc >= %{texlive_version}
Provides:       tex(beamercolorthemetrigon.sty)
Provides:       tex(beamerfontthemetrigon.sty)
Provides:       tex(beamerinnerthemetrigon.sty)
Provides:       tex(beamerouterthemetrigon.sty)
Provides:       tex(beamerthemetrigon.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(sourcesanspro.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source75:       beamertheme-trigon.tar.xz
Source76:       beamertheme-trigon.doc.tar.xz

%description -n texlive-beamertheme-trigon
This package provides a modern, elegant and versatile theme for
Beamer, with a high degree of customization. Trigon found its
origin and inspiration in the graphical guidelines resulting
from the visual identity overhaul of the University of Liege.
Although directly inspired from these guidelines, the theme was
stripped out of any mention or specificities related to the
University and its faculties. This makes the Trigon theme
perfectly suitable for many different contexts. The final
product provides a modern, elegant and versatile theme with a
high degree of customization. The main design focuses on
triangular shapes for major layout elements and noise
minimization for the main body of the work. The theme's
implementation is heavily inspired from the Metropolis theme.
Most options from Metropolis have been ported to Trigon in
order to improve customization and ease-of-use. Trigon also
includes different styles and layouts for the main title page,
the section page and the default slide background.

%package -n texlive-beamertheme-trigon-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn65985
Release:        0
Summary:        Documentation for texlive-beamertheme-trigon
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-trigon and texlive-alldocumentation)

%description -n texlive-beamertheme-trigon-doc
This package includes the documentation for texlive-beamertheme-trigon

%post -n texlive-beamertheme-trigon
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-trigon
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-trigon
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-trigon-doc
%{_texmfdistdir}/doc/latex/beamertheme-trigon/README.md
%{_texmfdistdir}/doc/latex/beamertheme-trigon/frames.tex
%{_texmfdistdir}/doc/latex/beamertheme-trigon/library.jpg
%{_texmfdistdir}/doc/latex/beamertheme-trigon/trigon_demo.pdf
%{_texmfdistdir}/doc/latex/beamertheme-trigon/trigon_demo.tex
%{_texmfdistdir}/doc/latex/beamertheme-trigon/trigon_full.pdf
%{_texmfdistdir}/doc/latex/beamertheme-trigon/trigon_small.pdf
%{_texmfdistdir}/doc/latex/beamertheme-trigon/trigontheme.pdf

%files -n texlive-beamertheme-trigon
%{_texmfdistdir}/tex/latex/beamertheme-trigon/beamercolorthemetrigon.sty
%{_texmfdistdir}/tex/latex/beamertheme-trigon/beamerfontthemetrigon.sty
%{_texmfdistdir}/tex/latex/beamertheme-trigon/beamerinnerthemetrigon.sty
%{_texmfdistdir}/tex/latex/beamertheme-trigon/beamerouterthemetrigon.sty
%{_texmfdistdir}/tex/latex/beamertheme-trigon/beamerthemetrigon.sty

%package -n texlive-beamertheme-upenn-bc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn29937
Release:        0
License:        LPPL-1.0
Summary:        Beamer themes for Boston College and the University of Pennsylvania
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamertheme-upenn-bc-doc >= %{texlive_version}
Provides:       tex(beamercolorthemegoeagles.sty)
Provides:       tex(beamercolorthemepenn.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source77:       beamertheme-upenn-bc.tar.xz
Source78:       beamertheme-upenn-bc.doc.tar.xz

%description -n texlive-beamertheme-upenn-bc
Beamer themes in the colors of the University of Pennsylvania,
USA, and Boston College, USA. Both were tested for the
presentation theme 'Warsaw'. Please note that these color
themes are neither official nor exact! The colours are
approximated from the universities' style guidelines and
websites, and slightly modified where necessary to generate an
appealing look. The universities neither endorse, nor provide
any support for, these color themes. I give no warranty for the
code.

%package -n texlive-beamertheme-upenn-bc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn29937
Release:        0
Summary:        Documentation for texlive-beamertheme-upenn-bc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamertheme-upenn-bc and texlive-alldocumentation)

%description -n texlive-beamertheme-upenn-bc-doc
This package includes the documentation for texlive-beamertheme-upenn-bc

%post -n texlive-beamertheme-upenn-bc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamertheme-upenn-bc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamertheme-upenn-bc
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamertheme-upenn-bc-doc
%{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/README
%{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/beamerBCstyle.pdf
%{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/beamerBCstyle.tex
%{_texmfdistdir}/doc/latex/beamertheme-upenn-bc/beamerPENNstyle.pdf

%files -n texlive-beamertheme-upenn-bc
%{_texmfdistdir}/tex/latex/beamertheme-upenn-bc/beamercolorthemegoeagles.sty
%{_texmfdistdir}/tex/latex/beamertheme-upenn-bc/beamercolorthemepenn.sty

%package -n texlive-beamerthemeamurmaple
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn69742
Release:        0
License:        LPPL-1.0
Summary:        A new modern beamer theme
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerthemeamurmaple-doc >= %{texlive_version}
Provides:       tex(beamerthemeAmurmaple.sty)
Requires:       tex(expl3.sty)
Requires:       tex(fontawesome5.sty)
Requires:       tex(iftex.sty)
Requires:       tex(luamesh.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pgfpages.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(xfp.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source79:       beamerthemeamurmaple.tar.xz
Source80:       beamerthemeamurmaple.doc.tar.xz

%description -n texlive-beamerthemeamurmaple
This Beamer theme is a suitable theme for my use of Beamer in
applied mathematics research. It meets my needs in my work.
However, if you like this theme, and if you want to ask for or
make improvements, don't hesitate to write to me!

%package -n texlive-beamerthemeamurmaple-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn69742
Release:        0
Summary:        Documentation for texlive-beamerthemeamurmaple
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerthemeamurmaple and texlive-alldocumentation)

%description -n texlive-beamerthemeamurmaple-doc
This package includes the documentation for texlive-beamerthemeamurmaple

%post -n texlive-beamerthemeamurmaple
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerthemeamurmaple
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerthemeamurmaple
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerthemeamurmaple-doc
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/LICENSE
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/README.md
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-black.pdf
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-blue.pdf
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-doc.pdf
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-doc.tex
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-green.pdf
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-leftframetitle.pdf
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-sidebar.pdf
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/beamer-amurmaple-test.pdf
%{_texmfdistdir}/doc/latex/beamerthemeamurmaple/logo.png

%files -n texlive-beamerthemeamurmaple
%{_texmfdistdir}/tex/latex/beamerthemeamurmaple/beamerthemeAmurmaple.sty

%package -n texlive-beamerthemeconcrete
Version:        %{texlive_version}.%{texlive_noarch}.2024bsvn69528
Release:        0
License:        LPPL-1.0
Summary:        A collection of flat beamer themes
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerthemeconcrete-doc >= %{texlive_version}
Provides:       tex(beamerthemecbernoulli.sty)
Provides:       tex(beamerthemecdirichlet.sty)
Provides:       tex(beamerthemecfermat.sty)
Provides:       tex(beamerthemecgauss.sty)
Provides:       tex(beamerthemeclagrange.sty)
Provides:       tex(beamerthemecmobius.sty)
Provides:       tex(beamerthemecriemann.sty)
Requires:       tex(adjustbox.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontawesome.sty)
Requires:       tex(manfnt.sty)
Requires:       tex(multicol.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varwidth.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source81:       beamerthemeconcrete.tar.xz
Source82:       beamerthemeconcrete.doc.tar.xz

%description -n texlive-beamerthemeconcrete
The concrete bundle provides a collection of flat beamer themes
for making LaTeX presentations, especially for academic and
scientific presentations.

%package -n texlive-beamerthemeconcrete-doc
Version:        %{texlive_version}.%{texlive_noarch}.2024bsvn69528
Release:        0
Summary:        Documentation for texlive-beamerthemeconcrete
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerthemeconcrete and texlive-alldocumentation)

%description -n texlive-beamerthemeconcrete-doc
This package includes the documentation for texlive-beamerthemeconcrete

%post -n texlive-beamerthemeconcrete
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerthemeconcrete
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerthemeconcrete
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerthemeconcrete-doc
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/README.md
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cbernoulli.pdf
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cbernoulli.tex
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cdirichlet.pdf
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cdirichlet.tex
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cfermat.pdf
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cfermat.tex
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cgauss.pdf
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cgauss.tex
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-clagrange.pdf
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-clagrange.tex
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cmobius.pdf
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-cmobius.tex
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-criemann.pdf
%{_texmfdistdir}/doc/latex/beamerthemeconcrete/demo-criemann.tex

%files -n texlive-beamerthemeconcrete
%{_texmfdistdir}/tex/latex/beamerthemeconcrete/beamerthemecbernoulli.sty
%{_texmfdistdir}/tex/latex/beamerthemeconcrete/beamerthemecdirichlet.sty
%{_texmfdistdir}/tex/latex/beamerthemeconcrete/beamerthemecfermat.sty
%{_texmfdistdir}/tex/latex/beamerthemeconcrete/beamerthemecgauss.sty
%{_texmfdistdir}/tex/latex/beamerthemeconcrete/beamerthemeclagrange.sty
%{_texmfdistdir}/tex/latex/beamerthemeconcrete/beamerthemecmobius.sty
%{_texmfdistdir}/tex/latex/beamerthemeconcrete/beamerthemecriemann.sty

%package -n texlive-beamerthemejltree
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn21977
Release:        0
License:        GPL-2.0-or-later
Summary:        Contributed beamer theme
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Provides:       tex(beamerthemeJLTree.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source83:       beamerthemejltree.tar.xz

%description -n texlive-beamerthemejltree
A theme for beamer presentations.

%post -n texlive-beamerthemejltree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerthemejltree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerthemejltree
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerthemejltree
%{_texmfdistdir}/tex/latex/beamerthemejltree/beamerthemeJLTree.sty

%package -n texlive-beamerthemelalic
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn58777
Release:        0
License:        GPL-2.0-or-later
Summary:        A beamer theme for LALIC
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerthemelalic-doc >= %{texlive_version}
Provides:       tex(beamercolorthemelalic.sty)
Provides:       tex(beamerfontthemelalic.sty)
Provides:       tex(beamerinnerthemelalic.sty)
Provides:       tex(beamerouterthemelalic.sty)
Provides:       tex(beamerthemelalic.sty)
Requires:       tex(calculator.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source84:       beamerthemelalic.tar.xz
Source85:       beamerthemelalic.doc.tar.xz

%description -n texlive-beamerthemelalic
This package provides the beamer theme for LALIC (Laboratorio
de Linguistica e Inteligencia Computacional of the Federal
University of Sao Carlos, Brazil).

%package -n texlive-beamerthemelalic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn58777
Release:        0
Summary:        Documentation for texlive-beamerthemelalic
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerthemelalic and texlive-alldocumentation)

%description -n texlive-beamerthemelalic-doc
This package includes the documentation for texlive-beamerthemelalic

%post -n texlive-beamerthemelalic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerthemelalic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerthemelalic
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerthemelalic-doc
%{_texmfdistdir}/doc/latex/beamerthemelalic/LICENSE
%{_texmfdistdir}/doc/latex/beamerthemelalic/README.md
%{_texmfdistdir}/doc/latex/beamerthemelalic/beamerthemelalic-exemplo.pdf
%{_texmfdistdir}/doc/latex/beamerthemelalic/beamerthemelalic-exemplo.tex

%files -n texlive-beamerthemelalic
%{_texmfdistdir}/tex/latex/beamerthemelalic/beamercolorthemelalic.sty
%{_texmfdistdir}/tex/latex/beamerthemelalic/beamerfontthemelalic.sty
%{_texmfdistdir}/tex/latex/beamerthemelalic/beamerinnerthemelalic.sty
%{_texmfdistdir}/tex/latex/beamerthemelalic/beamerouterthemelalic.sty
%{_texmfdistdir}/tex/latex/beamerthemelalic/beamerthemelalic.sty

%package -n texlive-beamerthemenirma
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn20765
Release:        0
License:        LPPL-1.0
Summary:        A Beamer theme for academic presentations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerthemenirma-doc >= %{texlive_version}
Provides:       tex(beamerthemenirma.sty)
Requires:       tex(beamerbasethemes.sty)
Requires:       tex(pgf.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source86:       beamerthemenirma.tar.xz
Source87:       beamerthemenirma.doc.tar.xz

%description -n texlive-beamerthemenirma
The package developed for academic purposes. The distribution
includes nothing more than style file needed for preparing
presentations.

%package -n texlive-beamerthemenirma-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn20765
Release:        0
Summary:        Documentation for texlive-beamerthemenirma
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerthemenirma and texlive-alldocumentation)

%description -n texlive-beamerthemenirma-doc
This package includes the documentation for texlive-beamerthemenirma

%post -n texlive-beamerthemenirma
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerthemenirma
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerthemenirma
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerthemenirma-doc
%{_texmfdistdir}/doc/latex/beamerthemenirma/README

%files -n texlive-beamerthemenirma
%{_texmfdistdir}/tex/latex/beamerthemenirma/beamerthemenirma.sty

%package -n texlive-beamerthemenord
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn56180
Release:        0
License:        LPPL-1.0
Summary:        A simple beamer theme using the "Nord" color theme
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beamerthemenord-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeNord.sty)
Provides:       tex(beamerfontthemeNord.sty)
Provides:       tex(beamerthemeNord.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source88:       beamerthemenord.tar.xz
Source89:       beamerthemenord.doc.tar.xz

%description -n texlive-beamerthemenord
This package provides a simple beamer theme using the Nord
color theme.

%package -n texlive-beamerthemenord-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn56180
Release:        0
Summary:        Documentation for texlive-beamerthemenord
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beamerthemenord and texlive-alldocumentation)

%description -n texlive-beamerthemenord-doc
This package includes the documentation for texlive-beamerthemenord

%post -n texlive-beamerthemenord
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beamerthemenord
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beamerthemenord
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beamerthemenord-doc
%{_texmfdistdir}/doc/latex/beamerthemenord/README.md
%{_texmfdistdir}/doc/latex/beamerthemenord/beamerthemeNord.pdf
%{_texmfdistdir}/doc/latex/beamerthemenord/beamerthemeNord.tex
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/dark-blocks.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/dark-colors.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/dark-fonts.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/dark-titlepage.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/dark-toc.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/dark-usage.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/light-blocks.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/light-colors.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/light-fonts.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/light-titlepage.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/light-toc.png
%{_texmfdistdir}/doc/latex/beamerthemenord/screenshots/light-usage.png

%files -n texlive-beamerthemenord
%{_texmfdistdir}/tex/latex/beamerthemenord/beamercolorthemeNord.sty
%{_texmfdistdir}/tex/latex/beamerthemenord/beamerfontthemeNord.sty
%{_texmfdistdir}/tex/latex/beamerthemenord/beamerthemeNord.sty

%package -n texlive-bearwear
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn54826
Release:        0
License:        LPPL-1.0
Summary:        Shirts to dress TikZbears
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bearwear-doc >= %{texlive_version}
Provides:       tex(bearwear.sty)
Requires:       tex(tikzlings-bears.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source90:       bearwear.tar.xz
Source91:       bearwear.doc.tar.xz

%description -n texlive-bearwear
The package offers tools to create shirts for TikZbears from
the TikZlings package.

%package -n texlive-bearwear-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn54826
Release:        0
Summary:        Documentation for texlive-bearwear
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bearwear and texlive-alldocumentation)

%description -n texlive-bearwear-doc
This package includes the documentation for texlive-bearwear

%post -n texlive-bearwear
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bearwear
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bearwear
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bearwear-doc
%{_texmfdistdir}/doc/latex/bearwear/README.md
%{_texmfdistdir}/doc/latex/bearwear/baer.png
%{_texmfdistdir}/doc/latex/bearwear/bearwear-doc.tex
%{_texmfdistdir}/doc/latex/bearwear/bearwear.pdf
%{_texmfdistdir}/doc/latex/bearwear/flag.pdf
%{_texmfdistdir}/doc/latex/bearwear/latex-project-logo.pdf
%{_texmfdistdir}/doc/latex/bearwear/montblanc.jpg
%{_texmfdistdir}/doc/latex/bearwear/tartan3.jpg
%{_texmfdistdir}/doc/latex/bearwear/ulrike.pdf

%files -n texlive-bearwear
%{_texmfdistdir}/tex/latex/bearwear/bearwear.sty

%package -n texlive-beaulivre
Version:        %{texlive_version}.%{texlive_noarch}.svn70049
Release:        0
License:        LPPL-1.0
Summary:        Write your books in a colorful way
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-colorist >= %{texlive_version}
#!BuildIgnore: texlive-colorist
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beaulivre-doc >= %{texlive_version}
Provides:       tex(beaulivre.cls)
Requires:       tex(amssymb.sty)
Requires:       tex(caption.sty)
Requires:       tex(colorist.sty)
Requires:       tex(ctex.sty)
Requires:       tex(draftwatermark.sty)
Requires:       tex(embrac.sty)
Requires:       tex(float.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(lua-widow-control.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(nowidow.sty)
Requires:       tex(projlib-font.sty)
Requires:       tex(regexpatch.sty)
Requires:       tex(silence.sty)
Requires:       tex(tikz-cd.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(wrapfig.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source92:       beaulivre.tar.xz
Source93:       beaulivre.doc.tar.xz

%description -n texlive-beaulivre
This package provides a LaTeX class for typesetting books with
a colorful design. Currently, it has native support for Chinese
(both simplified and traditional), English, French, German,
Italian, Japanese, Portuguese (European and Brazilian), Russian
and Spanish typesetting. It compiles with either XeLaTeX or
LuaLaTeX. This is part of the colorist class series and depends
on colorist.sty from the colorist package. The package name
"beaulivre" is taken from the French words "beau" (=
"beautiful") and "livre" (= "book").

%package -n texlive-beaulivre-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn70049
Release:        0
Summary:        Documentation for texlive-beaulivre
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beaulivre and texlive-alldocumentation)

%description -n texlive-beaulivre-doc
This package includes the documentation for texlive-beaulivre

%post -n texlive-beaulivre
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beaulivre
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beaulivre
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beaulivre-doc
%{_texmfdistdir}/doc/latex/beaulivre/DEPENDS.txt
%{_texmfdistdir}/doc/latex/beaulivre/LICENSE
%{_texmfdistdir}/doc/latex/beaulivre/README.md

%files -n texlive-beaulivre
%{_texmfdistdir}/tex/latex/beaulivre/beaulivre.cls

%package -n texlive-beautybook
Version:        %{texlive_version}.%{texlive_noarch}.svn68438
Release:        0
License:        LPPL-1.0
Summary:        A beautiful book template for maths and science
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beautybook-doc >= %{texlive_version}
Provides:       tex(Beautybook-CN.cls)
Provides:       tex(Beautybook-EN.cls)
Provides:       tex(Beautybook-bottompage.sty)
Provides:       tex(Beautybook-cover-birkar.sty)
Provides:       tex(Beautybook-cover-cn.sty)
Provides:       tex(Beautybook-cover-en.sty)
Provides:       tex(Beautybook-cover-enfig.sty)
Requires:       tex(adjustbox.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(appendix.sty)
Requires:       tex(bclogo.sty)
Requires:       tex(bm.sty)
Requires:       tex(book.cls)
Requires:       tex(bropd.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(cncolours.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(ctexbook.cls)
Requires:       tex(dashrule.sty)
Requires:       tex(ean13isbn.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(epigraph-keys.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(extarrows.sty)
Requires:       tex(fitbox.sty)
Requires:       tex(fontawesome5.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multicol.sty)
Requires:       tex(ninecolors.sty)
Requires:       tex(paracol.sty)
Requires:       tex(pgfornament-han.sty)
Requires:       tex(pgfornament.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(rotating.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(stix.sty)
Requires:       tex(tabularray.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(thm-restate.sty)
Requires:       tex(thmtools.sty)
Requires:       tex(tikz-cd.sty)
Requires:       tex(tikz-imagelabels.sty)
Requires:       tex(tikz.sty)
Requires:       tex(times.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(todonotes.sty)
Requires:       tex(ulem.sty)
Requires:       tex(upgreek.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(zhnumber.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source94:       beautybook.tar.xz
Source95:       beautybook.doc.tar.xz

%description -n texlive-beautybook
The package contains LaTeX classes (both a Chinese and an
English version) as well as style files for creating beautiful
science books.

%package -n texlive-beautybook-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn68438
Release:        0
Summary:        Documentation for texlive-beautybook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beautybook and texlive-alldocumentation)

%description -n texlive-beautybook-doc
This package includes the documentation for texlive-beautybook

%post -n texlive-beautybook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beautybook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beautybook
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beautybook-doc
%{_texmfdistdir}/doc/latex/beautybook/Beautybook-cn.pdf
%{_texmfdistdir}/doc/latex/beautybook/Beautybook-cn.tex
%{_texmfdistdir}/doc/latex/beautybook/README.md
%{_texmfdistdir}/doc/latex/beautybook/beautybook-en.pdf
%{_texmfdistdir}/doc/latex/beautybook/beautybook-en.tex
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/coverimage.jpg
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/ivy-ge998908f8_1280.jpg
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/logo.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/even1.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/even2.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/even3.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/even4.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid1.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid10.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid11.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid2.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid3.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid4.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid5.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid6.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid7.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid8.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/mid9.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd1.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd10.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd11.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd12.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd13.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd14.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd15.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd2.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd3.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd4.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd5.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd6.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd7.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd8.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/odd9.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/songeven.png
%{_texmfdistdir}/doc/latex/beautybook/inner_pics/titleimages/songodd.png
%{_texmfdistdir}/doc/latex/beautybook/ref.bib

%files -n texlive-beautybook
%{_texmfdistdir}/tex/latex/beautybook/Beautybook-CN.cls
%{_texmfdistdir}/tex/latex/beautybook/Beautybook-EN.cls
%{_texmfdistdir}/tex/latex/beautybook/stys/Beautybook-bottompage.sty
%{_texmfdistdir}/tex/latex/beautybook/stys/Beautybook-cover-birkar.sty
%{_texmfdistdir}/tex/latex/beautybook/stys/Beautybook-cover-cn.sty
%{_texmfdistdir}/tex/latex/beautybook/stys/Beautybook-cover-en.sty
%{_texmfdistdir}/tex/latex/beautybook/stys/Beautybook-cover-enfig.sty

%package -n texlive-beautynote
Version:        %{texlive_version}.%{texlive_noarch}.svn70155
Release:        0
License:        LPPL-1.0
Summary:        A package designed to meet the publication of books and the production of LaTeX templates, with elegant chapter
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beautynote-doc >= %{texlive_version}
Provides:       tex(beautynote.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(bbding.sty)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(bropd.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(doclicense.sty)
Requires:       tex(empheq.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(extramarks.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fbox.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(mdframed.sty)
Requires:       tex(ninecolors.sty)
Requires:       tex(pgfornament-han.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(physics.sty)
Requires:       tex(pifont.sty)
Requires:       tex(psfrag.sty)
Requires:       tex(report.cls)
Requires:       tex(rotating.sty)
Requires:       tex(shadowtext.sty)
Requires:       tex(tikz.sty)
Requires:       tex(times.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(transparent.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source96:       beautynote.tar.xz
Source97:       beautynote.doc.tar.xz

%description -n texlive-beautynote
The package is a specially designed to meet the publication of
books and the production of LaTeX templates, with elegant
chapter styles and unique page styles.

%package -n texlive-beautynote-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn70155
Release:        0
Summary:        Documentation for texlive-beautynote
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beautynote and texlive-alldocumentation)

%description -n texlive-beautynote-doc
This package includes the documentation for texlive-beautynote

%post -n texlive-beautynote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beautynote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beautynote
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beautynote-doc
%{_texmfdistdir}/doc/latex/beautynote/README.md
%{_texmfdistdir}/doc/latex/beautynote/beautynote.pdf
%{_texmfdistdir}/doc/latex/beautynote/beautynote.tex
%{_texmfdistdir}/doc/latex/beautynote/figures/fibonacci.jpg
%{_texmfdistdir}/doc/latex/beautynote/figures/titlepage.png

%files -n texlive-beautynote
%{_texmfdistdir}/tex/latex/beautynote/beautynote.cls

%package -n texlive-beebe
Version:        %{texlive_version}.%{texlive_noarch}.svn70062
Release:        0
License:        SUSE-Public-Domain
Summary:        A collection of bibliographies
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Provides:       tex(bibnames.sty)
Provides:       tex(texnames.sty)
Provides:       tex(tugboat.def)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source98:       beebe.tar.xz

%description -n texlive-beebe
A collection of BibTeX bibliographies on TeX-related topics
(including, for example, spell-checking and SGML). Each
includes a LaTeX wrapper file to typeset the bibliography.

%post -n texlive-beebe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beebe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beebe
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beebe
%{_texmfdistdir}/bibtex/bib/beebe/epodd.bib
%{_texmfdistdir}/bibtex/bib/beebe/font.bib
%{_texmfdistdir}/bibtex/bib/beebe/printing-history.bib
%{_texmfdistdir}/bibtex/bib/beebe/serif.bib
%{_texmfdistdir}/bibtex/bib/beebe/texbook1.bib
%{_texmfdistdir}/bibtex/bib/beebe/texbook2.bib
%{_texmfdistdir}/bibtex/bib/beebe/texbook3.bib
%{_texmfdistdir}/bibtex/bib/beebe/texgraph.bib
%{_texmfdistdir}/bibtex/bib/beebe/texjourn.bib
%{_texmfdistdir}/bibtex/bib/beebe/texnique.bib
%{_texmfdistdir}/bibtex/bib/beebe/tugboat.bib
%{_texmfdistdir}/bibtex/bib/beebe/type.bib
%{_texmfdistdir}/bibtex/bib/beebe/typeset.bib
%{_texmfdistdir}/tex/generic/beebe/bibnames.sty
%{_texmfdistdir}/tex/generic/beebe/texnames.sty
%{_texmfdistdir}/tex/generic/beebe/tugboat.def

%package -n texlive-begingreek
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn63255
Release:        0
License:        LPPL-1.0
Summary:        Greek environment to be used with pdfLaTeX only
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-begingreek-doc >= %{texlive_version}
Provides:       tex(begingreek.sty)
Requires:       tex(iftex.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source99:       begingreek.tar.xz
Source100:      begingreek.doc.tar.xz

%description -n texlive-begingreek
This simple package defines a greek environment to be used with
pdfLaTeX only, that accepts an optional Greek font family name
to type its contents with. A similar \greektxt command does a
similar action for shorter texts.

%package -n texlive-begingreek-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn63255
Release:        0
Summary:        Documentation for texlive-begingreek
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-begingreek and texlive-alldocumentation)

%description -n texlive-begingreek-doc
This package includes the documentation for texlive-begingreek

%post -n texlive-begingreek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-begingreek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-begingreek
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-begingreek-doc
%{_texmfdistdir}/doc/latex/begingreek/README.txt
%{_texmfdistdir}/doc/latex/begingreek/begingreek.pdf

%files -n texlive-begingreek
%{_texmfdistdir}/tex/latex/begingreek/begingreek.sty

%package -n texlive-begriff
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Typeset Begriffschrift
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-begriff-doc >= %{texlive_version}
Provides:       tex(begriff.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source101:      begriff.tar.xz
Source102:      begriff.doc.tar.xz

%description -n texlive-begriff
The package defines maths mode commands for typesetting Frege's
Begriffschrift.

%package -n texlive-begriff-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn15878
Release:        0
Summary:        Documentation for texlive-begriff
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-begriff and texlive-alldocumentation)

%description -n texlive-begriff-doc
This package includes the documentation for texlive-begriff

%post -n texlive-begriff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-begriff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-begriff
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-begriff-doc
%{_texmfdistdir}/doc/latex/begriff/COPYING
%{_texmfdistdir}/doc/latex/begriff/README
%{_texmfdistdir}/doc/latex/begriff/examples.pdf
%{_texmfdistdir}/doc/latex/begriff/examples.tex

%files -n texlive-begriff
%{_texmfdistdir}/tex/latex/begriff/begriff.sty

%package -n texlive-beilstein
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn56193
Release:        0
License:        LPPL-1.0
Summary:        Support for submissions to the "Beilstein Journal of Nanotechnology"
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beilstein-doc >= %{texlive_version}
Provides:       tex(beilstein.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(flafter.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lineno.sty)
Requires:       tex(longtable.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(newtxtt.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tgheros.sty)
Requires:       tex(url.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source103:      beilstein.tar.xz
Source104:      beilstein.doc.tar.xz

%description -n texlive-beilstein
The package provides a LaTeX class file and a BibTeX style file
in accordance with the requirements of submissions to the
``Beilstein Journal of Nanotechnology''. Although the files can
be used for any kind of document, they have only been designed
and tested to be suitable for submissions to the Beilstein
Journal of Nanotechnology.

%package -n texlive-beilstein-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn56193
Release:        0
Summary:        Documentation for texlive-beilstein
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beilstein and texlive-alldocumentation)

%description -n texlive-beilstein-doc
This package includes the documentation for texlive-beilstein

%post -n texlive-beilstein
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beilstein
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beilstein
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beilstein-doc
%{_texmfdistdir}/doc/latex/beilstein/BJNANO_Technical_Handbook.pdf
%{_texmfdistdir}/doc/latex/beilstein/CHANGELOG.md
%{_texmfdistdir}/doc/latex/beilstein/README.md
%{_texmfdistdir}/doc/latex/beilstein/beilstein-template.bib
%{_texmfdistdir}/doc/latex/beilstein/beilstein-template.tex
%{_texmfdistdir}/doc/latex/beilstein/figure1.pdf
%{_texmfdistdir}/doc/latex/beilstein/scheme1.pdf
%{_texmfdistdir}/doc/latex/beilstein/scheme2.pdf

%files -n texlive-beilstein
%{_texmfdistdir}/bibtex/bst/beilstein/bjnano.bst
%{_texmfdistdir}/tex/latex/beilstein/beilstein.cls

%package -n texlive-belleek
Version:        %{texlive_version}.%{texlive_noarch}.svn66115
Release:        0
License:        SUSE-Public-Domain
Summary:        Free replacement for basic MathTime fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Requires:       texlive-belleek-fonts >= %{texlive_version}
Suggests:       texlive-belleek-doc >= %{texlive_version}
Provides:       tex(belleek.map)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source105:      belleek.tar.xz
Source106:      belleek.doc.tar.xz

%description -n texlive-belleek
This package replaces the original MathTime fonts, not
MathTime-Plus or MathTime Professional (the last being the only
currently available commercial bundle).

%package -n texlive-belleek-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn66115
Release:        0
Summary:        Documentation for texlive-belleek
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-belleek and texlive-alldocumentation)

%description -n texlive-belleek-doc
This package includes the documentation for texlive-belleek

%package -n texlive-belleek-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn66115
Release:        0
Summary:        Severed fonts for texlive-belleek
License:        SUSE-Public-Domain
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

%description -n texlive-belleek-fonts
The  separated fonts package for texlive-belleek

%post -n texlive-belleek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap belleek.map' >> /var/run/texlive/run-updmap

%postun -n texlive-belleek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap belleek.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-belleek
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-belleek-fonts

%files -n texlive-belleek-doc
%{_texmfdistdir}/doc/fonts/belleek/README

%files -n texlive-belleek
%{_texmfdistdir}/fonts/map/dvips/belleek/belleek.map
%verify(link) %{_texmfdistdir}/fonts/truetype/public/belleek/blex.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/belleek/blsy.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/belleek/rblmi.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/belleek/blex.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/belleek/blsy.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/belleek/rblmi.pfb

%files -n texlive-belleek-fonts
%dir %{_datadir}/fonts/texlive-belleek
%{_datadir}/fontconfig/conf.avail/58-texlive-belleek.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-belleek.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-belleek.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-belleek/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-belleek/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-belleek/fonts.scale
%{_datadir}/fonts/texlive-belleek/blex.ttf
%{_datadir}/fonts/texlive-belleek/blsy.ttf
%{_datadir}/fonts/texlive-belleek/rblmi.ttf
%{_datadir}/fonts/texlive-belleek/blex.pfb
%{_datadir}/fonts/texlive-belleek/blsy.pfb
%{_datadir}/fonts/texlive-belleek/rblmi.pfb

%package -n texlive-bengali
Version:        %{texlive_version}.%{texlive_noarch}.svn55475
Release:        0
License:        LPPL-1.0
Summary:        Support for the Bengali language
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bengali-doc >= %{texlive_version}
Provides:       tex(beng.sty)
Provides:       tex(bnr10.tfm)
Provides:       tex(bnsl10.tfm)
Provides:       tex(ubn.fd)
Provides:       tex(ubnx.fd)
Provides:       tex(xbnr10.tfm)
Provides:       tex(xbnsl10.tfm)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source107:      bengali.tar.xz
Source108:      bengali.doc.tar.xz

%description -n texlive-bengali
The package is based on Velthuis' transliteration scheme, with
extensions to deal with the Bengali letters that are not in
Devanagari. The package also supports Assamese.

%package -n texlive-bengali-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn55475
Release:        0
Summary:        Documentation for texlive-bengali
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bengali and texlive-alldocumentation)

%description -n texlive-bengali-doc
This package includes the documentation for texlive-bengali

%post -n texlive-bengali
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bengali
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bengali
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bengali-doc
%{_texmfdistdir}/doc/fonts/bengali/README
%{_texmfdistdir}/doc/fonts/bengali/bengdoc.bn
%{_texmfdistdir}/doc/fonts/bengali/bengdoc.pdf
%{_texmfdistdir}/doc/fonts/bengali/example.bn
%{_texmfdistdir}/doc/fonts/bengali/example.pdf
%{_texmfdistdir}/doc/fonts/bengali/manifest.txt

%files -n texlive-bengali
%{_texmfdistdir}/fonts/source/public/bengali/bn.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnbanjon.mf
%{_texmfdistdir}/fonts/source/public/bengali/bndigit.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnjuk.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnkaar.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnlig.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnligtbl.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnmacro.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnmisc.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnpunct.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnr10.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnsl10.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnswar.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnr10.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnsl10.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnsupp.mf
%{_texmfdistdir}/fonts/tfm/public/bengali/bnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/bnsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/xbnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/xbnsl10.tfm
%{_texmfdistdir}/tex/latex/bengali/beng.sty
%{_texmfdistdir}/tex/latex/bengali/ubn.fd
%{_texmfdistdir}/tex/latex/bengali/ubnx.fd

%package -n texlive-bera
Version:        %{texlive_version}.%{texlive_noarch}.svn20031
Release:        0
License:        LPPL-1.0
Summary:        Bera fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Requires:       texlive-bera-fonts >= %{texlive_version}
Suggests:       texlive-bera-doc >= %{texlive_version}
Provides:       tex(bera.map)
Provides:       tex(bera.sty)
Provides:       tex(beramono.sty)
Provides:       tex(berasans.sty)
Provides:       tex(beraserif.sty)
Provides:       tex(fveb8a.tfm)
Provides:       tex(fveb8c.tfm)
Provides:       tex(fveb8c.vf)
Provides:       tex(fveb8r.tfm)
Provides:       tex(fveb8t.tfm)
Provides:       tex(fveb8t.vf)
Provides:       tex(fvebo8c.tfm)
Provides:       tex(fvebo8c.vf)
Provides:       tex(fvebo8r.tfm)
Provides:       tex(fvebo8t.tfm)
Provides:       tex(fvebo8t.vf)
Provides:       tex(fver8a.tfm)
Provides:       tex(fver8c.tfm)
Provides:       tex(fver8c.vf)
Provides:       tex(fver8r.tfm)
Provides:       tex(fver8t.tfm)
Provides:       tex(fver8t.vf)
Provides:       tex(fvero8c.tfm)
Provides:       tex(fvero8c.vf)
Provides:       tex(fvero8r.tfm)
Provides:       tex(fvero8t.tfm)
Provides:       tex(fvero8t.vf)
Provides:       tex(fvmb8a.tfm)
Provides:       tex(fvmb8c.tfm)
Provides:       tex(fvmb8c.vf)
Provides:       tex(fvmb8r.tfm)
Provides:       tex(fvmb8t.tfm)
Provides:       tex(fvmb8t.vf)
Provides:       tex(fvmbo8a.tfm)
Provides:       tex(fvmbo8c.tfm)
Provides:       tex(fvmbo8c.vf)
Provides:       tex(fvmbo8r.tfm)
Provides:       tex(fvmbo8t.tfm)
Provides:       tex(fvmbo8t.vf)
Provides:       tex(fvmr8a.tfm)
Provides:       tex(fvmr8c.tfm)
Provides:       tex(fvmr8c.vf)
Provides:       tex(fvmr8r.tfm)
Provides:       tex(fvmr8t.tfm)
Provides:       tex(fvmr8t.vf)
Provides:       tex(fvmro8a.tfm)
Provides:       tex(fvmro8c.tfm)
Provides:       tex(fvmro8c.vf)
Provides:       tex(fvmro8r.tfm)
Provides:       tex(fvmro8t.tfm)
Provides:       tex(fvmro8t.vf)
Provides:       tex(fvsb8a.tfm)
Provides:       tex(fvsb8c.tfm)
Provides:       tex(fvsb8c.vf)
Provides:       tex(fvsb8r.tfm)
Provides:       tex(fvsb8t.tfm)
Provides:       tex(fvsb8t.vf)
Provides:       tex(fvsbo8a.tfm)
Provides:       tex(fvsbo8c.tfm)
Provides:       tex(fvsbo8c.vf)
Provides:       tex(fvsbo8r.tfm)
Provides:       tex(fvsbo8t.tfm)
Provides:       tex(fvsbo8t.vf)
Provides:       tex(fvsr8a.tfm)
Provides:       tex(fvsr8c.tfm)
Provides:       tex(fvsr8c.vf)
Provides:       tex(fvsr8r.tfm)
Provides:       tex(fvsr8t.tfm)
Provides:       tex(fvsr8t.vf)
Provides:       tex(fvsro8a.tfm)
Provides:       tex(fvsro8c.tfm)
Provides:       tex(fvsro8c.vf)
Provides:       tex(fvsro8r.tfm)
Provides:       tex(fvsro8t.tfm)
Provides:       tex(fvsro8t.vf)
Provides:       tex(t1fve.fd)
Provides:       tex(t1fvm.fd)
Provides:       tex(t1fvs.fd)
Provides:       tex(ts1fve.fd)
Provides:       tex(ts1fvm.fd)
Provides:       tex(ts1fvs.fd)
Requires:       tex(fontenc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(textcomp.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source109:      bera.tar.xz
Source110:      bera.doc.tar.xz

%description -n texlive-bera
The package contains the Bera Type 1 fonts, and a zip archive
containing files to use the fonts with LaTeX. Bera is a set of
three font families: Bera Serif (a slab-serif Roman), Bera Sans
(a Frutiger descendant), and Bera Mono (monospaced/typewriter).
Support for use in LaTeX is also provided. The Bera family is a
repackaging, for use with TeX, of the Bitstream Vera family.

%package -n texlive-bera-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20031
Release:        0
Summary:        Documentation for texlive-bera
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bera and texlive-alldocumentation)

%description -n texlive-bera-doc
This package includes the documentation for texlive-bera

%package -n texlive-bera-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn20031
Release:        0
Summary:        Severed fonts for texlive-bera
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

%description -n texlive-bera-fonts
The  separated fonts package for texlive-bera

%post -n texlive-bera
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap bera.map' >> /var/run/texlive/run-updmap

%postun -n texlive-bera
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap bera.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-bera
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-bera-fonts

%files -n texlive-bera-doc
%{_texmfdistdir}/doc/fonts/bera/LICENSE
%{_texmfdistdir}/doc/fonts/bera/README
%{_texmfdistdir}/doc/fonts/bera/bera.pdf
%{_texmfdistdir}/doc/fonts/bera/bera.txt

%files -n texlive-bera
%{_texmfdistdir}/fonts/afm/public/bera/fveb8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fver8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmb8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmbo8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmr8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmro8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsb8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsbo8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsr8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsro8a.afm
%{_texmfdistdir}/fonts/map/dvips/bera/bera.map
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvebo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvebo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvebo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvero8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvero8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvero8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8t.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fveb8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fver8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvmb8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvmbo8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvmr8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvmro8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvsb8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvsbo8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvsr8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bera/fvsro8a.pfb
%{_texmfdistdir}/fonts/vf/public/bera/fveb8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fveb8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvebo8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvebo8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fver8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fver8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvero8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvero8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmb8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmb8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmbo8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmbo8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmr8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmr8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmro8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmro8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsb8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsb8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsbo8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsbo8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsr8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsr8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsro8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsro8t.vf
%{_texmfdistdir}/tex/latex/bera/bera.sty
%{_texmfdistdir}/tex/latex/bera/beramono.sty
%{_texmfdistdir}/tex/latex/bera/berasans.sty
%{_texmfdistdir}/tex/latex/bera/beraserif.sty
%{_texmfdistdir}/tex/latex/bera/t1fve.fd
%{_texmfdistdir}/tex/latex/bera/t1fvm.fd
%{_texmfdistdir}/tex/latex/bera/t1fvs.fd
%{_texmfdistdir}/tex/latex/bera/ts1fve.fd
%{_texmfdistdir}/tex/latex/bera/ts1fvm.fd
%{_texmfdistdir}/tex/latex/bera/ts1fvs.fd

%files -n texlive-bera-fonts
%dir %{_datadir}/fonts/texlive-bera
%{_datadir}/fontconfig/conf.avail/58-texlive-bera.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bera/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bera/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bera/fonts.scale
%{_datadir}/fonts/texlive-bera/fveb8a.pfb
%{_datadir}/fonts/texlive-bera/fver8a.pfb
%{_datadir}/fonts/texlive-bera/fvmb8a.pfb
%{_datadir}/fonts/texlive-bera/fvmbo8a.pfb
%{_datadir}/fonts/texlive-bera/fvmr8a.pfb
%{_datadir}/fonts/texlive-bera/fvmro8a.pfb
%{_datadir}/fonts/texlive-bera/fvsb8a.pfb
%{_datadir}/fonts/texlive-bera/fvsbo8a.pfb
%{_datadir}/fonts/texlive-bera/fvsr8a.pfb
%{_datadir}/fonts/texlive-bera/fvsro8a.pfb

%package -n texlive-berenisadf
Version:        %{texlive_version}.%{texlive_noarch}.1.004svn32215
Release:        0
License:        LPPL-1.0
Summary:        Berenis ADF fonts and TeX/LaTeX support
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Requires:       texlive-berenisadf-fonts >= %{texlive_version}
Suggests:       texlive-berenisadf-doc >= %{texlive_version}
Provides:       tex(berenis.sty)
Provides:       tex(ly1ybd.fd)
Provides:       tex(ly1ybd0.fd)
Provides:       tex(ly1ybd1.fd)
Provides:       tex(ly1ybd2.fd)
Provides:       tex(ly1ybd2j.fd)
Provides:       tex(ly1ybd2jw.fd)
Provides:       tex(ly1ybd2w.fd)
Provides:       tex(ly1ybdj.fd)
Provides:       tex(ly1ybdjw.fd)
Provides:       tex(ly1ybdw.fd)
Provides:       tex(t1-ybd.enc)
Provides:       tex(t1-ybd0.enc)
Provides:       tex(t1-ybd1.enc)
Provides:       tex(t1-ybd2.enc)
Provides:       tex(t1-ybd2j.enc)
Provides:       tex(t1-ybdj.enc)
Provides:       tex(t1ybd.fd)
Provides:       tex(t1ybd0.fd)
Provides:       tex(t1ybd1.fd)
Provides:       tex(t1ybd2.fd)
Provides:       tex(t1ybd2j.fd)
Provides:       tex(t1ybdj.fd)
Provides:       tex(texnansi-ybd.enc)
Provides:       tex(texnansi-ybd0.enc)
Provides:       tex(texnansi-ybd1.enc)
Provides:       tex(texnansi-ybd2.enc)
Provides:       tex(texnansi-ybd2j.enc)
Provides:       tex(texnansi-ybdj.enc)
Provides:       tex(texnansx-ybd2jw.enc)
Provides:       tex(texnansx-ybd2w.enc)
Provides:       tex(texnansx-ybdjw.enc)
Provides:       tex(texnansx-ybdw.enc)
Provides:       tex(ts1-ybd.enc)
Provides:       tex(ts1-ybd0.enc)
Provides:       tex(ts1-ybd1.enc)
Provides:       tex(ts1-ybd2.enc)
Provides:       tex(ts1-ybd2j.enc)
Provides:       tex(ts1-ybdj.enc)
Provides:       tex(ts1ybd.fd)
Provides:       tex(ts1ybd0.fd)
Provides:       tex(ts1ybd1.fd)
Provides:       tex(ts1ybd2.fd)
Provides:       tex(ts1ybd2j.fd)
Provides:       tex(ts1ybdj.fd)
Provides:       tex(ybd.map)
Provides:       tex(ybdb08c.tfm)
Provides:       tex(ybdb08t.tfm)
Provides:       tex(ybdb08y.tfm)
Provides:       tex(ybdb0c8c.tfm)
Provides:       tex(ybdb0c8t.tfm)
Provides:       tex(ybdb0c8y.tfm)
Provides:       tex(ybdb0ci8c.tfm)
Provides:       tex(ybdb0ci8t.tfm)
Provides:       tex(ybdb0ci8y.tfm)
Provides:       tex(ybdb0i8c.tfm)
Provides:       tex(ybdb0i8t.tfm)
Provides:       tex(ybdb0i8y.tfm)
Provides:       tex(ybdb18c.tfm)
Provides:       tex(ybdb18t.tfm)
Provides:       tex(ybdb18y.tfm)
Provides:       tex(ybdb1c8c.tfm)
Provides:       tex(ybdb1c8t.tfm)
Provides:       tex(ybdb1c8y.tfm)
Provides:       tex(ybdb1ci8c.tfm)
Provides:       tex(ybdb1ci8t.tfm)
Provides:       tex(ybdb1ci8y.tfm)
Provides:       tex(ybdb1i8c.tfm)
Provides:       tex(ybdb1i8t.tfm)
Provides:       tex(ybdb1i8y.tfm)
Provides:       tex(ybdb28c.tfm)
Provides:       tex(ybdb28t.tfm)
Provides:       tex(ybdb28y.tfm)
Provides:       tex(ybdb2c8c.tfm)
Provides:       tex(ybdb2c8t.tfm)
Provides:       tex(ybdb2c8y.tfm)
Provides:       tex(ybdb2ci8c.tfm)
Provides:       tex(ybdb2ci8t.tfm)
Provides:       tex(ybdb2ci8y.tfm)
Provides:       tex(ybdb2cij8c.tfm)
Provides:       tex(ybdb2cij8t.tfm)
Provides:       tex(ybdb2cij8y.tfm)
Provides:       tex(ybdb2cijw8y.tfm)
Provides:       tex(ybdb2ciw8y.tfm)
Provides:       tex(ybdb2cj8c.tfm)
Provides:       tex(ybdb2cj8t.tfm)
Provides:       tex(ybdb2cj8y.tfm)
Provides:       tex(ybdb2cjw8y.tfm)
Provides:       tex(ybdb2cw8y.tfm)
Provides:       tex(ybdb2i8c.tfm)
Provides:       tex(ybdb2i8t.tfm)
Provides:       tex(ybdb2i8y.tfm)
Provides:       tex(ybdb2ij8c.tfm)
Provides:       tex(ybdb2ij8t.tfm)
Provides:       tex(ybdb2ij8y.tfm)
Provides:       tex(ybdb2ijw8y.tfm)
Provides:       tex(ybdb2iw8y.tfm)
Provides:       tex(ybdb2j8c.tfm)
Provides:       tex(ybdb2j8t.tfm)
Provides:       tex(ybdb2j8y.tfm)
Provides:       tex(ybdb2jw8y.tfm)
Provides:       tex(ybdb2w8y.tfm)
Provides:       tex(ybdb8c.tfm)
Provides:       tex(ybdb8t.tfm)
Provides:       tex(ybdb8y.tfm)
Provides:       tex(ybdbc8c.tfm)
Provides:       tex(ybdbc8t.tfm)
Provides:       tex(ybdbc8y.tfm)
Provides:       tex(ybdbci8c.tfm)
Provides:       tex(ybdbci8t.tfm)
Provides:       tex(ybdbci8y.tfm)
Provides:       tex(ybdbcij8c.tfm)
Provides:       tex(ybdbcij8t.tfm)
Provides:       tex(ybdbcij8y.tfm)
Provides:       tex(ybdbcijw8y.tfm)
Provides:       tex(ybdbciw8y.tfm)
Provides:       tex(ybdbcj8c.tfm)
Provides:       tex(ybdbcj8t.tfm)
Provides:       tex(ybdbcj8y.tfm)
Provides:       tex(ybdbcjw8y.tfm)
Provides:       tex(ybdbcw8y.tfm)
Provides:       tex(ybdbi8c.tfm)
Provides:       tex(ybdbi8t.tfm)
Provides:       tex(ybdbi8y.tfm)
Provides:       tex(ybdbij8c.tfm)
Provides:       tex(ybdbij8t.tfm)
Provides:       tex(ybdbij8y.tfm)
Provides:       tex(ybdbijw8y.tfm)
Provides:       tex(ybdbiw8y.tfm)
Provides:       tex(ybdbj8c.tfm)
Provides:       tex(ybdbj8t.tfm)
Provides:       tex(ybdbj8y.tfm)
Provides:       tex(ybdbjw8y.tfm)
Provides:       tex(ybdbw8y.tfm)
Provides:       tex(ybdr08c.tfm)
Provides:       tex(ybdr08t.tfm)
Provides:       tex(ybdr08y.tfm)
Provides:       tex(ybdr0c8c.tfm)
Provides:       tex(ybdr0c8t.tfm)
Provides:       tex(ybdr0c8y.tfm)
Provides:       tex(ybdr0ci8c.tfm)
Provides:       tex(ybdr0ci8t.tfm)
Provides:       tex(ybdr0ci8y.tfm)
Provides:       tex(ybdr0i8c.tfm)
Provides:       tex(ybdr0i8t.tfm)
Provides:       tex(ybdr0i8y.tfm)
Provides:       tex(ybdr18c.tfm)
Provides:       tex(ybdr18t.tfm)
Provides:       tex(ybdr18y.tfm)
Provides:       tex(ybdr1c8c.tfm)
Provides:       tex(ybdr1c8t.tfm)
Provides:       tex(ybdr1c8y.tfm)
Provides:       tex(ybdr1ci8c.tfm)
Provides:       tex(ybdr1ci8t.tfm)
Provides:       tex(ybdr1ci8y.tfm)
Provides:       tex(ybdr1i8c.tfm)
Provides:       tex(ybdr1i8t.tfm)
Provides:       tex(ybdr1i8y.tfm)
Provides:       tex(ybdr28c.tfm)
Provides:       tex(ybdr28t.tfm)
Provides:       tex(ybdr28y.tfm)
Provides:       tex(ybdr2c8c.tfm)
Provides:       tex(ybdr2c8t.tfm)
Provides:       tex(ybdr2c8y.tfm)
Provides:       tex(ybdr2ci8c.tfm)
Provides:       tex(ybdr2ci8t.tfm)
Provides:       tex(ybdr2ci8y.tfm)
Provides:       tex(ybdr2cij8c.tfm)
Provides:       tex(ybdr2cij8t.tfm)
Provides:       tex(ybdr2cij8y.tfm)
Provides:       tex(ybdr2cijw8y.tfm)
Provides:       tex(ybdr2ciw8y.tfm)
Provides:       tex(ybdr2cj8c.tfm)
Provides:       tex(ybdr2cj8t.tfm)
Provides:       tex(ybdr2cj8y.tfm)
Provides:       tex(ybdr2cjw8y.tfm)
Provides:       tex(ybdr2cw8y.tfm)
Provides:       tex(ybdr2i8c.tfm)
Provides:       tex(ybdr2i8t.tfm)
Provides:       tex(ybdr2i8y.tfm)
Provides:       tex(ybdr2ij8c.tfm)
Provides:       tex(ybdr2ij8t.tfm)
Provides:       tex(ybdr2ij8y.tfm)
Provides:       tex(ybdr2ijw8y.tfm)
Provides:       tex(ybdr2iw8y.tfm)
Provides:       tex(ybdr2j8c.tfm)
Provides:       tex(ybdr2j8t.tfm)
Provides:       tex(ybdr2j8y.tfm)
Provides:       tex(ybdr2jw8y.tfm)
Provides:       tex(ybdr2w8y.tfm)
Provides:       tex(ybdr8c.tfm)
Provides:       tex(ybdr8t.tfm)
Provides:       tex(ybdr8y.tfm)
Provides:       tex(ybdrc8c.tfm)
Provides:       tex(ybdrc8t.tfm)
Provides:       tex(ybdrc8y.tfm)
Provides:       tex(ybdrci8c.tfm)
Provides:       tex(ybdrci8t.tfm)
Provides:       tex(ybdrci8y.tfm)
Provides:       tex(ybdrcij8c.tfm)
Provides:       tex(ybdrcij8t.tfm)
Provides:       tex(ybdrcij8y.tfm)
Provides:       tex(ybdrcijw8y.tfm)
Provides:       tex(ybdrciw8y.tfm)
Provides:       tex(ybdrcj8c.tfm)
Provides:       tex(ybdrcj8t.tfm)
Provides:       tex(ybdrcj8y.tfm)
Provides:       tex(ybdrcjw8y.tfm)
Provides:       tex(ybdrcw8y.tfm)
Provides:       tex(ybdri8c.tfm)
Provides:       tex(ybdri8t.tfm)
Provides:       tex(ybdri8y.tfm)
Provides:       tex(ybdrij8c.tfm)
Provides:       tex(ybdrij8t.tfm)
Provides:       tex(ybdrij8y.tfm)
Provides:       tex(ybdrijw8y.tfm)
Provides:       tex(ybdriw8y.tfm)
Provides:       tex(ybdrj8c.tfm)
Provides:       tex(ybdrj8t.tfm)
Provides:       tex(ybdrj8y.tfm)
Provides:       tex(ybdrjw8y.tfm)
Provides:       tex(ybdrw8y.tfm)
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source111:      berenisadf.tar.xz
Source112:      berenisadf.doc.tar.xz

%description -n texlive-berenisadf
The bundle provides the BerenisADF Pro font collection, in
OpenType and PostScript Type 1 formats, together with support
files to use the fonts in TeXnANSI (LY1) and LaTeX standard T1
and TS1 encodings.

%package -n texlive-berenisadf-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.004svn32215
Release:        0
Summary:        Documentation for texlive-berenisadf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-berenisadf and texlive-alldocumentation)

%description -n texlive-berenisadf-doc
This package includes the documentation for texlive-berenisadf

%package -n texlive-berenisadf-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.004svn32215
Release:        0
Summary:        Severed fonts for texlive-berenisadf
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

%description -n texlive-berenisadf-fonts
The  separated fonts package for texlive-berenisadf

%post -n texlive-berenisadf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap ybd.map' >> /var/run/texlive/run-updmap

%postun -n texlive-berenisadf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap ybd.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-berenisadf
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-berenisadf-fonts

%files -n texlive-berenisadf-doc
%{_texmfdistdir}/doc/fonts/berenisadf/COPYING
%{_texmfdistdir}/doc/fonts/berenisadf/COPYING.unix
%{_texmfdistdir}/doc/fonts/berenisadf/Makefile.source
%{_texmfdistdir}/doc/fonts/berenisadf/NOTICE.txt
%{_texmfdistdir}/doc/fonts/berenisadf/README.doc
%{_texmfdistdir}/doc/fonts/berenisadf/berenisadf.pdf
%{_texmfdistdir}/doc/fonts/berenisadf/berenisadf.tex
%{_texmfdistdir}/doc/fonts/berenisadf/cfr.gwneud.cyhoeddus
%{_texmfdistdir}/doc/fonts/berenisadf/ff-ybd.pe
%{_texmfdistdir}/doc/fonts/berenisadf/manifest.txt
%{_texmfdistdir}/doc/fonts/berenisadf/ybd-8t.lig
%{_texmfdistdir}/doc/fonts/berenisadf/ybd-8y.lig
%{_texmfdistdir}/doc/fonts/berenisadf/ybd.nam

%files -n texlive-berenisadf
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdb.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdbc.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdbci.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdbi.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdr.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdrc.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdrci.afm
%{_texmfdistdir}/fonts/afm/arkandis/berenisadf/ybdri.afm
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd0.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd1.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd2.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybd2j.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/t1-ybdj.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd0.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd1.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd2.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybd2j.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansi-ybdj.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybd2jw.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybd2w.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybdjw.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/texnansx-ybdw.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd0.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd1.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd2.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybd2j.enc
%{_texmfdistdir}/fonts/enc/dvips/berenisadf/ts1-ybdj.enc
%{_texmfdistdir}/fonts/map/dvips/berenisadf/ybd.map
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFPro-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/BerenisADFProSC-Regular.otf
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb08y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb0i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb18y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb1i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb28c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb28t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb28y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2cw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2ijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2iw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2j8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2j8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2j8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2jw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb2w8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdb8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbc8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbc8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbcw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbi8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbi8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbi8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbiw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdbw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr08c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr08t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr08y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr0i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr18c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr18t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr18y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr1i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr28c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr28t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr28y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2c8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2c8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2c8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2cw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2i8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2i8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2i8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2ijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2iw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2j8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2j8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2j8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2jw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr2w8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdr8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrc8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrc8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrci8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrci8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrci8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrciw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrcw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdri8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdri8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdri8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrij8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrij8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrij8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrijw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdriw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrj8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrj8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrj8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrjw8y.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/berenisadf/ybdrw8y.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdbc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdbci.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdbi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdr.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdrc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdrci.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/berenisadf/ybdri.pfb
%{_texmfdistdir}/tex/latex/berenisadf/berenis.sty
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd0.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd1.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2j.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2jw.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybd2w.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybdj.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybdjw.fd
%{_texmfdistdir}/tex/latex/berenisadf/ly1ybdw.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd0.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd1.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd2.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybd2j.fd
%{_texmfdistdir}/tex/latex/berenisadf/t1ybdj.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd0.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd1.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd2.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybd2j.fd
%{_texmfdistdir}/tex/latex/berenisadf/ts1ybdj.fd

%files -n texlive-berenisadf-fonts
%dir %{_datadir}/fonts/texlive-berenisadf
%{_datadir}/fontconfig/conf.avail/58-texlive-berenisadf.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-berenisadf.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-berenisadf.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-berenisadf/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-berenisadf/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-berenisadf/fonts.scale
%{_datadir}/fonts/texlive-berenisadf/BerenisADFPro-Bold.otf
%{_datadir}/fonts/texlive-berenisadf/BerenisADFPro-BoldItalic.otf
%{_datadir}/fonts/texlive-berenisadf/BerenisADFPro-Italic.otf
%{_datadir}/fonts/texlive-berenisadf/BerenisADFPro-Regular.otf
%{_datadir}/fonts/texlive-berenisadf/BerenisADFProSC-Bold.otf
%{_datadir}/fonts/texlive-berenisadf/BerenisADFProSC-BoldItalic.otf
%{_datadir}/fonts/texlive-berenisadf/BerenisADFProSC-Italic.otf
%{_datadir}/fonts/texlive-berenisadf/BerenisADFProSC-Regular.otf
%{_datadir}/fonts/texlive-berenisadf/ybdb.pfb
%{_datadir}/fonts/texlive-berenisadf/ybdbc.pfb
%{_datadir}/fonts/texlive-berenisadf/ybdbci.pfb
%{_datadir}/fonts/texlive-berenisadf/ybdbi.pfb
%{_datadir}/fonts/texlive-berenisadf/ybdr.pfb
%{_datadir}/fonts/texlive-berenisadf/ybdrc.pfb
%{_datadir}/fonts/texlive-berenisadf/ybdrci.pfb
%{_datadir}/fonts/texlive-berenisadf/ybdri.pfb

%package -n texlive-besjournals
Version:        %{texlive_version}.%{texlive_noarch}.svn45662
Release:        0
License:        LPPL-1.0
Summary:        Bibliographies suitable for British Ecological Society journals
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-besjournals-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source113:      besjournals.tar.xz
Source114:      besjournals.doc.tar.xz

%description -n texlive-besjournals
The package provides a BibTeX style for use with journals
published by the British Ecological Society. The style was
produced independently of the Society, and has no formal
approval by the BES.

%package -n texlive-besjournals-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn45662
Release:        0
Summary:        Documentation for texlive-besjournals
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-besjournals and texlive-alldocumentation)

%description -n texlive-besjournals-doc
This package includes the documentation for texlive-besjournals

%post -n texlive-besjournals
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-besjournals
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-besjournals
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-besjournals-doc
%{_texmfdistdir}/doc/bibtex/besjournals/README
%{_texmfdistdir}/doc/bibtex/besjournals/besjournals.dbj

%files -n texlive-besjournals
%{_texmfdistdir}/bibtex/bst/besjournals/besjournals.bst

%package -n texlive-bestpapers
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn38708
Release:        0
License:        SUSE-Public-Domain
Summary:        A BibTeX package to produce lists of authors' best papers
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bestpapers-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source115:      bestpapers.tar.xz
Source116:      bestpapers.doc.tar.xz

%description -n texlive-bestpapers
Many people preparing their resumes find the requirement
"please list five (or six, or ten) papers authored by you". The
same requirement is often stated for reports prepared by
professional teams. The creation of such lists may be a
cumbersome task. Even more difficult is it to support such
lists over the time, when new papers are added. The BibTeX
style bestpapers.bst is intended to facilitate this task. It is
based on the idea that it is easier to score than to sort: We
can assign a score to a paper and then let the computer select
the papers with highest scores. This work was commissioned by
the Consumer Financial Protection Bureau, United States
Treasury. This package is in the public domain.

%package -n texlive-bestpapers-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn38708
Release:        0
Summary:        Documentation for texlive-bestpapers
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bestpapers and texlive-alldocumentation)

%description -n texlive-bestpapers-doc
This package includes the documentation for texlive-bestpapers

%post -n texlive-bestpapers
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bestpapers
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bestpapers
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bestpapers-doc
%{_texmfdistdir}/doc/bibtex/bestpapers/Makefile
%{_texmfdistdir}/doc/bibtex/bestpapers/README
%{_texmfdistdir}/doc/bibtex/bestpapers/bestpapers-guide.pdf
%{_texmfdistdir}/doc/bibtex/bestpapers/bestpapers-guide.tex
%{_texmfdistdir}/doc/bibtex/bestpapers/tex.bib
%{_texmfdistdir}/doc/bibtex/bestpapers/typography.bib

%files -n texlive-bestpapers
%{_texmfdistdir}/bibtex/bst/bestpapers/bestpapers-export.bst
%{_texmfdistdir}/bibtex/bst/bestpapers/bestpapers.bst

%package -n texlive-betababel
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn15878
Release:        0
License:        LPPL-1.0
Summary:        Insert ancient greek text coded in Beta Code
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-betababel-doc >= %{texlive_version}
Provides:       tex(betababel.sty)
Requires:       tex(babel.sty)
Requires:       tex(teubner.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source117:      betababel.tar.xz
Source118:      betababel.doc.tar.xz

%description -n texlive-betababel
The betababel package extends the babel polutonikogreek option
to provide a simple way to insert ancient Greek texts with
diacritical characters into your document using the commonly
used Beta Code transliteration. You can directly insert Beta
Code texts -- as they can be found at the Perseus project, for
example -- without modification.

%package -n texlive-betababel-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn15878
Release:        0
Summary:        Documentation for texlive-betababel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-betababel and texlive-alldocumentation)

%description -n texlive-betababel-doc
This package includes the documentation for texlive-betababel

%post -n texlive-betababel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-betababel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-betababel
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-betababel-doc
%{_texmfdistdir}/doc/latex/betababel/betatest.pdf
%{_texmfdistdir}/doc/latex/betababel/betatest.tex

%files -n texlive-betababel
%{_texmfdistdir}/tex/latex/betababel/betababel.sty

%package -n texlive-beton
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Use Concrete fonts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-beton-doc >= %{texlive_version}
Provides:       tex(beton.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source119:      beton.tar.xz
Source120:      beton.doc.tar.xz

%description -n texlive-beton
Typeset a LaTeX2e document with the Concrete fonts designed by
Don Knuth and used in his book "Concrete Mathematics".

%package -n texlive-beton-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-beton
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beton and texlive-alldocumentation)

%description -n texlive-beton-doc
This package includes the documentation for texlive-beton

%post -n texlive-beton
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-beton
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-beton
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-beton-doc
%{_texmfdistdir}/doc/latex/beton/beton.pdf
%{_texmfdistdir}/doc/latex/beton/legal.txt

%files -n texlive-beton
%{_texmfdistdir}/tex/latex/beton/beton.sty

%package -n texlive-beuron
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn46374
Release:        0
License:        LPPL-1.0
Summary:        The script of the Beuronese art school
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Requires:       texlive-beuron-fonts >= %{texlive_version}
Suggests:       texlive-beuron-doc >= %{texlive_version}
Provides:       tex(beuron.map)
Provides:       tex(beuron.sty)
Provides:       tex(beuron.tfm)
Provides:       tex(beuronc.tfm)
Provides:       tex(beuronx.tfm)
Provides:       tex(t1beuron.fd)
Requires:       tex(expl3.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source121:      beuron.tar.xz
Source122:      beuron.doc.tar.xz

%description -n texlive-beuron
This package provides the script used in the works of the
Beuron art school for use with TeX and LaTeX. It is a
monumental script consisting of capital letters only. The fonts
are provided as Metafont sources, in the Type1 and in the
OpenType format. The package includes suitable font selection
commands for use with LaTeX.

%package -n texlive-beuron-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn46374
Release:        0
Summary:        Documentation for texlive-beuron
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-beuron and texlive-alldocumentation)
Provides:       locale(texlive-beuron-doc:de;en)

%description -n texlive-beuron-doc
This package includes the documentation for texlive-beuron

%package -n texlive-beuron-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn46374
Release:        0
Summary:        Severed fonts for texlive-beuron
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

%description -n texlive-beuron-fonts
The  separated fonts package for texlive-beuron

%post -n texlive-beuron
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap beuron.map' >> /var/run/texlive/run-updmap

%postun -n texlive-beuron
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap beuron.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-beuron
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-beuron-fonts

%files -n texlive-beuron-doc
%{_texmfdistdir}/doc/fonts/beuron/Literatur.bib
%{_texmfdistdir}/doc/fonts/beuron/README
%{_texmfdistdir}/doc/fonts/beuron/beuron-de.pdf
%{_texmfdistdir}/doc/fonts/beuron/beuron-de.tex
%{_texmfdistdir}/doc/fonts/beuron/beuron-en.pdf
%{_texmfdistdir}/doc/fonts/beuron/beuron-en.tex

%files -n texlive-beuron
%{_texmfdistdir}/fonts/map/dvips/beuron/beuron.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/beuron/Beuron-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/beuron/BeuronCondensed-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/beuron/BeuronExtended-Regular.otf
%{_texmfdistdir}/fonts/source/public/beuron/beuron.mf
%{_texmfdistdir}/fonts/source/public/beuron/beuronbuchst.mf
%{_texmfdistdir}/fonts/source/public/beuron/beuronc.mf
%{_texmfdistdir}/fonts/source/public/beuron/beuronkern.mf
%{_texmfdistdir}/fonts/source/public/beuron/beuronx.mf
%{_texmfdistdir}/fonts/tfm/public/beuron/beuron.tfm
%{_texmfdistdir}/fonts/tfm/public/beuron/beuronc.tfm
%{_texmfdistdir}/fonts/tfm/public/beuron/beuronx.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/beuron/beuron.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/beuron/beuronc.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/beuron/beuronx.pfb
%{_texmfdistdir}/tex/latex/beuron/beuron.sty
%{_texmfdistdir}/tex/latex/beuron/t1beuron.fd

%files -n texlive-beuron-fonts
%dir %{_datadir}/fonts/texlive-beuron
%{_datadir}/fontconfig/conf.avail/58-texlive-beuron.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-beuron.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-beuron.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-beuron/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-beuron/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-beuron/fonts.scale
%{_datadir}/fonts/texlive-beuron/Beuron-Regular.otf
%{_datadir}/fonts/texlive-beuron/BeuronCondensed-Regular.otf
%{_datadir}/fonts/texlive-beuron/BeuronExtended-Regular.otf
%{_datadir}/fonts/texlive-beuron/beuron.pfb
%{_datadir}/fonts/texlive-beuron/beuronc.pfb
%{_datadir}/fonts/texlive-beuron/beuronx.pfb

%package -n texlive-bewerbung
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn61632
Release:        0
License:        LPPL-1.0
Summary:        Typesetting job applications
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bewerbung-doc >= %{texlive_version}
Provides:       tex(argetabelle.cls)
Provides:       tex(bewerbung-cv-casual.sty)
Provides:       tex(bewerbung-cv-classic.sty)
Provides:       tex(bewerbung-cv-oldstyle.sty)
Provides:       tex(bewerbung-cv.sty)
Provides:       tex(bewerbung.cls)
Provides:       tex(bewerbung.sty)
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(comment.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(datatool.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(longtable.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source123:      bewerbung.tar.xz
Source124:      bewerbung.doc.tar.xz

%description -n texlive-bewerbung
The package provides packages and classes for typesetting
applications with titlepage, cover letter, cv and additional
documents in just a single document. There is also a class for
printing a table of the latest applications that can be shown
to the German authorities. The data for these applications can
be maintained in a simple CSV file.

%package -n texlive-bewerbung-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn61632
Release:        0
Summary:        Documentation for texlive-bewerbung
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bewerbung and texlive-alldocumentation)
Provides:       locale(texlive-bewerbung-doc:de;de,en)

%description -n texlive-bewerbung-doc
This package includes the documentation for texlive-bewerbung

%post -n texlive-bewerbung
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bewerbung
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bewerbung
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bewerbung-doc
%{_texmfdistdir}/doc/latex/bewerbung/Foto.pdf
%{_texmfdistdir}/doc/latex/bewerbung/README
%{_texmfdistdir}/doc/latex/bewerbung/README_DE
%{_texmfdistdir}/doc/latex/bewerbung/anschrift.csv
%{_texmfdistdir}/doc/latex/bewerbung/argetabelle-example.pdf
%{_texmfdistdir}/doc/latex/bewerbung/argetabelle-example.tex
%{_texmfdistdir}/doc/latex/bewerbung/bewerbung-example.pdf
%{_texmfdistdir}/doc/latex/bewerbung/bewerbung-example.tex
%{_texmfdistdir}/doc/latex/bewerbung/bewerbung.pdf
%{_texmfdistdir}/doc/latex/bewerbung/config.inc
%{_texmfdistdir}/doc/latex/bewerbung/neueBewerbung.sh
%{_texmfdistdir}/doc/latex/bewerbung/titlepage.inc

%files -n texlive-bewerbung
%{_texmfdistdir}/tex/latex/bewerbung/argetabelle.cls
%{_texmfdistdir}/tex/latex/bewerbung/bewerbung-cv-casual.sty
%{_texmfdistdir}/tex/latex/bewerbung/bewerbung-cv-classic.sty
%{_texmfdistdir}/tex/latex/bewerbung/bewerbung-cv-oldstyle.sty
%{_texmfdistdir}/tex/latex/bewerbung/bewerbung-cv.sty
%{_texmfdistdir}/tex/latex/bewerbung/bewerbung.cls
%{_texmfdistdir}/tex/latex/bewerbung/bewerbung.sty

%package -n texlive-bez123
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn15878
Release:        0
License:        LPPL-1.0
Summary:        Support for Bezier curves
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bez123-doc >= %{texlive_version}
Provides:       tex(bez123.sty)
Provides:       tex(multiply.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source125:      bez123.tar.xz
Source126:      bez123.doc.tar.xz

%description -n texlive-bez123
Provides additional facilities in a picture environment for
drawing linear, cubic, and rational quadratic Bezier curves
(standard LaTeX only offers non-rational quadratic splines).
Provides a package multiply that provides a command for
multiplication of a length without numerical overflow.

%package -n texlive-bez123-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn15878
Release:        0
Summary:        Documentation for texlive-bez123
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bez123 and texlive-alldocumentation)

%description -n texlive-bez123-doc
This package includes the documentation for texlive-bez123

%post -n texlive-bez123
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bez123
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bez123
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bez123-doc
%{_texmfdistdir}/doc/latex/bez123/README
%{_texmfdistdir}/doc/latex/bez123/bez123.pdf

%files -n texlive-bez123
%{_texmfdistdir}/tex/latex/bez123/bez123.sty
%{_texmfdistdir}/tex/latex/bez123/multiply.sty

%package -n texlive-bezierplot
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51398
Release:        0
License:        LPPL-1.0
Summary:        Approximate smooth function graphs with cubic bezier splines for use with TikZ or MetaPost
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bezierplot-doc >= %{texlive_version}
Provides:       tex(bezierplot.sty)
Requires:       tex(iftex.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source127:      bezierplot.tar.xz
Source128:      bezierplot.doc.tar.xz

%description -n texlive-bezierplot
This package consists of a Lua program as well as a (Lua)LaTeX
.sty file. Given a smooth function, bezierplot returns a smooth
bezier path written in TikZ notation (which also matches
MetaPost) that approximates the graph of the function. For
polynomial functions of degree [?] 3 and their inverses the
approximation is exact (up to numeric precision). bezierplot
also finds special points such as extreme points and inflection
points and reduces the number of used points.

%package -n texlive-bezierplot-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51398
Release:        0
Summary:        Documentation for texlive-bezierplot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bezierplot and texlive-alldocumentation)

%description -n texlive-bezierplot-doc
This package includes the documentation for texlive-bezierplot

%post -n texlive-bezierplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bezierplot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bezierplot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bezierplot-doc
%{_texmfdistdir}/doc/lualatex/bezierplot/README
%{_texmfdistdir}/doc/lualatex/bezierplot/bezierplot-doc.pdf
%{_texmfdistdir}/doc/lualatex/bezierplot/bezierplot-doc.tex

%files -n texlive-bezierplot
%{_texmfdistdir}/tex/lualatex/bezierplot/bezierplot.lua
%{_texmfdistdir}/tex/lualatex/bezierplot/bezierplot.sty

%package -n texlive-bfh-ci
Version:        %{texlive_version}.%{texlive_noarch}.2.2.0svn68828
Release:        0
License:        LPPL-1.0
Summary:        Corporate Design for Bern University of Applied Sciences
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-adjustbox >= %{texlive_version}
#!BuildIgnore: texlive-adjustbox
Requires:       texlive-amsfonts >= %{texlive_version}
#!BuildIgnore: texlive-amsfonts
Requires:       texlive-amsmath >= %{texlive_version}
#!BuildIgnore: texlive-amsmath
Requires:       texlive-anyfontsize >= %{texlive_version}
#!BuildIgnore: texlive-anyfontsize
Requires:       texlive-beamer >= %{texlive_version}
#!BuildIgnore: texlive-beamer
Requires:       texlive-fontawesome >= %{texlive_version}
#!BuildIgnore: texlive-fontawesome
Requires:       texlive-fontspec >= %{texlive_version}
#!BuildIgnore: texlive-fontspec
Requires:       texlive-geometry >= %{texlive_version}
#!BuildIgnore: texlive-geometry
Requires:       texlive-graphics >= %{texlive_version}
#!BuildIgnore: texlive-graphics
Requires:       texlive-handoutwithnotes >= %{texlive_version}
#!BuildIgnore: texlive-handoutwithnotes
Requires:       texlive-hyperref >= %{texlive_version}
#!BuildIgnore: texlive-hyperref
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires:       texlive-koma-script >= %{texlive_version}
#!BuildIgnore: texlive-koma-script
Requires:       texlive-l3kernel >= %{texlive_version}
#!BuildIgnore: texlive-l3kernel
Requires:       texlive-l3packages >= %{texlive_version}
#!BuildIgnore: texlive-l3packages
Requires:       texlive-listings >= %{texlive_version}
#!BuildIgnore: texlive-listings
Requires:       texlive-nunito >= %{texlive_version}
#!BuildIgnore: texlive-nunito
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires:       texlive-qrcode >= %{texlive_version}
#!BuildIgnore: texlive-qrcode
Requires:       texlive-sourceserifpro >= %{texlive_version}
#!BuildIgnore: texlive-sourceserifpro
Requires:       texlive-tcolorbox >= %{texlive_version}
#!BuildIgnore: texlive-tcolorbox
Requires:       texlive-tools >= %{texlive_version}
#!BuildIgnore: texlive-tools
Requires:       texlive-translations >= %{texlive_version}
#!BuildIgnore: texlive-translations
Requires:       texlive-url >= %{texlive_version}
#!BuildIgnore: texlive-url
Requires:       texlive-xcolor >= %{texlive_version}
#!BuildIgnore: texlive-xcolor
Requires:       texlive-zref >= %{texlive_version}
#!BuildIgnore: texlive-zref
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bfh-ci-doc >= %{texlive_version}
Provides:       tex(beamercolorthemeBFH.sty)
Provides:       tex(beamerfontthemeBFH.sty)
Provides:       tex(beamerinnerthemeBFH.sty)
Provides:       tex(beamerouterthemeBFH-sidebar.sty)
Provides:       tex(beamerouterthemeBFH.sty)
Provides:       tex(beamerthemeBFH.sty)
Provides:       tex(bfh-a0paper.clo)
Provides:       tex(bfh-a1paper.clo)
Provides:       tex(bfh-a2paper.clo)
Provides:       tex(bfh-a3paper.clo)
Provides:       tex(bfh-a4paper.clo)
Provides:       tex(bfh-a5paper.clo)
Provides:       tex(bfh-a6paper.clo)
Provides:       tex(bfh-beamerarticle.cfg)
Provides:       tex(bfh-factsheet.cfg)
Provides:       tex(bfh-layout-boxes.cfg)
Provides:       tex(bfh-layout-listings.cfg)
Provides:       tex(bfh-layout-rules.cfg)
Provides:       tex(bfh-layout-tabular.cfg)
Provides:       tex(bfh-layout-terminal.cfg)
Provides:       tex(bfh-projectproposal.cfg)
Provides:       tex(bfhbeamer.cls)
Provides:       tex(bfhcolors.sty)
Provides:       tex(bfhfonts.sty)
Provides:       tex(bfhlayout.sty)
Provides:       tex(bfhletter.sty)
Provides:       tex(bfhlettersize9.5pt.clo)
Provides:       tex(bfhmodule.sty)
Provides:       tex(bfhpub.cls)
Provides:       tex(bfhsciposter.cls)
Provides:       tex(bfhthesis.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(beamer.cls)
Requires:       tex(expl3.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(handoutWithNotes.sty)
Requires:       tex(iftex.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(nunito.sty)
Requires:       tex(qrcode.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(scrletter.sty)
Requires:       tex(sourceserifpro.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(translations.sty)
Requires:       tex(trimclip.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(zref.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source129:      bfh-ci.tar.xz
Source130:      bfh-ci.doc.tar.xz

%description -n texlive-bfh-ci
This bundle provides possibilities to use the Corporate Design
of Bern University of Applied Sciences (BFH) with LaTeX. To
this end it contains classes as well as some helper packages
and config files together with some demo files.

%package -n texlive-bfh-ci-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2.0svn68828
Release:        0
Summary:        Documentation for texlive-bfh-ci
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bfh-ci and texlive-alldocumentation)

%description -n texlive-bfh-ci-doc
This package includes the documentation for texlive-bfh-ci

%post -n texlive-bfh-ci
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bfh-ci
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bfh-ci
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bfh-ci-doc
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHBeamer-Sidebar.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHBeamer-Sidebar.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHBeamer.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHBeamer.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHFactsheet.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHFactsheet.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHFromaddress.lco
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHLetter.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHLetter.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHProjektProposal.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHProjektProposal.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHPub.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHPub.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHSciPoster.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHSciPoster.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHThesis.pdf
%{_texmfdistdir}/doc/latex/bfh-ci/DEMO-BFHThesis.tex
%{_texmfdistdir}/doc/latex/bfh-ci/DEPENDS.txt
%{_texmfdistdir}/doc/latex/bfh-ci/README.md
%{_texmfdistdir}/doc/latex/bfh-ci/bfhhkb-doc.cfg

%files -n texlive-bfh-ci
%{_texmfdistdir}/tex/latex/bfh-ci/beamercolorthemeBFH.sty
%{_texmfdistdir}/tex/latex/bfh-ci/beamerfontthemeBFH.sty
%{_texmfdistdir}/tex/latex/bfh-ci/beamerinnerthemeBFH.sty
%{_texmfdistdir}/tex/latex/bfh-ci/beamerouterthemeBFH-sidebar.sty
%{_texmfdistdir}/tex/latex/bfh-ci/beamerouterthemeBFH.sty
%{_texmfdistdir}/tex/latex/bfh-ci/beamerthemeBFH.sty
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-a0paper.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-a1paper.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-a2paper.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-a3paper.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-a4paper.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-a5paper.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-a6paper.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-beamerarticle.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-factsheet.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-layout-boxes.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-layout-listings.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-layout-rules.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-layout-tabular.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-layout-terminal.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfh-projectproposal.cfg
%{_texmfdistdir}/tex/latex/bfh-ci/bfhbeamer.cls
%{_texmfdistdir}/tex/latex/bfh-ci/bfhcolors.sty
%{_texmfdistdir}/tex/latex/bfh-ci/bfhfonts.sty
%{_texmfdistdir}/tex/latex/bfh-ci/bfhlayout.sty
%{_texmfdistdir}/tex/latex/bfh-ci/bfhletter.sty
%{_texmfdistdir}/tex/latex/bfh-ci/bfhlettersize9.5pt.clo
%{_texmfdistdir}/tex/latex/bfh-ci/bfhmodule.sty
%{_texmfdistdir}/tex/latex/bfh-ci/bfhpub.cls
%{_texmfdistdir}/tex/latex/bfh-ci/bfhsciposter.cls
%{_texmfdistdir}/tex/latex/bfh-ci/bfhthesis.cls
%{_texmfdistdir}/tex/latex/bfh-ci/bfhtranslations-english.trsl
%{_texmfdistdir}/tex/latex/bfh-ci/bfhtranslations-french.trsl
%{_texmfdistdir}/tex/latex/bfh-ci/bfhtranslations-german.trsl

%package -n texlive-bgteubner
Version:        %{texlive_version}.%{texlive_noarch}.2.11svn54080
Release:        0
License:        LPPL-1.0
Summary:        Class for producing books for the publisher "Teubner Verlag"
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bgteubner-doc >= %{texlive_version}
Provides:       tex(bgteubner.cls)
Provides:       tex(hhfixme.sty)
Provides:       tex(hhsubfigure.sty)
Provides:       tex(ptmxcomp.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(babelbib.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(color.sty)
Requires:       tex(courier.sty)
Requires:       tex(exscale.sty)
Requires:       tex(fixltx2e.sty)
Requires:       tex(fixmath.sty)
Requires:       tex(fnbreak.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(framed.sty)
Requires:       tex(ginpenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(hfoldsty.sty)
Requires:       tex(hhtensor.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(mathcomp.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(mdwlist.sty)
Requires:       tex(multicol.sty)
Requires:       tex(numprint.sty)
Requires:       tex(onlyamsmath.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pdfcprot.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(relsize.sty)
Requires:       tex(scrbook.cls)
Requires:       tex(setspace.sty)
Requires:       tex(slantsc.sty)
Requires:       tex(subfloat.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(warning.sty)
Requires:       tex(wasysym.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source131:      bgteubner.tar.xz
Source132:      bgteubner.doc.tar.xz

%description -n texlive-bgteubner
The bgteubner document class has been programmed by order of
the Teubner Verlag, Wiesbaden, Germany, to ensure that books of
this publisher have a unique layout. Unfortunately, most of the
documentation is only available in German. Since the document
class is intended to generate a unique layout, many things
(layout etc.) are fixed and cannot be altered by the user. If
you want to use the document class for another purpose than
publishing with the Teubner Verlag, this may arouse unwanted
restrictions (for instance, the document class provides only
two paper sizes: DIN A5 and 17cm x 24cm; only two font families
are supported: Times and European Computer Modern).

%package -n texlive-bgteubner-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.11svn54080
Release:        0
Summary:        Documentation for texlive-bgteubner
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bgteubner and texlive-alldocumentation)
Provides:       locale(texlive-bgteubner-doc:de)

%description -n texlive-bgteubner-doc
This package includes the documentation for texlive-bgteubner

%post -n texlive-bgteubner
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bgteubner
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bgteubner
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bgteubner-doc
%{_texmfdistdir}/doc/latex/bgteubner/01b.png
%{_texmfdistdir}/doc/latex/bgteubner/02b.png
%{_texmfdistdir}/doc/latex/bgteubner/ChangeLog
%{_texmfdistdir}/doc/latex/bgteubner/LIESMICH
%{_texmfdistdir}/doc/latex/bgteubner/Makefile.hhsubfigure
%{_texmfdistdir}/doc/latex/bgteubner/Makefile.source
%{_texmfdistdir}/doc/latex/bgteubner/Makefile.src
%{_texmfdistdir}/doc/latex/bgteubner/README
%{_texmfdistdir}/doc/latex/bgteubner/README.hhsubfigure
%{_texmfdistdir}/doc/latex/bgteubner/ToDo
%{_texmfdistdir}/doc/latex/bgteubner/anhang.tex
%{_texmfdistdir}/doc/latex/bgteubner/befehlsreferenz.tex
%{_texmfdistdir}/doc/latex/bgteubner/beispiel1.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-17x24-cm.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-17x24-mathtime.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-17x24-times.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-a5-cm.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-a5-mathtime.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-a5-times.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-cm.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner-with-hyperref.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bgteubner.tex
%{_texmfdistdir}/doc/latex/bgteubner/bgteucls.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bgteuversion.tex
%{_texmfdistdir}/doc/latex/bgteubner/bild4c.png
%{_texmfdistdir}/doc/latex/bgteubner/bild_ganz.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_ganz.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_ganz.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bild_mitte.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_mitte.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_mitte.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bild_oben.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_oben.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_oben.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bild_oben_unten.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_oben_unten.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_oben_unten.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bild_umflossen.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_umflossen.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_umflossen.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bild_unten.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_unten.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_unten.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang2.eps
%{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang2.fig
%{_texmfdistdir}/doc/latex/bgteubner/bild_zu_lang2.pdf
%{_texmfdistdir}/doc/latex/bgteubner/bilder.tex
%{_texmfdistdir}/doc/latex/bgteubner/cdcover.tex
%{_texmfdistdir}/doc/latex/bgteubner/checkliste.tex
%{_texmfdistdir}/doc/latex/bgteubner/einleitung.tex
%{_texmfdistdir}/doc/latex/bgteubner/formelzeichen.tex
%{_texmfdistdir}/doc/latex/bgteubner/getversion.tex
%{_texmfdistdir}/doc/latex/bgteubner/globales.tex
%{_texmfdistdir}/doc/latex/bgteubner/hyphenation.tex
%{_texmfdistdir}/doc/latex/bgteubner/index.tex
%{_texmfdistdir}/doc/latex/bgteubner/installation.tex
%{_texmfdistdir}/doc/latex/bgteubner/kapitel2.tex
%{_texmfdistdir}/doc/latex/bgteubner/literatur.bib
%{_texmfdistdir}/doc/latex/bgteubner/literatur.tex
%{_texmfdistdir}/doc/latex/bgteubner/manifest.txt
%{_texmfdistdir}/doc/latex/bgteubner/math-cm.pdf
%{_texmfdistdir}/doc/latex/bgteubner/math-cm.tex
%{_texmfdistdir}/doc/latex/bgteubner/math-mathtime.pdf
%{_texmfdistdir}/doc/latex/bgteubner/math-mathtime.tex
%{_texmfdistdir}/doc/latex/bgteubner/math.pdf
%{_texmfdistdir}/doc/latex/bgteubner/math.tex
%{_texmfdistdir}/doc/latex/bgteubner/optionen-advanced.tex
%{_texmfdistdir}/doc/latex/bgteubner/testquick.tex
%{_texmfdistdir}/doc/latex/bgteubner/testtimes.tex
%{_texmfdistdir}/doc/latex/bgteubner/tex_aufruf.tex
%{_texmfdistdir}/doc/latex/bgteubner/tex_bilder.tex
%{_texmfdistdir}/doc/latex/bgteubner/tex_globales.tex
%{_texmfdistdir}/doc/latex/bgteubner/tex_textelemente.tex
%{_texmfdistdir}/doc/latex/bgteubner/tex_typographie.tex
%{_texmfdistdir}/doc/latex/bgteubner/tex_verzeichnisse.tex
%{_texmfdistdir}/doc/latex/bgteubner/textelemente.tex
%{_texmfdistdir}/doc/latex/bgteubner/times-ja2.png
%{_texmfdistdir}/doc/latex/bgteubner/times-nein2.png
%{_texmfdistdir}/doc/latex/bgteubner/umbruch1.pdf
%{_texmfdistdir}/doc/latex/bgteubner/umbruch1.tex
%{_texmfdistdir}/doc/latex/bgteubner/umbruch1a.pdf
%{_texmfdistdir}/doc/latex/bgteubner/umbruch1a.tex
%{_texmfdistdir}/doc/latex/bgteubner/umbruch2.pdf
%{_texmfdistdir}/doc/latex/bgteubner/umbruch2.tex
%{_texmfdistdir}/doc/latex/bgteubner/umbruch2a.pdf
%{_texmfdistdir}/doc/latex/bgteubner/umbruch2a.tex
%{_texmfdistdir}/doc/latex/bgteubner/umbruch3.pdf
%{_texmfdistdir}/doc/latex/bgteubner/umbruch3.tex
%{_texmfdistdir}/doc/latex/bgteubner/umbruch3a.pdf
%{_texmfdistdir}/doc/latex/bgteubner/umbruch3a.tex
%{_texmfdistdir}/doc/latex/bgteubner/usefiles.txt
%{_texmfdistdir}/doc/latex/bgteubner/verzeichnisse.tex
%{_texmfdistdir}/doc/latex/bgteubner/vorwort.tex

%files -n texlive-bgteubner
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteuabbr.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteuabbr2.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteupln.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteupln2.bst
%{_texmfdistdir}/bibtex/bst/bgteubner/bgteupln3.bst
%{_texmfdistdir}/makeindex/bgteubner/bgteubner.ist
%{_texmfdistdir}/makeindex/bgteubner/bgteuglo.ist
%{_texmfdistdir}/makeindex/bgteubner/bgteuglochar.ist
%{_texmfdistdir}/tex/latex/bgteubner/bgteubner.cls
%{_texmfdistdir}/tex/latex/bgteubner/hhfixme.sty
%{_texmfdistdir}/tex/latex/bgteubner/hhsubfigure.sty
%{_texmfdistdir}/tex/latex/bgteubner/ptmxcomp.sty

%package -n texlive-bguq
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn27401
Release:        0
License:        LPPL-1.0
Summary:        Improved quantifier stroke for Begriffsschrift packages
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Requires:       texlive-bguq-fonts >= %{texlive_version}
Suggests:       texlive-bguq-doc >= %{texlive_version}
Provides:       tex(Ubguq04.fd)
Provides:       tex(Ubguq05.fd)
Provides:       tex(Ubguq06.fd)
Provides:       tex(Ubguq07.fd)
Provides:       tex(Ubguq08.fd)
Provides:       tex(Ubguq09.fd)
Provides:       tex(Ubguq10.fd)
Provides:       tex(Ubguq11.fd)
Provides:       tex(Ubguq12.fd)
Provides:       tex(begriff-bguq.sty)
Provides:       tex(bguq.cfg)
Provides:       tex(bguq.map)
Provides:       tex(bguq.sty)
Provides:       tex(bguq10t04.tfm)
Provides:       tex(bguq10t05.tfm)
Provides:       tex(bguq10t06.tfm)
Provides:       tex(bguq10t07.tfm)
Provides:       tex(bguq10t08.tfm)
Provides:       tex(bguq10t09.tfm)
Provides:       tex(bguq10t10.tfm)
Provides:       tex(bguq10t11.tfm)
Provides:       tex(bguq10t12.tfm)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source133:      bguq.tar.xz
Source134:      bguq.doc.tar.xz

%description -n texlive-bguq
The font contains a single character: the Begriffsschrift
quantifier (in several sizes), as used to set the
Begriffsschrift (concept notation) of Frege. The font is not
intended for end users; instead it is expected that it will be
used by other packages which implement the Begriffsschrift. An
(unofficial) modified version of Josh Parsons' begriff is
included as an example of implementation.

%package -n texlive-bguq-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn27401
Release:        0
Summary:        Documentation for texlive-bguq
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bguq and texlive-alldocumentation)

%description -n texlive-bguq-doc
This package includes the documentation for texlive-bguq

%package -n texlive-bguq-fonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn27401
Release:        0
Summary:        Severed fonts for texlive-bguq
License:        LPPL-1.0
URL:            https://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Suggests:       xorg-x11-fonts-core

%description -n texlive-bguq-fonts
The  separated fonts package for texlive-bguq

%post -n texlive-bguq
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap bguq.map' >> /var/run/texlive/run-updmap

%postun -n texlive-bguq
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap bguq.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-bguq
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-bguq-fonts

%files -n texlive-bguq-doc
%{_texmfdistdir}/doc/fonts/bguq/INSTALL.txt
%{_texmfdistdir}/doc/fonts/bguq/Makefile
%{_texmfdistdir}/doc/fonts/bguq/README
%{_texmfdistdir}/doc/fonts/bguq/bguq-doc.pdf

%files -n texlive-bguq
%{_texmfdistdir}/fonts/map/dvips/bguq/bguq.map
%{_texmfdistdir}/fonts/source/public/bguq/bguq.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t04.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t05.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t06.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t07.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t08.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t09.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t10.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t11.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t12.mf
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t04.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t05.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t06.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t07.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t08.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t09.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t10.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t11.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t12.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t04.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t05.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t06.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t07.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t08.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t09.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/bguq/bguq10t12.pfb
%{_texmfdistdir}/tex/latex/bguq/Ubguq04.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq05.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq06.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq07.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq08.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq09.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq10.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq11.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq12.fd
%{_texmfdistdir}/tex/latex/bguq/begriff-bguq.sty
%{_texmfdistdir}/tex/latex/bguq/bguq.cfg
%{_texmfdistdir}/tex/latex/bguq/bguq.sty

%files -n texlive-bguq-fonts
%dir %{_datadir}/fonts/texlive-bguq
%{_datadir}/fontconfig/conf.avail/58-texlive-bguq.conf
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bguq/encodings.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bguq/fonts.dir
%verify(not md5 size mtime) %{_datadir}/fonts/texlive-bguq/fonts.scale
%{_datadir}/fonts/texlive-bguq/bguq10t04.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t05.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t06.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t07.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t08.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t09.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t10.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t11.pfb
%{_datadir}/fonts/texlive-bguq/bguq10t12.pfb

%package -n texlive-bhcexam
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn64093
Release:        0
License:        LPPL-1.0
Summary:        An exam class for mathematics teachers in China
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bhcexam-doc >= %{texlive_version}
Provides:       tex(BHCexam.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(article.cls)
Requires:       tex(bbding.sty)
Requires:       tex(caption.sty)
Requires:       tex(ctex.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pifont.sty)
Requires:       tex(romannum.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source135:      bhcexam.tar.xz
Source136:      bhcexam.doc.tar.xz

%description -n texlive-bhcexam
This exam class is specially designed for mathematics teachers
in China. It is used by mathcrowd.cn (an opensource math exam
database) as the default class for exporting exam papers to
pdf. Using BHCexam you can separate the format and the content
very well; export both teacher paper and student paper; typeset
multiple choice questions with 3-6 options keeping adaptively
neat alignment; typeset cloze questions with a customizable
underline; typeset questions with subquestions in lists; group
questions in a list to control whether to show score, leave
spacing, initialize question number; and more (see BHCexam
Documentation).

%package -n texlive-bhcexam-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn64093
Release:        0
Summary:        Documentation for texlive-bhcexam
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bhcexam and texlive-alldocumentation)
Provides:       locale(texlive-bhcexam-doc:zh)

%description -n texlive-bhcexam-doc
This package includes the documentation for texlive-bhcexam

%post -n texlive-bhcexam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bhcexam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bhcexam
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bhcexam-doc
%{_texmfdistdir}/doc/xelatex/bhcexam/README-zh.md
%{_texmfdistdir}/doc/xelatex/bhcexam/README.md
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/To7VxKXpZaOWO5Qq9qzeZGtlwYTwJ5KF.jpg
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/example_student_paper.pdf
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/example_student_paper.tex
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/example_teacher_paper.pdf
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/example_teacher_paper.tex
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/logo.png
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/naive.pdf
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/naive.tex
%{_texmfdistdir}/doc/xelatex/bhcexam/examples/qrcode.png

%files -n texlive-bhcexam
%{_texmfdistdir}/tex/xelatex/bhcexam/BHCexam.cls

%package -n texlive-bib-fr
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
License:        LPPL-1.0
Summary:        French translation of classical BibTeX styles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bib-fr-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source137:      bib-fr.tar.xz
Source138:      bib-fr.doc.tar.xz

%description -n texlive-bib-fr
These files are French translations of the classical BibTeX
style files. The translations can easily be modified by simply
redefining FUNCTIONs named fr.*, at the beginning (lines
50-150) of each file.

%package -n texlive-bib-fr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Documentation for texlive-bib-fr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bib-fr and texlive-alldocumentation)

%description -n texlive-bib-fr-doc
This package includes the documentation for texlive-bib-fr

%post -n texlive-bib-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bib-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bib-fr
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bib-fr-doc
%{_texmfdistdir}/doc/bibtex/bib-fr/CHANGELOG
%{_texmfdistdir}/doc/bibtex/bib-fr/README

%files -n texlive-bib-fr
%{_texmfdistdir}/bibtex/bst/bib-fr/abbrv-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/abbrvnat-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/alpha-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/apalike-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/ieeetr-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/plain-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/plainnat-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/siam-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/unsrt-fr.bst
%{_texmfdistdir}/bibtex/bst/bib-fr/unsrtnat-fr.bst

%package -n texlive-bib2gls
Version:        %{texlive_version}.%{texlive_noarch}.3.9svn69635
Release:        0
License:        GPL-2.0-or-later
Summary:        Command line application to convert .bib files to glossaries-extra.sty resource files
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bib2gls-bin >= %{texlive_version}
#!BuildIgnore: texlive-bib2gls-bin
Requires:       texlive-glossaries-extra >= %{texlive_version}
#!BuildIgnore: texlive-glossaries-extra
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bib2gls-doc >= %{texlive_version}
Provides:       tex(bib2gls.jar)
Provides:       tex(convertgls2bib.jar)
Provides:       tex(texparserlib.jar)
Requires:       java
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source139:      bib2gls.tar.xz
Source140:      bib2gls.doc.tar.xz

%description -n texlive-bib2gls
This Java command line application may be used to extract
glossary information stored in a .bib file and convert it into
glossary entry definition commands. This application should be
used with glossaries-extra.sty's 'record' package option. It
performs two functions in one: selects entries according to
records found in the .aux file (similar to bibtex),
hierarchically sorts entries and collates location lists
(similar to makeindex or xindy). The glossary entries can then
be managed in a system such as JabRef, and only the entries
that are actually required will be defined, reducing the
resources required by TeX. The supplementary application
convertgls2bib can be used to convert existing .tex files
containing definitions (\newglossaryentry etc.) to the .bib
format required by bib2gls.

%package -n texlive-bib2gls-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.9svn69635
Release:        0
Summary:        Documentation for texlive-bib2gls
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bib2gls and texlive-alldocumentation)
Provides:       man(bib2gls.1)
Provides:       man(convertgls2bib.1)

%description -n texlive-bib2gls-doc
This package includes the documentation for texlive-bib2gls

%post -n texlive-bib2gls
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bib2gls
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bib2gls
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bib2gls-doc
%{_mandir}/man1/bib2gls.1*
%{_mandir}/man1/convertgls2bib.1*
%{_texmfdistdir}/doc/support/bib2gls/CHANGES
%{_texmfdistdir}/doc/support/bib2gls/DEPENDS.txt
%{_texmfdistdir}/doc/support/bib2gls/README.md
%{_texmfdistdir}/doc/support/bib2gls/bib2gls-begin.pdf
%{_texmfdistdir}/doc/support/bib2gls/bib2gls-extra-en.xml
%{_texmfdistdir}/doc/support/bib2gls/bib2gls-extra-nl.xml
%{_texmfdistdir}/doc/support/bib2gls/bib2gls.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/animals.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/bacteria.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/baseunits.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/bigmathsymbols.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/binaryoperators.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/books.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/chemicalformula.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/citations.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/constants.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/derivedunits.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/films.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/interpret-preamble.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/interpret-preamble2.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/markuplanguages.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/mathgreek.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/mathsobjects.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/mathsrelations.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/minerals.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/miscsymbols.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/no-interpret-preamble.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/people.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-authors.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-authors.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-bacteria.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-bacteria.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-chemical.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-chemical.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-citations.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-citations.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-constants.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-constants.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-hierarchical.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-hierarchical.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-markuplanguages.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-markuplanguages.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-maths.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-maths.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-media.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-media.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-msymbols.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-msymbols.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-multi1.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-multi1.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-multi2.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-multi2.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-nested.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-nested.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-people.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-people.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-textsymbols.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-textsymbols.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-textsymbols2.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-textsymbols2.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-units1.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-units1.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-units2.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-units2.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-units3.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-units3.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-usergroups.pdf
%{_texmfdistdir}/doc/support/bib2gls/examples/sample-usergroups.tex
%{_texmfdistdir}/doc/support/bib2gls/examples/terms.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/topics.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/unaryoperators.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/usergroups.bib
%{_texmfdistdir}/doc/support/bib2gls/examples/vegetables.bib

%files -n texlive-bib2gls
%{_texmfdistdir}/scripts/bib2gls/bib2gls.jar
%{_texmfdistdir}/scripts/bib2gls/bib2gls.sh
%{_texmfdistdir}/scripts/bib2gls/convertgls2bib.jar
%{_texmfdistdir}/scripts/bib2gls/convertgls2bib.sh
%{_texmfdistdir}/scripts/bib2gls/resources/bib2gls-en.xml
%{_texmfdistdir}/scripts/bib2gls/texparserlib.jar

%package -n texlive-bibarts
Version:        %{texlive_version}.%{texlive_noarch}.2.6svn67407
Release:        0
License:        GPL-2.0-or-later
Summary:        "Arts"-style bibliographical information
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibarts-doc >= %{texlive_version}
Provides:       tex(bibarts.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source141:      bibarts.tar.xz
Source142:      bibarts.doc.tar.xz

%description -n texlive-bibarts
BibArts is a LaTeX package to assist in making bibliographical
features common in the arts and the humanities (history,
political science, philosophy, etc.). bibarts.sty provides
commands for quotations, abbreviations, and especially for a
formatted citation of literature, journals (periodicals),
edited sources, and archive sources. In difference to earlier
versions, BibArts 2.x helps to use slanted fonts (italics) and
is able to set ibidem automatically in footnotes. It will also
copy all citation information, abbreviations, and register key
words into lists for an automatically generated appendix. These
lists may refer to page and footnote numbers. BibArts has
nothing to do with BibTeX. The lists are created by bibsort
(see below). BibArts requires the program bibsort, for which
the sources and a Windows executable are provided. This program
creates the bibliography without using MakeIndex or BibTeX. Its
source is not written with any specific operating system in
mind. A summary of contents is in English; the full
documentation is in German.

%package -n texlive-bibarts-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.6svn67407
Release:        0
Summary:        Documentation for texlive-bibarts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibarts and texlive-alldocumentation)
Provides:       locale(texlive-bibarts-doc:de)

%description -n texlive-bibarts-doc
This package includes the documentation for texlive-bibarts

%post -n texlive-bibarts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibarts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibarts
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibarts-doc
%{_texmfdistdir}/doc/latex/bibarts/COPYING
%{_texmfdistdir}/doc/latex/bibarts/README.txt
%{_texmfdistdir}/doc/latex/bibarts/ba-short.pdf
%{_texmfdistdir}/doc/latex/bibarts/ba-short.tex
%{_texmfdistdir}/doc/latex/bibarts/bibarts.pdf
%{_texmfdistdir}/doc/latex/bibarts/bibarts.tex

%files -n texlive-bibarts
%{_texmfdistdir}/tex/latex/bibarts/bibarts.sty

%package -n texlive-bibcop
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.19svn69467
Release:        0
License:        LPPL-1.0
Summary:        Style checker for .bib files
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibcop-bin >= %{texlive_version}
#!BuildIgnore: texlive-bibcop-bin
Requires:       texlive-iexec >= %{texlive_version}
#!BuildIgnore: texlive-iexec
Requires:       texlive-pgfopts >= %{texlive_version}
#!BuildIgnore: texlive-pgfopts
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibcop-doc >= %{texlive_version}
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
Provides:       tex(bibcop.sty)
Requires:       tex(iexec.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(shellesc.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source143:      bibcop.tar.xz
Source144:      bibcop.doc.tar.xz

%description -n texlive-bibcop
This LaTeX package checks the quality of your .bib file and
emits warning messages if any issues are found. For this, the
TeX processor must be run with the --shell-escape option, and
Perl must be installed. bibcop.pl can also be used as a
standalone command line tool. The package does not work on
Windows.

%package -n texlive-bibcop-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.19svn69467
Release:        0
Summary:        Documentation for texlive-bibcop
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibcop and texlive-alldocumentation)
Provides:       man(bibcop.1)

%description -n texlive-bibcop-doc
This package includes the documentation for texlive-bibcop

%post -n texlive-bibcop
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibcop
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibcop
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibcop-doc
%{_texmfdistdir}/doc/bibtex/bibcop/DEPENDS.txt
%{_texmfdistdir}/doc/bibtex/bibcop/LICENSE.txt
%{_texmfdistdir}/doc/bibtex/bibcop/README.md
%{_texmfdistdir}/doc/bibtex/bibcop/bibcop-logo.pdf
%{_texmfdistdir}/doc/bibtex/bibcop/bibcop.pdf
%{_mandir}/man1/bibcop.1*

%files -n texlive-bibcop
%{_texmfdistdir}/scripts/bibcop/bibcop.pl
%{_texmfdistdir}/tex/latex/bibcop/bibcop.sty

%package -n texlive-biber
Version:        %{texlive_version}.%{texlive_noarch}.2.19svn68188
Release:        0
License:        Artistic-2.0 AND GPL-2.0-or-later
Summary:        A BibTeX replacement for users of BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-biber-bin >= %{texlive_version}
#!BuildIgnore: texlive-biber-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source145:      biber.doc.tar.xz

%description -n texlive-biber
Biber is a BibTeX replacement for users of BibLaTeX. Biber
supports full UTF-8, can (re)-encode input and output, supports
highly configurable sorting, dynamic bibliography sets and many
other features. The CTAN distribution offers a compressed tar
archive of the sources, etc., together with "binary"
distributions for a variety of platforms. Note: on SourceForge
biber is formally named "biblatex-biber", to distinguish it
from an earlier (now apparently moribund) project called
"biber".

%post -n texlive-biber
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biber
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biber
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biber
%{_texmfdistdir}/doc/bibtex/biber/biber.pdf

%package -n texlive-biber-ms
Version:        %{texlive_version}.%{texlive_noarch}.4.0_1svn66478
Release:        0
License:        Artistic-2.0 AND GPL-2.0-or-later
Summary:        A BibTeX replacement for users of BibLaTeX (multiscript version)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-biber-ms-bin >= %{texlive_version}
#!BuildIgnore: texlive-biber-ms-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biber-ms-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source146:      biber-ms.source.tar.xz
Source147:      biber-ms.doc.tar.xz

%description -n texlive-biber-ms
This is the multiscript version of biber (biber-ms) and must be
used with the multiscript version of biblatex-ms

%package -n texlive-biber-ms-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.0_1svn66478
Release:        0
Summary:        Documentation for texlive-biber-ms
License:        Artistic-2.0 AND GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biber-ms and texlive-alldocumentation)

%description -n texlive-biber-ms-doc
This package includes the documentation for texlive-biber-ms

%post -n texlive-biber-ms
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biber-ms
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biber-ms
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biber-ms-doc
%{_texmfdistdir}/doc/bibtex/biber-ms/biber-ms.pdf

%files -n texlive-biber-ms
%{_texmfdistdir}/source/bibtex/biber-ms/Changes
%{_texmfdistdir}/source/bibtex/biber-ms/README.biber-ms-linux
%{_texmfdistdir}/source/bibtex/biber-ms/README.biber-ms-macos
%{_texmfdistdir}/source/bibtex/biber-ms/README.biber-ms-windows
%{_texmfdistdir}/source/bibtex/biber-ms/README.md
%{_texmfdistdir}/source/bibtex/biber-ms/biblatex-biber-ms.tar.gz
%{_texmfdistdir}/source/bibtex/biber-ms/utf8-macro-map.html

%package -n texlive-bibexport
Version:        %{texlive_version}.%{texlive_noarch}.3.03svn50677
Release:        0
License:        LPPL-1.0
Summary:        Extract a BibTeX file based on a .aux file
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibexport-bin >= %{texlive_version}
#!BuildIgnore: texlive-bibexport-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibexport-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source148:      bibexport.tar.xz
Source149:      bibexport.doc.tar.xz

%description -n texlive-bibexport
A Bourne shell script that uses BibTeX to extract bibliography
entries that are \cite'd in a document. It can also expand a
BibTeX file, expanding the abbreviations (other than the
built-in ones like month names) and following the
cross-references.

%package -n texlive-bibexport-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.03svn50677
Release:        0
Summary:        Documentation for texlive-bibexport
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibexport and texlive-alldocumentation)

%description -n texlive-bibexport-doc
This package includes the documentation for texlive-bibexport

%post -n texlive-bibexport
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibexport
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibexport
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibexport-doc
%{_texmfdistdir}/doc/bibtex/bibexport/README
%{_texmfdistdir}/doc/bibtex/bibexport/bibexport.pdf

%files -n texlive-bibexport
%{_texmfdistdir}/bibtex/bst/bibexport/expcites.bst
%{_texmfdistdir}/bibtex/bst/bibexport/expkeys.bst
%{_texmfdistdir}/bibtex/bst/bibexport/export.bst
%{_texmfdistdir}/scripts/bibexport/bibexport.sh

%package -n texlive-bibhtml
Version:        %{texlive_version}.%{texlive_noarch}.2.0.2svn31607
Release:        0
License:        GPL-2.0-or-later
Summary:        BibTeX support for HTML files
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibhtml-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source150:      bibhtml.tar.xz
Source151:      bibhtml.doc.tar.xz

%description -n texlive-bibhtml
Bibhtml consists of a Perl script and a set of BibTeX style
files, which together allow you to output a bibliography as a
collection of HTML files. The references in the text are linked
directly to the corresponding bibliography entry, and if a URL
is defined in the entry within the BibTeX database file, then
the generated bibliography entry is linked to this. The package
provides three different style files derived from each of the
standard plain.bst and alpha.bst, as well as two style files
derived from abbrv.bst and unsrt.bst (i.e., eight in total).

%package -n texlive-bibhtml-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.2svn31607
Release:        0
Summary:        Documentation for texlive-bibhtml
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibhtml and texlive-alldocumentation)

%description -n texlive-bibhtml-doc
This package includes the documentation for texlive-bibhtml

%post -n texlive-bibhtml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibhtml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibhtml
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibhtml-doc
%{_texmfdistdir}/doc/bibtex/bibhtml/LICENCE
%{_texmfdistdir}/doc/bibtex/bibhtml/README
%{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml
%{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml-extract-aux.xslt
%{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml-insert-bib.xslt
%{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml.html
%{_texmfdistdir}/doc/bibtex/bibhtml/bibrefs.bib
%{_texmfdistdir}/doc/bibtex/bibhtml/detex.sed
%{_texmfdistdir}/doc/bibtex/bibhtml/style.css

%files -n texlive-bibhtml
%{_texmfdistdir}/bibtex/bst/bibhtml/abbrvhtml.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/alphahtml.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/alphahtmldate.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/alphahtmldater.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/plainhtml.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/plainhtmldate.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/plainhtmldater.bst
%{_texmfdistdir}/bibtex/bst/bibhtml/unsrthtml.bst

%package -n texlive-biblatex
Version:        %{texlive_version}.%{texlive_noarch}.3.19svn66403
Release:        0
License:        LPPL-1.0
Summary:        Sophisticated Bibliographies in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-etoolbox >= %{texlive_version}
#!BuildIgnore: texlive-etoolbox
Requires:       texlive-kvoptions >= %{texlive_version}
#!BuildIgnore: texlive-kvoptions
Requires:       texlive-logreq >= %{texlive_version}
#!BuildIgnore: texlive-logreq
Requires:       texlive-pdftexcmds >= %{texlive_version}
#!BuildIgnore: texlive-pdftexcmds
Requires:       texlive-url >= %{texlive_version}
#!BuildIgnore: texlive-url
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-doc >= %{texlive_version}
Provides:       tex(UKenglish.lbx)
Provides:       tex(USenglish.lbx)
Provides:       tex(alphabetic-verb.bbx)
Provides:       tex(alphabetic-verb.cbx)
Provides:       tex(alphabetic.bbx)
Provides:       tex(alphabetic.cbx)
Provides:       tex(american.lbx)
Provides:       tex(australian.lbx)
Provides:       tex(austrian.lbx)
Provides:       tex(authortitle-comp.bbx)
Provides:       tex(authortitle-comp.cbx)
Provides:       tex(authortitle-ibid.bbx)
Provides:       tex(authortitle-ibid.cbx)
Provides:       tex(authortitle-icomp.bbx)
Provides:       tex(authortitle-icomp.cbx)
Provides:       tex(authortitle-tcomp.bbx)
Provides:       tex(authortitle-tcomp.cbx)
Provides:       tex(authortitle-terse.bbx)
Provides:       tex(authortitle-terse.cbx)
Provides:       tex(authortitle-ticomp.bbx)
Provides:       tex(authortitle-ticomp.cbx)
Provides:       tex(authortitle.bbx)
Provides:       tex(authortitle.cbx)
Provides:       tex(authoryear-comp.bbx)
Provides:       tex(authoryear-comp.cbx)
Provides:       tex(authoryear-ibid.bbx)
Provides:       tex(authoryear-ibid.cbx)
Provides:       tex(authoryear-icomp.bbx)
Provides:       tex(authoryear-icomp.cbx)
Provides:       tex(authoryear.bbx)
Provides:       tex(authoryear.cbx)
Provides:       tex(basque.lbx)
Provides:       tex(biblatex.cfg)
Provides:       tex(biblatex.def)
Provides:       tex(biblatex.sty)
Provides:       tex(blx-bibtex.def)
Provides:       tex(blx-case-expl3.sty)
Provides:       tex(blx-case-latex2e.sty)
Provides:       tex(blx-compat.def)
Provides:       tex(blx-dm.def)
Provides:       tex(blx-mcite.def)
Provides:       tex(blx-natbib.def)
Provides:       tex(blx-unicode.def)
Provides:       tex(brazil.lbx)
Provides:       tex(brazilian.lbx)
Provides:       tex(british.lbx)
Provides:       tex(bulgarian.lbx)
Provides:       tex(canadian.lbx)
Provides:       tex(catalan.lbx)
Provides:       tex(croatian.lbx)
Provides:       tex(czech.lbx)
Provides:       tex(danish.lbx)
Provides:       tex(debug.bbx)
Provides:       tex(debug.cbx)
Provides:       tex(draft.bbx)
Provides:       tex(draft.cbx)
Provides:       tex(dutch.lbx)
Provides:       tex(english.lbx)
Provides:       tex(estonian.lbx)
Provides:       tex(finnish.lbx)
Provides:       tex(french.lbx)
Provides:       tex(galician.lbx)
Provides:       tex(german.lbx)
Provides:       tex(greek.lbx)
Provides:       tex(hungarian.lbx)
Provides:       tex(icelandic.lbx)
Provides:       tex(italian.lbx)
Provides:       tex(latvian.lbx)
Provides:       tex(lithuanian.lbx)
Provides:       tex(magyar.lbx)
Provides:       tex(marathi.lbx)
Provides:       tex(naustrian.lbx)
Provides:       tex(newzealand.lbx)
Provides:       tex(ngerman.lbx)
Provides:       tex(norsk.lbx)
Provides:       tex(nswissgerman.lbx)
Provides:       tex(numeric-comp.bbx)
Provides:       tex(numeric-comp.cbx)
Provides:       tex(numeric-verb.bbx)
Provides:       tex(numeric-verb.cbx)
Provides:       tex(numeric.bbx)
Provides:       tex(numeric.cbx)
Provides:       tex(nynorsk.lbx)
Provides:       tex(polish.lbx)
Provides:       tex(portuges.lbx)
Provides:       tex(portuguese.lbx)
Provides:       tex(reading.bbx)
Provides:       tex(reading.cbx)
Provides:       tex(romanian.lbx)
Provides:       tex(russian.lbx)
Provides:       tex(serbian.lbx)
Provides:       tex(serbianc.lbx)
Provides:       tex(slovak.lbx)
Provides:       tex(slovene.lbx)
Provides:       tex(slovenian.lbx)
Provides:       tex(spanish.lbx)
Provides:       tex(standard.bbx)
Provides:       tex(swedish.lbx)
Provides:       tex(swissgerman.lbx)
Provides:       tex(turkish.lbx)
Provides:       tex(ukrainian.lbx)
Provides:       tex(verbose-ibid.bbx)
Provides:       tex(verbose-ibid.cbx)
Provides:       tex(verbose-inote.bbx)
Provides:       tex(verbose-inote.cbx)
Provides:       tex(verbose-note.bbx)
Provides:       tex(verbose-note.cbx)
Provides:       tex(verbose-trad1.bbx)
Provides:       tex(verbose-trad1.cbx)
Provides:       tex(verbose-trad2.bbx)
Provides:       tex(verbose-trad2.cbx)
Provides:       tex(verbose-trad3.bbx)
Provides:       tex(verbose-trad3.cbx)
Provides:       tex(verbose.bbx)
Provides:       tex(verbose.cbx)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(logreq.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(url.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source152:      biblatex.tar.xz
Source153:      biblatex.doc.tar.xz

%description -n texlive-biblatex
BibLaTeX is a complete reimplementation of the bibliographic
facilities provided by LaTeX. Formatting of the bibliography is
entirely controlled by LaTeX macros, and a working knowledge of
LaTeX should be sufficient to design new bibliography and
citation styles. BibLaTeX uses its own data backend program
called "biber" to read and process the bibliographic data. With
biber, BibLaTeX has many features rivalling or surpassing other
bibliography systems. To mention a few: Full Unicode support
Highly customisable sorting using the Unicode Collation
Algorithm + CLDR tailoring Highly customisable bibliography
labels Complex macro-based on-the-fly data modification without
changing your data sources A tool mode for transforming
bibliographic data sources Multiple bibliographies and lists of
bibliographic information in the same document with different
sorting Highly customisable data source inheritance rules
Polyglossia and babel suppport for automatic language switching
for bibliographic entries and citations Automatic bibliography
data recoding (UTF-8 -> latin1, LaTeX macros -> UTF-8 etc)
Remote data sources Highly sophisticated automatic name and
name list disambiguation system Highly customisable data model
so users can define their own bibliographic data types
Validation of bibliographic data against a data model
Subdivided and/or filtered bibligraphies, bibliographies per
chapter, section etc. Apart from the features unique to
BibLaTeX, the package also incorporates core features of the
following packages: babelbib, bibtopic, bibunits, chapterbib,
cite, inlinebib, mcite and mciteplus, mlbib, multibib,
splitbib. The package strictly requires e-TeX BibTeX, bibtex8,
or Biber etoolbox 2.1 or later logreq 1.0 or later keyval
ifthen url Biber, babel / polyglossia, and csquotes 4.4 or
later are strongly recommended.

%package -n texlive-biblatex-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.19svn66403
Release:        0
Summary:        Documentation for texlive-biblatex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-doc:en)

%description -n texlive-biblatex-doc
This package includes the documentation for texlive-biblatex

%post -n texlive-biblatex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-doc
%{_texmfdistdir}/doc/latex/biblatex/CHANGES.md
%{_texmfdistdir}/doc/latex/biblatex/README
%{_texmfdistdir}/doc/latex/biblatex/biber/bltxml/biblatex-examples.bltxml
%{_texmfdistdir}/doc/latex/biblatex/biblatex.pdf
%{_texmfdistdir}/doc/latex/biblatex/biblatex.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/01-introduction-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/01-introduction-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/01-introduction.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/02-annotations-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/02-annotations-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/02-annotations.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/03-localization-keys-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/03-localization-keys-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/03-localization-keys.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/04-delimiters-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/04-delimiters-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/04-delimiters.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/10-references-per-section-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/10-references-per-section-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/10-references-per-section.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/11-references-by-section-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/11-references-by-section-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/11-references-by-section.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/12-references-by-segment-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/12-references-by-segment-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/12-references-by-segment.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/13-references-by-keyword-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/13-references-by-keyword-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/13-references-by-keyword.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/14-references-by-category-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/14-references-by-category-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/14-references-by-category.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/15-references-by-type-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/15-references-by-type-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/15-references-by-type.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/16-numeric-prefixed-1-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/16-numeric-prefixed-1-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/16-numeric-prefixed-1.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/17-numeric-prefixed-2-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/17-numeric-prefixed-2-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/17-numeric-prefixed-2.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/18-numeric-hybrid-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/18-numeric-hybrid-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/18-numeric-hybrid.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/19-alphabetic-prefixed-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/19-alphabetic-prefixed-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/19-alphabetic-prefixed.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/20-indexing-single-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/20-indexing-single-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/20-indexing-single.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/21-indexing-multiple-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/21-indexing-multiple-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/21-indexing-multiple.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/22-indexing-subentry-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/22-indexing-subentry-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/22-indexing-subentry.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/30-style-numeric-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/30-style-numeric-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/30-style-numeric.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/31-style-numeric-comp-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/31-style-numeric-comp-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/31-style-numeric-comp.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/32-style-numeric-verb-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/32-style-numeric-verb-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/32-style-numeric-verb.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/40-style-alphabetic-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/40-style-alphabetic-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/40-style-alphabetic.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/41-style-alphabetic-verb-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/41-style-alphabetic-verb-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/41-style-alphabetic-verb.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/42-style-alphabetic-template-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/42-style-alphabetic-template-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/42-style-alphabetic-template.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/50-style-authoryear-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/50-style-authoryear-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/50-style-authoryear.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/51-style-authoryear-ibid-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/51-style-authoryear-ibid-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/51-style-authoryear-ibid.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/52-style-authoryear-comp-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/52-style-authoryear-comp-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/52-style-authoryear-comp.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/53-style-authoryear-icomp-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/53-style-authoryear-icomp-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/53-style-authoryear-icomp.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/60-style-authortitle-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/60-style-authortitle-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/60-style-authortitle.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/61-style-authortitle-ibid-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/61-style-authortitle-ibid-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/61-style-authortitle-ibid.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/62-style-authortitle-comp-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/62-style-authortitle-comp-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/62-style-authortitle-comp.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/63-style-authortitle-icomp-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/63-style-authortitle-icomp-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/63-style-authortitle-icomp.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/64-style-authortitle-terse-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/64-style-authortitle-terse-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/64-style-authortitle-terse.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/65-style-authortitle-tcomp-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/65-style-authortitle-tcomp-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/65-style-authortitle-tcomp.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/66-style-authortitle-ticomp-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/66-style-authortitle-ticomp-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/66-style-authortitle-ticomp.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/70-style-verbose-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/70-style-verbose-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/70-style-verbose.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/71-style-verbose-ibid-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/71-style-verbose-ibid-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/71-style-verbose-ibid.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/72-style-verbose-note-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/72-style-verbose-note-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/72-style-verbose-note.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/73-style-verbose-inote-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/73-style-verbose-inote-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/73-style-verbose-inote.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/74-style-verbose-trad1-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/74-style-verbose-trad1-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/74-style-verbose-trad1.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/75-style-verbose-trad2-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/75-style-verbose-trad2-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/75-style-verbose-trad2.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/76-style-verbose-trad3-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/76-style-verbose-trad3-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/76-style-verbose-trad3.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/80-style-reading-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/80-style-reading-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/80-style-reading.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/81-style-draft-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/81-style-draft-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/81-style-draft.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/82-style-debug-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/82-style-debug-bibtex.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/82-style-debug.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/90-related-entries-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/90-related-entries.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/91-sorting-schemes-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/91-sorting-schemes.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/92-bibliographylists-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/92-bibliographylists.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/93-nameparts-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/93-nameparts.dbx
%{_texmfdistdir}/doc/latex/biblatex/examples/93-nameparts.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/94-labelprefix-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/94-labelprefix.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/95-customlists-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/95-customlists.bib
%{_texmfdistdir}/doc/latex/biblatex/examples/95-customlists.dbx
%{_texmfdistdir}/doc/latex/biblatex/examples/95-customlists.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/96-dates-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/96-dates.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/97-annotations-biber.pdf
%{_texmfdistdir}/doc/latex/biblatex/examples/97-annotations.bib
%{_texmfdistdir}/doc/latex/biblatex/examples/97-annotations.tex
%{_texmfdistdir}/doc/latex/biblatex/examples/biblatex-examples.bib
%{_texmfdistdir}/doc/latex/biblatex/examples/biblatex-examples.bltxml

%files -n texlive-biblatex
%{_texmfdistdir}/bibtex/bib/biblatex/biblatex/biblatex-examples.bib
%{_texmfdistdir}/bibtex/bst/biblatex/biblatex.bst
%{_texmfdistdir}/tex/latex/biblatex/bbx/alphabetic-verb.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-icomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-tcomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-terse.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle-ticomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authortitle.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear-icomp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/authoryear.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/debug.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/draft.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/numeric-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/numeric-verb.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/reading.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/standard.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-inote.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-note.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-trad1.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-trad2.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose-trad3.bbx
%{_texmfdistdir}/tex/latex/biblatex/bbx/verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex/biblatex.cfg
%{_texmfdistdir}/tex/latex/biblatex/biblatex.def
%{_texmfdistdir}/tex/latex/biblatex/biblatex.sty
%{_texmfdistdir}/tex/latex/biblatex/blx-bibtex.def
%{_texmfdistdir}/tex/latex/biblatex/blx-case-expl3.sty
%{_texmfdistdir}/tex/latex/biblatex/blx-case-latex2e.sty
%{_texmfdistdir}/tex/latex/biblatex/blx-compat.def
%{_texmfdistdir}/tex/latex/biblatex/blx-dm.def
%{_texmfdistdir}/tex/latex/biblatex/blx-mcite.def
%{_texmfdistdir}/tex/latex/biblatex/blx-natbib.def
%{_texmfdistdir}/tex/latex/biblatex/blx-unicode.def
%{_texmfdistdir}/tex/latex/biblatex/cbx/alphabetic-verb.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-icomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-tcomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-terse.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle-ticomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authortitle.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear-icomp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/authoryear.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/debug.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/draft.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/numeric-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/numeric-verb.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/reading.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-inote.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-note.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-trad1.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-trad2.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose-trad3.cbx
%{_texmfdistdir}/tex/latex/biblatex/cbx/verbose.cbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/UKenglish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/USenglish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/american.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/australian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/austrian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/basque.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/brazil.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/brazilian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/british.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/bulgarian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/canadian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/catalan.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/croatian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/czech.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/danish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/dutch.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/english.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/estonian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/finnish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/french.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/galician.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/german.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/greek.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/hungarian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/icelandic.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/italian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/latvian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/lithuanian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/magyar.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/marathi.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/naustrian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/newzealand.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/ngerman.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/norsk.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/nswissgerman.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/nynorsk.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/polish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/portuges.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/portuguese.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/romanian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/russian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/serbian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/serbianc.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/slovak.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/slovene.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/slovenian.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/spanish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/swedish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/swissgerman.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/turkish.lbx
%{_texmfdistdir}/tex/latex/biblatex/lbx/ukrainian.lbx

%package -n texlive-biblatex-abnt
Version:        %{texlive_version}.%{texlive_noarch}.3.4svn49179
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX style for Brazil's ABNT rules
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-abnt-doc >= %{texlive_version}
Provides:       tex(abnt-ibid.bbx)
Provides:       tex(abnt-ibid.cbx)
Provides:       tex(abnt-numeric.bbx)
Provides:       tex(abnt-numeric.cbx)
Provides:       tex(abnt.bbx)
Provides:       tex(abnt.cbx)
Provides:       tex(american-abnt.lbx)
Provides:       tex(australian-abnt.lbx)
Provides:       tex(brazil-abnt.lbx)
Provides:       tex(brazilian-abnt.lbx)
Provides:       tex(british-abnt.lbx)
Provides:       tex(canadian-abnt.lbx)
Provides:       tex(english-abnt.lbx)
Provides:       tex(portuges-abnt.lbx)
Provides:       tex(portuguese-abnt.lbx)
Provides:       tex(spanish-abnt.lbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(brazilian.lbx)
Requires:       tex(english.lbx)
Requires:       tex(expl3.sty)
Requires:       tex(numeric.cbx)
Requires:       tex(spanish.lbx)
Requires:       tex(standard.bbx)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source154:      biblatex-abnt.tar.xz
Source155:      biblatex-abnt.doc.tar.xz

%description -n texlive-biblatex-abnt
This package offers a BibLaTeX style for Brazil's ABNT
(Brazilian Association of Technical Norms) rules.

%package -n texlive-biblatex-abnt-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.4svn49179
Release:        0
Summary:        Documentation for texlive-biblatex-abnt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-abnt and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-abnt-doc:pt_BR)

%description -n texlive-biblatex-abnt-doc
This package includes the documentation for texlive-biblatex-abnt

%post -n texlive-biblatex-abnt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-abnt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-abnt
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-abnt-doc
%{_texmfdistdir}/doc/latex/biblatex-abnt/CHANGELOG.md
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR10520-2002.bib
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR10520-2002.tex
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR10520-2002_reference.pdf
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR10520-2002_test.tex
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR6023-2002.bib
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR6023-2002.tex
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR6023-2002_reference.pdf
%{_texmfdistdir}/doc/latex/biblatex-abnt/NBR6023-2002_test.tex
%{_texmfdistdir}/doc/latex/biblatex-abnt/README.md
%{_texmfdistdir}/doc/latex/biblatex-abnt/biblatex-abnt.bib
%{_texmfdistdir}/doc/latex/biblatex-abnt/biblatex-abnt.pdf
%{_texmfdistdir}/doc/latex/biblatex-abnt/biblatex-abnt.tex
%{_texmfdistdir}/doc/latex/biblatex-abnt/test.sh
%{_texmfdistdir}/doc/latex/biblatex-abnt/tests/README.md
%{_texmfdistdir}/doc/latex/biblatex-abnt/texlive.sh

%files -n texlive-biblatex-abnt
%{_texmfdistdir}/tex/latex/biblatex-abnt/abnt-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/abnt-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/abnt-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/abnt-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/abnt.bbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/abnt.cbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/american-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/australian-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/brazil-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/brazilian-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/british-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/canadian-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/english-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/portuges-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/portuguese-abnt.lbx
%{_texmfdistdir}/tex/latex/biblatex-abnt/spanish-abnt.lbx

%package -n texlive-biblatex-ajc2020unofficial
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn54401
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX style for the Australasian Journal of Combinatorics
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-ajc2020unofficial-doc >= %{texlive_version}
Provides:       tex(ajc2020unofficial.bbx)
Provides:       tex(ajc2020unofficial.cbx)
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
Requires:       tex(shortmathj.sty)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source156:      biblatex-ajc2020unofficial.tar.xz
Source157:      biblatex-ajc2020unofficial.doc.tar.xz

%description -n texlive-biblatex-ajc2020unofficial
This is an unofficial BibLaTeX style for the Australasian
Journal of Combinatorics. Note that the journal (as for 01
March 2020) does not accept BibLaTeX, so you probably want to
use biblatex2bibitem.

%package -n texlive-biblatex-ajc2020unofficial-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn54401
Release:        0
Summary:        Documentation for texlive-biblatex-ajc2020unofficial
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-ajc2020unofficial and texlive-alldocumentation)

%description -n texlive-biblatex-ajc2020unofficial-doc
This package includes the documentation for texlive-biblatex-ajc2020unofficial

%post -n texlive-biblatex-ajc2020unofficial
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-ajc2020unofficial
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-ajc2020unofficial
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-ajc2020unofficial-doc
%{_texmfdistdir}/doc/latex/biblatex-ajc2020unofficial/README.md

%files -n texlive-biblatex-ajc2020unofficial
%{_texmfdistdir}/tex/latex/biblatex-ajc2020unofficial/ajc2020unofficial.bbx
%{_texmfdistdir}/tex/latex/biblatex-ajc2020unofficial/ajc2020unofficial.cbx

%package -n texlive-biblatex-anonymous
Version:        %{texlive_version}.%{texlive_noarch}.2.6.2svn48548
Release:        0
License:        LPPL-1.0
Summary:        A tool to manage anonymous work with BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-anonymous-doc >= %{texlive_version}
Provides:       tex(biblatex-anonymous.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source158:      biblatex-anonymous.tar.xz
Source159:      biblatex-anonymous.doc.tar.xz

%description -n texlive-biblatex-anonymous
The package provides tools to help manage anonymous work with
BibLaTeX. It will be useful, for example, in history or
classical philology.

%package -n texlive-biblatex-anonymous-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.6.2svn48548
Release:        0
Summary:        Documentation for texlive-biblatex-anonymous
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-anonymous and texlive-alldocumentation)

%description -n texlive-biblatex-anonymous-doc
This package includes the documentation for texlive-biblatex-anonymous

%post -n texlive-biblatex-anonymous
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-anonymous
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-anonymous
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-anonymous-doc
%{_texmfdistdir}/doc/latex/biblatex-anonymous/README
%{_texmfdistdir}/doc/latex/biblatex-anonymous/biblatex-anonymous.pdf
%{_texmfdistdir}/doc/latex/biblatex-anonymous/biblatex-anonymous.tex
%{_texmfdistdir}/doc/latex/biblatex-anonymous/latexmkrc
%{_texmfdistdir}/doc/latex/biblatex-anonymous/makefile

%files -n texlive-biblatex-anonymous
%{_texmfdistdir}/tex/latex/biblatex-anonymous/biblatex-anonymous.sty

%package -n texlive-biblatex-apa
Version:        %{texlive_version}.%{texlive_noarch}.9.17svn66605
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX citation and reference style for APA
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-apa-doc >= %{texlive_version}
Provides:       tex(american-apa.lbx)
Provides:       tex(apa.bbx)
Provides:       tex(apa.cbx)
Provides:       tex(austrian-apa.lbx)
Provides:       tex(brazilian-apa.lbx)
Provides:       tex(british-apa.lbx)
Provides:       tex(catalan-apa.lbx)
Provides:       tex(danish-apa.lbx)
Provides:       tex(dutch-apa.lbx)
Provides:       tex(english-apa.lbx)
Provides:       tex(finnish-apa.lbx)
Provides:       tex(french-apa.lbx)
Provides:       tex(galician-apa.lbx)
Provides:       tex(german-apa.lbx)
Provides:       tex(greek-apa.lbx)
Provides:       tex(hungarian-apa.lbx)
Provides:       tex(italian-apa.lbx)
Provides:       tex(naustrian-apa.lbx)
Provides:       tex(ngerman-apa.lbx)
Provides:       tex(norsk-apa.lbx)
Provides:       tex(norwegian-apa.lbx)
Provides:       tex(nswissgerman-apa.lbx)
Provides:       tex(nynorsk-apa.lbx)
Provides:       tex(portuguese-apa.lbx)
Provides:       tex(russian-apa.lbx)
Provides:       tex(slovene-apa.lbx)
Provides:       tex(spanish-apa.lbx)
Provides:       tex(swedish-apa.lbx)
Provides:       tex(swissgerman-apa.lbx)
Provides:       tex(turkish-apa.lbx)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source160:      biblatex-apa.tar.xz
Source161:      biblatex-apa.doc.tar.xz

%description -n texlive-biblatex-apa
This is a fairly complete BibLaTeX style (citations and
references) for APA (American Psychological Association)
publications. It implements and automates most of the
guidelines in the APA 7th edition style guide for citations and
references. An example document is also given which typesets
every citation and reference example in the APA 7th edition
style guide. This version of the package requires use of
csquotes [?]4.3, BibLaTeX [?]3.4, and the biber backend for
BibLaTeX [?]2.5.

%package -n texlive-biblatex-apa-doc
Version:        %{texlive_version}.%{texlive_noarch}.9.17svn66605
Release:        0
Summary:        Documentation for texlive-biblatex-apa
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-apa and texlive-alldocumentation)

%description -n texlive-biblatex-apa-doc
This package includes the documentation for texlive-biblatex-apa

%post -n texlive-biblatex-apa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-apa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-apa
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-apa-doc
%{_texmfdistdir}/doc/latex/biblatex-apa/README
%{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test-citations.bib
%{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test-misc.bib
%{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test-references.bib
%{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test.pdf
%{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa-test.tex
%{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa.pdf
%{_texmfdistdir}/doc/latex/biblatex-apa/biblatex-apa.tex

%files -n texlive-biblatex-apa
%{_texmfdistdir}/tex/latex/biblatex-apa/american-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/apa.bbx
%{_texmfdistdir}/tex/latex/biblatex-apa/apa.cbx
%{_texmfdistdir}/tex/latex/biblatex-apa/apa.dbx
%{_texmfdistdir}/tex/latex/biblatex-apa/apa.lua
%{_texmfdistdir}/tex/latex/biblatex-apa/austrian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/brazilian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/british-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/catalan-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/danish-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/dutch-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/english-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/finnish-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/french-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/galician-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/german-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/greek-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/hungarian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/italian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/naustrian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/ngerman-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/norsk-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/norwegian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/nswissgerman-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/nynorsk-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/portuguese-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/russian-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/slovene-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/spanish-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/swedish-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/swissgerman-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa/turkish-apa.lbx

%package -n texlive-biblatex-apa6
Version:        %{texlive_version}.%{texlive_noarch}.8.5svn56209
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX citation and reference style for APA 6th Edition
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-apa6-doc >= %{texlive_version}
Provides:       tex(american-apa6.lbx)
Provides:       tex(apa6.bbx)
Provides:       tex(apa6.cbx)
Provides:       tex(austrian-apa6.lbx)
Provides:       tex(brazilian-apa6.lbx)
Provides:       tex(british-apa6.lbx)
Provides:       tex(danish-apa6.lbx)
Provides:       tex(dutch-apa6.lbx)
Provides:       tex(english-apa6.lbx)
Provides:       tex(french-apa6.lbx)
Provides:       tex(galician-apa6.lbx)
Provides:       tex(german-apa6.lbx)
Provides:       tex(greek-apa6.lbx)
Provides:       tex(italian-apa6.lbx)
Provides:       tex(naustrian-apa6.lbx)
Provides:       tex(ngerman-apa6.lbx)
Provides:       tex(norsk-apa6.lbx)
Provides:       tex(norwegian-apa6.lbx)
Provides:       tex(nswissgerman-apa6.lbx)
Provides:       tex(nynorsk-apa6.lbx)
Provides:       tex(portuguese-apa6.lbx)
Provides:       tex(russian-apa6.lbx)
Provides:       tex(slovene-apa6.lbx)
Provides:       tex(spanish-apa6.lbx)
Provides:       tex(swedish-apa6.lbx)
Provides:       tex(swissgerman-apa6.lbx)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source162:      biblatex-apa6.tar.xz
Source163:      biblatex-apa6.doc.tar.xz

%description -n texlive-biblatex-apa6
This is a fairly complete BibLaTeX style (citations and
references) for APA (American Psychological Association) 6th
Edition conformant publications. It implements and automates
most of the guidelines in the APA 6th edition style guide for
citations and references. An example document is also given
which typesets every citation and reference example in the APA
6th edition style guide. This is a legacy style for 6th Edition
documents. Please use the BibLaTeX-apa style package for the
latest APA edition conformance.

%package -n texlive-biblatex-apa6-doc
Version:        %{texlive_version}.%{texlive_noarch}.8.5svn56209
Release:        0
Summary:        Documentation for texlive-biblatex-apa6
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-apa6 and texlive-alldocumentation)

%description -n texlive-biblatex-apa6-doc
This package includes the documentation for texlive-biblatex-apa6

%post -n texlive-biblatex-apa6
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-apa6
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-apa6
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-apa6-doc
%{_texmfdistdir}/doc/latex/biblatex-apa6/README
%{_texmfdistdir}/doc/latex/biblatex-apa6/biblatex-apa6-test-citations.bib
%{_texmfdistdir}/doc/latex/biblatex-apa6/biblatex-apa6-test-references.bib
%{_texmfdistdir}/doc/latex/biblatex-apa6/biblatex-apa6-test.pdf
%{_texmfdistdir}/doc/latex/biblatex-apa6/biblatex-apa6-test.tex
%{_texmfdistdir}/doc/latex/biblatex-apa6/biblatex-apa6.pdf
%{_texmfdistdir}/doc/latex/biblatex-apa6/biblatex-apa6.tex

%files -n texlive-biblatex-apa6
%{_texmfdistdir}/tex/latex/biblatex-apa6/american-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/apa6.bbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/apa6.cbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/apa6.dbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/austrian-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/brazilian-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/british-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/danish-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/dutch-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/english-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/french-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/galician-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/german-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/greek-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/italian-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/naustrian-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/ngerman-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/norsk-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/norwegian-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/nswissgerman-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/nynorsk-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/portuguese-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/russian-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/slovene-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/spanish-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/swedish-apa6.lbx
%{_texmfdistdir}/tex/latex/biblatex-apa6/swissgerman-apa6.lbx

%package -n texlive-biblatex-archaeology
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn53281
Release:        0
License:        LPPL-1.0
Summary:        A collection of BibLaTeX styles for German prehistory
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-archaeology-doc >= %{texlive_version}
Provides:       tex(UKenglish-aefkw.lbx)
Provides:       tex(UKenglish-archa.lbx)
Provides:       tex(UKenglish-archaeology.lbx)
Provides:       tex(UKenglish-dguf-alt.lbx)
Provides:       tex(UKenglish-dguf-apa.lbx)
Provides:       tex(UKenglish-eaz.lbx)
Provides:       tex(UKenglish-foe.lbx)
Provides:       tex(UKenglish-jb-kreis-neuss.lbx)
Provides:       tex(UKenglish-karl.lbx)
Provides:       tex(UKenglish-kunde.lbx)
Provides:       tex(UKenglish-maja.lbx)
Provides:       tex(UKenglish-mpk.lbx)
Provides:       tex(UKenglish-mpkoeaw.lbx)
Provides:       tex(UKenglish-niedersachsen.lbx)
Provides:       tex(UKenglish-offa.lbx)
Provides:       tex(UKenglish-rgzm.lbx)
Provides:       tex(UKenglish-zaak.lbx)
Provides:       tex(UKenglish-zaes.lbx)
Provides:       tex(USenglish-aefkw.lbx)
Provides:       tex(USenglish-archa.lbx)
Provides:       tex(USenglish-archaeology.lbx)
Provides:       tex(USenglish-dguf-alt.lbx)
Provides:       tex(USenglish-dguf-apa.lbx)
Provides:       tex(USenglish-eaz.lbx)
Provides:       tex(USenglish-foe.lbx)
Provides:       tex(USenglish-jb-kreis-neuss.lbx)
Provides:       tex(USenglish-karl.lbx)
Provides:       tex(USenglish-kunde.lbx)
Provides:       tex(USenglish-maja.lbx)
Provides:       tex(USenglish-mpk.lbx)
Provides:       tex(USenglish-mpkoeaw.lbx)
Provides:       tex(USenglish-niedersachsen.lbx)
Provides:       tex(USenglish-offa.lbx)
Provides:       tex(USenglish-rgzm.lbx)
Provides:       tex(USenglish-zaak.lbx)
Provides:       tex(USenglish-zaes.lbx)
Provides:       tex(aefkw.bbx)
Provides:       tex(aefkw.cbx)
Provides:       tex(afwl.bbx)
Provides:       tex(afwl.cbx)
Provides:       tex(american-aefkw.lbx)
Provides:       tex(american-archa.lbx)
Provides:       tex(american-archaeology.lbx)
Provides:       tex(american-dguf-alt.lbx)
Provides:       tex(american-dguf-apa.lbx)
Provides:       tex(american-eaz.lbx)
Provides:       tex(american-foe.lbx)
Provides:       tex(american-jb-kreis-neuss.lbx)
Provides:       tex(american-karl.lbx)
Provides:       tex(american-kunde.lbx)
Provides:       tex(american-maja.lbx)
Provides:       tex(american-mpk.lbx)
Provides:       tex(american-mpkoeaw.lbx)
Provides:       tex(american-niedersachsen.lbx)
Provides:       tex(american-offa.lbx)
Provides:       tex(american-rgzm.lbx)
Provides:       tex(american-zaak.lbx)
Provides:       tex(american-zaes.lbx)
Provides:       tex(amit.bbx)
Provides:       tex(amit.cbx)
Provides:       tex(archa.bbx)
Provides:       tex(archa.cbx)
Provides:       tex(australian-aefkw.lbx)
Provides:       tex(australian-archa.lbx)
Provides:       tex(australian-archaeology.lbx)
Provides:       tex(australian-dguf-alt.lbx)
Provides:       tex(australian-dguf-apa.lbx)
Provides:       tex(australian-eaz.lbx)
Provides:       tex(australian-foe.lbx)
Provides:       tex(australian-jb-kreis-neuss.lbx)
Provides:       tex(australian-karl.lbx)
Provides:       tex(australian-kunde.lbx)
Provides:       tex(australian-maja.lbx)
Provides:       tex(australian-mpk.lbx)
Provides:       tex(australian-mpkoeaw.lbx)
Provides:       tex(australian-niedersachsen.lbx)
Provides:       tex(australian-offa.lbx)
Provides:       tex(australian-rgzm.lbx)
Provides:       tex(australian-zaak.lbx)
Provides:       tex(australian-zaes.lbx)
Provides:       tex(austrian-aefkw.lbx)
Provides:       tex(austrian-archa.lbx)
Provides:       tex(austrian-archaeology.lbx)
Provides:       tex(austrian-dguf-alt.lbx)
Provides:       tex(austrian-dguf-apa.lbx)
Provides:       tex(austrian-eaz.lbx)
Provides:       tex(austrian-foe.lbx)
Provides:       tex(austrian-jb-kreis-neuss.lbx)
Provides:       tex(austrian-karl.lbx)
Provides:       tex(austrian-kunde.lbx)
Provides:       tex(austrian-maja.lbx)
Provides:       tex(austrian-mpk.lbx)
Provides:       tex(austrian-mpkoeaw.lbx)
Provides:       tex(austrian-niedersachsen.lbx)
Provides:       tex(austrian-offa.lbx)
Provides:       tex(austrian-rgzm.lbx)
Provides:       tex(austrian-zaak.lbx)
Provides:       tex(austrian-zaes.lbx)
Provides:       tex(authoryear-archaeology.bbx)
Provides:       tex(authoryear-archaeology.cbx)
Provides:       tex(authoryear-comp-archaeology.bbx)
Provides:       tex(authoryear-comp-archaeology.cbx)
Provides:       tex(authoryear-ibid-archaeology.bbx)
Provides:       tex(authoryear-ibid-archaeology.cbx)
Provides:       tex(authoryear-icomp-archaeology.bbx)
Provides:       tex(authoryear-icomp-archaeology.cbx)
Provides:       tex(biblatex-archaeology.sty)
Provides:       tex(british-aefkw.lbx)
Provides:       tex(british-archa.lbx)
Provides:       tex(british-archaeology.lbx)
Provides:       tex(british-dguf-alt.lbx)
Provides:       tex(british-dguf-apa.lbx)
Provides:       tex(british-eaz.lbx)
Provides:       tex(british-foe.lbx)
Provides:       tex(british-jb-kreis-neuss.lbx)
Provides:       tex(british-karl.lbx)
Provides:       tex(british-kunde.lbx)
Provides:       tex(british-maja.lbx)
Provides:       tex(british-mpk.lbx)
Provides:       tex(british-mpkoeaw.lbx)
Provides:       tex(british-niedersachsen.lbx)
Provides:       tex(british-offa.lbx)
Provides:       tex(british-rgzm.lbx)
Provides:       tex(british-zaak.lbx)
Provides:       tex(british-zaes.lbx)
Provides:       tex(canadian-aefkw.lbx)
Provides:       tex(canadian-archa.lbx)
Provides:       tex(canadian-archaeology.lbx)
Provides:       tex(canadian-dguf-alt.lbx)
Provides:       tex(canadian-dguf-apa.lbx)
Provides:       tex(canadian-eaz.lbx)
Provides:       tex(canadian-foe.lbx)
Provides:       tex(canadian-jb-kreis-neuss.lbx)
Provides:       tex(canadian-karl.lbx)
Provides:       tex(canadian-kunde.lbx)
Provides:       tex(canadian-maja.lbx)
Provides:       tex(canadian-mpk.lbx)
Provides:       tex(canadian-mpkoeaw.lbx)
Provides:       tex(canadian-niedersachsen.lbx)
Provides:       tex(canadian-offa.lbx)
Provides:       tex(canadian-rgzm.lbx)
Provides:       tex(canadian-zaak.lbx)
Provides:       tex(canadian-zaes.lbx)
Provides:       tex(dguf-alt.bbx)
Provides:       tex(dguf-alt.cbx)
Provides:       tex(dguf-apa.bbx)
Provides:       tex(dguf-apa.cbx)
Provides:       tex(dguf.bbx)
Provides:       tex(dguf.cbx)
Provides:       tex(eaz-alt.bbx)
Provides:       tex(eaz-alt.cbx)
Provides:       tex(eaz.bbx)
Provides:       tex(eaz.cbx)
Provides:       tex(english-aefkw.lbx)
Provides:       tex(english-archa.lbx)
Provides:       tex(english-archaeology.lbx)
Provides:       tex(english-dguf-alt.lbx)
Provides:       tex(english-dguf-apa.lbx)
Provides:       tex(english-eaz.lbx)
Provides:       tex(english-foe.lbx)
Provides:       tex(english-jb-kreis-neuss.lbx)
Provides:       tex(english-karl.lbx)
Provides:       tex(english-kunde.lbx)
Provides:       tex(english-maja.lbx)
Provides:       tex(english-mpk.lbx)
Provides:       tex(english-mpkoeaw.lbx)
Provides:       tex(english-niedersachsen.lbx)
Provides:       tex(english-offa.lbx)
Provides:       tex(english-rgzm.lbx)
Provides:       tex(english-zaak.lbx)
Provides:       tex(english-zaes.lbx)
Provides:       tex(foe.bbx)
Provides:       tex(foe.cbx)
Provides:       tex(german-aefkw.lbx)
Provides:       tex(german-archa.lbx)
Provides:       tex(german-archaeology.lbx)
Provides:       tex(german-dguf-alt.lbx)
Provides:       tex(german-dguf-apa.lbx)
Provides:       tex(german-eaz.lbx)
Provides:       tex(german-foe.lbx)
Provides:       tex(german-jb-kreis-neuss.lbx)
Provides:       tex(german-karl.lbx)
Provides:       tex(german-kunde.lbx)
Provides:       tex(german-maja.lbx)
Provides:       tex(german-mpk.lbx)
Provides:       tex(german-mpkoeaw.lbx)
Provides:       tex(german-niedersachsen.lbx)
Provides:       tex(german-offa.lbx)
Provides:       tex(german-rgzm.lbx)
Provides:       tex(german-zaak.lbx)
Provides:       tex(german-zaes.lbx)
Provides:       tex(jb-halle.bbx)
Provides:       tex(jb-halle.cbx)
Provides:       tex(jb-kreis-neuss.bbx)
Provides:       tex(jb-kreis-neuss.cbx)
Provides:       tex(karl.bbx)
Provides:       tex(karl.cbx)
Provides:       tex(kunde.bbx)
Provides:       tex(kunde.cbx)
Provides:       tex(maja.bbx)
Provides:       tex(maja.cbx)
Provides:       tex(mpk.bbx)
Provides:       tex(mpk.cbx)
Provides:       tex(mpkoeaw.bbx)
Provides:       tex(mpkoeaw.cbx)
Provides:       tex(naustrian-aefkw.lbx)
Provides:       tex(naustrian-archa.lbx)
Provides:       tex(naustrian-archaeology.lbx)
Provides:       tex(naustrian-dguf-alt.lbx)
Provides:       tex(naustrian-dguf-apa.lbx)
Provides:       tex(naustrian-eaz.lbx)
Provides:       tex(naustrian-foe.lbx)
Provides:       tex(naustrian-jb-kreis-neuss.lbx)
Provides:       tex(naustrian-karl.lbx)
Provides:       tex(naustrian-kunde.lbx)
Provides:       tex(naustrian-maja.lbx)
Provides:       tex(naustrian-mpk.lbx)
Provides:       tex(naustrian-mpkoeaw.lbx)
Provides:       tex(naustrian-niedersachsen.lbx)
Provides:       tex(naustrian-offa.lbx)
Provides:       tex(naustrian-rgzm.lbx)
Provides:       tex(naustrian-zaak.lbx)
Provides:       tex(naustrian-zaes.lbx)
Provides:       tex(newzealand-aefkw.lbx)
Provides:       tex(newzealand-archa.lbx)
Provides:       tex(newzealand-archaeology.lbx)
Provides:       tex(newzealand-dguf-alt.lbx)
Provides:       tex(newzealand-dguf-apa.lbx)
Provides:       tex(newzealand-eaz.lbx)
Provides:       tex(newzealand-foe.lbx)
Provides:       tex(newzealand-jb-kreis-neuss.lbx)
Provides:       tex(newzealand-karl.lbx)
Provides:       tex(newzealand-kunde.lbx)
Provides:       tex(newzealand-maja.lbx)
Provides:       tex(newzealand-mpk.lbx)
Provides:       tex(newzealand-mpkoeaw.lbx)
Provides:       tex(newzealand-niedersachsen.lbx)
Provides:       tex(newzealand-offa.lbx)
Provides:       tex(newzealand-rgzm.lbx)
Provides:       tex(newzealand-zaak.lbx)
Provides:       tex(newzealand-zaes.lbx)
Provides:       tex(ngerman-aefkw.lbx)
Provides:       tex(ngerman-archa.lbx)
Provides:       tex(ngerman-archaeology.lbx)
Provides:       tex(ngerman-dguf-alt.lbx)
Provides:       tex(ngerman-dguf-apa.lbx)
Provides:       tex(ngerman-eaz.lbx)
Provides:       tex(ngerman-foe.lbx)
Provides:       tex(ngerman-jb-kreis-neuss.lbx)
Provides:       tex(ngerman-karl.lbx)
Provides:       tex(ngerman-kunde.lbx)
Provides:       tex(ngerman-maja.lbx)
Provides:       tex(ngerman-mpk.lbx)
Provides:       tex(ngerman-mpkoeaw.lbx)
Provides:       tex(ngerman-niedersachsen.lbx)
Provides:       tex(ngerman-offa.lbx)
Provides:       tex(ngerman-rgzm.lbx)
Provides:       tex(ngerman-zaak.lbx)
Provides:       tex(ngerman-zaes.lbx)
Provides:       tex(niedersachsen.bbx)
Provides:       tex(niedersachsen.cbx)
Provides:       tex(nnu.bbx)
Provides:       tex(nnu.cbx)
Provides:       tex(nswissgerman-aefkw.lbx)
Provides:       tex(nswissgerman-archa.lbx)
Provides:       tex(nswissgerman-archaeology.lbx)
Provides:       tex(nswissgerman-dguf-alt.lbx)
Provides:       tex(nswissgerman-dguf-apa.lbx)
Provides:       tex(nswissgerman-eaz.lbx)
Provides:       tex(nswissgerman-foe.lbx)
Provides:       tex(nswissgerman-jb-kreis-neuss.lbx)
Provides:       tex(nswissgerman-karl.lbx)
Provides:       tex(nswissgerman-kunde.lbx)
Provides:       tex(nswissgerman-maja.lbx)
Provides:       tex(nswissgerman-mpk.lbx)
Provides:       tex(nswissgerman-mpkoeaw.lbx)
Provides:       tex(nswissgerman-niedersachsen.lbx)
Provides:       tex(nswissgerman-offa.lbx)
Provides:       tex(nswissgerman-rgzm.lbx)
Provides:       tex(nswissgerman-zaak.lbx)
Provides:       tex(nswissgerman-zaes.lbx)
Provides:       tex(numeric-comp-archaeology.bbx)
Provides:       tex(numeric-comp-archaeology.cbx)
Provides:       tex(offa.bbx)
Provides:       tex(offa.cbx)
Provides:       tex(rgk-inline-old.bbx)
Provides:       tex(rgk-inline-old.cbx)
Provides:       tex(rgk-inline.bbx)
Provides:       tex(rgk-inline.cbx)
Provides:       tex(rgk-numeric-old.bbx)
Provides:       tex(rgk-numeric-old.cbx)
Provides:       tex(rgk-numeric.bbx)
Provides:       tex(rgk-numeric.cbx)
Provides:       tex(rgk-verbose-old.bbx)
Provides:       tex(rgk-verbose-old.cbx)
Provides:       tex(rgk-verbose.bbx)
Provides:       tex(rgk-verbose.cbx)
Provides:       tex(rgzm-inline.bbx)
Provides:       tex(rgzm-inline.cbx)
Provides:       tex(rgzm-numeric.bbx)
Provides:       tex(rgzm-numeric.cbx)
Provides:       tex(rgzm-verbose.bbx)
Provides:       tex(rgzm-verbose.cbx)
Provides:       tex(swissgerman-aefkw.lbx)
Provides:       tex(swissgerman-archa.lbx)
Provides:       tex(swissgerman-archaeology.lbx)
Provides:       tex(swissgerman-dguf-alt.lbx)
Provides:       tex(swissgerman-dguf-apa.lbx)
Provides:       tex(swissgerman-eaz.lbx)
Provides:       tex(swissgerman-foe.lbx)
Provides:       tex(swissgerman-jb-kreis-neuss.lbx)
Provides:       tex(swissgerman-karl.lbx)
Provides:       tex(swissgerman-kunde.lbx)
Provides:       tex(swissgerman-maja.lbx)
Provides:       tex(swissgerman-mpk.lbx)
Provides:       tex(swissgerman-mpkoeaw.lbx)
Provides:       tex(swissgerman-niedersachsen.lbx)
Provides:       tex(swissgerman-offa.lbx)
Provides:       tex(swissgerman-rgzm.lbx)
Provides:       tex(swissgerman-zaak.lbx)
Provides:       tex(swissgerman-zaes.lbx)
Provides:       tex(ufg-muenster-inline.bbx)
Provides:       tex(ufg-muenster-inline.cbx)
Provides:       tex(ufg-muenster-numeric.bbx)
Provides:       tex(ufg-muenster-numeric.cbx)
Provides:       tex(ufg-muenster-verbose.bbx)
Provides:       tex(ufg-muenster-verbose.cbx)
Provides:       tex(verbose-archaeology.bbx)
Provides:       tex(verbose-archaeology.cbx)
Provides:       tex(verbose-ibid-archaeology.bbx)
Provides:       tex(verbose-ibid-archaeology.cbx)
Provides:       tex(verbose-trad2note-archaeology.bbx)
Provides:       tex(verbose-trad2note-archaeology.cbx)
Provides:       tex(volkskunde.bbx)
Provides:       tex(volkskunde.cbx)
Provides:       tex(zaak.bbx)
Provides:       tex(zaak.cbx)
Provides:       tex(zaes.bbx)
Provides:       tex(zaes.cbx)
Requires:       tex(array.sty)
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear-ibid.bbx)
Requires:       tex(authoryear-ibid.cbx)
Requires:       tex(authoryear-icomp.bbx)
Requires:       tex(authoryear-icomp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(calc.sty)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(tabulary.sty)
Requires:       tex(verbose-ibid.bbx)
Requires:       tex(verbose-ibid.cbx)
Requires:       tex(verbose-trad2.bbx)
Requires:       tex(verbose-trad2.cbx)
Requires:       tex(verbose.bbx)
Requires:       tex(verbose.cbx)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source164:      biblatex-archaeology.tar.xz
Source165:      biblatex-archaeology.doc.tar.xz

%description -n texlive-biblatex-archaeology
This package provides additional BibLaTeX styles for German
humanities. Its core purpose is to enable the referencing rules
of the Romano-Germanic Commission (>Romisch-Germanische
Kommission), the department of prehistory of the German
Archaeological Institute (Deutsches Archaologisches Institut),
since these are referenced by most guidelines in German
prehistory and medieval archaeology and serve as a kind of
template. biblatex-archaeology provides verbose, numeric and
author date styles as well and adaptions to specific document
types like exhibition and auction catalogues.

%package -n texlive-biblatex-archaeology-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn53281
Release:        0
Summary:        Documentation for texlive-biblatex-archaeology
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-archaeology and texlive-alldocumentation)

%description -n texlive-biblatex-archaeology-doc
This package includes the documentation for texlive-biblatex-archaeology

%post -n texlive-biblatex-archaeology
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-archaeology
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-archaeology
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-archaeology-doc
%{_texmfdistdir}/doc/latex/biblatex-archaeology/README.htm
%{_texmfdistdir}/doc/latex/biblatex-archaeology/README.md
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology-example.bib
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology-manual.bib
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology-strings-full-subtitle.bib
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology-strings-full.bib
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology-strings-rgk.bib
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology.conf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/biblatex-archaeology.xml
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/aefkw-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/afwl-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/amit-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/archa-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/authoryear-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/authoryear-comp-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/authoryear-ibid-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/authoryear-icomp-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/biblatex-archaeology_example.tex
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/dguf-alt-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/dguf-apa-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/dguf-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/eaz-alt-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/eaz-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/foe-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/jb-halle-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/jb-kreis-neuss-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/karl-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/kunde-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/maja-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/mpk-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/mpkoeaw-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/niedersachsen-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/nnu-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/numeric-comp-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/offa-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgk-inline-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgk-inline-old-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgk-numeric-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgk-numeric-old-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgk-verbose-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgk-verbose-old-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgzm-inline-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgzm-numeric-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/rgzm-verbose-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/ufg-muenster-inline-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/ufg-muenster-numeric-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/ufg-muenster-verbose-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/verbose-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/verbose-ibid-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/verbose-trad2note-archaeology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/volkskunde-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/zaak-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-archaeology/example/zaes-example.pdf

%files -n texlive-biblatex-archaeology
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/UKenglish-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/USenglish-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/aefkw.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/aefkw.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/aefkw.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/afwl.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/afwl.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/afwl.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/american-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/amit.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/amit.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/amit.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/archa.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/archa.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/archa.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/australian-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/austrian-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-comp-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-comp-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-comp-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-ibid-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-ibid-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-ibid-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-icomp-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-icomp-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/authoryear-icomp-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/biblatex-archaeology.sty
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/british-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/canadian-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf-alt.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf-alt.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf-alt.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf-apa.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf-apa.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf-apa.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/dguf.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/eaz-alt.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/eaz-alt.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/eaz-alt.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/eaz.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/eaz.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/eaz.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/english-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/foe.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/foe.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/foe.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/german-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/jb-halle.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/jb-halle.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/jb-halle.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/jb-kreis-neuss.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/jb-kreis-neuss.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/jb-kreis-neuss.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/karl.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/karl.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/karl.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/kunde.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/kunde.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/kunde.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/maja.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/maja.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/maja.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/mpk.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/mpk.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/mpk.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/mpkoeaw.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/mpkoeaw.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/mpkoeaw.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/naustrian-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/newzealand-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ngerman-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/niedersachsen.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/niedersachsen.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/niedersachsen.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nnu.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nnu.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nnu.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/nswissgerman-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/numeric-comp-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/numeric-comp-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/numeric-comp-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/offa.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/offa.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/offa.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-inline-old.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-inline-old.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-inline-old.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-inline.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-inline.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-inline.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-numeric-old.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-numeric-old.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-numeric-old.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-numeric.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-verbose-old.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-verbose-old.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-verbose-old.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-verbose.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgk-verbose.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-inline.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-inline.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-inline.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-numeric.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-verbose.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/rgzm-verbose.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-aefkw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-archa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-archaeology.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-dguf-alt.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-dguf-apa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-eaz.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-foe.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-jb-kreis-neuss.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-karl.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-kunde.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-maja.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-mpk.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-mpkoeaw.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-niedersachsen.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-offa.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-rgzm.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-zaak.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/swissgerman-zaes.lbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-inline.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-inline.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-inline.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-numeric.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-verbose.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/ufg-muenster-verbose.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-ibid-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-ibid-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-ibid-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-trad2note-archaeology.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-trad2note-archaeology.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/verbose-trad2note-archaeology.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/volkskunde.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/volkskunde.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/volkskunde.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/zaak.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/zaak.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/zaak.dbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/zaes.bbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/zaes.cbx
%{_texmfdistdir}/tex/latex/biblatex-archaeology/zaes.dbx

%package -n texlive-biblatex-arthistory-bonn
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn46637
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX citation style covers the citation and bibliography guidelines for art historians
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-arthistory-bonn-doc >= %{texlive_version}
Provides:       tex(arthistory-bonn-english.lbx)
Provides:       tex(arthistory-bonn-german.lbx)
Provides:       tex(arthistory-bonn.bbx)
Provides:       tex(arthistory-bonn.cbx)
Requires:       tex(authoryear-ibid.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(csquotes.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source166:      biblatex-arthistory-bonn.tar.xz
Source167:      biblatex-arthistory-bonn.doc.tar.xz

%description -n texlive-biblatex-arthistory-bonn
This citation style covers the citation and bibliography
guidelines of the Kunsthistorisches Institut der Universitat
Bonn for undergraduates. It introduces bibliography entry types
for catalogs and features a tabular bibliography, among other
things. Various options are available to change and adjust the
outcome according to one's own preferences. The style is
compatible with English and German.

%package -n texlive-biblatex-arthistory-bonn-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn46637
Release:        0
Summary:        Documentation for texlive-biblatex-arthistory-bonn
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-arthistory-bonn and texlive-alldocumentation)

%description -n texlive-biblatex-arthistory-bonn-doc
This package includes the documentation for texlive-biblatex-arthistory-bonn

%post -n texlive-biblatex-arthistory-bonn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-arthistory-bonn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-arthistory-bonn
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-arthistory-bonn-doc
%{_texmfdistdir}/doc/latex/biblatex-arthistory-bonn/README.md
%{_texmfdistdir}/doc/latex/biblatex-arthistory-bonn/arthistory-bonn-examples.bib
%{_texmfdistdir}/doc/latex/biblatex-arthistory-bonn/arthistory-bonn.pdf
%{_texmfdistdir}/doc/latex/biblatex-arthistory-bonn/arthistory-bonn.tex

%files -n texlive-biblatex-arthistory-bonn
%{_texmfdistdir}/tex/latex/biblatex-arthistory-bonn/arthistory-bonn-english.lbx
%{_texmfdistdir}/tex/latex/biblatex-arthistory-bonn/arthistory-bonn-german.lbx
%{_texmfdistdir}/tex/latex/biblatex-arthistory-bonn/arthistory-bonn.bbx
%{_texmfdistdir}/tex/latex/biblatex-arthistory-bonn/arthistory-bonn.cbx
%{_texmfdistdir}/tex/latex/biblatex-arthistory-bonn/arthistory-bonn.dbx

%package -n texlive-biblatex-bath
Version:        %{texlive_version}.%{texlive_noarch}.6.0svn63401
Release:        0
License:        LPPL-1.0
Summary:        Harvard referencing style as recommended by the University of Bath Library
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-bath-doc >= %{texlive_version}
Provides:       tex(bath.bbx)
Provides:       tex(bath.cbx)
Provides:       tex(british-bath.lbx)
Provides:       tex(english-bath.lbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(etoolbox.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source168:      biblatex-bath.tar.xz
Source169:      biblatex-bath.doc.tar.xz

%description -n texlive-biblatex-bath
This package provides a BibLaTeX style to format reference
lists in the Harvard style recommended by the University of
Bath Library.

%package -n texlive-biblatex-bath-doc
Version:        %{texlive_version}.%{texlive_noarch}.6.0svn63401
Release:        0
Summary:        Documentation for texlive-biblatex-bath
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-bath and texlive-alldocumentation)

%description -n texlive-biblatex-bath-doc
This package includes the documentation for texlive-biblatex-bath

%post -n texlive-biblatex-bath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-bath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-bath
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-bath-doc
%{_texmfdistdir}/doc/latex/biblatex-bath/README.md
%{_texmfdistdir}/doc/latex/biblatex-bath/biblatex-bath.bib
%{_texmfdistdir}/doc/latex/biblatex-bath/biblatex-bath.pdf

%files -n texlive-biblatex-bath
%{_texmfdistdir}/tex/latex/biblatex-bath/bath.bbx
%{_texmfdistdir}/tex/latex/biblatex-bath/bath.cbx
%{_texmfdistdir}/tex/latex/biblatex-bath/bath.dbx
%{_texmfdistdir}/tex/latex/biblatex-bath/british-bath.lbx
%{_texmfdistdir}/tex/latex/biblatex-bath/english-bath.lbx

%package -n texlive-biblatex-bookinarticle
Version:        %{texlive_version}.%{texlive_noarch}.1.3.1asvn40323
Release:        0
License:        LPPL-1.0
Summary:        Manage book edited in article
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-bookinarticle-doc >= %{texlive_version}
Provides:       tex(biblatex-bookinarticle.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source170:      biblatex-bookinarticle.tar.xz
Source171:      biblatex-bookinarticle.doc.tar.xz

%description -n texlive-biblatex-bookinarticle
This package provides three new BibLaTeX entry types -
@bookinarticle, @bookinincollection and @bookinthesis - to
refer to a modern edition of an old book, where this modern
edition is provided in a @article, @incollection or in a
@thesis. The package is now superseded by biblatex-bookinother.

%package -n texlive-biblatex-bookinarticle-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.1asvn40323
Release:        0
Summary:        Documentation for texlive-biblatex-bookinarticle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-bookinarticle and texlive-alldocumentation)

%description -n texlive-biblatex-bookinarticle-doc
This package includes the documentation for texlive-biblatex-bookinarticle

%post -n texlive-biblatex-bookinarticle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-bookinarticle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-bookinarticle
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-bookinarticle-doc
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/README
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle-crossref.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle.tex
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/example-bookinarticle.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/example-bookinincollection.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/example-bookinthesis.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/documentation/makefile
%{_texmfdistdir}/doc/latex/biblatex-bookinarticle/makefile

%files -n texlive-biblatex-bookinarticle
%{_texmfdistdir}/tex/latex/biblatex-bookinarticle/biblatex-bookinarticle.sty

%package -n texlive-biblatex-bookinother
Version:        %{texlive_version}.%{texlive_noarch}.2.3.3svn54015
Release:        0
License:        LPPL-1.0
Summary:        Manage book edited in other entry type
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-bookinother-doc >= %{texlive_version}
Provides:       tex(bookinother.bbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source172:      biblatex-bookinother.tar.xz
Source173:      biblatex-bookinother.doc.tar.xz

%description -n texlive-biblatex-bookinother
This package provides new BibLaTeX entry types and fields for
book edited in other types, like for instance @bookinarticle.
It offers more types than the older package
biblatex-bookinarticle which it superseeds.

%package -n texlive-biblatex-bookinother-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3.3svn54015
Release:        0
Summary:        Documentation for texlive-biblatex-bookinother
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-bookinother and texlive-alldocumentation)

%description -n texlive-biblatex-bookinother-doc
This package includes the documentation for texlive-biblatex-bookinother

%post -n texlive-biblatex-bookinother
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-bookinother
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-bookinother
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-bookinother-doc
%{_texmfdistdir}/doc/latex/biblatex-bookinother/README
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/biblatex-bookinother.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/biblatex-bookinother.tex
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinarticle.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinarticle.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinarticle.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookincollection.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookincollection.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookincollection.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininarticle.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininarticle.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininarticle.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininbook.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininbook.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininbook.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinincollection.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinincollection.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinincollection.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininproceedings.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininproceedings.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookininproceedings.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinjournal.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinjournal.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinjournal.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinproceedings.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinproceedings.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinproceedings.pdf
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinthesis.bib
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinthesis.dot
%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/example-bookinthesis.pdf

%files -n texlive-biblatex-bookinother
%{_texmfdistdir}/tex/latex/biblatex-bookinother/bookinother.bbx
%{_texmfdistdir}/tex/latex/biblatex-bookinother/bookinother.dbx

%package -n texlive-biblatex-bwl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn26556
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX citations for FU Berlin
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-bwl-doc >= %{texlive_version}
Provides:       tex(bwl-FU.bbx)
Provides:       tex(bwl-FU.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source174:      biblatex-bwl.tar.xz
Source175:      biblatex-bwl.doc.tar.xz

%description -n texlive-biblatex-bwl
The bundle provides a set of BibLaTeX implementations of
bibliography and citation styles for the Business
Administration Department of the Free University of Berlin.

%package -n texlive-biblatex-bwl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.02svn26556
Release:        0
Summary:        Documentation for texlive-biblatex-bwl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-bwl and texlive-alldocumentation)

%description -n texlive-biblatex-bwl-doc
This package includes the documentation for texlive-biblatex-bwl

%post -n texlive-biblatex-bwl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-bwl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-bwl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-bwl-doc
%{_texmfdistdir}/doc/latex/biblatex-bwl/Changes
%{_texmfdistdir}/doc/latex/biblatex-bwl/doc/bwl-FU.bib
%{_texmfdistdir}/doc/latex/biblatex-bwl/doc/bwl-FU.pdf
%{_texmfdistdir}/doc/latex/biblatex-bwl/doc/bwl-FU.tex

%files -n texlive-biblatex-bwl
%{_texmfdistdir}/tex/latex/biblatex-bwl/bwl-FU.bbx
%{_texmfdistdir}/tex/latex/biblatex-bwl/bwl-FU.cbx

%package -n texlive-biblatex-caspervector
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.7svn70491
Release:        0
License:        LPPL-1.0
Summary:        A simple citation style for Chinese users
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-caspervector-doc >= %{texlive_version}
Provides:       tex(blx-caspervector-base.def)
Provides:       tex(blx-caspervector-gbk.def)
Provides:       tex(blx-caspervector-utf8.def)
Provides:       tex(caspervector-ay.bbx)
Provides:       tex(caspervector-ay.cbx)
Provides:       tex(caspervector.bbx)
Provides:       tex(caspervector.cbx)
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source176:      biblatex-caspervector.tar.xz
Source177:      biblatex-caspervector.doc.tar.xz

%description -n texlive-biblatex-caspervector
The package provides a simple and easily extensible
biblography/citation style for Chinese LaTeX users, using
BibLaTeX.

%package -n texlive-biblatex-caspervector-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.7svn70491
Release:        0
Summary:        Documentation for texlive-biblatex-caspervector
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-caspervector and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-caspervector-doc:zh)

%description -n texlive-biblatex-caspervector-doc
This package includes the documentation for texlive-biblatex-caspervector

%post -n texlive-biblatex-caspervector
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-caspervector
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-caspervector
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-caspervector-doc
%{_texmfdistdir}/doc/latex/biblatex-caspervector/ChangeLog.txt
%{_texmfdistdir}/doc/latex/biblatex-caspervector/README.txt
%{_texmfdistdir}/doc/latex/biblatex-caspervector/caspervector-ay.pdf
%{_texmfdistdir}/doc/latex/biblatex-caspervector/caspervector-ay.tex
%{_texmfdistdir}/doc/latex/biblatex-caspervector/caspervector.bib
%{_texmfdistdir}/doc/latex/biblatex-caspervector/caspervector.pdf
%{_texmfdistdir}/doc/latex/biblatex-caspervector/caspervector.tex
%{_texmfdistdir}/doc/latex/biblatex-caspervector/latexmkrc

%files -n texlive-biblatex-caspervector
%{_texmfdistdir}/tex/latex/biblatex-caspervector/blx-caspervector-base.def
%{_texmfdistdir}/tex/latex/biblatex-caspervector/blx-caspervector-gbk.def
%{_texmfdistdir}/tex/latex/biblatex-caspervector/blx-caspervector-utf8.def
%{_texmfdistdir}/tex/latex/biblatex-caspervector/caspervector-ay.bbx
%{_texmfdistdir}/tex/latex/biblatex-caspervector/caspervector-ay.cbx
%{_texmfdistdir}/tex/latex/biblatex-caspervector/caspervector.bbx
%{_texmfdistdir}/tex/latex/biblatex-caspervector/caspervector.cbx

%package -n texlive-biblatex-cheatsheet
Version:        %{texlive_version}.%{texlive_noarch}.svn44685
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX/Biber 'cheat sheet'
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source178:      biblatex-cheatsheet.doc.tar.xz

%description -n texlive-biblatex-cheatsheet
A BibLaTeX/Biber 'cheat sheet' which I wrote because I wanted
one to distribute to students, but couldn't find an existing
one.

%post -n texlive-biblatex-cheatsheet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-cheatsheet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-cheatsheet
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-cheatsheet
%{_texmfdistdir}/doc/latex/biblatex-cheatsheet/README
%{_texmfdistdir}/doc/latex/biblatex-cheatsheet/biblatex-cheatsheet.pdf
%{_texmfdistdir}/doc/latex/biblatex-cheatsheet/biblatex-cheatsheet.tex

%package -n texlive-biblatex-chem
Version:        %{texlive_version}.%{texlive_noarch}.1.1zsvn57904
Release:        0
License:        LPPL-1.0
Summary:        A set of BibLaTeX implementations of chemistry-related bibliography styles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-chem-doc >= %{texlive_version}
Provides:       tex(chem-acs.bbx)
Provides:       tex(chem-acs.cbx)
Provides:       tex(chem-angew.bbx)
Provides:       tex(chem-angew.cbx)
Provides:       tex(chem-biochem.bbx)
Provides:       tex(chem-biochem.cbx)
Provides:       tex(chem-rsc.bbx)
Provides:       tex(chem-rsc.cbx)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source179:      biblatex-chem.tar.xz
Source180:      biblatex-chem.doc.tar.xz

%description -n texlive-biblatex-chem
The bundle offers a set of styles to allow chemists to use
BibLaTeX. The package has complete styles for: all ACS
journals; RSC journals using standard (Chem. Commun.) style;
and Angewandte Chem. style, (thus covering a wide range of
journals). A comprehensive set of examples of use is included.

%package -n texlive-biblatex-chem-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1zsvn57904
Release:        0
Summary:        Documentation for texlive-biblatex-chem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-chem and texlive-alldocumentation)

%description -n texlive-biblatex-chem-doc
This package includes the documentation for texlive-biblatex-chem

%post -n texlive-biblatex-chem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-chem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-chem
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-chem-doc
%{_texmfdistdir}/doc/latex/biblatex-chem/README.md
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-acs.pdf
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-acs.tex
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-angew.pdf
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-angew.tex
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-biochem.pdf
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-biochem.tex
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-rsc.pdf
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem-rsc.tex
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem.bib
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem.pdf
%{_texmfdistdir}/doc/latex/biblatex-chem/biblatex-chem.tex

%files -n texlive-biblatex-chem
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-acs.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-acs.cbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-angew.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-angew.cbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-biochem.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-biochem.cbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-rsc.bbx
%{_texmfdistdir}/tex/latex/biblatex-chem/chem-rsc.cbx

%package -n texlive-biblatex-chicago
Version:        %{texlive_version}.%{texlive_noarch}.2.3asvn65037
Release:        0
License:        LPPL-1.0
Summary:        Chicago style files for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-chicago-doc >= %{texlive_version}
Provides:       tex(biblatex-chicago.sty)
Provides:       tex(chicago-authordate-trad.bbx)
Provides:       tex(chicago-authordate-trad.cbx)
Provides:       tex(chicago-authordate-trad16.bbx)
Provides:       tex(chicago-authordate-trad16.cbx)
Provides:       tex(chicago-authordate.bbx)
Provides:       tex(chicago-authordate.cbx)
Provides:       tex(chicago-authordate16.bbx)
Provides:       tex(chicago-authordate16.cbx)
Provides:       tex(chicago-dates-common.cbx)
Provides:       tex(chicago-dates-common16.cbx)
Provides:       tex(chicago-notes.bbx)
Provides:       tex(chicago-notes.cbx)
Provides:       tex(chicago-notes16.bbx)
Provides:       tex(chicago-notes16.cbx)
Provides:       tex(cms-american.lbx)
Provides:       tex(cms-brazilian.lbx)
Provides:       tex(cms-british.lbx)
Provides:       tex(cms-dutch.lbx)
Provides:       tex(cms-finnish.lbx)
Provides:       tex(cms-french.lbx)
Provides:       tex(cms-german.lbx)
Provides:       tex(cms-icelandic.lbx)
Provides:       tex(cms-ngerman.lbx)
Provides:       tex(cms-norsk.lbx)
Provides:       tex(cms-norwegian.lbx)
Provides:       tex(cms-nynorsk.lbx)
Provides:       tex(cms-romanian.lbx)
Provides:       tex(cms-spanish.lbx)
Provides:       tex(cms-swedish.lbx)
Provides:       tex(cmsdocs.sty)
Provides:       tex(cmsendnotes.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(endnotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(nameref.sty)
Requires:       tex(refcount.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source181:      biblatex-chicago.tar.xz
Source182:      biblatex-chicago.doc.tar.xz

%description -n texlive-biblatex-chicago
This is a BibLaTeX style that implements the Chicago
'author-date' and 'notes with bibliography' style
specifications given in the Chicago Manual of Style, 17th
edition (with continuing support for the 16th edition, too).
The style implements entry types for citing audio-visual
materials, among many others. The package was previously known
as biblatex-chicago-notes-df.

%package -n texlive-biblatex-chicago-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3asvn65037
Release:        0
Summary:        Documentation for texlive-biblatex-chicago
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-chicago and texlive-alldocumentation)

%description -n texlive-biblatex-chicago-doc
This package includes the documentation for texlive-biblatex-chicago

%post -n texlive-biblatex-chicago
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-chicago
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-chicago
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-chicago-doc
%{_texmfdistdir}/doc/latex/biblatex-chicago/README
%{_texmfdistdir}/doc/latex/biblatex-chicago/RELEASE
%{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/biblatex-chicago.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-intro.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-intro.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-sample.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-dates-sample.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-legal-sample.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-legal-sample.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-noteref-demo.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-noteref-demo.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-intro.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-intro.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-sample.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-notes-sample.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-trad-appendix.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-trad-appendix.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-trad-sample.pdf
%{_texmfdistdir}/doc/latex/biblatex-chicago/cms-trad-sample.tex
%{_texmfdistdir}/doc/latex/biblatex-chicago/dates-test.bib
%{_texmfdistdir}/doc/latex/biblatex-chicago/legal-test.bib
%{_texmfdistdir}/doc/latex/biblatex-chicago/notes-test.bib

%files -n texlive-biblatex-chicago
%{_texmfdistdir}/tex/latex/biblatex-chicago/biblatex-chicago.sty
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate-trad.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate-trad.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate-trad16.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate-trad16.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate16.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-authordate16.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-dates-common.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-dates-common16.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes16.bbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/chicago-notes16.cbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-american.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-brazilian.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-british.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-dutch.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-finnish.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-french.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-german.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-icelandic.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-ngerman.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-norsk.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-norwegian.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-nynorsk.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-romanian.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-spanish.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms-swedish.lbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cms.dbx
%{_texmfdistdir}/tex/latex/biblatex-chicago/cmsdocs.sty
%{_texmfdistdir}/tex/latex/biblatex-chicago/cmsendnotes.sty

%package -n texlive-biblatex-claves
Version:        %{texlive_version}.%{texlive_noarch}.1.2.1svn43723
Release:        0
License:        LPPL-1.0
Summary:        A tool to manage claves of old litterature with BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-claves-doc >= %{texlive_version}
Provides:       tex(claves.bbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source183:      biblatex-claves.tar.xz
Source184:      biblatex-claves.doc.tar.xz

%description -n texlive-biblatex-claves
When studying antic and medieval literature, we may find many
different texts published with the same title, or, in contrary,
the same text published with different titles. To avoid
confusion, scholars have published claves, which are books
listing ancient texts, identifying them by an identifier -- a
number or a string of text. For example, for early
Christianity, we have the Bibliotheca Hagiographica Graeca, the
Clavis Apocryphorum Novi Testamenti and other claves. It could
be useful to print the identifier of a texts in one specific
clavis, or in many claves. The package allows us to create new
field for different claves, and to present all these fields in
a consistent way.

%package -n texlive-biblatex-claves-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2.1svn43723
Release:        0
Summary:        Documentation for texlive-biblatex-claves
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-claves and texlive-alldocumentation)

%description -n texlive-biblatex-claves-doc
This package includes the documentation for texlive-biblatex-claves

%post -n texlive-biblatex-claves
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-claves
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-claves
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-claves-doc
%{_texmfdistdir}/doc/latex/biblatex-claves/README
%{_texmfdistdir}/doc/latex/biblatex-claves/documentation/biblatex-claves-ref.bib
%{_texmfdistdir}/doc/latex/biblatex-claves/documentation/biblatex-claves.bib
%{_texmfdistdir}/doc/latex/biblatex-claves/documentation/biblatex-claves.pdf
%{_texmfdistdir}/doc/latex/biblatex-claves/documentation/biblatex-claves.tex
%{_texmfdistdir}/doc/latex/biblatex-claves/documentation/latexmkrc
%{_texmfdistdir}/doc/latex/biblatex-claves/documentation/makefile
%{_texmfdistdir}/doc/latex/biblatex-claves/makefile

%files -n texlive-biblatex-claves
%{_texmfdistdir}/tex/latex/biblatex-claves/claves.bbx
%{_texmfdistdir}/tex/latex/biblatex-claves/claves.dbx

%package -n texlive-biblatex-cv
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn59433
Release:        0
License:        LPPL-1.0
Summary:        Create a CV from BibTeX files
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-cv-doc >= %{texlive_version}
Provides:       tex(american-cv.lbx)
Provides:       tex(biblatex-cv.bbx)
Provides:       tex(biblatex-cv.cbx)
Provides:       tex(biblatex-cv.sty)
Requires:       tex(american.lbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(biblatex.sty)
Requires:       tex(datenumber.sty)
Requires:       tex(expl3.sty)
Requires:       tex(fp.sty)
Requires:       tex(totcount.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source185:      biblatex-cv.tar.xz
Source186:      biblatex-cv.doc.tar.xz

%description -n texlive-biblatex-cv
This package creates an academic curriculum vitae (CV) from a
BibTeX .bib file. The package makes use of BibLaTeX/biber to
automatically format, group, and sort the entries on a CV.

%package -n texlive-biblatex-cv-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn59433
Release:        0
Summary:        Documentation for texlive-biblatex-cv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-cv and texlive-alldocumentation)

%description -n texlive-biblatex-cv-doc
This package includes the documentation for texlive-biblatex-cv

%post -n texlive-biblatex-cv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-cv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-cv
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-cv-doc
%{_texmfdistdir}/doc/latex/biblatex-cv/README.md
%{_texmfdistdir}/doc/latex/biblatex-cv/biblatex-cv.bib
%{_texmfdistdir}/doc/latex/biblatex-cv/biblatex-cv.pdf
%{_texmfdistdir}/doc/latex/biblatex-cv/biblatex-cv.tex
%{_texmfdistdir}/doc/latex/biblatex-cv/cv.pdf
%{_texmfdistdir}/doc/latex/biblatex-cv/cv.tex

%files -n texlive-biblatex-cv
%{_texmfdistdir}/tex/latex/biblatex-cv/american-cv.lbx
%{_texmfdistdir}/tex/latex/biblatex-cv/biblatex-cv.bbx
%{_texmfdistdir}/tex/latex/biblatex-cv/biblatex-cv.cbx
%{_texmfdistdir}/tex/latex/biblatex-cv/biblatex-cv.dbx
%{_texmfdistdir}/tex/latex/biblatex-cv/biblatex-cv.sty

%package -n texlive-biblatex-dw
Version:        %{texlive_version}.%{texlive_noarch}.1.7bsvn66579
Release:        0
License:        LPPL-1.0
Summary:        Humanities styles for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-dw-doc >= %{texlive_version}
Provides:       tex(authortitle-dw.bbx)
Provides:       tex(authortitle-dw.cbx)
Provides:       tex(english-dw.lbx)
Provides:       tex(footnote-dw.bbx)
Provides:       tex(footnote-dw.cbx)
Provides:       tex(german-dw.lbx)
Provides:       tex(standard-dw.bbx)
Provides:       tex(standard-dw.cbx)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source187:      biblatex-dw.tar.xz
Source188:      biblatex-dw.doc.tar.xz

%description -n texlive-biblatex-dw
A small collection of styles for the BibLaTeX package. It was
designed for citations in the humanities and offers some
features that are not provided by the standard BibLaTeX styles.
The styles are dependent on BibLaTeX (at least version 0.9b)
and cannot be used without it. Eine kleine Sammlung von Stilen
fur das Paket BibLaTeX. Es ist auf geisteswissenschaftliche
Zitierweise zugeschnitten und bietet einige Funktionen, die von
den Standard-Stilen von BibLaTeX nicht direkt bereitgestellt
werden. Das Paket baut vollstandig auf BibLaTeX auf und kann
nicht ohne BibLaTeX (mindestens in der Version 0.9b) verwendet
werden.

%package -n texlive-biblatex-dw-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7bsvn66579
Release:        0
Summary:        Documentation for texlive-biblatex-dw
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-dw and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-dw-doc:de;en)

%description -n texlive-biblatex-dw-doc
This package includes the documentation for texlive-biblatex-dw

%post -n texlive-biblatex-dw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-dw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-dw
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-dw-doc
%{_texmfdistdir}/doc/latex/biblatex-dw/CHANGES
%{_texmfdistdir}/doc/latex/biblatex-dw/LIESMICH
%{_texmfdistdir}/doc/latex/biblatex-dw/README
%{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw-preamble.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw-print.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw-screen.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw.pdf
%{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/de-biblatex-dw.pdf
%{_texmfdistdir}/doc/latex/biblatex-dw/de-biblatex-dw.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-authortitle-dw.pdf
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-authortitle-dw.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-examples-dw.bib
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-footnote-dw.pdf
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-footnote-dw.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-authortitle-dw.pdf
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-authortitle-dw.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-footnote-dw.pdf
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-footnote-dw.tex
%{_texmfdistdir}/doc/latex/biblatex-dw/examples/examples-dw.bib

%files -n texlive-biblatex-dw
%{_texmfdistdir}/tex/latex/biblatex-dw/bbx/authortitle-dw.bbx
%{_texmfdistdir}/tex/latex/biblatex-dw/bbx/footnote-dw.bbx
%{_texmfdistdir}/tex/latex/biblatex-dw/bbx/standard-dw.bbx
%{_texmfdistdir}/tex/latex/biblatex-dw/cbx/authortitle-dw.cbx
%{_texmfdistdir}/tex/latex/biblatex-dw/cbx/footnote-dw.cbx
%{_texmfdistdir}/tex/latex/biblatex-dw/cbx/standard-dw.cbx
%{_texmfdistdir}/tex/latex/biblatex-dw/lbx/english-dw.lbx
%{_texmfdistdir}/tex/latex/biblatex-dw/lbx/german-dw.lbx

%package -n texlive-biblatex-enc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn44627
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX style for the Ecole nationale des chartes (Paris)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-enc-doc >= %{texlive_version}
Provides:       tex(enc.bbx)
Provides:       tex(enc.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source189:      biblatex-enc.tar.xz
Source190:      biblatex-enc.doc.tar.xz

%description -n texlive-biblatex-enc
This package provides a citation and bibliography style for use
with BibLaTeX. It conforms to the bibliographic standards used
at the Ecole nationale des chartes (Paris), and may be suitable
for a more general use in historical and philological works.
The package was initially derived from historische-zeitschrift,
with the necessary modifications.

%package -n texlive-biblatex-enc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn44627
Release:        0
Summary:        Documentation for texlive-biblatex-enc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-enc and texlive-alldocumentation)

%description -n texlive-biblatex-enc-doc
This package includes the documentation for texlive-biblatex-enc

%post -n texlive-biblatex-enc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-enc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-enc
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-enc-doc
%{_texmfdistdir}/doc/latex/biblatex-enc/README

%files -n texlive-biblatex-enc
%{_texmfdistdir}/tex/latex/biblatex-enc/enc.bbx
%{_texmfdistdir}/tex/latex/biblatex-enc/enc.cbx

%package -n texlive-biblatex-ext
Version:        %{texlive_version}.%{texlive_noarch}.0.0.17svn66641
Release:        0
License:        LPPL-1.0
Summary:        Extended BibLaTeX standard styles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-ext-doc >= %{texlive_version}
Provides:       tex(biblatex-ext-oa-doiapi.sty)
Provides:       tex(biblatex-ext-oa.sty)
Provides:       tex(biblatex-ext-oasymb-l3draw.sty)
Provides:       tex(biblatex-ext-oasymb-pict2e.sty)
Provides:       tex(biblatex-ext-oasymb-tikz.sty)
Provides:       tex(biblatex-ext-tabular.sty)
Provides:       tex(ext-alphabetic-verb.bbx)
Provides:       tex(ext-alphabetic-verb.cbx)
Provides:       tex(ext-alphabetic.bbx)
Provides:       tex(ext-alphabetic.cbx)
Provides:       tex(ext-authornumber-comp.bbx)
Provides:       tex(ext-authornumber-comp.cbx)
Provides:       tex(ext-authornumber-ecomp.bbx)
Provides:       tex(ext-authornumber-ecomp.cbx)
Provides:       tex(ext-authornumber-tcomp.bbx)
Provides:       tex(ext-authornumber-tcomp.cbx)
Provides:       tex(ext-authornumber-tecomp.bbx)
Provides:       tex(ext-authornumber-tecomp.cbx)
Provides:       tex(ext-authornumber-terse.bbx)
Provides:       tex(ext-authornumber-terse.cbx)
Provides:       tex(ext-authornumber.bbx)
Provides:       tex(ext-authornumber.cbx)
Provides:       tex(ext-authortitle-common.bbx)
Provides:       tex(ext-authortitle-comp.bbx)
Provides:       tex(ext-authortitle-comp.cbx)
Provides:       tex(ext-authortitle-ibid.bbx)
Provides:       tex(ext-authortitle-ibid.cbx)
Provides:       tex(ext-authortitle-icomp.bbx)
Provides:       tex(ext-authortitle-icomp.cbx)
Provides:       tex(ext-authortitle-tcomp.bbx)
Provides:       tex(ext-authortitle-tcomp.cbx)
Provides:       tex(ext-authortitle-terse.bbx)
Provides:       tex(ext-authortitle-terse.cbx)
Provides:       tex(ext-authortitle-ticomp.bbx)
Provides:       tex(ext-authortitle-ticomp.cbx)
Provides:       tex(ext-authortitle.bbx)
Provides:       tex(ext-authortitle.cbx)
Provides:       tex(ext-authoryear-common.bbx)
Provides:       tex(ext-authoryear-comp.bbx)
Provides:       tex(ext-authoryear-comp.cbx)
Provides:       tex(ext-authoryear-ecomp.bbx)
Provides:       tex(ext-authoryear-ecomp.cbx)
Provides:       tex(ext-authoryear-ibid.bbx)
Provides:       tex(ext-authoryear-ibid.cbx)
Provides:       tex(ext-authoryear-icomp.bbx)
Provides:       tex(ext-authoryear-icomp.cbx)
Provides:       tex(ext-authoryear-iecomp.bbx)
Provides:       tex(ext-authoryear-iecomp.cbx)
Provides:       tex(ext-authoryear-tcomp.bbx)
Provides:       tex(ext-authoryear-tcomp.cbx)
Provides:       tex(ext-authoryear-tecomp.bbx)
Provides:       tex(ext-authoryear-tecomp.cbx)
Provides:       tex(ext-authoryear-terse.bbx)
Provides:       tex(ext-authoryear-terse.cbx)
Provides:       tex(ext-authoryear-ticomp.bbx)
Provides:       tex(ext-authoryear-ticomp.cbx)
Provides:       tex(ext-authoryear-tiecomp.bbx)
Provides:       tex(ext-authoryear-tiecomp.cbx)
Provides:       tex(ext-authoryear.bbx)
Provides:       tex(ext-authoryear.cbx)
Provides:       tex(ext-biblatex-aux.def)
Provides:       tex(ext-dashed-common.bbx)
Provides:       tex(ext-numeric-comp.bbx)
Provides:       tex(ext-numeric-comp.cbx)
Provides:       tex(ext-numeric-verb.bbx)
Provides:       tex(ext-numeric-verb.cbx)
Provides:       tex(ext-numeric.bbx)
Provides:       tex(ext-numeric.cbx)
Provides:       tex(ext-standard.bbx)
Provides:       tex(ext-verbose-common.cbx)
Provides:       tex(ext-verbose-ibid.bbx)
Provides:       tex(ext-verbose-ibid.cbx)
Provides:       tex(ext-verbose-inote.bbx)
Provides:       tex(ext-verbose-inote.cbx)
Provides:       tex(ext-verbose-note-common.cbx)
Provides:       tex(ext-verbose-note.bbx)
Provides:       tex(ext-verbose-note.cbx)
Provides:       tex(ext-verbose-trad1.bbx)
Provides:       tex(ext-verbose-trad1.cbx)
Provides:       tex(ext-verbose-trad2.bbx)
Provides:       tex(ext-verbose-trad2.cbx)
Provides:       tex(ext-verbose-trad3.bbx)
Provides:       tex(ext-verbose-trad3.cbx)
Provides:       tex(ext-verbose.bbx)
Provides:       tex(ext-verbose.cbx)
Requires:       tex(alphabetic-verb.bbx)
Requires:       tex(alphabetic-verb.cbx)
Requires:       tex(alphabetic.bbx)
Requires:       tex(alphabetic.cbx)
Requires:       tex(authortitle-comp.bbx)
Requires:       tex(authortitle-comp.cbx)
Requires:       tex(authortitle-ibid.bbx)
Requires:       tex(authortitle-ibid.cbx)
Requires:       tex(authortitle-icomp.bbx)
Requires:       tex(authortitle-icomp.cbx)
Requires:       tex(authortitle-tcomp.bbx)
Requires:       tex(authortitle-terse.bbx)
Requires:       tex(authortitle-ticomp.bbx)
Requires:       tex(authortitle.bbx)
Requires:       tex(authortitle.cbx)
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear-ibid.bbx)
Requires:       tex(authoryear-ibid.cbx)
Requires:       tex(authoryear-icomp.bbx)
Requires:       tex(authoryear-icomp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(biblatex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(l3draw.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(numeric-verb.bbx)
Requires:       tex(numeric-verb.cbx)
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
Requires:       tex(pict2e.sty)
Requires:       tex(standard.bbx)
Requires:       tex(tikz.sty)
Requires:       tex(verbose-ibid.bbx)
Requires:       tex(verbose-ibid.cbx)
Requires:       tex(verbose-inote.bbx)
Requires:       tex(verbose-inote.cbx)
Requires:       tex(verbose-note.bbx)
Requires:       tex(verbose-note.cbx)
Requires:       tex(verbose-trad1.bbx)
Requires:       tex(verbose-trad1.cbx)
Requires:       tex(verbose-trad2.bbx)
Requires:       tex(verbose-trad2.cbx)
Requires:       tex(verbose-trad3.bbx)
Requires:       tex(verbose-trad3.cbx)
Requires:       tex(verbose.bbx)
Requires:       tex(verbose.cbx)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source191:      biblatex-ext.tar.xz
Source192:      biblatex-ext.doc.tar.xz

%description -n texlive-biblatex-ext
The BibLaTeX-ext bundle provides styles that slightly extend
the standard styles that ship with BibLaTeX. The styles offered
in this bundle provide a simple interface to change some of the
stylistic decisions made in the standard styles. At the same
time they stay as close to their standard counterparts as
possible, so that most customisation methods can be applied
here as well.

%package -n texlive-biblatex-ext-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.17svn66641
Release:        0
Summary:        Documentation for texlive-biblatex-ext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-ext and texlive-alldocumentation)

%description -n texlive-biblatex-ext-doc
This package includes the documentation for texlive-biblatex-ext

%post -n texlive-biblatex-ext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-ext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-ext
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-ext-doc
%{_texmfdistdir}/doc/latex/biblatex-ext/CHANGES.md
%{_texmfdistdir}/doc/latex/biblatex-ext/README.md
%{_texmfdistdir}/doc/latex/biblatex-ext/biblatex-ext-examples.bib
%{_texmfdistdir}/doc/latex/biblatex-ext/biblatex-ext.pdf
%{_texmfdistdir}/doc/latex/biblatex-ext/biblatex-ext.tex

%files -n texlive-biblatex-ext
%{_texmfdistdir}/tex/latex/biblatex-ext/biblatex-ext-oa-doiapi.sty
%{_texmfdistdir}/tex/latex/biblatex-ext/biblatex-ext-oa.sty
%{_texmfdistdir}/tex/latex/biblatex-ext/biblatex-ext-oasymb-l3draw.sty
%{_texmfdistdir}/tex/latex/biblatex-ext/biblatex-ext-oasymb-pict2e.sty
%{_texmfdistdir}/tex/latex/biblatex-ext/biblatex-ext-oasymb-tikz.sty
%{_texmfdistdir}/tex/latex/biblatex-ext/biblatex-ext-tabular.sty
%{_texmfdistdir}/tex/latex/biblatex-ext/blxextdoiapi.lua
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-alphabetic-verb.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-alphabetic-verb.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-ecomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-ecomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-tcomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-tcomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-tecomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-tecomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-terse.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber-terse.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authornumber.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-common.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-icomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-icomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-tcomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-tcomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-terse.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-terse.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-ticomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle-ticomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authortitle.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-common.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-ecomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-ecomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-icomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-icomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-iecomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-iecomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-tcomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-tcomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-tecomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-tecomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-terse.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-terse.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-ticomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-ticomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-tiecomp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear-tiecomp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-authoryear.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-biblatex-aux.def
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-dashed-common.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-numeric-comp.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-numeric-comp.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-numeric-verb.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-numeric-verb.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-standard.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-common.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-inote.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-inote.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-note-common.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-note.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-note.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-trad1.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-trad1.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-trad2.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-trad2.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-trad3.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose-trad3.cbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex-ext/ext-verbose.cbx

%package -n texlive-biblatex-fiwi
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn45876
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX styles for use in German humanities
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-fiwi-doc >= %{texlive_version}
Provides:       tex(fiwi-yearbeginning.bbx)
Provides:       tex(fiwi.bbx)
Provides:       tex(fiwi.cbx)
Provides:       tex(fiwi2.bbx)
Provides:       tex(fiwi2.cbx)
Requires:       tex(ragged2e.sty)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source193:      biblatex-fiwi.tar.xz
Source194:      biblatex-fiwi.doc.tar.xz

%description -n texlive-biblatex-fiwi
The package provides a collection of styles for BibLaTeX
(version 3.5 is required, currently). It was designed for
citations in German Humanities, especially film studies, and
offers some features that are not provided by the standard
BibLaTeX styles. The style is highly optimized for documents
written in German, and the main documentation is only available
in German.

%package -n texlive-biblatex-fiwi-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn45876
Release:        0
Summary:        Documentation for texlive-biblatex-fiwi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-fiwi and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-fiwi-doc:de)

%description -n texlive-biblatex-fiwi-doc
This package includes the documentation for texlive-biblatex-fiwi

%post -n texlive-biblatex-fiwi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-fiwi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-fiwi
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-fiwi-doc
%{_texmfdistdir}/doc/latex/biblatex-fiwi/README
%{_texmfdistdir}/doc/latex/biblatex-fiwi/biblatex-fiwi.pdf
%{_texmfdistdir}/doc/latex/biblatex-fiwi/biblatex-fiwi.tex
%{_texmfdistdir}/doc/latex/biblatex-fiwi/diss.xdy
%{_texmfdistdir}/doc/latex/biblatex-fiwi/dissff.xdy
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi-options.pdf
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi-options.tex
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi-xindy.pdf
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi-xindy.tex
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi.pdf
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi.tex
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi2-options.pdf
%{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi2-options.tex
%{_texmfdistdir}/doc/latex/biblatex-fiwi/examples.bib

%files -n texlive-biblatex-fiwi
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi-yearbeginning.bbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi.bbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi.cbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi.dbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi2.bbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi2.cbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi2.dbx

%package -n texlive-biblatex-gb7714-2015
Version:        %{texlive_version}.%{texlive_noarch}.1.1psvn69790
Release:        0
License:        LPPL-1.0
Summary:        A BibLaTeX implementation of the GBT7714-2015 bibliography style for Chinese users
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-gb7714-2015-doc >= %{texlive_version}
Provides:       tex(chinese-css.bbx)
Provides:       tex(chinese-css.cbx)
Provides:       tex(chinese-erj.bbx)
Provides:       tex(chinese-erj.cbx)
Provides:       tex(chinese-jmw.bbx)
Provides:       tex(chinese-jmw.cbx)
Provides:       tex(gb7714-1987.bbx)
Provides:       tex(gb7714-1987.cbx)
Provides:       tex(gb7714-1987ay.bbx)
Provides:       tex(gb7714-1987ay.cbx)
Provides:       tex(gb7714-2005.bbx)
Provides:       tex(gb7714-2005.cbx)
Provides:       tex(gb7714-2005ay.bbx)
Provides:       tex(gb7714-2005ay.cbx)
Provides:       tex(gb7714-2015-gbk.def)
Provides:       tex(gb7714-2015.bbx)
Provides:       tex(gb7714-2015.cbx)
Provides:       tex(gb7714-2015ay.bbx)
Provides:       tex(gb7714-2015ay.cbx)
Provides:       tex(gb7714-2015ms.bbx)
Provides:       tex(gb7714-2015ms.cbx)
Provides:       tex(gb7714-2015mx.bbx)
Provides:       tex(gb7714-2015mx.cbx)
Provides:       tex(gb7714-CCNU.bbx)
Provides:       tex(gb7714-CCNU.cbx)
Provides:       tex(gb7714-NWAFU.bbx)
Provides:       tex(gb7714-NWAFU.cbx)
Provides:       tex(gb7714-SEU.bbx)
Provides:       tex(gb7714-SEU.cbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(mfirstuc.sty)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source195:      biblatex-gb7714-2015.tar.xz
Source196:      biblatex-gb7714-2015.doc.tar.xz

%description -n texlive-biblatex-gb7714-2015
This package provides an implementation of the GBT7714-2015
bibliography style. This implementation follows the
GBT7714-2015 standard and can be used by simply loading
BibLaTeX with the appropriate option. A demonstration database
is provided to show how to format input for the style.

%package -n texlive-biblatex-gb7714-2015-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1psvn69790
Release:        0
Summary:        Documentation for texlive-biblatex-gb7714-2015
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-gb7714-2015 and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-gb7714-2015-doc:zh)

%description -n texlive-biblatex-gb7714-2015-doc
This package includes the documentation for texlive-biblatex-gb7714-2015

%post -n texlive-biblatex-gb7714-2015
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-gb7714-2015
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-gb7714-2015
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-gb7714-2015-doc
%{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/README.md
%{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/biblatex-gb7714-2015-preamble.tex
%{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/biblatex-gb7714-2015.pdf
%{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/biblatex-gb7714-2015.tex
%{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/example.bib
%{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/gb7714texttobib.pl
%{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/makeall.py

%files -n texlive-biblatex-gb7714-2015
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/chinese-css.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/chinese-css.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/chinese-erj.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/chinese-erj.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/chinese-jmw.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/chinese-jmw.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-1987.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-1987.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-1987ay.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-1987ay.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2005.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2005.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2005ay.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2005ay.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015-gbk.def
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015ay.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015ay.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015mx.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-2015mx.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-CCNU.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-CCNU.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-NWAFU.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-NWAFU.cbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-SEU.bbx
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015/gb7714-SEU.cbx

%package -n texlive-biblatex-german-legal
Version:        %{texlive_version}.%{texlive_noarch}.003svn66461
Release:        0
License:        LPPL-1.0
Summary:        Comprehensive citation style for German legal texts
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-german-legal-doc >= %{texlive_version}
Provides:       tex(german-legal-book.bbx)
Provides:       tex(german-legal-book.cbx)
Requires:       tex(ext-authortitle.bbx)
Requires:       tex(ext-authortitle.cbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source197:      biblatex-german-legal.tar.xz
Source198:      biblatex-german-legal.doc.tar.xz

%description -n texlive-biblatex-german-legal
This package aims to provide citation styles (for footnotes and
bibliographies) for German legal texts. It is currently focused
on citations in books (style german-legal-book), but may be
extended to journal articles in the future. Dieses Paket
enthalt BibLaTeX-Zitierstile fur die Rechtswissenschaften in
Deutschland. Aktuell enthalt es einen auf Monographien in den
deutschen Rechtswissenschaften ausgerichteten Zitierstil namens
german-legal-book.

%package -n texlive-biblatex-german-legal-doc
Version:        %{texlive_version}.%{texlive_noarch}.003svn66461
Release:        0
Summary:        Documentation for texlive-biblatex-german-legal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-german-legal and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-german-legal-doc:de)

%description -n texlive-biblatex-german-legal-doc
This package includes the documentation for texlive-biblatex-german-legal

%post -n texlive-biblatex-german-legal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-german-legal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-german-legal
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-german-legal-doc
%{_texmfdistdir}/doc/latex/biblatex-german-legal/README.md
%{_texmfdistdir}/doc/latex/biblatex-german-legal/biblatex-german-legal.pdf
%{_texmfdistdir}/doc/latex/biblatex-german-legal/biblatex-german-legal.tex

%files -n texlive-biblatex-german-legal
%{_texmfdistdir}/tex/latex/biblatex-german-legal/german-legal-book.bbx
%{_texmfdistdir}/tex/latex/biblatex-german-legal/german-legal-book.cbx

%package -n texlive-biblatex-gost
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn66935
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX support for GOST standard bibliographies
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-gost-doc >= %{texlive_version}
Provides:       tex(american-gost.lbx)
Provides:       tex(biblatex-gost.def)
Provides:       tex(brazilian-gost.lbx)
Provides:       tex(british-gost.lbx)
Provides:       tex(catalan-gost.lbx)
Provides:       tex(croatian-gost.lbx)
Provides:       tex(english-gost.lbx)
Provides:       tex(french-gost.lbx)
Provides:       tex(galician-gost.lbx)
Provides:       tex(german-gost.lbx)
Provides:       tex(gost-alphabetic-min.bbx)
Provides:       tex(gost-alphabetic-min.cbx)
Provides:       tex(gost-alphabetic.bbx)
Provides:       tex(gost-alphabetic.cbx)
Provides:       tex(gost-authoryear-min.bbx)
Provides:       tex(gost-authoryear-min.cbx)
Provides:       tex(gost-authoryear.bbx)
Provides:       tex(gost-authoryear.cbx)
Provides:       tex(gost-footnote-min.bbx)
Provides:       tex(gost-footnote-min.cbx)
Provides:       tex(gost-footnote.bbx)
Provides:       tex(gost-footnote.cbx)
Provides:       tex(gost-inline-min.bbx)
Provides:       tex(gost-inline-min.cbx)
Provides:       tex(gost-inline.bbx)
Provides:       tex(gost-inline.cbx)
Provides:       tex(gost-numeric-min.bbx)
Provides:       tex(gost-numeric-min.cbx)
Provides:       tex(gost-numeric.bbx)
Provides:       tex(gost-numeric.cbx)
Provides:       tex(gost-standard.bbx)
Provides:       tex(greek-gost.lbx)
Provides:       tex(icelandic-gost.lbx)
Provides:       tex(italian-gost.lbx)
Provides:       tex(portuguese-gost.lbx)
Provides:       tex(russian-gost.lbx)
Provides:       tex(slovene-gost.lbx)
Provides:       tex(spanish-gost.lbx)
Requires:       tex(alphabetic.cbx)
Requires:       tex(american.lbx)
Requires:       tex(brazilian.lbx)
Requires:       tex(british.lbx)
Requires:       tex(catalan.lbx)
Requires:       tex(croatian.lbx)
Requires:       tex(english.lbx)
Requires:       tex(french.lbx)
Requires:       tex(galician.lbx)
Requires:       tex(german.lbx)
Requires:       tex(greek.lbx)
Requires:       tex(icelandic.lbx)
Requires:       tex(italian.lbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(portuguese.lbx)
Requires:       tex(slovene.lbx)
Requires:       tex(spanish.lbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source199:      biblatex-gost.tar.xz
Source200:      biblatex-gost.doc.tar.xz

%description -n texlive-biblatex-gost
The package provides BibLaTeX support for Russian bibliography
style GOST 7.0.5-2008

%package -n texlive-biblatex-gost-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.24svn66935
Release:        0
Summary:        Documentation for texlive-biblatex-gost
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-gost and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-gost-doc:en,ru)

%description -n texlive-biblatex-gost-doc
This package includes the documentation for texlive-biblatex-gost

%post -n texlive-biblatex-gost
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-gost
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-gost
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-gost-doc
%{_texmfdistdir}/doc/latex/biblatex-gost/README.md
%{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost-examples.bib
%{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost-examples.pdf
%{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost-examples.tex
%{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost.pdf
%{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost.tex
%{_texmfdistdir}/doc/latex/biblatex-gost/ltxdockit.cfg
%{_texmfdistdir}/doc/latex/biblatex-gost/ltxdockit.cls

%files -n texlive-biblatex-gost
%{_texmfdistdir}/tex/latex/biblatex-gost/american-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/biblatex-gost.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/biblatex-gost.def
%{_texmfdistdir}/tex/latex/biblatex-gost/brazilian-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/british-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/catalan-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/croatian-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/english-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/french-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/galician-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/german-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-standard.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/greek-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/icelandic-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/italian-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/portuguese-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/russian-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/slovene-gost.lbx
%{_texmfdistdir}/tex/latex/biblatex-gost/spanish-gost.lbx

%package -n texlive-biblatex-historian
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn19787
Release:        0
License:        LPPL-1.0
Summary:        A BibLaTeX style
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-historian-doc >= %{texlive_version}
Provides:       tex(historian.bbx)
Provides:       tex(historian.cbx)
Provides:       tex(historian.lbx)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source201:      biblatex-historian.tar.xz
Source202:      biblatex-historian.doc.tar.xz

%description -n texlive-biblatex-historian
A BibLaTeX style, based on the Turabian Manual (a version of
Chicago).

%package -n texlive-biblatex-historian-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4svn19787
Release:        0
Summary:        Documentation for texlive-biblatex-historian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-historian and texlive-alldocumentation)

%description -n texlive-biblatex-historian-doc
This package includes the documentation for texlive-biblatex-historian

%post -n texlive-biblatex-historian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-historian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-historian
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-historian-doc
%{_texmfdistdir}/doc/latex/biblatex-historian/README.txt
%{_texmfdistdir}/doc/latex/biblatex-historian/historian.bib
%{_texmfdistdir}/doc/latex/biblatex-historian/historian.pdf

%files -n texlive-biblatex-historian
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.bbx
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.cbx
%{_texmfdistdir}/tex/latex/biblatex-historian/historian.lbx

%package -n texlive-biblatex-ieee
Version:        %{texlive_version}.%{texlive_noarch}.1.3fsvn61243
Release:        0
License:        LPPL-1.0
Summary:        IEEE style files for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-ieee-doc >= %{texlive_version}
Provides:       tex(ieee-alphabetic.bbx)
Provides:       tex(ieee-alphabetic.cbx)
Provides:       tex(ieee.bbx)
Provides:       tex(ieee.cbx)
Provides:       tex(magyar-ieee.lbx)
Requires:       tex(alphabetic.cbx)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source203:      biblatex-ieee.tar.xz
Source204:      biblatex-ieee.doc.tar.xz

%description -n texlive-biblatex-ieee
This is a BibLaTeX style that implements the bibliography style
of the IEEE for BibLaTeX. The implementation follows standard
BibLaTeX conventions, and can be used simply by loading
BibLaTeX with the appropriate option:
\usepackage[style=ieee]{biblatex} A demonstration database is
provided to show how to format input for the style.
biblatex-ieee requires BibLaTeX 2.7 or later, and works with
both BibTeX and Biber as the database back-end.

%package -n texlive-biblatex-ieee-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3fsvn61243
Release:        0
Summary:        Documentation for texlive-biblatex-ieee
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-ieee and texlive-alldocumentation)

%description -n texlive-biblatex-ieee-doc
This package includes the documentation for texlive-biblatex-ieee

%post -n texlive-biblatex-ieee
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-ieee
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-ieee
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-ieee-doc
%{_texmfdistdir}/doc/latex/biblatex-ieee/README.md
%{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee-alphabetic.pdf
%{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee-alphabetic.tex
%{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.bib
%{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.pdf
%{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.tex

%files -n texlive-biblatex-ieee
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee-alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee-alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee.bbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee.cbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/magyar-ieee.lbx

%package -n texlive-biblatex-ijsra
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn41634
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX style for the International Journal of Student Research in Archaeology
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-ijsra-doc >= %{texlive_version}
Provides:       tex(ijsra.bbx)
Provides:       tex(ijsra.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source205:      biblatex-ijsra.tar.xz
Source206:      biblatex-ijsra.doc.tar.xz

%description -n texlive-biblatex-ijsra
BibLaTeX style used for the journal International Journal of
Student Research in Archaeology.

%package -n texlive-biblatex-ijsra-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn41634
Release:        0
Summary:        Documentation for texlive-biblatex-ijsra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-ijsra and texlive-alldocumentation)

%description -n texlive-biblatex-ijsra-doc
This package includes the documentation for texlive-biblatex-ijsra

%post -n texlive-biblatex-ijsra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-ijsra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-ijsra
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-ijsra-doc
%{_texmfdistdir}/doc/latex/biblatex-ijsra/README.md
%{_texmfdistdir}/doc/latex/biblatex-ijsra/biblatex-ijsra.pdf
%{_texmfdistdir}/doc/latex/biblatex-ijsra/biblatex-ijsra.tex

%files -n texlive-biblatex-ijsra
%{_texmfdistdir}/tex/latex/biblatex-ijsra/ijsra.bbx
%{_texmfdistdir}/tex/latex/biblatex-ijsra/ijsra.cbx

%package -n texlive-biblatex-iso690
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4.1svn62866
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX style for ISO 690 standard
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-iso690-doc >= %{texlive_version}
Provides:       tex(bulgarian-iso.lbx)
Provides:       tex(czech-iso.lbx)
Provides:       tex(english-iso.lbx)
Provides:       tex(french-iso.lbx)
Provides:       tex(german-iso.lbx)
Provides:       tex(iso-alphabetic.bbx)
Provides:       tex(iso-alphabetic.cbx)
Provides:       tex(iso-authortitle.bbx)
Provides:       tex(iso-authortitle.cbx)
Provides:       tex(iso-authoryear.bbx)
Provides:       tex(iso-authoryear.cbx)
Provides:       tex(iso-fullcite.cbx)
Provides:       tex(iso-numeric.bbx)
Provides:       tex(iso-numeric.cbx)
Provides:       tex(iso.bbx)
Provides:       tex(ngerman-iso.lbx)
Provides:       tex(polish-iso.lbx)
Provides:       tex(slovak-iso.lbx)
Provides:       tex(spanish-iso.lbx)
Requires:       tex(alphabetic.cbx)
Requires:       tex(authortitle.cbx)
Requires:       tex(authoryear.cbx)
Requires:       tex(bulgarian.lbx)
Requires:       tex(czech.lbx)
Requires:       tex(english.lbx)
Requires:       tex(french.lbx)
Requires:       tex(german.lbx)
Requires:       tex(ngerman.lbx)
Requires:       tex(numeric.cbx)
Requires:       tex(polish.lbx)
Requires:       tex(slovak.lbx)
Requires:       tex(spanish.lbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source207:      biblatex-iso690.tar.xz
Source208:      biblatex-iso690.doc.tar.xz

%description -n texlive-biblatex-iso690
The package provides a bibliography and citation style which
conforms to the latest revision of the international standard
ISO 690:2010. The implementation follows BibLaTeX conventions
and requires BibLaTeX [?] 3.4 and biber [?] 2.5.

%package -n texlive-biblatex-iso690-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4.1svn62866
Release:        0
Summary:        Documentation for texlive-biblatex-iso690
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-iso690 and texlive-alldocumentation)

%description -n texlive-biblatex-iso690-doc
This package includes the documentation for texlive-biblatex-iso690

%post -n texlive-biblatex-iso690
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-iso690
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-iso690
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-iso690-doc
%{_texmfdistdir}/doc/latex/biblatex-iso690/README.md
%{_texmfdistdir}/doc/latex/biblatex-iso690/biblatex-iso690-examples.bib
%{_texmfdistdir}/doc/latex/biblatex-iso690/biblatex-iso690.pdf
%{_texmfdistdir}/doc/latex/biblatex-iso690/biblatex-iso690.tex

%files -n texlive-biblatex-iso690
%{_texmfdistdir}/tex/latex/biblatex-iso690/bulgarian-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/czech-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/english-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/french-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/german-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-alphabetic.dbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-authortitle.bbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-authortitle.cbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-authortitle.dbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-authoryear.bbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-authoryear.cbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-authoryear.dbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-fullcite.cbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso-numeric.dbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/iso.bbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/ngerman-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/polish-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/slovak-iso.lbx
%{_texmfdistdir}/tex/latex/biblatex-iso690/spanish-iso.lbx

%package -n texlive-biblatex-jura2
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn64762
Release:        0
License:        LPPL-1.0
Summary:        Citation style for the German legal profession
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-jura2-doc >= %{texlive_version}
Provides:       tex(jura2.bbx)
Provides:       tex(jura2.cbx)
Requires:       tex(ext-authortitle-ibid.bbx)
Requires:       tex(ext-authortitle-ibid.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source209:      biblatex-jura2.tar.xz
Source210:      biblatex-jura2.doc.tar.xz

%description -n texlive-biblatex-jura2
The package offers BibLaTeX support for citations in German
legal texts.

%package -n texlive-biblatex-jura2-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn64762
Release:        0
Summary:        Documentation for texlive-biblatex-jura2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-jura2 and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-jura2-doc:de)

%description -n texlive-biblatex-jura2-doc
This package includes the documentation for texlive-biblatex-jura2

%post -n texlive-biblatex-jura2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-jura2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-jura2
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-jura2-doc
%{_texmfdistdir}/doc/latex/biblatex-jura2/README.md
%{_texmfdistdir}/doc/latex/biblatex-jura2/biblatex-jura2.tex
%{_texmfdistdir}/doc/latex/biblatex-jura2/biblatex_jura2.pdf
%{_texmfdistdir}/doc/latex/biblatex-jura2/mylit.bib

%files -n texlive-biblatex-jura2
%{_texmfdistdir}/tex/latex/biblatex-jura2/jura2.bbx
%{_texmfdistdir}/tex/latex/biblatex-jura2/jura2.cbx

%package -n texlive-biblatex-juradiss
Version:        %{texlive_version}.%{texlive_noarch}.0.0.23svn56502
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX stylefiles for German law theses
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-juradiss-doc >= %{texlive_version}
Provides:       tex(biblatex-juradiss.bbx)
Provides:       tex(biblatex-juradiss.cbx)
Requires:       tex(authortitle-dw.bbx)
Requires:       tex(authortitle-dw.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source211:      biblatex-juradiss.tar.xz
Source212:      biblatex-juradiss.doc.tar.xz

%description -n texlive-biblatex-juradiss
The package provides a custom citation-style for typesetting a
German law thesis with LaTeX. The package (using BibLaTeX) is
based on biblatex-dw and uses biber.

%package -n texlive-biblatex-juradiss-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.23svn56502
Release:        0
Summary:        Documentation for texlive-biblatex-juradiss
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-juradiss and texlive-alldocumentation)

%description -n texlive-biblatex-juradiss-doc
This package includes the documentation for texlive-biblatex-juradiss

%post -n texlive-biblatex-juradiss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-juradiss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-juradiss
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-juradiss-doc
%{_texmfdistdir}/doc/latex/biblatex-juradiss/Changes
%{_texmfdistdir}/doc/latex/biblatex-juradiss/README
%{_texmfdistdir}/doc/latex/biblatex-juradiss/biblatex-juradiss.pdf
%{_texmfdistdir}/doc/latex/biblatex-juradiss/biblatex-juradiss.tex

%files -n texlive-biblatex-juradiss
%{_texmfdistdir}/tex/latex/biblatex-juradiss/biblatex-juradiss.bbx
%{_texmfdistdir}/tex/latex/biblatex-juradiss/biblatex-juradiss.cbx
%{_texmfdistdir}/tex/latex/biblatex-juradiss/biblatex-juradiss.dbx

%package -n texlive-biblatex-license
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn58437
Release:        0
License:        LPPL-1.0
Summary:        Add license data to the bibliography
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-license-doc >= %{texlive_version}
Provides:       tex(biblatex-license.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source213:      biblatex-license.tar.xz
Source214:      biblatex-license.doc.tar.xz

%description -n texlive-biblatex-license
This package is for adding license data to bibliography entries
via BibLaTeX's built-in related mechanism. It provides a new
relatedtype license and some bibmacros for typesetting these
related entries.

%package -n texlive-biblatex-license-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn58437
Release:        0
Summary:        Documentation for texlive-biblatex-license
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-license and texlive-alldocumentation)

%description -n texlive-biblatex-license-doc
This package includes the documentation for texlive-biblatex-license

%post -n texlive-biblatex-license
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-license
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-license
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-license-doc
%{_texmfdistdir}/doc/latex/biblatex-license/README.md
%{_texmfdistdir}/doc/latex/biblatex-license/biblatex-license.pdf
%{_texmfdistdir}/doc/latex/biblatex-license/biblatex-license.tex

%files -n texlive-biblatex-license
%{_texmfdistdir}/tex/latex/biblatex-license/biblatex-license.sty

%package -n texlive-biblatex-lncs
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn67053
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX style for Springer Lecture Notes in Computer Science
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-lncs-doc >= %{texlive_version}
Provides:       tex(lncs.bbx)
Provides:       tex(lncs.cbx)
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source215:      biblatex-lncs.tar.xz
Source216:      biblatex-lncs.doc.tar.xz

%description -n texlive-biblatex-lncs
This is a BibLaTeX style for Springer Lecture Notes in Computer
Science (LNCS). It extends the standard BiBTeX model by an
acronym entry.

%package -n texlive-biblatex-lncs-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn67053
Release:        0
Summary:        Documentation for texlive-biblatex-lncs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-lncs and texlive-alldocumentation)

%description -n texlive-biblatex-lncs-doc
This package includes the documentation for texlive-biblatex-lncs

%post -n texlive-biblatex-lncs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-lncs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-lncs
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-lncs-doc
%{_texmfdistdir}/doc/latex/biblatex-lncs/LICENSE
%{_texmfdistdir}/doc/latex/biblatex-lncs/README.md
%{_texmfdistdir}/doc/latex/biblatex-lncs/biblatex-lncs-test.bib
%{_texmfdistdir}/doc/latex/biblatex-lncs/biblatex-lncs-test.tex

%files -n texlive-biblatex-lncs
%{_texmfdistdir}/tex/latex/biblatex-lncs/lncs.bbx
%{_texmfdistdir}/tex/latex/biblatex-lncs/lncs.cbx
%{_texmfdistdir}/tex/latex/biblatex-lncs/lncs.dbx

%package -n texlive-biblatex-lni
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn68755
Release:        0
License:        LPPL-1.0
Summary:        LNI style for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-lni-doc >= %{texlive_version}
Provides:       tex(LNI-english.lbx)
Provides:       tex(LNI-ngerman.lbx)
Provides:       tex(LNI.bbx)
Provides:       tex(LNI.cbx)
Requires:       tex(alphabetic.bbx)
Requires:       tex(alphabetic.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source217:      biblatex-lni.tar.xz
Source218:      biblatex-lni.doc.tar.xz

%description -n texlive-biblatex-lni
BibLaTeX style for the Lecture Notes in Informatics, which is
published by the Gesellschaft fur Informatik (GI e.V.).

%package -n texlive-biblatex-lni-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn68755
Release:        0
Summary:        Documentation for texlive-biblatex-lni
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-lni and texlive-alldocumentation)

%description -n texlive-biblatex-lni-doc
This package includes the documentation for texlive-biblatex-lni

%post -n texlive-biblatex-lni
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-lni
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-lni
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-lni-doc
%{_texmfdistdir}/doc/latex/biblatex-lni/CHANGELOG.md
%{_texmfdistdir}/doc/latex/biblatex-lni/LICENSE
%{_texmfdistdir}/doc/latex/biblatex-lni/LNI-examples.bib
%{_texmfdistdir}/doc/latex/biblatex-lni/README.md
%{_texmfdistdir}/doc/latex/biblatex-lni/basic-test-de.tex
%{_texmfdistdir}/doc/latex/biblatex-lni/basic-test-en.tex
%{_texmfdistdir}/doc/latex/biblatex-lni/mwe-de.tex
%{_texmfdistdir}/doc/latex/biblatex-lni/mwe-en.tex

%files -n texlive-biblatex-lni
%{_texmfdistdir}/tex/latex/biblatex-lni/LNI-english.lbx
%{_texmfdistdir}/tex/latex/biblatex-lni/LNI-ngerman.lbx
%{_texmfdistdir}/tex/latex/biblatex-lni/LNI.bbx
%{_texmfdistdir}/tex/latex/biblatex-lni/LNI.cbx

%package -n texlive-biblatex-luh-ipw
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn32180
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX styles for social sciences
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-luh-ipw-doc >= %{texlive_version}
Provides:       tex(authoryear-luh-ipw.bbx)
Provides:       tex(authoryear-luh-ipw.cbx)
Provides:       tex(english-luh-ipw.lbx)
Provides:       tex(german-luh-ipw.lbx)
Provides:       tex(standard-luh-ipw.bbx)
Provides:       tex(standard-luh-ipw.cbx)
Provides:       tex(verbose-inote-luh-ipw.bbx)
Provides:       tex(verbose-inote-luh-ipw.cbx)
Requires:       tex(authoryear-icomp.bbx)
Requires:       tex(authoryear-icomp.cbx)
Requires:       tex(verbose-inote.bbx)
Requires:       tex(verbose-inote.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source219:      biblatex-luh-ipw.tar.xz
Source220:      biblatex-luh-ipw.doc.tar.xz

%description -n texlive-biblatex-luh-ipw
The bundle is a small collection of styles for BibLaTeX. It was
designed for citations in the Humanities, following the
guidelines of style of the institutes for the social sciences
of the Leibniz University Hannover/LUH (especially the
Institute of Political Science). The bundle depends on BibLaTeX
(version 1.1 at least) and cannot be used without it.

%package -n texlive-biblatex-luh-ipw-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn32180
Release:        0
Summary:        Documentation for texlive-biblatex-luh-ipw
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-luh-ipw and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-luh-ipw-doc:de)

%description -n texlive-biblatex-luh-ipw-doc
This package includes the documentation for texlive-biblatex-luh-ipw

%post -n texlive-biblatex-luh-ipw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-luh-ipw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-luh-ipw
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-luh-ipw-doc
%{_texmfdistdir}/doc/latex/biblatex-luh-ipw/README
%{_texmfdistdir}/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-preamble.tex
%{_texmfdistdir}/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-print.tex
%{_texmfdistdir}/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-screen.tex
%{_texmfdistdir}/doc/latex/biblatex-luh-ipw/de-biblatex-luh-ipw.pdf
%{_texmfdistdir}/doc/latex/biblatex-luh-ipw/de-biblatex-luh-ipw.tex

%files -n texlive-biblatex-luh-ipw
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/bbx/authoryear-luh-ipw.bbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/bbx/standard-luh-ipw.bbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/bbx/verbose-inote-luh-ipw.bbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/cbx/authoryear-luh-ipw.cbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/cbx/standard-luh-ipw.cbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/cbx/verbose-inote-luh-ipw.cbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/lbx/english-luh-ipw.lbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/lbx/german-luh-ipw.lbx

%package -n texlive-biblatex-manuscripts-philology
Version:        %{texlive_version}.%{texlive_noarch}.2.1.4svn66977
Release:        0
License:        LPPL-1.0
Summary:        Manage classical manuscripts with BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-manuscripts-philology-doc >= %{texlive_version}
Provides:       tex(english-manuscripts.lbx)
Provides:       tex(french-manuscripts.lbx)
Provides:       tex(italian-manuscripts.lbx)
Provides:       tex(latin-manuscripts.lbx)
Provides:       tex(manuscripts-NewBibliographyString.sty)
Provides:       tex(manuscripts-noautoshorthand.bbx)
Provides:       tex(manuscripts-shared.bbx)
Provides:       tex(manuscripts.bbx)
Requires:       tex(english.lbx)
Requires:       tex(french.lbx)
Requires:       tex(italian.lbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source221:      biblatex-manuscripts-philology.tar.xz
Source222:      biblatex-manuscripts-philology.doc.tar.xz

%description -n texlive-biblatex-manuscripts-philology
The package adds a new entry type: @manuscript to manage
manuscript in classical philology, for example to prepare a
critical edition.

%package -n texlive-biblatex-manuscripts-philology-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1.4svn66977
Release:        0
Summary:        Documentation for texlive-biblatex-manuscripts-philology
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-manuscripts-philology and texlive-alldocumentation)

%description -n texlive-biblatex-manuscripts-philology-doc
This package includes the documentation for texlive-biblatex-manuscripts-philology

%post -n texlive-biblatex-manuscripts-philology
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-manuscripts-philology
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-manuscripts-philology
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-manuscripts-philology-doc
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/README
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology-example.bib
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology-example.tex
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology.pdf
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/biblatex-manuscripts-philology.tex
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/documentation/makefile
%{_texmfdistdir}/doc/latex/biblatex-manuscripts-philology/makefile

%files -n texlive-biblatex-manuscripts-philology
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/english-manuscripts.lbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/french-manuscripts.lbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/italian-manuscripts.lbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/latin-manuscripts.lbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts-NewBibliographyString.sty
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts-noautoshorthand.bbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts-noautoshorthand.dbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts-shared.bbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts-shared.dbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts.bbx
%{_texmfdistdir}/tex/latex/biblatex-manuscripts-philology/manuscripts.dbx

%package -n texlive-biblatex-mla
Version:        %{texlive_version}.%{texlive_noarch}.2.1asvn62138
Release:        0
License:        LPPL-1.0
Summary:        MLA style files for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-mla-doc >= %{texlive_version}
Provides:       tex(american-mla.lbx)
Provides:       tex(english-mla.lbx)
Provides:       tex(italian-mla.lbx)
Provides:       tex(mla-footnotes.cbx)
Provides:       tex(mla-new.bbx)
Provides:       tex(mla-new.cbx)
Provides:       tex(mla-strict.bbx)
Provides:       tex(mla-strict.cbx)
Provides:       tex(mla.bbx)
Provides:       tex(mla.cbx)
Provides:       tex(mla7.bbx)
Provides:       tex(mla7.cbx)
Provides:       tex(portuguese-mla.lbx)
Provides:       tex(spanish-mla.lbx)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source223:      biblatex-mla.tar.xz
Source224:      biblatex-mla.doc.tar.xz

%description -n texlive-biblatex-mla
The package provides BibLaTeX support for citations in the
format specified by the MLA handbook.

%package -n texlive-biblatex-mla-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1asvn62138
Release:        0
Summary:        Documentation for texlive-biblatex-mla
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-mla and texlive-alldocumentation)

%description -n texlive-biblatex-mla-doc
This package includes the documentation for texlive-biblatex-mla

%post -n texlive-biblatex-mla
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-mla
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-mla
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-mla-doc
%{_texmfdistdir}/doc/latex/biblatex-mla/CHANGES
%{_texmfdistdir}/doc/latex/biblatex-mla/README
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/biblatex-mla.pdf
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/biblatex-mla.tex
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/bibtex_documentation.sty
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/examples.bib
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/examples.pdf
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/examples.tex
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/handbook9.bib
%{_texmfdistdir}/doc/latex/biblatex-mla/doc/handbook9_messy.bib

%files -n texlive-biblatex-mla
%{_texmfdistdir}/tex/latex/biblatex-mla/american-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/english-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/italian-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla-footnotes.cbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla-new.bbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla-new.cbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla-strict.bbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla-strict.cbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla.bbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla.cbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla.dbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla7.bbx
%{_texmfdistdir}/tex/latex/biblatex-mla/mla7.cbx
%{_texmfdistdir}/tex/latex/biblatex-mla/portuguese-mla.lbx
%{_texmfdistdir}/tex/latex/biblatex-mla/spanish-mla.lbx

%package -n texlive-biblatex-morenames
Version:        %{texlive_version}.%{texlive_noarch}.1.3.1svn43049
Release:        0
License:        LPPL-1.0
Summary:        New names for standard BibLaTeX entry type
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-morenames-doc >= %{texlive_version}
Provides:       tex(morenames.bbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source225:      biblatex-morenames.tar.xz
Source226:      biblatex-morenames.doc.tar.xz

%description -n texlive-biblatex-morenames
This package adds new fields of "name" type to the standard
entry types of BibLaTeX. For example: maineditor, for a
@collection, means the editor of @mvcollection, and not the
editor of the @collection. bookineditor, for a @bookinbook,
means the editor of the entry, and not, as the standard editor
field, the editor of the volume in which the entry is
contained.

%package -n texlive-biblatex-morenames-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.1svn43049
Release:        0
Summary:        Documentation for texlive-biblatex-morenames
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-morenames and texlive-alldocumentation)

%description -n texlive-biblatex-morenames-doc
This package includes the documentation for texlive-biblatex-morenames

%post -n texlive-biblatex-morenames
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-morenames
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-morenames
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-morenames-doc
%{_texmfdistdir}/doc/latex/biblatex-morenames/README
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/biblatex-morenames.pdf
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/biblatex-morenames.tex
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-bookineditor-BookineditorFromEditor.bib
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-bookineditor-BookineditorFromEditor.dot
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-bookineditor-BookineditorFromEditor.pdf
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-bookineditor.bib
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-bookineditor.dot
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-bookineditor.pdf
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-maineditor.bib
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-maineditor.dot
%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/example-maineditor.pdf

%files -n texlive-biblatex-morenames
%{_texmfdistdir}/tex/latex/biblatex-morenames/morenames.bbx
%{_texmfdistdir}/tex/latex/biblatex-morenames/morenames.dbx

%package -n texlive-biblatex-ms
Version:        %{texlive_version}.%{texlive_noarch}.4.0_1svn66480
Release:        0
License:        LPPL-1.0
Summary:        Sophisticated Bibliographies in LaTeX (multiscript version)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires:       texlive-etoolbox >= %{texlive_version}
#!BuildIgnore: texlive-etoolbox
Requires:       texlive-kvoptions >= %{texlive_version}
#!BuildIgnore: texlive-kvoptions
Requires:       texlive-logreq >= %{texlive_version}
#!BuildIgnore: texlive-logreq
Requires:       texlive-pdftexcmds >= %{texlive_version}
#!BuildIgnore: texlive-pdftexcmds
Requires:       texlive-url >= %{texlive_version}
#!BuildIgnore: texlive-url
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-ms-doc >= %{texlive_version}
Provides:       tex(UKenglish-ms.lbx)
Provides:       tex(USenglish-ms.lbx)
Provides:       tex(alphabetic-ms.bbx)
Provides:       tex(alphabetic-ms.cbx)
Provides:       tex(alphabetic-verb-ms.bbx)
Provides:       tex(alphabetic-verb-ms.cbx)
Provides:       tex(american-ms.lbx)
Provides:       tex(australian-ms.lbx)
Provides:       tex(austrian-ms.lbx)
Provides:       tex(authortitle-comp-ms.bbx)
Provides:       tex(authortitle-comp-ms.cbx)
Provides:       tex(authortitle-ibid-ms.bbx)
Provides:       tex(authortitle-ibid-ms.cbx)
Provides:       tex(authortitle-icomp-ms.bbx)
Provides:       tex(authortitle-icomp-ms.cbx)
Provides:       tex(authortitle-ms.bbx)
Provides:       tex(authortitle-ms.cbx)
Provides:       tex(authortitle-tcomp-ms.bbx)
Provides:       tex(authortitle-tcomp-ms.cbx)
Provides:       tex(authortitle-terse-ms.bbx)
Provides:       tex(authortitle-terse-ms.cbx)
Provides:       tex(authortitle-ticomp-ms.bbx)
Provides:       tex(authortitle-ticomp-ms.cbx)
Provides:       tex(authoryear-comp-ms.bbx)
Provides:       tex(authoryear-comp-ms.cbx)
Provides:       tex(authoryear-ibid-ms.bbx)
Provides:       tex(authoryear-ibid-ms.cbx)
Provides:       tex(authoryear-icomp-ms.bbx)
Provides:       tex(authoryear-icomp-ms.cbx)
Provides:       tex(authoryear-ms.bbx)
Provides:       tex(authoryear-ms.cbx)
Provides:       tex(basque-ms.lbx)
Provides:       tex(biblatex-ms.cfg)
Provides:       tex(biblatex-ms.def)
Provides:       tex(biblatex-ms.sty)
Provides:       tex(blx-bibtex-ms.def)
Provides:       tex(blx-case-expl3-ms.sty)
Provides:       tex(blx-case-latex2e-ms.sty)
Provides:       tex(blx-compat-ms.def)
Provides:       tex(blx-dm-ms.def)
Provides:       tex(blx-mcite-ms.def)
Provides:       tex(blx-natbib-ms.def)
Provides:       tex(blx-unicode-ms.def)
Provides:       tex(brazil-ms.lbx)
Provides:       tex(brazilian-ms.lbx)
Provides:       tex(british-ms.lbx)
Provides:       tex(bulgarian-ms.lbx)
Provides:       tex(canadian-ms.lbx)
Provides:       tex(catalan-ms.lbx)
Provides:       tex(croatian-ms.lbx)
Provides:       tex(czech-ms.lbx)
Provides:       tex(danish-ms.lbx)
Provides:       tex(debug-ms.bbx)
Provides:       tex(debug-ms.cbx)
Provides:       tex(draft-ms.bbx)
Provides:       tex(draft-ms.cbx)
Provides:       tex(dutch-ms.lbx)
Provides:       tex(english-ms.lbx)
Provides:       tex(estonian-ms.lbx)
Provides:       tex(finnish-ms.lbx)
Provides:       tex(french-ms.lbx)
Provides:       tex(galician-ms.lbx)
Provides:       tex(german-ms.lbx)
Provides:       tex(greek-ms.lbx)
Provides:       tex(hungarian-ms.lbx)
Provides:       tex(icelandic-ms.lbx)
Provides:       tex(italian-ms.lbx)
Provides:       tex(latvian-ms.lbx)
Provides:       tex(lithuanian-ms.lbx)
Provides:       tex(magyar-ms.lbx)
Provides:       tex(marathi-ms.lbx)
Provides:       tex(naustrian-ms.lbx)
Provides:       tex(newzealand-ms.lbx)
Provides:       tex(ngerman-ms.lbx)
Provides:       tex(norsk-ms.lbx)
Provides:       tex(nswissgerman-ms.lbx)
Provides:       tex(numeric-comp-ms.bbx)
Provides:       tex(numeric-comp-ms.cbx)
Provides:       tex(numeric-ms.bbx)
Provides:       tex(numeric-ms.cbx)
Provides:       tex(numeric-verb-ms.bbx)
Provides:       tex(numeric-verb-ms.cbx)
Provides:       tex(nynorsk-ms.lbx)
Provides:       tex(polish-ms.lbx)
Provides:       tex(portuges-ms.lbx)
Provides:       tex(portuguese-ms.lbx)
Provides:       tex(reading-ms.bbx)
Provides:       tex(reading-ms.cbx)
Provides:       tex(romanian-ms.lbx)
Provides:       tex(russian-ms.lbx)
Provides:       tex(serbian-ms.lbx)
Provides:       tex(serbianc-ms.lbx)
Provides:       tex(slovak-ms.lbx)
Provides:       tex(slovene-ms.lbx)
Provides:       tex(slovenian-ms.lbx)
Provides:       tex(spanish-ms.lbx)
Provides:       tex(standard-ms.bbx)
Provides:       tex(swedish-ms.lbx)
Provides:       tex(swissgerman-ms.lbx)
Provides:       tex(turkish-ms.lbx)
Provides:       tex(ukrainian-ms.lbx)
Provides:       tex(verbose-ibid-ms.bbx)
Provides:       tex(verbose-ibid-ms.cbx)
Provides:       tex(verbose-inote-ms.bbx)
Provides:       tex(verbose-inote-ms.cbx)
Provides:       tex(verbose-ms.bbx)
Provides:       tex(verbose-ms.cbx)
Provides:       tex(verbose-note-ms.bbx)
Provides:       tex(verbose-note-ms.cbx)
Provides:       tex(verbose-trad1-ms.bbx)
Provides:       tex(verbose-trad1-ms.cbx)
Provides:       tex(verbose-trad2-ms.bbx)
Provides:       tex(verbose-trad2-ms.cbx)
Provides:       tex(verbose-trad3-ms.bbx)
Provides:       tex(verbose-trad3-ms.cbx)
Requires:       tex(alphabetic.bbx)
Requires:       tex(american.lbx)
Requires:       tex(authortitle-comp.cbx)
Requires:       tex(authortitle-icomp.cbx)
Requires:       tex(authortitle.bbx)
Requires:       tex(authortitle.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(brazilian.lbx)
Requires:       tex(british.lbx)
Requires:       tex(english.lbx)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(logreq.sty)
Requires:       tex(magyar.lbx)
Requires:       tex(numeric.bbx)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(portuguese.lbx)
Requires:       tex(slovene.lbx)
Requires:       tex(standard.bbx)
Requires:       tex(url.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source227:      biblatex-ms.tar.xz
Source228:      biblatex-ms.doc.tar.xz

%description -n texlive-biblatex-ms
This package is the "multiscript" version of the BibLaTeX
package intended to solve the issues faced by those wishing to
create multiligual bibliographies. It is intended to be
backwards-compatible with the standard BibLaTeX package and
includes significantly enhanced optional functionality: Fields
in data files can have different form/language alternates in
the same entry Options to select/print a specific alternate are
generally available babel/polyglossia language switching is
done automatically based on the language associated with a
field The intention is that this version will eventually
replace standard BibLaTeX and is being released as an
independent package to allow for wider testing and feedback. It
can be installed in parallel with standard BibLaTeX and the
package name is biblatex-ms. It requires the use of the
multiscript version of biber (biber-ms).

%package -n texlive-biblatex-ms-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.0_1svn66480
Release:        0
Summary:        Documentation for texlive-biblatex-ms
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-ms and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-ms-doc:en)

%description -n texlive-biblatex-ms-doc
This package includes the documentation for texlive-biblatex-ms

%post -n texlive-biblatex-ms
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-ms
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-ms
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-ms-doc
%{_texmfdistdir}/doc/latex/biblatex-ms/CHANGES.md
%{_texmfdistdir}/doc/latex/biblatex-ms/README
%{_texmfdistdir}/doc/latex/biblatex-ms/biber/bltxml/biblatex-examples-ms.bltxml
%{_texmfdistdir}/doc/latex/biblatex-ms/biblatex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/biblatex-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/01-introduction-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/01-introduction-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/01-introduction-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/01-introduction.run-ms.xml
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/02-annotations-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/02-annotations-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/02-annotations-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/03-localization-keys-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/03-localization-keys-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/03-localization-keys-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/04-delimiters-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/04-delimiters-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/04-delimiters-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/10-references-per-section-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/10-references-per-section-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/10-references-per-section-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/11-references-by-section-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/11-references-by-section-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/11-references-by-section-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/12-references-by-segment-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/12-references-by-segment-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/12-references-by-segment-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/13-references-by-keyword-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/13-references-by-keyword-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/13-references-by-keyword-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/14-references-by-category-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/14-references-by-category-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/14-references-by-category-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/15-references-by-type-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/15-references-by-type-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/15-references-by-type-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/16-numeric-prefixed-1-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/16-numeric-prefixed-1-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/16-numeric-prefixed-1-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/17-numeric-prefixed-2-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/17-numeric-prefixed-2-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/17-numeric-prefixed-2-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/18-numeric-hybrid-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/18-numeric-hybrid-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/18-numeric-hybrid-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/19-alphabetic-prefixed-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/19-alphabetic-prefixed-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/19-alphabetic-prefixed-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/20-indexing-single-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/20-indexing-single-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/20-indexing-single-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/21-indexing-multiple-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/21-indexing-multiple-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/21-indexing-multiple-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/22-indexing-subentry-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/22-indexing-subentry-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/22-indexing-subentry-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/30-style-numeric-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/30-style-numeric-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/30-style-numeric-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/31-style-numeric-comp-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/31-style-numeric-comp-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/31-style-numeric-comp-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/32-style-numeric-verb-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/32-style-numeric-verb-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/32-style-numeric-verb-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/40-style-alphabetic-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/40-style-alphabetic-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/40-style-alphabetic-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/41-style-alphabetic-verb-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/41-style-alphabetic-verb-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/41-style-alphabetic-verb-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/42-style-alphabetic-template-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/42-style-alphabetic-template-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/42-style-alphabetic-template-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/50-style-authoryear-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/50-style-authoryear-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/50-style-authoryear-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/51-style-authoryear-ibid-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/51-style-authoryear-ibid-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/51-style-authoryear-ibid-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/52-style-authoryear-comp-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/52-style-authoryear-comp-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/52-style-authoryear-comp-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/53-style-authoryear-icomp-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/53-style-authoryear-icomp-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/53-style-authoryear-icomp-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/60-style-authortitle-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/60-style-authortitle-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/60-style-authortitle-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/61-style-authortitle-ibid-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/61-style-authortitle-ibid-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/61-style-authortitle-ibid-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/62-style-authortitle-comp-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/62-style-authortitle-comp-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/62-style-authortitle-comp-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/63-style-authortitle-icomp-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/63-style-authortitle-icomp-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/63-style-authortitle-icomp-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/64-style-authortitle-terse-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/64-style-authortitle-terse-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/64-style-authortitle-terse-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/65-style-authortitle-tcomp-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/65-style-authortitle-tcomp-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/65-style-authortitle-tcomp-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/66-style-authortitle-ticomp-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/66-style-authortitle-ticomp-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/66-style-authortitle-ticomp-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/70-style-verbose-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/70-style-verbose-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/70-style-verbose-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/71-style-verbose-ibid-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/71-style-verbose-ibid-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/71-style-verbose-ibid-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/72-style-verbose-note-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/72-style-verbose-note-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/72-style-verbose-note-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/73-style-verbose-inote-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/73-style-verbose-inote-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/73-style-verbose-inote-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/74-style-verbose-trad1-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/74-style-verbose-trad1-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/74-style-verbose-trad1-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/75-style-verbose-trad2-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/75-style-verbose-trad2-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/75-style-verbose-trad2-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/76-style-verbose-trad3-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/76-style-verbose-trad3-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/76-style-verbose-trad3-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/80-style-reading-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/80-style-reading-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/80-style-reading-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/81-style-draft-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/81-style-draft-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/81-style-draft-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/82-style-debug-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/82-style-debug-bibtex-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/82-style-debug-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/90-related-entries-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/90-related-entries-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/91-sorting-schemes-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/91-sorting-schemes-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/92-bibliographylists-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/92-bibliographylists-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/93-nameparts-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/93-nameparts-ms.dbx
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/93-nameparts-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/94-labelprefix-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/94-labelprefix-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/95-customlists-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/95-customlists-ms.bib
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/95-customlists-ms.dbx
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/95-customlists-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/96-dates-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/96-dates-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/97-annotations-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/97-annotations-ms.bib
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/97-annotations-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/98-multiscript-biber-ms.pdf
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/98-multiscript-ms.tex
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/biblatex-examples-ms.bib
%{_texmfdistdir}/doc/latex/biblatex-ms/examples/biblatex-examples-ms.bltxml

%files -n texlive-biblatex-ms
%{_texmfdistdir}/bibtex/bib/biblatex-ms/biblatex/biblatex-examples-ms.bib
%{_texmfdistdir}/bibtex/bst/biblatex-ms/biblatex-ms.bst
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/alphabetic-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/alphabetic-verb-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authortitle-comp-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authortitle-ibid-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authortitle-icomp-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authortitle-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authortitle-tcomp-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authortitle-terse-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authortitle-ticomp-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authoryear-comp-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authoryear-ibid-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authoryear-icomp-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/authoryear-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/debug-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/draft-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/numeric-comp-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/numeric-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/numeric-verb-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/reading-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/standard-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/verbose-ibid-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/verbose-inote-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/verbose-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/verbose-note-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/verbose-trad1-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/verbose-trad2-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/bbx/verbose-trad3-ms.bbx
%{_texmfdistdir}/tex/latex/biblatex-ms/biblatex-ms.cfg
%{_texmfdistdir}/tex/latex/biblatex-ms/biblatex-ms.def
%{_texmfdistdir}/tex/latex/biblatex-ms/biblatex-ms.sty
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-bibtex-ms.def
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-case-expl3-ms.sty
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-case-latex2e-ms.sty
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-compat-ms.def
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-dm-ms.def
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-mcite-ms.def
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-natbib-ms.def
%{_texmfdistdir}/tex/latex/biblatex-ms/blx-unicode-ms.def
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/alphabetic-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/alphabetic-verb-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authortitle-comp-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authortitle-ibid-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authortitle-icomp-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authortitle-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authortitle-tcomp-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authortitle-terse-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authortitle-ticomp-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authoryear-comp-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authoryear-ibid-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authoryear-icomp-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/authoryear-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/debug-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/draft-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/numeric-comp-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/numeric-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/numeric-verb-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/reading-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/verbose-ibid-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/verbose-inote-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/verbose-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/verbose-note-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/verbose-trad1-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/verbose-trad2-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/cbx/verbose-trad3-ms.cbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/UKenglish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/USenglish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/american-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/australian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/austrian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/basque-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/brazil-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/brazilian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/british-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/bulgarian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/canadian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/catalan-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/croatian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/czech-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/danish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/dutch-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/english-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/estonian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/finnish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/french-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/galician-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/german-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/greek-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/hungarian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/icelandic-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/italian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/latvian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/lithuanian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/magyar-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/marathi-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/naustrian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/newzealand-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/ngerman-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/norsk-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/nswissgerman-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/nynorsk-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/polish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/portuges-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/portuguese-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/romanian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/russian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/serbian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/serbianc-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/slovak-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/slovene-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/slovenian-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/spanish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/swedish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/swissgerman-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/turkish-ms.lbx
%{_texmfdistdir}/tex/latex/biblatex-ms/lbx/ukrainian-ms.lbx

%package -n texlive-biblatex-multiple-dm
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn37081
Release:        0
License:        LPPL-1.0
Summary:        Load multiple datamodels in BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-multiple-dm-doc >= %{texlive_version}
Provides:       tex(biblatex-multiple-dm.sty)
Provides:       tex(multiple-dm.bbx)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source229:      biblatex-multiple-dm.tar.xz
Source230:      biblatex-multiple-dm.doc.tar.xz

%description -n texlive-biblatex-multiple-dm
The package adds the possibility to BibLaTeX to load data
models from multiple sources.

%package -n texlive-biblatex-multiple-dm-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn37081
Release:        0
Summary:        Documentation for texlive-biblatex-multiple-dm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-multiple-dm and texlive-alldocumentation)

%description -n texlive-biblatex-multiple-dm-doc
This package includes the documentation for texlive-biblatex-multiple-dm

%post -n texlive-biblatex-multiple-dm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-multiple-dm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-multiple-dm
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-multiple-dm-doc
%{_texmfdistdir}/doc/latex/biblatex-multiple-dm/README
%{_texmfdistdir}/doc/latex/biblatex-multiple-dm/biblatex-multiple-dm.pdf
%{_texmfdistdir}/doc/latex/biblatex-multiple-dm/biblatex-multiple-dm.tex
%{_texmfdistdir}/doc/latex/biblatex-multiple-dm/latexmkrc
%{_texmfdistdir}/doc/latex/biblatex-multiple-dm/makefile

%files -n texlive-biblatex-multiple-dm
%{_texmfdistdir}/tex/latex/biblatex-multiple-dm/biblatex-multiple-dm.sty
%{_texmfdistdir}/tex/latex/biblatex-multiple-dm/multiple-dm.bbx
%{_texmfdistdir}/tex/latex/biblatex-multiple-dm/multiple-dm.dbx

%package -n texlive-biblatex-musuos
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn24097
Release:        0
License:        LPPL-1.0
Summary:        A BibLaTeX style for citations in musuos.cls
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-musuos-doc >= %{texlive_version}
Provides:       tex(german-musuos.lbx)
Provides:       tex(musuos.bbx)
Provides:       tex(musuos.cbx)
Requires:       tex(authortitle.bbx)
Requires:       tex(verbose-ibid.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source231:      biblatex-musuos.tar.xz
Source232:      biblatex-musuos.doc.tar.xz

%description -n texlive-biblatex-musuos
The style is designed for use with the musuos class, but it
should be usable with other classes, too.

%package -n texlive-biblatex-musuos-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn24097
Release:        0
Summary:        Documentation for texlive-biblatex-musuos
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-musuos and texlive-alldocumentation)

%description -n texlive-biblatex-musuos-doc
This package includes the documentation for texlive-biblatex-musuos

%post -n texlive-biblatex-musuos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-musuos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-musuos
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-musuos-doc
%{_texmfdistdir}/doc/latex/biblatex-musuos/README
%{_texmfdistdir}/doc/latex/biblatex-musuos/biblatex-musuos.pdf
%{_texmfdistdir}/doc/latex/biblatex-musuos/biblatex-musuos.tex
%{_texmfdistdir}/doc/latex/biblatex-musuos/musuos-bsp.bib

%files -n texlive-biblatex-musuos
%{_texmfdistdir}/tex/latex/biblatex-musuos/german-musuos.lbx
%{_texmfdistdir}/tex/latex/biblatex-musuos/musuos.bbx
%{_texmfdistdir}/tex/latex/biblatex-musuos/musuos.cbx

%package -n texlive-biblatex-nature
Version:        %{texlive_version}.%{texlive_noarch}.1.3dsvn57262
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX support for Nature
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-nature-doc >= %{texlive_version}
Provides:       tex(nature.bbx)
Provides:       tex(nature.cbx)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source233:      biblatex-nature.tar.xz
Source234:      biblatex-nature.doc.tar.xz

%description -n texlive-biblatex-nature
The bundle offers styles that allow authors to use BibLaTeX
when preparing papers for submission to the journal Nature.

%package -n texlive-biblatex-nature-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3dsvn57262
Release:        0
Summary:        Documentation for texlive-biblatex-nature
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-nature and texlive-alldocumentation)

%description -n texlive-biblatex-nature-doc
This package includes the documentation for texlive-biblatex-nature

%post -n texlive-biblatex-nature
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-nature
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-nature
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-nature-doc
%{_texmfdistdir}/doc/latex/biblatex-nature/README.md
%{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.bib
%{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.pdf
%{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.tex

%files -n texlive-biblatex-nature
%{_texmfdistdir}/tex/latex/biblatex-nature/nature.bbx
%{_texmfdistdir}/tex/latex/biblatex-nature/nature.cbx

%package -n texlive-biblatex-nejm
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.0svn49839
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX style for the New England Journal of Medicine (NEJM)
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-nejm-doc >= %{texlive_version}
Provides:       tex(nejm.bbx)
Provides:       tex(nejm.cbx)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(numeric.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source235:      biblatex-nejm.tar.xz
Source236:      biblatex-nejm.doc.tar.xz

%description -n texlive-biblatex-nejm
This is a BibLaTeX numeric style based on the design of the New
England Journal of Medicine (NEJM).

%package -n texlive-biblatex-nejm-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5.0svn49839
Release:        0
Summary:        Documentation for texlive-biblatex-nejm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-nejm and texlive-alldocumentation)

%description -n texlive-biblatex-nejm-doc
This package includes the documentation for texlive-biblatex-nejm

%post -n texlive-biblatex-nejm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-nejm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-nejm
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-nejm-doc
%{_texmfdistdir}/doc/latex/biblatex-nejm/README
%{_texmfdistdir}/doc/latex/biblatex-nejm/biblatex-nejm.pdf
%{_texmfdistdir}/doc/latex/biblatex-nejm/biblatex-nejm.tex

%files -n texlive-biblatex-nejm
%{_texmfdistdir}/tex/latex/biblatex-nejm/nejm.bbx
%{_texmfdistdir}/tex/latex/biblatex-nejm/nejm.cbx

%package -n texlive-biblatex-nottsclassic
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn41596
Release:        0
License:        LPPL-1.0
Summary:        Citation style for the University of Nottingham
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-nottsclassic-doc >= %{texlive_version}
Provides:       tex(nottsclassic-english.lbx)
Provides:       tex(nottsclassic.bbx)
Provides:       tex(nottsclassic.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(british.sty)
Requires:       tex(csquotes.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source237:      biblatex-nottsclassic.tar.xz
Source238:      biblatex-nottsclassic.doc.tar.xz

%description -n texlive-biblatex-nottsclassic
This citation-style covers the citation and bibliography rules
of the University of Nottingham.

%package -n texlive-biblatex-nottsclassic-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn41596
Release:        0
Summary:        Documentation for texlive-biblatex-nottsclassic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-nottsclassic and texlive-alldocumentation)

%description -n texlive-biblatex-nottsclassic-doc
This package includes the documentation for texlive-biblatex-nottsclassic

%post -n texlive-biblatex-nottsclassic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-nottsclassic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-nottsclassic
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-nottsclassic-doc
%{_texmfdistdir}/doc/latex/biblatex-nottsclassic/README.md
%{_texmfdistdir}/doc/latex/biblatex-nottsclassic/nottsclassic.pdf
%{_texmfdistdir}/doc/latex/biblatex-nottsclassic/nottsclassic.tex

%files -n texlive-biblatex-nottsclassic
%{_texmfdistdir}/tex/latex/biblatex-nottsclassic/nottsclassic-english.lbx
%{_texmfdistdir}/tex/latex/biblatex-nottsclassic/nottsclassic.bbx
%{_texmfdistdir}/tex/latex/biblatex-nottsclassic/nottsclassic.cbx

%package -n texlive-biblatex-opcit-booktitle
Version:        %{texlive_version}.%{texlive_noarch}.1.9.0svn48983
Release:        0
License:        LPPL-1.0
Summary:        Use op. cit. for the booktitle of a subentry
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-opcit-booktitle-doc >= %{texlive_version}
Provides:       tex(biblatex-opcit-booktitle.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source239:      biblatex-opcit-booktitle.tar.xz
Source240:      biblatex-opcit-booktitle.doc.tar.xz

%description -n texlive-biblatex-opcit-booktitle
The default citation styles verbose-trad1+; verbose-trad2 ;
verbose-trad3 use the op. cit. form in order to have a shorter
reference when a title has already been cited. However, when
you cite two entries which share the same booktitle but not the
same title, the op. cit. mechanism does not work. This package
enables to obtain references like this: Author1, Title, in
Booktitle, Location, Publisher, Year, pages xxx Author2,
Title2, in Booktitle, op. cit, pages.

%package -n texlive-biblatex-opcit-booktitle-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9.0svn48983
Release:        0
Summary:        Documentation for texlive-biblatex-opcit-booktitle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-opcit-booktitle and texlive-alldocumentation)

%description -n texlive-biblatex-opcit-booktitle-doc
This package includes the documentation for texlive-biblatex-opcit-booktitle

%post -n texlive-biblatex-opcit-booktitle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-opcit-booktitle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-opcit-booktitle
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-opcit-booktitle-doc
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/README
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle-example.bib
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle-example.tex
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle.pdf
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/documentation/biblatex-opcit-booktitle.tex
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/documentation/latexmkrc
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/documentation/makefile
%{_texmfdistdir}/doc/latex/biblatex-opcit-booktitle/makefile

%files -n texlive-biblatex-opcit-booktitle
%{_texmfdistdir}/tex/latex/biblatex-opcit-booktitle/biblatex-opcit-booktitle.sty

%package -n texlive-biblatex-oxref
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn68950
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX styles inspired by the Oxford Guide to Style
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-oxref-doc >= %{texlive_version}
Provides:       tex(american-oxref.lbx)
Provides:       tex(british-oxref.lbx)
Provides:       tex(english-oxref.lbx)
Provides:       tex(oxalph.bbx)
Provides:       tex(oxalph.cbx)
Provides:       tex(oxnotes-ibid.bbx)
Provides:       tex(oxnotes-ibid.cbx)
Provides:       tex(oxnotes-inote.bbx)
Provides:       tex(oxnotes-inote.cbx)
Provides:       tex(oxnotes-note.bbx)
Provides:       tex(oxnotes-note.cbx)
Provides:       tex(oxnotes-trad1.bbx)
Provides:       tex(oxnotes-trad1.cbx)
Provides:       tex(oxnotes-trad2.bbx)
Provides:       tex(oxnotes-trad2.cbx)
Provides:       tex(oxnotes-trad3.bbx)
Provides:       tex(oxnotes-trad3.cbx)
Provides:       tex(oxnotes.bbx)
Provides:       tex(oxnotes.cbx)
Provides:       tex(oxnum.bbx)
Provides:       tex(oxnum.cbx)
Provides:       tex(oxref.bbx)
Provides:       tex(oxyear.bbx)
Provides:       tex(oxyear.cbx)
Provides:       tex(spanish-oxref.lbx)
Requires:       tex(alphabetic.cbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(english.lbx)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(numeric-comp.cbx)
Requires:       tex(standard.bbx)
Requires:       tex(verbose-ibid.cbx)
Requires:       tex(verbose-inote.cbx)
Requires:       tex(verbose-note.cbx)
Requires:       tex(verbose-trad1.cbx)
Requires:       tex(verbose-trad2.cbx)
Requires:       tex(verbose-trad3.cbx)
Requires:       tex(verbose.cbx)
Requires:       tex(xpatch.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source241:      biblatex-oxref.tar.xz
Source242:      biblatex-oxref.doc.tar.xz

%description -n texlive-biblatex-oxref
This bundle provides four BibLaTeX styles that implement (many
of) the stipulations and examples provided by the 2014 New
Hart's Rules and the 2002 Oxford Guide to Style: 'oxnotes' is a
style similar to the standard 'verbose', intended for use with
footnotes; 'oxnum' is a style similar to the standard
'numeric', intended for use with numeric in-text citations;
'oxalph' is a style similar to the standard 'alphabetic',
intended for use with alphabetic in-text citations; 'oxyear' is
a style similar to the standard 'author-year', intended for use
with parenthetical in-text citations. The bundle provides
support for a wide variety of content types, including
manuscripts, audiovisual resources, social media and legal
references.

%package -n texlive-biblatex-oxref-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn68950
Release:        0
Summary:        Documentation for texlive-biblatex-oxref
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-oxref and texlive-alldocumentation)

%description -n texlive-biblatex-oxref-doc
This package includes the documentation for texlive-biblatex-oxref

%post -n texlive-biblatex-oxref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-oxref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-oxref
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-oxref-doc
%{_texmfdistdir}/doc/latex/biblatex-oxref/README.md
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxalph-doc.pdf
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxalph-doc.tex
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxnotes-doc.pdf
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxnotes-doc.tex
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxnum-doc.pdf
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxnum-doc.tex
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxref.bib
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxref.pdf
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxyear-doc.pdf
%{_texmfdistdir}/doc/latex/biblatex-oxref/oxyear-doc.tex

%files -n texlive-biblatex-oxref
%{_texmfdistdir}/tex/latex/biblatex-oxref/american-oxref.lbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/british-oxref.lbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/english-oxref.lbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxalph.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxalph.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxalph.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-ibid.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-ibid.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-ibid.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-inote.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-inote.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-inote.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-note.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-note.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-note.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad1.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad1.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad1.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad2.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad2.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad2.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad3.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad3.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes-trad3.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnotes.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnum.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnum.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxnum.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxref.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxyear.bbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxyear.cbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/oxyear.dbx
%{_texmfdistdir}/tex/latex/biblatex-oxref/spanish-oxref.lbx

%package -n texlive-biblatex-philosophy
Version:        %{texlive_version}.%{texlive_noarch}.1.9.8gsvn64414
Release:        0
License:        LPPL-1.0
Summary:        Styles for using BibLaTeX for work in philosophy
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-philosophy-doc >= %{texlive_version}
Provides:       tex(english-philosophy.lbx)
Provides:       tex(french-philosophy.lbx)
Provides:       tex(italian-philosophy.lbx)
Provides:       tex(philosophy-classic.bbx)
Provides:       tex(philosophy-classic.cbx)
Provides:       tex(philosophy-modern.bbx)
Provides:       tex(philosophy-modern.cbx)
Provides:       tex(philosophy-standard.bbx)
Provides:       tex(philosophy-verbose.bbx)
Provides:       tex(philosophy-verbose.cbx)
Provides:       tex(spanish-philosophy.lbx)
Requires:       tex(authortitle.bbx)
Requires:       tex(authoryear-comp.bbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(standard.bbx)
Requires:       tex(verbose-trad2.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source243:      biblatex-philosophy.tar.xz
Source244:      biblatex-philosophy.doc.tar.xz

%description -n texlive-biblatex-philosophy
The bundle offers two styles - philosophy-classic and
philosophy-modern - that facilitate the production of two
different kinds of bibliography, based on the authoryear style,
with options and features to manage the information about the
translation of foreign texts or their reprints. Though the
package's default settings are based on the conventions used in
Italian publications, these styles can be used with every
language recognized by babel, possibly with some simple
redefinitions.

%package -n texlive-biblatex-philosophy-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9.8gsvn64414
Release:        0
Summary:        Documentation for texlive-biblatex-philosophy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-philosophy and texlive-alldocumentation)

%description -n texlive-biblatex-philosophy-doc
This package includes the documentation for texlive-biblatex-philosophy

%post -n texlive-biblatex-philosophy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-philosophy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-philosophy
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-philosophy-doc
%{_texmfdistdir}/doc/latex/biblatex-philosophy/README
%{_texmfdistdir}/doc/latex/biblatex-philosophy/biblatex-philosophy.pdf
%{_texmfdistdir}/doc/latex/biblatex-philosophy/examples.zip

%files -n texlive-biblatex-philosophy
%{_texmfdistdir}/tex/latex/biblatex-philosophy/english-philosophy.lbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/french-philosophy.lbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/italian-philosophy.lbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-classic.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-classic.cbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-modern.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-modern.cbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-standard.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-verbose.bbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/philosophy-verbose.cbx
%{_texmfdistdir}/tex/latex/biblatex-philosophy/spanish-philosophy.lbx

%package -n texlive-biblatex-phys
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn55643
Release:        0
License:        LPPL-1.0
Summary:        A BibLaTeX implementation of the AIP and APS bibliography style
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-phys-doc >= %{texlive_version}
Provides:       tex(phys.bbx)
Provides:       tex(phys.cbx)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source245:      biblatex-phys.tar.xz
Source246:      biblatex-phys.doc.tar.xz

%description -n texlive-biblatex-phys
The package provides an implementation of the bibliography
styles of both the AIP and the APS for BibLaTeX. This
implementation follows standard BibLaTeX conventions, and can
be used simply by loading BibLaTeX with the appropriate option:
\usepackage[style=phys]{biblatex} A demonstration database is
provided to show how to format input for the style. Style
options are provided to cover the minor formatting variations
between the AIP and APS bibliography styles.

%package -n texlive-biblatex-phys-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn55643
Release:        0
Summary:        Documentation for texlive-biblatex-phys
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-phys and texlive-alldocumentation)

%description -n texlive-biblatex-phys-doc
This package includes the documentation for texlive-biblatex-phys

%post -n texlive-biblatex-phys
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-phys
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-phys
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-phys-doc
%{_texmfdistdir}/doc/latex/biblatex-phys/README.md
%{_texmfdistdir}/doc/latex/biblatex-phys/biblatex-phys.bib
%{_texmfdistdir}/doc/latex/biblatex-phys/biblatex-phys.pdf
%{_texmfdistdir}/doc/latex/biblatex-phys/biblatex-phys.tex

%files -n texlive-biblatex-phys
%{_texmfdistdir}/tex/latex/biblatex-phys/phys.bbx
%{_texmfdistdir}/tex/latex/biblatex-phys/phys.cbx
%{_texmfdistdir}/tex/latex/biblatex-phys/phys.dbx

%package -n texlive-biblatex-publist
Version:        %{texlive_version}.%{texlive_noarch}.2.8svn70508
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX bibliography support for publication lists
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-publist-doc >= %{texlive_version}
Provides:       tex(publist.bbx)
Provides:       tex(publist.cbx)
Requires:       tex(numeric.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source247:      biblatex-publist.tar.xz
Source248:      biblatex-publist.doc.tar.xz

%description -n texlive-biblatex-publist
The package provides a BibLaTeX bibliography style file (*.bbx)
for publication lists. The style file draws on BibLaTeX's
authoryear style, but provides some extra features often
desired for publication lists, such as the omission of the
author's own name from author or editor data. At least version
3.4 of biblatex is required.

%package -n texlive-biblatex-publist-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.8svn70508
Release:        0
Summary:        Documentation for texlive-biblatex-publist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-publist and texlive-alldocumentation)

%description -n texlive-biblatex-publist-doc
This package includes the documentation for texlive-biblatex-publist

%post -n texlive-biblatex-publist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-publist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-publist
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-publist-doc
%{_texmfdistdir}/doc/latex/biblatex-publist/README
%{_texmfdistdir}/doc/latex/biblatex-publist/biblatex-publist.pdf
%{_texmfdistdir}/doc/latex/biblatex-publist/biblatex-publist.tex

%files -n texlive-biblatex-publist
%{_texmfdistdir}/tex/latex/biblatex-publist/publist.bbx
%{_texmfdistdir}/tex/latex/biblatex-publist/publist.cbx
%{_texmfdistdir}/tex/latex/biblatex-publist/publist.dbx

%package -n texlive-biblatex-readbbl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn61549
Release:        0
License:        LPPL-1.0
Summary:        Read a .bbl file created by biber
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-readbbl-doc >= %{texlive_version}
Provides:       tex(biblatex-readbbl.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source249:      biblatex-readbbl.tar.xz
Source250:      biblatex-readbbl.doc.tar.xz

%description -n texlive-biblatex-readbbl
This small package modifies the biblatex macro which reads a
.bbl file created by Biber. It is thus possible to include a
.bbl file into the main document with the filecontents
environment and send it to a publisher who does not need to run
the Biber program. However, when the bibliography changes one
has to create a new .bbl file.

%package -n texlive-biblatex-readbbl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn61549
Release:        0
Summary:        Documentation for texlive-biblatex-readbbl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-readbbl and texlive-alldocumentation)

%description -n texlive-biblatex-readbbl-doc
This package includes the documentation for texlive-biblatex-readbbl

%post -n texlive-biblatex-readbbl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-readbbl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-readbbl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-readbbl-doc
%{_texmfdistdir}/doc/latex/biblatex-readbbl/Changes
%{_texmfdistdir}/doc/latex/biblatex-readbbl/README
%{_texmfdistdir}/doc/latex/biblatex-readbbl/biblatex-readbbl.pdf
%{_texmfdistdir}/doc/latex/biblatex-readbbl/biblatex-readbbl.tex

%files -n texlive-biblatex-readbbl
%{_texmfdistdir}/tex/latex/biblatex-readbbl/biblatex-readbbl.sty

%package -n texlive-biblatex-realauthor
Version:        %{texlive_version}.%{texlive_noarch}.2.7.1asvn45865
Release:        0
License:        LPPL-1.0
Summary:        Indicate the real author of a work
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-realauthor-doc >= %{texlive_version}
Provides:       tex(realauthor.bbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source251:      biblatex-realauthor.tar.xz
Source252:      biblatex-realauthor.doc.tar.xz

%description -n texlive-biblatex-realauthor
This package allows to use a new field "realauthor", which
indicates the real author of a work, when published in a
pseudepigraphic name.

%package -n texlive-biblatex-realauthor-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.7.1asvn45865
Release:        0
Summary:        Documentation for texlive-biblatex-realauthor
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-realauthor and texlive-alldocumentation)

%description -n texlive-biblatex-realauthor-doc
This package includes the documentation for texlive-biblatex-realauthor

%post -n texlive-biblatex-realauthor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-realauthor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-realauthor
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-realauthor-doc
%{_texmfdistdir}/doc/latex/biblatex-realauthor/README
%{_texmfdistdir}/doc/latex/biblatex-realauthor/documentation/biblatex-realauthor.pdf
%{_texmfdistdir}/doc/latex/biblatex-realauthor/documentation/biblatex-realauthor.tex
%{_texmfdistdir}/doc/latex/biblatex-realauthor/documentation/example-realauthor.bib
%{_texmfdistdir}/doc/latex/biblatex-realauthor/documentation/example-realauthor.pdf
%{_texmfdistdir}/doc/latex/biblatex-realauthor/documentation/example-realauthor.tex
%{_texmfdistdir}/doc/latex/biblatex-realauthor/documentation/makefile
%{_texmfdistdir}/doc/latex/biblatex-realauthor/makefile

%files -n texlive-biblatex-realauthor
%{_texmfdistdir}/tex/latex/biblatex-realauthor/realauthor.bbx
%{_texmfdistdir}/tex/latex/biblatex-realauthor/realauthor.dbx

%package -n texlive-biblatex-sbl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn63639
Release:        0
License:        LPPL-1.0
Summary:        Society of Biblical Literature (SBL) style files for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-sbl-doc >= %{texlive_version}
Provides:       tex(american-sbl.lbx)
Provides:       tex(biblatex-sbl.def)
Provides:       tex(english-sbl.lbx)
Provides:       tex(german-sbl.lbx)
Provides:       tex(sbl-paper.sty)
Provides:       tex(sbl.bbx)
Provides:       tex(sbl.cbx)
Provides:       tex(spanish-sbl.lbx)
Requires:       tex(american.lbx)
Requires:       tex(biblatex.sty)
Requires:       tex(bibleref-parse.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(setspace.sty)
Requires:       tex(standard.bbx)
Requires:       tex(textcase.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source253:      biblatex-sbl.tar.xz
Source254:      biblatex-sbl.doc.tar.xz

%description -n texlive-biblatex-sbl
The package provides BibLaTeX support for citations in the
format specified by the second edition of the Society of
Biblical Literature (SBL) Handbook of Style. All example notes
and bibliography entries from the handbook are supported and
shown in an example file. A style file for writing SBL student
papers is also included.

%package -n texlive-biblatex-sbl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn63639
Release:        0
Summary:        Documentation for texlive-biblatex-sbl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-sbl and texlive-alldocumentation)

%description -n texlive-biblatex-sbl-doc
This package includes the documentation for texlive-biblatex-sbl

%post -n texlive-biblatex-sbl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-sbl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-sbl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-sbl-doc
%{_texmfdistdir}/doc/latex/biblatex-sbl/README.md
%{_texmfdistdir}/doc/latex/biblatex-sbl/biblatex-sbl-examples.pdf
%{_texmfdistdir}/doc/latex/biblatex-sbl/biblatex-sbl-examples.tex
%{_texmfdistdir}/doc/latex/biblatex-sbl/biblatex-sbl-ibid.pdf
%{_texmfdistdir}/doc/latex/biblatex-sbl/biblatex-sbl-ibid.tex
%{_texmfdistdir}/doc/latex/biblatex-sbl/biblatex-sbl.bib
%{_texmfdistdir}/doc/latex/biblatex-sbl/biblatex-sbl.pdf
%{_texmfdistdir}/doc/latex/biblatex-sbl/biblatex-sbl.tex
%{_texmfdistdir}/doc/latex/biblatex-sbl/sbl-paper.pdf
%{_texmfdistdir}/doc/latex/biblatex-sbl/sbl-paper.tex

%files -n texlive-biblatex-sbl
%{_texmfdistdir}/makeindex/biblatex-sbl/sbl-paper-bibleref.ist
%{_texmfdistdir}/tex/latex/biblatex-sbl/american-sbl.lbx
%{_texmfdistdir}/tex/latex/biblatex-sbl/biblatex-sbl.def
%{_texmfdistdir}/tex/latex/biblatex-sbl/english-sbl.lbx
%{_texmfdistdir}/tex/latex/biblatex-sbl/german-sbl.lbx
%{_texmfdistdir}/tex/latex/biblatex-sbl/sbl-paper.sty
%{_texmfdistdir}/tex/latex/biblatex-sbl/sbl.bbx
%{_texmfdistdir}/tex/latex/biblatex-sbl/sbl.cbx
%{_texmfdistdir}/tex/latex/biblatex-sbl/sbl.dbx
%{_texmfdistdir}/tex/latex/biblatex-sbl/spanish-sbl.lbx

%package -n texlive-biblatex-science
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn48945
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX implementation of the Science bibliography style
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-science-doc >= %{texlive_version}
Provides:       tex(science.bbx)
Provides:       tex(science.cbx)
Requires:       tex(numeric-comp.bbx)
Requires:       tex(numeric-comp.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source255:      biblatex-science.tar.xz
Source256:      biblatex-science.doc.tar.xz

%description -n texlive-biblatex-science
The bundle offers styles that allow authors to use BibLaTeX
when preparing papers for submission to the journal Science.

%package -n texlive-biblatex-science-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn48945
Release:        0
Summary:        Documentation for texlive-biblatex-science
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-science and texlive-alldocumentation)

%description -n texlive-biblatex-science-doc
This package includes the documentation for texlive-biblatex-science

%post -n texlive-biblatex-science
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-science
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-science
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-science-doc
%{_texmfdistdir}/doc/latex/biblatex-science/LICENSE.md
%{_texmfdistdir}/doc/latex/biblatex-science/README.md
%{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.bib
%{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.pdf
%{_texmfdistdir}/doc/latex/biblatex-science/biblatex-science.tex

%files -n texlive-biblatex-science
%{_texmfdistdir}/tex/latex/biblatex-science/science.bbx
%{_texmfdistdir}/tex/latex/biblatex-science/science.cbx

%package -n texlive-biblatex-shortfields
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn45858
Release:        0
License:        LPPL-1.0
Summary:        Use short forms of fields with BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-shortfields-doc >= %{texlive_version}
Provides:       tex(biblatex-shortfields.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source257:      biblatex-shortfields.tar.xz
Source258:      biblatex-shortfields.doc.tar.xz

%description -n texlive-biblatex-shortfields
The BibLaTeX package provides shortseries and shortjournal
field, but the default styles don't use them. It also provides
a mechanism to print the equivalence between short forms of
fields and long fields (\printbiblist), but this mechanism does
not allow to mix between different type of short fields, for
example, between short forms of journal title and short forms
of series titles. This package provides a solution to these two
problems: If a shortjournal field is defined, it prints it
instead of the \journal field. If a shortseries field is
defined, it prints it instead of the \series field. It provides
a \printbibshortfields command to print a list of the sort
forms of the fields. This list also includes the claves defined
with the biblatex-claves package version 1.2 or later.

%package -n texlive-biblatex-shortfields-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn45858
Release:        0
Summary:        Documentation for texlive-biblatex-shortfields
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-shortfields and texlive-alldocumentation)

%description -n texlive-biblatex-shortfields-doc
This package includes the documentation for texlive-biblatex-shortfields

%post -n texlive-biblatex-shortfields
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-shortfields
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-shortfields
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-shortfields-doc
%{_texmfdistdir}/doc/latex/biblatex-shortfields/README
%{_texmfdistdir}/doc/latex/biblatex-shortfields/documentation/biblatex-shortfields-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-shortfields/documentation/biblatex-shortfields-example.tex
%{_texmfdistdir}/doc/latex/biblatex-shortfields/documentation/biblatex-shortfields.bib
%{_texmfdistdir}/doc/latex/biblatex-shortfields/documentation/biblatex-shortfields.pdf
%{_texmfdistdir}/doc/latex/biblatex-shortfields/documentation/biblatex-shortfields.tex
%{_texmfdistdir}/doc/latex/biblatex-shortfields/documentation/latexmkrc
%{_texmfdistdir}/doc/latex/biblatex-shortfields/documentation/makefile
%{_texmfdistdir}/doc/latex/biblatex-shortfields/makefile

%files -n texlive-biblatex-shortfields
%{_texmfdistdir}/tex/latex/biblatex-shortfields/biblatex-shortfields.sty

%package -n texlive-biblatex-socialscienceshuberlin
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.1svn47839
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX-style for the social sciences at HU Berlin
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-socialscienceshuberlin-doc >= %{texlive_version}
Provides:       tex(german-socialscienceshuberlin.lbx)
Provides:       tex(socialscienceshuberlin.bbx)
Provides:       tex(socialscienceshuberlin.cbx)
Requires:       tex(ext-authoryear.bbx)
Requires:       tex(ext-authoryear.cbx)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source259:      biblatex-socialscienceshuberlin.tar.xz
Source260:      biblatex-socialscienceshuberlin.doc.tar.xz

%description -n texlive-biblatex-socialscienceshuberlin
This is a BibLaTeX style for the social sciences at the
Humboldt-Universitat zu Berlin.

%package -n texlive-biblatex-socialscienceshuberlin-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.1svn47839
Release:        0
Summary:        Documentation for texlive-biblatex-socialscienceshuberlin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-socialscienceshuberlin and texlive-alldocumentation)

%description -n texlive-biblatex-socialscienceshuberlin-doc
This package includes the documentation for texlive-biblatex-socialscienceshuberlin

%post -n texlive-biblatex-socialscienceshuberlin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-socialscienceshuberlin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-socialscienceshuberlin
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-socialscienceshuberlin-doc
%{_texmfdistdir}/doc/latex/biblatex-socialscienceshuberlin/README.md
%{_texmfdistdir}/doc/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin-examples.bib
%{_texmfdistdir}/doc/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.pdf
%{_texmfdistdir}/doc/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.tex

%files -n texlive-biblatex-socialscienceshuberlin
%{_texmfdistdir}/tex/latex/biblatex-socialscienceshuberlin/german-socialscienceshuberlin.lbx
%{_texmfdistdir}/tex/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.bbx
%{_texmfdistdir}/tex/latex/biblatex-socialscienceshuberlin/socialscienceshuberlin.cbx

%package -n texlive-biblatex-software
Version:        %{texlive_version}.%{texlive_noarch}.1.2_5svn64030
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX stylefiles for software products
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-software-doc >= %{texlive_version}
Provides:       tex(english-software.lbx)
Provides:       tex(french-software.lbx)
Provides:       tex(software-biblatex.sty)
Provides:       tex(software.bbx)
Requires:       tex(english.lbx)
Requires:       tex(french.lbx)
Requires:       tex(xurl.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source261:      biblatex-software.tar.xz
Source262:      biblatex-software.doc.tar.xz

%description -n texlive-biblatex-software
This package implements software entry types for BibLaTeX in
the form of a bibliography style extension. It requires the
Biber backend.

%package -n texlive-biblatex-software-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2_5svn64030
Release:        0
Summary:        Documentation for texlive-biblatex-software
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-software and texlive-alldocumentation)

%description -n texlive-biblatex-software-doc
This package includes the documentation for texlive-biblatex-software

%post -n texlive-biblatex-software
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-software
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-software
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-software-doc
%{_texmfdistdir}/doc/latex/biblatex-software/Changes
%{_texmfdistdir}/doc/latex/biblatex-software/LICENSE
%{_texmfdistdir}/doc/latex/biblatex-software/README.md
%{_texmfdistdir}/doc/latex/biblatex-software/biblio.bib
%{_texmfdistdir}/doc/latex/biblatex-software/manual.bib
%{_texmfdistdir}/doc/latex/biblatex-software/mkbiblatexstubs.sh
%{_texmfdistdir}/doc/latex/biblatex-software/sample-content.tex
%{_texmfdistdir}/doc/latex/biblatex-software/sample-use-sty.pdf
%{_texmfdistdir}/doc/latex/biblatex-software/sample-use-sty.tex
%{_texmfdistdir}/doc/latex/biblatex-software/sample.tex
%{_texmfdistdir}/doc/latex/biblatex-software/software-biblatex.pdf
%{_texmfdistdir}/doc/latex/biblatex-software/software-biblatex.tex
%{_texmfdistdir}/doc/latex/biblatex-software/stublist
%{_texmfdistdir}/doc/latex/biblatex-software/swentries.tex

%files -n texlive-biblatex-software
%{_texmfdistdir}/tex/latex/biblatex-software/english-software.lbx
%{_texmfdistdir}/tex/latex/biblatex-software/french-software.lbx
%{_texmfdistdir}/tex/latex/biblatex-software/software-biblatex.sty
%{_texmfdistdir}/tex/latex/biblatex-software/software.bbx
%{_texmfdistdir}/tex/latex/biblatex-software/software.dbx

%package -n texlive-biblatex-source-division
Version:        %{texlive_version}.%{texlive_noarch}.2.4.2svn45379
Release:        0
License:        LPPL-1.0
Summary:        References by "division" in classical sources
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-source-division-doc >= %{texlive_version}
Provides:       tex(biblatex-source-division.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source263:      biblatex-source-division.tar.xz
Source264:      biblatex-source-division.doc.tar.xz

%description -n texlive-biblatex-source-division
The package enables the user to make reference to "division
marks" (such as book, chapter, section), in the document being
referenced, in addition to the page-based references that
BibTeX-based citations have always had. The citation is made in
the same way as the LaTeX standard, but what's inside the
square brackets may include the "division" specification, as in
\cite[(<division spec.>)<page number>]{<document>}

%package -n texlive-biblatex-source-division-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4.2svn45379
Release:        0
Summary:        Documentation for texlive-biblatex-source-division
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-source-division and texlive-alldocumentation)

%description -n texlive-biblatex-source-division-doc
This package includes the documentation for texlive-biblatex-source-division

%post -n texlive-biblatex-source-division
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-source-division
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-source-division
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-source-division-doc
%{_texmfdistdir}/doc/latex/biblatex-source-division/README
%{_texmfdistdir}/doc/latex/biblatex-source-division/biblatex-source-division.bib
%{_texmfdistdir}/doc/latex/biblatex-source-division/biblatex-source-division.pdf
%{_texmfdistdir}/doc/latex/biblatex-source-division/biblatex-source-division.tex
%{_texmfdistdir}/doc/latex/biblatex-source-division/latexmkrc
%{_texmfdistdir}/doc/latex/biblatex-source-division/makefile

%files -n texlive-biblatex-source-division
%{_texmfdistdir}/tex/latex/biblatex-source-division/biblatex-source-division.sty

%package -n texlive-biblatex-spbasic
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn61439
Release:        0
License:        LPPL-1.0
Summary:        A BibLaTeX style emulating Springer's old spbasic.bst
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-spbasic-doc >= %{texlive_version}
Provides:       tex(biblatex-spbasic.bbx)
Provides:       tex(biblatex-spbasic.cbx)
Provides:       tex(biblatex-spbasic.lbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(authoryear.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source265:      biblatex-spbasic.tar.xz
Source266:      biblatex-spbasic.doc.tar.xz

%description -n texlive-biblatex-spbasic
This package provides a bibliography and citation style for
BibLaTeX/biber for typesetting articles for Springer's
journals. It is the same as the old BibTeX style spbasic.bst.

%package -n texlive-biblatex-spbasic-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn61439
Release:        0
Summary:        Documentation for texlive-biblatex-spbasic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-spbasic and texlive-alldocumentation)

%description -n texlive-biblatex-spbasic-doc
This package includes the documentation for texlive-biblatex-spbasic

%post -n texlive-biblatex-spbasic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-spbasic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-spbasic
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-spbasic-doc
%{_texmfdistdir}/doc/latex/biblatex-spbasic/Changes
%{_texmfdistdir}/doc/latex/biblatex-spbasic/README
%{_texmfdistdir}/doc/latex/biblatex-spbasic/biblatex-spbasic.bib
%{_texmfdistdir}/doc/latex/biblatex-spbasic/biblatex-spbasic.pdf
%{_texmfdistdir}/doc/latex/biblatex-spbasic/biblatex-spbasic.tex

%files -n texlive-biblatex-spbasic
%{_texmfdistdir}/tex/latex/biblatex-spbasic/biblatex-spbasic.bbx
%{_texmfdistdir}/tex/latex/biblatex-spbasic/biblatex-spbasic.cbx
%{_texmfdistdir}/tex/latex/biblatex-spbasic/biblatex-spbasic.lbx

%package -n texlive-biblatex-subseries
Version:        %{texlive_version}.%{texlive_noarch}.1.2.0svn43330
Release:        0
License:        LPPL-1.0
Summary:        Manages subseries with BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-subseries-doc >= %{texlive_version}
Provides:       tex(subseries.bbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source267:      biblatex-subseries.tar.xz
Source268:      biblatex-subseries.doc.tar.xz

%description -n texlive-biblatex-subseries
Some publishers organize book series with subseries. In this
case, two numbers are associated with one volume: the number
inside the series and the number inside the subseries. That is
the case of the series Corpus Scriptorium Christianorum
Orientalium published by Peeters. This package provides new
fields to manage such system.

%package -n texlive-biblatex-subseries-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2.0svn43330
Release:        0
Summary:        Documentation for texlive-biblatex-subseries
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-subseries and texlive-alldocumentation)

%description -n texlive-biblatex-subseries-doc
This package includes the documentation for texlive-biblatex-subseries

%post -n texlive-biblatex-subseries
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-subseries
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-subseries
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-subseries-doc
%{_texmfdistdir}/doc/latex/biblatex-subseries/README
%{_texmfdistdir}/doc/latex/biblatex-subseries/documentation/biblatex-subseries-example.bib
%{_texmfdistdir}/doc/latex/biblatex-subseries/documentation/biblatex-subseries-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-subseries/documentation/biblatex-subseries-example.tex
%{_texmfdistdir}/doc/latex/biblatex-subseries/documentation/biblatex-subseries.pdf
%{_texmfdistdir}/doc/latex/biblatex-subseries/documentation/biblatex-subseries.tex
%{_texmfdistdir}/doc/latex/biblatex-subseries/documentation/makefile
%{_texmfdistdir}/doc/latex/biblatex-subseries/makefile

%files -n texlive-biblatex-subseries
%{_texmfdistdir}/tex/latex/biblatex-subseries/subseries.bbx
%{_texmfdistdir}/tex/latex/biblatex-subseries/subseries.dbx

%package -n texlive-biblatex-swiss-legal
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2asvn64491
Release:        0
License:        LPPL-1.0
Summary:        Bibliography and citation styles following Swiss legal practice
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-swiss-legal-doc >= %{texlive_version}
Provides:       tex(biblatex-swiss-legal-base.bbx)
Provides:       tex(biblatex-swiss-legal-base.cbx)
Provides:       tex(biblatex-swiss-legal-bibliography.bbx)
Provides:       tex(biblatex-swiss-legal-bibliography.cbx)
Provides:       tex(biblatex-swiss-legal-de.lbx)
Provides:       tex(biblatex-swiss-legal-fr.lbx)
Provides:       tex(biblatex-swiss-legal-general.bbx)
Provides:       tex(biblatex-swiss-legal-general.cbx)
Provides:       tex(biblatex-swiss-legal-longarticle.bbx)
Provides:       tex(biblatex-swiss-legal-longarticle.cbx)
Provides:       tex(biblatex-swiss-legal-shortarticle.bbx)
Provides:       tex(biblatex-swiss-legal-shortarticle.cbx)
Requires:       tex(amssymb.sty)
Requires:       tex(french.lbx)
Requires:       tex(ngerman.lbx)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source269:      biblatex-swiss-legal.tar.xz
Source270:      biblatex-swiss-legal.doc.tar.xz

%description -n texlive-biblatex-swiss-legal
The package provides BibLaTeX bibliography and citation styles
for documents written in accordance with Swiss legal citation
standards in either French or German. However, according to
https://tex.stackexchange.com/questions/426142/bibliography-usi
ng-biblatex-swiss-legal-not-displayed-correctly the package is
at present outdated and does not work properly with newer
versions of BibLaTeX.

%package -n texlive-biblatex-swiss-legal-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2asvn64491
Release:        0
Summary:        Documentation for texlive-biblatex-swiss-legal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-swiss-legal and texlive-alldocumentation)
Provides:       locale(texlive-biblatex-swiss-legal-doc:fr)

%description -n texlive-biblatex-swiss-legal-doc
This package includes the documentation for texlive-biblatex-swiss-legal

%post -n texlive-biblatex-swiss-legal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-swiss-legal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-swiss-legal
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-swiss-legal-doc
%{_texmfdistdir}/doc/latex/biblatex-swiss-legal/README
%{_texmfdistdir}/doc/latex/biblatex-swiss-legal/biblatex-swiss-legal.pdf
%{_texmfdistdir}/doc/latex/biblatex-swiss-legal/doc_source/biblatex-swiss-legal.bib
%{_texmfdistdir}/doc/latex/biblatex-swiss-legal/doc_source/biblatex-swiss-legal.tex

%files -n texlive-biblatex-swiss-legal
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-base.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-base.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-bibliography.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-bibliography.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-de.lbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-fr.lbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-general.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-longarticle.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-longarticle.cbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-shortarticle.bbx
%{_texmfdistdir}/tex/latex/biblatex-swiss-legal/biblatex-swiss-legal-shortarticle.cbx

%package -n texlive-biblatex-trad
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn58169
Release:        0
License:        LPPL-1.0
Summary:        "Traditional" BibTeX styles with BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-trad-doc >= %{texlive_version}
Provides:       tex(trad-abbrv.bbx)
Provides:       tex(trad-abbrv.cbx)
Provides:       tex(trad-alpha.bbx)
Provides:       tex(trad-alpha.cbx)
Provides:       tex(trad-plain.bbx)
Provides:       tex(trad-plain.cbx)
Provides:       tex(trad-standard.bbx)
Provides:       tex(trad-standard.cbx)
Provides:       tex(trad-unsrt.bbx)
Provides:       tex(trad-unsrt.cbx)
Requires:       tex(alphabetic.cbx)
Requires:       tex(numeric.cbx)
Requires:       tex(standard.bbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source271:      biblatex-trad.tar.xz
Source272:      biblatex-trad.doc.tar.xz

%description -n texlive-biblatex-trad
The bundle provides implementations of the "traditional" BibTeX
styles (plain, abbrev, unsrt and alpha) with BibLaTeX.

%package -n texlive-biblatex-trad-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn58169
Release:        0
Summary:        Documentation for texlive-biblatex-trad
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-trad and texlive-alldocumentation)

%description -n texlive-biblatex-trad-doc
This package includes the documentation for texlive-biblatex-trad

%post -n texlive-biblatex-trad
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-trad
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-trad
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-trad-doc
%{_texmfdistdir}/doc/latex/biblatex-trad/README.md
%{_texmfdistdir}/doc/latex/biblatex-trad/biblatex-trad.pdf
%{_texmfdistdir}/doc/latex/biblatex-trad/biblatex-trad.tex

%files -n texlive-biblatex-trad
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-abbrv.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-abbrv.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-alpha.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-alpha.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-plain.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-plain.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-standard.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-standard.cbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-unsrt.bbx
%{_texmfdistdir}/tex/latex/biblatex-trad/trad-unsrt.cbx

%package -n texlive-biblatex-true-citepages-omit
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn44653
Release:        0
License:        LPPL-1.0
Summary:        Correction of some limitation of the citepages=omit option of BibLaTeX styles
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-true-citepages-omit-doc >= %{texlive_version}
Provides:       tex(biblatex-true-citepages-omit.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source273:      biblatex-true-citepages-omit.tar.xz
Source274:      biblatex-true-citepages-omit.doc.tar.xz

%description -n texlive-biblatex-true-citepages-omit
This package deals with a limitation of the citepages=omit
option of the verbose family of BibLaTeX citestyles. The option
works when you \cite[xx]{key}, but not when you \cite[\pno~xx,
some text]{key}. The package corrects this problem.

%package -n texlive-biblatex-true-citepages-omit-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn44653
Release:        0
Summary:        Documentation for texlive-biblatex-true-citepages-omit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-true-citepages-omit and texlive-alldocumentation)

%description -n texlive-biblatex-true-citepages-omit-doc
This package includes the documentation for texlive-biblatex-true-citepages-omit

%post -n texlive-biblatex-true-citepages-omit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-true-citepages-omit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-true-citepages-omit
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-true-citepages-omit-doc
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/README
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit-example.pdf
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit-example.tex
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.bib
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.pdf
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.tex
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/example.bib
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/latexmkrc
%{_texmfdistdir}/doc/latex/biblatex-true-citepages-omit/makefile

%files -n texlive-biblatex-true-citepages-omit
%{_texmfdistdir}/tex/latex/biblatex-true-citepages-omit/biblatex-true-citepages-omit.sty

%package -n texlive-biblatex-unified
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn64975
Release:        0
License:        LPPL-1.0
Summary:        BibLaTeX implementation of the unified stylesheet for linguistics journals
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-unified-doc >= %{texlive_version}
Provides:       tex(unified.bbx)
Provides:       tex(unified.cbx)
Requires:       tex(authoryear-comp.cbx)
Requires:       tex(authoryear.bbx)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source275:      biblatex-unified.tar.xz
Source276:      biblatex-unified.doc.tar.xz

%description -n texlive-biblatex-unified
BibLaTeX-unified is an opinionated BibLaTeX implementation of
the Unified Stylesheet for Linguistics Journals

%package -n texlive-biblatex-unified-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn64975
Release:        0
Summary:        Documentation for texlive-biblatex-unified
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-unified and texlive-alldocumentation)

%description -n texlive-biblatex-unified-doc
This package includes the documentation for texlive-biblatex-unified

%post -n texlive-biblatex-unified
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-unified
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-unified
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-unified-doc
%{_texmfdistdir}/doc/latex/biblatex-unified/JournalUnifiedStyleSheet2007.pdf
%{_texmfdistdir}/doc/latex/biblatex-unified/LICENSE
%{_texmfdistdir}/doc/latex/biblatex-unified/README.md
%{_texmfdistdir}/doc/latex/biblatex-unified/biblatex-unified.md
%{_texmfdistdir}/doc/latex/biblatex-unified/biblatex-unified.pdf
%{_texmfdistdir}/doc/latex/biblatex-unified/biblatex-unified.tex
%{_texmfdistdir}/doc/latex/biblatex-unified/unified-test.bib
%{_texmfdistdir}/doc/latex/biblatex-unified/unified-test.pdf
%{_texmfdistdir}/doc/latex/biblatex-unified/unified-test.tex

%files -n texlive-biblatex-unified
%{_texmfdistdir}/tex/latex/biblatex-unified/unified.bbx
%{_texmfdistdir}/tex/latex/biblatex-unified/unified.cbx

%package -n texlive-biblatex-vancouver
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn55339
Release:        0
License:        GPL-2.0-or-later
Summary:        Vancouver style for BibLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex-vancouver-doc >= %{texlive_version}
Provides:       tex(vancouver.bbx)
Provides:       tex(vancouver.cbx)
Requires:       tex(ifthen.sty)
Requires:       tex(numeric.bbx)
Requires:       tex(numeric.cbx)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source277:      biblatex-vancouver.tar.xz
Source278:      biblatex-vancouver.doc.tar.xz

%description -n texlive-biblatex-vancouver
This package provides the Vancouver reference style for
BibLaTeX. It is based on the numeric style and requires biber.

%package -n texlive-biblatex-vancouver-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn55339
Release:        0
Summary:        Documentation for texlive-biblatex-vancouver
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex-vancouver and texlive-alldocumentation)

%description -n texlive-biblatex-vancouver-doc
This package includes the documentation for texlive-biblatex-vancouver

%post -n texlive-biblatex-vancouver
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex-vancouver
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex-vancouver
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex-vancouver-doc
%{_texmfdistdir}/doc/latex/biblatex-vancouver/LICENSE
%{_texmfdistdir}/doc/latex/biblatex-vancouver/README

%files -n texlive-biblatex-vancouver
%{_texmfdistdir}/tex/latex/biblatex-vancouver/vancouver.bbx
%{_texmfdistdir}/tex/latex/biblatex-vancouver/vancouver.cbx

%package -n texlive-biblatex2bibitem
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.2svn67201
Release:        0
License:        LPPL-1.0
Summary:        Convert BibLaTeX-generated bibliography to bibitems
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblatex2bibitem-doc >= %{texlive_version}
Provides:       tex(biblatex2bibitem.sty)
Requires:       tex(biblatex.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source279:      biblatex2bibitem.tar.xz
Source280:      biblatex2bibitem.doc.tar.xz

%description -n texlive-biblatex2bibitem
Some journals accept the reference list only as \bibitems. If
you use BibTeX, there is no problem: just paste the content of
the .bbl file into your document. However, there was no
out-of-the-box way to do the same for biblatex, and you had to
struggle with searching appropriate .bst files, or formatting
your reference list by hand, or something like that. Using the
workaround provided by this package solves the problem.

%package -n texlive-biblatex2bibitem-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.2svn67201
Release:        0
Summary:        Documentation for texlive-biblatex2bibitem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblatex2bibitem and texlive-alldocumentation)

%description -n texlive-biblatex2bibitem-doc
This package includes the documentation for texlive-biblatex2bibitem

%post -n texlive-biblatex2bibitem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblatex2bibitem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblatex2bibitem
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblatex2bibitem-doc
%{_texmfdistdir}/doc/latex/biblatex2bibitem/LICENSE.txt
%{_texmfdistdir}/doc/latex/biblatex2bibitem/README.md
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-examples.bib
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref-result.pdf
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref-result.tex
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref.pdf
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-hyperref.tex
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe-result.pdf
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe-result.tex
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe.pdf
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-mwe.tex
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-new-result.pdf
%{_texmfdistdir}/doc/latex/biblatex2bibitem/biblatex2bibitem-new.pdf

%files -n texlive-biblatex2bibitem
%{_texmfdistdir}/tex/latex/biblatex2bibitem/biblatex2bibitem.sty

%package -n texlive-bibleref
Version:        %{texlive_version}.%{texlive_noarch}.1.25svn55626
Release:        0
License:        LPPL-1.0
Summary:        Format bible citations
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibleref-doc >= %{texlive_version}
Provides:       tex(bibleref-xidx.sty)
Provides:       tex(bibleref.sty)
Requires:       tex(amsgen.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source281:      bibleref.tar.xz
Source282:      bibleref.doc.tar.xz

%description -n texlive-bibleref
The bibleref package offers consistent formatting of references
to parts of the Christian bible, in a number of well-defined
formats. It depends on ifthen, fmtcount, and amsgen.

%package -n texlive-bibleref-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.25svn55626
Release:        0
Summary:        Documentation for texlive-bibleref
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibleref and texlive-alldocumentation)

%description -n texlive-bibleref-doc
This package includes the documentation for texlive-bibleref

%post -n texlive-bibleref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibleref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibleref
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibleref-doc
%{_texmfdistdir}/doc/latex/bibleref/CHANGES
%{_texmfdistdir}/doc/latex/bibleref/README
%{_texmfdistdir}/doc/latex/bibleref/bibleref.pdf
%{_texmfdistdir}/doc/latex/bibleref/makefile
%{_texmfdistdir}/doc/latex/bibleref/sample.ist
%{_texmfdistdir}/doc/latex/bibleref/samples/sample-categories.pdf
%{_texmfdistdir}/doc/latex/bibleref/samples/sample-indextools.pdf
%{_texmfdistdir}/doc/latex/bibleref/samples/sample-xidx.pdf
%{_texmfdistdir}/doc/latex/bibleref/samples/sample.pdf

%files -n texlive-bibleref
%{_texmfdistdir}/tex/latex/bibleref/bibleref-xidx.sty
%{_texmfdistdir}/tex/latex/bibleref/bibleref.sty

%package -n texlive-bibleref-french
Version:        %{texlive_version}.%{texlive_noarch}.2.3.3svn53138
Release:        0
License:        LPPL-1.0
Summary:        French translations for bibleref
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibleref-french-doc >= %{texlive_version}
Provides:       tex(bibleref-french.sty)
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source283:      bibleref-french.tar.xz
Source284:      bibleref-french.doc.tar.xz

%description -n texlive-bibleref-french
The package provides translations and alternative typesetting
conventions for use of bibleref in French.

%package -n texlive-bibleref-french-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3.3svn53138
Release:        0
Summary:        Documentation for texlive-bibleref-french
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibleref-french and texlive-alldocumentation)
Provides:       locale(texlive-bibleref-french-doc:fr;en)

%description -n texlive-bibleref-french-doc
This package includes the documentation for texlive-bibleref-french

%post -n texlive-bibleref-french
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibleref-french
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibleref-french
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibleref-french-doc
%{_texmfdistdir}/doc/latex/bibleref-french/Lacroux-Bible.pdf
%{_texmfdistdir}/doc/latex/bibleref-french/README
%{_texmfdistdir}/doc/latex/bibleref-french/bible.bib
%{_texmfdistdir}/doc/latex/bibleref-french/bibleref-french-francais.pdf
%{_texmfdistdir}/doc/latex/bibleref-french/bibleref-french-francais.tex
%{_texmfdistdir}/doc/latex/bibleref-french/bibleref-french.pdf
%{_texmfdistdir}/doc/latex/bibleref-french/livres.tex
%{_texmfdistdir}/doc/latex/bibleref-french/makefile
%{_texmfdistdir}/doc/latex/bibleref-french/styles.tex
%{_texmfdistdir}/doc/latex/bibleref-french/test.tex

%files -n texlive-bibleref-french
%{_texmfdistdir}/tex/latex/bibleref-french/bibleref-french.sty

%package -n texlive-bibleref-german
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn21923
Release:        0
License:        LPPL-1.0
Summary:        German adaptation of bibleref
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibleref-german-doc >= %{texlive_version}
Provides:       tex(bibleref-german.sty)
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source285:      bibleref-german.tar.xz
Source286:      bibleref-german.doc.tar.xz

%description -n texlive-bibleref-german
The package provides translations and various formats for the
use of bibleref in German documents. The German naming of the
bible books complies with the 'Loccumer Richtlinien' (Locum
guidelines). In addition, the Vulgate (Latin bible) is
supported.

%package -n texlive-bibleref-german-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn21923
Release:        0
Summary:        Documentation for texlive-bibleref-german
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibleref-german and texlive-alldocumentation)
Provides:       locale(texlive-bibleref-german-doc:de;en)

%description -n texlive-bibleref-german-doc
This package includes the documentation for texlive-bibleref-german

%post -n texlive-bibleref-german
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibleref-german
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibleref-german
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibleref-german-doc
%{_texmfdistdir}/doc/latex/bibleref-german/CHANGES
%{_texmfdistdir}/doc/latex/bibleref-german/LIESMICH
%{_texmfdistdir}/doc/latex/bibleref-german/README
%{_texmfdistdir}/doc/latex/bibleref-german/bibleref-german-preamble.tex
%{_texmfdistdir}/doc/latex/bibleref-german/bibleref-german-print.tex
%{_texmfdistdir}/doc/latex/bibleref-german/bibleref-german-screen.tex
%{_texmfdistdir}/doc/latex/bibleref-german/de-bibleref-german.pdf
%{_texmfdistdir}/doc/latex/bibleref-german/de-bibleref-german.tex
%{_texmfdistdir}/doc/latex/bibleref-german/en-bibleref-german.pdf
%{_texmfdistdir}/doc/latex/bibleref-german/en-bibleref-german.tex

%files -n texlive-bibleref-german
%{_texmfdistdir}/tex/latex/bibleref-german/bibleref-german.sty

%package -n texlive-bibleref-lds
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25526
Release:        0
License:        LPPL-1.0
Summary:        Bible references, including those to the scriptures of the Church of Jesus Christ of Latter Day Saints
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibleref-lds-doc >= %{texlive_version}
Provides:       tex(bibleref-lds.sty)
Requires:       tex(bibleref-mouth.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source287:      bibleref-lds.tar.xz
Source288:      bibleref-lds.doc.tar.xz

%description -n texlive-bibleref-lds
The package extends the bibleref-mouth package to support
references to the scriptures of The Church of Jesus Christ of
Latter-day Saints (LDS). The package requires bibleref-mouth to
run, and its reference syntax is the same as that of the parent
package.

%package -n texlive-bibleref-lds-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25526
Release:        0
Summary:        Documentation for texlive-bibleref-lds
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibleref-lds and texlive-alldocumentation)

%description -n texlive-bibleref-lds-doc
This package includes the documentation for texlive-bibleref-lds

%post -n texlive-bibleref-lds
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibleref-lds
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibleref-lds
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibleref-lds-doc
%{_texmfdistdir}/doc/latex/bibleref-lds/README
%{_texmfdistdir}/doc/latex/bibleref-lds/bibleref-lds.pdf

%files -n texlive-bibleref-lds
%{_texmfdistdir}/tex/latex/bibleref-lds/bibleref-lds.sty

%package -n texlive-bibleref-mouth
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25527
Release:        0
License:        LPPL-1.0
Summary:        Consistent formatting of Bible references
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibleref-mouth-doc >= %{texlive_version}
Provides:       tex(bibleref-mouth.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(hyperref.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source289:      bibleref-mouth.tar.xz
Source290:      bibleref-mouth.doc.tar.xz

%description -n texlive-bibleref-mouth
The package allows Bible references to be formatted in a
consistent way. It is similar to the bibleref package, except
that the formatting macros are all purely expandable -- that
is, they are all implemented in TeX's mouth. This means that
they can be used in any expandable context, such as an argument
to a \url command.

%package -n texlive-bibleref-mouth-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn25527
Release:        0
Summary:        Documentation for texlive-bibleref-mouth
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibleref-mouth and texlive-alldocumentation)

%description -n texlive-bibleref-mouth-doc
This package includes the documentation for texlive-bibleref-mouth

%post -n texlive-bibleref-mouth
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibleref-mouth
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibleref-mouth
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibleref-mouth-doc
%{_texmfdistdir}/doc/latex/bibleref-mouth/README
%{_texmfdistdir}/doc/latex/bibleref-mouth/bibleref-mouth.pdf

%files -n texlive-bibleref-mouth
%{_texmfdistdir}/tex/latex/bibleref-mouth/bibleref-mouth.sty

%package -n texlive-bibleref-parse
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn22054
Release:        0
License:        LPPL-1.0
Summary:        Specify Bible passages in human-readable format
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibleref-parse-doc >= %{texlive_version}
Provides:       tex(bibleref-parse.sty)
Requires:       tex(bibleref.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(scrlfile.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source291:      bibleref-parse.tar.xz
Source292:      bibleref-parse.doc.tar.xz

%description -n texlive-bibleref-parse
The package parses Bible passages that are given in human
readable format. It accepts a wide variety of formats. This
allows for a simpler and more convenient interface to the
functionality of the bibleref package.

%package -n texlive-bibleref-parse-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn22054
Release:        0
Summary:        Documentation for texlive-bibleref-parse
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibleref-parse and texlive-alldocumentation)

%description -n texlive-bibleref-parse-doc
This package includes the documentation for texlive-bibleref-parse

%post -n texlive-bibleref-parse
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibleref-parse
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibleref-parse
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibleref-parse-doc
%{_texmfdistdir}/doc/latex/bibleref-parse/README
%{_texmfdistdir}/doc/latex/bibleref-parse/bibleref-parse.pdf
%{_texmfdistdir}/doc/latex/bibleref-parse/bibleref-parse.tex

%files -n texlive-bibleref-parse
%{_texmfdistdir}/tex/latex/bibleref-parse/bibleref-parse.sty

%package -n texlive-bibletext
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.2svn45196
Release:        0
License:        LPPL-1.0
Summary:        Insert Bible passages by their reference
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibletext-doc >= %{texlive_version}
Provides:       tex(bibletext.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source293:      bibletext.tar.xz
Source294:      bibletext.doc.tar.xz

%description -n texlive-bibletext
The package allows to insert Bible texts in a document by
specifying references.

%package -n texlive-bibletext-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.2svn45196
Release:        0
Summary:        Documentation for texlive-bibletext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibletext and texlive-alldocumentation)

%description -n texlive-bibletext-doc
This package includes the documentation for texlive-bibletext

%post -n texlive-bibletext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibletext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibletext
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibletext-doc
%{_texmfdistdir}/doc/latex/bibletext/LICENSE
%{_texmfdistdir}/doc/latex/bibletext/README.md
%{_texmfdistdir}/doc/latex/bibletext/bibletext.pdf
%{_texmfdistdir}/doc/latex/bibletext/bibletext.tex

%files -n texlive-bibletext
%{_texmfdistdir}/tex/latex/bibletext/bibletext.sty

%package -n texlive-biblist
Version:        %{texlive_version}.%{texlive_noarch}.svn17116
Release:        0
License:        GPL-2.0-or-later
Summary:        Print a BibTeX database
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biblist-doc >= %{texlive_version}
Provides:       tex(biblist.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source295:      biblist.tar.xz
Source296:      biblist.doc.tar.xz

%description -n texlive-biblist
The package provides the means of listing an entire BibTeX
database, avoiding the potentially large (macro) impact
associated with \nocite{*}.

%package -n texlive-biblist-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17116
Release:        0
Summary:        Documentation for texlive-biblist
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biblist and texlive-alldocumentation)

%description -n texlive-biblist-doc
This package includes the documentation for texlive-biblist

%post -n texlive-biblist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biblist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biblist
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biblist-doc
%{_texmfdistdir}/doc/latex/biblist/README
%{_texmfdistdir}/doc/latex/biblist/biblist.bst-dist
%{_texmfdistdir}/doc/latex/biblist/biblist.gde
%{_texmfdistdir}/doc/latex/biblist/biblist.pdf
%{_texmfdistdir}/doc/latex/biblist/biblist.tex

%files -n texlive-biblist
%{_texmfdistdir}/tex/latex/biblist/biblist.sty

%package -n texlive-bibtex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.99dsvn70015
Release:        0
License:        SUSE-TeX
Summary:        Process bibliographies (bib files) for LaTeX or other formats
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtex-bin >= %{texlive_version}
#!BuildIgnore: texlive-bibtex-bin
Requires:       texlive-kpathsea >= %{texlive_version}
#!BuildIgnore: texlive-kpathsea
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibtex-doc >= %{texlive_version}
Provides:       tex(apalike.sty)
Provides:       tex(apalike.tex)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source297:      bibtex.tar.xz
Source298:      bibtex.doc.tar.xz

%description -n texlive-bibtex
BibTeX allows the user to store his citation data in generic
form, while printing citations in a document in the form
specified by a BibTeX style, to be specified in the document
itself (one often needs a LaTeX citation-style package, such as
natbib, as well). BibTeX knows nothing about Unicode sorting
algorithms or scripts, although it will pass on whatever bytes
it reads. Its descendant bibtexu does support Unicode, via the
ICU library. The older alternative bibtex8 supports 8-bit
character sets. Another Unicode-aware alternative is the
(independently developed) biber program, used with the BibLaTeX
package to typeset its output.

%package -n texlive-bibtex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.99dsvn70015
Release:        0
Summary:        Documentation for texlive-bibtex
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibtex and texlive-alldocumentation)
Provides:       man(bibtex.1)

%description -n texlive-bibtex-doc
This package includes the documentation for texlive-bibtex

%post -n texlive-bibtex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibtex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibtex
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibtex-doc
%{_texmfdistdir}/doc/bibtex/base/README
%{_texmfdistdir}/doc/bibtex/base/btxbst.doc
%{_texmfdistdir}/doc/bibtex/base/btxdoc.bib
%{_texmfdistdir}/doc/bibtex/base/btxdoc.pdf
%{_texmfdistdir}/doc/bibtex/base/btxdoc.tex
%{_texmfdistdir}/doc/bibtex/base/btxhak.pdf
%{_texmfdistdir}/doc/bibtex/base/btxhak.tex
%{_mandir}/man1/bibtex.1*

%files -n texlive-bibtex
%{_texmfdistdir}/bibtex/bib/base/xampl.bib
%{_texmfdistdir}/bibtex/bst/base/abbrv.bst
%{_texmfdistdir}/bibtex/bst/base/acm.bst
%{_texmfdistdir}/bibtex/bst/base/alpha.bst
%{_texmfdistdir}/bibtex/bst/base/apalike.bst
%{_texmfdistdir}/bibtex/bst/base/ieeetr.bst
%{_texmfdistdir}/bibtex/bst/base/plain.bst
%{_texmfdistdir}/bibtex/bst/base/siam.bst
%{_texmfdistdir}/bibtex/bst/base/unsrt.bst
%{_texmfdistdir}/tex/generic/bibtex/apalike.sty
%{_texmfdistdir}/tex/generic/bibtex/apalike.tex

%package -n texlive-bibtex8
Version:        %{texlive_version}.%{texlive_noarch}.3.72svn66186
Release:        0
License:        GPL-2.0-or-later
Summary:        BibTeX variant supporting 8-bit encodings
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtex8-bin >= %{texlive_version}
#!BuildIgnore: texlive-bibtex8-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibtex8-doc >= %{texlive_version}
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source299:      bibtex8.tar.xz
Source300:      bibtex8.doc.tar.xz

%description -n texlive-bibtex8
An enhanced, portable C version of BibTeX. Enhanced by
conversion to larger (32-bit) capacity, addition of run-time
selectable capacity and 8-bit support extensions. National
character set and sorting order are controlled by an external
configuration file. Various examples are included. Originally
written by Niel Kempson and Alejandro Aguilar-Sierra, it is now
maintained as part of TeX Live.

%package -n texlive-bibtex8-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.72svn66186
Release:        0
Summary:        Documentation for texlive-bibtex8
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibtex8 and texlive-alldocumentation)
Provides:       man(bibtex8.1)

%description -n texlive-bibtex8-doc
This package includes the documentation for texlive-bibtex8

%post -n texlive-bibtex8
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibtex8
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibtex8
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibtex8-doc
%{_texmfdistdir}/doc/bibtex8/00bibtex8-history.txt
%{_texmfdistdir}/doc/bibtex8/00bibtex8-readme.txt
%{_texmfdistdir}/doc/bibtex8/csfile.txt
%{_texmfdistdir}/doc/bibtex8/file_id.diz
%{_mandir}/man1/bibtex8.1*

%files -n texlive-bibtex8
%{_texmfdistdir}/bibtex/csf/base/88591lat.csf
%{_texmfdistdir}/bibtex/csf/base/88591sca.csf
%{_texmfdistdir}/bibtex/csf/base/README.TEXLIVE
%{_texmfdistdir}/bibtex/csf/base/ascii.csf
%{_texmfdistdir}/bibtex/csf/base/cp437lat.csf
%{_texmfdistdir}/bibtex/csf/base/cp850lat.csf
%{_texmfdistdir}/bibtex/csf/base/cp850sca.csf
%{_texmfdistdir}/bibtex/csf/base/cp866rus.csf
%{_texmfdistdir}/bibtex/csf/base/csfile.txt
%{_texmfdistdir}/bibtex/csf/polish-csf/88592pl.csf
%{_texmfdistdir}/bibtex/csf/polish-csf/cp1250pl.csf
%{_texmfdistdir}/bibtex/csf/polish-csf/cp852pl.csf
%{_texmfdistdir}/bibtex/csf/polish-csf/iso8859-7.csf

%package -n texlive-bibtexperllibs
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn68910
Release:        0
License:        GPL-2.0-or-later
Summary:        BibTeX Perl Libraries
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtexperllibs-bin >= %{texlive_version}
#!BuildIgnore: texlive-bibtexperllibs-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibtexperllibs-doc >= %{texlive_version}
Requires:       perl(BibTeX::Parser)
#!BuildIgnore:  perl(BibTeX::Parser)
Requires:       perl(BibTeX::Parser::Author)
#!BuildIgnore:  perl(BibTeX::Parser::Author)
Requires:       perl(BibTeX::Parser::Entry)
#!BuildIgnore:  perl(BibTeX::Parser::Entry)
Requires:       perl(Cwd)
#!BuildIgnore:  perl(Cwd)
Requires:       perl(Encode)
#!BuildIgnore:  perl(Encode)
Requires:       perl(Exporter)
#!BuildIgnore:  perl(Exporter)
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(LaTeX::ToUnicode)
#!BuildIgnore:  perl(LaTeX::ToUnicode)
Requires:       perl(LaTeX::ToUnicode::Tables)
#!BuildIgnore:  perl(LaTeX::ToUnicode::Tables)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(utf8)
#!BuildIgnore:  perl(utf8)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source301:      bibtexperllibs.tar.xz
Source302:      bibtexperllibs.doc.tar.xz

%description -n texlive-bibtexperllibs
This package provides BibTeX related Perl libraries by Gerhard
Gossen, repacked by Boris Veytsman, for TeX Live and other
TDS-compliant distributions. The libraries are written in pure
Perl, so should work out of the box on any architecture. They
have been packaged here mostly for Boris Veytsman's BibTeX
suite, but can be used in any other Perl script.

%package -n texlive-bibtexperllibs-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn68910
Release:        0
Summary:        Documentation for texlive-bibtexperllibs
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibtexperllibs and texlive-alldocumentation)
Provides:       man(ltx2unitxt.1)

%description -n texlive-bibtexperllibs-doc
This package includes the documentation for texlive-bibtexperllibs

%post -n texlive-bibtexperllibs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibtexperllibs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibtexperllibs
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibtexperllibs-doc
%{_mandir}/man1/ltx2unitxt.1*

%files -n texlive-bibtexperllibs
%{_texmfdistdir}/scripts/bibtexperllibs/BibTeX/Parser.pm
%{_texmfdistdir}/scripts/bibtexperllibs/BibTeX/Parser/Author.pm
%{_texmfdistdir}/scripts/bibtexperllibs/BibTeX/Parser/Entry.pm
%{_texmfdistdir}/scripts/bibtexperllibs/LaTeX/ToUnicode.pm
%{_texmfdistdir}/scripts/bibtexperllibs/LaTeX/ToUnicode/Tables.pm
%{_texmfdistdir}/scripts/bibtexperllibs/ltx2unitxt

%package -n texlive-bibtexu
Version:        %{texlive_version}.%{texlive_noarch}.3.72svn66186
Release:        0
License:        GPL-2.0-or-later
Summary:        BibTeX variant supporting Unicode (UTF-8), via ICU
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-bibtexu-bin >= %{texlive_version}
#!BuildIgnore: texlive-bibtexu-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Provides:       man(bibtexu.1)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source303:      bibtexu.doc.tar.xz

%description -n texlive-bibtexu
An enhanced, portable C version of BibTeX. Unicode is supported
via the ICU library. Originally written by Yannis Haralambous
and his students, and derived from bibtex8, with substantial
updates from the Japanese TeX Development Community, it is now
maintained as part of TeX Live.

%post -n texlive-bibtexu
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibtexu
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibtexu
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibtexu
%{_texmfdistdir}/doc/bibtexu/README
%{_texmfdistdir}/doc/bibtexu/examples/test.bbl
%{_texmfdistdir}/doc/bibtexu/examples/test.bib
%{_texmfdistdir}/doc/bibtexu/examples/test.pdf
%{_texmfdistdir}/doc/bibtexu/examples/test.tex
%{_mandir}/man1/bibtexu.1*

%package -n texlive-bibtools
Version:        %{texlive_version}.%{texlive_noarch}.svn67386
Release:        0
License:        LPPL-1.0
Summary:        Bib management tools
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source304:      bibtools.tar.xz

%description -n texlive-bibtools
A set of bibliography tools. Includes: aux2bib, a perl script
which will take an .aux file and make a portable .bib file to
go with it; bibify, a shell script that will optimise away one
pass of the LaTeX/BibTeX cycle, in some cases bibkey, a shell
script that finds entries whose "keyword" field matches the
given keys (uses sed and awk); cleantex, a shell script to tidy
up after a LaTeX run; looktex, a shell script to list entries
that match a given regexp; makebib, a shell script to make an
exportable .bib file from an existing (set of) .bib file(s) and
an optional set of citations (uses sed) printbib, a shell
script to make a dvi file from a .bib file, sorted by cite key,
and including fields like "keyword", "abstract", and "comment".
bib2html, a perl script that makes a browsable HTML version of
a bibliography (several .bst files are supplied); and citekeys,
a shell script that lists the citation keys of a .bib file.

%post -n texlive-bibtools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibtools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibtools
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibtools
%{_texmfdistdir}/bibtex/bst/bibtools/abstract.bst

%package -n texlive-bibtopic
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Include multiple bibliographies in a document
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibtopic-doc >= %{texlive_version}
Provides:       tex(bibtopic.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source305:      bibtopic.tar.xz
Source306:      bibtopic.doc.tar.xz

%description -n texlive-bibtopic
The package allows the user to include several bibliographies
covering different 'topics' or bibliographic material into a
document (e.g., one bibliography for primary literature and one
for secondary literature). The package provides commands to
include either all references from a .bib file, only the
references actually cited or those not cited in your document.
The user has to construct a separate .bib file for each
bibliographic 'topic', each of which will be processed
separately by BibTeX. If you want to have bibliographies
specific to one part of a document, see the packages bibunits
or chapterbib.

%package -n texlive-bibtopic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn15878
Release:        0
Summary:        Documentation for texlive-bibtopic
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibtopic and texlive-alldocumentation)

%description -n texlive-bibtopic-doc
This package includes the documentation for texlive-bibtopic

%post -n texlive-bibtopic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibtopic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibtopic
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibtopic-doc
%{_texmfdistdir}/doc/latex/bibtopic/README
%{_texmfdistdir}/doc/latex/bibtopic/articles.bib
%{_texmfdistdir}/doc/latex/bibtopic/bibtopic.pdf
%{_texmfdistdir}/doc/latex/bibtopic/books.bib
%{_texmfdistdir}/doc/latex/bibtopic/sample.tex

%files -n texlive-bibtopic
%{_texmfdistdir}/tex/latex/bibtopic/bibtopic.sty

%package -n texlive-bibtopicprefix
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn15878
Release:        0
License:        LPPL-1.0
Summary:        Prefix references to bibliographies produced by bibtopic
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibtopicprefix-doc >= %{texlive_version}
Provides:       tex(bibtopicprefix.sty)
Requires:       tex(bibtopic.sty)
Requires:       tex(scrlfile.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source307:      bibtopicprefix.tar.xz
Source308:      bibtopicprefix.doc.tar.xz

%description -n texlive-bibtopicprefix
The package permits users to apply prefixes (fixed strings) to
references to entries in bibliographies produced by the
bibtopic package.

%package -n texlive-bibtopicprefix-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn15878
Release:        0
Summary:        Documentation for texlive-bibtopicprefix
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibtopicprefix and texlive-alldocumentation)

%description -n texlive-bibtopicprefix-doc
This package includes the documentation for texlive-bibtopicprefix

%post -n texlive-bibtopicprefix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibtopicprefix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibtopicprefix
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibtopicprefix-doc
%{_texmfdistdir}/doc/latex/bibtopicprefix/README
%{_texmfdistdir}/doc/latex/bibtopicprefix/bibtopicprefix.pdf
%{_texmfdistdir}/doc/latex/bibtopicprefix/bibtopicprefix.xml

%files -n texlive-bibtopicprefix
%{_texmfdistdir}/tex/latex/bibtopicprefix/bibtopicprefix.sty

%package -n texlive-bibunits
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn15878
Release:        0
License:        LPPL-1.0
Summary:        Multiple bibliographies in one document
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bibunits-doc >= %{texlive_version}
Provides:       tex(bibunits.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source309:      bibunits.tar.xz
Source310:      bibunits.doc.tar.xz

%description -n texlive-bibunits
The package provide a mechanism to generate separate
bibliographies for different units (chapters, sections or
bibunit-environments) of a text. The package separates the
citations of each unit of text into a separate file to be
processed by BibTeX. The global bibliography section produced
by LaTeX may also appear in the document and citations can be
placed in both the local unit and the global bibliographies at
the same time. The package is compatible with koma-script and
with the babel French option frenchb.

%package -n texlive-bibunits-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn15878
Release:        0
Summary:        Documentation for texlive-bibunits
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bibunits and texlive-alldocumentation)

%description -n texlive-bibunits-doc
This package includes the documentation for texlive-bibunits

%post -n texlive-bibunits
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bibunits
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bibunits
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bibunits-doc
%{_texmfdistdir}/doc/latex/bibunits/README
%{_texmfdistdir}/doc/latex/bibunits/bibtexall
%{_texmfdistdir}/doc/latex/bibunits/bibunits.pdf

%files -n texlive-bibunits
%{_texmfdistdir}/tex/latex/bibunits/bibunits.sty

%package -n texlive-bidi
Version:        %{texlive_version}.%{texlive_noarch}.39.8svn67798
Release:        0
License:        LPPL-1.0
Summary:        Bidirectional typesetting in plain TeX and LaTeX, using XeTeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bidi-doc >= %{texlive_version}
Provides:       tex(adjmulticol-xetex-bidi.def)
Provides:       tex(algorithm2e-xetex-bidi.def)
Provides:       tex(amsart-xetex-bidi.def)
Provides:       tex(amsbook-xetex-bidi.def)
Provides:       tex(amsmath-xetex-bidi.def)
Provides:       tex(amstext-xetex-bidi.def)
Provides:       tex(amsthm-xetex-bidi.def)
Provides:       tex(array-xetex-bidi.def)
Provides:       tex(article-xetex-bidi.def)
Provides:       tex(artikel1-xetex-bidi.def)
Provides:       tex(artikel2-xetex-bidi.def)
Provides:       tex(artikel3-xetex-bidi.def)
Provides:       tex(arydshln-xetex-bidi.def)
Provides:       tex(beamer-xetex-bidi.def)
Provides:       tex(beamerbaseauxtemplates-xetex-bidi.def)
Provides:       tex(beamerbaseboxes-xetex-bidi.def)
Provides:       tex(beamerbasecolor-xetex-bidi.def)
Provides:       tex(beamerbasecompatibility-xetex-bidi.def)
Provides:       tex(beamerbaseframecomponents-xetex-bidi.def)
Provides:       tex(beamerbaseframesize-xetex-bidi.def)
Provides:       tex(beamerbaselocalstructure-xetex-bidi.def)
Provides:       tex(beamerbasemisc-xetex-bidi.def)
Provides:       tex(beamerbasenavigation-xetex-bidi.def)
Provides:       tex(beamerbaseoverlay-xetex-bidi.def)
Provides:       tex(beamerinnerthemecircles-xetex-bidi.def)
Provides:       tex(beamerinnerthemedefault-xetex-bidi.def)
Provides:       tex(beamerinnerthemefocus-xetex-bidi.def)
Provides:       tex(beamerinnerthemeinmargin-xetex-bidi.def)
Provides:       tex(beamerinnerthememetropolis-xetex-bidi.def)
Provides:       tex(beamerinnerthemerectangles-xetex-bidi.def)
Provides:       tex(beamerinnerthemerounded-xetex-bidi.def)
Provides:       tex(beamerouterthemedefault-xetex-bidi.def)
Provides:       tex(beamerouterthemefocus-xetex-bidi.def)
Provides:       tex(beamerouterthemeinfolines-xetex-bidi.def)
Provides:       tex(beamerouterthememetropolis-xetex-bidi.def)
Provides:       tex(beamerouterthememiniframes-xetex-bidi.def)
Provides:       tex(beamerouterthemeshadow-xetex-bidi.def)
Provides:       tex(beamerouterthemesidebar-xetex-bidi.def)
Provides:       tex(beamerouterthemesmoothbars-xetex-bidi.def)
Provides:       tex(beamerouterthemesmoothtree-xetex-bidi.def)
Provides:       tex(beamerouterthemesplit-xetex-bidi.def)
Provides:       tex(beamerouterthemetree-xetex-bidi.def)
Provides:       tex(beamerthemeHannover-xetex-bidi.def)
Provides:       tex(beamerthemeSingapore-xetex-bidi.def)
Provides:       tex(bidi-media9.sty)
Provides:       tex(bidi-perpage.sty)
Provides:       tex(bidi.sty)
Provides:       tex(bidi.tex)
Provides:       tex(bidi2in1.sty)
Provides:       tex(bidicode.sty)
Provides:       tex(bidiftnxtra.sty)
Provides:       tex(bidimoderncv.cls)
Provides:       tex(bidipoem.sty)
Provides:       tex(biditools.sty)
Provides:       tex(biditufte-book.cls)
Provides:       tex(biditufte-handout.cls)
Provides:       tex(bidituftefloat.sty)
Provides:       tex(bidituftegeneralstructure.sty)
Provides:       tex(bidituftehyperref.sty)
Provides:       tex(bidituftesidenote.sty)
Provides:       tex(bidituftetitle.sty)
Provides:       tex(bidituftetoc.sty)
Provides:       tex(boek-xetex-bidi.def)
Provides:       tex(boek3-xetex-bidi.def)
Provides:       tex(book-xetex-bidi.def)
Provides:       tex(bookest-xetex-bidi.def)
Provides:       tex(breqn-xetex-bidi.def)
Provides:       tex(cals-xetex-bidi.def)
Provides:       tex(caption-xetex-bidi.def)
Provides:       tex(caption3-xetex-bidi.def)
Provides:       tex(color-xetex-bidi.def)
Provides:       tex(colortbl-xetex-bidi.def)
Provides:       tex(combine-xetex-bidi.def)
Provides:       tex(crop-xetex-bidi.def)
Provides:       tex(cuted-xetex-bidi.def)
Provides:       tex(cutwin-xetex-bidi.def)
Provides:       tex(cvthemebidicasual.sty)
Provides:       tex(cvthemebidiclassic.sty)
Provides:       tex(dblfnote-xetex-bidi.def)
Provides:       tex(diagbox-xetex-bidi.def)
Provides:       tex(draftwatermark-xetex-bidi.def)
Provides:       tex(empheq-xetex-bidi.def)
Provides:       tex(eso-pic-xetex-bidi.def)
Provides:       tex(extarticle-xetex-bidi.def)
Provides:       tex(extbook-xetex-bidi.def)
Provides:       tex(extletter-xetex-bidi.def)
Provides:       tex(extrafootnotefeatures-xetex-bidi.def)
Provides:       tex(extreport-xetex-bidi.def)
Provides:       tex(fancybox-xetex-bidi.def)
Provides:       tex(fancyhdr-xetex-bidi.def)
Provides:       tex(fix2col-xetex-bidi.def)
Provides:       tex(fleqn-xetex-bidi.def)
Provides:       tex(float-xetex-bidi.def)
Provides:       tex(floatrow-xetex-bidi.def)
Provides:       tex(flowfram-xetex-bidi.def)
Provides:       tex(footnote-xetex-bidi.def)
Provides:       tex(footnotebackref-xetex-bidi.def)
Provides:       tex(framed-xetex-bidi.def)
Provides:       tex(ftnright-xetex-bidi.def)
Provides:       tex(geometry-xetex-bidi.def)
Provides:       tex(graphicx-xetex-bidi.def)
Provides:       tex(hvfloat-xetex-bidi.def)
Provides:       tex(hyperref-xetex-bidi.def)
Provides:       tex(imsproc-xetex-bidi.def)
Provides:       tex(latex-xetex-bidi.def)
Provides:       tex(leqno-xetex-bidi.def)
Provides:       tex(letter-xetex-bidi.def)
Provides:       tex(lettrine-xetex-bidi.def)
Provides:       tex(lineno-xetex-bidi.def)
Provides:       tex(listings-xetex-bidi.def)
Provides:       tex(loadingorder-xetex-bidi.def)
Provides:       tex(longtable-xetex-bidi.def)
Provides:       tex(lscape-xetex-bidi.def)
Provides:       tex(mathtools-xetex-bidi.def)
Provides:       tex(mdframed-xetex-bidi.def)
Provides:       tex(memoir-xetex-bidi.def)
Provides:       tex(midfloat-xetex-bidi.def)
Provides:       tex(minitoc-xetex-bidi.def)
Provides:       tex(multicol-xetex-bidi.def)
Provides:       tex(multienum-xetex-bidi.def)
Provides:       tex(natbib-xetex-bidi.def)
Provides:       tex(newfloat-xetex-bidi.def)
Provides:       tex(nicematrix-xetex-bidi.def)
Provides:       tex(ntheorem-hyper-xetex-bidi.def)
Provides:       tex(ntheorem-xetex-bidi.def)
Provides:       tex(overpic-xetex-bidi.def)
Provides:       tex(pdfbase-xetex-bidi.def)
Provides:       tex(pdflscape-xetex-bidi.def)
Provides:       tex(pdfpages-xetex-bidi.def)
Provides:       tex(pgfcorescopes.code-xetex-bidi.def)
Provides:       tex(pgfsys.code-xetex-bidi.def)
Provides:       tex(picinpar-xetex-bidi.def)
Provides:       tex(plain-xetex-bidi.def)
Provides:       tex(pstricks-xetex-bidi.def)
Provides:       tex(quotchap-xetex-bidi.def)
Provides:       tex(ragged2e-xetex-bidi.def)
Provides:       tex(rapport1-xetex-bidi.def)
Provides:       tex(rapport3-xetex-bidi.def)
Provides:       tex(refrep-xetex-bidi.def)
Provides:       tex(report-xetex-bidi.def)
Provides:       tex(rotating-xetex-bidi.def)
Provides:       tex(scrartcl-xetex-bidi.def)
Provides:       tex(scrbook-xetex-bidi.def)
Provides:       tex(scrreprt-xetex-bidi.def)
Provides:       tex(sidecap-xetex-bidi.def)
Provides:       tex(soul-xetex-bidi.def)
Provides:       tex(stabular-xetex-bidi.def)
Provides:       tex(subfigure-xetex-bidi.def)
Provides:       tex(tabls-xetex-bidi.def)
Provides:       tex(tabularx-xetex-bidi.def)
Provides:       tex(tabulary-xetex-bidi.def)
Provides:       tex(tc-xetex-bidi.def)
Provides:       tex(tcolorbox-xetex-bidi.def)
Provides:       tex(titlesec-xetex-bidi.def)
Provides:       tex(titletoc-xetex-bidi.def)
Provides:       tex(tocbasic-xetex-bidi.def)
Provides:       tex(tocbibind-xetex-bidi.def)
Provides:       tex(tocloft-xetex-bidi.def)
Provides:       tex(tocstyle-xetex-bidi.def)
Provides:       tex(todonotes-xetex-bidi.def)
Provides:       tex(wrapfig-xetex-bidi.def)
Provides:       tex(xcolor-xetex-bidi.def)
Provides:       tex(xltxtra-xetex-bidi.def)
Requires:       tex(article.cls)
Requires:       tex(auxhook.sty)
Requires:       tex(bibentry.sty)
Requires:       tex(book.cls)
Requires:       tex(changepage.sty)
Requires:       tex(chngpage.sty)
Requires:       tex(color.sty)
Requires:       tex(crop.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(floatrow.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lscape.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(media9.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Requires:       tex(optparams.sty)
Requires:       tex(paralist.sty)
Requires:       tex(placeins.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(setspace.sty)
Requires:       tex(showexpl.sty)
Requires:       tex(sidecap.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(zref-abspage.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source311:      bidi.tar.xz
Source312:      bidi.doc.tar.xz

%description -n texlive-bidi
A convenient interface for typesetting bidirectional texts with
plain TeX and LaTeX. The package includes adaptations for use
with many other commonly-used packages.

%package -n texlive-bidi-doc
Version:        %{texlive_version}.%{texlive_noarch}.39.8svn67798
Release:        0
Summary:        Documentation for texlive-bidi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bidi and texlive-alldocumentation)

%description -n texlive-bidi-doc
This package includes the documentation for texlive-bidi

%post -n texlive-bidi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bidi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bidi
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bidi-doc
%{_texmfdistdir}/doc/xelatex/bidi/README
%{_texmfdistdir}/doc/xelatex/bidi/bidi-bibitem.pdf
%{_texmfdistdir}/doc/xelatex/bidi/bidi-doc.pdf
%{_texmfdistdir}/doc/xelatex/bidi/bidi-logo.tex
%{_texmfdistdir}/doc/xelatex/bidi/bidi.pdf
%{_texmfdistdir}/doc/xelatex/bidi/bidisample2e.tex
%{_texmfdistdir}/doc/xelatex/bidi/bidismall2e.tex
%{_texmfdistdir}/doc/xelatex/bidi/gull.jpg
%{_texmfdistdir}/doc/xelatex/bidi/picture.jpg
%{_texmfdistdir}/doc/xelatex/bidi/test-arydshln.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-bidi.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-brochure.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-casualcv.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-classiccv.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-color.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-supertabular.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-tabular.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-tabularx.tex
%{_texmfdistdir}/doc/xelatex/bidi/test-tabulary.tex
%{_texmfdistdir}/doc/xelatex/bidi/test1-colortbl.tex
%{_texmfdistdir}/doc/xelatex/bidi/test1-wrapfig.tex
%{_texmfdistdir}/doc/xelatex/bidi/test2-colortbl.tex
%{_texmfdistdir}/doc/xelatex/bidi/test2-wrapfig.tex
%{_texmfdistdir}/doc/xelatex/bidi/test3-wrapfig.tex

%files -n texlive-bidi
%{_texmfdistdir}/tex/xelatex/bidi/adjmulticol-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/algorithm2e-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amsart-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amsbook-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amsmath-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amstext-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/amsthm-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/array-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/article-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/artikel1-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/artikel2-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/artikel3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/arydshln-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamer-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbaseauxtemplates-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbaseboxes-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbasecolor-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbasecompatibility-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbaseframecomponents-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbaseframesize-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbaselocalstructure-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbasemisc-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbasenavigation-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerbaseoverlay-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerinnerthemecircles-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerinnerthemedefault-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerinnerthemefocus-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerinnerthemeinmargin-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerinnerthememetropolis-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerinnerthemerectangles-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerinnerthemerounded-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemedefault-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemefocus-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemeinfolines-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthememetropolis-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthememiniframes-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemeshadow-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemesidebar-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemesmoothbars-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemesmoothtree-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemesplit-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerouterthemetree-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerthemeHannover-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/beamerthemeSingapore-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/bidi-logo.pdf
%{_texmfdistdir}/tex/xelatex/bidi/bidi-media9.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidi-perpage.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidi.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidi.tex
%{_texmfdistdir}/tex/xelatex/bidi/bidi2in1.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidicode.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidiftnxtra.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidimoderncv.cls
%{_texmfdistdir}/tex/xelatex/bidi/bidipoem.sty
%{_texmfdistdir}/tex/xelatex/bidi/biditools.sty
%{_texmfdistdir}/tex/xelatex/bidi/biditufte-book.cls
%{_texmfdistdir}/tex/xelatex/bidi/biditufte-handout.cls
%{_texmfdistdir}/tex/xelatex/bidi/bidituftefloat.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftegeneralstructure.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftehyperref.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftesidenote.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftetitle.sty
%{_texmfdistdir}/tex/xelatex/bidi/bidituftetoc.sty
%{_texmfdistdir}/tex/xelatex/bidi/boek-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/boek3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/book-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/bookest-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/breqn-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cals-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/caption-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/caption3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/color-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/colortbl-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/combine-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/crop-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cuted-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cutwin-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/cvthemebidicasual.sty
%{_texmfdistdir}/tex/xelatex/bidi/cvthemebidiclassic.sty
%{_texmfdistdir}/tex/xelatex/bidi/dblfnote-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/diagbox-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/draftwatermark-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/empheq-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/eso-pic-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extarticle-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extbook-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extletter-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extrafootnotefeatures-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/extreport-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fancybox-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fancyhdr-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fix2col-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/fleqn-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/float-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/floatrow-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/flowfram-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/footnote-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/footnotebackref-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/framed-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ftnright-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/geometry-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/graphicx-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/hvfloat-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/hyperref-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/imsproc-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/latex-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/leqno-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/letter-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/lettrine-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/lineno-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/listings-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/loadingorder-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/longtable-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/lscape-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/mathtools-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/mdframed-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/memoir-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/midfloat-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/minitoc-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/multicol-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/multienum-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/natbib-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/newfloat-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/nicematrix-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ntheorem-hyper-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ntheorem-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/overpic-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pdfbase-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pdflscape-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pdfpages-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pgfcorescopes.code-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pgfsys.code-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/picinpar-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/plain-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/pstricks-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/quotchap-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/ragged2e-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/rapport1-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/rapport3-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/refrep-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/report-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/rotating-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/scrartcl-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/scrbook-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/scrreprt-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/sidecap-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/soul-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/stabular-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/subfigure-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tabls-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tabularx-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tabulary-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tc-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tcolorbox-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/titlesec-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/titletoc-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tocbasic-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tocbibind-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tocloft-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/tocstyle-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/todonotes-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/wrapfig-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/xcolor-xetex-bidi.def
%{_texmfdistdir}/tex/xelatex/bidi/xltxtra-xetex-bidi.def

%package -n texlive-bidi-atbegshi
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn62009
Release:        0
License:        LPPL-1.0
Summary:        Bidi-aware shipout macros
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bidi-atbegshi-doc >= %{texlive_version}
Provides:       tex(bidi-atbegshi.sty)
Requires:       tex(atbegshi-ltx.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source313:      bidi-atbegshi.tar.xz
Source314:      bidi-atbegshi.doc.tar.xz

%description -n texlive-bidi-atbegshi
The package adds some commands to the atbegshi package for
proper placement of background material in the left and right
corners of the output page, in both LTR and RTL modes. The
package only works with xelatex format and should be loaded
before the bidi package.

%package -n texlive-bidi-atbegshi-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn62009
Release:        0
Summary:        Documentation for texlive-bidi-atbegshi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bidi-atbegshi and texlive-alldocumentation)

%description -n texlive-bidi-atbegshi-doc
This package includes the documentation for texlive-bidi-atbegshi

%post -n texlive-bidi-atbegshi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bidi-atbegshi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bidi-atbegshi
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bidi-atbegshi-doc
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/README
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/bidi-atbegshi-doc.pdf
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/bidi-atbegshi-doc.tex
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-LTR.pdf
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-LTR.tex
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-RTL.pdf
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-RTL.tex
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-foreground-LTR.pdf
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-foreground-LTR.tex
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-foreground-RTL.pdf
%{_texmfdistdir}/doc/xelatex/bidi-atbegshi/test-foreground-RTL.tex

%files -n texlive-bidi-atbegshi
%{_texmfdistdir}/tex/xelatex/bidi-atbegshi/bidi-atbegshi.sty

%package -n texlive-bidicontour
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn34631
Release:        0
License:        LPPL-1.0
Summary:        Bidi-aware coloured contour around text
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bidicontour-doc >= %{texlive_version}
Provides:       tex(bidicontour.sty)
Requires:       tex(color.sty)
Requires:       tex(trig.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source315:      bidicontour.tar.xz
Source316:      bidicontour.doc.tar.xz

%description -n texlive-bidicontour
The package is a re-implementation of the contour package,
making it bidi-aware, and adding support of the xdvipdfmx (when
the outline option of the package is used).

%package -n texlive-bidicontour-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn34631
Release:        0
Summary:        Documentation for texlive-bidicontour
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bidicontour and texlive-alldocumentation)

%description -n texlive-bidicontour-doc
This package includes the documentation for texlive-bidicontour

%post -n texlive-bidicontour
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bidicontour
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bidicontour
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bidicontour-doc
%{_texmfdistdir}/doc/xelatex/bidicontour/README
%{_texmfdistdir}/doc/xelatex/bidicontour/bidicontour-doc.pdf
%{_texmfdistdir}/doc/xelatex/bidicontour/bidicontour-doc.tex
%{_texmfdistdir}/doc/xelatex/bidicontour/bidicontour-example-copies.pdf
%{_texmfdistdir}/doc/xelatex/bidicontour/bidicontour-example-copies.tex
%{_texmfdistdir}/doc/xelatex/bidicontour/bidicontour-example-outline.pdf
%{_texmfdistdir}/doc/xelatex/bidicontour/bidicontour-example-outline.tex

%files -n texlive-bidicontour
%{_texmfdistdir}/tex/xelatex/bidicontour/bidicontour.sty

%package -n texlive-bidihl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn37795
Release:        0
License:        LPPL-1.0
Summary:        Experimental bidi-aware text highlighting
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bidihl-doc >= %{texlive_version}
Provides:       tex(bidihl.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source317:      bidihl.tar.xz
Source318:      bidihl.doc.tar.xz

%description -n texlive-bidihl
Experimental bidi-aware text highlighting.

%package -n texlive-bidihl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn37795
Release:        0
Summary:        Documentation for texlive-bidihl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bidihl and texlive-alldocumentation)

%description -n texlive-bidihl-doc
This package includes the documentation for texlive-bidihl

%post -n texlive-bidihl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bidihl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bidihl
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bidihl-doc
%{_texmfdistdir}/doc/xelatex/bidihl/README
%{_texmfdistdir}/doc/xelatex/bidihl/bidihl-doc.pdf
%{_texmfdistdir}/doc/xelatex/bidihl/bidihl-doc.tex
%{_texmfdistdir}/doc/xelatex/bidihl/test-bidihl.pdf
%{_texmfdistdir}/doc/xelatex/bidihl/test-bidihl.tex

%files -n texlive-bidihl
%{_texmfdistdir}/tex/xelatex/bidihl/bidihl.sty

%package -n texlive-bidipagegrid
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn34632
Release:        0
License:        LPPL-1.0
Summary:        Bidi-aware page grid in background
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bidipagegrid-doc >= %{texlive_version}
Provides:       tex(bidipagegrid.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source319:      bidipagegrid.tar.xz
Source320:      bidipagegrid.doc.tar.xz

%description -n texlive-bidipagegrid
The package is based on pagegrid.

%package -n texlive-bidipagegrid-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn34632
Release:        0
Summary:        Documentation for texlive-bidipagegrid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bidipagegrid and texlive-alldocumentation)

%description -n texlive-bidipagegrid-doc
This package includes the documentation for texlive-bidipagegrid

%post -n texlive-bidipagegrid
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bidipagegrid
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bidipagegrid
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bidipagegrid-doc
%{_texmfdistdir}/doc/xelatex/bidipagegrid/README
%{_texmfdistdir}/doc/xelatex/bidipagegrid/bidipagegrid-doc.pdf
%{_texmfdistdir}/doc/xelatex/bidipagegrid/bidipagegrid-doc.tex

%files -n texlive-bidipagegrid
%{_texmfdistdir}/tex/xelatex/bidipagegrid/bidipagegrid.sty

%package -n texlive-bidipresentation
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn35267
Release:        0
License:        LPPL-1.0
Summary:        Experimental bidi presentation
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bidipresentation-doc >= %{texlive_version}
Provides:       tex(bidiprescolors.cfg)
Provides:       tex(bidipresentation.cls)
Requires:       tex(article.cls)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(scrlfile.sty)
Requires:       tex(xecolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source321:      bidipresentation.tar.xz
Source322:      bidipresentation.doc.tar.xz

%description -n texlive-bidipresentation
A great portion of the code is borrowed from the texpower
bundle, with modifications to get things working properly in
both right to left and left to right modes.

%package -n texlive-bidipresentation-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn35267
Release:        0
Summary:        Documentation for texlive-bidipresentation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bidipresentation and texlive-alldocumentation)

%description -n texlive-bidipresentation-doc
This package includes the documentation for texlive-bidipresentation

%post -n texlive-bidipresentation
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bidipresentation
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bidipresentation
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bidipresentation-doc
%{_texmfdistdir}/doc/xelatex/bidipresentation/README
%{_texmfdistdir}/doc/xelatex/bidipresentation/fig-1.pdf
%{_texmfdistdir}/doc/xelatex/bidipresentation/sample.pdf
%{_texmfdistdir}/doc/xelatex/bidipresentation/sample.tex

%files -n texlive-bidipresentation
%{_texmfdistdir}/tex/xelatex/bidipresentation/bidiprescolors.cfg
%{_texmfdistdir}/tex/xelatex/bidipresentation/bidipresentation.cls

%package -n texlive-bidishadowtext
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn34633
Release:        0
License:        LPPL-1.0
Summary:        Bidi-aware shadow text
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bidishadowtext-doc >= %{texlive_version}
Provides:       tex(bidishadowtext.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source323:      bidishadowtext.tar.xz
Source324:      bidishadowtext.doc.tar.xz

%description -n texlive-bidishadowtext
This package allows you to typeset bidi-aware shadow text. It
is a re-implementation of the shadowtext package adding bidi
support.

%package -n texlive-bidishadowtext-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn34633
Release:        0
Summary:        Documentation for texlive-bidishadowtext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bidishadowtext and texlive-alldocumentation)

%description -n texlive-bidishadowtext-doc
This package includes the documentation for texlive-bidishadowtext

%post -n texlive-bidishadowtext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bidishadowtext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bidishadowtext
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bidishadowtext-doc
%{_texmfdistdir}/doc/xelatex/bidishadowtext/bidishadowtext-demo.pdf
%{_texmfdistdir}/doc/xelatex/bidishadowtext/bidishadowtext-demo.tex
%{_texmfdistdir}/doc/xelatex/bidishadowtext/bidishadowtext-doc.pdf
%{_texmfdistdir}/doc/xelatex/bidishadowtext/bidishadowtext-doc.tex

%files -n texlive-bidishadowtext
%{_texmfdistdir}/tex/xelatex/bidishadowtext/bidishadowtext.sty

%package -n texlive-bigfoot
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn38248
Release:        0
License:        GPL-2.0-or-later
Summary:        Footnotes for critical editions
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bigfoot-doc >= %{texlive_version}
Provides:       tex(bigfoot.sty)
Provides:       tex(perpage.sty)
Provides:       tex(suffix.sty)
Requires:       tex(etex.sty)
Requires:       tex(manyfoot.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source325:      bigfoot.tar.xz
Source326:      bigfoot.doc.tar.xz

%description -n texlive-bigfoot
The package aims to provide a 'one-stop' solution to
requirements for footnotes. It offers: Multiple footnote
apparatus superior to that of manyfoot Footnotes can be
formatted in separate paragraphs, or be run into a single
paragraph (this choice may be selected per footnote series);
Things you might have expected (such as \verb-like material in
footnotes, and colour selections over page breaks) now work.
Note that the majority of the bigfoot package's interface is
identical to that of manyfoot; users should seek information
from that package's documentation. The bigfoot bundle also
provides the perpage and suffix packages.

%package -n texlive-bigfoot-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn38248
Release:        0
Summary:        Documentation for texlive-bigfoot
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bigfoot and texlive-alldocumentation)

%description -n texlive-bigfoot-doc
This package includes the documentation for texlive-bigfoot

%post -n texlive-bigfoot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bigfoot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bigfoot
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bigfoot-doc
%{_texmfdistdir}/doc/latex/bigfoot/COPYING
%{_texmfdistdir}/doc/latex/bigfoot/Makefile
%{_texmfdistdir}/doc/latex/bigfoot/README
%{_texmfdistdir}/doc/latex/bigfoot/bigfoot.pdf
%{_texmfdistdir}/doc/latex/bigfoot/perpage.pdf
%{_texmfdistdir}/doc/latex/bigfoot/suffix.pdf

%files -n texlive-bigfoot
%{_texmfdistdir}/tex/latex/bigfoot/bigfoot.sty
%{_texmfdistdir}/tex/latex/bigfoot/perpage.sty
%{_texmfdistdir}/tex/latex/bigfoot/suffix.sty

%package -n texlive-bigintcalc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn53172
Release:        0
License:        LPPL-1.0
Summary:        Integer calculations on very large numbers
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bigintcalc-doc >= %{texlive_version}
Provides:       tex(bigintcalc.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source327:      bigintcalc.tar.xz
Source328:      bigintcalc.doc.tar.xz

%description -n texlive-bigintcalc
This package provides expandable arithmetic operations with big
integers that can exceed TeX's number limits.

%package -n texlive-bigintcalc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn53172
Release:        0
Summary:        Documentation for texlive-bigintcalc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bigintcalc and texlive-alldocumentation)

%description -n texlive-bigintcalc-doc
This package includes the documentation for texlive-bigintcalc

%post -n texlive-bigintcalc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bigintcalc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bigintcalc
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bigintcalc-doc
%{_texmfdistdir}/doc/latex/bigintcalc/README.md
%{_texmfdistdir}/doc/latex/bigintcalc/bigintcalc.pdf

%files -n texlive-bigintcalc
%{_texmfdistdir}/tex/generic/bigintcalc/bigintcalc.sty

%package -n texlive-bigints
Version:        %{texlive_version}.%{texlive_noarch}.svn29803
Release:        0
License:        LPPL-1.0
Summary:        Writing big integrals
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bigints-doc >= %{texlive_version}
Provides:       tex(bigints.sty)
Requires:       tex(amsmath.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source329:      bigints.tar.xz
Source330:      bigints.doc.tar.xz

%description -n texlive-bigints
The package provides facilities for drawing big integral signs
when needed. An example would be when the integrand is a
matrix.

%package -n texlive-bigints-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn29803
Release:        0
Summary:        Documentation for texlive-bigints
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bigints and texlive-alldocumentation)

%description -n texlive-bigints-doc
This package includes the documentation for texlive-bigints

%post -n texlive-bigints
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bigints
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bigints
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bigints-doc
%{_texmfdistdir}/doc/latex/bigints/Makefile
%{_texmfdistdir}/doc/latex/bigints/README
%{_texmfdistdir}/doc/latex/bigints/bigints.forlisting
%{_texmfdistdir}/doc/latex/bigints/bigints.pdf
%{_texmfdistdir}/doc/latex/bigints/bigints.tex
%{_texmfdistdir}/doc/latex/bigints/perso.ist

%files -n texlive-bigints
%{_texmfdistdir}/tex/latex/bigints/bigints.sty

%package -n texlive-bilingualpages
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn59643
Release:        0
License:        LPPL-1.0
Summary:        Typeset two columns in parallel
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-bilingualpages-doc >= %{texlive_version}
Provides:       tex(bilingualpages.sty)
Requires:       tex(paracol.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source331:      bilingualpages.tar.xz
Source332:      bilingualpages.doc.tar.xz

%description -n texlive-bilingualpages
This is a simple wrapper for the paracol package for setting
two-column parallel text.

%package -n texlive-bilingualpages-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn59643
Release:        0
Summary:        Documentation for texlive-bilingualpages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-bilingualpages and texlive-alldocumentation)

%description -n texlive-bilingualpages-doc
This package includes the documentation for texlive-bilingualpages

%post -n texlive-bilingualpages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bilingualpages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bilingualpages
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bilingualpages-doc
%{_texmfdistdir}/doc/latex/bilingualpages/README.md

%files -n texlive-bilingualpages
%{_texmfdistdir}/tex/latex/bilingualpages/bilingualpages.sty

%package -n texlive-binarytree
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn41777
Release:        0
License:        LPPL-1.0
Summary:        Drawing binary trees using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-binarytree-doc >= %{texlive_version}
Provides:       tex(binarytree.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source333:      binarytree.tar.xz
Source334:      binarytree.doc.tar.xz

%description -n texlive-binarytree
This package provides an easy but flexible way to draw binary
trees using TikZ. A path specification and the setting of
various options determine the style for each edge of the tree.
There is support for the external library of TikZ which does
not affect externalization of the rest of the TikZ figures in
the document. There is an option to use automatic file naming:
useful if the trees are often moved around.

%package -n texlive-binarytree-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn41777
Release:        0
Summary:        Documentation for texlive-binarytree
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-binarytree and texlive-alldocumentation)

%description -n texlive-binarytree-doc
This package includes the documentation for texlive-binarytree

%post -n texlive-binarytree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-binarytree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-binarytree
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-binarytree-doc
%{_texmfdistdir}/doc/latex/binarytree/README
%{_texmfdistdir}/doc/latex/binarytree/binarytree.pdf
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex1.pdf
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex1.tex
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex2.pdf
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex2.tex
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex3.pdf
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex3.tex
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex4.pdf
%{_texmfdistdir}/doc/latex/binarytree/examples/binarytree-ex4.tex
%{_texmfdistdir}/doc/latex/binarytree/examples/btree-5_up_0,0,0_3729359_7458719_655360_0.7_0.7_-lrr-x--_-llrr-x--_-rll-x--_-rrll-x--.pdf

%files -n texlive-binarytree
%{_texmfdistdir}/tex/latex/binarytree/binarytree.sty

%package -n texlive-binomexp
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        Calculate Pascal's triangle
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-binomexp-doc >= %{texlive_version}
Provides:       tex(binomexp.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source335:      binomexp.tar.xz
Source336:      binomexp.doc.tar.xz

%description -n texlive-binomexp
The package calculates and prints rows of Pascal's triangle. It
may be used: simply to print successive rows of the triangle,
or to print the rows inside an array or tabular.

%package -n texlive-binomexp-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-binomexp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-binomexp and texlive-alldocumentation)

%description -n texlive-binomexp-doc
This package includes the documentation for texlive-binomexp

%post -n texlive-binomexp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-binomexp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-binomexp
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-binomexp-doc
%{_texmfdistdir}/doc/latex/binomexp/README
%{_texmfdistdir}/doc/latex/binomexp/binomexp.pdf

%files -n texlive-binomexp
%{_texmfdistdir}/tex/latex/binomexp/binomexp.sty

%package -n texlive-biochemistry-colors
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn54512
Release:        0
License:        LPPL-1.0
Summary:        Colors used to display amino acids, nucleotides, sugars or atoms in biochemistry
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biochemistry-colors-doc >= %{texlive_version}
Provides:       tex(Biochemistry-colors.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source337:      biochemistry-colors.tar.xz
Source338:      biochemistry-colors.doc.tar.xz

%description -n texlive-biochemistry-colors
Biochemistry-colors.sty defines the standard colors of
biochemistry for use with the color package and the xcolor
package. xcolor is loaded by Biochemistry-colors.sty. Colors
include: Shapely-colors for amino acids and nucleotides.
CPK-Colors (Corey, Pauling and Koltun) of elements. Jmol-colors
of elements, important isotopes and structures. Glycopedia
colors for sugars.

%package -n texlive-biochemistry-colors-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn54512
Release:        0
Summary:        Documentation for texlive-biochemistry-colors
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biochemistry-colors and texlive-alldocumentation)

%description -n texlive-biochemistry-colors-doc
This package includes the documentation for texlive-biochemistry-colors

%post -n texlive-biochemistry-colors
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biochemistry-colors
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biochemistry-colors
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biochemistry-colors-doc
%{_texmfdistdir}/doc/latex/biochemistry-colors/Biochemistry-colors.pdf
%{_texmfdistdir}/doc/latex/biochemistry-colors/Biochemistry-colors.xls
%{_texmfdistdir}/doc/latex/biochemistry-colors/README.txt

%files -n texlive-biochemistry-colors
%{_texmfdistdir}/tex/latex/biochemistry-colors/Biochemistry-colors.sty

%package -n texlive-biocon
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Typesetting biological species names
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
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
Suggests:       texlive-biocon-doc >= %{texlive_version}
Provides:       tex(biocon-old.sty)
Provides:       tex(biocon.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp.tug.org/texlive/tlnet/archive/
# from 20240311
Source339:      biocon.tar.xz
Source340:      biocon.doc.tar.xz

%description -n texlive-biocon
The biocon--biological conventions--package aids the
typesetting of some biological conventions. At the moment, it
makes a good job of typesetting species names (and ranks below
the species level). A distinction is made between the Plant,
Fungi, Animalia and Bacteria kingdoms. There are default
settings for the way species names are typeset, but they can be
customized. Different default styles are used in different
situations.

%package -n texlive-biocon-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-biocon
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            https://www.tug.org/texlive/
Supplements:    (texlive-biocon and texlive-alldocumentation)

%description -n texlive-biocon-doc
This package includes the documentation for texlive-biocon

%post -n texlive-biocon
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-biocon
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-biocon
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-biocon-doc
%{_texmfdistdir}/doc/latex/biocon/COPYING
%{_texmfdistdir}/doc/latex/biocon/INSTALL
%{_texmfdistdir}/doc/latex/biocon/README
%{_texmfdistdir}/doc/latex/biocon/biocon.nw
%{_texmfdistdir}/doc/latex/biocon/literature.bib
%{_texmfdistdir}/doc/latex/biocon/manual-old.pdf
%{_texmfdistdir}/doc/latex/biocon/manual-old.tex
%{_texmfdistdir}/doc/latex/biocon/manual.pdf
%{_texmfdistdir}/doc/latex/biocon/manual.tex
%{_texmfdistdir}/doc/latex/biocon/source.pdf
%{_texmfdistdir}/doc/latex/biocon/source.tex

%files -n texlive-biocon
%{_texmfdistdir}/tex/latex/biocon/biocon-old.sty
%{_texmfdistdir}/tex/latex/biocon/biocon.sty

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
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    pushd %{buildroot}%{_datadir}/texlive/texmf-dist
	patch --reject-format=unified --quoting-style=literal -f -p1 -F0 -T < %{S:9}
    popd
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-bbold-type1
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/bbold-type1/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-bbold-type1
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-bbold-type1/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-bbold-type1/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-bbold-type1/
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-bbold-type1.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-bbold-type1    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-bbold-type1/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-bboldx
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/bboldx/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-bboldx
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-bboldx/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-bboldx/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-bboldx/
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-bboldx.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-bboldx    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-bboldx/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-belleek
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/belleek/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/belleek/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-belleek
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-belleek/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-belleek/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-belleek/
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-belleek.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-belleek    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-belleek/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-belleek.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-belleek/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-belleek.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-belleek.conf
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-bera
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/bera/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-bera
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-bera/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-bera/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-bera/
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-bera.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-bera    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-bera/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-berenisadf
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/arkandis/berenisadf/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/arkandis/berenisadf/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-berenisadf
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-berenisadf/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-berenisadf/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-berenisadf/
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-berenisadf.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-berenisadf    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-berenisadf/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-berenisadf.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-berenisadf/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-berenisadf.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-berenisadf.conf
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-beuron
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/beuron/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/beuron/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-beuron
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-beuron/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-beuron/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-beuron/
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-beuron.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-beuron    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-beuron/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-beuron.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-beuron/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-beuron.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-beuron.conf
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/tex/lualatex/bezierplot/bezierplot.lua
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
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-bguq
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/bguq/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-bguq
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-bguq/${base} ${font}
    done
    /usr/bin/mkfontscale %{buildroot}%{_datadir}/fonts/texlive-bguq/
    /usr/bin/mkfontdir -e /usr/share/fonts/encodings/ %{buildroot}%{_datadir}/fonts/texlive-bguq/
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-bguq.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-bguq    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-bguq/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive
    # Strip executable bit from non-scripts
    for txt in %{_texmfdistdir}/scripts/bib2gls/bib2gls.jar \
	       %{_texmfdistdir}/scripts/bib2gls/convertgls2bib.jar \
	       %{_texmfdistdir}/scripts/bib2gls/texparserlib.jar
    do
	test -e %{buildroot}/$txt || continue
	chmod 0644 %{buildroot}/$txt
    done
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/bibarts/bibsort.exe
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/bibtex/bibhtml/bibhtml
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
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/generate-crossref-graphs.py
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/latexmkrc
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-bookinother/documentation/makefile
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-bookinother/makefile
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/makeall.py
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Extend python3 scripts with major version only if any
    for scr in %{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/makeall.py
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@python3@python%python3_bin_suffix@
		.
		w
		q
	EOF
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/latex/biblatex-gb7714-2015/makeall.py
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
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/generate-crossref-graphs.py
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/latexmkrc
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-morenames/documentation/makefile
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/biblatex-morenames/makefile
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:277} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:278} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:279} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:280} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:281} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:282} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:283} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:284} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:285} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:286} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:287} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:288} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:289} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:290} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:291} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:292} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:293} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:294} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:295} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:296} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:297} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:298} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:299} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:300} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:301} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:302} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/bibtexperllibs/ltx2unitxt
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
    tar --use-compress-program=xz -xf %{S:303} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:304} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:305} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:306} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:307} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:308} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:309} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:310} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:311} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:312} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:313} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:314} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:315} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:316} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:317} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:318} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:319} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:320} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:321} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:322} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:323} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:324} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:325} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:326} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:327} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:328} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:329} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:330} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:331} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:332} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:333} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:334} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:335} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:336} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:337} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:338} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:339} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:340} -C %{buildroot}%{_datadir}/texlive/texmf-dist
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
