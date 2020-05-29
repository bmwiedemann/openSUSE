#
# spec file for package texlive-specs-j
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

Name:           texlive-specs-j
Version:        2020
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for j
License:        BSD-3-Clause and GFDL-1.2 and GPL-2.0+ and LGPL-2.1+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain and SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-j-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-float
Version:        %{texlive_version}.%{texlive_noarch}.1.3dsvn15878
Release:        0
Summary:        Improved interface for floating objects
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
Recommends:     texlive-float-doc >= %{texlive_version}
Provides:       tex(float.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source1:        float.tar.xz
Source2:        float.doc.tar.xz

%description -n texlive-float
Improves the interface for defining floating objects such as
figures and tables. Introduces the boxed float, the ruled float
and the plaintop float. You can define your own floats and
improve the behaviour of the old ones. The package also
provides the H float modifier option of the obsolete here
package. You can select this as automatic default with
\floatplacement{figure}{H}.

%package -n texlive-float-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3dsvn15878
Release:        0
Summary:        Documentation for texlive-float
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-float-doc
This package includes the documentation for texlive-float

%post -n texlive-float
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-float 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-float
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-float-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/float/README
%{_texmfdistdir}/doc/latex/float/float.pdf

%files -n texlive-float
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/float/float.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-float-%{texlive_version}.%{texlive_noarch}.1.3dsvn15878-%{release}-zypper
%endif

%package -n texlive-floatrow
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3bsvn15878
Release:        0
Summary:        Modifying the layout of floats
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
Recommends:     texlive-floatrow-doc >= %{texlive_version}
Provides:       tex(floatpagestyle.sty)
Provides:       tex(floatrow.sty)
Provides:       tex(fr-fancy.sty)
Provides:       tex(fr-longtable.sty)
Provides:       tex(fr-subfig.sty)
Provides:       tex(listpen.sty)
Requires:       tex(caption3.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(keyval.sty)
Requires:       tex(longtable.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source3:        floatrow.tar.xz
Source4:        floatrow.doc.tar.xz

%description -n texlive-floatrow
The floatrow package provides many ways to customize layouts of
floating environments and has code to cooperate with the
caption 3.x package. The package offers mechanisms to put
floats side by side, and to put the caption beside its float.
The floatrow settings could be expanded to the floats created
by packages rotating, wrapfig, subfig (in the case of rows of
subfloats), and longtable.

%package -n texlive-floatrow-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3bsvn15878
Release:        0
Summary:        Documentation for texlive-floatrow
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-floatrow-doc:ru;en)

%description -n texlive-floatrow-doc
This package includes the documentation for texlive-floatrow

%post -n texlive-floatrow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-floatrow 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-floatrow
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-floatrow-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/floatrow/README
%{_texmfdistdir}/doc/latex/floatrow/floatrow-rus.pdf
%{_texmfdistdir}/doc/latex/floatrow/floatrow-rus.tex
%{_texmfdistdir}/doc/latex/floatrow/floatrow.pdf
%{_texmfdistdir}/doc/latex/floatrow/fr-sample.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample01.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample02.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample03.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample04.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample05.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample06.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample07.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample10.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample11.tex
%{_texmfdistdir}/doc/latex/floatrow/frsample12.tex
%{_texmfdistdir}/doc/latex/floatrow/pictures.tex
%{_texmfdistdir}/doc/latex/floatrow/sample-longtable-rus.tex
%{_texmfdistdir}/doc/latex/floatrow/sample-longtable.tex

%files -n texlive-floatrow
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/floatrow/floatpagestyle.sty
%{_texmfdistdir}/tex/latex/floatrow/floatrow.sty
%{_texmfdistdir}/tex/latex/floatrow/fr-fancy.sty
%{_texmfdistdir}/tex/latex/floatrow/fr-longtable.sty
%{_texmfdistdir}/tex/latex/floatrow/fr-subfig.sty
%{_texmfdistdir}/tex/latex/floatrow/listpen.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-floatrow-%{texlive_version}.%{texlive_noarch}.0.0.3bsvn15878-%{release}-zypper
%endif

%package -n texlive-flowchart
Version:        %{texlive_version}.%{texlive_noarch}.3.3svn36572
Release:        0
Summary:        Shapes for drawing flowcharts, using TikZ
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
Recommends:     texlive-flowchart-doc >= %{texlive_version}
Provides:       tex(flowchart.sty)
Requires:       tex(makeshape.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source5:        flowchart.tar.xz
Source6:        flowchart.doc.tar.xz

%description -n texlive-flowchart
The package provides a set of 'traditional' flowchart element
shapes; the documentation shows how to build a flowchart from
these elements, using pgf/TikZ. The package also requires the
makeshape package.

%package -n texlive-flowchart-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.3svn36572
Release:        0
Summary:        Documentation for texlive-flowchart
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-flowchart-doc
This package includes the documentation for texlive-flowchart

%post -n texlive-flowchart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-flowchart 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-flowchart
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-flowchart-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/flowchart/README
%{_texmfdistdir}/doc/latex/flowchart/flowchart.pdf

%files -n texlive-flowchart
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/flowchart/flowchart.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-flowchart-%{texlive_version}.%{texlive_noarch}.3.3svn36572-%{release}-zypper
%endif

%package -n texlive-flowfram
Version:        %{texlive_version}.%{texlive_noarch}.1.17svn35291
Release:        0
Summary:        Create text frames for posters, brochures or magazines
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
Recommends:     texlive-flowfram-doc >= %{texlive_version}
Provides:       tex(flowfram.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphics.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xfor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source7:        flowfram.tar.xz
Source8:        flowfram.doc.tar.xz

%description -n texlive-flowfram
The flowfram package enables you to create frames in a document
such that the contents of the document environment flow from
one frame to the next in the order in which they were defined.
This is useful for creating posters or magazines, indeed any
form of document that does not conform to the standard one or
two column layout.

%package -n texlive-flowfram-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.17svn35291
Release:        0
Summary:        Documentation for texlive-flowfram
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-flowfram-doc
This package includes the documentation for texlive-flowfram

%post -n texlive-flowfram
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-flowfram 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-flowfram
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-flowfram-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/flowfram/CHANGES
%{_texmfdistdir}/doc/latex/flowfram/README
%{_texmfdistdir}/doc/latex/flowfram/ffuserguide.pdf
%{_texmfdistdir}/doc/latex/flowfram/ffuserguide.tex
%{_texmfdistdir}/doc/latex/flowfram/ffuserguideidx.ist
%{_texmfdistdir}/doc/latex/flowfram/flowfram.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/egg.eps
%{_texmfdistdir}/doc/latex/flowfram/samples/egg.png
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-article.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-article.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-blanks.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-brochure.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-brochure.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-news.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-news.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-news2.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-news2.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-pages.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-pages.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-poster.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-poster.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-rot.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample-rot.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample1.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample1.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample2.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample2.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sample3.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sample3.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sampleRL.pdf
%{_texmfdistdir}/doc/latex/flowfram/samples/sampleRL.tex
%{_texmfdistdir}/doc/latex/flowfram/samples/sheep.eps
%{_texmfdistdir}/doc/latex/flowfram/samples/sheep.png

%files -n texlive-flowfram
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/flowfram/flowfram.perl
%{_texmfdistdir}/tex/latex/flowfram/flowfram.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-flowfram-%{texlive_version}.%{texlive_noarch}.1.17svn35291-%{release}-zypper
%endif

%package -n texlive-fltpoint
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn15878
Release:        0
Summary:        Simple floating point arithmetic
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
Recommends:     texlive-fltpoint-doc >= %{texlive_version}
Provides:       tex(deccomma.sty)
Provides:       tex(fltpoint.sty)
Provides:       tex(fltpoint.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source9:        fltpoint.tar.xz
Source10:       fltpoint.doc.tar.xz

%description -n texlive-fltpoint
The package provides simple floating point operations
(addition, subtraction, multiplication, division and rounding).
Used, for example, by rccol.

%package -n texlive-fltpoint-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn15878
Release:        0
Summary:        Documentation for texlive-fltpoint
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fltpoint-doc
This package includes the documentation for texlive-fltpoint

%post -n texlive-fltpoint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fltpoint 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fltpoint
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fltpoint-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/fltpoint/README
%{_texmfdistdir}/doc/generic/fltpoint/fltpoint.pdf

%files -n texlive-fltpoint
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/fltpoint/deccomma.sty
%{_texmfdistdir}/tex/generic/fltpoint/fltpoint.sty
%{_texmfdistdir}/tex/generic/fltpoint/fltpoint.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fltpoint-%{texlive_version}.%{texlive_noarch}.1.1bsvn15878-%{release}-zypper
%endif

%package -n texlive-fmp
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Include Functional MetaPost in LaTeX
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
Recommends:     texlive-fmp-doc >= %{texlive_version}
Provides:       tex(fmp.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source11:       fmp.tar.xz
Source12:       fmp.doc.tar.xz

%description -n texlive-fmp
The fmp package

%package -n texlive-fmp-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-fmp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fmp-doc
This package includes the documentation for texlive-fmp

%post -n texlive-fmp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fmp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fmp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fmp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fmp/README
%{_texmfdistdir}/doc/latex/fmp/fmp.pdf

%files -n texlive-fmp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fmp/fmp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fmp-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-fmtcount
Version:        %{texlive_version}.%{texlive_noarch}.3.07svn53912
Release:        0
Summary:        Display the value of a LaTeX counter in a variety of formats
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
Recommends:     texlive-fmtcount-doc >= %{texlive_version}
Provides:       tex(fc-UKenglish.def)
Provides:       tex(fc-USenglish.def)
Provides:       tex(fc-american.def)
Provides:       tex(fc-brazilian.def)
Provides:       tex(fc-british.def)
Provides:       tex(fc-english.def)
Provides:       tex(fc-francais.def)
Provides:       tex(fc-french.def)
Provides:       tex(fc-frenchb.def)
Provides:       tex(fc-german.def)
Provides:       tex(fc-germanb.def)
Provides:       tex(fc-italian.def)
Provides:       tex(fc-ngerman.def)
Provides:       tex(fc-ngermanb.def)
Provides:       tex(fc-portuges.def)
Provides:       tex(fc-portuguese.def)
Provides:       tex(fc-spanish.def)
Provides:       tex(fcnumparser.sty)
Provides:       tex(fcprefix.sty)
Provides:       tex(fmtcount.sty)
Requires:       tex(amsgen.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(itnumpar.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source13:       fmtcount.tar.xz
Source14:       fmtcount.doc.tar.xz

%description -n texlive-fmtcount
The package provides commands that display the value of a LaTeX
counter in a variety of formats (ordinal, text, hexadecimal,
decimal, octal, binary etc). The package offers some
multilingual support; configurations for use in English (both
British and American usage), French (including Belgian and
Swiss variants), German, Italian, Portuguese and Spanish
documents are provided. This package was originally provided as
part of the author's datetime package, but is now distributed
separately.

%package -n texlive-fmtcount-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.07svn53912
Release:        0
Summary:        Documentation for texlive-fmtcount
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fmtcount-doc
This package includes the documentation for texlive-fmtcount

%post -n texlive-fmtcount
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fmtcount 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fmtcount
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fmtcount-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fmtcount/CHANGES
%{_texmfdistdir}/doc/latex/fmtcount/README
%{_texmfdistdir}/doc/latex/fmtcount/fc-lang.tex
%{_texmfdistdir}/doc/latex/fmtcount/fmtcount.pdf

%files -n texlive-fmtcount
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/fmtcount/fmtcount.perl
%{_texmfdistdir}/tex/latex/fmtcount/fc-UKenglish.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-USenglish.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-american.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-brazilian.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-british.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-english.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-francais.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-french.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-frenchb.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-german.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-germanb.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-italian.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-ngerman.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-ngermanb.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-portuges.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-portuguese.def
%{_texmfdistdir}/tex/latex/fmtcount/fc-spanish.def
%{_texmfdistdir}/tex/latex/fmtcount/fcnumparser.sty
%{_texmfdistdir}/tex/latex/fmtcount/fcprefix.sty
%{_texmfdistdir}/tex/latex/fmtcount/fmtcount.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fmtcount-%{texlive_version}.%{texlive_noarch}.3.07svn53912-%{release}-zypper
%endif

%package -n texlive-fn2end
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Convert footnotes to endnotes
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
Recommends:     texlive-fn2end-doc >= %{texlive_version}
Provides:       tex(fn2end.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source15:       fn2end.tar.xz
Source16:       fn2end.doc.tar.xz

%description -n texlive-fn2end
Defines macros \makeendnotes, which converts \footnote to
produce endnotes; and \theendnotes which prints them out.

%package -n texlive-fn2end-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Documentation for texlive-fn2end
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fn2end-doc
This package includes the documentation for texlive-fn2end

%post -n texlive-fn2end
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fn2end 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fn2end
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fn2end-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fn2end/fn2end.pdf
%{_texmfdistdir}/doc/latex/fn2end/fn2end.tex

%files -n texlive-fn2end
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fn2end/fn2end.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fn2end-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif

%package -n texlive-fnbreak
Version:        %{texlive_version}.%{texlive_noarch}.1.30svn25003
Release:        0
Summary:        Warn for split footnotes
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
Recommends:     texlive-fnbreak-doc >= %{texlive_version}
Provides:       tex(fnbreak.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source17:       fnbreak.tar.xz
Source18:       fnbreak.doc.tar.xz

%description -n texlive-fnbreak
This package detects footnotes that are split over several
pages, and writes a warning to the log file.

%package -n texlive-fnbreak-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.30svn25003
Release:        0
Summary:        Documentation for texlive-fnbreak
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fnbreak-doc
This package includes the documentation for texlive-fnbreak

%post -n texlive-fnbreak
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fnbreak 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fnbreak
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fnbreak-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fnbreak/ChangeLog
%{_texmfdistdir}/doc/latex/fnbreak/Makefile
%{_texmfdistdir}/doc/latex/fnbreak/README
%{_texmfdistdir}/doc/latex/fnbreak/fnbreak-v.tex
%{_texmfdistdir}/doc/latex/fnbreak/fnbreak.pdf
%{_texmfdistdir}/doc/latex/fnbreak/fnbreak.xml
%{_texmfdistdir}/doc/latex/fnbreak/fnbreaktest.tex

%files -n texlive-fnbreak
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fnbreak/fnbreak.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fnbreak-%{texlive_version}.%{texlive_noarch}.1.30svn25003-%{release}-zypper
%endif

%package -n texlive-fncychap
Version:        %{texlive_version}.%{texlive_noarch}.1.34svn20710
Release:        0
Summary:        Seven predefined chapter heading styles
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
Recommends:     texlive-fncychap-doc >= %{texlive_version}
Provides:       tex(fncychap.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source19:       fncychap.tar.xz
Source20:       fncychap.doc.tar.xz

%description -n texlive-fncychap
Each style can be modified using a set of simple commands.
Optionally one can modify the formatting routines in order to
create additional chapter headings. This package was previously
known as FancyChapter.

%package -n texlive-fncychap-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.34svn20710
Release:        0
Summary:        Documentation for texlive-fncychap
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fncychap-doc
This package includes the documentation for texlive-fncychap

%post -n texlive-fncychap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fncychap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fncychap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fncychap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fncychap/Bjarne.eps
%{_texmfdistdir}/doc/latex/fncychap/Bjarnes.eps
%{_texmfdistdir}/doc/latex/fncychap/Bjornstrup.eps
%{_texmfdistdir}/doc/latex/fncychap/BjornstrupS.eps
%{_texmfdistdir}/doc/latex/fncychap/Conny.eps
%{_texmfdistdir}/doc/latex/fncychap/Connys.eps
%{_texmfdistdir}/doc/latex/fncychap/Glenn.eps
%{_texmfdistdir}/doc/latex/fncychap/Glenns.eps
%{_texmfdistdir}/doc/latex/fncychap/Lenny.eps
%{_texmfdistdir}/doc/latex/fncychap/Lennys.eps
%{_texmfdistdir}/doc/latex/fncychap/README
%{_texmfdistdir}/doc/latex/fncychap/Rejne.eps
%{_texmfdistdir}/doc/latex/fncychap/Rejnes.eps
%{_texmfdistdir}/doc/latex/fncychap/Sonny.eps
%{_texmfdistdir}/doc/latex/fncychap/Sonnys.eps
%{_texmfdistdir}/doc/latex/fncychap/fncychap.pdf
%{_texmfdistdir}/doc/latex/fncychap/fncychap.tex
%{_texmfdistdir}/doc/latex/fncychap/manifest.txt

%files -n texlive-fncychap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fncychap/fncychap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fncychap-%{texlive_version}.%{texlive_noarch}.1.34svn20710-%{release}-zypper
%endif

%package -n texlive-fncylab
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52090
Release:        0
Summary:        Alter the format of \label references
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
Recommends:     texlive-fncylab-doc >= %{texlive_version}
Provides:       tex(fncylab.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source21:       fncylab.tar.xz
Source22:       fncylab.doc.tar.xz

%description -n texlive-fncylab
LaTeX provides a mechanism for altering the appearance of
references to labels, but it's somewhat flawed, and requires
that the user manipulate internal commands. The package solves
the problem, by providing a \labelformat command for changing
the format of references to labels. The package also provides a
\Ref command to make reference to such redefined labels at the
start of a sentence.

%package -n texlive-fncylab-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52090
Release:        0
Summary:        Documentation for texlive-fncylab
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fncylab-doc
This package includes the documentation for texlive-fncylab

%post -n texlive-fncylab
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fncylab 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fncylab
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fncylab-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fncylab/README.md
%{_texmfdistdir}/doc/latex/fncylab/fncylab-example.tex
%{_texmfdistdir}/doc/latex/fncylab/fncylab.pdf
%{_texmfdistdir}/doc/latex/fncylab/fncylab.tex

%files -n texlive-fncylab
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fncylab/fncylab.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fncylab-%{texlive_version}.%{texlive_noarch}.1.1svn52090-%{release}-zypper
%endif

%package -n texlive-fnpara
Version:        %{texlive_version}.%{texlive_noarch}.svn25607
Release:        0
Summary:        Footnotes in paragraphs
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
Recommends:     texlive-fnpara-doc >= %{texlive_version}
Provides:       tex(fnpara.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source23:       fnpara.tar.xz
Source24:       fnpara.doc.tar.xz

%description -n texlive-fnpara
Typeset footnotes in run-on paragraphs, instead of one above
another; this is a re-seating, for the LaTeX environment, of an
example in the TeXbook. The same basic code, improved for use
in e-TeX-based LaTeX, appears in the comprehensive footnote
package footmisc, and superior versions are also available in
the manyfoot and bigfoot packages.

%package -n texlive-fnpara-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn25607
Release:        0
Summary:        Documentation for texlive-fnpara
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fnpara-doc
This package includes the documentation for texlive-fnpara

%post -n texlive-fnpara
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fnpara 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fnpara
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fnpara-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fnpara/fnpara-doc.pdf
%{_texmfdistdir}/doc/latex/fnpara/fnpara-doc.tex

%files -n texlive-fnpara
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fnpara/fnpara.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fnpara-%{texlive_version}.%{texlive_noarch}.svn25607-%{release}-zypper
%endif

%package -n texlive-fnpct
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn54512
Release:        0
Summary:        Manage footnote marks' interaction with punctuation
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
Recommends:     texlive-fnpct-doc >= %{texlive_version}
Provides:       tex(fnpct.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(scrlfile.sty)
Requires:       tex(translations.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source25:       fnpct.tar.xz
Source26:       fnpct.doc.tar.xz

%description -n texlive-fnpct
The package moves footnote marks after following punctuation
(comma or full stop), and adjusts kerning as appropriate. As a
side effect, a change to the handling of multiple footnotes is
provided.

%package -n texlive-fnpct-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn54512
Release:        0
Summary:        Documentation for texlive-fnpct
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fnpct-doc
This package includes the documentation for texlive-fnpct

%post -n texlive-fnpct
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fnpct 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fnpct
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fnpct-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fnpct/README
%{_texmfdistdir}/doc/latex/fnpct/fnpct_en.pdf
%{_texmfdistdir}/doc/latex/fnpct/fnpct_en.tex

%files -n texlive-fnpct
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fnpct/fnpct.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fnpct-%{texlive_version}.%{texlive_noarch}.0.0.5svn54512-%{release}-zypper
%endif

%package -n texlive-fnspe
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn45360
Release:        0
Summary:        Macros for supporting mainly students of FNSPE CTU in Prague
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
Recommends:     texlive-fnspe-doc >= %{texlive_version}
Provides:       tex(fnspe.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bm.sty)
Requires:       tex(listings.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(physics.sty)
Requires:       tex(substr.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source27:       fnspe.tar.xz
Source28:       fnspe.doc.tar.xz

%description -n texlive-fnspe
This package is primary intended for students of FNSPE CTU in
Prague but many other students or scientists can found this
package as useful. This package implements different standards
of tensor notation, interval notation and complex notation.
Further many macros and shortcuts are added, e.q. for spaces,
operators, physics unit, etc.

%package -n texlive-fnspe-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn45360
Release:        0
Summary:        Documentation for texlive-fnspe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fnspe-doc
This package includes the documentation for texlive-fnspe

%post -n texlive-fnspe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fnspe 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fnspe
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fnspe-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fnspe/README
%{_texmfdistdir}/doc/latex/fnspe/fnspe.pdf
%{_texmfdistdir}/doc/latex/fnspe/fnspe.tex

%files -n texlive-fnspe
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fnspe/fnspe.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fnspe-%{texlive_version}.%{texlive_noarch}.1.2asvn45360-%{release}-zypper
%endif

%package -n texlive-fntproof
Version:        %{texlive_version}.%{texlive_noarch}.svn20638
Release:        0
Summary:        A programmable font test pattern generator
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
Recommends:     texlive-fntproof-doc >= %{texlive_version}
Provides:       tex(fntproof.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source29:       fntproof.tar.xz
Source30:       fntproof.doc.tar.xz

%description -n texlive-fntproof
The package implements all the font testing commands of Knuth's
testfont.tex, but arranges that information necessary for each
command is supplied as arguments to that command, rather than
prompted for. This makes it possible to type all the tests in
one command line, and easy to input the package in a file and
to use the commands there. A few additional commands supporting
this last purpose are also made available.

%package -n texlive-fntproof-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20638
Release:        0
Summary:        Documentation for texlive-fntproof
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fntproof-doc
This package includes the documentation for texlive-fntproof

%post -n texlive-fntproof
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fntproof 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fntproof
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fntproof-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/fntproof/README
%{_texmfdistdir}/doc/generic/fntproof/fntproof-doc.pdf
%{_texmfdistdir}/doc/generic/fntproof/fntproof-doc.tex

%files -n texlive-fntproof
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/fntproof/fntproof.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fntproof-%{texlive_version}.%{texlive_noarch}.svn20638-%{release}-zypper
%endif

%package -n texlive-fnumprint
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn29173
Release:        0
Summary:        Print a number in 'appropriate' format
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
Recommends:     texlive-fnumprint-doc >= %{texlive_version}
Provides:       tex(fnumprint.sty)
Requires:       tex(numprint.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(zahl2string.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source31:       fnumprint.tar.xz
Source32:       fnumprint.doc.tar.xz

%description -n texlive-fnumprint
The package defines two macros which decide to typeset a number
either as an Arabic number or as a word (or words) for the
number. If the number is between zero and twelve (including
zero and twelve) then words will be used; if the number is
outside that range, it will be typeset using the package
numprint Words for English representation of numbers are
generated within the package, while those for German are
generated using the package zahl2string.

%package -n texlive-fnumprint-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn29173
Release:        0
Summary:        Documentation for texlive-fnumprint
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fnumprint-doc
This package includes the documentation for texlive-fnumprint

%post -n texlive-fnumprint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fnumprint 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fnumprint
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fnumprint-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fnumprint/README
%{_texmfdistdir}/doc/latex/fnumprint/fnumprint.pdf

%files -n texlive-fnumprint
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fnumprint/fnumprint.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fnumprint-%{texlive_version}.%{texlive_noarch}.1.1asvn29173-%{release}-zypper
%endif

%package -n texlive-foekfont
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        The title font of the Mads Fok magazine
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
Requires:       texlive-foekfont-fonts >= %{texlive_version}
Recommends:     texlive-foekfont-doc >= %{texlive_version}
Provides:       tex(foekfont.map)
Provides:       tex(foekfont.sty)
Provides:       tex(foekfont.tfm)
Provides:       tex(ot1foekfont.fd)
Provides:       tex(t1foekfont.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source33:       foekfont.tar.xz
Source34:       foekfont.doc.tar.xz

%description -n texlive-foekfont
The bundle provides an Adobe Type 1 font, and LaTeX support for
its use. The magazine web site shows the font in use in a few
places.

%package -n texlive-foekfont-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-foekfont
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-foekfont-doc
This package includes the documentation for texlive-foekfont


%package -n texlive-foekfont-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Severed fonts for texlive-foekfont
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-foekfont-fonts
The  separated fonts package for texlive-foekfont
%post -n texlive-foekfont
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap foekfont.map' >> /var/run/texlive/run-updmap

%postun -n texlive-foekfont 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap foekfont.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-foekfont
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-foekfont-fonts
%files -n texlive-foekfont-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/foekfont/FoekFont.sfd
%{_texmfdistdir}/doc/latex/foekfont/README
%{_texmfdistdir}/doc/latex/foekfont/foekfont.pdf
%{_texmfdistdir}/doc/latex/foekfont/foekfont.tex

%files -n texlive-foekfont
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/foekfont/foekfont.map
%{_texmfdistdir}/fonts/tfm/public/foekfont/foekfont.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/foekfont/FoekFont.pfb
%{_texmfdistdir}/tex/latex/foekfont/foekfont.sty
%{_texmfdistdir}/tex/latex/foekfont/ot1foekfont.fd
%{_texmfdistdir}/tex/latex/foekfont/t1foekfont.fd

%files -n texlive-foekfont-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-foekfont
%{_datadir}/fontconfig/conf.avail/58-texlive-foekfont.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-foekfont/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-foekfont/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-foekfont/fonts.scale
%{_datadir}/fonts/texlive-foekfont/FoekFont.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-foekfont-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-foilhtml
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn21855
Release:        0
Summary:        Interface between foiltex and LaTeX2HTML
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
Recommends:     texlive-foilhtml-doc >= %{texlive_version}
Provides:       tex(foilhtml.cfg)
Provides:       tex(foilhtml.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source35:       foilhtml.tar.xz
Source36:       foilhtml.doc.tar.xz

%description -n texlive-foilhtml
Provides integration between FoilTeX and LaTeX2HTML, adding
sectioning commands and elements of logical formatting to
FoilTeX and providing support for FoilTeX commands in
LaTeX2HTML.

%package -n texlive-foilhtml-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn21855
Release:        0
Summary:        Documentation for texlive-foilhtml
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-foilhtml-doc
This package includes the documentation for texlive-foilhtml

%post -n texlive-foilhtml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-foilhtml 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-foilhtml
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-foilhtml-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/foilhtml/foilhtml-96.perl
%{_texmfdistdir}/doc/latex/foilhtml/foils-97.perl
%{_texmfdistdir}/doc/latex/foilhtml/foils.perl
%{_texmfdistdir}/doc/latex/foilhtml/readme.v12

%files -n texlive-foilhtml
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/foilhtml/foilhtml.cfg
%{_texmfdistdir}/tex/latex/foilhtml/foilhtml.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-foilhtml-%{texlive_version}.%{texlive_noarch}.1.2svn21855-%{release}-zypper
%endif

%package -n texlive-fonetika
Version:        %{texlive_version}.%{texlive_noarch}.svn21326
Release:        0
Summary:        Support for the Danish "Dania" phonetic system
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
Requires:       texlive-fonetika-fonts >= %{texlive_version}
Recommends:     texlive-fonetika-doc >= %{texlive_version}
Provides:       tex(fonetika.map)
Provides:       tex(fonetika.sty)
Provides:       tex(fonetika.tfm)
Provides:       tex(fonetikabold.tfm)
Provides:       tex(fonetikasans.tfm)
Provides:       tex(fonetikasansbold.tfm)
Provides:       tex(t1fonetika.fd)
Requires:       tex(fontenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source37:       fonetika.tar.xz
Source38:       fonetika.doc.tar.xz

%description -n texlive-fonetika
Fonetika Dania is a font bundle with a serif font and a sans
serif font for the danish phonetic system Dania. Both fonts
exist in regular and bold weights. LaTeX support is provided.
The fonts are based on URW Palladio and Iwona Condensed, and
were created using FontForge.

%package -n texlive-fonetika-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn21326
Release:        0
Summary:        Documentation for texlive-fonetika
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fonetika-doc
This package includes the documentation for texlive-fonetika


%package -n texlive-fonetika-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn21326
Release:        0
Summary:        Severed fonts for texlive-fonetika
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fonetika-fonts
The  separated fonts package for texlive-fonetika
%post -n texlive-fonetika
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap fonetika.map' >> /var/run/texlive/run-updmap

%postun -n texlive-fonetika 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap fonetika.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-fonetika
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fonetika-fonts
%files -n texlive-fonetika-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fonetika/README
%{_texmfdistdir}/doc/fonts/fonetika/fonetika.pdf
%{_texmfdistdir}/doc/fonts/fonetika/fonetika.tex

%files -n texlive-fonetika
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaIwonaeBold.afm
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaIwonaeRegular.afm
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaPallaeBold.afm
%{_texmfdistdir}/fonts/afm/public/fonetika/FonetikaDaniaPallaeRegular.afm
%{_texmfdistdir}/fonts/map/dvips/fonetika/fonetika.map
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetika.tfm
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetikabold.tfm
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetikasans.tfm
%{_texmfdistdir}/fonts/tfm/public/fonetika/fonetikasansbold.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaIwonaeBold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaIwonaeRegular.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaPallaeBold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonetika/FonetikaDaniaPallaeRegular.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaIwonaeBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaIwonaeRegular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaPallaeBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonetika/FonetikaDaniaPallaeRegular.pfb
%{_texmfdistdir}/tex/latex/fonetika/fonetika.sty
%{_texmfdistdir}/tex/latex/fonetika/t1fonetika.fd

%files -n texlive-fonetika-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fonetika
%{_datadir}/fontconfig/conf.avail/58-texlive-fonetika.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-fonetika.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-fonetika.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonetika/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonetika/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonetika/fonts.scale
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaIwonaeBold.ttf
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaIwonaeRegular.ttf
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaPallaeBold.ttf
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaPallaeRegular.ttf
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaIwonaeBold.pfb
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaIwonaeRegular.pfb
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaPallaeBold.pfb
%{_datadir}/fonts/texlive-fonetika/FonetikaDaniaPallaeRegular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fonetika-fonts-%{texlive_version}.%{texlive_noarch}.svn21326-%{release}-zypper
%endif

%package -n texlive-font-change
Version:        %{texlive_version}.%{texlive_noarch}.2015.2svn40403
Release:        0
Summary:        Macros to change text and mathematics fonts in plain TeX
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
Recommends:     texlive-font-change-doc >= %{texlive_version}
Provides:       tex(default-amssymbols.tex)
Provides:       tex(font_antp_euler.tex)
Provides:       tex(font_antt-condensed-light.tex)
Provides:       tex(font_antt-condensed-medium.tex)
Provides:       tex(font_antt-condensed.tex)
Provides:       tex(font_antt-light.tex)
Provides:       tex(font_antt-medium.tex)
Provides:       tex(font_antt.tex)
Provides:       tex(font_arev.tex)
Provides:       tex(font_artemisia_euler.tex)
Provides:       tex(font_bera_concrete.tex)
Provides:       tex(font_bera_euler.tex)
Provides:       tex(font_bera_fnc.tex)
Provides:       tex(font_bookman.tex)
Provides:       tex(font_century.tex)
Provides:       tex(font_charter.tex)
Provides:       tex(font_cm.tex)
Provides:       tex(font_cmbright.tex)
Provides:       tex(font_concrete.tex)
Provides:       tex(font_epigrafica_euler.tex)
Provides:       tex(font_epigrafica_palatino.tex)
Provides:       tex(font_iwona-bold.tex)
Provides:       tex(font_iwona-condensed-bold.tex)
Provides:       tex(font_iwona-condensed-light.tex)
Provides:       tex(font_iwona-condensed-medium.tex)
Provides:       tex(font_iwona-condensed.tex)
Provides:       tex(font_iwona-light.tex)
Provides:       tex(font_iwona-medium.tex)
Provides:       tex(font_iwona.tex)
Provides:       tex(font_kp-light.tex)
Provides:       tex(font_kp.tex)
Provides:       tex(font_kurier-bold.tex)
Provides:       tex(font_kurier-condensed-bold.tex)
Provides:       tex(font_kurier-condensed-light.tex)
Provides:       tex(font_kurier-condensed-medium.tex)
Provides:       tex(font_kurier-condensed.tex)
Provides:       tex(font_kurier-light.tex)
Provides:       tex(font_kurier-medium.tex)
Provides:       tex(font_kurier.tex)
Provides:       tex(font_libertine_kp.tex)
Provides:       tex(font_libertine_palatino.tex)
Provides:       tex(font_libertine_times.tex)
Provides:       tex(font_mdutopia.tex)
Provides:       tex(font_pagella.tex)
Provides:       tex(font_palatino.tex)
Provides:       tex(font_times.tex)
Provides:       tex(font_utopia.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source39:       font-change.tar.xz
Source40:       font-change.doc.tar.xz

%description -n texlive-font-change
Macros to Change Text and Mathematics fonts in TeX: 45
Beautiful Variants The macros are written for plain TeX and may
be used with other packages like AmSTeX, eplain, etc. They also
work with XeTeX. The macros allow users to change the fonts
(for both text and mathematics) in their TeX document with only
one statement. The fonts may be used readily at various
predefined sizes. All the fonts called by these macro files are
free and are included in current MiKTeX and TeX Live
distributions.

%package -n texlive-font-change-doc
Version:        %{texlive_version}.%{texlive_noarch}.2015.2svn40403
Release:        0
Summary:        Documentation for texlive-font-change
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-font-change-doc
This package includes the documentation for texlive-font-change

%post -n texlive-font-change
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-font-change 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-font-change
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-font-change-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/font-change/README.txt
%{_texmfdistdir}/doc/plain/font-change/font-change.pdf
%{_texmfdistdir}/doc/plain/font-change/font-change.tex
%{_texmfdistdir}/doc/plain/font-change/font-change_FRENCH.pdf
%{_texmfdistdir}/doc/plain/font-change/font-change_FRENCH.tex

%files -n texlive-font-change
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/font-change/default-amssymbols.tex
%{_texmfdistdir}/tex/plain/font-change/font_antp_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-condensed-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-condensed-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-condensed.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_antt.tex
%{_texmfdistdir}/tex/plain/font-change/font_arev.tex
%{_texmfdistdir}/tex/plain/font-change/font_artemisia_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_bera_concrete.tex
%{_texmfdistdir}/tex/plain/font-change/font_bera_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_bera_fnc.tex
%{_texmfdistdir}/tex/plain/font-change/font_bookman.tex
%{_texmfdistdir}/tex/plain/font-change/font_century.tex
%{_texmfdistdir}/tex/plain/font-change/font_charter.tex
%{_texmfdistdir}/tex/plain/font-change/font_cm.tex
%{_texmfdistdir}/tex/plain/font-change/font_cmbright.tex
%{_texmfdistdir}/tex/plain/font-change/font_concrete.tex
%{_texmfdistdir}/tex/plain/font-change/font_epigrafica_euler.tex
%{_texmfdistdir}/tex/plain/font-change/font_epigrafica_palatino.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-condensed.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_iwona.tex
%{_texmfdistdir}/tex/plain/font-change/font_kp-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_kp.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed-bold.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-condensed.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-light.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier-medium.tex
%{_texmfdistdir}/tex/plain/font-change/font_kurier.tex
%{_texmfdistdir}/tex/plain/font-change/font_libertine_kp.tex
%{_texmfdistdir}/tex/plain/font-change/font_libertine_palatino.tex
%{_texmfdistdir}/tex/plain/font-change/font_libertine_times.tex
%{_texmfdistdir}/tex/plain/font-change/font_mdutopia.tex
%{_texmfdistdir}/tex/plain/font-change/font_pagella.tex
%{_texmfdistdir}/tex/plain/font-change/font_palatino.tex
%{_texmfdistdir}/tex/plain/font-change/font_times.tex
%{_texmfdistdir}/tex/plain/font-change/font_utopia.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-font-change-%{texlive_version}.%{texlive_noarch}.2015.2svn40403-%{release}-zypper
%endif

%package -n texlive-font-change-xetex
Version:        %{texlive_version}.%{texlive_noarch}.2016.1svn40404
Release:        0
Summary:        Macros to change text and mathematics fonts in plain XeTeX
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
Recommends:     texlive-font-change-xetex-doc >= %{texlive_version}
Provides:       tex(font-change-xetex.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source41:       font-change-xetex.tar.xz
Source42:       font-change-xetex.doc.tar.xz

%description -n texlive-font-change-xetex
This package consists of macros that can be used to typeset
"plain" XeTeX documents using any OpenType or TrueType font
installed on the computer system. The macros allow the user to
change the text mode fonts and some math mode fonts. For any
declared font family, various font style, weight, and size
variants like bold, italics, small caps, etc., are available
through standard and custom TeX control statements. Using the
optional argument of the macros, the available XeTeX font
features and OpenType tags can be accessed. Other features of
the package include activating and deactivating hanging
punctuation, and support for special Unicode characters.

%package -n texlive-font-change-xetex-doc
Version:        %{texlive_version}.%{texlive_noarch}.2016.1svn40404
Release:        0
Summary:        Documentation for texlive-font-change-xetex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-font-change-xetex-doc
This package includes the documentation for texlive-font-change-xetex

%post -n texlive-font-change-xetex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-font-change-xetex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-font-change-xetex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-font-change-xetex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xetex/font-change-xetex/README.txt
%{_texmfdistdir}/doc/xetex/font-change-xetex/font-change-xetex.pdf
%{_texmfdistdir}/doc/xetex/font-change-xetex/font-change-xetex.tex

%files -n texlive-font-change-xetex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xetex/font-change-xetex/font-change-xetex.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-font-change-xetex-%{texlive_version}.%{texlive_noarch}.2016.1svn40404-%{release}-zypper
%endif

%package -n texlive-fontawesome
Version:        %{texlive_version}.%{texlive_noarch}.4.6.3.2svn48145
Release:        0
Summary:        Font containing web-related icons
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
Requires:       texlive-fontawesome-fonts >= %{texlive_version}
Recommends:     texlive-fontawesome-doc >= %{texlive_version}
Provides:       tex(FontAwesome--fontawesomeone.tfm)
Provides:       tex(FontAwesome--fontawesomethree.tfm)
Provides:       tex(FontAwesome--fontawesometwo.tfm)
Provides:       tex(fontawesome.map)
Provides:       tex(fontawesome.sty)
Provides:       tex(fontawesomeone.enc)
Provides:       tex(fontawesomesymbols-generic.tex)
Provides:       tex(fontawesomesymbols-pdftex.tex)
Provides:       tex(fontawesomesymbols-xeluatex.tex)
Provides:       tex(fontawesomethree.enc)
Provides:       tex(fontawesometwo.enc)
Provides:       tex(ufontawesomeone.fd)
Provides:       tex(ufontawesomethree.fd)
Provides:       tex(ufontawesometwo.fd)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source43:       fontawesome.tar.xz
Source44:       fontawesome.doc.tar.xz

%description -n texlive-fontawesome
The package offers access to the large number of web-related
icons provided by the included font. The package requires the
package, fontspec, if run with XeTeX or LuaTeX.

%package -n texlive-fontawesome-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.6.3.2svn48145
Release:        0
Summary:        Documentation for texlive-fontawesome
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontawesome-doc
This package includes the documentation for texlive-fontawesome


%package -n texlive-fontawesome-fonts
Version:        %{texlive_version}.%{texlive_noarch}.4.6.3.2svn48145
Release:        0
Summary:        Severed fonts for texlive-fontawesome
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fontawesome-fonts
The  separated fonts package for texlive-fontawesome
%post -n texlive-fontawesome
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap fontawesome.map' >> /var/run/texlive/run-updmap

%postun -n texlive-fontawesome 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap fontawesome.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-fontawesome
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fontawesome-fonts
%files -n texlive-fontawesome-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fontawesome/README.md
%{_texmfdistdir}/doc/fonts/fontawesome/fontawesome.pdf
%{_texmfdistdir}/doc/fonts/fontawesome/fontawesome.tex

%files -n texlive-fontawesome
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/fontawesome/fontawesomeone.enc
%{_texmfdistdir}/fonts/enc/dvips/fontawesome/fontawesomethree.enc
%{_texmfdistdir}/fonts/enc/dvips/fontawesome/fontawesometwo.enc
%{_texmfdistdir}/fonts/map/dvips/fontawesome/fontawesome.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fontawesome/FontAwesome.otf
%{_texmfdistdir}/fonts/tfm/public/fontawesome/FontAwesome--fontawesomeone.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome/FontAwesome--fontawesomethree.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome/FontAwesome--fontawesometwo.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fontawesome/FontAwesome.pfb
%{_texmfdistdir}/tex/latex/fontawesome/fontawesome.sty
%{_texmfdistdir}/tex/latex/fontawesome/fontawesomesymbols-generic.tex
%{_texmfdistdir}/tex/latex/fontawesome/fontawesomesymbols-pdftex.tex
%{_texmfdistdir}/tex/latex/fontawesome/fontawesomesymbols-xeluatex.tex
%{_texmfdistdir}/tex/latex/fontawesome/ufontawesomeone.fd
%{_texmfdistdir}/tex/latex/fontawesome/ufontawesomethree.fd
%{_texmfdistdir}/tex/latex/fontawesome/ufontawesometwo.fd

%files -n texlive-fontawesome-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fontawesome
%{_datadir}/fontconfig/conf.avail/58-texlive-fontawesome.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-fontawesome.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-fontawesome.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontawesome/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontawesome/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontawesome/fonts.scale
%{_datadir}/fonts/texlive-fontawesome/FontAwesome.otf
%{_datadir}/fonts/texlive-fontawesome/FontAwesome.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontawesome-fonts-%{texlive_version}.%{texlive_noarch}.4.6.3.2svn48145-%{release}-zypper
%endif

%package -n texlive-fontawesome5
Version:        %{texlive_version}.%{texlive_noarch}.5.13.0svn54517
Release:        0
Summary:        Font Awesome 5 with LaTeX support
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
Requires:       texlive-fontawesome5-fonts >= %{texlive_version}
Recommends:     texlive-fontawesome5-doc >= %{texlive_version}
Provides:       tex(fa5brands0.enc)
Provides:       tex(fa5brands0.tfm)
Provides:       tex(fa5brands1.enc)
Provides:       tex(fa5brands1.tfm)
Provides:       tex(fa5free0.enc)
Provides:       tex(fa5free0regular.tfm)
Provides:       tex(fa5free0solid.tfm)
Provides:       tex(fa5free1.enc)
Provides:       tex(fa5free1regular.tfm)
Provides:       tex(fa5free1solid.tfm)
Provides:       tex(fa5free2.enc)
Provides:       tex(fa5free2regular.tfm)
Provides:       tex(fa5free2solid.tfm)
Provides:       tex(fa5free3.enc)
Provides:       tex(fa5free3regular.tfm)
Provides:       tex(fa5free3solid.tfm)
Provides:       tex(fontawesome5-generic-helper.sty)
Provides:       tex(fontawesome5-mapping.def)
Provides:       tex(fontawesome5-utex-helper.sty)
Provides:       tex(fontawesome5.map)
Provides:       tex(fontawesome5.sty)
Provides:       tex(tufontawesomebrands.fd)
Provides:       tex(tufontawesomefree.fd)
Provides:       tex(tufontawesomepro.fd)
Provides:       tex(ufontawesomebrands0.fd)
Provides:       tex(ufontawesomebrands1.fd)
Provides:       tex(ufontawesomefree0.fd)
Provides:       tex(ufontawesomefree1.fd)
Provides:       tex(ufontawesomefree2.fd)
Provides:       tex(ufontawesomefree3.fd)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source45:       fontawesome5.tar.xz
Source46:       fontawesome5.doc.tar.xz

%description -n texlive-fontawesome5
This package provides LaTeX support for the included "Font
Awesome 5 Free" icon set. These icons were designed by Fort
Awesome and released under the SIL OFL 1.1 license. The
commercial "Pro" version is also supported, if it is installed
and XeLaTeX or LuaLaTeX is used.

%package -n texlive-fontawesome5-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.13.0svn54517
Release:        0
Summary:        Documentation for texlive-fontawesome5
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontawesome5-doc
This package includes the documentation for texlive-fontawesome5


%package -n texlive-fontawesome5-fonts
Version:        %{texlive_version}.%{texlive_noarch}.5.13.0svn54517
Release:        0
Summary:        Severed fonts for texlive-fontawesome5
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fontawesome5-fonts
The  separated fonts package for texlive-fontawesome5
%post -n texlive-fontawesome5
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap fontawesome5.map' >> /var/run/texlive/run-updmap

%postun -n texlive-fontawesome5 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap fontawesome5.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-fontawesome5
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fontawesome5-fonts
%files -n texlive-fontawesome5-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fontawesome5/README.md
%{_texmfdistdir}/doc/fonts/fontawesome5/fontawesome5.pdf
%{_texmfdistdir}/doc/fonts/fontawesome5/fontawesome5.tex
%{_texmfdistdir}/doc/fonts/fontawesome5/fulllist.tex

%files -n texlive-fontawesome5
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/fontawesome5/fa5brands0.enc
%{_texmfdistdir}/fonts/enc/dvips/fontawesome5/fa5brands1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontawesome5/fa5free0.enc
%{_texmfdistdir}/fonts/enc/dvips/fontawesome5/fa5free1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontawesome5/fa5free2.enc
%{_texmfdistdir}/fonts/enc/dvips/fontawesome5/fa5free3.enc
%{_texmfdistdir}/fonts/map/dvips/fontawesome5/fontawesome5.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fontawesome5/FontAwesome5Brands-Regular-400.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fontawesome5/FontAwesome5Free-Regular-400.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fontawesome5/FontAwesome5Free-Solid-900.otf
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5brands0.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5brands1.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free0regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free0solid.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free1regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free1solid.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free2regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free2solid.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free3regular.tfm
%{_texmfdistdir}/fonts/tfm/public/fontawesome5/fa5free3solid.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fontawesome5/FontAwesome5Brands-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fontawesome5/FontAwesome5Free-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fontawesome5/FontAwesome5Free-Solid.pfb
%{_texmfdistdir}/tex/latex/fontawesome5/fontawesome5-generic-helper.sty
%{_texmfdistdir}/tex/latex/fontawesome5/fontawesome5-mapping.def
%{_texmfdistdir}/tex/latex/fontawesome5/fontawesome5-utex-helper.sty
%{_texmfdistdir}/tex/latex/fontawesome5/fontawesome5.lua
%{_texmfdistdir}/tex/latex/fontawesome5/fontawesome5.sty
%{_texmfdistdir}/tex/latex/fontawesome5/tufontawesomebrands.fd
%{_texmfdistdir}/tex/latex/fontawesome5/tufontawesomefree.fd
%{_texmfdistdir}/tex/latex/fontawesome5/tufontawesomepro.fd
%{_texmfdistdir}/tex/latex/fontawesome5/ufontawesomebrands0.fd
%{_texmfdistdir}/tex/latex/fontawesome5/ufontawesomebrands1.fd
%{_texmfdistdir}/tex/latex/fontawesome5/ufontawesomefree0.fd
%{_texmfdistdir}/tex/latex/fontawesome5/ufontawesomefree1.fd
%{_texmfdistdir}/tex/latex/fontawesome5/ufontawesomefree2.fd
%{_texmfdistdir}/tex/latex/fontawesome5/ufontawesomefree3.fd

%files -n texlive-fontawesome5-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fontawesome5
%{_datadir}/fontconfig/conf.avail/58-texlive-fontawesome5.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-fontawesome5.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-fontawesome5.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontawesome5/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontawesome5/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontawesome5/fonts.scale
%{_datadir}/fonts/texlive-fontawesome5/FontAwesome5Brands-Regular-400.otf
%{_datadir}/fonts/texlive-fontawesome5/FontAwesome5Free-Regular-400.otf
%{_datadir}/fonts/texlive-fontawesome5/FontAwesome5Free-Solid-900.otf
%{_datadir}/fonts/texlive-fontawesome5/FontAwesome5Brands-Regular.pfb
%{_datadir}/fonts/texlive-fontawesome5/FontAwesome5Free-Regular.pfb
%{_datadir}/fonts/texlive-fontawesome5/FontAwesome5Free-Solid.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontawesome5-fonts-%{texlive_version}.%{texlive_noarch}.5.13.0svn54517-%{release}-zypper
%endif

%package -n texlive-fontaxes
Version:        %{texlive_version}.%{texlive_noarch}.1.0dsvn33276
Release:        0
Summary:        Additional font axes for LaTeX
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
Recommends:     texlive-fontaxes-doc >= %{texlive_version}
Provides:       tex(fontaxes.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source47:       fontaxes.tar.xz
Source48:       fontaxes.doc.tar.xz

%description -n texlive-fontaxes
The package adds several new font axes on top of LaTeX's New
Font Selection Scheme. In particular, it splits the shape axis
into a primary and a secondary shape axis, and it adds three
new axes to deal with the different figure versions offered by
many professional fonts.

%package -n texlive-fontaxes-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0dsvn33276
Release:        0
Summary:        Documentation for texlive-fontaxes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontaxes-doc
This package includes the documentation for texlive-fontaxes

%post -n texlive-fontaxes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontaxes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontaxes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontaxes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fontaxes/README
%{_texmfdistdir}/doc/latex/fontaxes/fontaxes.pdf
%{_texmfdistdir}/doc/latex/fontaxes/test-fontaxes.tex

%files -n texlive-fontaxes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fontaxes/fontaxes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontaxes-%{texlive_version}.%{texlive_noarch}.1.0dsvn33276-%{release}-zypper
%endif

%package -n texlive-fontbook
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn23608
Release:        0
Summary:        Generate a font book
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
Recommends:     texlive-fontbook-doc >= %{texlive_version}
Provides:       tex(fontbook.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source49:       fontbook.tar.xz
Source50:       fontbook.doc.tar.xz

%description -n texlive-fontbook
The package provides a means of producing a 'book' of font
samples (for evaluation, etc.).

%package -n texlive-fontbook-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn23608
Release:        0
Summary:        Documentation for texlive-fontbook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontbook-doc
This package includes the documentation for texlive-fontbook

%post -n texlive-fontbook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontbook 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontbook
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontbook-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/fontbook/README
%{_texmfdistdir}/doc/xelatex/fontbook/fontbook-freefonts.pdf
%{_texmfdistdir}/doc/xelatex/fontbook/fontbook-freefonts.tex
%{_texmfdistdir}/doc/xelatex/fontbook/fontbook.pdf

%files -n texlive-fontbook
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/fontbook/fontbook.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontbook-%{texlive_version}.%{texlive_noarch}.0.0.2svn23608-%{release}-zypper
%endif

%package -n texlive-fontch
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn17859
Release:        0
Summary:        Changing fonts, sizes and encodings in Plain TeX
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
Recommends:     texlive-fontch-doc >= %{texlive_version}
Provides:       tex(DSmac.tex)
Provides:       tex(TS1mac.tex)
Provides:       tex(bsymbols.tex)
Provides:       tex(fontch.tex)
Provides:       tex(fontch_doc.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source51:       fontch.tar.xz
Source52:       fontch.doc.tar.xz

%description -n texlive-fontch
The fontch macros allow the user to change font size and family
anywhere in a plain TeX document. Sizes of 8, 10, 12, 14, 20
and 24 points are available. A sans serif family (\sf) is
defined in addition to the families already defined in plain
TeX. Optional support for Latin Modern T1 and TS1 fonts is
given. There are macros for non-latin1 letters and for most TS1
symbols. Math mode always uses CM fonts. A command for
producing doubled-spaced documents is also provided. The
present version of the package is designed to deal with the
latest release of the Latin Modern fonts version 1.106.
Unfortunately, it can no longer support earlier versions of the
fonts, so an obsolete version of the package is retained for
users who don't yet have access to the latest version of the
fonts.

%package -n texlive-fontch-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn17859
Release:        0
Summary:        Documentation for texlive-fontch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontch-doc
This package includes the documentation for texlive-fontch

%post -n texlive-fontch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/fontch/README
%{_texmfdistdir}/doc/plain/fontch/fontch.pdf

%files -n texlive-fontch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/fontch/DSmac.tex
%{_texmfdistdir}/tex/plain/fontch/TS1mac.tex
%{_texmfdistdir}/tex/plain/fontch/bsymbols.tex
%{_texmfdistdir}/tex/plain/fontch/fontch.tex
%{_texmfdistdir}/tex/plain/fontch/fontch_doc.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontch-%{texlive_version}.%{texlive_noarch}.2.2svn17859-%{release}-zypper
%endif

%package -n texlive-fontinst
Version:        %{texlive_version}.%{texlive_noarch}.1.933svn53562
Release:        0
Summary:        Help with installing fonts for TeX and LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-fontinst-bin >= %{texlive_version}
#!BuildIgnore: texlive-fontinst-bin
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
Recommends:     texlive-fontinst-doc >= %{texlive_version}
Provides:       tex(bbox.sty)
Provides:       tex(cfntinst.sty)
Provides:       tex(csc2x.tex)
Provides:       tex(csckrn2x.tex)
Provides:       tex(finstmsc.sty)
Provides:       tex(fontdoc.sty)
Provides:       tex(fontinst.sty)
Provides:       tex(multislot.sty)
Provides:       tex(osf2x.tex)
Provides:       tex(xfntinst.sty)
Requires:       tex(amstext.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source53:       fontinst.tar.xz
Source54:       fontinst.doc.tar.xz

%description -n texlive-fontinst
TeX macros for converting Adobe Font Metric files to TeX metric
and virtual font format. Fontinst helps mainly with the number
crunching and shovelling parts of font installation. This means
in practice that it creates a number of files which give the
TeX metrics (and related information) for a font family that
(La)TeX needs to do any typesetting in these fonts. Fontinst
furthermore makes it easy to create fonts containing glyphs
from more than one base font, taking advantage of (e.g.)
"expert" font sets. Fontinst cannot examine files to see if
they contain any useful information, nor automatically search
for files or work with binary file formats; those tasks must
normally be done manually or with the help of some other tool,
such as the pltotf and vptovf programs.

%package -n texlive-fontinst-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.933svn53562
Release:        0
Summary:        Documentation for texlive-fontinst
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(fontinst.1)

%description -n texlive-fontinst-doc
This package includes the documentation for texlive-fontinst

%post -n texlive-fontinst
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontinst 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontinst
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontinst-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fontinst/README
%{_texmfdistdir}/doc/fonts/fontinst/encspecs/encspecs.tex
%{_texmfdistdir}/doc/fonts/fontinst/encspecs/omxdraft.etx
%{_texmfdistdir}/doc/fonts/fontinst/encspecs/ot1draft.etx
%{_texmfdistdir}/doc/fonts/fontinst/encspecs/t1draft.etx
%{_texmfdistdir}/doc/fonts/fontinst/examples/basic/basicex.tex
%{_texmfdistdir}/doc/fonts/fontinst/examples/basic/basicex2.tex
%{_texmfdistdir}/doc/fonts/fontinst/examples/eurofont/Makefile
%{_texmfdistdir}/doc/fonts/fontinst/examples/eurofont/eurofont.map
%{_texmfdistdir}/doc/fonts/fontinst/examples/eurofont/eurofont.tex
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/Makefile
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/fontptcm.tex
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/mathtest.tex
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/resetsy.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/unsetmu.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrmhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrmkern.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zrvhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptm/zryhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/Makefile
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/fontptcmx.tex
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/mathptmx.sty
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/mathtestx.tex
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/resetsy.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/unsetmu.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrmhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrmkernx.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrvhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zryhax.mtx
%{_texmfdistdir}/doc/fonts/fontinst/examples/mathptmx/zrykernx.mtx
%{_texmfdistdir}/doc/fonts/fontinst/manual/fontinst.pdf
%{_texmfdistdir}/doc/fonts/fontinst/manual/fontinst.tex
%{_texmfdistdir}/doc/fonts/fontinst/manual/intro98.pdf
%{_texmfdistdir}/doc/fonts/fontinst/manual/intro98.tex
%{_texmfdistdir}/doc/fonts/fontinst/manual/roadmap.eps
%{_texmfdistdir}/doc/fonts/fontinst/talks/et99-font-tables.pdf
%{_texmfdistdir}/doc/fonts/fontinst/talks/et99-font-tutorial.pdf
%{_texmfdistdir}/doc/fonts/fontinst/test/cc-pl.enc
%{_texmfdistdir}/doc/fonts/fontinst/test/comparemetrics.sty
%{_texmfdistdir}/doc/fonts/fontinst/test/comparepls.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/fadrr.mtx
%{_texmfdistdir}/doc/fonts/fontinst/test/multislot-test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/multislot.etx
%{_texmfdistdir}/doc/fonts/fontinst/test/omsdraft.etx
%{_texmfdistdir}/doc/fonts/fontinst/test/testsc.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1901test.mtx
%{_texmfdistdir}/doc/fonts/fontinst/test/v1901test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1902test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1905test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1906test.etx
%{_texmfdistdir}/doc/fonts/fontinst/test/v1906test.mtx
%{_texmfdistdir}/doc/fonts/fontinst/test/v1906test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1913test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1914test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1914testmap.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1914testshow.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1915test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1915testmap.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1916test.mtx
%{_texmfdistdir}/doc/fonts/fontinst/test/v1916test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1916test2.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1923test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1927test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1928test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1928test2.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1930test.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1931test0.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1931test1.tex
%{_texmfdistdir}/doc/fonts/fontinst/test/v1931test2.tex
%{_mandir}/man1/fontinst.1*

%files -n texlive-fontinst
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/texlive-extra/fontinst.sh
%{_texmfdistdir}/tex/fontinst/base/bbox.sty
%{_texmfdistdir}/tex/fontinst/base/cfntinst.sty
%{_texmfdistdir}/tex/fontinst/base/finstmsc.sty
%{_texmfdistdir}/tex/fontinst/base/fontinst.ini
%{_texmfdistdir}/tex/fontinst/base/fontinst.sty
%{_texmfdistdir}/tex/fontinst/base/multislot.sty
%{_texmfdistdir}/tex/fontinst/base/xfntinst.sty
%{_texmfdistdir}/tex/fontinst/latinetx/8r.etx
%{_texmfdistdir}/tex/fontinst/latinetx/8y.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1c.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1cj.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1ctt.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1i.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1ij.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1itt.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1j.etx
%{_texmfdistdir}/tex/fontinst/latinetx/ot1tt.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1c.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1cj.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1i.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1ij.etx
%{_texmfdistdir}/tex/fontinst/latinetx/t1j.etx
%{_texmfdistdir}/tex/fontinst/latinetx/txtfdmns.etx
%{_texmfdistdir}/tex/fontinst/latinmtx/8r.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/8y.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/latin.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/latinsc.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/llbuild.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lsbuild.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lsfake.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lsmisc.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/ltcmds.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/ltpunct.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/lubuild.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/newlatin.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/resetsc.mtx
%{_texmfdistdir}/tex/fontinst/latinmtx/unsetalf.mtx
%{_texmfdistdir}/tex/fontinst/mathetx/euex.etx
%{_texmfdistdir}/tex/fontinst/mathetx/eufrak.etx
%{_texmfdistdir}/tex/fontinst/mathetx/eurm.etx
%{_texmfdistdir}/tex/fontinst/mathetx/euscr.etx
%{_texmfdistdir}/tex/fontinst/mathetx/msam.etx
%{_texmfdistdir}/tex/fontinst/mathetx/msbm.etx
%{_texmfdistdir}/tex/fontinst/mathetx/oml.etx
%{_texmfdistdir}/tex/fontinst/mathetx/oms.etx
%{_texmfdistdir}/tex/fontinst/mathetx/omx.etx
%{_texmfdistdir}/tex/fontinst/mathetx/rsfs.etx
%{_texmfdistdir}/tex/fontinst/mathmtx/mathex.mtx
%{_texmfdistdir}/tex/fontinst/mathmtx/mathit.mtx
%{_texmfdistdir}/tex/fontinst/mathmtx/mathsy.mtx
%{_texmfdistdir}/tex/fontinst/misc/csc2x.tex
%{_texmfdistdir}/tex/fontinst/misc/csckrn2x.tex
%{_texmfdistdir}/tex/fontinst/misc/glyphbox.mtx
%{_texmfdistdir}/tex/fontinst/misc/glyphoff.mtx
%{_texmfdistdir}/tex/fontinst/misc/glyphon.mtx
%{_texmfdistdir}/tex/fontinst/misc/kernoff.mtx
%{_texmfdistdir}/tex/fontinst/misc/kernon.mtx
%{_texmfdistdir}/tex/fontinst/misc/osf2x.tex
%{_texmfdistdir}/tex/fontinst/smbletx/digit2.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1i.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1ij.etx
%{_texmfdistdir}/tex/fontinst/smbletx/ts1j.etx
%{_texmfdistdir}/tex/fontinst/smblmtx/resetosf.mtx
%{_texmfdistdir}/tex/fontinst/smblmtx/textcomp.mtx
%{_texmfdistdir}/tex/fontinst/smblmtx/unsetnum.mtx
%{_texmfdistdir}/tex/latex/fontinst/fontdoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontinst-%{texlive_version}.%{texlive_noarch}.1.933svn53562-%{release}-zypper
%endif

%package -n texlive-fontmfizz
Version:        %{texlive_version}.%{texlive_noarch}.svn43546
Release:        0
Summary:        Font Mfizz icons for use in LaTeX
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
Requires:       texlive-fontmfizz-fonts >= %{texlive_version}
Recommends:     texlive-fontmfizz-doc >= %{texlive_version}
Provides:       tex(fontmfizz.sty)
Requires:       tex(fontspec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source55:       fontmfizz.tar.xz
Source56:       fontmfizz.doc.tar.xz

%description -n texlive-fontmfizz
The MFizz font provides scalable vector icons representing
programming languages, operating systems, software engineering,
and technology. It can be seen as an extension to FontAwesome.
This package requires the fontspec package and either the
Xe(La)TeX or Lua(La)TeX engine to load the included ttf font.

%package -n texlive-fontmfizz-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn43546
Release:        0
Summary:        Documentation for texlive-fontmfizz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontmfizz-doc
This package includes the documentation for texlive-fontmfizz


%package -n texlive-fontmfizz-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn43546
Release:        0
Summary:        Severed fonts for texlive-fontmfizz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fontmfizz-fonts
The  separated fonts package for texlive-fontmfizz
%post -n texlive-fontmfizz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontmfizz 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontmfizz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fontmfizz-fonts
%files -n texlive-fontmfizz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fontmfizz/LICENSE
%{_texmfdistdir}/doc/fonts/fontmfizz/README
%{_texmfdistdir}/doc/fonts/fontmfizz/fontmfizz.pdf
%{_texmfdistdir}/doc/fonts/fontmfizz/fontmfizz.tex

%files -n texlive-fontmfizz
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fontmfizz/font-mfizz.ttf
%{_texmfdistdir}/tex/latex/fontmfizz/fontmfizz.sty

%files -n texlive-fontmfizz-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fontmfizz
%{_datadir}/fontconfig/conf.avail/58-texlive-fontmfizz.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontmfizz/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontmfizz/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fontmfizz/fonts.scale
%{_datadir}/fonts/texlive-fontmfizz/font-mfizz.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontmfizz-fonts-%{texlive_version}.%{texlive_noarch}.svn43546-%{release}-zypper
%endif

%package -n texlive-fontname
Version:        %{texlive_version}.%{texlive_noarch}.svn53228
Release:        0
Summary:        Scheme for naming fonts in TeX
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
Recommends:     texlive-fontname-doc >= %{texlive_version}
Provides:       tex(adobe.map)
Provides:       tex(apple.map)
Provides:       tex(bitstrea.map)
Provides:       tex(dtc.map)
Provides:       tex(itc.map)
Provides:       tex(linot-cd.map)
Provides:       tex(linotype-cd.map)
Provides:       tex(linotype.map)
Provides:       tex(monotype.map)
Provides:       tex(skey1250.map)
Provides:       tex(skey1555.map)
Provides:       tex(softkey-1250.map)
Provides:       tex(softkey-1555.map)
Provides:       tex(softkey.map)
Provides:       tex(special.map)
Provides:       tex(supplier.map)
Provides:       tex(texfonts.map)
Provides:       tex(typeface.map)
Provides:       tex(urw.map)
Provides:       tex(variant.map)
Provides:       tex(weight.map)
Provides:       tex(width.map)
Provides:       tex(yandy.map)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source57:       fontname.tar.xz
Source58:       fontname.doc.tar.xz

%description -n texlive-fontname
The scheme for assigning names is described (in the
documentation part of the package), and map files giving the
relation between foundry name and 'TeX-name' are also provided.

%package -n texlive-fontname-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn53228
Release:        0
Summary:        Documentation for texlive-fontname
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(preun): %install_info_prereq
Requires(post): %install_info_prereq

%description -n texlive-fontname-doc
This package includes the documentation for texlive-fontname

%post -n texlive-fontname
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontname 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontname
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%preun -n texlive-fontname-doc
if test $1 = 0; then
    %install_info_delete --info-dir=%{_infodir} %{_infodir}/fontname.info
fi

%post -n texlive-fontname-doc
%install_info --info-dir=%{_infodir} %{_infodir}/fontname.info
%files -n texlive-fontname-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fontname/8a.html
%{_texmfdistdir}/doc/fonts/fontname/8r.html
%{_texmfdistdir}/doc/fonts/fontname/Adobe-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Apple-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Bitstream-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/ChangeLog
%{_texmfdistdir}/doc/fonts/fontname/DTC-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Encodings.html
%{_texmfdistdir}/doc/fonts/fontname/Filenames-for-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Font-legalities.html
%{_texmfdistdir}/doc/fonts/fontname/Font-name-lists.html
%{_texmfdistdir}/doc/fonts/fontname/History.html
%{_texmfdistdir}/doc/fonts/fontname/ITC-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Introduction.html
%{_texmfdistdir}/doc/fonts/fontname/Linotype-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Long-names.html
%{_texmfdistdir}/doc/fonts/fontname/Long-naming-scheme.html
%{_texmfdistdir}/doc/fonts/fontname/Makefile
%{_texmfdistdir}/doc/fonts/fontname/Monotype-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Name-mapping-file.html
%{_texmfdistdir}/doc/fonts/fontname/References.html
%{_texmfdistdir}/doc/fonts/fontname/Standard-PostScript-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Suppliers.html
%{_texmfdistdir}/doc/fonts/fontname/Typefaces.html
%{_texmfdistdir}/doc/fonts/fontname/URW-fonts.html
%{_texmfdistdir}/doc/fonts/fontname/Variants.html
%{_texmfdistdir}/doc/fonts/fontname/Weights.html
%{_texmfdistdir}/doc/fonts/fontname/Widths.html
%{_texmfdistdir}/doc/fonts/fontname/bitstrea.aka
%{_texmfdistdir}/doc/fonts/fontname/cork.html
%{_texmfdistdir}/doc/fonts/fontname/dvips.html
%{_texmfdistdir}/doc/fonts/fontname/fontname.aux
%{_texmfdistdir}/doc/fonts/fontname/fontname.cp
%{_texmfdistdir}/doc/fonts/fontname/fontname.html
%{_texmfdistdir}/doc/fonts/fontname/fontname.pdf
%{_texmfdistdir}/doc/fonts/fontname/fontname.texi
%{_texmfdistdir}/doc/fonts/fontname/fontname.toc
%{_texmfdistdir}/doc/fonts/fontname/index.html
%{_texmfdistdir}/doc/fonts/fontname/texmext.html
%{_texmfdistdir}/doc/fonts/fontname/texmital.html
%{_texmfdistdir}/doc/fonts/fontname/texmsym.html
%{_texmfdistdir}/doc/fonts/fontname/texnansi.html
%{_texmfdistdir}/doc/fonts/fontname/texnansx.html
%{_texmfdistdir}/doc/fonts/fontname/xl2.html
%{_texmfdistdir}/doc/fonts/fontname/xt2.html
%{_infodir}/fontname.info*

%files -n texlive-fontname
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/fontname/adobe.map
%{_texmfdistdir}/fonts/map/fontname/apple.map
%{_texmfdistdir}/fonts/map/fontname/bitstrea.map
%{_texmfdistdir}/fonts/map/fontname/dtc.map
%{_texmfdistdir}/fonts/map/fontname/itc.map
%{_texmfdistdir}/fonts/map/fontname/linot-cd.map
%{_texmfdistdir}/fonts/map/fontname/linotype-cd.map
%{_texmfdistdir}/fonts/map/fontname/linotype.map
%{_texmfdistdir}/fonts/map/fontname/monotype.map
%{_texmfdistdir}/fonts/map/fontname/skey1250.map
%{_texmfdistdir}/fonts/map/fontname/skey1555.map
%{_texmfdistdir}/fonts/map/fontname/softkey-1250.map
%{_texmfdistdir}/fonts/map/fontname/softkey-1555.map
%{_texmfdistdir}/fonts/map/fontname/softkey.map
%{_texmfdistdir}/fonts/map/fontname/special.map
%{_texmfdistdir}/fonts/map/fontname/supplier.map
%{_texmfdistdir}/fonts/map/fontname/texfonts.map
%{_texmfdistdir}/fonts/map/fontname/typeface.map
%{_texmfdistdir}/fonts/map/fontname/urw.map
%{_texmfdistdir}/fonts/map/fontname/variant.map
%{_texmfdistdir}/fonts/map/fontname/weight.map
%{_texmfdistdir}/fonts/map/fontname/width.map
%{_texmfdistdir}/fonts/map/fontname/yandy.map
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontname-%{texlive_version}.%{texlive_noarch}.svn53228-%{release}-zypper
%endif

%package -n texlive-fontools
Version:        %{texlive_version}.%{texlive_noarch}.svn53593
Release:        0
Summary:        Tools to simplify using fonts (especially TT/OTF ones)
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-fontools-bin >= %{texlive_version}
#!BuildIgnore: texlive-fontools-bin
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
Recommends:     texlive-fontools-doc >= %{texlive_version}
Requires:       perl(Cwd)
#!BuildIgnore:  perl(Cwd)
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Path)
#!BuildIgnore:  perl(File::Path)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(List::Util)
#!BuildIgnore:  perl(List::Util)
Requires:       perl(POSIX)
#!BuildIgnore:  perl(POSIX)
Requires:       perl(Pod::Usage)
#!BuildIgnore:  perl(Pod::Usage)
Requires:       perl(integer)
#!BuildIgnore:  perl(integer)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
Provides:       tex(fontools_lgr.enc)
Provides:       tex(fontools_ly1.enc)
Provides:       tex(fontools_ot1.enc)
Provides:       tex(fontools_t1.enc)
Provides:       tex(fontools_t2a.enc)
Provides:       tex(fontools_t2b.enc)
Provides:       tex(fontools_t2c.enc)
Provides:       tex(fontools_t3.enc)
Provides:       tex(fontools_ts1.enc)
Provides:       tex(fontools_ts3.enc)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source59:       fontools.tar.xz
Source60:       fontools.doc.tar.xz

%description -n texlive-fontools
This package provides tools to simplify using OpenType fonts
with LaTeX. By far the most important program in this bundle is
autoinst: autoinst - a wrapper script around Eddie Kohler's
LCDF TypeTools. Autoinst aims to automate the installation of
OpenType fonts in LaTeX by calling the LCDF TypeTools (with the
correct options) for all fonts you wish to install, and
generating the necessary .fd and .sty files. In addition, this
bundle contains a few other, less important utilities: afm2afm
- re-encode .afm files, ot2kpx - extract kerning pairs from
OpenType fonts, splitttc - split an OpenType Collection file
(ttc or otc) into individual fonts.

%package -n texlive-fontools-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn53593
Release:        0
Summary:        Documentation for texlive-fontools
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(afm2afm.1)
Provides:       man(autoinst.1)
Provides:       man(ot2kpx.1)

%description -n texlive-fontools-doc
This package includes the documentation for texlive-fontools

%post -n texlive-fontools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontools-doc
%defattr(-,root,root,755)
%{_mandir}/man1/afm2afm.1*
%{_mandir}/man1/autoinst.1*
%{_mandir}/man1/ot2kpx.1*
%{_texmfdistdir}/doc/support/fontools/GPLv2.txt
%{_texmfdistdir}/doc/support/fontools/README
%{_texmfdistdir}/doc/support/fontools/splitttc

%files -n texlive-fontools
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ly1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_t3.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ts3.enc
%{_texmfdistdir}/scripts/fontools/afm2afm
%{_texmfdistdir}/scripts/fontools/autoinst
%{_texmfdistdir}/scripts/fontools/ot2kpx
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontools-%{texlive_version}.%{texlive_noarch}.svn53593-%{release}-zypper
%endif

%package -n texlive-fonts-churchslavonic
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn43121
Release:        0
Summary:        Fonts for typesetting in Church Slavonic language
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-fonts-churchslavonic-fonts >= %{texlive_version}
Recommends:     texlive-fonts-churchslavonic-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source61:       fonts-churchslavonic.tar.xz
Source62:       fonts-churchslavonic.doc.tar.xz

%description -n texlive-fonts-churchslavonic
The package provides Unicode-encoded OpenType fonts for Church
Slavonic.

%package -n texlive-fonts-churchslavonic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn43121
Release:        0
Summary:        Documentation for texlive-fonts-churchslavonic
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fonts-churchslavonic-doc
This package includes the documentation for texlive-fonts-churchslavonic


%package -n texlive-fonts-churchslavonic-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn43121
Release:        0
Summary:        Severed fonts for texlive-fonts-churchslavonic
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fonts-churchslavonic-fonts
The  separated fonts package for texlive-fonts-churchslavonic
%post -n texlive-fonts-churchslavonic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fonts-churchslavonic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fonts-churchslavonic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fonts-churchslavonic-fonts
%files -n texlive-fonts-churchslavonic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/GPL.txt
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/LICENSE
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/OFL.txt
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/README
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/fonts-churchslavonic.pdf
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/fonts-churchslavonic.tex
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/opentype.png
%{_texmfdistdir}/doc/fonts/fonts-churchslavonic/truetype.png

%files -n texlive-fonts-churchslavonic
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic/FedorovskUnicode.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic/IndictionUnicode.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic/MenaionUnicode.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic/MonomakhUnicode.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic/PomorskyUnicode.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic/PonomarUnicode.otf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonts-churchslavonic/FedorovskUnicode.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonts-churchslavonic/IndictionUnicode.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonts-churchslavonic/MenaionUnicode.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonts-churchslavonic/MonomakhUnicode.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonts-churchslavonic/PomorskyUnicode.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/fonts-churchslavonic/PonomarUnicode.ttf

%files -n texlive-fonts-churchslavonic-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fonts-churchslavonic
%{_datadir}/fontconfig/conf.avail/58-texlive-fonts-churchslavonic.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonts-churchslavonic/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonts-churchslavonic/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonts-churchslavonic/fonts.scale
%{_datadir}/fonts/texlive-fonts-churchslavonic/FedorovskUnicode.otf
%{_datadir}/fonts/texlive-fonts-churchslavonic/IndictionUnicode.otf
%{_datadir}/fonts/texlive-fonts-churchslavonic/MenaionUnicode.otf
%{_datadir}/fonts/texlive-fonts-churchslavonic/MonomakhUnicode.otf
%{_datadir}/fonts/texlive-fonts-churchslavonic/PomorskyUnicode.otf
%{_datadir}/fonts/texlive-fonts-churchslavonic/PonomarUnicode.otf
%{_datadir}/fonts/texlive-fonts-churchslavonic/FedorovskUnicode.ttf
%{_datadir}/fonts/texlive-fonts-churchslavonic/IndictionUnicode.ttf
%{_datadir}/fonts/texlive-fonts-churchslavonic/MenaionUnicode.ttf
%{_datadir}/fonts/texlive-fonts-churchslavonic/MonomakhUnicode.ttf
%{_datadir}/fonts/texlive-fonts-churchslavonic/PomorskyUnicode.ttf
%{_datadir}/fonts/texlive-fonts-churchslavonic/PonomarUnicode.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fonts-churchslavonic-fonts-%{texlive_version}.%{texlive_noarch}.1.1svn43121-%{release}-zypper
%endif

%package -n texlive-fonts-tlwg
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.1svn54512
Release:        0
Summary:        Thai fonts for LaTeX from TLWG
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
Requires:       texlive-fonts-tlwg-fonts >= %{texlive_version}
Recommends:     texlive-fonts-tlwg-doc >= %{texlive_version}
Provides:       tex(fonts-tlwg.sty)
Provides:       tex(garuda.tfm)
Provides:       tex(garuda.vf)
Provides:       tex(garuda_b.tfm)
Provides:       tex(garuda_b.vf)
Provides:       tex(garuda_bo.tfm)
Provides:       tex(garuda_bo.vf)
Provides:       tex(garuda_o.tfm)
Provides:       tex(garuda_o.vf)
Provides:       tex(kinnari.tfm)
Provides:       tex(kinnari.vf)
Provides:       tex(kinnari_b.tfm)
Provides:       tex(kinnari_b.vf)
Provides:       tex(kinnari_bi.tfm)
Provides:       tex(kinnari_bi.vf)
Provides:       tex(kinnari_bo.tfm)
Provides:       tex(kinnari_bo.vf)
Provides:       tex(kinnari_i.tfm)
Provides:       tex(kinnari_i.vf)
Provides:       tex(kinnari_o.tfm)
Provides:       tex(kinnari_o.vf)
Provides:       tex(laksaman.tfm)
Provides:       tex(laksaman.vf)
Provides:       tex(laksaman_b.tfm)
Provides:       tex(laksaman_b.vf)
Provides:       tex(laksaman_bi.tfm)
Provides:       tex(laksaman_bi.vf)
Provides:       tex(laksaman_i.tfm)
Provides:       tex(laksaman_i.vf)
Provides:       tex(loma.tfm)
Provides:       tex(loma.vf)
Provides:       tex(loma_b.tfm)
Provides:       tex(loma_b.vf)
Provides:       tex(loma_bo.tfm)
Provides:       tex(loma_bo.vf)
Provides:       tex(loma_o.tfm)
Provides:       tex(loma_o.vf)
Provides:       tex(lthgaruda.fd)
Provides:       tex(lthkinnari.fd)
Provides:       tex(lthlaksaman.fd)
Provides:       tex(lthloma.fd)
Provides:       tex(lthnorasi.fd)
Provides:       tex(lthpurisa.fd)
Provides:       tex(lthsawasdee.fd)
Provides:       tex(lthtlwg.enc)
Provides:       tex(lthttype.fd)
Provides:       tex(lthttypist.fd)
Provides:       tex(lthumpush.fd)
Provides:       tex(lthwaree.fd)
Provides:       tex(nectec.map)
Provides:       tex(nf.map)
Provides:       tex(norasi.tfm)
Provides:       tex(norasi.vf)
Provides:       tex(norasi_b.tfm)
Provides:       tex(norasi_b.vf)
Provides:       tex(norasi_bi.tfm)
Provides:       tex(norasi_bi.vf)
Provides:       tex(norasi_bo.tfm)
Provides:       tex(norasi_bo.vf)
Provides:       tex(norasi_i.tfm)
Provides:       tex(norasi_i.vf)
Provides:       tex(norasi_o.tfm)
Provides:       tex(norasi_o.vf)
Provides:       tex(purisa.tfm)
Provides:       tex(purisa.vf)
Provides:       tex(purisa_b.tfm)
Provides:       tex(purisa_b.vf)
Provides:       tex(purisa_bo.tfm)
Provides:       tex(purisa_bo.vf)
Provides:       tex(purisa_o.tfm)
Provides:       tex(purisa_o.vf)
Provides:       tex(rgaruda.tfm)
Provides:       tex(rgaruda_b.tfm)
Provides:       tex(rgaruda_bo.tfm)
Provides:       tex(rgaruda_o.tfm)
Provides:       tex(rkinnari.tfm)
Provides:       tex(rkinnari_b.tfm)
Provides:       tex(rkinnari_bi.tfm)
Provides:       tex(rkinnari_bo.tfm)
Provides:       tex(rkinnari_i.tfm)
Provides:       tex(rkinnari_o.tfm)
Provides:       tex(rlaksaman.tfm)
Provides:       tex(rlaksaman_b.tfm)
Provides:       tex(rlaksaman_bi.tfm)
Provides:       tex(rlaksaman_i.tfm)
Provides:       tex(rloma.tfm)
Provides:       tex(rloma_b.tfm)
Provides:       tex(rloma_bo.tfm)
Provides:       tex(rloma_o.tfm)
Provides:       tex(rnorasi.tfm)
Provides:       tex(rnorasi_b.tfm)
Provides:       tex(rnorasi_bi.tfm)
Provides:       tex(rnorasi_bo.tfm)
Provides:       tex(rnorasi_i.tfm)
Provides:       tex(rnorasi_o.tfm)
Provides:       tex(rpurisa.tfm)
Provides:       tex(rpurisa_b.tfm)
Provides:       tex(rpurisa_bo.tfm)
Provides:       tex(rpurisa_o.tfm)
Provides:       tex(rsawasdee.tfm)
Provides:       tex(rsawasdee_b.tfm)
Provides:       tex(rsawasdee_bo.tfm)
Provides:       tex(rsawasdee_o.tfm)
Provides:       tex(rttype.tfm)
Provides:       tex(rttype_b.tfm)
Provides:       tex(rttype_bo.tfm)
Provides:       tex(rttype_o.tfm)
Provides:       tex(rttypist.tfm)
Provides:       tex(rttypist_b.tfm)
Provides:       tex(rttypist_bo.tfm)
Provides:       tex(rttypist_o.tfm)
Provides:       tex(rumpush.tfm)
Provides:       tex(rumpush_b.tfm)
Provides:       tex(rumpush_bo.tfm)
Provides:       tex(rumpush_l.tfm)
Provides:       tex(rumpush_lo.tfm)
Provides:       tex(rumpush_o.tfm)
Provides:       tex(rwaree.tfm)
Provides:       tex(rwaree_b.tfm)
Provides:       tex(rwaree_bo.tfm)
Provides:       tex(rwaree_o.tfm)
Provides:       tex(sawasdee.tfm)
Provides:       tex(sawasdee.vf)
Provides:       tex(sawasdee_b.tfm)
Provides:       tex(sawasdee_b.vf)
Provides:       tex(sawasdee_bo.tfm)
Provides:       tex(sawasdee_bo.vf)
Provides:       tex(sawasdee_o.tfm)
Provides:       tex(sawasdee_o.vf)
Provides:       tex(sipa.map)
Provides:       tex(tlwg.map)
Provides:       tex(ttype.tfm)
Provides:       tex(ttype.vf)
Provides:       tex(ttype_b.tfm)
Provides:       tex(ttype_b.vf)
Provides:       tex(ttype_bo.tfm)
Provides:       tex(ttype_bo.vf)
Provides:       tex(ttype_o.tfm)
Provides:       tex(ttype_o.vf)
Provides:       tex(ttypist.tfm)
Provides:       tex(ttypist.vf)
Provides:       tex(ttypist_b.tfm)
Provides:       tex(ttypist_b.vf)
Provides:       tex(ttypist_bo.tfm)
Provides:       tex(ttypist_bo.vf)
Provides:       tex(ttypist_o.tfm)
Provides:       tex(ttypist_o.vf)
Provides:       tex(umpush.tfm)
Provides:       tex(umpush.vf)
Provides:       tex(umpush_b.tfm)
Provides:       tex(umpush_b.vf)
Provides:       tex(umpush_bo.tfm)
Provides:       tex(umpush_bo.vf)
Provides:       tex(umpush_l.tfm)
Provides:       tex(umpush_l.vf)
Provides:       tex(umpush_lo.tfm)
Provides:       tex(umpush_lo.vf)
Provides:       tex(umpush_o.tfm)
Provides:       tex(umpush_o.vf)
Provides:       tex(waree.tfm)
Provides:       tex(waree.vf)
Provides:       tex(waree_b.tfm)
Provides:       tex(waree_b.vf)
Provides:       tex(waree_bo.tfm)
Provides:       tex(waree_bo.vf)
Provides:       tex(waree_o.tfm)
Provides:       tex(waree_o.vf)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source63:       fonts-tlwg.tar.xz
Source64:       fonts-tlwg.doc.tar.xz

%description -n texlive-fonts-tlwg
A collection of free Thai fonts, supplied as FontForge sources,
and with LaTeX .fd files. This package depends on the thailatex
package.

%package -n texlive-fonts-tlwg-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.1svn54512
Release:        0
Summary:        Documentation for texlive-fonts-tlwg
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fonts-tlwg-doc
This package includes the documentation for texlive-fonts-tlwg


%package -n texlive-fonts-tlwg-fonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.1svn54512
Release:        0
Summary:        Severed fonts for texlive-fonts-tlwg
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fonts-tlwg-fonts
The  separated fonts package for texlive-fonts-tlwg
%post -n texlive-fonts-tlwg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap nectec.map' >> /var/run/texlive/run-updmap
echo 'addMap nf.map' >> /var/run/texlive/run-updmap
echo 'addMap sipa.map' >> /var/run/texlive/run-updmap
echo 'addMap tlwg.map' >> /var/run/texlive/run-updmap

%postun -n texlive-fonts-tlwg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap nectec.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap nf.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap sipa.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap tlwg.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-fonts-tlwg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fonts-tlwg-fonts
%files -n texlive-fonts-tlwg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fonts-tlwg/README.latex
%{_texmfdistdir}/doc/fonts/fonts-tlwg/examples/testsans.tex
%{_texmfdistdir}/doc/fonts/fonts-tlwg/examples/testscaled-120.tex
%{_texmfdistdir}/doc/fonts/fonts-tlwg/examples/testscaled-65.tex
%{_texmfdistdir}/doc/fonts/fonts-tlwg/examples/teststd.tex

%files -n texlive-fonts-tlwg
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/garuda_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_bi.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_i.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/kinnari_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/laksaman.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/laksaman_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/laksaman_bi.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/laksaman_i.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/loma_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_bi.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_i.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/norasi_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/purisa_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/sawasdee_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttype_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/ttypist_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_l.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_lo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/umpush_o.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree_b.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree_bo.afm
%{_texmfdistdir}/fonts/afm/public/fonts-tlwg/waree_o.afm
%{_texmfdistdir}/fonts/enc/dvips/fonts-tlwg/lthtlwg.enc
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg/nectec.map
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg/nf.map
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg/sipa.map
%{_texmfdistdir}/fonts/map/dvips/fonts-tlwg/tlwg.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Garuda-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Garuda-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Garuda-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Garuda.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Kinnari-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Kinnari-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Kinnari-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Kinnari-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Kinnari-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Kinnari.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Laksaman-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Laksaman-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Laksaman-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Laksaman.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Loma-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Loma-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Loma-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Loma.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Norasi-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Norasi-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Norasi-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Norasi-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Norasi-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Norasi.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Purisa-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Purisa-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Purisa-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Purisa.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Sawasdee-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Sawasdee-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Sawasdee-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Sawasdee.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgMono-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgMono-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgMono-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgMono.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypewriter-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypewriter-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypewriter-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypewriter.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypist-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypist-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypist-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypist.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypo-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypo-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypo-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/TlwgTypo.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Umpush-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Umpush-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Umpush-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Umpush-LightOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Umpush-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Umpush.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Waree-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Waree-BoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Waree-Oblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/Waree.otf
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/garuda_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/kinnari_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/laksaman.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/laksaman_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/laksaman_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/laksaman_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/loma_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/norasi_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/purisa_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rgaruda_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rkinnari_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rlaksaman.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rlaksaman_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rlaksaman_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rlaksaman_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rloma_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_bi.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_i.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rnorasi_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rpurisa_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rsawasdee_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttype_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rttypist_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_l.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_lo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rumpush_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/rwaree_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/sawasdee_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttype_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/ttypist_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_l.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_lo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/umpush_o.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree_b.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree_bo.tfm
%{_texmfdistdir}/fonts/tfm/public/fonts-tlwg/waree_o.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/garuda_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_bi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_i.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/kinnari_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/laksaman.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/laksaman_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/laksaman_bi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/laksaman_i.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/loma_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_bi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_i.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/norasi_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/purisa_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/sawasdee_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttype_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/ttypist_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_l.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_lo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/umpush_o.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree_b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree_bo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fonts-tlwg/waree_o.pfb
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/garuda_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_bi.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_i.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/kinnari_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/laksaman.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/laksaman_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/laksaman_bi.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/laksaman_i.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/loma_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_bi.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_i.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/norasi_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/purisa_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/sawasdee_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttype_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/ttypist_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_l.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_lo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/umpush_o.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree_b.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree_bo.vf
%{_texmfdistdir}/fonts/vf/public/fonts-tlwg/waree_o.vf
%{_texmfdistdir}/tex/latex/fonts-tlwg/fonts-tlwg.sty
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthgaruda.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthkinnari.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthlaksaman.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthloma.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthnorasi.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthpurisa.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthsawasdee.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthttype.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthttypist.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthumpush.fd
%{_texmfdistdir}/tex/latex/fonts-tlwg/lthwaree.fd

%files -n texlive-fonts-tlwg-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fonts-tlwg
%{_datadir}/fontconfig/conf.avail/58-texlive-fonts-tlwg.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-fonts-tlwg.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-fonts-tlwg.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonts-tlwg/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonts-tlwg/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fonts-tlwg/fonts.scale
%{_datadir}/fonts/texlive-fonts-tlwg/Garuda-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Garuda-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Garuda-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Garuda.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Kinnari-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Kinnari-BoldItalic.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Kinnari-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Kinnari-Italic.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Kinnari-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Kinnari.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Laksaman-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Laksaman-BoldItalic.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Laksaman-Italic.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Laksaman.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Loma-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Loma-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Loma-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Loma.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Norasi-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Norasi-BoldItalic.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Norasi-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Norasi-Italic.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Norasi-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Norasi.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Purisa-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Purisa-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Purisa-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Purisa.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Sawasdee-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Sawasdee-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Sawasdee-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Sawasdee.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgMono-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgMono-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgMono-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgMono.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypewriter-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypewriter-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypewriter-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypewriter.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypist-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypist-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypist-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypist.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypo-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypo-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypo-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/TlwgTypo.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Umpush-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Umpush-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Umpush-Light.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Umpush-LightOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Umpush-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Umpush.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Waree-Bold.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Waree-BoldOblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Waree-Oblique.otf
%{_datadir}/fonts/texlive-fonts-tlwg/Waree.otf
%{_datadir}/fonts/texlive-fonts-tlwg/garuda.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/garuda_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/garuda_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/garuda_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/kinnari.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/kinnari_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/kinnari_bi.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/kinnari_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/kinnari_i.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/kinnari_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/laksaman.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/laksaman_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/laksaman_bi.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/laksaman_i.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/loma.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/loma_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/loma_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/loma_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/norasi.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/norasi_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/norasi_bi.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/norasi_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/norasi_i.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/norasi_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/purisa.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/purisa_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/purisa_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/purisa_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/sawasdee.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/sawasdee_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/sawasdee_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/sawasdee_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttype.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttype_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttype_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttype_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttypist.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttypist_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttypist_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/ttypist_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/umpush.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/umpush_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/umpush_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/umpush_l.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/umpush_lo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/umpush_o.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/waree.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/waree_b.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/waree_bo.pfb
%{_datadir}/fonts/texlive-fonts-tlwg/waree_o.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fonts-tlwg-fonts-%{texlive_version}.%{texlive_noarch}.0.0.7.1svn54512-%{release}-zypper
%endif

%package -n texlive-fontsetup
Version:        %{texlive_version}.%{texlive_noarch}.1.002svn53195
Release:        0
Summary:        A front-end to fontspec, for selected fonts with math support
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
Recommends:     texlive-fontsetup-doc >= %{texlive_version}
Provides:       tex(fontsetup.sty)
Provides:       tex(fspdefaultfontsot.sty)
Provides:       tex(fspebgaramondot.sty)
Provides:       tex(fspfiraot.sty)
Provides:       tex(fspgfsartemisiaot.sty)
Provides:       tex(fspgfsdidotclassicot.sty)
Provides:       tex(fspgfsdidotot.sty)
Provides:       tex(fspgfsneohellenicot.sty)
Provides:       tex(fspkerkisot.sty)
Provides:       tex(fspneoeulerot.sty)
Provides:       tex(fsppalatinoot.sty)
Provides:       tex(fspstixtwoot.sty)
Provides:       tex(fsptimesot.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(libertinus-otf.sty)
Requires:       tex(ucharclasses.sty)
Requires:       tex(unicode-math.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source65:       fontsetup.tar.xz
Source66:       fontsetup.doc.tar.xz

%description -n texlive-fontsetup
This package facilitates the use of fontspec for users who do
not wish to bother with details, with a special focus on
quality fonts supporting Mathematics.

%package -n texlive-fontsetup-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.002svn53195
Release:        0
Summary:        Documentation for texlive-fontsetup
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontsetup-doc
This package includes the documentation for texlive-fontsetup

%post -n texlive-fontsetup
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontsetup 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontsetup
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontsetup-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fontsetup/README
%{_texmfdistdir}/doc/latex/fontsetup/README.TEXLIVE
%{_texmfdistdir}/doc/latex/fontsetup/fontsetup-doc.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fontsetup-doc.tex
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-cmr.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-ebgaramond.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-fira.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-gfsartemisia.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-gfsdidot.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-gfsdidotclassic.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-gfsneohellenic.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-kerkis.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-libertinus.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-neoeuler.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-palatino.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-stixtwo.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample-times.pdf
%{_texmfdistdir}/doc/latex/fontsetup/fspsample.tex
%{_texmfdistdir}/doc/latex/fontsetup/system-install-fonts/fsplpscel.otf
%{_texmfdistdir}/doc/latex/fontsetup/system-install-fonts/fspmnscel.otf

%files -n texlive-fontsetup
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fontsetup/fontsetup.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspdefaultfontsot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspebgaramondot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspfiraot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspgfsartemisiaot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspgfsdidotclassicot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspgfsdidotot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspgfsneohellenicot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspkerkisot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspneoeulerot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fsppalatinoot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fspstixtwoot.sty
%{_texmfdistdir}/tex/latex/fontsetup/fsptimesot.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontsetup-%{texlive_version}.%{texlive_noarch}.1.002svn53195-%{release}-zypper
%endif

%package -n texlive-fontsize
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn53874
Release:        0
Summary:        A small package to set arbitrary sizes for the main font of the document
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
Recommends:     texlive-fontsize-doc >= %{texlive_version}
Provides:       tex(fontsize.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source67:       fontsize.tar.xz
Source68:       fontsize.doc.tar.xz

%description -n texlive-fontsize
The package allows you to set arbitrary sizes for the main font
of the document, through the fontsize=<size> option.

%package -n texlive-fontsize-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn53874
Release:        0
Summary:        Documentation for texlive-fontsize
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontsize-doc
This package includes the documentation for texlive-fontsize

%post -n texlive-fontsize
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontsize 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontsize
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontsize-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fontsize/README
%{_texmfdistdir}/doc/latex/fontsize/fontsize.pdf

%files -n texlive-fontsize
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fontsize/fontsize.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontsize-%{texlive_version}.%{texlive_noarch}.0.0.1svn53874-%{release}-zypper
%endif

%package -n texlive-fontspec
Version:        %{texlive_version}.%{texlive_noarch}.2.7isvn53860
Release:        0
Summary:        Advanced font selection in XeLaTeX and LuaLaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-euenc >= %{texlive_version}
#!BuildIgnore: texlive-euenc
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires:       texlive-l3kernel >= %{texlive_version}
#!BuildIgnore: texlive-l3kernel
Requires:       texlive-l3packages >= %{texlive_version}
#!BuildIgnore: texlive-l3packages
Requires:       texlive-lm >= %{texlive_version}
#!BuildIgnore: texlive-lm
Requires:       texlive-xunicode >= %{texlive_version}
#!BuildIgnore: texlive-xunicode
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
Recommends:     texlive-fontspec-doc >= %{texlive_version}
Provides:       tex(fontspec-luatex.sty)
Provides:       tex(fontspec-xetex.sty)
Provides:       tex(fontspec.cfg)
Provides:       tex(fontspec.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source69:       fontspec.tar.xz
Source70:       fontspec.doc.tar.xz

%description -n texlive-fontspec
Fontspec is a package for XeLaTeX and LuaLaTeX. It provides an
automatic and unified interface to feature-rich AAT and
OpenType fonts through the NFSS in LaTeX running on XeTeX or
LuaTeX engines. The package requires the l3kernel and xparse
bundles from the LaTeX3 development team.

%package -n texlive-fontspec-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.7isvn53860
Release:        0
Summary:        Documentation for texlive-fontspec
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontspec-doc
This package includes the documentation for texlive-fontspec

%post -n texlive-fontspec
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontspec 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontspec
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontspec-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fontspec/CHANGES.md
%{_texmfdistdir}/doc/latex/fontspec/LICENSE
%{_texmfdistdir}/doc/latex/fontspec/README.md
%{_texmfdistdir}/doc/latex/fontspec/fontspec-code.pdf
%{_texmfdistdir}/doc/latex/fontspec/fontspec-example.tex
%{_texmfdistdir}/doc/latex/fontspec/fontspec.pdf

%files -n texlive-fontspec
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fontspec/fontspec-luatex.sty
%{_texmfdistdir}/tex/latex/fontspec/fontspec-xetex.sty
%{_texmfdistdir}/tex/latex/fontspec/fontspec.cfg
%{_texmfdistdir}/tex/latex/fontspec/fontspec.lua
%{_texmfdistdir}/tex/latex/fontspec/fontspec.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontspec-%{texlive_version}.%{texlive_noarch}.2.7isvn53860-%{release}-zypper
%endif

%package -n texlive-fonttable
Version:        %{texlive_version}.%{texlive_noarch}.1.6csvn44799
Release:        0
Summary:        Print font tables from a LaTeX document
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
Recommends:     texlive-fonttable-doc >= %{texlive_version}
Provides:       tex(fonttable.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source71:       fonttable.tar.xz
Source72:       fonttable.doc.tar.xz

%description -n texlive-fonttable
This is a package version of nfssfont.tex (part of the LaTeX
distribution); it enables you to print a table of the
characters of a font and/or some text (for demonstration or
testing purposes), from within a document. (Packages such as
testfont and nfssfont.tex provide these facilities, but they
run as interactive programs: the user is expected to type
details of what is needed.) Note that the package mftinc also
has a \fonttable function; the documentation explains how avoid
a clash with that package.

%package -n texlive-fonttable-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6csvn44799
Release:        0
Summary:        Documentation for texlive-fonttable
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fonttable-doc
This package includes the documentation for texlive-fonttable

%post -n texlive-fonttable
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fonttable 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fonttable
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fonttable-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fonttable/README
%{_texmfdistdir}/doc/latex/fonttable/fonttable.pdf

%files -n texlive-fonttable
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fonttable/fonttable.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fonttable-%{texlive_version}.%{texlive_noarch}.1.6csvn44799-%{release}-zypper
%endif

%package -n texlive-fontware
Version:        %{texlive_version}.%{texlive_noarch}.svn54070
Release:        0
Summary:        Tools for virtual font metrics
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-fontware-bin >= %{texlive_version}
#!BuildIgnore: texlive-fontware-bin
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
Provides:       man(pltotf.1)
Provides:       man(tftopl.1)
Provides:       man(vftovp.1)
Provides:       man(vptovf.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source73:       fontware.doc.tar.xz

%description -n texlive-fontware
Virtual font metrics are usually created in a textual form, the
Virtual Property List, but programs that use them need to use
binary files (the Virtual Font and the TeX Font Metric). The
present two programs translate between the two forms: - vptovf
takes a VPL file and generates a VF file and a TFM file; -
vftovp takes a VF file and a TFM file and generates a VPL file.
The programs are to be found in every distribution of TeX.
%post -n texlive-fontware
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontware 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontware
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontware
%defattr(-,root,root,755)
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontware-%{texlive_version}.%{texlive_noarch}.svn54070-%{release}-zypper
%endif

%package -n texlive-fontwrap
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Bind fonts to specific unicode blocks
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
Recommends:     texlive-fontwrap-doc >= %{texlive_version}
Provides:       tex(fontwrap.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(perltex.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xunicode.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source74:       fontwrap.tar.xz
Source75:       fontwrap.doc.tar.xz

%description -n texlive-fontwrap
The package (which runs under XeLaTeX) lets you bind fonts to
specific unicode blocks, for automatic font tagging of
multilingual text. The package uses Perl (via perltex) to
construct its tables.

%package -n texlive-fontwrap-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-fontwrap
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fontwrap-doc
This package includes the documentation for texlive-fontwrap

%post -n texlive-fontwrap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fontwrap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fontwrap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fontwrap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/fontwrap/README
%{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap.pdf
%{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap.tex
%{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap_example.pdf
%{_texmfdistdir}/doc/xelatex/fontwrap/fontwrap_example.tex

%files -n texlive-fontwrap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/fontwrap/fontwrap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fontwrap-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-footbib
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn17115
Release:        0
Summary:        Bibliographic references as footnotes
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
Recommends:     texlive-footbib-doc >= %{texlive_version}
Provides:       tex(footbib.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source76:       footbib.tar.xz
Source77:       footbib.doc.tar.xz

%description -n texlive-footbib
The package makes bibliographic references appear as footnotes.
It defines a command \footcite which is similar to the LaTeX
\cite command but the references cited in this way appear at
the bottom of the pages. This 'foot bibliography' does not
conflict with the standard one and both may exist
simultaneously in a document. The command \cite may still be
used to produce the standard bibliography. The foot
bibliography uses its own style and bibliographic database
which may be specified independently of the standard one. Any
standard bibliography style may be used.

%package -n texlive-footbib-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn17115
Release:        0
Summary:        Documentation for texlive-footbib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-footbib-doc
This package includes the documentation for texlive-footbib

%post -n texlive-footbib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-footbib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-footbib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-footbib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/footbib/README
%{_texmfdistdir}/doc/latex/footbib/footbib.pdf

%files -n texlive-footbib
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/footbib/footbib.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-footbib-%{texlive_version}.%{texlive_noarch}.2.0.7svn17115-%{release}-zypper
%endif

%package -n texlive-footmisc
Version:        %{texlive_version}.%{texlive_noarch}.5.5bsvn23330
Release:        0
Summary:        A range of footnote options
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
Recommends:     texlive-footmisc-doc >= %{texlive_version}
Provides:       tex(footmisc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source78:       footmisc.tar.xz
Source79:       footmisc.doc.tar.xz

%description -n texlive-footmisc
A collection of ways to change the typesetting of footnotes.
The package provides means of changing the layout of the
footnotes themselves (including setting them in 'paragraphs' --
the para option), a way to number footnotes per page (the
perpage option), to make footnotes disappear in a 'moving'
argument (stable option) and to deal with multiple references
to footnotes from the same place (multiple option). The package
also has a range of techniques for labelling footnotes with
symbols rather than numbers. Some of the functions of the
package are overlap with the functionality of other packages.
The para option is also provided by the manyfoot and bigfoot
packages, though those are both also portmanteau packages.
(Don't be seduced by fnpara, whose implementation is improved
by the present package.) The perpage option is also offered by
footnpag and by the rather more general-purpose perpage

%package -n texlive-footmisc-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.5bsvn23330
Release:        0
Summary:        Documentation for texlive-footmisc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-footmisc-doc:en)

%description -n texlive-footmisc-doc
This package includes the documentation for texlive-footmisc

%post -n texlive-footmisc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-footmisc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-footmisc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-footmisc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/footmisc/README
%{_texmfdistdir}/doc/latex/footmisc/footmisc.pdf

%files -n texlive-footmisc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/footmisc/footmisc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-footmisc-%{texlive_version}.%{texlive_noarch}.5.5bsvn23330-%{release}-zypper
%endif

%package -n texlive-footmisx
Version:        %{texlive_version}.%{texlive_noarch}.20161201svn42621
Release:        0
Summary:        A range of footnote options
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
Recommends:     texlive-footmisx-doc >= %{texlive_version}
Provides:       tex(footmisx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source80:       footmisx.tar.xz
Source81:       footmisx.doc.tar.xz

%description -n texlive-footmisx
This a fork of footmisc package allowing to use hyperref. Here
is a copy of the description of package footmisc: A collection
of ways to change the typesetting of footnotes. The package
provides means of changing the layout of the footnotes
themselves (including setting them in 'paragraphs' -- the para
option), a way to number footnotes per page (the perpage
option), to make footnotes disappear in a 'moving' argument
(stable option) and to deal with multiple references to
footnotes from the same place (multiple option). The package
also has a range of techniques for labelling footnotes with
symbols rather than numbers. Some of the functions of the
package are overlap with the functionality of other packages.
The para option is also provided by the manyfoot and bigfoot
packages, though those are both also portmanteau packages.
(Don't be seduced by fnpara, whose implementation is improved
by the present package.) The perpage option is also offered by
footnpag and by the rather more general-purpose perpage

%package -n texlive-footmisx-doc
Version:        %{texlive_version}.%{texlive_noarch}.20161201svn42621
Release:        0
Summary:        Documentation for texlive-footmisx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-footmisx-doc
This package includes the documentation for texlive-footmisx

%post -n texlive-footmisx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-footmisx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-footmisx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-footmisx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/footmisx/README

%files -n texlive-footmisx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/footmisx/footmisx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-footmisx-%{texlive_version}.%{texlive_noarch}.20161201svn42621-%{release}-zypper
%endif

%package -n texlive-footnotebackref
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn27034
Release:        0
Summary:        Back-references from footnotes
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
Recommends:     texlive-footnotebackref-doc >= %{texlive_version}
Provides:       tex(footnotebackref.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(letltxmacro.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source82:       footnotebackref.tar.xz
Source83:       footnotebackref.doc.tar.xz

%description -n texlive-footnotebackref
The package provides the means of creating hyperlinks, from a
footnote at the bottom of the page, back to the occurence of
the footnote in the main text.

%package -n texlive-footnotebackref-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn27034
Release:        0
Summary:        Documentation for texlive-footnotebackref
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-footnotebackref-doc
This package includes the documentation for texlive-footnotebackref

%post -n texlive-footnotebackref
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-footnotebackref 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-footnotebackref
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-footnotebackref-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/footnotebackref/README
%{_texmfdistdir}/doc/latex/footnotebackref/footnotebackref.pdf
%{_texmfdistdir}/doc/latex/footnotebackref/footnotebackref.tex

%files -n texlive-footnotebackref
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/footnotebackref/footnotebackref.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-footnotebackref-%{texlive_version}.%{texlive_noarch}.1.0svn27034-%{release}-zypper
%endif

%package -n texlive-footnotehyper
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn52676
Release:        0
Summary:        Hyperref aware footnote.sty
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
Recommends:     texlive-footnotehyper-doc >= %{texlive_version}
Provides:       tex(footnotehyper.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source84:       footnotehyper.tar.xz
Source85:       footnotehyper.doc.tar.xz

%description -n texlive-footnotehyper
The footnote package by Mark Wooding dates back to 1997 and has
not been made hyperref compatible. The aim of the present
package is to do that.

%package -n texlive-footnotehyper-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn52676
Release:        0
Summary:        Documentation for texlive-footnotehyper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-footnotehyper-doc
This package includes the documentation for texlive-footnotehyper

%post -n texlive-footnotehyper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-footnotehyper 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-footnotehyper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-footnotehyper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/footnotehyper/README.md
%{_texmfdistdir}/doc/latex/footnotehyper/footnotehyper.pdf
%{_texmfdistdir}/doc/latex/footnotehyper/footnotehyper.tex

%files -n texlive-footnotehyper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/footnotehyper/footnotehyper.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-footnotehyper-%{texlive_version}.%{texlive_noarch}.1.1asvn52676-%{release}-zypper
%endif

%package -n texlive-footnoterange
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn52910
Release:        0
Summary:        References to ranges of footnotes
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
Recommends:     texlive-footnoterange-doc >= %{texlive_version}
Provides:       tex(footnoterange.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(ltxcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source86:       footnoterange.tar.xz
Source87:       footnoterange.doc.tar.xz

%description -n texlive-footnoterange
The package provides the environments footnoterange and
footnoterange*. Multiple footnotes inside these environments
are not referenced as (e.g.) "1 2 3" but as "1-3", i.e., the
range (from first to last referred footnote at that place) is
given. If the hyperref package is loaded with enabled
hyperfootnotes-option, then the references are hyperlinked.
(References to footnotes in footnoterange* environments are
never hyperlinked.)

%package -n texlive-footnoterange-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn52910
Release:        0
Summary:        Documentation for texlive-footnoterange
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-footnoterange-doc
This package includes the documentation for texlive-footnoterange

%post -n texlive-footnoterange
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-footnoterange 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-footnoterange
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-footnoterange-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/footnoterange/README
%{_texmfdistdir}/doc/latex/footnoterange/footnoterange-example.pdf
%{_texmfdistdir}/doc/latex/footnoterange/footnoterange.pdf

%files -n texlive-footnoterange
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/footnoterange/footnoterange.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-footnoterange-%{texlive_version}.%{texlive_noarch}.1.0csvn52910-%{release}-zypper
%endif

%package -n texlive-footnpag
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Per-page numbering of footnotes
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
Recommends:     texlive-footnpag-doc >= %{texlive_version}
Provides:       tex(footnpag.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source88:       footnpag.tar.xz
Source89:       footnpag.doc.tar.xz

%description -n texlive-footnpag
Allows footnotes on individual pages to be numbered from 1,
rather than being numbered sequentially through the document.

%package -n texlive-footnpag-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-footnpag
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-footnpag-doc
This package includes the documentation for texlive-footnpag

%post -n texlive-footnpag
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-footnpag 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-footnpag
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-footnpag-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/footnpag/CATALOG
%{_texmfdistdir}/doc/latex/footnpag/History
%{_texmfdistdir}/doc/latex/footnpag/INSTALL
%{_texmfdistdir}/doc/latex/footnpag/Imakefile
%{_texmfdistdir}/doc/latex/footnpag/License
%{_texmfdistdir}/doc/latex/footnpag/MANIFEST
%{_texmfdistdir}/doc/latex/footnpag/README
%{_texmfdistdir}/doc/latex/footnpag/TODO
%{_texmfdistdir}/doc/latex/footnpag/footnpag-doc.sty
%{_texmfdistdir}/doc/latex/footnpag/footnpag-user.pdf
%{_texmfdistdir}/doc/latex/footnpag/footnpag-user.tex
%{_texmfdistdir}/doc/latex/footnpag/footnpag.doc
%{_texmfdistdir}/doc/latex/footnpag/test/Imakefile
%{_texmfdistdir}/doc/latex/footnpag/test/eqnarray-fnmark.tex
%{_texmfdistdir}/doc/latex/footnpag/test/late.tex
%{_texmfdistdir}/doc/latex/footnpag/test/many.tex
%{_texmfdistdir}/doc/latex/footnpag/test/minipage.tex
%{_texmfdistdir}/doc/latex/footnpag/test/report.tex
%{_texmfdistdir}/doc/latex/footnpag/test/title-2col.tex

%files -n texlive-footnpag
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/footnpag/footnpag.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-footnpag-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-forarray
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Using array structures in LaTeX
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
Recommends:     texlive-forarray-doc >= %{texlive_version}
Provides:       tex(forarray.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source90:       forarray.tar.xz
Source91:       forarray.doc.tar.xz

%description -n texlive-forarray
The package provides functionality for processing lists and
array structures in LaTeX. Arrays can contain characters as
well as TeX and LaTeX commands, nesting of arrays is possible,
and arrays are processed within the same brace level as their
surrounding environment. Array levels can be delimited by
characters or control sequences defined by the user. Practical
uses of this package include data management, construction of
lists and tables, and calculations based on the contents of
lists and arrays.

%package -n texlive-forarray-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Documentation for texlive-forarray
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-forarray-doc
This package includes the documentation for texlive-forarray

%post -n texlive-forarray
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-forarray 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-forarray
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-forarray-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/forarray/README.txt
%{_texmfdistdir}/doc/latex/forarray/forarray
%{_texmfdistdir}/doc/latex/forarray/forarray-test.pdf
%{_texmfdistdir}/doc/latex/forarray/forarray-test.tex
%{_texmfdistdir}/doc/latex/forarray/forarray.dtm
%{_texmfdistdir}/doc/latex/forarray/forarray.dts
%{_texmfdistdir}/doc/latex/forarray/forarray.pdf

%files -n texlive-forarray
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/forarray/forarray.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-forarray-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif

%package -n texlive-foreign
Version:        %{texlive_version}.%{texlive_noarch}.2.7svn27819
Release:        0
Summary:        Systematic treatment of 'foreign' words in documents
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
Recommends:     texlive-foreign-doc >= %{texlive_version}
Provides:       tex(foreign.sty)
Requires:       tex(xpunctuate.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source92:       foreign.tar.xz
Source93:       foreign.doc.tar.xz

%description -n texlive-foreign
The package supports authors' use of consistent typesetting of
foreign words in documents.

%package -n texlive-foreign-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.7svn27819
Release:        0
Summary:        Documentation for texlive-foreign
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-foreign-doc
This package includes the documentation for texlive-foreign

%post -n texlive-foreign
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-foreign 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-foreign
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-foreign-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/foreign/README
%{_texmfdistdir}/doc/latex/foreign/foreign.pdf

%files -n texlive-foreign
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/foreign/foreign.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-foreign-%{texlive_version}.%{texlive_noarch}.2.7svn27819-%{release}-zypper
%endif

%package -n texlive-forest
Version:        %{texlive_version}.%{texlive_noarch}.2.1.5svn44797
Release:        0
Summary:        Drawing (linguistic) trees
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-elocalloc >= %{texlive_version}
#!BuildIgnore: texlive-elocalloc
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
Recommends:     texlive-forest-doc >= %{texlive_version}
Provides:       tex(forest-compat.sty)
Provides:       tex(forest-doc.sty)
Provides:       tex(forest-index.sty)
Provides:       tex(forest-lib-edges.sty)
Provides:       tex(forest-lib-linguistics.sty)
Provides:       tex(forest.sty)
Requires:       tex(dingbat.sty)
Requires:       tex(elocalloc.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(inlinedef.sty)
Requires:       tex(lstdoc.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source94:       forest.tar.xz
Source95:       forest.doc.tar.xz

%description -n texlive-forest
The package provides a PGF/TikZ-based mechanism for drawing
linguistic (and other kinds of) trees. Its main features are: a
packing algorithm which can produce very compact trees; a
user-friendly interface consisting of the familiar bracket
encoding of trees plus the key-value interface to
option-setting; many tree-formatting options, with control over
option values of individual nodes and mechanisms for their
manipulation; the possibility to decorate the tree using the
full power of PGF/TikZ; and an externalization mechanism
sensitive to code-changes.

%package -n texlive-forest-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1.5svn44797
Release:        0
Summary:        Documentation for texlive-forest
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-forest-doc
This package includes the documentation for texlive-forest

%post -n texlive-forest
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-forest 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-forest
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-forest-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/forest/LICENCE
%{_texmfdistdir}/doc/latex/forest/README
%{_texmfdistdir}/doc/latex/forest/forest-doc.pdf
%{_texmfdistdir}/doc/latex/forest/forest-doc.tex
%{_texmfdistdir}/doc/latex/forest/forest.pdf
%{_texmfdistdir}/doc/latex/forest/tex.bib

%files -n texlive-forest
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/forest/forest-doc.ist
%{_texmfdistdir}/tex/latex/forest/forest-compat.sty
%{_texmfdistdir}/tex/latex/forest/forest-doc.sty
%{_texmfdistdir}/tex/latex/forest/forest-index.sty
%{_texmfdistdir}/tex/latex/forest/forest-lib-edges.sty
%{_texmfdistdir}/tex/latex/forest/forest-lib-linguistics.sty
%{_texmfdistdir}/tex/latex/forest/forest.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-forest-%{texlive_version}.%{texlive_noarch}.2.1.5svn44797-%{release}-zypper
%endif

%package -n texlive-forest-quickstart
Version:        %{texlive_version}.%{texlive_noarch}.svn42503
Release:        0
Summary:        Quickstart Guide for Linguists package "forest"
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
Source96:       forest-quickstart.doc.tar.xz

%description -n texlive-forest-quickstart
forest is a PGF/TikZ-based package for drawing linguistic (and
other kinds of) trees. This manual provides a quickstart guide
for linguists with just the essential things that you need to
get started.
%post -n texlive-forest-quickstart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-forest-quickstart 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-forest-quickstart
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-forest-quickstart
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/forest-quickstart/ForestQuickstart.pdf
%{_texmfdistdir}/doc/latex/forest-quickstart/ForestQuickstart.tex
%{_texmfdistdir}/doc/latex/forest-quickstart/README
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-forest-quickstart-%{texlive_version}.%{texlive_noarch}.svn42503-%{release}-zypper
%endif

%package -n texlive-forloop
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Iteration in LaTeX
License:        LGPL-2.1-or-later
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
Recommends:     texlive-forloop-doc >= %{texlive_version}
Provides:       tex(forloop.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source97:       forloop.tar.xz
Source98:       forloop.doc.tar.xz

%description -n texlive-forloop
The package provides a command \forloop for doing iteration in
LaTeX macro programming.

%package -n texlive-forloop-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn15878
Release:        0
Summary:        Documentation for texlive-forloop
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-forloop-doc
This package includes the documentation for texlive-forloop

%post -n texlive-forloop
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-forloop 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-forloop
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-forloop-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/forloop/README
%{_texmfdistdir}/doc/latex/forloop/forloop.pdf

%files -n texlive-forloop
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/forloop/forloop.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-forloop-%{texlive_version}.%{texlive_noarch}.3.0svn15878-%{release}-zypper
%endif

%package -n texlive-formation-latex-ul
Version:        %{texlive_version}.%{texlive_noarch}.2019.03svn50205
Release:        0
Summary:        Introductory LaTeX course in French
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
Recommends:     texlive-formation-latex-ul-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source99:       formation-latex-ul.source.tar.xz
Source100:      formation-latex-ul.doc.tar.xz

%description -n texlive-formation-latex-ul
This package contains the supporting documentation, slides,
exercise files, and templates for an introductory LaTeX course
(in French) prepared for Universite Laval, Quebec, Canada.

%package -n texlive-formation-latex-ul-doc
Version:        %{texlive_version}.%{texlive_noarch}.2019.03svn50205
Release:        0
Summary:        Documentation for texlive-formation-latex-ul
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-formation-latex-ul-doc:fr)

%description -n texlive-formation-latex-ul-doc
This package includes the documentation for texlive-formation-latex-ul

%post -n texlive-formation-latex-ul
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-formation-latex-ul 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-formation-latex-ul
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-formation-latex-ul-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/formation-latex-ul/CONTRIBUTING.md
%{_texmfdistdir}/doc/latex/formation-latex-ul/LICENSE
%{_texmfdistdir}/doc/latex/formation-latex-ul/NEWS
%{_texmfdistdir}/doc/latex/formation-latex-ul/README.md
%{_texmfdistdir}/doc/latex/formation-latex-ul/b-a-ba-math.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/console-screenshot.pdf
%{_texmfdistdir}/doc/latex/formation-latex-ul/emacs.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_classe+paquetages.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_commandes.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_complet.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_demo.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_gabarit.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_include.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_mathematiques.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_minimal.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_parties.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_renvois.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_subcaption.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_trucs.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/exercice_ulthese.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/formation-latex-ul-diapos.pdf
%{_texmfdistdir}/doc/latex/formation-latex-ul/formation-latex-ul.pdf
%{_texmfdistdir}/doc/latex/formation-latex-ul/pagetitre.tex
%{_texmfdistdir}/doc/latex/formation-latex-ul/rpresentation.tex

%files -n texlive-formation-latex-ul
%defattr(-,root,root,755)
%{_texmfdistdir}/source/latex/formation-latex-ul/apparence-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/apparence.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-classe-article.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-classe-article.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-classe-book.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-classe-book.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-classe-report.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-classe-report.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-renvoi-autoref.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-renvoi-autoref.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-renvoi-hyperref.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-renvoi-hyperref.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-renvoi.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-renvoi.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-titre.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exemple-titre.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exercice_commandes-solution.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/auxdoc/exercice_commandes-solution.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/bases-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/bases.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/bibliographie.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/boites.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/colophon-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/colophon.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/commandes.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/couverture-arriere-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/couverture-arriere.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/couverture-avant-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/couverture-avant.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/formation-latex-ul-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/formation-latex-ul.bib
%{_texmfdistdir}/source/latex/formation-latex-ul/formation-latex-ul.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/francais.bst
%{_texmfdistdir}/source/latex/formation-latex-ul/images/Meerkat_stare-diapos.jpg
%{_texmfdistdir}/source/latex/formation-latex-ul/images/Meerkat_stare.jpg
%{_texmfdistdir}/source/latex/formation-latex-ul/images/bibtex-texmaker.png
%{_texmfdistdir}/source/latex/formation-latex-ul/images/bibtex-texshop.png
%{_texmfdistdir}/source/latex/formation-latex-ul/images/by-sa.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/by.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/exemple-bibliographie-cropped-1.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/exemple-bibliographie-cropped-2.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/exemple-bibliographie-cropped-3.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/exercice_commandes-solution.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/formation-latex-ul.png
%{_texmfdistdir}/source/latex/formation-latex-ul/images/knuth.jpg
%{_texmfdistdir}/source/latex/formation-latex-ul/images/ponctuation.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/sa.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/section-non-num.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/section-num.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/tdm-dans-pdf.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/ul_p.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/xyz-emph.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/images/xyz-math.pdf
%{_texmfdistdir}/source/latex/formation-latex-ul/introduction.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/listings/exemple-bibliographie.bib
%{_texmfdistdir}/source/latex/formation-latex-ul/listings/exemple-bibliographie.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/mathematiques-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/mathematiques.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/notices-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/notices.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/organisation-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/organisation.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/prerequis-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/presentation-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/presentation.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/solutions.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/suite-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/sweave-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/tableaux+figures.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/tableaux-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/trucs+astuces.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/ulthese-diapos.tex
%{_texmfdistdir}/source/latex/formation-latex-ul/ulthese.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-formation-latex-ul-%{texlive_version}.%{texlive_noarch}.2019.03svn50205-%{release}-zypper
%endif

%package -n texlive-formlett
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn21480
Release:        0
Summary:        Letters to multiple recipients
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
Recommends:     texlive-formlett-doc >= %{texlive_version}
Provides:       tex(formlett.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source101:      formlett.tar.xz
Source102:      formlett.doc.tar.xz

%description -n texlive-formlett
A package for multiple letters from the same basic source; the
package offers parametrisation of the letters actually sent.

%package -n texlive-formlett-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn21480
Release:        0
Summary:        Documentation for texlive-formlett
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-formlett-doc
This package includes the documentation for texlive-formlett

%post -n texlive-formlett
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-formlett 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-formlett
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-formlett-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/formlett/prog_manual.pdf
%{_texmfdistdir}/doc/generic/formlett/prog_manual.tex
%{_texmfdistdir}/doc/generic/formlett/user_manual.pdf
%{_texmfdistdir}/doc/generic/formlett/user_manual.tex

%files -n texlive-formlett
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/formlett/formlett.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-formlett-%{texlive_version}.%{texlive_noarch}.2.3svn21480-%{release}-zypper
%endif

%package -n texlive-forms16be
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn51305
Release:        0
Summary:        Initialize form properties using big-endian encoding
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
Recommends:     texlive-forms16be-doc >= %{texlive_version}
Provides:       tex(forms16be.sty)
Provides:       tex(uni4basic-latin.def)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source103:      forms16be.tar.xz
Source104:      forms16be.doc.tar.xz

%description -n texlive-forms16be
This package provides support for UTF-16BE Unicode character
encoding (called a big-endian character string) for the text
string type (PDF Reference, version 1.7, beginning on page
158). Text strings are used in "text annotations, bookmark
names, article threads, document information, and so forth" (to
partially quote page 158). The particular application is to set
property values of form fields, at least those properties that
take the text strings as its value. The package contains
support for Basic Latin plus the ability to enter any unicode
character using the notation \uXXXX, where XXXX are four hex
digits. The Package works for dvips/Distiller, pdfLaTeX,
LuaLaTeX, and XeLaTeX.

%package -n texlive-forms16be-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn51305
Release:        0
Summary:        Documentation for texlive-forms16be
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-forms16be-doc
This package includes the documentation for texlive-forms16be

%post -n texlive-forms16be
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-forms16be 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-forms16be
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-forms16be-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/forms16be/README.md
%{_texmfdistdir}/doc/latex/forms16be/doc/forms16be-man.pdf
%{_texmfdistdir}/doc/latex/forms16be/doc/forms16be-man.tex
%{_texmfdistdir}/doc/latex/forms16be/examples/forms16be-ap.tex
%{_texmfdistdir}/doc/latex/forms16be/examples/forms16be-ef.pdf
%{_texmfdistdir}/doc/latex/forms16be/examples/forms16be-ef.tex
%{_texmfdistdir}/doc/latex/forms16be/examples/forms16be-hy.tex

%files -n texlive-forms16be
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/forms16be/forms16be.sty
%{_texmfdistdir}/tex/latex/forms16be/uni4basic-latin.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-forms16be-%{texlive_version}.%{texlive_noarch}.1.3svn51305-%{release}-zypper
%endif

%package -n texlive-formular
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn15878
Release:        0
Summary:        Create forms containing field for manual entry
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
Recommends:     texlive-formular-doc >= %{texlive_version}
Provides:       tex(formular.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source105:      formular.tar.xz
Source106:      formular.doc.tar.xz

%description -n texlive-formular
When typesetting forms there often arises the need for defining
fields which consist of one or more lines where the customer
can write something down manually. This package offers some
commands for defining such fields in a distinctive way.

%package -n texlive-formular-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn15878
Release:        0
Summary:        Documentation for texlive-formular
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-formular-doc
This package includes the documentation for texlive-formular

%post -n texlive-formular
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-formular 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-formular
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-formular-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/formular/README
%{_texmfdistdir}/doc/latex/formular/formular.pdf

%files -n texlive-formular
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/formular/formular.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-formular-%{texlive_version}.%{texlive_noarch}.1.0asvn15878-%{release}-zypper
%endif

%package -n texlive-forum
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Forum fonts with LaTeX support
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
Requires:       texlive-forum-fonts >= %{texlive_version}
Recommends:     texlive-forum-doc >= %{texlive_version}
Provides:       tex(Forum-Bold-lf-ly1--base.tfm)
Provides:       tex(Forum-Bold-lf-ly1.tfm)
Provides:       tex(Forum-Bold-lf-ly1.vf)
Provides:       tex(Forum-Bold-lf-ot1.tfm)
Provides:       tex(Forum-Bold-lf-t1--base.tfm)
Provides:       tex(Forum-Bold-lf-t1.tfm)
Provides:       tex(Forum-Bold-lf-t1.vf)
Provides:       tex(Forum-Bold-lf-t2a.tfm)
Provides:       tex(Forum-Bold-lf-t2b.tfm)
Provides:       tex(Forum-Bold-lf-t2c.tfm)
Provides:       tex(Forum-Bold-lf-ts1--base.tfm)
Provides:       tex(Forum-Bold-lf-ts1.tfm)
Provides:       tex(Forum-Bold-lf-ts1.vf)
Provides:       tex(Forum-lf-ly1--base.tfm)
Provides:       tex(Forum-lf-ly1.tfm)
Provides:       tex(Forum-lf-ly1.vf)
Provides:       tex(Forum-lf-ot1.tfm)
Provides:       tex(Forum-lf-t1--base.tfm)
Provides:       tex(Forum-lf-t1.tfm)
Provides:       tex(Forum-lf-t1.vf)
Provides:       tex(Forum-lf-t2a.tfm)
Provides:       tex(Forum-lf-t2b.tfm)
Provides:       tex(Forum-lf-t2c.tfm)
Provides:       tex(Forum-lf-ts1--base.tfm)
Provides:       tex(Forum-lf-ts1.tfm)
Provides:       tex(Forum-lf-ts1.vf)
Provides:       tex(LY1Forum-LF.fd)
Provides:       tex(OT1Forum-LF.fd)
Provides:       tex(T1Forum-LF.fd)
Provides:       tex(T2AForum-LF.fd)
Provides:       tex(T2BForum-LF.fd)
Provides:       tex(T2CForum-LF.fd)
Provides:       tex(TS1Forum-LF.fd)
Provides:       tex(forum.map)
Provides:       tex(forum.sty)
Provides:       tex(frm_acf3pt.enc)
Provides:       tex(frm_b5i5mx.enc)
Provides:       tex(frm_e2otk2.enc)
Provides:       tex(frm_fx2ufv.enc)
Provides:       tex(frm_jsuphk.enc)
Provides:       tex(frm_o6hya7.enc)
Provides:       tex(frm_ylkcu6.enc)
Provides:       tex(frm_zacml7.enc)
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
Source107:      forum.tar.xz
Source108:      forum.doc.tar.xz

%description -n texlive-forum
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Forum font, designed by Denis Masharov. Forum
has antique, classic "Roman" proportions. It can be used to set
body texts and works well in titles and headlines too. It is
truly multilingual, with glyphs for Central and Eastern Europe,
Baltics, Cyrillic and Asian Cyrillic communities. There is
currently just a regular weight and an artificially emboldened
bold.

%package -n texlive-forum-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Documentation for texlive-forum
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-forum-doc
This package includes the documentation for texlive-forum


%package -n texlive-forum-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Severed fonts for texlive-forum
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-forum-fonts
The  separated fonts package for texlive-forum
%post -n texlive-forum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap forum.map' >> /var/run/texlive/run-updmap

%postun -n texlive-forum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap forum.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-forum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-forum-fonts
%files -n texlive-forum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/forum/OFL.txt
%{_texmfdistdir}/doc/fonts/forum/README
%{_texmfdistdir}/doc/fonts/forum/forum-samples.pdf
%{_texmfdistdir}/doc/fonts/forum/forum-samples.tex

%files -n texlive-forum
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_acf3pt.enc
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_b5i5mx.enc
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_e2otk2.enc
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_fx2ufv.enc
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_jsuphk.enc
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_o6hya7.enc
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_ylkcu6.enc
%{_texmfdistdir}/fonts/enc/dvips/forum/frm_zacml7.enc
%{_texmfdistdir}/fonts/map/dvips/forum/forum.map
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/forum/Forum-lf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/forum/Forum-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/forum/Forum-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/forum/Forum-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/forum/Forum-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/forum/Forum-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/forum/Forum-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/forum/Forum-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/forum/Forum-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/forum/Forum-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/forum/Forum-lf-ts1.vf
%{_texmfdistdir}/tex/latex/forum/LY1Forum-LF.fd
%{_texmfdistdir}/tex/latex/forum/OT1Forum-LF.fd
%{_texmfdistdir}/tex/latex/forum/T1Forum-LF.fd
%{_texmfdistdir}/tex/latex/forum/T2AForum-LF.fd
%{_texmfdistdir}/tex/latex/forum/T2BForum-LF.fd
%{_texmfdistdir}/tex/latex/forum/T2CForum-LF.fd
%{_texmfdistdir}/tex/latex/forum/TS1Forum-LF.fd
%{_texmfdistdir}/tex/latex/forum/forum.sty

%files -n texlive-forum-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-forum
%{_datadir}/fontconfig/conf.avail/58-texlive-forum.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-forum.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-forum.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-forum/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-forum/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-forum/fonts.scale
%{_datadir}/fonts/texlive-forum/Forum-Bold.ttf
%{_datadir}/fonts/texlive-forum/Forum-Regular.ttf
%{_datadir}/fonts/texlive-forum/Forum-Bold.pfb
%{_datadir}/fonts/texlive-forum/Forum-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-forum-fonts-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif

%package -n texlive-fouridx
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn32214
Release:        0
Summary:        Left sub- and superscripts in maths mode
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
Recommends:     texlive-fouridx-doc >= %{texlive_version}
Provides:       tex(fouridx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source109:      fouridx.tar.xz
Source110:      fouridx.doc.tar.xz

%description -n texlive-fouridx
The package enables left subscripts and superscripts in maths
mode. The sub- and superscripts are raised for optimum fitting
to the symbol indexed, in such a way that left and right sub-
and superscripts are set on the same level, as appropriate. The
package provides an alternative to the use of the \sideset
command in the amsmath package.

%package -n texlive-fouridx-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn32214
Release:        0
Summary:        Documentation for texlive-fouridx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fouridx-doc
This package includes the documentation for texlive-fouridx

%post -n texlive-fouridx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fouridx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fouridx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fouridx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fouridx/README
%{_texmfdistdir}/doc/latex/fouridx/fouridx.pdf

%files -n texlive-fouridx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fouridx/fouridx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fouridx-%{texlive_version}.%{texlive_noarch}.2.00svn32214-%{release}-zypper
%endif

%package -n texlive-fourier
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn54090
Release:        0
Summary:        Using Utopia fonts in LaTeX documents
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
Requires:       texlive-fourier-fonts >= %{texlive_version}
Recommends:     texlive-fourier-doc >= %{texlive_version}
Provides:       tex(fmlfutm.fd)
Provides:       tex(fmlfutmi.fd)
Provides:       tex(fmsfutm.fd)
Provides:       tex(fmxfutm.fd)
Provides:       tex(fourier-alt-black.tfm)
Provides:       tex(fourier-alt-bold-sl.tfm)
Provides:       tex(fourier-alt-bold.tfm)
Provides:       tex(fourier-alt-boldita.tfm)
Provides:       tex(fourier-alt-ita.tfm)
Provides:       tex(fourier-alt-semi-sl.tfm)
Provides:       tex(fourier-alt-semi.tfm)
Provides:       tex(fourier-alt-semiita.tfm)
Provides:       tex(fourier-alt-sl.tfm)
Provides:       tex(fourier-alt.tfm)
Provides:       tex(fourier-bb.tfm)
Provides:       tex(fourier-ligs-it.tfm)
Provides:       tex(fourier-ligs.tfm)
Provides:       tex(fourier-mcl.tfm)
Provides:       tex(fourier-mex.tfm)
Provides:       tex(fourier-ml.tfm)
Provides:       tex(fourier-mlb.tfm)
Provides:       tex(fourier-mlit.tfm)
Provides:       tex(fourier-mlitb.tfm)
Provides:       tex(fourier-ms.tfm)
Provides:       tex(fourier-orns.sty)
Provides:       tex(fourier-orns.tfm)
Provides:       tex(fourier-utopia-expert.map)
Provides:       tex(fourier.map)
Provides:       tex(fourier.sty)
Provides:       tex(fut-oldlatin-it.tfm)
Provides:       tex(fut-oldlatin.tfm)
Provides:       tex(futb-sup.tfm)
Provides:       tex(futb-sup.vf)
Provides:       tex(futb8c.tfm)
Provides:       tex(futb8c.vf)
Provides:       tex(futb8r.tfm)
Provides:       tex(futb8t.tfm)
Provides:       tex(futb8t.vf)
Provides:       tex(futb8x.tfm)
Provides:       tex(futb9c.tfm)
Provides:       tex(futb9c.vf)
Provides:       tex(futb9d.tfm)
Provides:       tex(futb9d.vf)
Provides:       tex(futb9e.tfm)
Provides:       tex(futb9e.vf)
Provides:       tex(futbc8t.tfm)
Provides:       tex(futbc8t.vf)
Provides:       tex(futbi-sup.tfm)
Provides:       tex(futbi-sup.vf)
Provides:       tex(futbi8c.tfm)
Provides:       tex(futbi8c.vf)
Provides:       tex(futbi8r.tfm)
Provides:       tex(futbi8t.tfm)
Provides:       tex(futbi8t.vf)
Provides:       tex(futbi8x.tfm)
Provides:       tex(futbi9c.tfm)
Provides:       tex(futbi9c.vf)
Provides:       tex(futbi9d.tfm)
Provides:       tex(futbi9d.vf)
Provides:       tex(futbi9e.tfm)
Provides:       tex(futbi9e.vf)
Provides:       tex(futbo8c.tfm)
Provides:       tex(futbo8c.vf)
Provides:       tex(futbo8r.tfm)
Provides:       tex(futbo8t.tfm)
Provides:       tex(futbo8t.vf)
Provides:       tex(futbo8x.tfm)
Provides:       tex(futbo9c.tfm)
Provides:       tex(futbo9c.vf)
Provides:       tex(futbo9d.tfm)
Provides:       tex(futbo9d.vf)
Provides:       tex(futbo9e.tfm)
Provides:       tex(futbo9e.vf)
Provides:       tex(futboorn.tfm)
Provides:       tex(futboorn.vf)
Provides:       tex(futborn.tfm)
Provides:       tex(futborn.vf)
Provides:       tex(futc-sup.tfm)
Provides:       tex(futc-sup.vf)
Provides:       tex(futc8r.tfm)
Provides:       tex(futc8x.tfm)
Provides:       tex(futc9c.tfm)
Provides:       tex(futc9c.vf)
Provides:       tex(futc9d.tfm)
Provides:       tex(futc9d.vf)
Provides:       tex(futc9e.tfm)
Provides:       tex(futc9e.vf)
Provides:       tex(futcorn.tfm)
Provides:       tex(futcorn.vf)
Provides:       tex(futmi.tfm)
Provides:       tex(futmi.vf)
Provides:       tex(futmib.tfm)
Provides:       tex(futmib.vf)
Provides:       tex(futmii.tfm)
Provides:       tex(futmii.vf)
Provides:       tex(futmiib.tfm)
Provides:       tex(futmiib.vf)
Provides:       tex(futr-sup.tfm)
Provides:       tex(futr-sup.vf)
Provides:       tex(futr8c.tfm)
Provides:       tex(futr8c.vf)
Provides:       tex(futr8r.tfm)
Provides:       tex(futr8t.tfm)
Provides:       tex(futr8t.vf)
Provides:       tex(futr8x.tfm)
Provides:       tex(futr9c.tfm)
Provides:       tex(futr9c.vf)
Provides:       tex(futr9d.tfm)
Provides:       tex(futr9d.vf)
Provides:       tex(futr9e.tfm)
Provides:       tex(futr9e.vf)
Provides:       tex(futrc8r.tfm)
Provides:       tex(futrc8t.tfm)
Provides:       tex(futrc8t.vf)
Provides:       tex(futrc9d.tfm)
Provides:       tex(futrc9d.vf)
Provides:       tex(futrc9e.tfm)
Provides:       tex(futrc9e.vf)
Provides:       tex(futrci9d.tfm)
Provides:       tex(futrci9d.vf)
Provides:       tex(futrci9e.tfm)
Provides:       tex(futrci9e.vf)
Provides:       tex(futrco8r.tfm)
Provides:       tex(futrco9d.tfm)
Provides:       tex(futrco9d.vf)
Provides:       tex(futrd8r.tfm)
Provides:       tex(futrd8t.tfm)
Provides:       tex(futrd8t.vf)
Provides:       tex(futri-sup.tfm)
Provides:       tex(futri-sup.vf)
Provides:       tex(futri8c.tfm)
Provides:       tex(futri8c.vf)
Provides:       tex(futri8r.tfm)
Provides:       tex(futri8t.tfm)
Provides:       tex(futri8t.vf)
Provides:       tex(futri8x.tfm)
Provides:       tex(futri9c.tfm)
Provides:       tex(futri9c.vf)
Provides:       tex(futri9d.tfm)
Provides:       tex(futri9d.vf)
Provides:       tex(futri9e.tfm)
Provides:       tex(futri9e.vf)
Provides:       tex(futro8c.tfm)
Provides:       tex(futro8c.vf)
Provides:       tex(futro8r.tfm)
Provides:       tex(futro8t.tfm)
Provides:       tex(futro8t.vf)
Provides:       tex(futro8x.tfm)
Provides:       tex(futro9c.tfm)
Provides:       tex(futro9c.vf)
Provides:       tex(futro9d.tfm)
Provides:       tex(futro9d.vf)
Provides:       tex(futro9e.tfm)
Provides:       tex(futro9e.vf)
Provides:       tex(futroorn.tfm)
Provides:       tex(futroorn.vf)
Provides:       tex(futrorn.tfm)
Provides:       tex(futrorn.vf)
Provides:       tex(futs-sup.tfm)
Provides:       tex(futs-sup.vf)
Provides:       tex(futs8r.tfm)
Provides:       tex(futs8x.tfm)
Provides:       tex(futs9c.tfm)
Provides:       tex(futs9c.vf)
Provides:       tex(futs9d.tfm)
Provides:       tex(futs9d.vf)
Provides:       tex(futs9e.tfm)
Provides:       tex(futs9e.vf)
Provides:       tex(futsc8r.tfm)
Provides:       tex(futsc9d.tfm)
Provides:       tex(futsc9d.vf)
Provides:       tex(futsc9e.tfm)
Provides:       tex(futsc9e.vf)
Provides:       tex(futsci9d.tfm)
Provides:       tex(futsci9d.vf)
Provides:       tex(futsci9e.tfm)
Provides:       tex(futsci9e.vf)
Provides:       tex(futsco8r.tfm)
Provides:       tex(futsco9d.vf)
Provides:       tex(futsi-sup.tfm)
Provides:       tex(futsi-sup.vf)
Provides:       tex(futsi8r.tfm)
Provides:       tex(futsi8x.tfm)
Provides:       tex(futsi9c.tfm)
Provides:       tex(futsi9c.vf)
Provides:       tex(futsi9d.tfm)
Provides:       tex(futsi9d.vf)
Provides:       tex(futsi9e.tfm)
Provides:       tex(futsi9e.vf)
Provides:       tex(futso8r.tfm)
Provides:       tex(futso8x.tfm)
Provides:       tex(futso9c.tfm)
Provides:       tex(futso9c.vf)
Provides:       tex(futso9d.tfm)
Provides:       tex(futso9d.vf)
Provides:       tex(futso9e.tfm)
Provides:       tex(futso9e.vf)
Provides:       tex(futsoorn.tfm)
Provides:       tex(futsoorn.vf)
Provides:       tex(futsorn.tfm)
Provides:       tex(futsorn.vf)
Provides:       tex(futsy.tfm)
Provides:       tex(futsy.vf)
Provides:       tex(putb8a.tfm)
Provides:       tex(putb8x.tfm)
Provides:       tex(putbi8a.tfm)
Provides:       tex(putbi8x.tfm)
Provides:       tex(putbo8x.tfm)
Provides:       tex(putc8a.tfm)
Provides:       tex(putc8x.tfm)
Provides:       tex(putr8a.tfm)
Provides:       tex(putr8x.tfm)
Provides:       tex(putrc8a.tfm)
Provides:       tex(putrd8a.tfm)
Provides:       tex(putri8a.tfm)
Provides:       tex(putri8x.tfm)
Provides:       tex(putro8x.tfm)
Provides:       tex(puts8a.tfm)
Provides:       tex(puts8x.tfm)
Provides:       tex(putsc8a.tfm)
Provides:       tex(putsi8a.tfm)
Provides:       tex(putsi8x.tfm)
Provides:       tex(putso8x.tfm)
Provides:       tex(t1fut-sup.fd)
Provides:       tex(t1futj.fd)
Provides:       tex(t1futs.fd)
Provides:       tex(t1futx.fd)
Provides:       tex(ts1futj.fd)
Provides:       tex(ts1futs.fd)
Provides:       tex(ts1futx.fd)
Provides:       tex(ufuts.fd)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(iftex.sty)
Requires:       tex(textcomp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source111:      fourier.tar.xz
Source112:      fourier.doc.tar.xz

%description -n texlive-fourier
Fourier-GUTenberg is a LaTeX typesetting system which uses
Adobe Utopia as its standard base font. Fourier-GUTenberg
provides all complementary typefaces needed to allow Utopia
based TeX typesetting, including an extensive mathematics set
and several other symbols. The system is absolutely
stand-alone: apart from Utopia and Fourier, no other typefaces
are required. The fourier fonts will also work with Adobe
Utopia Expert fonts, which are only available for purchase.
Utopia is a registered trademark of Adobe Systems Incorporated

%package -n texlive-fourier-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn54090
Release:        0
Summary:        Documentation for texlive-fourier
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fourier-doc
This package includes the documentation for texlive-fourier


%package -n texlive-fourier-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn54090
Release:        0
Summary:        Severed fonts for texlive-fourier
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fourier-fonts
The  separated fonts package for texlive-fourier
%post -n texlive-fourier
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap fourier-utopia-expert.map' >> /var/run/texlive/run-updmap
echo 'addMap fourier.map' >> /var/run/texlive/run-updmap

%postun -n texlive-fourier 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap fourier-utopia-expert.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap fourier.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-fourier
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fourier-fonts
%files -n texlive-fourier-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fourier/README
%{_texmfdistdir}/doc/fonts/fourier/fourier-doc-en.pdf
%{_texmfdistdir}/doc/fonts/fourier/fourier-doc-en.tex
%{_texmfdistdir}/doc/fonts/fourier/fourier-orns-doc.pdf
%{_texmfdistdir}/doc/fonts/fourier/fourier-orns-doc.tex

%files -n texlive-fourier
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-black.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-bold.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-boldita.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-ita.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-semi.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt-semiita.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-alt.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-bb.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mcl.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mex.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-ml.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mlb.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mlit.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-mlitb.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-ms.afm
%{_texmfdistdir}/fonts/afm/public/fourier/fourier-orns.afm
%{_texmfdistdir}/fonts/map/dvips/fourier/fourier-utopia-expert.map
%{_texmfdistdir}/fonts/map/dvips/fourier/fourier.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fourier/FourierOrns-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fourier/FourierOrns-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fourier/FourierOrns-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/fourier/FourierOrns-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-black.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-bold-sl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-boldita.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-ita.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-semi-sl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-semi.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-semiita.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt-sl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-alt.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-bb.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-ligs-it.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-ligs.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mcl.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mex.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-ml.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mlb.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mlit.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-mlitb.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-ms.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fourier-orns.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fut-oldlatin-it.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/fut-oldlatin.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb-sup.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futb9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi-sup.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbi9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futbo9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futboorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futborn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc-sup.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futc9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futcorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmi.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmib.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmii.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futmiib.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr-sup.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futr9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrc9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrci9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrci9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrco9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrd8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrd8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri-sup.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futri9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futro9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futroorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futrorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs-sup.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futs9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsc9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsc9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsci9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsci9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi-sup.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsi9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso8r.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso9c.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso9d.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futso9e.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsoorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsorn.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/futsy.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putb8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putbi8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putbo8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putc8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putr8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putrc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putrd8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putri8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putri8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putro8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/puts8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/puts8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putsi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putsi8x.tfm
%{_texmfdistdir}/fonts/tfm/public/fourier/putso8x.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-black.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-boldita.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-ita.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-semi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt-semiita.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-alt.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-bb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-mcl.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-mex.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-ml.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-mlb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-mlit.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-mlitb.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-ms.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/fourier/fourier-orns.pfb
%{_texmfdistdir}/fonts/vf/public/fourier/futb-sup.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futb9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbc8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi-sup.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbi9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futbo9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futboorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futborn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futc-sup.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futc9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futc9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futc9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futcorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmi.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmib.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmii.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futmiib.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr-sup.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futr9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrc8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrc9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrc9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrci9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrci9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrco9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrd8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri-sup.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futri9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro8c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro8t.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futro9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futroorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futrorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futs-sup.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futs9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futs9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futs9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsc9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsc9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsci9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsci9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsco9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsi-sup.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsi9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsi9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsi9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futso9c.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futso9d.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futso9e.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsoorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsorn.vf
%{_texmfdistdir}/fonts/vf/public/fourier/futsy.vf
%{_texmfdistdir}/tex/latex/fourier/fmlfutm.fd
%{_texmfdistdir}/tex/latex/fourier/fmlfutmi.fd
%{_texmfdistdir}/tex/latex/fourier/fmsfutm.fd
%{_texmfdistdir}/tex/latex/fourier/fmxfutm.fd
%{_texmfdistdir}/tex/latex/fourier/fourier-orns.sty
%{_texmfdistdir}/tex/latex/fourier/fourier.sty
%{_texmfdistdir}/tex/latex/fourier/t1fut-sup.fd
%{_texmfdistdir}/tex/latex/fourier/t1futj.fd
%{_texmfdistdir}/tex/latex/fourier/t1futs.fd
%{_texmfdistdir}/tex/latex/fourier/t1futx.fd
%{_texmfdistdir}/tex/latex/fourier/ts1futj.fd
%{_texmfdistdir}/tex/latex/fourier/ts1futs.fd
%{_texmfdistdir}/tex/latex/fourier/ts1futx.fd
%{_texmfdistdir}/tex/latex/fourier/ufuts.fd

%files -n texlive-fourier-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fourier
%{_datadir}/fontconfig/conf.avail/58-texlive-fourier.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-fourier.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-fourier.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fourier/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fourier/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fourier/fonts.scale
%{_datadir}/fonts/texlive-fourier/FourierOrns-Bold.otf
%{_datadir}/fonts/texlive-fourier/FourierOrns-BoldItalic.otf
%{_datadir}/fonts/texlive-fourier/FourierOrns-Italic.otf
%{_datadir}/fonts/texlive-fourier/FourierOrns-Regular.otf
%{_datadir}/fonts/texlive-fourier/fourier-alt-black.pfb
%{_datadir}/fonts/texlive-fourier/fourier-alt-bold.pfb
%{_datadir}/fonts/texlive-fourier/fourier-alt-boldita.pfb
%{_datadir}/fonts/texlive-fourier/fourier-alt-ita.pfb
%{_datadir}/fonts/texlive-fourier/fourier-alt-semi.pfb
%{_datadir}/fonts/texlive-fourier/fourier-alt-semiita.pfb
%{_datadir}/fonts/texlive-fourier/fourier-alt.pfb
%{_datadir}/fonts/texlive-fourier/fourier-bb.pfb
%{_datadir}/fonts/texlive-fourier/fourier-mcl.pfb
%{_datadir}/fonts/texlive-fourier/fourier-mex.pfb
%{_datadir}/fonts/texlive-fourier/fourier-ml.pfb
%{_datadir}/fonts/texlive-fourier/fourier-mlb.pfb
%{_datadir}/fonts/texlive-fourier/fourier-mlit.pfb
%{_datadir}/fonts/texlive-fourier/fourier-mlitb.pfb
%{_datadir}/fonts/texlive-fourier/fourier-ms.pfb
%{_datadir}/fonts/texlive-fourier/fourier-orns.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fourier-fonts-%{texlive_version}.%{texlive_noarch}.2.2svn54090-%{release}-zypper
%endif

%package -n texlive-fouriernc
Version:        %{texlive_version}.%{texlive_noarch}.svn29646
Release:        0
Summary:        Use New Century Schoolbook text with Fourier maths fonts
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
Recommends:     texlive-fouriernc-doc >= %{texlive_version}
Provides:       tex(fmlfncm.fd)
Provides:       tex(fmlfncmi.fd)
Provides:       tex(fmsfncm.fd)
Provides:       tex(fncmi.tfm)
Provides:       tex(fncmi.vf)
Provides:       tex(fncmib.tfm)
Provides:       tex(fncmib.vf)
Provides:       tex(fncmii.tfm)
Provides:       tex(fncmii.vf)
Provides:       tex(fncmiib.tfm)
Provides:       tex(fncmiib.vf)
Provides:       tex(fncsy.tfm)
Provides:       tex(fncsy.vf)
Provides:       tex(fouriernc.sty)
Provides:       tex(t1fnc.fd)
Provides:       tex(ts1fnc.fd)
Requires:       tex(fourier-mcl.tfm)
Requires:       tex(fourier-ml.tfm)
Requires:       tex(fourier-mlb.tfm)
Requires:       tex(fourier-mlit.tfm)
Requires:       tex(fourier-mlitb.tfm)
Requires:       tex(fourier-ms.tfm)
Requires:       tex(fourier.sty)
Requires:       tex(pncb8r.tfm)
Requires:       tex(pncbi8r.tfm)
Requires:       tex(pncr8r.tfm)
Requires:       tex(pncri8r.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source113:      fouriernc.tar.xz
Source114:      fouriernc.doc.tar.xz

%description -n texlive-fouriernc
This package provides a LaTeX mathematics font setup for use
with New Century Schoolbook text. In order to use it you need
to have the Fourier-GUTenberg fonts installed.

%package -n texlive-fouriernc-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn29646
Release:        0
Summary:        Documentation for texlive-fouriernc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fouriernc-doc
This package includes the documentation for texlive-fouriernc

%post -n texlive-fouriernc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fouriernc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fouriernc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fouriernc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fouriernc/README
%{_texmfdistdir}/doc/fonts/fouriernc/build-fouriernc.tex
%{_texmfdistdir}/doc/fonts/fouriernc/mathit.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/mathsy.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/omlgutop.etx
%{_texmfdistdir}/doc/fonts/fouriernc/omsgutop.etx
%{_texmfdistdir}/doc/fonts/fouriernc/setxheight.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/specialkernings.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/specialkerningsital.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/substitutes.zip
%{_texmfdistdir}/doc/fonts/fouriernc/test_fouriernc.pdf
%{_texmfdistdir}/doc/fonts/fouriernc/unset0.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/unset0A.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/unsetAlph.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/unsetUCgreek.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/unsetfontparams.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/unsetmu.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/unsetpar.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/zrmhax.mtx
%{_texmfdistdir}/doc/fonts/fouriernc/zrykernx.mtx

%files -n texlive-fouriernc
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mcl.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-ml.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mlb.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mlit.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-mlitb.afm
%{_texmfdistdir}/fonts/afm/public/fouriernc/fourier-ms.afm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmi.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmib.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmii.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncmiib.tfm
%{_texmfdistdir}/fonts/tfm/public/fouriernc/fncsy.tfm
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmi.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmib.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmii.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncmiib.vf
%{_texmfdistdir}/fonts/vf/public/fouriernc/fncsy.vf
%{_texmfdistdir}/tex/latex/fouriernc/fmlfncm.fd
%{_texmfdistdir}/tex/latex/fouriernc/fmlfncmi.fd
%{_texmfdistdir}/tex/latex/fouriernc/fmsfncm.fd
%{_texmfdistdir}/tex/latex/fouriernc/fouriernc.sty
%{_texmfdistdir}/tex/latex/fouriernc/t1fnc.fd
%{_texmfdistdir}/tex/latex/fouriernc/ts1fnc.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fouriernc-%{texlive_version}.%{texlive_noarch}.svn29646-%{release}-zypper
%endif

%package -n texlive-fp
Version:        %{texlive_version}.%{texlive_noarch}.2.1dsvn49719
Release:        0
Summary:        Fixed point arithmetic
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
Recommends:     texlive-fp-doc >= %{texlive_version}
Provides:       tex(defpattern.sty)
Provides:       tex(fp-addons.sty)
Provides:       tex(fp-basic.sty)
Provides:       tex(fp-eqn.sty)
Provides:       tex(fp-eval.sty)
Provides:       tex(fp-exp.sty)
Provides:       tex(fp-pas.sty)
Provides:       tex(fp-random.sty)
Provides:       tex(fp-snap.sty)
Provides:       tex(fp-trigo.sty)
Provides:       tex(fp-upn.sty)
Provides:       tex(fp.sty)
Provides:       tex(fp.tex)
Provides:       tex(lfp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source115:      fp.tar.xz
Source116:      fp.doc.tar.xz

%description -n texlive-fp
An extensive collection of arithmetic operations for fixed
point real numbers of high precision.

%package -n texlive-fp-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1dsvn49719
Release:        0
Summary:        Documentation for texlive-fp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fp-doc
This package includes the documentation for texlive-fp

%post -n texlive-fp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fp/README
%{_texmfdistdir}/doc/latex/fp/documentation.pdf
%{_texmfdistdir}/doc/latex/fp/fp.tex

%files -n texlive-fp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fp/defpattern.sty
%{_texmfdistdir}/tex/latex/fp/fp-addons.sty
%{_texmfdistdir}/tex/latex/fp/fp-basic.sty
%{_texmfdistdir}/tex/latex/fp/fp-eqn.sty
%{_texmfdistdir}/tex/latex/fp/fp-eval.sty
%{_texmfdistdir}/tex/latex/fp/fp-exp.sty
%{_texmfdistdir}/tex/latex/fp/fp-pas.sty
%{_texmfdistdir}/tex/latex/fp/fp-random.sty
%{_texmfdistdir}/tex/latex/fp/fp-snap.sty
%{_texmfdistdir}/tex/latex/fp/fp-trigo.sty
%{_texmfdistdir}/tex/latex/fp/fp-upn.sty
%{_texmfdistdir}/tex/latex/fp/fp.sty
%{_texmfdistdir}/tex/latex/fp/lfp.sty
%{_texmfdistdir}/tex/plain/fp/fp.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fp-%{texlive_version}.%{texlive_noarch}.2.1dsvn49719-%{release}-zypper
%endif

%package -n texlive-fpl
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn54512
Release:        0
Summary:        SC and OsF fonts for URW Palladio L
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
Requires:       texlive-fpl-fonts >= %{texlive_version}
Recommends:     texlive-fpl-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source117:      fpl.tar.xz
Source118:      fpl.doc.tar.xz

%description -n texlive-fpl
The FPL Fonts provide a set of SC/OsF fonts for URW Palladio L
which are compatible with respect to metrics with the Palatino
SC/OsF fonts from Adobe. Note that it is not my aim to exactly
reproduce the outlines of the original Adobe fonts. The SC and
OsF in the FPL Fonts were designed with the glyphs from URW
Palladio L as starting point. For some glyphs (e.g. 'o') I got
the best result by scaling and boldening. For others (e.g. 'h')
shifting selected portions of the character gave more
satisfying results. All this was done using the free font
editor FontForge. The kerning data in these fonts comes from
Walter Schmidt's improved Palatino metrics. LaTeX use is
enabled by the mathpazo package, which is part of the psnfss
distribution.

%package -n texlive-fpl-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn54512
Release:        0
Summary:        Documentation for texlive-fpl
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fpl-doc
This package includes the documentation for texlive-fpl


%package -n texlive-fpl-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.003svn54512
Release:        0
Summary:        Severed fonts for texlive-fpl
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-fpl-fonts
The  separated fonts package for texlive-fpl
%post -n texlive-fpl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fpl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fpl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-fpl-fonts
%files -n texlive-fpl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/fpl/COPYING
%{_texmfdistdir}/doc/fonts/fpl/README

%files -n texlive-fpl
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/fpl/fplbij8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/fplbj8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/fplrc8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/fplrij8a.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplb9d-kern.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplbi9d-kern.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplrc9d-kern.afm
%{_texmfdistdir}/fonts/afm/public/fpl/pplri9d-kern.afm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fpl/fplbij8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplbij8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fpl/fplbj8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplbj8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fpl/fplrc8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplrc8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/fpl/fplrij8a.pfb
%{_texmfdistdir}/fonts/type1/public/fpl/fplrij8a.pfm

%files -n texlive-fpl-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-fpl
%{_datadir}/fontconfig/conf.avail/58-texlive-fpl.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fpl/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fpl/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-fpl/fonts.scale
%{_datadir}/fonts/texlive-fpl/fplbij8a.pfb
%{_datadir}/fonts/texlive-fpl/fplbj8a.pfb
%{_datadir}/fonts/texlive-fpl/fplrc8a.pfb
%{_datadir}/fonts/texlive-fpl/fplrij8a.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fpl-fonts-%{texlive_version}.%{texlive_noarch}.1.003svn54512-%{release}-zypper
%endif

%package -n texlive-fragmaster
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn26313
Release:        0
Summary:        Using psfrag with pdfLaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-fragmaster-bin >= %{texlive_version}
#!BuildIgnore: texlive-fragmaster-bin
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
Recommends:     texlive-fragmaster-doc >= %{texlive_version}
Requires:       perl(Cwd)
#!BuildIgnore:  perl(Cwd)
Requires:       perl(File::Temp)
#!BuildIgnore:  perl(File::Temp)
Requires:       perl(Pod::Usage)
#!BuildIgnore:  perl(Pod::Usage)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source119:      fragmaster.tar.xz
Source120:      fragmaster.doc.tar.xz

%description -n texlive-fragmaster
Fragmaster enables you to use psfrag with pdfLaTeX. It takes
EPS files and psfrag substitution definition files, and
produces PDF and EPS files with the substitutions included.

%package -n texlive-fragmaster-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn26313
Release:        0
Summary:        Documentation for texlive-fragmaster
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-fragmaster-doc:en;de)

%description -n texlive-fragmaster-doc
This package includes the documentation for texlive-fragmaster

%post -n texlive-fragmaster
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fragmaster 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fragmaster
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fragmaster-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/fragmaster/AUTHORS
%{_texmfdistdir}/doc/support/fragmaster/COPYING
%{_texmfdistdir}/doc/support/fragmaster/CREDITS
%{_texmfdistdir}/doc/support/fragmaster/Changes
%{_texmfdistdir}/doc/support/fragmaster/README
%{_texmfdistdir}/doc/support/fragmaster/README.de
%{_texmfdistdir}/doc/support/fragmaster/example/document.pdf
%{_texmfdistdir}/doc/support/fragmaster/example/document.ps
%{_texmfdistdir}/doc/support/fragmaster/example/document.tex
%{_texmfdistdir}/doc/support/fragmaster/example/parabel.eps
%{_texmfdistdir}/doc/support/fragmaster/example/parabel.pdf
%{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm
%{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm.eps
%{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm.gp
%{_texmfdistdir}/doc/support/fragmaster/example/parabel_fm.pdf
%{_texmfdistdir}/doc/support/fragmaster/fragmaster.pdf

%files -n texlive-fragmaster
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/fragmaster/fragmaster.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fragmaster-%{texlive_version}.%{texlive_noarch}.1.6svn26313-%{release}-zypper
%endif

%package -n texlive-fragments
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Fragments of LaTeX code
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
Recommends:     texlive-fragments-doc >= %{texlive_version}
Provides:       tex(checklab.tex)
Provides:       tex(overrightarrow.sty)
Provides:       tex(removefr.tex)
Provides:       tex(subscript.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source121:      fragments.tar.xz
Source122:      fragments.doc.tar.xz

%description -n texlive-fragments
A collection of fragments of LaTeX code, suitable for inclusion
in packages, or (possibly) in users' documents. Included are:
checklab, for modifying the label checking code at
\end{document}; overrightarrow, defining a doubled over-arrow
macro; removefr, for removing 'reset' relations between
counters; and subscript, defining a \textsubscript command.

%package -n texlive-fragments-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-fragments
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fragments-doc
This package includes the documentation for texlive-fragments

%post -n texlive-fragments
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fragments 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fragments
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fragments-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fragments/README

%files -n texlive-fragments
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fragments/checklab.tex
%{_texmfdistdir}/tex/latex/fragments/overrightarrow.sty
%{_texmfdistdir}/tex/latex/fragments/removefr.tex
%{_texmfdistdir}/tex/latex/fragments/subscript.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fragments-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-frame
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18312
Release:        0
Summary:        Framed boxes for Plain TeX
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
Recommends:     texlive-frame-doc >= %{texlive_version}
Provides:       tex(frame.sty)
Provides:       tex(frame.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source123:      frame.tar.xz
Source124:      frame.doc.tar.xz

%description -n texlive-frame
A jiffy file (taken from fancybox) for placing a frame around a
box of text. The macros also provide for typesetting an empty
box of given dimensions.

%package -n texlive-frame-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18312
Release:        0
Summary:        Documentation for texlive-frame
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-frame-doc
This package includes the documentation for texlive-frame

%post -n texlive-frame
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-frame 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-frame
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-frame-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/frame/Changes
%{_texmfdistdir}/doc/generic/frame/Makefile
%{_texmfdistdir}/doc/generic/frame/README
%{_texmfdistdir}/doc/generic/frame/frame-doc.pdf
%{_texmfdistdir}/doc/generic/frame/frame-doc.tex

%files -n texlive-frame
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/frame/frame.sty
%{_texmfdistdir}/tex/generic/frame/frame.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frame-%{texlive_version}.%{texlive_noarch}.1.0svn18312-%{release}-zypper
%endif

%package -n texlive-framed
Version:        %{texlive_version}.%{texlive_noarch}.0.0.96svn26789
Release:        0
Summary:        Framed or shaded regions that can break across pages
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
Recommends:     texlive-framed-doc >= %{texlive_version}
Provides:       tex(framed.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source125:      framed.tar.xz
Source126:      framed.doc.tar.xz

%description -n texlive-framed
The package creates three environments: framed, which puts an
ordinary frame box around the region, shaded, which shades the
region, and leftbar, which places a line at the left side. The
environments allow a break at their start (the \FrameCommand
enables creation of a title that is "attached" to the
environment); breaks are also allowed in the course of the
framed/shaded matter. There is also a command \MakeFramed to
make your own framed-style environments.

%package -n texlive-framed-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.96svn26789
Release:        0
Summary:        Documentation for texlive-framed
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-framed-doc
This package includes the documentation for texlive-framed

%post -n texlive-framed
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-framed 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-framed
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-framed-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/framed/framed.pdf
%{_texmfdistdir}/doc/latex/framed/framed.tex

%files -n texlive-framed
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/framed/framed.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-framed-%{texlive_version}.%{texlive_noarch}.0.0.96svn26789-%{release}-zypper
%endif

%package -n texlive-francais-bst
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn38922
Release:        0
Summary:        Bibliographies conforming to French typographic standards
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
Recommends:     texlive-francais-bst-doc >= %{texlive_version}
Provides:       tex(francaisbst.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source127:      francais-bst.tar.xz
Source128:      francais-bst.doc.tar.xz

%description -n texlive-francais-bst
The package provides bibliographies (in French) conforming to
the rules in "Guide de la communication ecrite" (Malo, M.,
Quebec Amerique, 1996. ISBN 978-2-8903-7875-9) The BibTeX
styles were generated using custom-bib and they are compatible
with natbib

%package -n texlive-francais-bst-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn38922
Release:        0
Summary:        Documentation for texlive-francais-bst
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-francais-bst-doc:fr)

%description -n texlive-francais-bst-doc
This package includes the documentation for texlive-francais-bst

%post -n texlive-francais-bst
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-francais-bst 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-francais-bst
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-francais-bst-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/francais-bst/README

%files -n texlive-francais-bst
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/francais-bst/francais.bst
%{_texmfdistdir}/bibtex/bst/francais-bst/francaissc.bst
%{_texmfdistdir}/tex/latex/francais-bst/francaisbst.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-francais-bst-%{texlive_version}.%{texlive_noarch}.1.1svn38922-%{release}-zypper
%endif

%package -n texlive-frankenstein
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A collection of LaTeX packages
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
Recommends:     texlive-frankenstein-doc >= %{texlive_version}
Provides:       tex(abbrevs.cfg)
Provides:       tex(abbrevs.sty)
Provides:       tex(achicago.sty)
Provides:       tex(attrib.sty)
Provides:       tex(blkcntrl.sty)
Provides:       tex(compsci.cfg)
Provides:       tex(compsci.sty)
Provides:       tex(dialogue.sty)
Provides:       tex(lips.sty)
Provides:       tex(moredefs.sty)
Provides:       tex(newclude.sty)
Provides:       tex(slemph.cfg)
Provides:       tex(slemph.sty)
Provides:       tex(titles.cfg)
Provides:       tex(titles.sty)
Requires:       tex(relsize.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source129:      frankenstein.tar.xz
Source130:      frankenstein.doc.tar.xz

%description -n texlive-frankenstein
Frankenstein is a bundle of LaTeX packages serving various
purposes and a BibTeX bibliography style. Descriptions are
given under the individual packages: abbrevs, achicago package,
achicago bibstyle, attrib, blkcntrl, compsci, dialogue, lips,
moredefs, newclude, slemph, titles.

%package -n texlive-frankenstein-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-frankenstein
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-frankenstein-doc
This package includes the documentation for texlive-frankenstein

%post -n texlive-frankenstein
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-frankenstein 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-frankenstein
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-frankenstein-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/frankenstein/ChangeLog
%{_texmfdistdir}/doc/latex/frankenstein/Frankenfile
%{_texmfdistdir}/doc/latex/frankenstein/INSTALL
%{_texmfdistdir}/doc/latex/frankenstein/README
%{_texmfdistdir}/doc/latex/frankenstein/abbrevs.pdf
%{_texmfdistdir}/doc/latex/frankenstein/abbrevs.tex
%{_texmfdistdir}/doc/latex/frankenstein/achicago-bst.pdf
%{_texmfdistdir}/doc/latex/frankenstein/achicago-bst.tex
%{_texmfdistdir}/doc/latex/frankenstein/achicago-bst.ver
%{_texmfdistdir}/doc/latex/frankenstein/achicago.bsq
%{_texmfdistdir}/doc/latex/frankenstein/achicago.pdf
%{_texmfdistdir}/doc/latex/frankenstein/achicago.tex
%{_texmfdistdir}/doc/latex/frankenstein/attrib.pdf
%{_texmfdistdir}/doc/latex/frankenstein/attrib.tex
%{_texmfdistdir}/doc/latex/frankenstein/blkcntrl.pdf
%{_texmfdistdir}/doc/latex/frankenstein/blkcntrl.tex
%{_texmfdistdir}/doc/latex/frankenstein/compsci.pdf
%{_texmfdistdir}/doc/latex/frankenstein/compsci.tex
%{_texmfdistdir}/doc/latex/frankenstein/dialogue.pdf
%{_texmfdistdir}/doc/latex/frankenstein/dialogue.tex
%{_texmfdistdir}/doc/latex/frankenstein/lips.pdf
%{_texmfdistdir}/doc/latex/frankenstein/lips.tex
%{_texmfdistdir}/doc/latex/frankenstein/moredefs.pdf
%{_texmfdistdir}/doc/latex/frankenstein/moredefs.tex
%{_texmfdistdir}/doc/latex/frankenstein/newclude.pdf
%{_texmfdistdir}/doc/latex/frankenstein/newclude.tex
%{_texmfdistdir}/doc/latex/frankenstein/slemph.pdf
%{_texmfdistdir}/doc/latex/frankenstein/slemph.tex
%{_texmfdistdir}/doc/latex/frankenstein/titles.pdf
%{_texmfdistdir}/doc/latex/frankenstein/titles.tex
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/README-unsupported
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.cfg
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.ins
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.pdf
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.sty
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/bits.tex
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.ins
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.pdf
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.sty
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/drama.tex
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex-test.tex
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.ins
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.pdf
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.sty
%{_texmfdistdir}/doc/latex/frankenstein/unsupported/includex.tex

%files -n texlive-frankenstein
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/frankenstein/frankenstein.bib
%{_texmfdistdir}/bibtex/bst/frankenstein/achicago.bst
%{_texmfdistdir}/tex/latex/frankenstein/abbrevs.cfg
%{_texmfdistdir}/tex/latex/frankenstein/abbrevs.stq
%{_texmfdistdir}/tex/latex/frankenstein/abbrevs.sty
%{_texmfdistdir}/tex/latex/frankenstein/achicago.stq
%{_texmfdistdir}/tex/latex/frankenstein/achicago.sty
%{_texmfdistdir}/tex/latex/frankenstein/allocate.sto
%{_texmfdistdir}/tex/latex/frankenstein/attrib.stq
%{_texmfdistdir}/tex/latex/frankenstein/attrib.sty
%{_texmfdistdir}/tex/latex/frankenstein/blkcntrl.stq
%{_texmfdistdir}/tex/latex/frankenstein/blkcntrl.sty
%{_texmfdistdir}/tex/latex/frankenstein/compsci.cfg
%{_texmfdistdir}/tex/latex/frankenstein/compsci.stq
%{_texmfdistdir}/tex/latex/frankenstein/compsci.sty
%{_texmfdistdir}/tex/latex/frankenstein/dialogue.stq
%{_texmfdistdir}/tex/latex/frankenstein/dialogue.sty
%{_texmfdistdir}/tex/latex/frankenstein/lips.stq
%{_texmfdistdir}/tex/latex/frankenstein/lips.sty
%{_texmfdistdir}/tex/latex/frankenstein/moredefs.stq
%{_texmfdistdir}/tex/latex/frankenstein/moredefs.sty
%{_texmfdistdir}/tex/latex/frankenstein/newclude.stq
%{_texmfdistdir}/tex/latex/frankenstein/newclude.sty
%{_texmfdistdir}/tex/latex/frankenstein/simple.sto
%{_texmfdistdir}/tex/latex/frankenstein/slemph.cfg
%{_texmfdistdir}/tex/latex/frankenstein/slemph.stq
%{_texmfdistdir}/tex/latex/frankenstein/slemph.sty
%{_texmfdistdir}/tex/latex/frankenstein/tag.sto
%{_texmfdistdir}/tex/latex/frankenstein/titles.cfg
%{_texmfdistdir}/tex/latex/frankenstein/titles.stq
%{_texmfdistdir}/tex/latex/frankenstein/titles.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frankenstein-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-frcursive
Version:        %{texlive_version}.%{texlive_noarch}.svn24559
Release:        0
Summary:        French cursive hand fonts
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
Requires:       texlive-frcursive-fonts >= %{texlive_version}
Recommends:     texlive-frcursive-doc >= %{texlive_version}
Provides:       tex(frca10.tfm)
Provides:       tex(frcbx10.tfm)
Provides:       tex(frcbx14.tfm)
Provides:       tex(frcbx6.tfm)
Provides:       tex(frcc10.tfm)
Provides:       tex(frcc14.tfm)
Provides:       tex(frcc6.tfm)
Provides:       tex(frcf10.tfm)
Provides:       tex(frcf14.tfm)
Provides:       tex(frcf6.tfm)
Provides:       tex(frcr10.tfm)
Provides:       tex(frcr14.tfm)
Provides:       tex(frcr6.tfm)
Provides:       tex(frcsl10.tfm)
Provides:       tex(frcsl14.tfm)
Provides:       tex(frcsl6.tfm)
Provides:       tex(frcslbx10.tfm)
Provides:       tex(frcslbx14.tfm)
Provides:       tex(frcslbx6.tfm)
Provides:       tex(frcslc10.tfm)
Provides:       tex(frcslc14.tfm)
Provides:       tex(frcslc6.tfm)
Provides:       tex(frcursive.map)
Provides:       tex(frcursive.sty)
Provides:       tex(frcw10.tfm)
Provides:       tex(ot1frc.fd)
Provides:       tex(t1frc.fd)
Requires:       tex(fontenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source131:      frcursive.tar.xz
Source132:      frcursive.doc.tar.xz

%description -n texlive-frcursive
A hand-writing font in the style of the French academic
running-hand. The font was written in Metafont and has been
converted to Adobe Type 1 format. LaTeX support (NFFS fd files,
and a package) and font maps are provided.

%package -n texlive-frcursive-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn24559
Release:        0
Summary:        Documentation for texlive-frcursive
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-frcursive-doc
This package includes the documentation for texlive-frcursive


%package -n texlive-frcursive-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn24559
Release:        0
Summary:        Severed fonts for texlive-frcursive
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-frcursive-fonts
The  separated fonts package for texlive-frcursive
%post -n texlive-frcursive
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap frcursive.map' >> /var/run/texlive/run-updmap

%postun -n texlive-frcursive 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap frcursive.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-frcursive
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-frcursive-fonts
%files -n texlive-frcursive-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/frcursive/COPYING
%{_texmfdistdir}/doc/fonts/frcursive/README
%{_texmfdistdir}/doc/fonts/frcursive/frcursive.pdf

%files -n texlive-frcursive
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/frcursive/frcursive.map
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslc10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslc14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslc6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcursive.mf
%{_texmfdistdir}/fonts/tfm/public/frcursive/frca10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslc10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslc14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslc6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcw10.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frca10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcf10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcf14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcf6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcr10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcr14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcr6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcsl14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcsl6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcslbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcslbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcslbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcslc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcslc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcslc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/frcursive/frcw10.pfb
%{_texmfdistdir}/tex/latex/frcursive/frcursive.sty
%{_texmfdistdir}/tex/latex/frcursive/ot1frc.fd
%{_texmfdistdir}/tex/latex/frcursive/t1frc.fd

%files -n texlive-frcursive-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-frcursive
%{_datadir}/fontconfig/conf.avail/58-texlive-frcursive.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-frcursive/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-frcursive/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-frcursive/fonts.scale
%{_datadir}/fonts/texlive-frcursive/frca10.pfb
%{_datadir}/fonts/texlive-frcursive/frcbx10.pfb
%{_datadir}/fonts/texlive-frcursive/frcbx14.pfb
%{_datadir}/fonts/texlive-frcursive/frcbx6.pfb
%{_datadir}/fonts/texlive-frcursive/frcc10.pfb
%{_datadir}/fonts/texlive-frcursive/frcc14.pfb
%{_datadir}/fonts/texlive-frcursive/frcc6.pfb
%{_datadir}/fonts/texlive-frcursive/frcf10.pfb
%{_datadir}/fonts/texlive-frcursive/frcf14.pfb
%{_datadir}/fonts/texlive-frcursive/frcf6.pfb
%{_datadir}/fonts/texlive-frcursive/frcr10.pfb
%{_datadir}/fonts/texlive-frcursive/frcr14.pfb
%{_datadir}/fonts/texlive-frcursive/frcr6.pfb
%{_datadir}/fonts/texlive-frcursive/frcsl10.pfb
%{_datadir}/fonts/texlive-frcursive/frcsl14.pfb
%{_datadir}/fonts/texlive-frcursive/frcsl6.pfb
%{_datadir}/fonts/texlive-frcursive/frcslbx10.pfb
%{_datadir}/fonts/texlive-frcursive/frcslbx14.pfb
%{_datadir}/fonts/texlive-frcursive/frcslbx6.pfb
%{_datadir}/fonts/texlive-frcursive/frcslc10.pfb
%{_datadir}/fonts/texlive-frcursive/frcslc14.pfb
%{_datadir}/fonts/texlive-frcursive/frcslc6.pfb
%{_datadir}/fonts/texlive-frcursive/frcw10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frcursive-fonts-%{texlive_version}.%{texlive_noarch}.svn24559-%{release}-zypper
%endif

%package -n texlive-frederika2016
Version:        %{texlive_version}.%{texlive_noarch}.1.000_2016_initial_releasesvn42157
Release:        0
Summary:        An OpenType Greek calligraphy font
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-frederika2016-fonts >= %{texlive_version}
Recommends:     texlive-frederika2016-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source133:      frederika2016.tar.xz
Source134:      frederika2016.doc.tar.xz

%description -n texlive-frederika2016
Frederika2016 is an attempt to digitize Hermann Zapf's
Frederika font. The font is the Greek companion of Virtuosa by
the same designer. This font is a calligraphy font and this is
an initial release.

%package -n texlive-frederika2016-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.000_2016_initial_releasesvn42157
Release:        0
Summary:        Documentation for texlive-frederika2016
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-frederika2016-doc
This package includes the documentation for texlive-frederika2016


%package -n texlive-frederika2016-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.000_2016_initial_releasesvn42157
Release:        0
Summary:        Severed fonts for texlive-frederika2016
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-frederika2016-fonts
The  separated fonts package for texlive-frederika2016
%post -n texlive-frederika2016
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-frederika2016 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-frederika2016
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-frederika2016-fonts
%files -n texlive-frederika2016-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/frederika2016/FontInfo.pdf
%{_texmfdistdir}/doc/fonts/frederika2016/README
%{_texmfdistdir}/doc/fonts/frederika2016/testpol.pdf
%{_texmfdistdir}/doc/fonts/frederika2016/testpol.tex

%files -n texlive-frederika2016
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/frederika2016/Frederika2016.otf

%files -n texlive-frederika2016-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-frederika2016
%{_datadir}/fontconfig/conf.avail/58-texlive-frederika2016.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-frederika2016/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-frederika2016/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-frederika2016/fonts.scale
%{_datadir}/fonts/texlive-frederika2016/Frederika2016.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frederika2016-fonts-%{texlive_version}.%{texlive_noarch}.1.000_2016_initial_releasesvn42157-%{release}-zypper
%endif

%package -n texlive-frege
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn27417
Release:        0
Summary:        Typeset fregean Begriffsschrift
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
Recommends:     texlive-frege-doc >= %{texlive_version}
Provides:       tex(frege.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bguq.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source135:      frege.tar.xz
Source136:      frege.doc.tar.xz

%description -n texlive-frege
The package defines a number of new commands for typesetting
fregean Begriffsschrift in LaTeX. It is loosely based on the
package begriff, and offers a number of improvements including
better relative lengths of the content stroke with respect to
other strokes, content strokes that point at the middle of
lines rather than the bottom, a greater width for the assertion
stroke as compared to the content stroke, a more intuitive
structure for the conditional, greater care taken to allow for
the linewidth in the spacing of formulas.

%package -n texlive-frege-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn27417
Release:        0
Summary:        Documentation for texlive-frege
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-frege-doc
This package includes the documentation for texlive-frege

%post -n texlive-frege
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-frege 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-frege
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-frege-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/frege/GNU.txt
%{_texmfdistdir}/doc/latex/frege/INSTALL
%{_texmfdistdir}/doc/latex/frege/README
%{_texmfdistdir}/doc/latex/frege/frege.pdf
%{_texmfdistdir}/doc/latex/frege/frege.tex

%files -n texlive-frege
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/frege/frege.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frege-%{texlive_version}.%{texlive_noarch}.1.3svn27417-%{release}-zypper
%endif

%package -n texlive-frenchmath
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51192
Release:        0
Summary:        Typesetting mathematics according to French rules
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
Recommends:     texlive-frenchmath-doc >= %{texlive_version}
Provides:       tex(frenchmath.sty)
Requires:       tex(amsopn.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(icomma.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source137:      frenchmath.tar.xz
Source138:      frenchmath.doc.tar.xz

%description -n texlive-frenchmath
The package provides capital letters in upright shape for
mathematical mode according to French rule (package option),
correct spacing after commas and before a semicolon in math
mode, some useful macros and aliases for symbols used in
France: \infeg, \supeg, \paral, ... several macros for writing
french operator names like pgcd, ppcm, Card, rg, Vect, ...

%package -n texlive-frenchmath-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51192
Release:        0
Summary:        Documentation for texlive-frenchmath
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-frenchmath-doc:fr)

%description -n texlive-frenchmath-doc
This package includes the documentation for texlive-frenchmath

%post -n texlive-frenchmath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-frenchmath 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-frenchmath
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-frenchmath-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/frenchmath/README.md
%{_texmfdistdir}/doc/latex/frenchmath/frenchmath.pdf

%files -n texlive-frenchmath
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/frenchmath/frenchmath.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frenchmath-%{texlive_version}.%{texlive_noarch}.1.4svn51192-%{release}-zypper
%endif

%package -n texlive-frletter
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Typeset letters in the French style
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
Recommends:     texlive-frletter-doc >= %{texlive_version}
Provides:       tex(frletter.cls)
Requires:       tex(letter.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source139:      frletter.tar.xz
Source140:      frletter.doc.tar.xz

%description -n texlive-frletter
A small class for typesetting letters in France. No assumption
is made about the language in use. The class represents a small
modification of the beletter class, which is itself a
modification of the standard LaTeX letter class.

%package -n texlive-frletter-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-frletter
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-frletter-doc
This package includes the documentation for texlive-frletter

%post -n texlive-frletter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-frletter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-frletter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-frletter-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/frletter/README

%files -n texlive-frletter
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/frletter/frletter.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frletter-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-frontespizio
Version:        %{texlive_version}.%{texlive_noarch}.1.4asvn24054
Release:        0
Summary:        Create a frontispiece for Italian theses
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
Recommends:     texlive-frontespizio-doc >= %{texlive_version}
Provides:       tex(frontespizio.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source141:      frontespizio.tar.xz
Source142:      frontespizio.doc.tar.xz

%description -n texlive-frontespizio
Typesetting a frontispiece independently of the layout of the
main document is difficult. This package provides a solution by
producing an auxiliary TeX file to be typeset on its own and
the result is automatically included at the next run. The
markup necessary for the frontispiece is written in the main
document in a frontespizio environment. Documentation is mainly
in Italian, as the style is probably apt only to theses in
Italy.

%package -n texlive-frontespizio-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4asvn24054
Release:        0
Summary:        Documentation for texlive-frontespizio
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-frontespizio-doc:it)

%description -n texlive-frontespizio-doc
This package includes the documentation for texlive-frontespizio

%post -n texlive-frontespizio
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-frontespizio 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-frontespizio
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-frontespizio-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/frontespizio/README
%{_texmfdistdir}/doc/latex/frontespizio/examplea.pdf
%{_texmfdistdir}/doc/latex/frontespizio/examplea.tex
%{_texmfdistdir}/doc/latex/frontespizio/exampleasuf.pdf
%{_texmfdistdir}/doc/latex/frontespizio/exampleasuf.tex
%{_texmfdistdir}/doc/latex/frontespizio/exampleb.pdf
%{_texmfdistdir}/doc/latex/frontespizio/exampleb.tex
%{_texmfdistdir}/doc/latex/frontespizio/examplec.pdf
%{_texmfdistdir}/doc/latex/frontespizio/examplec.tex
%{_texmfdistdir}/doc/latex/frontespizio/exampled.pdf
%{_texmfdistdir}/doc/latex/frontespizio/exampled.tex
%{_texmfdistdir}/doc/latex/frontespizio/examplee.pdf
%{_texmfdistdir}/doc/latex/frontespizio/examplee.tex
%{_texmfdistdir}/doc/latex/frontespizio/fakelogo.mp
%{_texmfdistdir}/doc/latex/frontespizio/fakelogo.pdf
%{_texmfdistdir}/doc/latex/frontespizio/frontespizio.pdf

%files -n texlive-frontespizio
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/frontespizio/frontespizio.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-frontespizio-%{texlive_version}.%{texlive_noarch}.1.4asvn24054-%{release}-zypper
%endif

%package -n texlive-ftc-notebook
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn50043
Release:        0
Summary:        Typeset FIRST Tech Challenge (FTC) notebooks
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
Recommends:     texlive-ftc-notebook-doc >= %{texlive_version}
Provides:       tex(ftc-notebook.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(array.sty)
Requires:       tex(arrayjobx.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(datetime.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenx.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(mfirstuc.sty)
Requires:       tex(multido.sty)
Requires:       tex(multirow.sty)
Requires:       tex(needspace.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(paralist.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(suffix.sty)
Requires:       tex(t1enc.sty)
Requires:       tex(tabu.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(textpos.sty)
Requires:       tex(tikz.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source143:      ftc-notebook.tar.xz
Source144:      ftc-notebook.doc.tar.xz

%description -n texlive-ftc-notebook
This LaTeX package will greatly simplify filling entries for
your FIRST Tech Challenge (FTC) engineering or outreach
notebook. We developed this package to support most frequently
used constructs encountered in an FTC notebook: meetings,
tasks, decisions with pros and cons, tables, figures with
explanations, team stories and bios, and more. We developed
this package during the 2018-2019 season and are using it for
our engineering notebook. Team Robocracy is sharing this style
in the spirit of coopertition.

%package -n texlive-ftc-notebook-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn50043
Release:        0
Summary:        Documentation for texlive-ftc-notebook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ftc-notebook-doc
This package includes the documentation for texlive-ftc-notebook

%post -n texlive-ftc-notebook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ftc-notebook 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ftc-notebook
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ftc-notebook-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ftc-notebook/README.md
%{_texmfdistdir}/doc/latex/ftc-notebook/example-notebook.pdf
%{_texmfdistdir}/doc/latex/ftc-notebook/example-notebook.tex
%{_texmfdistdir}/doc/latex/ftc-notebook/ftc-notebook.pdf
%{_texmfdistdir}/doc/latex/ftc-notebook/ftc-notebook.tex
%{_texmfdistdir}/doc/latex/ftc-notebook/newmeeting.sh
%{_texmfdistdir}/doc/latex/ftc-notebook/src/aug19.tex
%{_texmfdistdir}/doc/latex/ftc-notebook/src/aug19/build-pict.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/aug19/chassi-cad.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/aug19/encoder-cad.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/aug19/first-build.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/aug19/first-cad.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/aug19/second-cad.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/bio.tex
%{_texmfdistdir}/doc/latex/ftc-notebook/src/bio/mitsiki.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/images/aug18.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/images/logo.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/images/robocracy2018.jpg
%{_texmfdistdir}/doc/latex/ftc-notebook/src/story.tex

%files -n texlive-ftc-notebook
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ftc-notebook/ftc-notebook.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ftc-notebook-%{texlive_version}.%{texlive_noarch}.1.1svn50043-%{release}-zypper
%endif

%package -n texlive-ftcap
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn17275
Release:        0
Summary:        Allows \caption at the beginning of a table-environment
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
Recommends:     texlive-ftcap-doc >= %{texlive_version}
Provides:       tex(ftcap.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source145:      ftcap.tar.xz
Source146:      ftcap.doc.tar.xz

%description -n texlive-ftcap
For several reasons a \caption may be desirable at the top of a
table environment. This package changes the table environment
such that \abovecaptionskip and \belowcaptionskip are swapped.
The package should also work with a non-standard table
environment.

%package -n texlive-ftcap-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn17275
Release:        0
Summary:        Documentation for texlive-ftcap
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ftcap-doc
This package includes the documentation for texlive-ftcap

%post -n texlive-ftcap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ftcap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ftcap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ftcap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ftcap/ftcap.pdf
%{_texmfdistdir}/doc/latex/ftcap/ftcap.tex

%files -n texlive-ftcap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ftcap/ftcap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ftcap-%{texlive_version}.%{texlive_noarch}.1.4svn17275-%{release}-zypper
%endif

%package -n texlive-ftnxtra
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn29652
Release:        0
Summary:        Extend the applicability of the \footnote command
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
Recommends:     texlive-ftnxtra-doc >= %{texlive_version}
Provides:       tex(ftnxtra.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source147:      ftnxtra.tar.xz
Source148:      ftnxtra.doc.tar.xz

%description -n texlive-ftnxtra
The package treats footnotes in \caption, the tabular
environment, and \chapter and other \section-like commands.

%package -n texlive-ftnxtra-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn29652
Release:        0
Summary:        Documentation for texlive-ftnxtra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ftnxtra-doc
This package includes the documentation for texlive-ftnxtra

%post -n texlive-ftnxtra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ftnxtra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ftnxtra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ftnxtra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ftnxtra/README
%{_texmfdistdir}/doc/latex/ftnxtra/ftnxtra.pdf
%{_texmfdistdir}/doc/latex/ftnxtra/ftnxtra.tex

%files -n texlive-ftnxtra
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ftnxtra/ftnxtra.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ftnxtra-%{texlive_version}.%{texlive_noarch}.0.0.1svn29652-%{release}-zypper
%endif

%package -n texlive-fullblck
Version:        %{texlive_version}.%{texlive_noarch}.1.03svn25434
Release:        0
Summary:        Left-blocking for letter class
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
Recommends:     texlive-fullblck-doc >= %{texlive_version}
Provides:       tex(fullblck.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source149:      fullblck.tar.xz
Source150:      fullblck.doc.tar.xz

%description -n texlive-fullblck
Used with the letter documentclass to set the letter in a
fullblock style (everything at the left margin).

%package -n texlive-fullblck-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.03svn25434
Release:        0
Summary:        Documentation for texlive-fullblck
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fullblck-doc
This package includes the documentation for texlive-fullblck

%post -n texlive-fullblck
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fullblck 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fullblck
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fullblck-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fullblck/README
%{_texmfdistdir}/doc/latex/fullblck/fullblck.pdf

%files -n texlive-fullblck
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fullblck/fullblck.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fullblck-%{texlive_version}.%{texlive_noarch}.1.03svn25434-%{release}-zypper
%endif

%package -n texlive-fullminipage
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn34545
Release:        0
Summary:        Minipage spanning a complete page
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
Recommends:     texlive-fullminipage-doc >= %{texlive_version}
Provides:       tex(fullminipage.sty)
Requires:       tex(color.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source151:      fullminipage.tar.xz
Source152:      fullminipage.doc.tar.xz

%description -n texlive-fullminipage
This package provides the environment fullminipage, which
generates a minipage spanning a new, complete page with page
style empty. The environment provides options to set margins
around the minipage and configure the background.

%package -n texlive-fullminipage-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn34545
Release:        0
Summary:        Documentation for texlive-fullminipage
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fullminipage-doc
This package includes the documentation for texlive-fullminipage

%post -n texlive-fullminipage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fullminipage 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fullminipage
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fullminipage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fullminipage/COPYING
%{_texmfdistdir}/doc/latex/fullminipage/Makefile
%{_texmfdistdir}/doc/latex/fullminipage/README
%{_texmfdistdir}/doc/latex/fullminipage/fullminipage.pdf
%{_texmfdistdir}/doc/latex/fullminipage/fullminipage_test.pdf
%{_texmfdistdir}/doc/latex/fullminipage/fullminipage_test.tex

%files -n texlive-fullminipage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fullminipage/fullminipage.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fullminipage-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn34545-%{release}-zypper
%endif

%package -n texlive-fullwidth
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn24684
Release:        0
Summary:        Adjust margins of text block
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
Recommends:     texlive-fullwidth-doc >= %{texlive_version}
Provides:       tex(fullwidth.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(zref-abspage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source153:      fullwidth.tar.xz
Source154:      fullwidth.doc.tar.xz

%description -n texlive-fullwidth
The package provides the environment fullwidth, which sets the
left and right margins in a simple way. There is no constraint
about page breaks; if you are using the twoside mode, you can
set the inner and outer margins to avoid the effects of the
different margins.

%package -n texlive-fullwidth-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn24684
Release:        0
Summary:        Documentation for texlive-fullwidth
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fullwidth-doc
This package includes the documentation for texlive-fullwidth

%post -n texlive-fullwidth
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fullwidth 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fullwidth
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fullwidth-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fullwidth/README
%{_texmfdistdir}/doc/latex/fullwidth/fullwidth-test.pdf
%{_texmfdistdir}/doc/latex/fullwidth/fullwidth-test.tex
%{_texmfdistdir}/doc/latex/fullwidth/fullwidth.pdf
%{_texmfdistdir}/doc/latex/fullwidth/fullwidth.tex

%files -n texlive-fullwidth
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fullwidth/fullwidth.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fullwidth-%{texlive_version}.%{texlive_noarch}.0.0.1svn24684-%{release}-zypper
%endif

%package -n texlive-functan
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Macros for functional analysis and PDE theory
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
Recommends:     texlive-functan-doc >= %{texlive_version}
Provides:       tex(functan.sty)
Requires:       tex(amsmath.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source155:      functan.tar.xz
Source156:      functan.doc.tar.xz

%description -n texlive-functan
This package provides a convenient and coherent way to deal
with name of functional spaces (mainly Sobolev spaces) in
functional analysis and PDE theory. It also provides a set of
macros for dealing with norms, scalar products and convergence
with some object oriented flavor (it gives the possibility to
override the standard behavior of norms, ...).

%package -n texlive-functan-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-functan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-functan-doc
This package includes the documentation for texlive-functan

%post -n texlive-functan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-functan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-functan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-functan-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/functan/README
%{_texmfdistdir}/doc/latex/functan/functan.pdf

%files -n texlive-functan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/functan/functan.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-functan-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-fundus-calligra
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn26018
Release:        0
Summary:        Support for the calligra font in LaTeX documents
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
Recommends:     texlive-fundus-calligra-doc >= %{texlive_version}
Provides:       tex(calligra.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source157:      fundus-calligra.tar.xz
Source158:      fundus-calligra.doc.tar.xz

%description -n texlive-fundus-calligra
The package offers support for the calligra handwriting font,
in LaTeX documents. The package is part of the fundus bundle.

%package -n texlive-fundus-calligra-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn26018
Release:        0
Summary:        Documentation for texlive-fundus-calligra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fundus-calligra-doc
This package includes the documentation for texlive-fundus-calligra

%post -n texlive-fundus-calligra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fundus-calligra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fundus-calligra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fundus-calligra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fundus-calligra/calligra.pdf

%files -n texlive-fundus-calligra
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fundus-calligra/calligra.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fundus-calligra-%{texlive_version}.%{texlive_noarch}.1.2svn26018-%{release}-zypper
%endif

%package -n texlive-fundus-cyr
Version:        %{texlive_version}.%{texlive_noarch}.svn26019
Release:        0
Summary:        Support for Washington University Cyrillic fonts
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
Provides:       tex(cyr.sty)
Requires:       tex(cyracc.def)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source159:      fundus-cyr.tar.xz

%description -n texlive-fundus-cyr
The package supports the use of the Washington Cyrillic fonts
with LaTeX (Note that standard LaTeX has support, too, as
encoding OT2). The package is distributed as part of the fundus
bundle.
%post -n texlive-fundus-cyr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fundus-cyr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fundus-cyr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fundus-cyr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fundus-cyr/cyr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fundus-cyr-%{texlive_version}.%{texlive_noarch}.svn26019-%{release}-zypper
%endif

%package -n texlive-fundus-sueterlin
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn26030
Release:        0
Summary:        Sutterlin
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
Recommends:     texlive-fundus-sueterlin-doc >= %{texlive_version}
Provides:       tex(suetterl.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source160:      fundus-sueterlin.tar.xz
Source161:      fundus-sueterlin.doc.tar.xz

%description -n texlive-fundus-sueterlin
The package supports use, in LaTeX, of the Metafont emulation
of the Sueterlin handwriting fonts The package is distributed
as part of the fundus bundle..

%package -n texlive-fundus-sueterlin-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn26030
Release:        0
Summary:        Documentation for texlive-fundus-sueterlin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fundus-sueterlin-doc
This package includes the documentation for texlive-fundus-sueterlin

%post -n texlive-fundus-sueterlin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fundus-sueterlin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fundus-sueterlin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fundus-sueterlin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fundus-sueterlin/suetterl.pdf

%files -n texlive-fundus-sueterlin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fundus-sueterlin/suetterl.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fundus-sueterlin-%{texlive_version}.%{texlive_noarch}.1.2svn26030-%{release}-zypper
%endif

%package -n texlive-fvextra
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn49947
Release:        0
Summary:        Extensions and patches for fancyvrb
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
Recommends:     texlive-fvextra-doc >= %{texlive_version}
Provides:       tex(fvextra.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lineno.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(upquote.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source162:      fvextra.tar.xz
Source163:      fvextra.doc.tar.xz

%description -n texlive-fvextra
fvextra provides several extensions to fancyvrb, including
automatic line breaking and improved math mode. It also patches
some fancyvrb internals. Parts of fvextra were originally
developed as part of pythontex and minted.

%package -n texlive-fvextra-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn49947
Release:        0
Summary:        Documentation for texlive-fvextra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fvextra-doc
This package includes the documentation for texlive-fvextra

%post -n texlive-fvextra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fvextra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fvextra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fvextra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fvextra/README
%{_texmfdistdir}/doc/latex/fvextra/fvextra.pdf

%files -n texlive-fvextra
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fvextra/fvextra.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fvextra-%{texlive_version}.%{texlive_noarch}.1.4svn49947-%{release}-zypper
%endif

%package -n texlive-fwlw
Version:        %{texlive_version}.%{texlive_noarch}.svn29803
Release:        0
Summary:        Get first and last words of a page
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
Recommends:     texlive-fwlw-doc >= %{texlive_version}
Provides:       tex(fwlw.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source164:      fwlw.tar.xz
Source165:      fwlw.doc.tar.xz

%description -n texlive-fwlw
The package extracts the first and last words of a page,
together with the first word of the next page, just before the
page is formed into the object to print. The package defines a
couple of page styles that use the words that have been
extracted.

%package -n texlive-fwlw-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn29803
Release:        0
Summary:        Documentation for texlive-fwlw
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-fwlw-doc
This package includes the documentation for texlive-fwlw

%post -n texlive-fwlw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-fwlw 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-fwlw
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-fwlw-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/fwlw/README
%{_texmfdistdir}/doc/latex/fwlw/fwlw.pdf
%{_texmfdistdir}/doc/latex/fwlw/fwlw.tex

%files -n texlive-fwlw
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/fwlw/fwlw.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-fwlw-%{texlive_version}.%{texlive_noarch}.svn29803-%{release}-zypper
%endif

%package -n texlive-g-brief
Version:        %{texlive_version}.%{texlive_noarch}.4.0.3svn50415
Release:        0
Summary:        Letter document class
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
Recommends:     texlive-g-brief-doc >= %{texlive_version}
Provides:       tex(g-brief.cls)
Provides:       tex(g-brief.sty)
Provides:       tex(g-brief2.cls)
Provides:       tex(g-brief2.sty)
Requires:       tex(babel.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(letter.cls)
Requires:       tex(marvosym.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source166:      g-brief.tar.xz
Source167:      g-brief.doc.tar.xz

%description -n texlive-g-brief
Designed for formatting formless letters in German; can also be
used for English (by those who can read the documentation).
There are LaTeX 2.09 documentstyle and LaTeX 2e class files for
both an 'old' and a 'new' version of g-brief.

%package -n texlive-g-brief-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.0.3svn50415
Release:        0
Summary:        Documentation for texlive-g-brief
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-g-brief-doc:de)

%description -n texlive-g-brief-doc
This package includes the documentation for texlive-g-brief

%post -n texlive-g-brief
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-g-brief 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-g-brief
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-g-brief-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/g-brief/README
%{_texmfdistdir}/doc/latex/g-brief/beispiel.pdf
%{_texmfdistdir}/doc/latex/g-brief/beispiel.tex
%{_texmfdistdir}/doc/latex/g-brief/beispiel2.pdf
%{_texmfdistdir}/doc/latex/g-brief/beispiel2.tex
%{_texmfdistdir}/doc/latex/g-brief/g-brief.pdf

%files -n texlive-g-brief
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/g-brief/g-brief.cls
%{_texmfdistdir}/tex/latex/g-brief/g-brief.sty
%{_texmfdistdir}/tex/latex/g-brief/g-brief2.cls
%{_texmfdistdir}/tex/latex/g-brief/g-brief2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-g-brief-%{texlive_version}.%{texlive_noarch}.4.0.3svn50415-%{release}-zypper
%endif

%package -n texlive-gaceta
Version:        %{texlive_version}.%{texlive_noarch}.1.06svn15878
Release:        0
Summary:        A class to typeset La Gaceta de la RSME
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
Recommends:     texlive-gaceta-doc >= %{texlive_version}
Provides:       tex(gaceta.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source168:      gaceta.tar.xz
Source169:      gaceta.doc.tar.xz

%description -n texlive-gaceta
The class will typeset papers for <<La Gaceta de la Real
Sociedad Matematica Espanola>>.

%package -n texlive-gaceta-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.06svn15878
Release:        0
Summary:        Documentation for texlive-gaceta
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-gaceta-doc:es)

%description -n texlive-gaceta-doc
This package includes the documentation for texlive-gaceta

%post -n texlive-gaceta
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gaceta 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gaceta
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gaceta-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gaceta/README
%{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-de-seccion.pdf
%{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-de-seccion.tex
%{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-suelto.pdf
%{_texmfdistdir}/doc/latex/gaceta/plantilla-articulo-suelto.tex

%files -n texlive-gaceta
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gaceta/gaceta.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gaceta-%{texlive_version}.%{texlive_noarch}.1.06svn15878-%{release}-zypper
%endif

%package -n texlive-galois
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Typeset Galois connections
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
Recommends:     texlive-galois-doc >= %{texlive_version}
Provides:       tex(galois.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source170:      galois.tar.xz
Source171:      galois.doc.tar.xz

%description -n texlive-galois
The package deals with connections in two-dimensional style,
optionally in colour.

%package -n texlive-galois-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Documentation for texlive-galois
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-galois-doc
This package includes the documentation for texlive-galois

%post -n texlive-galois
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-galois 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-galois
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-galois-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/galois/README
%{_texmfdistdir}/doc/latex/galois/galois.pdf

%files -n texlive-galois
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/galois/galois.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-galois-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif

%package -n texlive-gamebook
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn24714
Release:        0
Summary:        Typeset gamebooks and other interactive novels
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
Recommends:     texlive-gamebook-doc >= %{texlive_version}
Provides:       tex(gamebook.sty)
Requires:       tex(draftwatermark.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(extramarks.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(prelim2e.sty)
Requires:       tex(scrtime.sty)
Requires:       tex(titlesec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source172:      gamebook.tar.xz
Source173:      gamebook.doc.tar.xz

%description -n texlive-gamebook
This package provides the means in order to lay-out gamebooks
with LaTeX. A simple gamebook example is included with the
package, and acts as a tutorial.

%package -n texlive-gamebook-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn24714
Release:        0
Summary:        Documentation for texlive-gamebook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gamebook-doc
This package includes the documentation for texlive-gamebook

%post -n texlive-gamebook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gamebook 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gamebook
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gamebook-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gamebook/README
%{_texmfdistdir}/doc/latex/gamebook/gamebook-example.pdf
%{_texmfdistdir}/doc/latex/gamebook/gamebook-example.tex
%{_texmfdistdir}/doc/latex/gamebook/gamebook.pdf
%{_texmfdistdir}/doc/latex/gamebook/lppl.txt

%files -n texlive-gamebook
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gamebook/gamebook.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gamebook-%{texlive_version}.%{texlive_noarch}.1.0svn24714-%{release}-zypper
%endif

%package -n texlive-gammas
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn50012
Release:        0
Summary:        Template for the GAMM Archive for Students
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
Recommends:     texlive-gammas-doc >= %{texlive_version}
Provides:       tex(gammas.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(anyfontsize.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fourier.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(lineno.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(microtype.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(scrartcl.cls)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source174:      gammas.tar.xz
Source175:      gammas.doc.tar.xz

%description -n texlive-gammas
This is the official document class for typesetting journal
articles for GAMM Archive for Students (GAMMAS), the
open-access online yournal run by the GAMM Juniors.

%package -n texlive-gammas-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn50012
Release:        0
Summary:        Documentation for texlive-gammas
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gammas-doc
This package includes the documentation for texlive-gammas

%post -n texlive-gammas
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gammas 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gammas
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gammas-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gammas/README
%{_texmfdistdir}/doc/latex/gammas/example_bibliography.bib
%{_texmfdistdir}/doc/latex/gammas/gammas_template.tex

%files -n texlive-gammas
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/gammas/gammas.bst
%{_texmfdistdir}/tex/latex/gammas/gammas.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gammas-%{texlive_version}.%{texlive_noarch}.1.0svn50012-%{release}-zypper
%endif

%package -n texlive-garamond-libre
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51703
Release:        0
Summary:        The Garamond Libre font face
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
Requires:       texlive-garamond-libre-fonts >= %{texlive_version}
Recommends:     texlive-garamond-libre-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source176:      garamond-libre.tar.xz
Source177:      garamond-libre.doc.tar.xz

%description -n texlive-garamond-libre
Garamond Libre is a free and open-source old-style font family.
It is a "true Garamond," i.e., it is based off the designs of
16th-century French engraver Claude Garamond (also spelled
Garamont). The Roman design is Garamond's; the italics are from
a design by Robert Granjon. The upright Greek font is after a
design by Firmin Didot; the "italic" Greek font is after a
design by Alexander Wilson. The font family includes support
for Latin, Greek (monotonic and polytonic) and Cyrillic
scripts, as well as small capitals, old-style figures, superior
and inferior figures, historical ligatures, Byzantine musical
symbols, the IPA and swash capitals. Currently, regular, italic
and bold fonts are provided; there is no set timeframe for the
completion of a bold italic. The fonts are provided in OpenType
format, and are intended to be used with LuaLaTeX or XeLaTeX
via fontspec.

%package -n texlive-garamond-libre-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51703
Release:        0
Summary:        Documentation for texlive-garamond-libre
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-garamond-libre-doc
This package includes the documentation for texlive-garamond-libre


%package -n texlive-garamond-libre-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51703
Release:        0
Summary:        Severed fonts for texlive-garamond-libre
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-garamond-libre-fonts
The  separated fonts package for texlive-garamond-libre
%post -n texlive-garamond-libre
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-garamond-libre 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-garamond-libre
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-garamond-libre-fonts
%files -n texlive-garamond-libre-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/garamond-libre/README
%{_texmfdistdir}/doc/fonts/garamond-libre/garamond-libre.pdf
%{_texmfdistdir}/doc/fonts/garamond-libre/garamond-libre.tex

%files -n texlive-garamond-libre
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/garamond-libre/GaramondLibre-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/garamond-libre/GaramondLibre-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/garamond-libre/GaramondLibre-Regular.otf

%files -n texlive-garamond-libre-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-garamond-libre
%{_datadir}/fontconfig/conf.avail/58-texlive-garamond-libre.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-garamond-libre/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-garamond-libre/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-garamond-libre/fonts.scale
%{_datadir}/fonts/texlive-garamond-libre/GaramondLibre-Bold.otf
%{_datadir}/fonts/texlive-garamond-libre/GaramondLibre-Italic.otf
%{_datadir}/fonts/texlive-garamond-libre/GaramondLibre-Regular.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-garamond-libre-fonts-%{texlive_version}.%{texlive_noarch}.1.1svn51703-%{release}-zypper
%endif

%package -n texlive-garamond-math
Version:        %{texlive_version}.%{texlive_noarch}.svn52820
Release:        0
Summary:        An OTF math font matching EB Garamond
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-garamond-math-fonts >= %{texlive_version}
Recommends:     texlive-garamond-math-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source178:      garamond-math.tar.xz
Source179:      garamond-math.doc.tar.xz

%description -n texlive-garamond-math
Garamond-Math is an open type math font matching EB Garamond
(Octavio Pardo) and EB Garamond (Georg Mayr-Duffner). Many
mathematical symbols are derived from other fonts, others are
made from scratch. The metric is generated with a Python
script. The font is best used with XeTeX and the unicode-math
package. Other engines (e.g. LuaTeX; also: MS Word) are likely
to produce unsatifactory spacings. This font is still under
development, so do not expect it to be free of bugs. Any
component might be updated at any time. Issues, bug reports,
forks, and other contributions are welcome.

%package -n texlive-garamond-math-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn52820
Release:        0
Summary:        Documentation for texlive-garamond-math
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-garamond-math-doc
This package includes the documentation for texlive-garamond-math


%package -n texlive-garamond-math-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn52820
Release:        0
Summary:        Severed fonts for texlive-garamond-math
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-garamond-math-fonts
The  separated fonts package for texlive-garamond-math
%post -n texlive-garamond-math
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-garamond-math 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-garamond-math
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-garamond-math-fonts
%files -n texlive-garamond-math-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/garamond-math/Garamond-Math.pdf
%{_texmfdistdir}/doc/fonts/garamond-math/Garamond-Math.tex
%{_texmfdistdir}/doc/fonts/garamond-math/README.md

%files -n texlive-garamond-math
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/garamond-math/Garamond-Math.otf

%files -n texlive-garamond-math-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-garamond-math
%{_datadir}/fontconfig/conf.avail/58-texlive-garamond-math.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-garamond-math/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-garamond-math/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-garamond-math/fonts.scale
%{_datadir}/fonts/texlive-garamond-math/Garamond-Math.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-garamond-math-fonts-%{texlive_version}.%{texlive_noarch}.svn52820-%{release}-zypper
%endif

%package -n texlive-garrigues
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        MetaPost macros for the reproduction of Garrigues' Easter nomogram
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
Recommends:     texlive-garrigues-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source180:      garrigues.tar.xz
Source181:      garrigues.doc.tar.xz

%description -n texlive-garrigues
MetaPost macros for the reproduction of Garrigues' Easter
nomogram. These macros are described in Denis Roegel: An
introduction to nomography: Garrigues' nomogram for the
computation of Easter, TUGboat (volume 30, number 1, 2009,
pages 88-104)

%package -n texlive-garrigues-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-garrigues
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-garrigues-doc
This package includes the documentation for texlive-garrigues

%post -n texlive-garrigues
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-garrigues 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-garrigues
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-garrigues-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/garrigues/README
%{_texmfdistdir}/doc/metapost/garrigues/article.txt

%files -n texlive-garrigues
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/garrigues/garrigues.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-garrigues-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-garuda-c90
Version:        %{texlive_version}.%{texlive_noarch}.svn37677
Release:        0
Summary:        TeX support (from CJK) for the garuda font
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-fonts-tlwg >= %{texlive_version}
#!BuildIgnore: texlive-fonts-tlwg
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
Provides:       tex(fgdb8z.tfm)
Provides:       tex(fgdbo8z.tfm)
Provides:       tex(fgdo8z.tfm)
Provides:       tex(fgdr8z.tfm)
Provides:       tex(garuda-c90.map)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source182:      garuda-c90.tar.xz

%description -n texlive-garuda-c90
The garuda-c90 package
%post -n texlive-garuda-c90
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap garuda-c90.map' >> /var/run/texlive/run-updmap

%postun -n texlive-garuda-c90 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap garuda-c90.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-garuda-c90
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-garuda-c90
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/garuda-c90/config.garuda-c90
%{_texmfdistdir}/fonts/map/dvips/garuda-c90/garuda-c90.map
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdb8z.tfm
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdbo8z.tfm
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdo8z.tfm
%{_texmfdistdir}/fonts/tfm/public/garuda-c90/fgdr8z.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-garuda-c90-%{texlive_version}.%{texlive_noarch}.svn37677-%{release}-zypper
%endif

%package -n texlive-gastex
Version:        %{texlive_version}.%{texlive_noarch}.2.8svn54080
Release:        0
Summary:        Graphs and Automata Simplified in TeX
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
Recommends:     texlive-gastex-doc >= %{texlive_version}
Provides:       tex(gastex.sty)
Requires:       tex(calc.sty)
Requires:       tex(trig.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source183:      gastex.tar.xz
Source184:      gastex.doc.tar.xz

%description -n texlive-gastex
GasTeX is a set of LaTeX macros which enable the user to draw
graphs, automata, nets, diagrams, etc., very easily, in the
LaTeX picture environment. The package offers no documentation
(per se), but offers a couple of example files in the
distribution, and more on its home page. GasTeX generates its
own PostScript code, and therefore doesn't work directly under
pdfLaTeX.

%package -n texlive-gastex-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.8svn54080
Release:        0
Summary:        Documentation for texlive-gastex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gastex-doc
This package includes the documentation for texlive-gastex

%post -n texlive-gastex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gastex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gastex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gastex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gastex/README
%{_texmfdistdir}/doc/latex/gastex/ex-beamer-gastex.tex
%{_texmfdistdir}/doc/latex/gastex/ex-gastex.tex

%files -n texlive-gastex
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/gastex/gastex.pro
%{_texmfdistdir}/tex/latex/gastex/gastex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gastex-%{texlive_version}.%{texlive_noarch}.2.8svn54080-%{release}-zypper
%endif

%package -n texlive-gatech-thesis
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn19886
Release:        0
Summary:        Georgia Institute of Technology thesis class
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
Recommends:     texlive-gatech-thesis-doc >= %{texlive_version}
Provides:       tex(gatech-thesis-gloss.sty)
Provides:       tex(gatech-thesis-index.sty)
Provides:       tex(gatech-thesis-losa.sty)
Provides:       tex(gatech-thesis-patch.sty)
Provides:       tex(gatech-thesis.cls)
Requires:       tex(calc.sty)
Requires:       tex(gloss.sty)
Requires:       tex(index.sty)
Requires:       tex(multicol.sty)
Requires:       tex(report.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source185:      gatech-thesis.tar.xz
Source186:      gatech-thesis.doc.tar.xz

%description -n texlive-gatech-thesis
The output generated by using this class has been approved by
the Georgia Tech Office of Graduate Studies. It satisfies their
undocumented moving-target requirements in additional to the
actual documented requirements of the June 2002 Georgia Tech
Thesis Style Manual, as amended up to 2010.

%package -n texlive-gatech-thesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn19886
Release:        0
Summary:        Documentation for texlive-gatech-thesis
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gatech-thesis-doc
This package includes the documentation for texlive-gatech-thesis

%post -n texlive-gatech-thesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gatech-thesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gatech-thesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gatech-thesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gatech-thesis/CHANGES
%{_texmfdistdir}/doc/latex/gatech-thesis/COMPLIANCE
%{_texmfdistdir}/doc/latex/gatech-thesis/COPYING
%{_texmfdistdir}/doc/latex/gatech-thesis/ChangeLog
%{_texmfdistdir}/doc/latex/gatech-thesis/INSTALL
%{_texmfdistdir}/doc/latex/gatech-thesis/MANIFEST
%{_texmfdistdir}/doc/latex/gatech-thesis/NEWS
%{_texmfdistdir}/doc/latex/gatech-thesis/NOTES
%{_texmfdistdir}/doc/latex/gatech-thesis/README
%{_texmfdistdir}/doc/latex/gatech-thesis/TODO
%{_texmfdistdir}/doc/latex/gatech-thesis/example-thesis.bib
%{_texmfdistdir}/doc/latex/gatech-thesis/example-thesis.pdf
%{_texmfdistdir}/doc/latex/gatech-thesis/example-thesis.tex

%files -n texlive-gatech-thesis
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/gatech-thesis/gatech-thesis-losa.bst
%{_texmfdistdir}/bibtex/bst/gatech-thesis/gatech-thesis.bst
%{_texmfdistdir}/makeindex/gatech-thesis/gatech-thesis-index.ist
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-gloss.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-index.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-losa.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-patch.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gatech-thesis-%{texlive_version}.%{texlive_noarch}.1.8svn19886-%{release}-zypper
%endif

%package -n texlive-gates
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn29803
Release:        0
Summary:        Support for writing modular and customisable code
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
Recommends:     texlive-gates-doc >= %{texlive_version}
Provides:       tex(gates.sty)
Provides:       tex(gates.tex)
Provides:       tex(t-gates.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source187:      gates.tar.xz
Source188:      gates.doc.tar.xz

%description -n texlive-gates
The package provides the means of writing code in a modular
fashion: big macros or functions are divided into small chunks
(called gates) with names, which can be externally controlled
(e.g. they can be disabled, subjected to conditionals,
loops...) and/or augmented with new chunks. Thus complex code
may easily be customised without having to rewrite it, or even
understand its implementation: the behavior of existing gates
can be modified, and new ones can be added, without endangering
the whole design. This allows code to be hacked in ways the
original authors might have never envisioned. The gates package
is implemented independently for both TeX and Lua. The TeX
implementation, running in any current environment, requires
the texapi package, whereas the Lua version can be run with any
Lua interpreter, not just LuaTeX.

%package -n texlive-gates-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn29803
Release:        0
Summary:        Documentation for texlive-gates
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gates-doc
This package includes the documentation for texlive-gates

%post -n texlive-gates
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gates 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gates
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gates-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/gates/README
%{_texmfdistdir}/doc/generic/gates/gates-doc.pdf
%{_texmfdistdir}/doc/generic/gates/gates-doc.tex
%{_texmfdistdir}/doc/generic/gates/gates-doc.txt

%files -n texlive-gates
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/gates/gates.lua
%{_texmfdistdir}/tex/generic/gates/gates.sty
%{_texmfdistdir}/tex/generic/gates/gates.tex
%{_texmfdistdir}/tex/generic/gates/t-gates.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gates-%{texlive_version}.%{texlive_noarch}.0.0.2svn29803-%{release}-zypper
%endif

%package -n texlive-gatherenum
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn52209
Release:        0
Summary:        A crossover of align* and enumerate
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
Recommends:     texlive-gatherenum-doc >= %{texlive_version}
Provides:       tex(gatherenum.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(expl3.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source189:      gatherenum.tar.xz
Source190:      gatherenum.doc.tar.xz

%description -n texlive-gatherenum
This package (ab)uses the inline enumeration capabilities of
enumitem to add a "displayed" enumeration mode, triggered by
adding 'gathered' to the key-value option list of the enumerate
environment. The end result is similar to a regular enumerate
environment wrapped in a multicols environment, with the
following advantages: Gathered enumerate can pack items
depending on their actual width rather than a fixed, constant
number per line. Gathered enumeration fills items in a
line-major order (instead of column-major order), which my
students found less confusing. YMMV. The package depends on
enumitem, expl3, and xparse,

%package -n texlive-gatherenum-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn52209
Release:        0
Summary:        Documentation for texlive-gatherenum
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gatherenum-doc
This package includes the documentation for texlive-gatherenum

%post -n texlive-gatherenum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gatherenum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gatherenum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gatherenum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gatherenum/LICENSE
%{_texmfdistdir}/doc/latex/gatherenum/README.md
%{_texmfdistdir}/doc/latex/gatherenum/gatherenum.pdf

%files -n texlive-gatherenum
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gatherenum/gatherenum.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gatherenum-%{texlive_version}.%{texlive_noarch}.1.8svn52209-%{release}-zypper
%endif

%package -n texlive-gauss
Version:        %{texlive_version}.%{texlive_noarch}.svn32934
Release:        0
Summary:        A package for Gaussian operations
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
Recommends:     texlive-gauss-doc >= %{texlive_version}
Provides:       tex(gauss.sty)
Requires:       tex(amsmath.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source191:      gauss.tar.xz
Source192:      gauss.doc.tar.xz

%description -n texlive-gauss
The gauss package provides configurable tools for producing row
and column operations on matrices (a.k.a. Gaussian operations).

%package -n texlive-gauss-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn32934
Release:        0
Summary:        Documentation for texlive-gauss
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gauss-doc
This package includes the documentation for texlive-gauss

%post -n texlive-gauss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gauss 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gauss
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gauss-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gauss/README
%{_texmfdistdir}/doc/latex/gauss/gauss-doc.pdf
%{_texmfdistdir}/doc/latex/gauss/gauss-ex.pdf
%{_texmfdistdir}/doc/latex/gauss/gauss-ex.tex

%files -n texlive-gauss
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gauss/gauss.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gauss-%{texlive_version}.%{texlive_noarch}.svn32934-%{release}-zypper
%endif

%package -n texlive-gb4e
Version:        %{texlive_version}.%{texlive_noarch}.svn19216
Release:        0
Summary:        Linguistic tools
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
Recommends:     texlive-gb4e-doc >= %{texlive_version}
Provides:       tex(cgloss4e.sty)
Provides:       tex(gb4e.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source193:      gb4e.tar.xz
Source194:      gb4e.doc.tar.xz

%description -n texlive-gb4e
Provides an environment for linguistic examples, tools for
glosses, and various other goodies. The code was developed from
the midnight and covington packages.

%package -n texlive-gb4e-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn19216
Release:        0
Summary:        Documentation for texlive-gb4e
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gb4e-doc
This package includes the documentation for texlive-gb4e

%post -n texlive-gb4e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gb4e 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gb4e
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gb4e-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gb4e/README
%{_texmfdistdir}/doc/latex/gb4e/gb4e-doc.pdf
%{_texmfdistdir}/doc/latex/gb4e/gb4e-doc.tex

%files -n texlive-gb4e
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gb4e/cgloss4e.sty
%{_texmfdistdir}/tex/latex/gb4e/gb4e.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gb4e-%{texlive_version}.%{texlive_noarch}.svn19216-%{release}-zypper
%endif

%package -n texlive-gbt7714
Version:        %{texlive_version}.%{texlive_noarch}.2.0.1svn54758
Release:        0
Summary:        BibTeX implementation of China's bibliography style standard GB/T 7714-2015
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
Recommends:     texlive-gbt7714-doc >= %{texlive_version}
Provides:       tex(gbt7714.sty)
Requires:       tex(natbib.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source195:      gbt7714.tar.xz
Source196:      gbt7714.doc.tar.xz

%description -n texlive-gbt7714
The package provides a BibTeX implementation for the Chinese
national bibliography style standard GB/T 7714-2015. It
consists of two bst files for numerical and author-year styles
and a LaTeX package which provides the citation style defined
in the standard. It also support automatic language
recognization (Chinese and English) for each biblilography
entry and is designed to be fully compatible with natbib.

%package -n texlive-gbt7714-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.1svn54758
Release:        0
Summary:        Documentation for texlive-gbt7714
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-gbt7714-doc:zh)

%description -n texlive-gbt7714-doc
This package includes the documentation for texlive-gbt7714

%post -n texlive-gbt7714
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gbt7714 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gbt7714
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gbt7714-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/gbt7714/LICENSE
%{_texmfdistdir}/doc/bibtex/gbt7714/README.md
%{_texmfdistdir}/doc/bibtex/gbt7714/gbt7714.pdf

%files -n texlive-gbt7714
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/gbt7714/gbt7714-author-year.bst
%{_texmfdistdir}/bibtex/bst/gbt7714/gbt7714-numerical.bst
%{_texmfdistdir}/tex/latex/gbt7714/gbt7714.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gbt7714-%{texlive_version}.%{texlive_noarch}.2.0.1svn54758-%{release}-zypper
%endif

%package -n texlive-gcard
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Arrange text on a sheet to fold into a greeting card
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
Recommends:     texlive-gcard-doc >= %{texlive_version}
Provides:       tex(gcard.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(textpos.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source197:      gcard.tar.xz
Source198:      gcard.doc.tar.xz

%description -n texlive-gcard
The package provides a simple means of producing greeting
cards. It arranges four panels onto a single sheet so that when
the sheet is folded twice the four panels are arranged as front
cover, inside left and right pages, and back cover. It uses the
textpos package for placement on the sheet and the graphicx
package for the necessary rotation. The four panels are set in
minipages for formatting by the user.

%package -n texlive-gcard-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-gcard
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gcard-doc
This package includes the documentation for texlive-gcard

%post -n texlive-gcard
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gcard 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gcard
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gcard-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gcard/README
%{_texmfdistdir}/doc/latex/gcard/gcard.pdf
%{_texmfdistdir}/doc/latex/gcard/gcardex.tex
%{_texmfdistdir}/doc/latex/gcard/gcardminexample.tex

%files -n texlive-gcard
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gcard/gcard.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gcard-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-gchords
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn29803
Release:        0
Summary:        Typeset guitar chords
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
Recommends:     texlive-gchords-doc >= %{texlive_version}
Provides:       tex(gchords.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source199:      gchords.tar.xz
Source200:      gchords.doc.tar.xz

%description -n texlive-gchords
A LaTeX package for typesetting of guitar chord diagrams,
including options for chord names, finger numbers and
typesetting above lyrics. The bundle also includes a TCL script
(chordbox.tcl) that provides a graphical application which
creates LaTeX files that use gchords.sty.

%package -n texlive-gchords-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn29803
Release:        0
Summary:        Documentation for texlive-gchords
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gchords-doc
This package includes the documentation for texlive-gchords

%post -n texlive-gchords
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gchords 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gchords
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gchords-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gchords/README
%{_texmfdistdir}/doc/latex/gchords/chordbox.tcl
%{_texmfdistdir}/doc/latex/gchords/gchords_doc.pdf
%{_texmfdistdir}/doc/latex/gchords/gchords_doc.tex
%{_texmfdistdir}/doc/latex/gchords/get2knowu.tex

%files -n texlive-gchords
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gchords/gchords.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gchords-%{texlive_version}.%{texlive_noarch}.1.20svn29803-%{release}-zypper
%endif

%package -n texlive-gcite
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn15878
Release:        0
Summary:        Citations in a reader-friendly style
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
Recommends:     texlive-gcite-doc >= %{texlive_version}
Provides:       tex(gcite.sty)
Requires:       tex(biblatex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source201:      gcite.tar.xz
Source202:      gcite.doc.tar.xz

%description -n texlive-gcite
The package allows citations in the German style, which is
considered by many to be particularly reader-friendly. The
citation provides a small amount of bibliographic information
in a footnote on the page where each citation is made. It
combines a desire to eliminate unnecessary page-turning with
the look-up efficiency afforded by numeric citations. The
package makes use of BibLaTeX, and is considered experimental;
comment is invited.

%package -n texlive-gcite-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn15878
Release:        0
Summary:        Documentation for texlive-gcite
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gcite-doc
This package includes the documentation for texlive-gcite

%post -n texlive-gcite
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gcite 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gcite
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gcite-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gcite/CHANGES
%{_texmfdistdir}/doc/latex/gcite/README
%{_texmfdistdir}/doc/latex/gcite/gcite.bib
%{_texmfdistdir}/doc/latex/gcite/gcite.pdf

%files -n texlive-gcite
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gcite/gcite.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gcite-%{texlive_version}.%{texlive_noarch}.1.0.1svn15878-%{release}-zypper
%endif

%package -n texlive-gender
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36464
Release:        0
Summary:        Gender neutrality for languages with grammatical gender
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
Recommends:     texlive-gender-doc >= %{texlive_version}
Provides:       tex(gender.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source203:      gender.tar.xz
Source204:      gender.doc.tar.xz

%description -n texlive-gender
Many languages -- like German or French -- use masculine and
feminine grammatical genders. There are many ideas how to
promote gender neutrality in those languages. The gender
package uses alternately masculine and feminine forms. It is
also possible to use just one form out of a template.

%package -n texlive-gender-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36464
Release:        0
Summary:        Documentation for texlive-gender
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gender-doc
This package includes the documentation for texlive-gender

%post -n texlive-gender
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gender 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gender
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gender-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gender/README
%{_texmfdistdir}/doc/latex/gender/gender.pdf

%files -n texlive-gender
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gender/gender.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gender-%{texlive_version}.%{texlive_noarch}.1.0svn36464-%{release}-zypper
%endif

%package -n texlive-gene-logic
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn15878
Release:        0
Summary:        Typeset logic formulae, etcetera
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
Recommends:     texlive-gene-logic-doc >= %{texlive_version}
Provides:       tex(gn-logic14.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source205:      gene-logic.tar.xz
Source206:      gene-logic.doc.tar.xz

%description -n texlive-gene-logic
The package provides a facility to typeset certain logic
formulae. It provides an environment like eqnarray, a
newtheorem-like environment (NewTheorem), and several macros.

%package -n texlive-gene-logic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn15878
Release:        0
Summary:        Documentation for texlive-gene-logic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gene-logic-doc
This package includes the documentation for texlive-gene-logic

%post -n texlive-gene-logic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gene-logic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gene-logic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gene-logic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gene-logic/gn-logic14.pdf
%{_texmfdistdir}/doc/latex/gene-logic/gn-logic14.tex

%files -n texlive-gene-logic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gene-logic/gn-logic14.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gene-logic-%{texlive_version}.%{texlive_noarch}.1.4svn15878-%{release}-zypper
%endif

%package -n texlive-genealogy
Version:        %{texlive_version}.%{texlive_noarch}.svn25112
Release:        0
Summary:        A compilation genealogy font
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
Recommends:     texlive-genealogy-doc >= %{texlive_version}
Provides:       tex(drgen10.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source207:      genealogy.tar.xz
Source208:      genealogy.doc.tar.xz

%description -n texlive-genealogy
A simple compilation of the genealogical symbols found in the
wasy and gen fonts, adding the male and female symbols to
Knuth's 'gen' font, and so avoiding loading two fonts when you
need only genealogical symbols. The font is distributed as
Metafont source.

%package -n texlive-genealogy-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn25112
Release:        0
Summary:        Documentation for texlive-genealogy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-genealogy-doc
This package includes the documentation for texlive-genealogy

%post -n texlive-genealogy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-genealogy 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-genealogy
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-genealogy-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/genealogy/README
%{_texmfdistdir}/doc/fonts/genealogy/licence.txt
%{_texmfdistdir}/doc/fonts/genealogy/testgen.tex

%files -n texlive-genealogy
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/genealogy/drgen.mf
%{_texmfdistdir}/fonts/source/public/genealogy/drgen10.mf
%{_texmfdistdir}/fonts/tfm/public/genealogy/drgen10.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-genealogy-%{texlive_version}.%{texlive_noarch}.svn25112-%{release}-zypper
%endif

%package -n texlive-genealogytree
Version:        %{texlive_version}.%{texlive_noarch}.1.32svn50872
Release:        0
Summary:        Pedigree and genealogical tree diagrams
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
Recommends:     texlive-genealogytree-doc >= %{texlive_version}
Provides:       tex(genealogytree.sty)
Provides:       tex(gtrcore.contour.code.tex)
Provides:       tex(gtrcore.drawing.code.tex)
Provides:       tex(gtrcore.node.code.tex)
Provides:       tex(gtrcore.options.code.tex)
Provides:       tex(gtrcore.parser.code.tex)
Provides:       tex(gtrcore.processing.code.tex)
Provides:       tex(gtrcore.symbols.code.tex)
Provides:       tex(gtrlang.danish.code.tex)
Provides:       tex(gtrlang.dutch.code.tex)
Provides:       tex(gtrlang.english.code.tex)
Provides:       tex(gtrlang.french.code.tex)
Provides:       tex(gtrlang.german.code.tex)
Provides:       tex(gtrlang.italian.code.tex)
Provides:       tex(gtrlang.spanish.code.tex)
Provides:       tex(gtrlang.swedish.code.tex)
Provides:       tex(gtrlib.debug.code.tex)
Provides:       tex(gtrlib.templates.code.tex)
Requires:       tex(tcolorbox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source209:      genealogytree.tar.xz
Source210:      genealogytree.doc.tar.xz

%description -n texlive-genealogytree
Pedigree and genealogical tree diagrams are proven tools to
visualize genetic and relational connections between
individuals. The naming ("tree") derives from historical family
diagrams. However, even the smallest family entity consisting
of two parents and several children is hardly a 'mathematical'
tree -- it is a more general graph. The package provides a set
of tools to typeset genealogical trees (i.e., to typeset a set
of special graphs for the description of family-like
structures). The package uses an autolayout algorithm which can
be customized, e.g., to prioritize certain paths.

%package -n texlive-genealogytree-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.32svn50872
Release:        0
Summary:        Documentation for texlive-genealogytree
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-genealogytree-doc
This package includes the documentation for texlive-genealogytree

%post -n texlive-genealogytree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-genealogytree 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-genealogytree
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-genealogytree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/genealogytree/README
%{_texmfdistdir}/doc/latex/genealogytree/genealogytree-example-1.pdf
%{_texmfdistdir}/doc/latex/genealogytree/genealogytree-example-2.pdf
%{_texmfdistdir}/doc/latex/genealogytree/genealogytree-example-3.pdf
%{_texmfdistdir}/doc/latex/genealogytree/genealogytree-languages.pdf
%{_texmfdistdir}/doc/latex/genealogytree/genealogytree.doc.sources.zip
%{_texmfdistdir}/doc/latex/genealogytree/genealogytree.pdf

%files -n texlive-genealogytree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/genealogytree/genealogytree.sty
%{_texmfdistdir}/tex/latex/genealogytree/gtrcore.contour.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrcore.drawing.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrcore.node.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrcore.options.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrcore.parser.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrcore.processing.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrcore.symbols.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.danish.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.dutch.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.english.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.french.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.german.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.italian.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.spanish.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlang.swedish.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlib.debug.code.tex
%{_texmfdistdir}/tex/latex/genealogytree/gtrlib.templates.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-genealogytree-%{texlive_version}.%{texlive_noarch}.1.32svn50872-%{release}-zypper
%endif

%package -n texlive-genmpage
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.1svn15878
Release:        0
Summary:        Generalization of LaTeX's minipages
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
Recommends:     texlive-genmpage-doc >= %{texlive_version}
Provides:       tex(genmpage.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source211:      genmpage.tar.xz
Source212:      genmpage.doc.tar.xz

%description -n texlive-genmpage
The GenMPage package generalizes LaTeX's minipages. Keyval
options and styles can be used to determine their appearance in
an easy and consistent way. Includes options for paragraph
indentation and vertical alignment with respect to the visual
top and bottom margins.

%package -n texlive-genmpage-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.1svn15878
Release:        0
Summary:        Documentation for texlive-genmpage
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-genmpage-doc
This package includes the documentation for texlive-genmpage

%post -n texlive-genmpage
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-genmpage 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-genmpage
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-genmpage-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/genmpage/README
%{_texmfdistdir}/doc/latex/genmpage/genmpage.pdf

%files -n texlive-genmpage
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/genmpage/genmpage.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-genmpage-%{texlive_version}.%{texlive_noarch}.0.0.3.1svn15878-%{release}-zypper
%endif

%package -n texlive-gentium-tug
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Gentium fonts (in two formats) and support files
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
Requires:       texlive-gentium-tug-fonts >= %{texlive_version}
Recommends:     texlive-gentium-tug-doc >= %{texlive_version}
Provides:       tex(agr-gentiumplus-italic.tfm)
Provides:       tex(agr-gentiumplus-regular.tfm)
Provides:       tex(ec-gentiumbasic-bold.tfm)
Provides:       tex(ec-gentiumbasic-bolditalic.tfm)
Provides:       tex(ec-gentiumplus-italic-sc.tfm)
Provides:       tex(ec-gentiumplus-italic.tfm)
Provides:       tex(ec-gentiumplus-regular-sc.tfm)
Provides:       tex(ec-gentiumplus-regular.tfm)
Provides:       tex(gentium-agr.enc)
Provides:       tex(gentium-agr.map)
Provides:       tex(gentium-ec-sc.enc)
Provides:       tex(gentium-ec-ttf-sc.enc)
Provides:       tex(gentium-ec-ttf.enc)
Provides:       tex(gentium-ec.enc)
Provides:       tex(gentium-ec.map)
Provides:       tex(gentium-l7x-sc.enc)
Provides:       tex(gentium-l7x.enc)
Provides:       tex(gentium-l7x.map)
Provides:       tex(gentium-lgr.enc)
Provides:       tex(gentium-lgr.map)
Provides:       tex(gentium-ot1-sc.enc)
Provides:       tex(gentium-ot1.enc)
Provides:       tex(gentium-ot1.map)
Provides:       tex(gentium-qx-sc.enc)
Provides:       tex(gentium-qx.enc)
Provides:       tex(gentium-qx.map)
Provides:       tex(gentium-t2a-sc.enc)
Provides:       tex(gentium-t2a.enc)
Provides:       tex(gentium-t2a.map)
Provides:       tex(gentium-t2b-sc.enc)
Provides:       tex(gentium-t2b.enc)
Provides:       tex(gentium-t2b.map)
Provides:       tex(gentium-t2c-sc.enc)
Provides:       tex(gentium-t2c.enc)
Provides:       tex(gentium-t2c.map)
Provides:       tex(gentium-t5-sc.enc)
Provides:       tex(gentium-t5-ttf.enc)
Provides:       tex(gentium-t5.enc)
Provides:       tex(gentium-t5.map)
Provides:       tex(gentium-texnansi-sc.enc)
Provides:       tex(gentium-texnansi.enc)
Provides:       tex(gentium-texnansi.map)
Provides:       tex(gentium-truetype.map)
Provides:       tex(gentium-ts1.enc)
Provides:       tex(gentium-ts1.map)
Provides:       tex(gentium-type1.map)
Provides:       tex(gentium-x2-sc.enc)
Provides:       tex(gentium-x2.enc)
Provides:       tex(gentium-x2.map)
Provides:       tex(gentium.sty)
Provides:       tex(l7x-gentiumbasic-bold.tfm)
Provides:       tex(l7x-gentiumbasic-bolditalic.tfm)
Provides:       tex(l7x-gentiumplus-italic-sc.tfm)
Provides:       tex(l7x-gentiumplus-italic.tfm)
Provides:       tex(l7x-gentiumplus-regular-sc.tfm)
Provides:       tex(l7x-gentiumplus-regular.tfm)
Provides:       tex(l7xgentium.fd)
Provides:       tex(lgr-gentiumplus-italic.tfm)
Provides:       tex(lgr-gentiumplus-regular.tfm)
Provides:       tex(lgrgentium.fd)
Provides:       tex(ly1gentium.fd)
Provides:       tex(ot1-gentiumbasic-bold.tfm)
Provides:       tex(ot1-gentiumbasic-bolditalic.tfm)
Provides:       tex(ot1-gentiumplus-italic-sc.tfm)
Provides:       tex(ot1-gentiumplus-italic.tfm)
Provides:       tex(ot1-gentiumplus-regular-sc.tfm)
Provides:       tex(ot1-gentiumplus-regular.tfm)
Provides:       tex(ot1gentium.fd)
Provides:       tex(qx-gentiumbasic-bold.tfm)
Provides:       tex(qx-gentiumbasic-bolditalic.tfm)
Provides:       tex(qx-gentiumplus-italic-sc.tfm)
Provides:       tex(qx-gentiumplus-italic.tfm)
Provides:       tex(qx-gentiumplus-regular-sc.tfm)
Provides:       tex(qx-gentiumplus-regular.tfm)
Provides:       tex(qxgentium.fd)
Provides:       tex(t1gentium.fd)
Provides:       tex(t2a-gentiumplus-italic-sc.tfm)
Provides:       tex(t2a-gentiumplus-italic.tfm)
Provides:       tex(t2a-gentiumplus-regular-sc.tfm)
Provides:       tex(t2a-gentiumplus-regular.tfm)
Provides:       tex(t2agentium.fd)
Provides:       tex(t2b-gentiumplus-italic-sc.tfm)
Provides:       tex(t2b-gentiumplus-italic.tfm)
Provides:       tex(t2b-gentiumplus-regular-sc.tfm)
Provides:       tex(t2b-gentiumplus-regular.tfm)
Provides:       tex(t2bgentium.fd)
Provides:       tex(t2c-gentiumplus-italic-sc.tfm)
Provides:       tex(t2c-gentiumplus-italic.tfm)
Provides:       tex(t2c-gentiumplus-regular-sc.tfm)
Provides:       tex(t2c-gentiumplus-regular.tfm)
Provides:       tex(t2cgentium.fd)
Provides:       tex(t5-gentiumbasic-bold.tfm)
Provides:       tex(t5-gentiumbasic-bolditalic.tfm)
Provides:       tex(t5-gentiumplus-italic-sc.tfm)
Provides:       tex(t5-gentiumplus-italic.tfm)
Provides:       tex(t5-gentiumplus-regular-sc.tfm)
Provides:       tex(t5-gentiumplus-regular.tfm)
Provides:       tex(t5gentium.fd)
Provides:       tex(texnansi-gentiumbasic-bold.tfm)
Provides:       tex(texnansi-gentiumbasic-bolditalic.tfm)
Provides:       tex(texnansi-gentiumplus-italic-sc.tfm)
Provides:       tex(texnansi-gentiumplus-italic.tfm)
Provides:       tex(texnansi-gentiumplus-regular-sc.tfm)
Provides:       tex(texnansi-gentiumplus-regular.tfm)
Provides:       tex(ts1-gentiumbasic-bold.tfm)
Provides:       tex(ts1-gentiumbasic-bolditalic.tfm)
Provides:       tex(ts1-gentiumplus-italic.tfm)
Provides:       tex(ts1-gentiumplus-regular.tfm)
Provides:       tex(ts1gentium.fd)
Provides:       tex(x2-gentiumplus-italic-sc.tfm)
Provides:       tex(x2-gentiumplus-italic.tfm)
Provides:       tex(x2-gentiumplus-regular-sc.tfm)
Provides:       tex(x2-gentiumplus-regular.tfm)
Provides:       tex(x2gentium.fd)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source213:      gentium-tug.tar.xz
Source214:      gentium-tug.doc.tar.xz

%description -n texlive-gentium-tug
Gentium is a typeface family designed to enable the diverse
ethnic groups around the world who use the Latin, Cyrillic and
Greek scripts to produce readable, high-quality publications.
It supports a wide range of Latin- and Cyrillic-based
alphabets. The package consists of: The original (unaltered)
GentiumPlus, GentiumBook, and other Gentium-family fonts in
TrueType format, as developed by SIL and released under the OFL
(see OFL.txt and OFL-FAQ.txt); Converted fonts in PostScript
Type 1 format, released under the same terms. These incorporate
the name "Gentium" by permission of SIL given to the TeX Users
Group; ConTeXt, LaTeX and other supporting files; TeX-related
documentation, and the SIL documentation and other files.

%package -n texlive-gentium-tug-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Documentation for texlive-gentium-tug
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gentium-tug-doc
This package includes the documentation for texlive-gentium-tug


%package -n texlive-gentium-tug-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Severed fonts for texlive-gentium-tug
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gentium-tug-fonts
The  separated fonts package for texlive-gentium-tug
%post -n texlive-gentium-tug
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gentium-type1.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gentium-tug 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gentium-type1.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gentium-tug
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gentium-tug-fonts
%files -n texlive-gentium-tug-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gentium-tug/ChangeLog
%{_texmfdistdir}/doc/fonts/gentium-tug/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/GENTIUM-FAQ.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/OFL.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/QUOTES.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/Gentium/README.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/GENTIUM-FAQ.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumBasic/OFL.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/GENTIUM-FAQ.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/OFL.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/README.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/documentation/DOCUMENTATION.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/documentation/GentiumPlus-features.odt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlus/documentation/GentiumPlus-features.pdf
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlusCompact/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlusCompact/README.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/GentiumPlusCompact/feat_set_tuned.xml
%{_texmfdistdir}/doc/fonts/gentium-tug/Makefile
%{_texmfdistdir}/doc/fonts/gentium-tug/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/OFL.txt
%{_texmfdistdir}/doc/fonts/gentium-tug/README
%{_texmfdistdir}/doc/fonts/gentium-tug/gentium.pdf
%{_texmfdistdir}/doc/fonts/gentium-tug/gentium.tex

%files -n texlive-gentium-tug
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GenBasB.afm
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GenBasBI.afm
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GentiumPlus-I.afm
%{_texmfdistdir}/fonts/afm/public/gentium-tug/GentiumPlus-R.afm
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-agr.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec-ttf-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec-ttf.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-l7x-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-l7x.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ot1-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-qx-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2a-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2b-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2c-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t5-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t5-ttf.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-texnansi-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-texnansi.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-x2-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gentium-tug/gentium-x2.enc
%{_texmfdistdir}/fonts/map/dvips/gentium-tug/gentium-type1.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-agr.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-ec.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-l7x.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-lgr.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-ot1.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-qx.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t2a.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t2b.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t2c.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-t5.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-texnansi.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-truetype.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-ts1.map
%{_texmfdistdir}/fonts/map/pdftex/gentium-tug/gentium-x2.map
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/agr-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/agr-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ec-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/l7x-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/lgr-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/lgr-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ot1-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/qx-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2a-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2b-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t2c-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/t5-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/texnansi-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumbasic-bold.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumbasic-bolditalic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/ts1-gentiumplus-regular.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-italic-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-italic.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-regular-sc.tfm
%{_texmfdistdir}/fonts/tfm/public/gentium-tug/x2-gentiumplus-regular.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasB.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasBI.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasI.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBasR.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasB.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasBI.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasI.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GenBkBasR.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/Gentium-I.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/Gentium-R.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumAlt-I.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumAlt-R.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlus-I.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlus-R.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlusCompact-I.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gentium-tug/GentiumPlusCompact-R.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/gentium-tug/GenBasB.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gentium-tug/GenBasBI.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gentium-tug/GentiumPlus-I.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gentium-tug/GentiumPlus-R.pfb
%{_texmfdistdir}/tex/context/third/gentium-tug/type-gentium.mkii
%{_texmfdistdir}/tex/context/third/gentium-tug/type-gentium.mkiv
%{_texmfdistdir}/tex/latex/gentium-tug/gentium.sty
%{_texmfdistdir}/tex/latex/gentium-tug/l7xgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/lgrgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/ly1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/ot1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/qxgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t2agentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t2bgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t2cgentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/t5gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/ts1gentium.fd
%{_texmfdistdir}/tex/latex/gentium-tug/x2gentium.fd

%files -n texlive-gentium-tug-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gentium-tug
%{_datadir}/fontconfig/conf.avail/58-texlive-gentium-tug.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gentium-tug.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gentium-tug.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gentium-tug/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gentium-tug/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gentium-tug/fonts.scale
%{_datadir}/fonts/texlive-gentium-tug/GenBasB.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBasBI.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBasI.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBasR.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBkBasB.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBkBasBI.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBkBasI.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBkBasR.ttf
%{_datadir}/fonts/texlive-gentium-tug/Gentium-I.ttf
%{_datadir}/fonts/texlive-gentium-tug/Gentium-R.ttf
%{_datadir}/fonts/texlive-gentium-tug/GentiumAlt-I.ttf
%{_datadir}/fonts/texlive-gentium-tug/GentiumAlt-R.ttf
%{_datadir}/fonts/texlive-gentium-tug/GentiumPlus-I.ttf
%{_datadir}/fonts/texlive-gentium-tug/GentiumPlus-R.ttf
%{_datadir}/fonts/texlive-gentium-tug/GentiumPlusCompact-I.ttf
%{_datadir}/fonts/texlive-gentium-tug/GentiumPlusCompact-R.ttf
%{_datadir}/fonts/texlive-gentium-tug/GenBasB.pfb
%{_datadir}/fonts/texlive-gentium-tug/GenBasBI.pfb
%{_datadir}/fonts/texlive-gentium-tug/GentiumPlus-I.pfb
%{_datadir}/fonts/texlive-gentium-tug/GentiumPlus-R.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gentium-tug-fonts-%{texlive_version}.%{texlive_noarch}.1.1.1svn54512-%{release}-zypper
%endif

%package -n texlive-gentle
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A Gentle Introduction to TeX
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
Source215:      gentle.doc.tar.xz

%description -n texlive-gentle
The "Gentle Introduction" is the longest-established
comprehensive free tutorial on the use of plain TeX.
%post -n texlive-gentle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gentle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gentle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gentle
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/gentle/gentle.pdf
%{_texmfdistdir}/doc/plain/gentle/gentle.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gentle-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-gentombow
Version:        %{texlive_version}.%{texlive_noarch}.svn51697
Release:        0
Summary:        Generate Japanese-style crop marks
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
Recommends:     texlive-gentombow-doc >= %{texlive_version}
Provides:       tex(bounddvi.sty)
Provides:       tex(gentombow.sty)
Provides:       tex(pxgentombow.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pxatbegshi.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source216:      gentombow.tar.xz
Source217:      gentombow.doc.tar.xz

%description -n texlive-gentombow
This bundle provides a LaTeX package for generating
Japanese-style crop marks (called 'tombow' in Japanese) for
practical use in self-publishing. The bundle contains the
following packages: gentombow.sty: Generate crop marks (called
'tombow' in Japanese) for practical use in self-publishing. It
provides the core 'tombow' feature if not available.
pxgentombow.sty: Superseded by gentombow.sty; kept for
compatibility only. bounddvi.sty: Set papersize special to DVI
file. Can be used on LaTeX/pLaTeX/upLaTeX (with DVI output
mode) with dvips or dvipdfmx drivers.

%package -n texlive-gentombow-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn51697
Release:        0
Summary:        Documentation for texlive-gentombow
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-gentombow-doc:ja)

%description -n texlive-gentombow-doc
This package includes the documentation for texlive-gentombow

%post -n texlive-gentombow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gentombow 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gentombow
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gentombow-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gentombow/LICENSE
%{_texmfdistdir}/doc/latex/gentombow/README.md
%{_texmfdistdir}/doc/latex/gentombow/bounddvi-en.pdf
%{_texmfdistdir}/doc/latex/gentombow/bounddvi-en.tex
%{_texmfdistdir}/doc/latex/gentombow/bounddvi.pdf
%{_texmfdistdir}/doc/latex/gentombow/bounddvi.tex
%{_texmfdistdir}/doc/latex/gentombow/gentombow-ja.pdf
%{_texmfdistdir}/doc/latex/gentombow/gentombow-ja.tex
%{_texmfdistdir}/doc/latex/gentombow/gentombow.pdf
%{_texmfdistdir}/doc/latex/gentombow/gentombow.tex
%{_texmfdistdir}/doc/latex/gentombow/pxgentombow.pdf
%{_texmfdistdir}/doc/latex/gentombow/pxgentombow.tex

%files -n texlive-gentombow
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gentombow/bounddvi.sty
%{_texmfdistdir}/tex/latex/gentombow/gentombow.sty
%{_texmfdistdir}/tex/latex/gentombow/pxgentombow.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gentombow-%{texlive_version}.%{texlive_noarch}.svn51697-%{release}-zypper
%endif

%package -n texlive-geometry
Version:        %{texlive_version}.%{texlive_noarch}.5.9svn54080
Release:        0
Summary:        Flexible and complete interface to document dimensions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-graphics >= %{texlive_version}
#!BuildIgnore: texlive-graphics
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
Recommends:     texlive-geometry-doc >= %{texlive_version}
Provides:       tex(geometry.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source218:      geometry.tar.xz
Source219:      geometry.doc.tar.xz

%description -n texlive-geometry
The package provides an easy and flexible user interface to
customize page layout, implementing auto-centering and
auto-balancing mechanisms so that the users have only to give
the least description for the page layout. For example, if you
want to set each margin 2cm without header space, what you need
is just \usepackage[margin=2cm,nohead]{geometry}. The package
knows about all the standard paper sizes, so that the user need
not know what the nominal 'real' dimensions of the paper are,
just its standard name (such as a4, letter, etc.). An important
feature is the package's ability to communicate the paper size
it's set up to the output (whether via DVI \specials or via
direct interaction with pdf(La)TeX).

%package -n texlive-geometry-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.9svn54080
Release:        0
Summary:        Documentation for texlive-geometry
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-geometry-doc:de;en)

%description -n texlive-geometry-doc
This package includes the documentation for texlive-geometry

%post -n texlive-geometry
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-geometry 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-geometry
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-geometry-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/geometry/README.md
%{_texmfdistdir}/doc/latex/geometry/changes.txt
%{_texmfdistdir}/doc/latex/geometry/geometry-de.pdf
%{_texmfdistdir}/doc/latex/geometry/geometry-samples-de.tex
%{_texmfdistdir}/doc/latex/geometry/geometry-samples.tex
%{_texmfdistdir}/doc/latex/geometry/geometry.cfg
%{_texmfdistdir}/doc/latex/geometry/geometry.pdf

%files -n texlive-geometry
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/geometry/geometry.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-geometry-%{texlive_version}.%{texlive_noarch}.5.9svn54080-%{release}-zypper
%endif

%package -n texlive-german
Version:        %{texlive_version}.%{texlive_noarch}.2.5esvn42428
Release:        0
Summary:        Support for German typography
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
Recommends:     texlive-german-doc >= %{texlive_version}
Provides:       tex(german.sty)
Provides:       tex(ngerman.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source220:      german.tar.xz
Source221:      german.doc.tar.xz

%description -n texlive-german
Supports the old German orthography (alte deutsche
Rechtschreibung).

%package -n texlive-german-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.5esvn42428
Release:        0
Summary:        Documentation for texlive-german
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-german-doc:de)

%description -n texlive-german-doc
This package includes the documentation for texlive-german

%post -n texlive-german
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-german 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-german
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-german-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/german/00readme.1st
%{_texmfdistdir}/doc/generic/german/betatest/00readme.1st
%{_texmfdistdir}/doc/generic/german/gerdoc.pdf
%{_texmfdistdir}/doc/generic/german/gerdoc.tex
%{_texmfdistdir}/doc/generic/german/german.MISSING
%{_texmfdistdir}/doc/generic/german/hyphxmpl.cfg

%files -n texlive-german
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/german/german.sty
%{_texmfdistdir}/tex/generic/german/ngerman.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-german-%{texlive_version}.%{texlive_noarch}.2.5esvn42428-%{release}-zypper
%endif

%package -n texlive-germbib
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        German variants of standard BibTeX styles
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
Recommends:     texlive-germbib-doc >= %{texlive_version}
Provides:       tex(bibgerm.sty)
Provides:       tex(mynormal.sty)
Requires:       tex(german.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source222:      germbib.tar.xz
Source223:      germbib.doc.tar.xz

%description -n texlive-germbib
A development of the (old) german.sty, this bundle provides
German packages, BibTeX styles and documentary examples, for
writing documents with bibliographies. The author has since
developed the babelbib bundle, which (he asserts) supersedes
germbib.

%package -n texlive-germbib-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-germbib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-germbib-doc
This package includes the documentation for texlive-germbib

%post -n texlive-germbib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-germbib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-germbib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-germbib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/germbib/README.bibgerm
%{_texmfdistdir}/doc/bibtex/germbib/apalike.doc
%{_texmfdistdir}/doc/bibtex/germbib/apalike.germbib_sty
%{_texmfdistdir}/doc/bibtex/germbib/apalike.tex
%{_texmfdistdir}/doc/bibtex/germbib/btxdoc.tex
%{_texmfdistdir}/doc/bibtex/germbib/btxhak.tex
%{_texmfdistdir}/doc/bibtex/germbib/gerbibtx.bib
%{_texmfdistdir}/doc/bibtex/germbib/gerbibtx.tex
%{_texmfdistdir}/doc/bibtex/germbib/gerxampl.bib
%{_texmfdistdir}/doc/bibtex/germbib/schaum.bib
%{_texmfdistdir}/doc/bibtex/germbib/testbibgerm.tex
%{_texmfdistdir}/doc/bibtex/germbib/testgerb.tex
%{_texmfdistdir}/doc/bibtex/germbib/xampl.bib

%files -n texlive-germbib
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/germbib/gerabbrv.bst
%{_texmfdistdir}/bibtex/bst/germbib/geralpha.bst
%{_texmfdistdir}/bibtex/bst/germbib/gerapali.bst
%{_texmfdistdir}/bibtex/bst/germbib/gerplain.bst
%{_texmfdistdir}/bibtex/bst/germbib/gerunsrt.bst
%{_texmfdistdir}/tex/latex/germbib/bibgerm.sty
%{_texmfdistdir}/tex/latex/germbib/mynormal.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-germbib-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-germkorr
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Change kerning for German quotation marks
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
Recommends:     texlive-germkorr-doc >= %{texlive_version}
Provides:       tex(germkorr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source224:      germkorr.tar.xz
Source225:      germkorr.doc.tar.xz

%description -n texlive-germkorr
The package germcorr has to be loaded after the package german.
It brings some letters like T nearer to german single and
double quotes even when that letter wears a standard accent
like "`\.T"'.

%package -n texlive-germkorr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-germkorr
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-germkorr-doc
This package includes the documentation for texlive-germkorr

%post -n texlive-germkorr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-germkorr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-germkorr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-germkorr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/germkorr/COPYING
%{_texmfdistdir}/doc/latex/germkorr/README
%{_texmfdistdir}/doc/latex/germkorr/germkorr.pdf
%{_texmfdistdir}/doc/latex/germkorr/germkorr.tex

%files -n texlive-germkorr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/germkorr/germkorr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-germkorr-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-geschichtsfrkl
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn42121
Release:        0
Summary:        BibLaTeX style for historians
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
Recommends:     texlive-geschichtsfrkl-doc >= %{texlive_version}
Provides:       tex(geschichtsfrkl.bbx)
Provides:       tex(geschichtsfrkl.cbx)
Provides:       tex(geschichtsfrkldoc.sty)
Requires:       tex(standard.bbx)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source226:      geschichtsfrkl.tar.xz
Source227:      geschichtsfrkl.doc.tar.xz

%description -n texlive-geschichtsfrkl
The package provides a BibLaTeX style, (mostly) meeting the
requirements of the History Faculty of the University of
Freiburg (Germany).

%package -n texlive-geschichtsfrkl-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn42121
Release:        0
Summary:        Documentation for texlive-geschichtsfrkl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-geschichtsfrkl-doc:de)

%description -n texlive-geschichtsfrkl-doc
This package includes the documentation for texlive-geschichtsfrkl

%post -n texlive-geschichtsfrkl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-geschichtsfrkl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-geschichtsfrkl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-geschichtsfrkl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/geschichtsfrkl/README
%{_texmfdistdir}/doc/latex/geschichtsfrkl/geschichtsfrkl.pdf

%files -n texlive-geschichtsfrkl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/geschichtsfrkl/geschichtsfrkl.bbx
%{_texmfdistdir}/tex/latex/geschichtsfrkl/geschichtsfrkl.cbx
%{_texmfdistdir}/tex/latex/geschichtsfrkl/geschichtsfrkldoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-geschichtsfrkl-%{texlive_version}.%{texlive_noarch}.1.4svn42121-%{release}-zypper
%endif

%package -n texlive-getfiledate
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn16189
Release:        0
Summary:        Find the date of last modification of a file
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
Recommends:     texlive-getfiledate-doc >= %{texlive_version}
Provides:       tex(getfiledate.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(boxedminipage.sty)
Requires:       tex(etextools.sty)
Requires:       tex(ltxnew.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source228:      getfiledate.tar.xz
Source229:      getfiledate.doc.tar.xz

%description -n texlive-getfiledate
The package fetches from the system the date of last
modification or opening of an existing file, using the function
\pdffilemoddate (present in recent versions of pdfTeX); the
user may specify how the date is to be presented.

%package -n texlive-getfiledate-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn16189
Release:        0
Summary:        Documentation for texlive-getfiledate
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-getfiledate-doc
This package includes the documentation for texlive-getfiledate

%post -n texlive-getfiledate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-getfiledate 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-getfiledate
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-getfiledate-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/getfiledate/README
%{_texmfdistdir}/doc/latex/getfiledate/getfiledate-guide.pdf
%{_texmfdistdir}/doc/latex/getfiledate/getfiledate-guide.tex

%files -n texlive-getfiledate
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/getfiledate/getfiledate.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-getfiledate-%{texlive_version}.%{texlive_noarch}.1.2svn16189-%{release}-zypper
%endif

%package -n texlive-getitems
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn39365
Release:        0
Summary:        Gathering items from a list-like environment
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
Recommends:     texlive-getitems-doc >= %{texlive_version}
Provides:       tex(getitems.sty)
Requires:       tex(environ.sty)
Requires:       tex(trimspaces.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source230:      getitems.tar.xz
Source231:      getitems.doc.tar.xz

%description -n texlive-getitems
This package provides a \gatheritems command to parse a list of
data separated by \item tokens. This makes it easier to define
custom environments which structure their data in the same way
that itemize or enumerate do.

%package -n texlive-getitems-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn39365
Release:        0
Summary:        Documentation for texlive-getitems
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-getitems-doc
This package includes the documentation for texlive-getitems

%post -n texlive-getitems
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-getitems 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-getitems
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-getitems-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/getitems/README.md
%{_texmfdistdir}/doc/latex/getitems/getitems.pdf

%files -n texlive-getitems
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/getitems/getitems.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-getitems-%{texlive_version}.%{texlive_noarch}.1.0svn39365-%{release}-zypper
%endif

%package -n texlive-getmap
Version:        %{texlive_version}.%{texlive_noarch}.1.11svn50589
Release:        0
Summary:        Download OpenStreetMap maps for use in documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-getmap-bin >= %{texlive_version}
#!BuildIgnore: texlive-getmap-bin
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
Recommends:     texlive-getmap-doc >= %{texlive_version}
Provides:       tex(getmap.cfg)
Provides:       tex(getmap.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(stringenc.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source232:      getmap.tar.xz
Source233:      getmap.doc.tar.xz

%description -n texlive-getmap
The package provides a simple interface to OpenStreetMap, and
to Google Maps "map images". In the simplest case, it is
sufficient to specify the address you need (if you don't, the
package will use its own default). The package loads the map
image using an external lua script (invoked via \write 18:
LaTeX must be running with \write 18 enabled). The ("external")
lua script may be used from the command line; a bash version is
provided.

%package -n texlive-getmap-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.11svn50589
Release:        0
Summary:        Documentation for texlive-getmap
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-getmap-doc
This package includes the documentation for texlive-getmap

%post -n texlive-getmap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-getmap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-getmap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-getmap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/getmap/README.md
%{_texmfdistdir}/doc/latex/getmap/getmap-example.tex
%{_texmfdistdir}/doc/latex/getmap/getmap.dtx
%{_texmfdistdir}/doc/latex/getmap/getmap.pdf
%{_texmfdistdir}/doc/latex/getmap/makefile
%{_texmfdistdir}/doc/latex/getmap/manifest.txt

%files -n texlive-getmap
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/getmap/getmapdl.lua
%{_texmfdistdir}/tex/latex/getmap/getmap.cfg
%{_texmfdistdir}/tex/latex/getmap/getmap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-getmap-%{texlive_version}.%{texlive_noarch}.1.11svn50589-%{release}-zypper
%endif

%package -n texlive-getoptk
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23567
Release:        0
Summary:        Define macros with sophisticated options
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
Recommends:     texlive-getoptk-doc >= %{texlive_version}
Provides:       tex(getoptk.tex)
Provides:       tex(guide.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source234:      getoptk.tar.xz
Source235:      getoptk.doc.tar.xz

%description -n texlive-getoptk
The package provides a means of defining macros whose options
are taken from a dictionary, which includes options which
themselves have arguments. The package was designed for use
with Plain TeX; its syntax derives from that of the \hbox,
\hrule, etc., TeX primitives.

%package -n texlive-getoptk-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23567
Release:        0
Summary:        Documentation for texlive-getoptk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-getoptk-doc
This package includes the documentation for texlive-getoptk

%post -n texlive-getoptk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-getoptk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-getoptk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-getoptk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/getoptk/COPYING
%{_texmfdistdir}/doc/plain/getoptk/COPYING-FR
%{_texmfdistdir}/doc/plain/getoptk/README
%{_texmfdistdir}/doc/plain/getoptk/guide.pdf

%files -n texlive-getoptk
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/getoptk/getoptk.tex
%{_texmfdistdir}/tex/plain/getoptk/guide.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-getoptk-%{texlive_version}.%{texlive_noarch}.1.0svn23567-%{release}-zypper
%endif

%package -n texlive-gettitlestring
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn53170
Release:        0
Summary:        Clean up title references
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
Recommends:     texlive-gettitlestring-doc >= %{texlive_version}
Provides:       tex(gettitlestring.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source236:      gettitlestring.tar.xz
Source237:      gettitlestring.doc.tar.xz

%description -n texlive-gettitlestring
Cleans up the title string (removing \label commands) for
packages (such as nameref) that typeset such strings.

%package -n texlive-gettitlestring-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn53170
Release:        0
Summary:        Documentation for texlive-gettitlestring
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gettitlestring-doc
This package includes the documentation for texlive-gettitlestring

%post -n texlive-gettitlestring
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gettitlestring 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gettitlestring
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gettitlestring-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gettitlestring/README.md
%{_texmfdistdir}/doc/latex/gettitlestring/gettitlestring.pdf

%files -n texlive-gettitlestring
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/gettitlestring/gettitlestring.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gettitlestring-%{texlive_version}.%{texlive_noarch}.1.6svn53170-%{release}-zypper
%endif

%package -n texlive-gfnotation
Version:        %{texlive_version}.%{texlive_noarch}.2.9svn37156
Release:        0
Summary:        Typeset Gottlob Frege's notation in plain TeX
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
Recommends:     texlive-gfnotation-doc >= %{texlive_version}
Provides:       tex(GFnotation.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source238:      gfnotation.tar.xz
Source239:      gfnotation.doc.tar.xz

%description -n texlive-gfnotation
The package implements macros for plain TeX to typeset the
notation invented by Gottlob Frege in 1879 for his books
"Begriffsschrift" and "Grundgesetze der Arithmetik" (two
volumes). The output styles of both books are supported.

%package -n texlive-gfnotation-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.9svn37156
Release:        0
Summary:        Documentation for texlive-gfnotation
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfnotation-doc
This package includes the documentation for texlive-gfnotation

%post -n texlive-gfnotation
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gfnotation 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gfnotation
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gfnotation-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/gfnotation/COPYING
%{_texmfdistdir}/doc/plain/gfnotation/GFnotation-doc.pdf
%{_texmfdistdir}/doc/plain/gfnotation/GFnotation-doc.tex
%{_texmfdistdir}/doc/plain/gfnotation/README

%files -n texlive-gfnotation
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/gfnotation/GFnotation.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfnotation-%{texlive_version}.%{texlive_noarch}.2.9svn37156-%{release}-zypper
%endif

%package -n texlive-gfsartemisia
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19469
Release:        0
Summary:        A modern Greek font design
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
Requires:       texlive-gfsartemisia-fonts >= %{texlive_version}
Recommends:     texlive-gfsartemisia-doc >= %{texlive_version}
Provides:       tex(artemisia.enc)
Provides:       tex(artemisiab8a.tfm)
Provides:       tex(artemisiab8a.vf)
Provides:       tex(artemisiab8r.tfm)
Provides:       tex(artemisiab9a.tfm)
Provides:       tex(artemisiab9a.vf)
Provides:       tex(artemisiab9r.tfm)
Provides:       tex(artemisiabi8a.tfm)
Provides:       tex(artemisiabi8a.vf)
Provides:       tex(artemisiabi8r.tfm)
Provides:       tex(artemisiabi9a.tfm)
Provides:       tex(artemisiabi9a.vf)
Provides:       tex(artemisiabi9r.tfm)
Provides:       tex(artemisiabo8a.tfm)
Provides:       tex(artemisiabo8a.vf)
Provides:       tex(artemisiabo8r.tfm)
Provides:       tex(artemisiabo9a.tfm)
Provides:       tex(artemisiabo9a.vf)
Provides:       tex(artemisiabo9r.tfm)
Provides:       tex(artemisiadenomnums.enc)
Provides:       tex(artemisiadenomnums8a.tfm)
Provides:       tex(artemisiadenomnums8a.vf)
Provides:       tex(artemisiadenomnums8r.tfm)
Provides:       tex(artemisiaec.enc)
Provides:       tex(artemisiaecsc.enc)
Provides:       tex(artemisiael.enc)
Provides:       tex(artemisiaelsc.enc)
Provides:       tex(artemisiai8a.tfm)
Provides:       tex(artemisiai8a.vf)
Provides:       tex(artemisiai8r.tfm)
Provides:       tex(artemisiai9a.tfm)
Provides:       tex(artemisiai9a.vf)
Provides:       tex(artemisiai9r.tfm)
Provides:       tex(artemisiamath.enc)
Provides:       tex(artemisiamath8a.tfm)
Provides:       tex(artemisiamath8a.vf)
Provides:       tex(artemisiamath8r.tfm)
Provides:       tex(artemisianumnums.enc)
Provides:       tex(artemisianumnums8a.tfm)
Provides:       tex(artemisianumnums8a.vf)
Provides:       tex(artemisianumnums8r.tfm)
Provides:       tex(artemisiao8a.tfm)
Provides:       tex(artemisiao8a.vf)
Provides:       tex(artemisiao8r.tfm)
Provides:       tex(artemisiao9a.tfm)
Provides:       tex(artemisiao9a.vf)
Provides:       tex(artemisiao9r.tfm)
Provides:       tex(artemisiarg8a.tfm)
Provides:       tex(artemisiarg8a.vf)
Provides:       tex(artemisiarg8r.tfm)
Provides:       tex(artemisiarg9a.tfm)
Provides:       tex(artemisiarg9a.vf)
Provides:       tex(artemisiarg9r.tfm)
Provides:       tex(artemisiasc.enc)
Provides:       tex(artemisiasc8a.tfm)
Provides:       tex(artemisiasc8a.vf)
Provides:       tex(artemisiasc8r.tfm)
Provides:       tex(artemisiasc9a.tfm)
Provides:       tex(artemisiasc9a.vf)
Provides:       tex(artemisiasc9r.tfm)
Provides:       tex(artemisiasco8a.tfm)
Provides:       tex(artemisiasco8a.vf)
Provides:       tex(artemisiasco8r.tfm)
Provides:       tex(artemisiasco9a.tfm)
Provides:       tex(artemisiasco9a.vf)
Provides:       tex(artemisiasco9r.tfm)
Provides:       tex(artemisiatabnums.enc)
Provides:       tex(artemisiatabnums8a.tfm)
Provides:       tex(artemisiatabnums8a.vf)
Provides:       tex(artemisiatabnums8r.tfm)
Provides:       tex(gartemisiab6a.tfm)
Provides:       tex(gartemisiab6a.vf)
Provides:       tex(gartemisiab6r.tfm)
Provides:       tex(gartemisiabi6a.tfm)
Provides:       tex(gartemisiabi6a.vf)
Provides:       tex(gartemisiabi6r.tfm)
Provides:       tex(gartemisiabo6a.tfm)
Provides:       tex(gartemisiabo6a.vf)
Provides:       tex(gartemisiabo6r.tfm)
Provides:       tex(gartemisiai6a.tfm)
Provides:       tex(gartemisiai6a.vf)
Provides:       tex(gartemisiai6r.tfm)
Provides:       tex(gartemisiao6a.tfm)
Provides:       tex(gartemisiao6a.vf)
Provides:       tex(gartemisiao6r.tfm)
Provides:       tex(gartemisiarg6a.tfm)
Provides:       tex(gartemisiarg6a.vf)
Provides:       tex(gartemisiarg6r.tfm)
Provides:       tex(gartemisiasc6a.tfm)
Provides:       tex(gartemisiasc6a.vf)
Provides:       tex(gartemisiasc6r.tfm)
Provides:       tex(gartemisiasco6a.tfm)
Provides:       tex(gartemisiasco6a.vf)
Provides:       tex(gartemisiasco6r.tfm)
Provides:       tex(gfsartemisia-euler.sty)
Provides:       tex(gfsartemisia.map)
Provides:       tex(gfsartemisia.sty)
Provides:       tex(lgrartemisia.fd)
Provides:       tex(lgrartemisiaeuler.fd)
Provides:       tex(ot1artemisia.fd)
Provides:       tex(ot1artemisiaeuler.fd)
Provides:       tex(t1artemisia.fd)
Provides:       tex(t1artemisiaeuler.fd)
Provides:       tex(uartemisiaeulernums.fd)
Provides:       tex(uartemisianums.fd)
Requires:       tex(euler.sty)
Requires:       tex(txfonts.sty)
Requires:       tex(txmi.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source240:      gfsartemisia.tar.xz
Source241:      gfsartemisia.doc.tar.xz

%description -n texlive-gfsartemisia
GFS Artemisia is a relatively modern font, designed as a
'general purpose' font in the same sense as Times is nowadays
treated. The present version has been provided by the Greek
Font Society. The font supports the Greek and Latin alphabets.
LaTeX support is provided, using the OT1, T1 and LGR encodings.

%package -n texlive-gfsartemisia-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19469
Release:        0
Summary:        Documentation for texlive-gfsartemisia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsartemisia-doc
This package includes the documentation for texlive-gfsartemisia


%package -n texlive-gfsartemisia-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19469
Release:        0
Summary:        Severed fonts for texlive-gfsartemisia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsartemisia-fonts
The  separated fonts package for texlive-gfsartemisia
%post -n texlive-gfsartemisia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfsartemisia.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfsartemisia 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfsartemisia.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfsartemisia
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsartemisia-fonts
%files -n texlive-gfsartemisia-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsartemisia/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfsartemisia/OFL.txt
%{_texmfdistdir}/doc/fonts/gfsartemisia/README
%{_texmfdistdir}/doc/fonts/gfsartemisia/README.TEXLIVE
%{_texmfdistdir}/doc/fonts/gfsartemisia/gfsartemisia.pdf
%{_texmfdistdir}/doc/fonts/gfsartemisia/gfsartemisia.tex

%files -n texlive-gfsartemisia
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsartemisia/GFSArtemisia-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisia.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiadenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiaec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiaecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiael.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiaelsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiamath.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisianumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiasc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsartemisia/artemisiatabnums.enc
%{_texmfdistdir}/fonts/map/dvips/gfsartemisia/gfsartemisia.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisia.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisiaBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisiaBoldIt.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsartemisia/GFSArtemisiaIt.otf
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiab9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiabo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiadenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiadenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiai9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiamath8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiamath8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisianumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisianumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiao9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiarg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiasco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiatabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/artemisiatabnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiab6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiab6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabo6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiabo6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiai6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiai6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiao6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiao6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiarg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiarg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsartemisia/gartemisiasco6r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsartemisia/GFSArtemisia-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiab8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiab9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiabo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiadenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiai8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiai9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiamath8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisianumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiao8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiao9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiarg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiarg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiasco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/artemisiatabnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiab6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiabi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiabo6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiai6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiao6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiarg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiasc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsartemisia/gartemisiasco6a.vf
%{_texmfdistdir}/tex/latex/gfsartemisia/gfsartemisia-euler.sty
%{_texmfdistdir}/tex/latex/gfsartemisia/gfsartemisia.sty
%{_texmfdistdir}/tex/latex/gfsartemisia/lgrartemisia.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/lgrartemisiaeuler.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/ot1artemisia.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/ot1artemisiaeuler.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/t1artemisia.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/t1artemisiaeuler.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/uartemisiaeulernums.fd
%{_texmfdistdir}/tex/latex/gfsartemisia/uartemisianums.fd

%files -n texlive-gfsartemisia-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsartemisia
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsartemisia.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfsartemisia.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfsartemisia.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsartemisia/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsartemisia/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsartemisia/fonts.scale
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisia.otf
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisiaBold.otf
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisiaBoldIt.otf
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisiaIt.otf
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisia-Bold.pfb
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisia-BoldItalic.pfb
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisia-Italic.pfb
%{_datadir}/fonts/texlive-gfsartemisia/GFSArtemisia-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsartemisia-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn19469-%{release}-zypper
%endif

%package -n texlive-gfsbaskerville
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19440
Release:        0
Summary:        A Greek font, from one such by Baskerville
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
Requires:       texlive-gfsbaskerville-fonts >= %{texlive_version}
Recommends:     texlive-gfsbaskerville-doc >= %{texlive_version}
Provides:       tex(gfsbaskerville.map)
Provides:       tex(gfsbaskerville.sty)
Provides:       tex(ggfsbaskervillerg6a.tfm)
Provides:       tex(ggfsbaskervillerg6a.vf)
Provides:       tex(ggfsbaskervillerg6r.tfm)
Provides:       tex(gpgfsbaskerville.enc)
Provides:       tex(lgrgfsbaskerville.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source242:      gfsbaskerville.tar.xz
Source243:      gfsbaskerville.doc.tar.xz

%description -n texlive-gfsbaskerville
The font is a digital implementation of Baskerville's classic
Greek font, provided by the Greek Font Society. The font covers
Greek only, and LaTeX support provides for the use of LGR
encoding.

%package -n texlive-gfsbaskerville-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19440
Release:        0
Summary:        Documentation for texlive-gfsbaskerville
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsbaskerville-doc
This package includes the documentation for texlive-gfsbaskerville


%package -n texlive-gfsbaskerville-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19440
Release:        0
Summary:        Severed fonts for texlive-gfsbaskerville
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsbaskerville-fonts
The  separated fonts package for texlive-gfsbaskerville
%post -n texlive-gfsbaskerville
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfsbaskerville.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfsbaskerville 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfsbaskerville.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfsbaskerville
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsbaskerville-fonts
%files -n texlive-gfsbaskerville-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsbaskerville/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfsbaskerville/OFL.txt
%{_texmfdistdir}/doc/fonts/gfsbaskerville/README
%{_texmfdistdir}/doc/fonts/gfsbaskerville/README.TEXLIVE
%{_texmfdistdir}/doc/fonts/gfsbaskerville/gfsbaskerville.pdf
%{_texmfdistdir}/doc/fonts/gfsbaskerville/gfsbaskerville.tex

%files -n texlive-gfsbaskerville
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfsbaskerville/GFSBaskerville-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsbaskerville/gpgfsbaskerville.enc
%{_texmfdistdir}/fonts/map/dvips/gfsbaskerville/gfsbaskerville.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsbaskerville/GFSBaskerville.otf
%{_texmfdistdir}/fonts/tfm/public/gfsbaskerville/ggfsbaskervillerg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbaskerville/ggfsbaskervillerg6r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsbaskerville/GFSBaskerville-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsbaskerville/ggfsbaskervillerg6a.vf
%{_texmfdistdir}/tex/latex/gfsbaskerville/gfsbaskerville.sty
%{_texmfdistdir}/tex/latex/gfsbaskerville/lgrgfsbaskerville.fd

%files -n texlive-gfsbaskerville-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsbaskerville
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsbaskerville.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfsbaskerville.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfsbaskerville.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsbaskerville/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsbaskerville/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsbaskerville/fonts.scale
%{_datadir}/fonts/texlive-gfsbaskerville/GFSBaskerville.otf
%{_datadir}/fonts/texlive-gfsbaskerville/GFSBaskerville-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsbaskerville-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn19440-%{release}-zypper
%endif

%package -n texlive-gfsbodoni
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn28484
Release:        0
Summary:        A Greek and Latin font based on Bodoni
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
Requires:       texlive-gfsbodoni-fonts >= %{texlive_version}
Recommends:     texlive-gfsbodoni-doc >= %{texlive_version}
Provides:       tex(bodoni.enc)
Provides:       tex(bodonib8a.tfm)
Provides:       tex(bodonib8a.vf)
Provides:       tex(bodonib8r.tfm)
Provides:       tex(bodonib9a.tfm)
Provides:       tex(bodonib9a.vf)
Provides:       tex(bodonib9r.tfm)
Provides:       tex(bodonibi8a.tfm)
Provides:       tex(bodonibi8a.vf)
Provides:       tex(bodonibi8r.tfm)
Provides:       tex(bodonibi9a.tfm)
Provides:       tex(bodonibi9a.vf)
Provides:       tex(bodonibi9r.tfm)
Provides:       tex(bodonibo8a.tfm)
Provides:       tex(bodonibo8a.vf)
Provides:       tex(bodonibo8r.tfm)
Provides:       tex(bodonibo9a.tfm)
Provides:       tex(bodonibo9a.vf)
Provides:       tex(bodonibo9r.tfm)
Provides:       tex(bodonidenomnums.enc)
Provides:       tex(bodonidenomnums8a.tfm)
Provides:       tex(bodonidenomnums8a.vf)
Provides:       tex(bodonidenomnums8r.tfm)
Provides:       tex(bodoniec.enc)
Provides:       tex(bodoniecsc.enc)
Provides:       tex(bodoniel.enc)
Provides:       tex(bodonielsc.enc)
Provides:       tex(bodonii8a.tfm)
Provides:       tex(bodonii8a.vf)
Provides:       tex(bodonii8r.tfm)
Provides:       tex(bodonii9a.tfm)
Provides:       tex(bodonii9a.vf)
Provides:       tex(bodonii9r.tfm)
Provides:       tex(bodoninumnums.enc)
Provides:       tex(bodoninumnums8a.tfm)
Provides:       tex(bodoninumnums8a.vf)
Provides:       tex(bodoninumnums8r.tfm)
Provides:       tex(bodonio8a.tfm)
Provides:       tex(bodonio8a.vf)
Provides:       tex(bodonio8r.tfm)
Provides:       tex(bodonio9a.tfm)
Provides:       tex(bodonio9a.vf)
Provides:       tex(bodonio9r.tfm)
Provides:       tex(bodonirg8a.tfm)
Provides:       tex(bodonirg8a.vf)
Provides:       tex(bodonirg8r.tfm)
Provides:       tex(bodonirg9a.tfm)
Provides:       tex(bodonirg9a.vf)
Provides:       tex(bodonirg9r.tfm)
Provides:       tex(bodonisc.enc)
Provides:       tex(bodonisc8a.tfm)
Provides:       tex(bodonisc8a.vf)
Provides:       tex(bodonisc8r.tfm)
Provides:       tex(bodonisc9a.tfm)
Provides:       tex(bodonisc9a.vf)
Provides:       tex(bodonisc9r.tfm)
Provides:       tex(bodonisco8a.tfm)
Provides:       tex(bodonisco8a.vf)
Provides:       tex(bodonisco8r.tfm)
Provides:       tex(bodonisco9a.tfm)
Provides:       tex(bodonisco9a.vf)
Provides:       tex(bodonisco9r.tfm)
Provides:       tex(bodonitabnums.enc)
Provides:       tex(bodonitabnums8a.tfm)
Provides:       tex(bodonitabnums8a.vf)
Provides:       tex(bodonitabnums8r.tfm)
Provides:       tex(gbodonib6a.tfm)
Provides:       tex(gbodonib6a.vf)
Provides:       tex(gbodonib6r.tfm)
Provides:       tex(gbodonibi6a.tfm)
Provides:       tex(gbodonibi6a.vf)
Provides:       tex(gbodonibi6r.tfm)
Provides:       tex(gbodonibo6a.tfm)
Provides:       tex(gbodonibo6a.vf)
Provides:       tex(gbodonibo6r.tfm)
Provides:       tex(gbodonii6a.tfm)
Provides:       tex(gbodonii6a.vf)
Provides:       tex(gbodonii6r.tfm)
Provides:       tex(gbodonio6a.tfm)
Provides:       tex(gbodonio6a.vf)
Provides:       tex(gbodonio6r.tfm)
Provides:       tex(gbodonio9a.tfm)
Provides:       tex(gbodonio9a.vf)
Provides:       tex(gbodonirg6a.tfm)
Provides:       tex(gbodonirg6a.vf)
Provides:       tex(gbodonirg6r.tfm)
Provides:       tex(gbodonisc6a.tfm)
Provides:       tex(gbodonisc6a.vf)
Provides:       tex(gbodonisc6r.tfm)
Provides:       tex(gbodonisco6a.tfm)
Provides:       tex(gbodonisco6a.vf)
Provides:       tex(gbodonisco6r.tfm)
Provides:       tex(gfsbodoni.map)
Provides:       tex(gfsbodoni.sty)
Provides:       tex(lgrbodoni.fd)
Provides:       tex(ot1bodoni.fd)
Provides:       tex(t1bodoni.fd)
Provides:       tex(ubodoninums.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source244:      gfsbodoni.tar.xz
Source245:      gfsbodoni.doc.tar.xz

%description -n texlive-gfsbodoni
Bodoni's Greek fonts in the 18th century broke, for the first
time, with the Byzantine cursive tradition of Greek fonts. GFS
Bodoni resurrects his work for general use. The font family
supports both Greek and Latin letters. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings. The
fonts themselves are provided in Adobe Type 1 and OpenType
formats.

%package -n texlive-gfsbodoni-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn28484
Release:        0
Summary:        Documentation for texlive-gfsbodoni
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsbodoni-doc
This package includes the documentation for texlive-gfsbodoni


%package -n texlive-gfsbodoni-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn28484
Release:        0
Summary:        Severed fonts for texlive-gfsbodoni
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsbodoni-fonts
The  separated fonts package for texlive-gfsbodoni
%post -n texlive-gfsbodoni
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfsbodoni.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfsbodoni 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfsbodoni.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfsbodoni
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsbodoni-fonts
%files -n texlive-gfsbodoni-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsbodoni/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfsbodoni/OFL.txt
%{_texmfdistdir}/doc/fonts/gfsbodoni/README
%{_texmfdistdir}/doc/fonts/gfsbodoni/README.TEXLIVE
%{_texmfdistdir}/doc/fonts/gfsbodoni/gfsbodoni.pdf

%files -n texlive-gfsbodoni
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsbodoni/GFSBodoni-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoni.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonidenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoniec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoniecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoniel.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonielsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodoninumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonisc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsbodoni/bodonitabnums.enc
%{_texmfdistdir}/fonts/map/dvips/gfsbodoni/gfsbodoni.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoni.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoniBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoniBoldIt.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsbodoni/GFSBodoniIt.otf
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonib9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonibo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonidenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonidenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonii9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodoninumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodoninumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonio9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonirg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonisco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonitabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/bodonitabnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonib6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonib6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibo6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonibo6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonii6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonii6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonio6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonio6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonio9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonirg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonirg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsbodoni/gbodonisco6r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsbodoni/GFSBodoni-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonib8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonib9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonibo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonidenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonii8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonii9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodoninumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonio8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonio9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonirg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonirg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonisco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/bodonitabnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonib6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonibi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonibo6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonii6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonio6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonio9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonirg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonisc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsbodoni/gbodonisco6a.vf
%{_texmfdistdir}/tex/latex/gfsbodoni/gfsbodoni.sty
%{_texmfdistdir}/tex/latex/gfsbodoni/lgrbodoni.fd
%{_texmfdistdir}/tex/latex/gfsbodoni/ot1bodoni.fd
%{_texmfdistdir}/tex/latex/gfsbodoni/t1bodoni.fd
%{_texmfdistdir}/tex/latex/gfsbodoni/ubodoninums.fd

%files -n texlive-gfsbodoni-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsbodoni
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsbodoni.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfsbodoni.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfsbodoni.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsbodoni/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsbodoni/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsbodoni/fonts.scale
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoni.otf
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoniBold.otf
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoniBoldIt.otf
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoniIt.otf
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoni-Bold.pfb
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoni-BoldItalic.pfb
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoni-Italic.pfb
%{_datadir}/fonts/texlive-gfsbodoni/GFSBodoni-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsbodoni-fonts-%{texlive_version}.%{texlive_noarch}.1.01svn28484-%{release}-zypper
%endif

%package -n texlive-gfscomplutum
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19469
Release:        0
Summary:        A Greek font with a long history
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
Requires:       texlive-gfscomplutum-fonts >= %{texlive_version}
Recommends:     texlive-gfscomplutum-doc >= %{texlive_version}
Provides:       tex(gcomplutum8a.tfm)
Provides:       tex(gcomplutum8a.vf)
Provides:       tex(gcomplutum8r.tfm)
Provides:       tex(gcomplutumo8a.tfm)
Provides:       tex(gcomplutumo8a.vf)
Provides:       tex(gcomplutumo8r.tfm)
Provides:       tex(gfscomplutum.map)
Provides:       tex(gfscomplutum.sty)
Provides:       tex(gpcomplutum.enc)
Provides:       tex(lgrcomplutum.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source246:      gfscomplutum.tar.xz
Source247:      gfscomplutum.doc.tar.xz

%description -n texlive-gfscomplutum
GFS Complutum derives, via a long development, from a
minuscule-only font cut in the 16th century. An unsatisfactory
set of majuscules were added in the early 20th century, but its
author died before he could complete the revival of the font.
The Greek Font Society has released this version, which has a
new set of majuscules.

%package -n texlive-gfscomplutum-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19469
Release:        0
Summary:        Documentation for texlive-gfscomplutum
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfscomplutum-doc
This package includes the documentation for texlive-gfscomplutum


%package -n texlive-gfscomplutum-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn19469
Release:        0
Summary:        Severed fonts for texlive-gfscomplutum
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfscomplutum-fonts
The  separated fonts package for texlive-gfscomplutum
%post -n texlive-gfscomplutum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfscomplutum.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfscomplutum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfscomplutum.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfscomplutum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfscomplutum-fonts
%files -n texlive-gfscomplutum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfscomplutum/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfscomplutum/OFL.txt
%{_texmfdistdir}/doc/fonts/gfscomplutum/README
%{_texmfdistdir}/doc/fonts/gfscomplutum/README.TEXLIVE
%{_texmfdistdir}/doc/fonts/gfscomplutum/gfscomplutum.pdf
%{_texmfdistdir}/doc/fonts/gfscomplutum/gfscomplutum.tex

%files -n texlive-gfscomplutum
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfscomplutum/GFSComplutum-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfscomplutum/gpcomplutum.enc
%{_texmfdistdir}/fonts/map/dvips/gfscomplutum/gfscomplutum.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfscomplutum/GFSPolyglot.otf
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutum8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutum8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutumo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfscomplutum/gcomplutumo8r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfscomplutum/GFSComplutum-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfscomplutum/gcomplutum8a.vf
%{_texmfdistdir}/fonts/vf/public/gfscomplutum/gcomplutumo8a.vf
%{_texmfdistdir}/tex/latex/gfscomplutum/gfscomplutum.sty
%{_texmfdistdir}/tex/latex/gfscomplutum/lgrcomplutum.fd

%files -n texlive-gfscomplutum-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfscomplutum
%{_datadir}/fontconfig/conf.avail/58-texlive-gfscomplutum.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfscomplutum.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfscomplutum.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfscomplutum/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfscomplutum/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfscomplutum/fonts.scale
%{_datadir}/fonts/texlive-gfscomplutum/GFSPolyglot.otf
%{_datadir}/fonts/texlive-gfscomplutum/GFSComplutum-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfscomplutum-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn19469-%{release}-zypper
%endif

%package -n texlive-gfsdidot
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        A Greek font based on Didot's work
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
Requires:       texlive-gfsdidot-fonts >= %{texlive_version}
Recommends:     texlive-gfsdidot-doc >= %{texlive_version}
Provides:       tex(didot.enc)
Provides:       tex(didotOT1.enc)
Provides:       tex(didotOT1it.enc)
Provides:       tex(didotOT1sc.enc)
Provides:       tex(didotTS1.enc)
Provides:       tex(didotb7a.tfm)
Provides:       tex(didotb7a.vf)
Provides:       tex(didotb7r.tfm)
Provides:       tex(didotb8a.tfm)
Provides:       tex(didotb8a.vf)
Provides:       tex(didotb8r.tfm)
Provides:       tex(didotb9a.tfm)
Provides:       tex(didotb9a.vf)
Provides:       tex(didotb9r.tfm)
Provides:       tex(didotbi7a.tfm)
Provides:       tex(didotbi7a.vf)
Provides:       tex(didotbi7r.tfm)
Provides:       tex(didotbi8a.tfm)
Provides:       tex(didotbi8a.vf)
Provides:       tex(didotbi8r.tfm)
Provides:       tex(didotbi9a.tfm)
Provides:       tex(didotbi9a.vf)
Provides:       tex(didotbi9r.tfm)
Provides:       tex(didotbo7a.tfm)
Provides:       tex(didotbo7a.vf)
Provides:       tex(didotbo7r.tfm)
Provides:       tex(didotbo8a.tfm)
Provides:       tex(didotbo8a.vf)
Provides:       tex(didotbo8r.tfm)
Provides:       tex(didotbo9a.tfm)
Provides:       tex(didotbo9a.vf)
Provides:       tex(didotbo9r.tfm)
Provides:       tex(didotdenomnums.enc)
Provides:       tex(didotdenomnums8a.tfm)
Provides:       tex(didotdenomnums8a.vf)
Provides:       tex(didotdenomnums8r.tfm)
Provides:       tex(didotec.enc)
Provides:       tex(didoti7a.tfm)
Provides:       tex(didoti7a.vf)
Provides:       tex(didoti7r.tfm)
Provides:       tex(didoti8a.tfm)
Provides:       tex(didoti8a.vf)
Provides:       tex(didoti8r.tfm)
Provides:       tex(didoti9a.tfm)
Provides:       tex(didoti9a.vf)
Provides:       tex(didoti9r.tfm)
Provides:       tex(didotnumnums.enc)
Provides:       tex(didotnumnums8a.tfm)
Provides:       tex(didotnumnums8a.vf)
Provides:       tex(didotnumnums8r.tfm)
Provides:       tex(didoto7a.tfm)
Provides:       tex(didoto7a.vf)
Provides:       tex(didoto7r.tfm)
Provides:       tex(didoto8a.tfm)
Provides:       tex(didoto8a.vf)
Provides:       tex(didoto8r.tfm)
Provides:       tex(didoto9a.tfm)
Provides:       tex(didoto9a.vf)
Provides:       tex(didoto9r.tfm)
Provides:       tex(didotrg7a.tfm)
Provides:       tex(didotrg7a.vf)
Provides:       tex(didotrg7r.tfm)
Provides:       tex(didotrg8a.tfm)
Provides:       tex(didotrg8a.vf)
Provides:       tex(didotrg8r.tfm)
Provides:       tex(didotrg9a.tfm)
Provides:       tex(didotrg9a.vf)
Provides:       tex(didotrg9r.tfm)
Provides:       tex(didotsc7a.tfm)
Provides:       tex(didotsc7a.vf)
Provides:       tex(didotsc7r.tfm)
Provides:       tex(didotsc8a.tfm)
Provides:       tex(didotsc8a.vf)
Provides:       tex(didotsc8r.tfm)
Provides:       tex(didotsc9a.tfm)
Provides:       tex(didotsc9a.vf)
Provides:       tex(didotsc9r.tfm)
Provides:       tex(didotscb7a.tfm)
Provides:       tex(didotscb7a.vf)
Provides:       tex(didotscb7r.tfm)
Provides:       tex(didotscbo7a.tfm)
Provides:       tex(didotscbo7a.vf)
Provides:       tex(didotscbo7r.tfm)
Provides:       tex(didotsco7a.tfm)
Provides:       tex(didotsco7a.vf)
Provides:       tex(didotsco7r.tfm)
Provides:       tex(didotsco8a.tfm)
Provides:       tex(didotsco8a.vf)
Provides:       tex(didotsco8r.tfm)
Provides:       tex(didotsco9a.tfm)
Provides:       tex(didotsco9a.vf)
Provides:       tex(didotsco9r.tfm)
Provides:       tex(didottabnums.enc)
Provides:       tex(didottabnums8a.tfm)
Provides:       tex(didottabnums8a.vf)
Provides:       tex(didottabnums8r.tfm)
Provides:       tex(didotuecsc.enc)
Provides:       tex(didotui7a.tfm)
Provides:       tex(didotui7a.vf)
Provides:       tex(didotui7r.tfm)
Provides:       tex(didotui8a.tfm)
Provides:       tex(didotui8a.vf)
Provides:       tex(didotui8r.tfm)
Provides:       tex(didotui9a.tfm)
Provides:       tex(didotui9a.vf)
Provides:       tex(didotui9r.tfm)
Provides:       tex(didotusc.enc)
Provides:       tex(gdidotb6a.tfm)
Provides:       tex(gdidotb6a.vf)
Provides:       tex(gdidotb6r.tfm)
Provides:       tex(gdidotbi6a.tfm)
Provides:       tex(gdidotbi6a.vf)
Provides:       tex(gdidotbi6r.tfm)
Provides:       tex(gdidoti6a.tfm)
Provides:       tex(gdidoti6a.vf)
Provides:       tex(gdidoti6r.tfm)
Provides:       tex(gdidotrg6a.tfm)
Provides:       tex(gdidotrg6a.vf)
Provides:       tex(gdidotrg6r.tfm)
Provides:       tex(gdidotsc6a.tfm)
Provides:       tex(gdidotsc6a.vf)
Provides:       tex(gdidotsc6r.tfm)
Provides:       tex(gdidotsco6a.tfm)
Provides:       tex(gdidotsco6a.vf)
Provides:       tex(gdidotsco6r.tfm)
Provides:       tex(gfsdidot.map)
Provides:       tex(gfsdidot.sty)
Provides:       tex(gfsudidotmath.enc)
Provides:       tex(gfsudidotmath8a.tfm)
Provides:       tex(gfsudidotmath8a.vf)
Provides:       tex(gfsudidotmath8r.tfm)
Provides:       tex(golgai6a.tfm)
Provides:       tex(golgai6a.vf)
Provides:       tex(golgai6r.tfm)
Provides:       tex(golgaui6a.tfm)
Provides:       tex(golgaui6a.vf)
Provides:       tex(golgaui6r.tfm)
Provides:       tex(gpdidot.enc)
Provides:       tex(gpdidoti.enc)
Provides:       tex(gpdidotusc.enc)
Provides:       tex(gpolga.enc)
Provides:       tex(lgrudidot.fd)
Provides:       tex(omludidot.fd)
Provides:       tex(ot1udidot.fd)
Provides:       tex(t1udidot.fd)
Provides:       tex(testDidot.sty)
Provides:       tex(ts1-gfsdidotb-raw.tfm)
Provides:       tex(ts1-gfsdidotb.tfm)
Provides:       tex(ts1-gfsdidotb.vf)
Provides:       tex(ts1-gfsdidotbi-raw.tfm)
Provides:       tex(ts1-gfsdidotbi.tfm)
Provides:       tex(ts1-gfsdidotbi.vf)
Provides:       tex(ts1-gfsdidotbo-raw.tfm)
Provides:       tex(ts1-gfsdidotbo.tfm)
Provides:       tex(ts1-gfsdidotbo.vf)
Provides:       tex(ts1-gfsdidoto-raw.tfm)
Provides:       tex(ts1-gfsdidoto.tfm)
Provides:       tex(ts1-gfsdidoto.vf)
Provides:       tex(ts1-gfsdidotr-raw.tfm)
Provides:       tex(ts1-gfsdidotr.tfm)
Provides:       tex(ts1-gfsdidotr.vf)
Provides:       tex(ts1-gfsdidotri-raw.tfm)
Provides:       tex(ts1-gfsdidotri.tfm)
Provides:       tex(ts1-gfsdidotri.vf)
Provides:       tex(ts1-gfsdidotui-raw.tfm)
Provides:       tex(ts1-gfsdidotui.tfm)
Provides:       tex(ts1-gfsdidotui.vf)
Provides:       tex(ts1udidot.fd)
Provides:       tex(uudidotnums.fd)
Requires:       tex(cmbx10.tfm)
Requires:       tex(cmbxti10.tfm)
Requires:       tex(cmr10.tfm)
Requires:       tex(cmti10.tfm)
Requires:       tex(cs-qplb.tfm)
Requires:       tex(cs-qplbi.tfm)
Requires:       tex(cs-qplr.tfm)
Requires:       tex(cs-qplri.tfm)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(pxfonts.sty)
Requires:       tex(pxmi.tfm)
Requires:       tex(textcomp.sty)
Requires:       tex(ts1-qplb.tfm)
Requires:       tex(ts1-qplbi.tfm)
Requires:       tex(ts1-qplr.tfm)
Requires:       tex(ts1-qplri.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source248:      gfsdidot.tar.xz
Source249:      gfsdidot.doc.tar.xz

%description -n texlive-gfsdidot
The design of Didot's 1805 Greek typeface was influenced by the
neoclassical ideals of the late 18th century. The font was
brought to Greece at the time of the 1821 Greek Revolution, by
Didot's son, and was very widely used. The present version is
provided by the Greek Font Society. The font supports the Greek
alphabet, and is accompanied by a matching Latin alphabet based
on Zapf's Palatino. LaTeX support is provided, using the OT1,
T1, TS1, and LGR encodings.

%package -n texlive-gfsdidot-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Documentation for texlive-gfsdidot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsdidot-doc
This package includes the documentation for texlive-gfsdidot


%package -n texlive-gfsdidot-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Severed fonts for texlive-gfsdidot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsdidot-fonts
The  separated fonts package for texlive-gfsdidot
%post -n texlive-gfsdidot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfsdidot.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfsdidot 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfsdidot.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfsdidot
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsdidot-fonts
%files -n texlive-gfsdidot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsdidot/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfsdidot/OFL.txt
%{_texmfdistdir}/doc/fonts/gfsdidot/README
%{_texmfdistdir}/doc/fonts/gfsdidot/README.TEXLIVE
%{_texmfdistdir}/doc/fonts/gfsdidot/Readme.txt
%{_texmfdistdir}/doc/fonts/gfsdidot/didotb7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotbi7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotbo7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didoti7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didoto7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotrg7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotsc7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotscb7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotscbo7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotsco7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/didotui7a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/gdidotb6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/gdidotbi6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/gdidoti6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/gdidotrg6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/gdidotsc6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/gdidotsco6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/gfsudidotmath8a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/golgai6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/golgaui6a.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/installDidot.pl
%{_texmfdistdir}/doc/fonts/gfsdidot/showDidotFontsLaTeX.tex
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidot_model.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidot_model_1.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidotb.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidotbi.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidotbo.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidoto.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidotr.vpl
%{_texmfdistdir}/doc/fonts/gfsdidot/ts1-gfsdidotui.vpl

%files -n texlive-gfsdidot
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSDidot.afm
%{_texmfdistdir}/fonts/afm/public/gfsdidot/GFSOlga.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didot.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotOT1.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotOT1it.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotOT1sc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotTS1.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotdenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotnumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didottabnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotuecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/didotusc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gfsudidotmath.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpdidot.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpdidoti.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpdidotusc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsdidot/gpolga.enc
%{_texmfdistdir}/fonts/map/dvips/gfsdidot/gfsdidot.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidot.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidotBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidotBoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSDidotItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsdidot/GFSOlga.otf
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotb9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotbo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotdenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotdenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoti9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotnumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotnumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didoto9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotrg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotscb7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotscb7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotscbo7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotscbo7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotsco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didottabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didottabnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui7a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui7r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/didotui9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotbi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotbi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidoti6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidoti6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotrg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gdidotsco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gfsudidotmath8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/gfsudidotmath8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgai6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgai6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgaui6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/golgaui6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotb-raw.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotb.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotbi-raw.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotbi.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotbo-raw.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotbo.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidoto-raw.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidoto.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotr-raw.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotr.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotri-raw.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotri.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotui-raw.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsdidot/ts1-gfsdidotui.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSDidot.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsdidot/GFSOlga.pfb
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotb7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotb8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotb9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbi7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbo7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotbo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotdenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoti7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoti8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoti9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotnumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoto7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoto8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didoto9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotrg7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotrg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotrg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsc7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotscb7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotscbo7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsco7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotsco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didottabnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotui7a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotui8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/didotui9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotb6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotbi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidoti6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotrg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotsc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gdidotsco6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/gfsudidotmath8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/golgai6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/golgaui6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/ts1-gfsdidotb.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/ts1-gfsdidotbi.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/ts1-gfsdidotbo.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/ts1-gfsdidoto.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/ts1-gfsdidotr.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/ts1-gfsdidotri.vf
%{_texmfdistdir}/fonts/vf/public/gfsdidot/ts1-gfsdidotui.vf
%{_texmfdistdir}/tex/latex/gfsdidot/gfsdidot.sty
%{_texmfdistdir}/tex/latex/gfsdidot/lgrudidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/omludidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/ot1udidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/t1udidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/testDidot.sty
%{_texmfdistdir}/tex/latex/gfsdidot/ts1udidot.fd
%{_texmfdistdir}/tex/latex/gfsdidot/uudidotnums.fd

%files -n texlive-gfsdidot-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsdidot
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsdidot.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfsdidot.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfsdidot.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsdidot/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsdidot/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsdidot/fonts.scale
%{_datadir}/fonts/texlive-gfsdidot/GFSDidot.otf
%{_datadir}/fonts/texlive-gfsdidot/GFSDidotBold.otf
%{_datadir}/fonts/texlive-gfsdidot/GFSDidotBoldItalic.otf
%{_datadir}/fonts/texlive-gfsdidot/GFSDidotItalic.otf
%{_datadir}/fonts/texlive-gfsdidot/GFSOlga.otf
%{_datadir}/fonts/texlive-gfsdidot/GFSDidot-Bold.pfb
%{_datadir}/fonts/texlive-gfsdidot/GFSDidot-BoldItalic.pfb
%{_datadir}/fonts/texlive-gfsdidot/GFSDidot-Italic.pfb
%{_datadir}/fonts/texlive-gfsdidot/GFSDidot.pfb
%{_datadir}/fonts/texlive-gfsdidot/GFSOlga.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsdidot-fonts-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif

%package -n texlive-gfsdidotclassic
Version:        %{texlive_version}.%{texlive_noarch}.001.001svn52778
Release:        0
Summary:        The classic version of GFSDidot
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-gfsdidotclassic-fonts >= %{texlive_version}
Recommends:     texlive-gfsdidotclassic-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source250:      gfsdidotclassic.tar.xz
Source251:      gfsdidotclassic.doc.tar.xz

%description -n texlive-gfsdidotclassic
The classic version of GFSDidot provided for Unicode TeX
engines.

%package -n texlive-gfsdidotclassic-doc
Version:        %{texlive_version}.%{texlive_noarch}.001.001svn52778
Release:        0
Summary:        Documentation for texlive-gfsdidotclassic
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsdidotclassic-doc
This package includes the documentation for texlive-gfsdidotclassic


%package -n texlive-gfsdidotclassic-fonts
Version:        %{texlive_version}.%{texlive_noarch}.001.001svn52778
Release:        0
Summary:        Severed fonts for texlive-gfsdidotclassic
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsdidotclassic-fonts
The  separated fonts package for texlive-gfsdidotclassic
%post -n texlive-gfsdidotclassic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gfsdidotclassic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gfsdidotclassic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsdidotclassic-fonts
%files -n texlive-gfsdidotclassic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsdidotclassic/README
%{_texmfdistdir}/doc/fonts/gfsdidotclassic/README.TEXLIVE

%files -n texlive-gfsdidotclassic
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsdidotclassic/GFSDidot_Classic.otf

%files -n texlive-gfsdidotclassic-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsdidotclassic
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsdidotclassic.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsdidotclassic/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsdidotclassic/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsdidotclassic/fonts.scale
%{_datadir}/fonts/texlive-gfsdidotclassic/GFSDidot_Classic.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsdidotclassic-fonts-%{texlive_version}.%{texlive_noarch}.001.001svn52778-%{release}-zypper
%endif

%package -n texlive-gfsneohellenic
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        A font in the Neo-Hellenic style
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
Requires:       texlive-gfsneohellenic-fonts >= %{texlive_version}
Recommends:     texlive-gfsneohellenic-doc >= %{texlive_version}
Provides:       tex(gfsneohellenic.map)
Provides:       tex(gfsneohellenic.sty)
Provides:       tex(gfsneohellenicmath8a.tfm)
Provides:       tex(gfsneohellenicmath8a.vf)
Provides:       tex(gfsneohellenicmath8r.tfm)
Provides:       tex(gneohellenicb6a.tfm)
Provides:       tex(gneohellenicb6a.vf)
Provides:       tex(gneohellenicb6r.tfm)
Provides:       tex(gneohellenicbi6a.tfm)
Provides:       tex(gneohellenicbi6a.vf)
Provides:       tex(gneohellenicbi6r.tfm)
Provides:       tex(gneohellenicbo6a.tfm)
Provides:       tex(gneohellenicbo6a.vf)
Provides:       tex(gneohellenicbo6r.tfm)
Provides:       tex(gneohellenici6a.tfm)
Provides:       tex(gneohellenici6a.vf)
Provides:       tex(gneohellenici6r.tfm)
Provides:       tex(gneohellenico6a.tfm)
Provides:       tex(gneohellenico6a.vf)
Provides:       tex(gneohellenico6r.tfm)
Provides:       tex(gneohellenicrg6a.tfm)
Provides:       tex(gneohellenicrg6a.vf)
Provides:       tex(gneohellenicrg6r.tfm)
Provides:       tex(gneohellenicsc6a.tfm)
Provides:       tex(gneohellenicsc6a.vf)
Provides:       tex(gneohellenicsc6r.tfm)
Provides:       tex(gneohellenicsco6a.tfm)
Provides:       tex(gneohellenicsco6a.vf)
Provides:       tex(gneohellenicsco6r.tfm)
Provides:       tex(lgrneohellenic.fd)
Provides:       tex(neohellenic.enc)
Provides:       tex(neohellenicb8a.tfm)
Provides:       tex(neohellenicb8a.vf)
Provides:       tex(neohellenicb8r.tfm)
Provides:       tex(neohellenicb9a.tfm)
Provides:       tex(neohellenicb9a.vf)
Provides:       tex(neohellenicb9r.tfm)
Provides:       tex(neohellenicbi8a.tfm)
Provides:       tex(neohellenicbi8a.vf)
Provides:       tex(neohellenicbi8r.tfm)
Provides:       tex(neohellenicbi9a.tfm)
Provides:       tex(neohellenicbi9a.vf)
Provides:       tex(neohellenicbi9r.tfm)
Provides:       tex(neohellenicbo8a.tfm)
Provides:       tex(neohellenicbo8a.vf)
Provides:       tex(neohellenicbo8r.tfm)
Provides:       tex(neohellenicbo9a.tfm)
Provides:       tex(neohellenicbo9a.vf)
Provides:       tex(neohellenicbo9r.tfm)
Provides:       tex(neohellenicdenomnums.enc)
Provides:       tex(neohellenicdenomnums8a.tfm)
Provides:       tex(neohellenicdenomnums8a.vf)
Provides:       tex(neohellenicdenomnums8r.tfm)
Provides:       tex(neohellenicec.enc)
Provides:       tex(neohellenicecsc.enc)
Provides:       tex(neohellenicel.enc)
Provides:       tex(neohellenicelsc.enc)
Provides:       tex(neohellenici8a.tfm)
Provides:       tex(neohellenici8a.vf)
Provides:       tex(neohellenici8r.tfm)
Provides:       tex(neohellenici9a.tfm)
Provides:       tex(neohellenici9a.vf)
Provides:       tex(neohellenici9r.tfm)
Provides:       tex(neohellenicmath.enc)
Provides:       tex(neohellenicnumnums.enc)
Provides:       tex(neohellenicnumnums8a.tfm)
Provides:       tex(neohellenicnumnums8a.vf)
Provides:       tex(neohellenicnumnums8r.tfm)
Provides:       tex(neohellenico8a.tfm)
Provides:       tex(neohellenico8a.vf)
Provides:       tex(neohellenico8r.tfm)
Provides:       tex(neohellenico9a.tfm)
Provides:       tex(neohellenico9a.vf)
Provides:       tex(neohellenico9r.tfm)
Provides:       tex(neohellenicrg8a.tfm)
Provides:       tex(neohellenicrg8a.vf)
Provides:       tex(neohellenicrg8r.tfm)
Provides:       tex(neohellenicrg9a.tfm)
Provides:       tex(neohellenicrg9a.vf)
Provides:       tex(neohellenicrg9r.tfm)
Provides:       tex(neohellenicsc.enc)
Provides:       tex(neohellenicsc8a.tfm)
Provides:       tex(neohellenicsc8a.vf)
Provides:       tex(neohellenicsc8r.tfm)
Provides:       tex(neohellenicsc9a.tfm)
Provides:       tex(neohellenicsc9a.vf)
Provides:       tex(neohellenicsc9r.tfm)
Provides:       tex(neohellenicsco8a.tfm)
Provides:       tex(neohellenicsco8a.vf)
Provides:       tex(neohellenicsco8r.tfm)
Provides:       tex(neohellenicsco9a.tfm)
Provides:       tex(neohellenicsco9a.vf)
Provides:       tex(neohellenicsco9r.tfm)
Provides:       tex(neohellenictabnums.enc)
Provides:       tex(neohellenictabnums8a.tfm)
Provides:       tex(neohellenictabnums8a.vf)
Provides:       tex(neohellenictabnums8r.tfm)
Provides:       tex(omlneohellenic.fd)
Provides:       tex(ot1neohellenic.fd)
Provides:       tex(t1neohellenic.fd)
Provides:       tex(uneohellenicnums.fd)
Requires:       tex(cmbrmi10.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source252:      gfsneohellenic.tar.xz
Source253:      gfsneohellenic.doc.tar.xz

%description -n texlive-gfsneohellenic
The NeoHellenic style evolved in academic circles in the 19th
and 20th century; the present font follows a cut commissioned
from Monotype in 1927. The present version was provided by the
Greek Font Society. The font supports both Greek and Latin
characters, and has been adjusted to work well with the
cmbright fonts for mathematics support. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings.

%package -n texlive-gfsneohellenic-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Documentation for texlive-gfsneohellenic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsneohellenic-doc
This package includes the documentation for texlive-gfsneohellenic


%package -n texlive-gfsneohellenic-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Severed fonts for texlive-gfsneohellenic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsneohellenic-fonts
The  separated fonts package for texlive-gfsneohellenic
%post -n texlive-gfsneohellenic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfsneohellenic.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfsneohellenic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfsneohellenic.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfsneohellenic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsneohellenic-fonts
%files -n texlive-gfsneohellenic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsneohellenic/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfsneohellenic/OFL.txt
%{_texmfdistdir}/doc/fonts/gfsneohellenic/README
%{_texmfdistdir}/doc/fonts/gfsneohellenic/README.TEXLIVE
%{_texmfdistdir}/doc/fonts/gfsneohellenic/VERSION

%files -n texlive-gfsneohellenic
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Bold.afm
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Italic.afm
%{_texmfdistdir}/fonts/afm/public/gfsneohellenic/GFSNeohellenic-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenic.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicdenomnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicec.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicel.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicelsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicmath.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicnumnums.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenicsc.enc
%{_texmfdistdir}/fonts/enc/dvips/gfsneohellenic/neohellenictabnums.enc
%{_texmfdistdir}/fonts/map/dvips/gfsneohellenic/gfsneohellenic.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenicBoldIt.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/GFSNeohellenicIt.otf
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gfsneohellenicmath8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gfsneohellenicmath8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicb6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicb6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbi6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbi6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbo6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicbo6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenici6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenici6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenico6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenico6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicrg6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsc6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsc6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsco6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/gneohellenicsco6r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicb9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbi9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicbo9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicdenomnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicdenomnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenici9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicnumnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicnumnums8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenico9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicrg9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsc9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco9a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenicsco9r.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenictabnums8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsneohellenic/neohellenictabnums8r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsneohellenic/GFSNeohellenic-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gfsneohellenicmath8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicb6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicbi6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicbo6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenici6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenico6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicrg6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicsc6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/gneohellenicsco6a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicb8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicb9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbi8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbi9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbo8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicbo9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicdenomnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenici8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenici9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicnumnums8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenico8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenico9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicrg8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicrg9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsc8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsc9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsco8a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenicsco9a.vf
%{_texmfdistdir}/fonts/vf/public/gfsneohellenic/neohellenictabnums8a.vf
%{_texmfdistdir}/tex/latex/gfsneohellenic/gfsneohellenic.sty
%{_texmfdistdir}/tex/latex/gfsneohellenic/lgrneohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/omlneohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/ot1neohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/t1neohellenic.fd
%{_texmfdistdir}/tex/latex/gfsneohellenic/uneohellenicnums.fd

%files -n texlive-gfsneohellenic-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsneohellenic
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsneohellenic.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfsneohellenic.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfsneohellenic.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsneohellenic/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsneohellenic/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsneohellenic/fonts.scale
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenic.otf
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenicBold.otf
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenicBoldIt.otf
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenicIt.otf
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenic-Bold.pfb
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenic-BoldItalic.pfb
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenic-Italic.pfb
%{_datadir}/fonts/texlive-gfsneohellenic/GFSNeohellenic-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsneohellenic-fonts-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif

%package -n texlive-gfsneohellenicmath
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn52570
Release:        0
Summary:        A Greek math font in the Neo-Hellenic style
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
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-gfsneohellenicmath-fonts >= %{texlive_version}
Recommends:     texlive-gfsneohellenicmath-doc >= %{texlive_version}
Provides:       tex(gfsneohellenicot.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(unicode-math.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source254:      gfsneohellenicmath.tar.xz
Source255:      gfsneohellenicmath.doc.tar.xz

%description -n texlive-gfsneohellenicmath
The GFSNeohellenic font, a historic font first designed by
Victor Scholderer, and digitized by George Matthiopoulos of the
Greek Font Society (GFS), now has native support for
Mathematics. The project was commissioned to GFS by the
Department of Mathematics of the University of the Aegean,
Samos, Greece. The Math Table was constructed by the
Mathematics Professor A. Tsolomitis. A useful application is in
beamer documents since this is a Sans Math font. The
GFSNeohellenic fontfamily supports many languages (including
Greek), and it is distributed (both text and math) under the
OFL license.

%package -n texlive-gfsneohellenicmath-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn52570
Release:        0
Summary:        Documentation for texlive-gfsneohellenicmath
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsneohellenicmath-doc
This package includes the documentation for texlive-gfsneohellenicmath


%package -n texlive-gfsneohellenicmath-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn52570
Release:        0
Summary:        Severed fonts for texlive-gfsneohellenicmath
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsneohellenicmath-fonts
The  separated fonts package for texlive-gfsneohellenicmath
%post -n texlive-gfsneohellenicmath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gfsneohellenicmath 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gfsneohellenicmath
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsneohellenicmath-fonts
%files -n texlive-gfsneohellenicmath-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsneohellenicmath/MathematicsCheatSheet.pdf
%{_texmfdistdir}/doc/fonts/gfsneohellenicmath/README

%files -n texlive-gfsneohellenicmath
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsneohellenicmath/GFSNeohellenicMath.otf
%{_texmfdistdir}/tex/latex/gfsneohellenicmath/gfsneohellenicot.sty

%files -n texlive-gfsneohellenicmath-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsneohellenicmath
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsneohellenicmath.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsneohellenicmath/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsneohellenicmath/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsneohellenicmath/fonts.scale
%{_datadir}/fonts/texlive-gfsneohellenicmath/GFSNeohellenicMath.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsneohellenicmath-fonts-%{texlive_version}.%{texlive_noarch}.1.0.1svn52570-%{release}-zypper
%endif

%package -n texlive-gfsporson
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn18651
Release:        0
Summary:        A Greek font, originally from Porson
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
Requires:       texlive-gfsporson-fonts >= %{texlive_version}
Recommends:     texlive-gfsporson-doc >= %{texlive_version}
Provides:       tex(gfsporson.map)
Provides:       tex(gfsporson.sty)
Provides:       tex(gporsonrg6a.tfm)
Provides:       tex(gporsonrg6a.vf)
Provides:       tex(gporsonrg6r.tfm)
Provides:       tex(lgrporson.fd)
Provides:       tex(porsonel.enc)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source256:      gfsporson.tar.xz
Source257:      gfsporson.doc.tar.xz

%description -n texlive-gfsporson
Porson is an elegant Greek font, originally cut at the turn of
the 19th Century in England. The present version has been
provided by the Greek Font Society. The font supports the Greek
alphabet only. LaTeX support is provided, using the LGR
encoding.

%package -n texlive-gfsporson-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn18651
Release:        0
Summary:        Documentation for texlive-gfsporson
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfsporson-doc
This package includes the documentation for texlive-gfsporson


%package -n texlive-gfsporson-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn18651
Release:        0
Summary:        Severed fonts for texlive-gfsporson
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfsporson-fonts
The  separated fonts package for texlive-gfsporson
%post -n texlive-gfsporson
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfsporson.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfsporson 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfsporson.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfsporson
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfsporson-fonts
%files -n texlive-gfsporson-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfsporson/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfsporson/OFL.txt
%{_texmfdistdir}/doc/fonts/gfsporson/README
%{_texmfdistdir}/doc/fonts/gfsporson/gfsporson.pdf
%{_texmfdistdir}/doc/fonts/gfsporson/gfsporson.tex

%files -n texlive-gfsporson
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfsporson/GFSPorson-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfsporson/porsonel.enc
%{_texmfdistdir}/fonts/map/dvips/gfsporson/gfsporson.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfsporson/GFSPorson.otf
%{_texmfdistdir}/fonts/tfm/public/gfsporson/gporsonrg6a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfsporson/gporsonrg6r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfsporson/GFSPorson-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfsporson/gporsonrg6a.vf
%{_texmfdistdir}/tex/latex/gfsporson/gfsporson.sty
%{_texmfdistdir}/tex/latex/gfsporson/lgrporson.fd

%files -n texlive-gfsporson-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfsporson
%{_datadir}/fontconfig/conf.avail/58-texlive-gfsporson.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfsporson.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfsporson.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsporson/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsporson/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfsporson/fonts.scale
%{_datadir}/fonts/texlive-gfsporson/GFSPorson.otf
%{_datadir}/fonts/texlive-gfsporson/GFSPorson-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfsporson-fonts-%{texlive_version}.%{texlive_noarch}.1.01svn18651-%{release}-zypper
%endif

%package -n texlive-gfssolomos
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18651
Release:        0
Summary:        A Greek-alphabet font
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
Requires:       texlive-gfssolomos-fonts >= %{texlive_version}
Recommends:     texlive-gfssolomos-doc >= %{texlive_version}
Provides:       tex(gfssolomos.map)
Provides:       tex(gfssolomos.sty)
Provides:       tex(gpsolomos.enc)
Provides:       tex(gsolomos8a.tfm)
Provides:       tex(gsolomos8a.vf)
Provides:       tex(gsolomos8r.tfm)
Provides:       tex(lgrsolomos.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source258:      gfssolomos.tar.xz
Source259:      gfssolomos.doc.tar.xz

%description -n texlive-gfssolomos
Solomos is a font which traces its descent from a
calligraphically-inspired font of the mid-19th century. LaTeX
support, for use with the LGR encoding only, is provided.

%package -n texlive-gfssolomos-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18651
Release:        0
Summary:        Documentation for texlive-gfssolomos
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gfssolomos-doc
This package includes the documentation for texlive-gfssolomos


%package -n texlive-gfssolomos-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18651
Release:        0
Summary:        Severed fonts for texlive-gfssolomos
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gfssolomos-fonts
The  separated fonts package for texlive-gfssolomos
%post -n texlive-gfssolomos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gfssolomos.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gfssolomos 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gfssolomos.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gfssolomos
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gfssolomos-fonts
%files -n texlive-gfssolomos-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gfssolomos/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/gfssolomos/OFL.txt
%{_texmfdistdir}/doc/fonts/gfssolomos/README
%{_texmfdistdir}/doc/fonts/gfssolomos/gfssolomos.pdf
%{_texmfdistdir}/doc/fonts/gfssolomos/gfssolomos.tex

%files -n texlive-gfssolomos
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/gfssolomos/GFSSolomos-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/gfssolomos/gpsolomos.enc
%{_texmfdistdir}/fonts/map/dvips/gfssolomos/gfssolomos.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gfssolomos/GFSSolomos.otf
%{_texmfdistdir}/fonts/tfm/public/gfssolomos/gsolomos8a.tfm
%{_texmfdistdir}/fonts/tfm/public/gfssolomos/gsolomos8r.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/gfssolomos/GFSSolomos-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/gfssolomos/gsolomos8a.vf
%{_texmfdistdir}/tex/latex/gfssolomos/gfssolomos.sty
%{_texmfdistdir}/tex/latex/gfssolomos/lgrsolomos.fd

%files -n texlive-gfssolomos-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gfssolomos
%{_datadir}/fontconfig/conf.avail/58-texlive-gfssolomos.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gfssolomos.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gfssolomos.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfssolomos/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfssolomos/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gfssolomos/fonts.scale
%{_datadir}/fonts/texlive-gfssolomos/GFSSolomos.otf
%{_datadir}/fonts/texlive-gfssolomos/GFSSolomos-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gfssolomos-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn18651-%{release}-zypper
%endif

%package -n texlive-ghab
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn29803
Release:        0
Summary:        Typeset ghab boxes in LaTeX
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
Recommends:     texlive-ghab-doc >= %{texlive_version}
Provides:       tex(ghab.sty)
Requires:       tex(biditools.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source260:      ghab.tar.xz
Source261:      ghab.doc.tar.xz

%description -n texlive-ghab
The package defines a command \darghab that will typeset its
argument in a box with a decorated frame. The width of the box
may be set using an optional argument.

%package -n texlive-ghab-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn29803
Release:        0
Summary:        Documentation for texlive-ghab
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ghab-doc
This package includes the documentation for texlive-ghab

%post -n texlive-ghab
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ghab 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ghab
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ghab-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ghab/README
%{_texmfdistdir}/doc/latex/ghab/ghab-doc.pdf
%{_texmfdistdir}/doc/latex/ghab/ghab-doc.tex

%files -n texlive-ghab
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/ghab/ghab.mf
%{_texmfdistdir}/tex/latex/ghab/ghab.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ghab-%{texlive_version}.%{texlive_noarch}.0.0.5svn29803-%{release}-zypper
%endif

%package -n texlive-ghsystem
Version:        %{texlive_version}.%{texlive_noarch}.4.8csvn53822
Release:        0
Summary:        Globally harmonised system of chemical (etc) naming
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
Recommends:     texlive-ghsystem-doc >= %{texlive_version}
Provides:       tex(ghsystem.sty)
Provides:       tex(ghsystem_acid-8.tex)
Provides:       tex(ghsystem_acid.tex)
Provides:       tex(ghsystem_aqpol.tex)
Provides:       tex(ghsystem_bottle-2-black.tex)
Provides:       tex(ghsystem_bottle-2-white.tex)
Provides:       tex(ghsystem_bottle.tex)
Provides:       tex(ghsystem_english.def)
Provides:       tex(ghsystem_exclam.tex)
Provides:       tex(ghsystem_explos-1.tex)
Provides:       tex(ghsystem_explos-2.tex)
Provides:       tex(ghsystem_explos-3.tex)
Provides:       tex(ghsystem_explos-4.tex)
Provides:       tex(ghsystem_explos-5.tex)
Provides:       tex(ghsystem_explos-6.tex)
Provides:       tex(ghsystem_explos.tex)
Provides:       tex(ghsystem_flame-2-black.tex)
Provides:       tex(ghsystem_flame-2-white.tex)
Provides:       tex(ghsystem_flame-3-black.tex)
Provides:       tex(ghsystem_flame-3-white.tex)
Provides:       tex(ghsystem_flame-4-1.tex)
Provides:       tex(ghsystem_flame-4-2.tex)
Provides:       tex(ghsystem_flame-4-3-black.tex)
Provides:       tex(ghsystem_flame-4-3-white.tex)
Provides:       tex(ghsystem_flame-5-2-black.tex)
Provides:       tex(ghsystem_flame-5-2-white.tex)
Provides:       tex(ghsystem_flame-O-5-1.tex)
Provides:       tex(ghsystem_flame-O.tex)
Provides:       tex(ghsystem_flame.tex)
Provides:       tex(ghsystem_french.def)
Provides:       tex(ghsystem_german.def)
Provides:       tex(ghsystem_health.tex)
Provides:       tex(ghsystem_italian.def)
Provides:       tex(ghsystem_langtemplate.def)
Provides:       tex(ghsystem_skull-2.tex)
Provides:       tex(ghsystem_skull-6.tex)
Provides:       tex(ghsystem_skull.tex)
Provides:       tex(ghsystem_spanish.def)
Requires:       tex(chemmacros.sty)
Requires:       tex(expl3.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(longtable.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(translations.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source262:      ghsystem.tar.xz
Source263:      ghsystem.doc.tar.xz

%description -n texlive-ghsystem
The package provides the means to typeset all the hazard and
precautionary statements and pictograms in a straightforward
way. The statements are taken from EU regulation 1272/2008.

%package -n texlive-ghsystem-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.8csvn53822
Release:        0
Summary:        Documentation for texlive-ghsystem
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ghsystem-doc
This package includes the documentation for texlive-ghsystem

%post -n texlive-ghsystem
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ghsystem 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ghsystem
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ghsystem-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ghsystem/README
%{_texmfdistdir}/doc/latex/ghsystem/ghsystem-manual.cls
%{_texmfdistdir}/doc/latex/ghsystem/ghsystem-manual.pdf
%{_texmfdistdir}/doc/latex/ghsystem/ghsystem-manual.tex

%files -n texlive-ghsystem
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ghsystem/ghsystem.sty
%{_texmfdistdir}/tex/latex/ghsystem/language/ghsystem_english.def
%{_texmfdistdir}/tex/latex/ghsystem/language/ghsystem_french.def
%{_texmfdistdir}/tex/latex/ghsystem/language/ghsystem_german.def
%{_texmfdistdir}/tex/latex/ghsystem/language/ghsystem_italian.def
%{_texmfdistdir}/tex/latex/ghsystem/language/ghsystem_langtemplate.def
%{_texmfdistdir}/tex/latex/ghsystem/language/ghsystem_spanish.def
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid-8.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid-8.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid-8.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid-8.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid-8.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_acid.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_aqpol.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_aqpol.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_aqpol.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_aqpol.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_aqpol.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-black.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-black.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-black.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-black.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-black.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-white.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-white.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-white.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-white.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle-2-white.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_bottle.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_exclam.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_exclam.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_exclam.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_exclam.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_exclam.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-1.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-1.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-1.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-1.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-1.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-2.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-2.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-2.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-2.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-2.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-3.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-3.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-3.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-3.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-3.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-4.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-4.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-4.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-4.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-4.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-5.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-5.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-5.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-5.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-5.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-6.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-6.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-6.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-6.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos-6.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_explos.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-black.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-black.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-black.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-black.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-black.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-white.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-white.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-white.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-white.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-2-white.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-black.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-black.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-black.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-black.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-black.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-white.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-white.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-white.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-white.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-3-white.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-1.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-1.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-1.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-1.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-1.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-2.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-2.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-2.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-2.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-2.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-black.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-black.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-black.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-black.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-black.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-white.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-white.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-white.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-white.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-4-3-white.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-black.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-black.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-black.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-black.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-black.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-white.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-white.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-white.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-white.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-5-2-white.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O-5-1.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O-5-1.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O-5-1.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O-5-1.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O-5-1.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame-O.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_flame.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_health.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_health.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_health.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_health.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_health.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-2.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-2.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-2.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-2.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-2.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-6.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-6.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-6.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-6.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull-6.tex
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull.eps
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull.jpg
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull.pdf
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull.png
%{_texmfdistdir}/tex/latex/ghsystem/pictures/ghsystem_skull.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ghsystem-%{texlive_version}.%{texlive_noarch}.4.8csvn53822-%{release}-zypper
%endif

%package -n texlive-gillcm
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn19878
Release:        0
Summary:        Alternative unslanted italic Computer Modern fonts
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
Recommends:     texlive-gillcm-doc >= %{texlive_version}
Provides:       tex(cmg.map)
Provides:       tex(cmgb8r.tfm)
Provides:       tex(cmgbi7t.tfm)
Provides:       tex(cmgbi7t.vf)
Provides:       tex(cmgbi8c.tfm)
Provides:       tex(cmgbi8c.vf)
Provides:       tex(cmgbi8r.tfm)
Provides:       tex(cmgbi8t.tfm)
Provides:       tex(cmgbi8t.vf)
Provides:       tex(cmgbiu7t.tfm)
Provides:       tex(cmgbiu7t.vf)
Provides:       tex(cmgbiu8c.tfm)
Provides:       tex(cmgbiu8c.vf)
Provides:       tex(cmgbiu8r.tfm)
Provides:       tex(cmgbiu8t.tfm)
Provides:       tex(cmgbiu8t.vf)
Provides:       tex(cmgm8r.tfm)
Provides:       tex(cmgmi7t.tfm)
Provides:       tex(cmgmi7t.vf)
Provides:       tex(cmgmi8c.tfm)
Provides:       tex(cmgmi8c.vf)
Provides:       tex(cmgmi8r.tfm)
Provides:       tex(cmgmi8t.tfm)
Provides:       tex(cmgmi8t.vf)
Provides:       tex(cmgmiu7t.tfm)
Provides:       tex(cmgmiu7t.vf)
Provides:       tex(cmgmiu8c.tfm)
Provides:       tex(cmgmiu8c.vf)
Provides:       tex(cmgmiu8r.tfm)
Provides:       tex(cmgmiu8t.tfm)
Provides:       tex(cmgmiu8t.vf)
Provides:       tex(gillcm.sty)
Provides:       tex(ot1cmg.fd)
Provides:       tex(t1cmg.fd)
Provides:       tex(ts1cmg.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source264:      gillcm.tar.xz
Source265:      gillcm.doc.tar.xz

%description -n texlive-gillcm
This is a demonstration of the use of virtual fonts for unusual
effects: the package implements an old idea of Eric Gill. The
package was written for the author's talk at TUG 2010.

%package -n texlive-gillcm-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn19878
Release:        0
Summary:        Documentation for texlive-gillcm
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gillcm-doc
This package includes the documentation for texlive-gillcm

%post -n texlive-gillcm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gillcm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gillcm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gillcm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gillcm/README
%{_texmfdistdir}/doc/latex/gillcm/gillcm.bib
%{_texmfdistdir}/doc/latex/gillcm/gillcm.dtx
%{_texmfdistdir}/doc/latex/gillcm/gillcm.ins
%{_texmfdistdir}/doc/latex/gillcm/gillcm.pdf
%{_texmfdistdir}/doc/latex/gillcm/sample.pdf
%{_texmfdistdir}/doc/latex/gillcm/sample.tex

%files -n texlive-gillcm
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/gillcm/cmg.map
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgbiu8t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgm8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu7t.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu8c.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu8r.tfm
%{_texmfdistdir}/fonts/tfm/public/gillcm/cmgmiu8t.tfm
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbi7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbi8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbi8t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbiu7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbiu8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgbiu8t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmi7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmi8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmi8t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmiu7t.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmiu8c.vf
%{_texmfdistdir}/fonts/vf/public/gillcm/cmgmiu8t.vf
%{_texmfdistdir}/tex/latex/gillcm/gillcm.sty
%{_texmfdistdir}/tex/latex/gillcm/ot1cmg.fd
%{_texmfdistdir}/tex/latex/gillcm/t1cmg.fd
%{_texmfdistdir}/tex/latex/gillcm/ts1cmg.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gillcm-%{texlive_version}.%{texlive_noarch}.1.1svn19878-%{release}-zypper
%endif

%package -n texlive-gillius
Version:        %{texlive_version}.%{texlive_noarch}.svn32068
Release:        0
Summary:        Gillius fonts with LaTeX support
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
Requires:       texlive-gillius-fonts >= %{texlive_version}
Recommends:     texlive-gillius-doc >= %{texlive_version}
Provides:       tex(GilliusADF-Bold-lf-ly1--base.tfm)
Provides:       tex(GilliusADF-Bold-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADF-Bold-lf-ly1.tfm)
Provides:       tex(GilliusADF-Bold-lf-ly1.vf)
Provides:       tex(GilliusADF-Bold-lf-ot1--base.tfm)
Provides:       tex(GilliusADF-Bold-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADF-Bold-lf-ot1.tfm)
Provides:       tex(GilliusADF-Bold-lf-ot1.vf)
Provides:       tex(GilliusADF-Bold-lf-t1--base.tfm)
Provides:       tex(GilliusADF-Bold-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADF-Bold-lf-t1.tfm)
Provides:       tex(GilliusADF-Bold-lf-t1.vf)
Provides:       tex(GilliusADF-Bold-lf-ts1--base.tfm)
Provides:       tex(GilliusADF-Bold-lf-ts1.tfm)
Provides:       tex(GilliusADF-Bold-lf-ts1.vf)
Provides:       tex(GilliusADF-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ly1.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ly1.vf)
Provides:       tex(GilliusADF-BoldItalic-lf-ot1--base.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ot1.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ot1.vf)
Provides:       tex(GilliusADF-BoldItalic-lf-t1--base.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-t1.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-t1.vf)
Provides:       tex(GilliusADF-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ts1.tfm)
Provides:       tex(GilliusADF-BoldItalic-lf-ts1.vf)
Provides:       tex(GilliusADF-Italic-lf-ly1--base.tfm)
Provides:       tex(GilliusADF-Italic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADF-Italic-lf-ly1.tfm)
Provides:       tex(GilliusADF-Italic-lf-ly1.vf)
Provides:       tex(GilliusADF-Italic-lf-ot1--base.tfm)
Provides:       tex(GilliusADF-Italic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADF-Italic-lf-ot1.tfm)
Provides:       tex(GilliusADF-Italic-lf-ot1.vf)
Provides:       tex(GilliusADF-Italic-lf-t1--base.tfm)
Provides:       tex(GilliusADF-Italic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADF-Italic-lf-t1.tfm)
Provides:       tex(GilliusADF-Italic-lf-t1.vf)
Provides:       tex(GilliusADF-Italic-lf-ts1--base.tfm)
Provides:       tex(GilliusADF-Italic-lf-ts1.tfm)
Provides:       tex(GilliusADF-Italic-lf-ts1.vf)
Provides:       tex(GilliusADF-Regular-lf-ly1--base.tfm)
Provides:       tex(GilliusADF-Regular-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADF-Regular-lf-ly1.tfm)
Provides:       tex(GilliusADF-Regular-lf-ly1.vf)
Provides:       tex(GilliusADF-Regular-lf-ot1--base.tfm)
Provides:       tex(GilliusADF-Regular-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADF-Regular-lf-ot1.tfm)
Provides:       tex(GilliusADF-Regular-lf-ot1.vf)
Provides:       tex(GilliusADF-Regular-lf-t1--base.tfm)
Provides:       tex(GilliusADF-Regular-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADF-Regular-lf-t1.tfm)
Provides:       tex(GilliusADF-Regular-lf-t1.vf)
Provides:       tex(GilliusADF-Regular-lf-ts1--base.tfm)
Provides:       tex(GilliusADF-Regular-lf-ts1.tfm)
Provides:       tex(GilliusADF-Regular-lf-ts1.vf)
Provides:       tex(GilliusADFCond-Bold-lf-ly1--base.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ly1.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ly1.vf)
Provides:       tex(GilliusADFCond-Bold-lf-ot1--base.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ot1.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ot1.vf)
Provides:       tex(GilliusADFCond-Bold-lf-t1--base.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-t1.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-t1.vf)
Provides:       tex(GilliusADFCond-Bold-lf-ts1--base.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ts1.tfm)
Provides:       tex(GilliusADFCond-Bold-lf-ts1.vf)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1.vf)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1--base.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1.vf)
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1--base.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1.vf)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ts1.tfm)
Provides:       tex(GilliusADFCond-BoldItalic-lf-ts1.vf)
Provides:       tex(GilliusADFCond-Italic-lf-ly1--base.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ly1.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ly1.vf)
Provides:       tex(GilliusADFCond-Italic-lf-ot1--base.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ot1.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ot1.vf)
Provides:       tex(GilliusADFCond-Italic-lf-t1--base.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-t1.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-t1.vf)
Provides:       tex(GilliusADFCond-Italic-lf-ts1--base.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ts1.tfm)
Provides:       tex(GilliusADFCond-Italic-lf-ts1.vf)
Provides:       tex(GilliusADFCond-Regular-lf-ly1--base.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ly1.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ly1.vf)
Provides:       tex(GilliusADFCond-Regular-lf-ot1--base.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ot1.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ot1.vf)
Provides:       tex(GilliusADFCond-Regular-lf-t1--base.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-t1.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-t1.vf)
Provides:       tex(GilliusADFCond-Regular-lf-ts1--base.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ts1.tfm)
Provides:       tex(GilliusADFCond-Regular-lf-ts1.vf)
Provides:       tex(GilliusADFNo2-Bold-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ly1.vf)
Provides:       tex(GilliusADFNo2-Bold-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ot1.vf)
Provides:       tex(GilliusADFNo2-Bold-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-t1.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-t1.vf)
Provides:       tex(GilliusADFNo2-Bold-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2-Bold-lf-ts1.vf)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1.vf)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1.vf)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1.vf)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ts1.vf)
Provides:       tex(GilliusADFNo2-Italic-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ly1.vf)
Provides:       tex(GilliusADFNo2-Italic-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ot1.vf)
Provides:       tex(GilliusADFNo2-Italic-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-t1.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-t1.vf)
Provides:       tex(GilliusADFNo2-Italic-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2-Italic-lf-ts1.vf)
Provides:       tex(GilliusADFNo2-Regular-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ly1.vf)
Provides:       tex(GilliusADFNo2-Regular-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ot1.vf)
Provides:       tex(GilliusADFNo2-Regular-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-t1.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-t1.vf)
Provides:       tex(GilliusADFNo2-Regular-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2-Regular-lf-ts1.vf)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1.vf)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1.vf)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1.vf)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ts1.vf)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1.vf)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1.vf)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1.vf)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ts1.vf)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1.vf)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1.vf)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1.vf)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ts1.vf)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1.vf)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1.vf)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1--lcdfj.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1.vf)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ts1--base.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ts1.tfm)
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ts1.vf)
Provides:       tex(LY1GilliusADF-LF.fd)
Provides:       tex(LY1GilliusADFCond-LF.fd)
Provides:       tex(LY1GilliusADFNoTwo-LF.fd)
Provides:       tex(LY1GilliusADFNoTwoCond-LF.fd)
Provides:       tex(OT1GilliusADF-LF.fd)
Provides:       tex(OT1GilliusADFCond-LF.fd)
Provides:       tex(OT1GilliusADFNoTwo-LF.fd)
Provides:       tex(OT1GilliusADFNoTwoCond-LF.fd)
Provides:       tex(T1GilliusADF-LF.fd)
Provides:       tex(T1GilliusADFCond-LF.fd)
Provides:       tex(T1GilliusADFNoTwo-LF.fd)
Provides:       tex(T1GilliusADFNoTwoCond-LF.fd)
Provides:       tex(TS1GilliusADF-LF.fd)
Provides:       tex(TS1GilliusADFCond-LF.fd)
Provides:       tex(TS1GilliusADFNoTwo-LF.fd)
Provides:       tex(TS1GilliusADFNoTwoCond-LF.fd)
Provides:       tex(gillius.map)
Provides:       tex(gillius.sty)
Provides:       tex(gillius2.sty)
Provides:       tex(gls_4bsedw.enc)
Provides:       tex(gls_a6mi7n.enc)
Provides:       tex(gls_az7pev.enc)
Provides:       tex(gls_bg5e7z.enc)
Provides:       tex(gls_efuo7w.enc)
Provides:       tex(gls_lf6eoq.enc)
Provides:       tex(gls_pqq4vh.enc)
Provides:       tex(gls_shb4ap.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source266:      gillius.tar.xz
Source267:      gillius.doc.tar.xz

%description -n texlive-gillius
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Gillius and Gillius No. 2 families of sans
serif fonts and condensed versions of them, designed by Hirwen
Harendal. According to the designer, the fonts were inspired by
Gill Sans.

%package -n texlive-gillius-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn32068
Release:        0
Summary:        Documentation for texlive-gillius
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gillius-doc
This package includes the documentation for texlive-gillius


%package -n texlive-gillius-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn32068
Release:        0
Summary:        Severed fonts for texlive-gillius
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gillius-fonts
The  separated fonts package for texlive-gillius
%post -n texlive-gillius
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap gillius.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gillius 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap gillius.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gillius
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gillius-fonts
%files -n texlive-gillius-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gillius/COPYING
%{_texmfdistdir}/doc/fonts/gillius/Gillius-cat.pdf
%{_texmfdistdir}/doc/fonts/gillius/README
%{_texmfdistdir}/doc/fonts/gillius/gillius-samples.pdf
%{_texmfdistdir}/doc/fonts/gillius/gillius-samples.tex
%{_texmfdistdir}/doc/fonts/gillius/gillius2-samples.pdf
%{_texmfdistdir}/doc/fonts/gillius/gillius2-samples.tex

%files -n texlive-gillius
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_4bsedw.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_a6mi7n.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_az7pev.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_bg5e7z.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_efuo7w.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_lf6eoq.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_pqq4vh.enc
%{_texmfdistdir}/fonts/enc/dvips/gillius/gls_shb4ap.enc
%{_texmfdistdir}/fonts/map/dvips/gillius/gillius.map
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADF-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFCond-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/arkandis/gillius/GilliusADFNo2Cond-Regular.otf
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADF-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFCond-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADF-RegularLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFCond-RegularLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2-RegularLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/gillius/GilliusADFNo2Cond-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADF-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFCond-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/arkandis/gillius/GilliusADFNo2Cond-Regular-lf-ts1.vf
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/LY1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/OT1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/T1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADF-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADFCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADFNoTwo-LF.fd
%{_texmfdistdir}/tex/latex/gillius/TS1GilliusADFNoTwoCond-LF.fd
%{_texmfdistdir}/tex/latex/gillius/gillius.sty
%{_texmfdistdir}/tex/latex/gillius/gillius2.sty

%files -n texlive-gillius-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gillius
%{_datadir}/fontconfig/conf.avail/58-texlive-gillius.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gillius.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gillius.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gillius/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gillius/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gillius/fonts.scale
%{_datadir}/fonts/texlive-gillius/GilliusADF-Bold.otf
%{_datadir}/fonts/texlive-gillius/GilliusADF-BoldItalic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADF-Italic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADF-Regular.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-Bold.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-BoldItalic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-Italic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-Regular.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-Bold.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-BoldItalic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-Italic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-Regular.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-Bold.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-BoldItalic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-Italic.otf
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-Regular.otf
%{_datadir}/fonts/texlive-gillius/GilliusADF-Bold.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADF-BoldItalic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADF-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADF-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADF-Italic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADF-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADF-Regular.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADF-RegularLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-Bold.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-BoldItalic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-Italic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-Regular.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFCond-RegularLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-Bold.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-BoldItalic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-Italic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-Regular.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2-RegularLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-Bold.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-BoldItalic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-Italic.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-Regular.pfb
%{_datadir}/fonts/texlive-gillius/GilliusADFNo2Cond-RegularLCDFJ.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gillius-fonts-%{texlive_version}.%{texlive_noarch}.svn32068-%{release}-zypper
%endif

%package -n texlive-gincltex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn23835
Release:        0
Summary:        Include TeX files as graphics (.tex support for \includegraphics)
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
Recommends:     texlive-gincltex-doc >= %{texlive_version}
Provides:       tex(gincltex.sty)
Requires:       tex(adjustbox.sty)
Requires:       tex(svn-prov.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source268:      gincltex.tar.xz
Source269:      gincltex.doc.tar.xz

%description -n texlive-gincltex
The package builds on the standard LaTeX packages graphics
and/or graphicx and allows external LaTeX source files to be
included, in the same way as graphic files, by
\includegraphics. In effect, then package adds support for the
.tex extension. Some of the lower level operations like
clipping and trimming are implemented using the adjustbox
package which includes native pdfLaTeX support and uses the pgf
package for other output formats.

%package -n texlive-gincltex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn23835
Release:        0
Summary:        Documentation for texlive-gincltex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gincltex-doc
This package includes the documentation for texlive-gincltex

%post -n texlive-gincltex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gincltex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gincltex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gincltex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gincltex/README
%{_texmfdistdir}/doc/latex/gincltex/gincltex.pdf

%files -n texlive-gincltex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gincltex/gincltex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gincltex-%{texlive_version}.%{texlive_noarch}.0.0.3svn23835-%{release}-zypper
%endif

%package -n texlive-gindex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn52311
Release:        0
Summary:        Formatting indexes
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
Recommends:     texlive-gindex-doc >= %{texlive_version}
Provides:       tex(gindex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source270:      gindex.tar.xz
Source271:      gindex.doc.tar.xz

%description -n texlive-gindex
This package provides a way to generate the format of index
entries from within LaTeX.

%package -n texlive-gindex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn52311
Release:        0
Summary:        Documentation for texlive-gindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gindex-doc
This package includes the documentation for texlive-gindex

%post -n texlive-gindex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gindex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gindex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gindex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gindex/README.md
%{_texmfdistdir}/doc/latex/gindex/gindex.pdf
%{_texmfdistdir}/doc/latex/gindex/gindex.tex

%files -n texlive-gindex
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/gindex/gindex.ist
%{_texmfdistdir}/makeindex/gindex/gindexh.ist
%{_texmfdistdir}/tex/latex/gindex/gindex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gindex-%{texlive_version}.%{texlive_noarch}.0.0.2svn52311-%{release}-zypper
%endif

%package -n texlive-ginpenc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn24980
Release:        0
Summary:        Modification of inputenc for German
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
Recommends:     texlive-ginpenc-doc >= %{texlive_version}
Provides:       tex(ginpenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source272:      ginpenc.tar.xz
Source273:      ginpenc.doc.tar.xz

%description -n texlive-ginpenc
If the inputenc is used and German umlauts are input directly,
they are converted to the LICR representation \"a (etc.). This
breaks the sort algorithm of makeindex, for instance. Ginpenc
converts umlauts and the sharp-s to the short forms defined by
babel, e.g., "a instead, if the text is typeset in German.

%package -n texlive-ginpenc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn24980
Release:        0
Summary:        Documentation for texlive-ginpenc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ginpenc-doc
This package includes the documentation for texlive-ginpenc

%post -n texlive-ginpenc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ginpenc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ginpenc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ginpenc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ginpenc/ChangeLog
%{_texmfdistdir}/doc/latex/ginpenc/Makefile
%{_texmfdistdir}/doc/latex/ginpenc/README
%{_texmfdistdir}/doc/latex/ginpenc/ginpenc.pdf
%{_texmfdistdir}/doc/latex/ginpenc/news-message.txt
%{_texmfdistdir}/doc/latex/ginpenc/testginpenc.tex

%files -n texlive-ginpenc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ginpenc/ansinew.gie
%{_texmfdistdir}/tex/latex/ginpenc/applemac.gie
%{_texmfdistdir}/tex/latex/ginpenc/ascii.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp1250.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp1252.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp437.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp437de.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp850.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp852.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp865.gie
%{_texmfdistdir}/tex/latex/ginpenc/decmulti.gie
%{_texmfdistdir}/tex/latex/ginpenc/ginpenc.sty
%{_texmfdistdir}/tex/latex/ginpenc/latin1.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin2.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin3.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin5.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin9.gie
%{_texmfdistdir}/tex/latex/ginpenc/next.gie
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ginpenc-%{texlive_version}.%{texlive_noarch}.1.0svn24980-%{release}-zypper
%endif

%package -n texlive-git-latexdiff
Version:        %{texlive_version}.%{texlive_noarch}.1.6.0svn54732
Release:        0
Summary:        Call latexdiff on two Git revisions of a file
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-git-latexdiff-bin >= %{texlive_version}
#!BuildIgnore: texlive-git-latexdiff-bin
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
Recommends:     texlive-git-latexdiff-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source274:      git-latexdiff.tar.xz
Source275:      git-latexdiff.doc.tar.xz

%description -n texlive-git-latexdiff
git-latexdiff is a tool to graphically visualize differences
between different versions of a LaTeX file. Technically, it is
a wrapper around git and latexdiff.

%package -n texlive-git-latexdiff-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6.0svn54732
Release:        0
Summary:        Documentation for texlive-git-latexdiff
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(git-latexdiff.1)

%description -n texlive-git-latexdiff-doc
This package includes the documentation for texlive-git-latexdiff

%post -n texlive-git-latexdiff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-git-latexdiff 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-git-latexdiff
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-git-latexdiff-doc
%defattr(-,root,root,755)
%{_mandir}/man1/git-latexdiff.1*
%{_texmfdistdir}/doc/support/git-latexdiff/README.md

%files -n texlive-git-latexdiff
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/git-latexdiff/git-latexdiff
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-git-latexdiff-%{texlive_version}.%{texlive_noarch}.1.6.0svn54732-%{release}-zypper
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
       %{buildroot}/var/adm/update-scripts/texlive-float-%{texlive_version}.%{texlive_noarch}.1.3dsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-floatrow-%{texlive_version}.%{texlive_noarch}.0.0.3bsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-flowchart-%{texlive_version}.%{texlive_noarch}.3.3svn36572-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-flowfram-%{texlive_version}.%{texlive_noarch}.1.17svn35291-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/scripts/flowfram/flowfram.perl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/flowfram/flowfram.perl
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
       %{buildroot}/var/adm/update-scripts/texlive-fltpoint-%{texlive_version}.%{texlive_noarch}.1.1bsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fmp-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fmtcount-%{texlive_version}.%{texlive_noarch}.3.07svn53912-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fn2end-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fnbreak-%{texlive_version}.%{texlive_noarch}.1.30svn25003-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fncychap-%{texlive_version}.%{texlive_noarch}.1.34svn20710-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fncylab-%{texlive_version}.%{texlive_noarch}.1.1svn52090-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fnpara-%{texlive_version}.%{texlive_noarch}.svn25607-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fnpct-%{texlive_version}.%{texlive_noarch}.0.0.5svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fnspe-%{texlive_version}.%{texlive_noarch}.1.2asvn45360-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fntproof-%{texlive_version}.%{texlive_noarch}.svn20638-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fnumprint-%{texlive_version}.%{texlive_noarch}.1.1asvn29173-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-foekfont-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-foekfont
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/foekfont/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-foekfont
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-foekfont/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-foekfont/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-foekfont/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-foekfont/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-foekfont.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-foekfont    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-foekfont/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-foilhtml-%{texlive_version}.%{texlive_noarch}.1.2svn21855-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fonetika-fonts-%{texlive_version}.%{texlive_noarch}.svn21326-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fonetika
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/fonetika/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/fonetika/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fonetika
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fonetika/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fonetika/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fonetika/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fonetika/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fonetika.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fonetika    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fonetika/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-fonetika.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-fonetika/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-fonetika.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-fonetika.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-font-change-%{texlive_version}.%{texlive_noarch}.2015.2svn40403-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-font-change-xetex-%{texlive_version}.%{texlive_noarch}.2016.1svn40404-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontawesome-fonts-%{texlive_version}.%{texlive_noarch}.4.6.3.2svn48145-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fontawesome
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/fontawesome/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/fontawesome/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fontawesome
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fontawesome/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fontawesome/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fontawesome/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fontawesome/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fontawesome.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fontawesome    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fontawesome/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-fontawesome.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-fontawesome/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-fontawesome.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-fontawesome.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontawesome5-fonts-%{texlive_version}.%{texlive_noarch}.5.13.0svn54517-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fontawesome5
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/fontawesome5/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/fontawesome5/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fontawesome5
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fontawesome5/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fontawesome5/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fontawesome5/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fontawesome5/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fontawesome5.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fontawesome5    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fontawesome5/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-fontawesome5.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-fontawesome5/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-fontawesome5.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-fontawesome5.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontaxes-%{texlive_version}.%{texlive_noarch}.1.0dsvn33276-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontbook-%{texlive_version}.%{texlive_noarch}.0.0.2svn23608-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontch-%{texlive_version}.%{texlive_noarch}.2.2svn17859-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontinst-%{texlive_version}.%{texlive_noarch}.1.933svn53562-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontmfizz-fonts-%{texlive_version}.%{texlive_noarch}.svn43546-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fontmfizz
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/fontmfizz/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fontmfizz
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fontmfizz/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fontmfizz/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fontmfizz/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fontmfizz/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fontmfizz.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fontmfizz    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fontmfizz/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontname-%{texlive_version}.%{texlive_noarch}.svn53228-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontools-%{texlive_version}.%{texlive_noarch}.svn53593-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/fontools/afm2afm \
	       %{_texmfdistdir}/scripts/fontools/autoinst \
	       %{_texmfdistdir}/scripts/fontools/ot2kpx \
	       %{_texmfdistdir}/doc/support/fontools/splitttc
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
       %{buildroot}/var/adm/update-scripts/texlive-fonts-churchslavonic-fonts-%{texlive_version}.%{texlive_noarch}.1.1svn43121-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fonts-churchslavonic
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/fonts-churchslavonic/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/truetype/public/fonts-churchslavonic/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fonts-churchslavonic
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fonts-churchslavonic/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fonts-churchslavonic/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fonts-churchslavonic/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fonts-churchslavonic/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fonts-churchslavonic.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fonts-churchslavonic    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fonts-churchslavonic/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fonts-tlwg-fonts-%{texlive_version}.%{texlive_noarch}.0.0.7.1svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fonts-tlwg
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/fonts-tlwg/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/fonts-tlwg/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fonts-tlwg
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fonts-tlwg/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fonts-tlwg/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fonts-tlwg/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fonts-tlwg/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fonts-tlwg.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fonts-tlwg    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fonts-tlwg/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-fonts-tlwg.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-fonts-tlwg/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-fonts-tlwg.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-fonts-tlwg.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontsetup-%{texlive_version}.%{texlive_noarch}.1.002svn53195-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontsize-%{texlive_version}.%{texlive_noarch}.0.0.1svn53874-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontspec-%{texlive_version}.%{texlive_noarch}.2.7isvn53860-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fonttable-%{texlive_version}.%{texlive_noarch}.1.6csvn44799-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontware-%{texlive_version}.%{texlive_noarch}.svn54070-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fontwrap-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-footbib-%{texlive_version}.%{texlive_noarch}.2.0.7svn17115-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-footmisc-%{texlive_version}.%{texlive_noarch}.5.5bsvn23330-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-footmisx-%{texlive_version}.%{texlive_noarch}.20161201svn42621-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-footnotebackref-%{texlive_version}.%{texlive_noarch}.1.0svn27034-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-footnotehyper-%{texlive_version}.%{texlive_noarch}.1.1asvn52676-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-footnoterange-%{texlive_version}.%{texlive_noarch}.1.0csvn52910-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-footnpag-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-forarray-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/forarray/forarray
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-foreign-%{texlive_version}.%{texlive_noarch}.2.7svn27819-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-forest-%{texlive_version}.%{texlive_noarch}.2.1.5svn44797-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-forest-quickstart-%{texlive_version}.%{texlive_noarch}.svn42503-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-forloop-%{texlive_version}.%{texlive_noarch}.3.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-formation-latex-ul-%{texlive_version}.%{texlive_noarch}.2019.03svn50205-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-formlett-%{texlive_version}.%{texlive_noarch}.2.3svn21480-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-forms16be-%{texlive_version}.%{texlive_noarch}.1.3svn51305-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-formular-%{texlive_version}.%{texlive_noarch}.1.0asvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-forum-fonts-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-forum
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/forum/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/forum/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-forum
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-forum/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-forum/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-forum/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-forum/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-forum.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-forum    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-forum/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-forum.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-forum/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-forum.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-forum.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fouridx-%{texlive_version}.%{texlive_noarch}.2.00svn32214-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fourier-fonts-%{texlive_version}.%{texlive_noarch}.2.2svn54090-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fourier
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/fourier/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/fourier/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fourier
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fourier/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fourier/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fourier/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fourier/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fourier.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fourier    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fourier/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-fourier.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-fourier/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-fourier.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-fourier.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fouriernc-%{texlive_version}.%{texlive_noarch}.svn29646-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fp-%{texlive_version}.%{texlive_noarch}.2.1dsvn49719-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fpl-fonts-%{texlive_version}.%{texlive_noarch}.1.003svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-fpl
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/fpl/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-fpl
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-fpl/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-fpl/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fpl/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-fpl/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-fpl.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-fpl    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-fpl/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fragmaster-%{texlive_version}.%{texlive_noarch}.1.6svn26313-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fragments-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frame-%{texlive_version}.%{texlive_noarch}.1.0svn18312-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-framed-%{texlive_version}.%{texlive_noarch}.0.0.96svn26789-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-francais-bst-%{texlive_version}.%{texlive_noarch}.1.1svn38922-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frankenstein-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frcursive-fonts-%{texlive_version}.%{texlive_noarch}.svn24559-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-frcursive
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/frcursive/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-frcursive
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-frcursive/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-frcursive/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-frcursive/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-frcursive/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-frcursive.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-frcursive    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-frcursive/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frederika2016-fonts-%{texlive_version}.%{texlive_noarch}.1.000_2016_initial_releasesvn42157-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-frederika2016
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/frederika2016/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-frederika2016
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-frederika2016/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-frederika2016/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-frederika2016/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-frederika2016/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-frederika2016.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-frederika2016    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-frederika2016/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frege-%{texlive_version}.%{texlive_noarch}.1.3svn27417-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frenchmath-%{texlive_version}.%{texlive_noarch}.1.4svn51192-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frletter-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-frontespizio-%{texlive_version}.%{texlive_noarch}.1.4asvn24054-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ftc-notebook-%{texlive_version}.%{texlive_noarch}.1.1svn50043-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ftcap-%{texlive_version}.%{texlive_noarch}.1.4svn17275-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ftnxtra-%{texlive_version}.%{texlive_noarch}.0.0.1svn29652-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fullblck-%{texlive_version}.%{texlive_noarch}.1.03svn25434-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fullminipage-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn34545-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fullwidth-%{texlive_version}.%{texlive_noarch}.0.0.1svn24684-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-functan-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fundus-calligra-%{texlive_version}.%{texlive_noarch}.1.2svn26018-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fundus-cyr-%{texlive_version}.%{texlive_noarch}.svn26019-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fundus-sueterlin-%{texlive_version}.%{texlive_noarch}.1.2svn26030-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fvextra-%{texlive_version}.%{texlive_noarch}.1.4svn49947-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-fwlw-%{texlive_version}.%{texlive_noarch}.svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-g-brief-%{texlive_version}.%{texlive_noarch}.4.0.3svn50415-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gaceta-%{texlive_version}.%{texlive_noarch}.1.06svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-galois-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gamebook-%{texlive_version}.%{texlive_noarch}.1.0svn24714-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gammas-%{texlive_version}.%{texlive_noarch}.1.0svn50012-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-garamond-libre-fonts-%{texlive_version}.%{texlive_noarch}.1.1svn51703-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-garamond-libre
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/garamond-libre/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-garamond-libre
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-garamond-libre/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-garamond-libre/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-garamond-libre/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-garamond-libre/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-garamond-libre.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-garamond-libre    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-garamond-libre/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-garamond-math-fonts-%{texlive_version}.%{texlive_noarch}.svn52820-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-garamond-math
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/garamond-math/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-garamond-math
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-garamond-math/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-garamond-math/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-garamond-math/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-garamond-math/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-garamond-math.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-garamond-math    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-garamond-math/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-garrigues-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-garuda-c90-%{texlive_version}.%{texlive_noarch}.svn37677-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gastex-%{texlive_version}.%{texlive_noarch}.2.8svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gatech-thesis-%{texlive_version}.%{texlive_noarch}.1.8svn19886-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gates-%{texlive_version}.%{texlive_noarch}.0.0.2svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gatherenum-%{texlive_version}.%{texlive_noarch}.1.8svn52209-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gauss-%{texlive_version}.%{texlive_noarch}.svn32934-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gb4e-%{texlive_version}.%{texlive_noarch}.svn19216-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gbt7714-%{texlive_version}.%{texlive_noarch}.2.0.1svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gcard-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gchords-%{texlive_version}.%{texlive_noarch}.1.20svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gcite-%{texlive_version}.%{texlive_noarch}.1.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gender-%{texlive_version}.%{texlive_noarch}.1.0svn36464-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gene-logic-%{texlive_version}.%{texlive_noarch}.1.4svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-genealogy-%{texlive_version}.%{texlive_noarch}.svn25112-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-genealogytree-%{texlive_version}.%{texlive_noarch}.1.32svn50872-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-genmpage-%{texlive_version}.%{texlive_noarch}.0.0.3.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gentium-tug-fonts-%{texlive_version}.%{texlive_noarch}.1.1.1svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gentium-tug
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/gentium-tug/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gentium-tug/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gentium-tug
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gentium-tug/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gentium-tug/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gentium-tug/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gentium-tug/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gentium-tug.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gentium-tug    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gentium-tug/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gentium-tug.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gentium-tug/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gentium-tug.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gentium-tug.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gentle-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gentombow-%{texlive_version}.%{texlive_noarch}.svn51697-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-geometry-%{texlive_version}.%{texlive_noarch}.5.9svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-german-%{texlive_version}.%{texlive_noarch}.2.5esvn42428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-germbib-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-germkorr-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-geschichtsfrkl-%{texlive_version}.%{texlive_noarch}.1.4svn42121-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-getfiledate-%{texlive_version}.%{texlive_noarch}.1.2svn16189-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-getitems-%{texlive_version}.%{texlive_noarch}.1.0svn39365-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-getmap-%{texlive_version}.%{texlive_noarch}.1.11svn50589-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/getmap/getmapdl.lua
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
       %{buildroot}/var/adm/update-scripts/texlive-getoptk-%{texlive_version}.%{texlive_noarch}.1.0svn23567-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gettitlestring-%{texlive_version}.%{texlive_noarch}.1.6svn53170-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfnotation-%{texlive_version}.%{texlive_noarch}.2.9svn37156-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsartemisia-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn19469-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsartemisia
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsartemisia/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfsartemisia/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsartemisia
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsartemisia/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsartemisia/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsartemisia/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsartemisia/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsartemisia.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsartemisia    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsartemisia/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfsartemisia.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfsartemisia/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfsartemisia.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfsartemisia.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsbaskerville-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn19440-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsbaskerville
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsbaskerville/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfsbaskerville/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsbaskerville
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsbaskerville/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsbaskerville/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsbaskerville/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsbaskerville/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsbaskerville.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsbaskerville    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsbaskerville/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfsbaskerville.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfsbaskerville/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfsbaskerville.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfsbaskerville.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsbodoni-fonts-%{texlive_version}.%{texlive_noarch}.1.01svn28484-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsbodoni
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsbodoni/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfsbodoni/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsbodoni
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsbodoni/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsbodoni/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsbodoni/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsbodoni/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsbodoni.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsbodoni    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsbodoni/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfsbodoni.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfsbodoni/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfsbodoni.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfsbodoni.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfscomplutum-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn19469-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfscomplutum
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfscomplutum/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfscomplutum/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfscomplutum
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfscomplutum/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfscomplutum/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfscomplutum/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfscomplutum/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfscomplutum.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfscomplutum    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfscomplutum/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfscomplutum.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfscomplutum/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfscomplutum.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfscomplutum.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsdidot-fonts-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/fonts/gfsdidot/installDidot.pl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsdidot
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsdidot/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfsdidot/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsdidot
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsdidot/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsdidot/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsdidot/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsdidot/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsdidot.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsdidot    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsdidot/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfsdidot.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfsdidot/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfsdidot.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfsdidot.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsdidotclassic-fonts-%{texlive_version}.%{texlive_noarch}.001.001svn52778-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsdidotclassic
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsdidotclassic/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsdidotclassic
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsdidotclassic/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsdidotclassic/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsdidotclassic/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsdidotclassic/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsdidotclassic.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsdidotclassic    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsdidotclassic/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsneohellenic-fonts-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenic
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsneohellenic/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfsneohellenic/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenic
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsneohellenic/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenic/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenic/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenic/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsneohellenic.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsneohellenic    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsneohellenic/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfsneohellenic.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfsneohellenic/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfsneohellenic.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfsneohellenic.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsneohellenicmath-fonts-%{texlive_version}.%{texlive_noarch}.1.0.1svn52570-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenicmath
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsneohellenicmath/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenicmath
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsneohellenicmath/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenicmath/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenicmath/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsneohellenicmath/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsneohellenicmath.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsneohellenicmath    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsneohellenicmath/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfsporson-fonts-%{texlive_version}.%{texlive_noarch}.1.01svn18651-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfsporson
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfsporson/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfsporson/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfsporson
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfsporson/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsporson/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsporson/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfsporson/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfsporson.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfsporson    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfsporson/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfsporson.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfsporson/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfsporson.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfsporson.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gfssolomos-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn18651-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gfssolomos
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gfssolomos/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/gfssolomos/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gfssolomos
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gfssolomos/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gfssolomos/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfssolomos/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gfssolomos/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gfssolomos.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gfssolomos    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gfssolomos/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gfssolomos.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gfssolomos/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gfssolomos.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gfssolomos.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ghab-%{texlive_version}.%{texlive_noarch}.0.0.5svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ghsystem-%{texlive_version}.%{texlive_noarch}.4.8csvn53822-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gillcm-%{texlive_version}.%{texlive_noarch}.1.1svn19878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gillius-fonts-%{texlive_version}.%{texlive_noarch}.svn32068-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gillius
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/arkandis/gillius/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/arkandis/gillius/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gillius
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gillius/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gillius/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gillius/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gillius/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gillius.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gillius    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gillius/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gillius.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gillius/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gillius.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gillius.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gincltex-%{texlive_version}.%{texlive_noarch}.0.0.3svn23835-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gindex-%{texlive_version}.%{texlive_noarch}.0.0.2svn52311-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ginpenc-%{texlive_version}.%{texlive_noarch}.1.0svn24980-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-git-latexdiff-%{texlive_version}.%{texlive_noarch}.1.6.0svn54732-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive
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
    # Handle info documents
    rm -vf  %{buildroot}%{_texmfmaindir}/doc/info/dir
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/info/dir
    mkdir -p %{buildroot}%{_infodir}
    for inf in %{buildroot}%{_texmfmaindir}/doc/info/*.info \
               %{buildroot}%{_texmfdistdir}/doc/info/*.info
    do
        test -e "$inf" || continue
        mv -f $inf %{buildroot}%{_infodir}/
    done
    rm -rf %{buildroot}%{_texmfmaindir}/doc/info
    rm -rf %{buildroot}%{_texmfdistdir}/doc/info
    find %{buildroot}%{_texmfmaindir}/ %{buildroot}%{_texmfdistdir}/ \
        -type f -a -perm /g+w,o+w | xargs --no-run-if-empty chmod g-w,o-w

%changelog
