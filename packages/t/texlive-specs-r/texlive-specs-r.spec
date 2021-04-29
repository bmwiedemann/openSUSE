#
# spec file for package texlive-specs-r
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


%bcond_with	zypper_posttrans

%define texlive_version  2021
%define texlive_previous 2020
%define texlive_release  20210325
%define texlive_noarch   185

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

Name:           texlive-specs-r
Version:        2021
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for r
License:        BSD-3-Clause and GPL-2.0-or-later and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain and SUSE-TeX
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Group:          Productivity/Publishing/TeX/Base
Source0:        texlive-specs-r-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-overlays
Version:        %{texlive_version}.%{texlive_noarch}.2.12svn57866
Release:        0
License:        LPPL-1.0
Summary:        Incremental slides
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-overlays-doc >= %{texlive_version}
Provides:       tex(overlays.sty)
Requires:       tex(environ.sty)
Requires:       tex(pgffor.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source1:        overlays.tar.xz
Source2:        overlays.doc.tar.xz

%description -n texlive-overlays
This package allows to write presentations with incremental
slides. It does not presuppose any specific document class.
Rather, it is a lightweight alternative to full-fledged
presentation classes like beamer. The package requires xcolor,
environ, and pgffor (from the pgf bundle).

%package -n texlive-overlays-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.12svn57866
Release:        0
Summary:        Documentation for texlive-overlays
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-overlays-doc
This package includes the documentation for texlive-overlays

%post -n texlive-overlays
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-overlays
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-overlays
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-overlays-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/overlays/COPYING
%{_texmfdistdir}/doc/latex/overlays/ChangeLog
%{_texmfdistdir}/doc/latex/overlays/README
%{_texmfdistdir}/doc/latex/overlays/overlays.pdf
%{_texmfdistdir}/doc/latex/overlays/overlays.tex
%{_texmfdistdir}/doc/latex/overlays/sample.pdf
%{_texmfdistdir}/doc/latex/overlays/sample.tex

%files -n texlive-overlays
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/overlays/overlays.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-overlays-%{texlive_version}.%{texlive_noarch}.2.12svn57866-%{release}-zypper
%endif

%package -n texlive-overlock
Version:        %{texlive_version}.%{texlive_noarch}.svn56079
Release:        0
License:        OFL-1.1
Summary:        Overlock sans fonts with LaTeX support
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-overlock-fonts >= %{texlive_version}
Recommends:     texlive-overlock-doc >= %{texlive_version}
Provides:       tex(LY1Ovrlck-LF.fd)
Provides:       tex(LY1Ovrlck-OsF.fd)
Provides:       tex(OT1Ovrlck-LF.fd)
Provides:       tex(OT1Ovrlck-OsF.fd)
Provides:       tex(Ovrlck-Black-lf-ly1--base.tfm)
Provides:       tex(Ovrlck-Black-lf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Black-lf-ly1.tfm)
Provides:       tex(Ovrlck-Black-lf-ly1.vf)
Provides:       tex(Ovrlck-Black-lf-ot1--base.tfm)
Provides:       tex(Ovrlck-Black-lf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Black-lf-ot1.tfm)
Provides:       tex(Ovrlck-Black-lf-ot1.vf)
Provides:       tex(Ovrlck-Black-lf-t1--base.tfm)
Provides:       tex(Ovrlck-Black-lf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Black-lf-t1.tfm)
Provides:       tex(Ovrlck-Black-lf-t1.vf)
Provides:       tex(Ovrlck-Black-lf-ts1--base.tfm)
Provides:       tex(Ovrlck-Black-lf-ts1.tfm)
Provides:       tex(Ovrlck-Black-lf-ts1.vf)
Provides:       tex(Ovrlck-Black-osf-ly1--base.tfm)
Provides:       tex(Ovrlck-Black-osf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Black-osf-ly1.tfm)
Provides:       tex(Ovrlck-Black-osf-ly1.vf)
Provides:       tex(Ovrlck-Black-osf-ot1--base.tfm)
Provides:       tex(Ovrlck-Black-osf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Black-osf-ot1.tfm)
Provides:       tex(Ovrlck-Black-osf-ot1.vf)
Provides:       tex(Ovrlck-Black-osf-t1--base.tfm)
Provides:       tex(Ovrlck-Black-osf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Black-osf-t1.tfm)
Provides:       tex(Ovrlck-Black-osf-t1.vf)
Provides:       tex(Ovrlck-Black-osf-ts1--base.tfm)
Provides:       tex(Ovrlck-Black-osf-ts1.tfm)
Provides:       tex(Ovrlck-Black-osf-ts1.vf)
Provides:       tex(Ovrlck-BlackItalic-lf-ly1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ly1.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ly1.vf)
Provides:       tex(Ovrlck-BlackItalic-lf-ot1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ot1.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ot1.vf)
Provides:       tex(Ovrlck-BlackItalic-lf-t1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-t1.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-t1.vf)
Provides:       tex(Ovrlck-BlackItalic-lf-ts1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ts1.tfm)
Provides:       tex(Ovrlck-BlackItalic-lf-ts1.vf)
Provides:       tex(Ovrlck-BlackItalic-osf-ly1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ly1.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ly1.vf)
Provides:       tex(Ovrlck-BlackItalic-osf-ot1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ot1.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ot1.vf)
Provides:       tex(Ovrlck-BlackItalic-osf-t1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-t1.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-t1.vf)
Provides:       tex(Ovrlck-BlackItalic-osf-ts1--base.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ts1.tfm)
Provides:       tex(Ovrlck-BlackItalic-osf-ts1.vf)
Provides:       tex(Ovrlck-Bold-lf-ly1--base.tfm)
Provides:       tex(Ovrlck-Bold-lf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Bold-lf-ly1.tfm)
Provides:       tex(Ovrlck-Bold-lf-ly1.vf)
Provides:       tex(Ovrlck-Bold-lf-ot1--base.tfm)
Provides:       tex(Ovrlck-Bold-lf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Bold-lf-ot1.tfm)
Provides:       tex(Ovrlck-Bold-lf-ot1.vf)
Provides:       tex(Ovrlck-Bold-lf-t1--base.tfm)
Provides:       tex(Ovrlck-Bold-lf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Bold-lf-t1.tfm)
Provides:       tex(Ovrlck-Bold-lf-t1.vf)
Provides:       tex(Ovrlck-Bold-lf-ts1--base.tfm)
Provides:       tex(Ovrlck-Bold-lf-ts1.tfm)
Provides:       tex(Ovrlck-Bold-lf-ts1.vf)
Provides:       tex(Ovrlck-Bold-osf-ly1--base.tfm)
Provides:       tex(Ovrlck-Bold-osf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Bold-osf-ly1.tfm)
Provides:       tex(Ovrlck-Bold-osf-ly1.vf)
Provides:       tex(Ovrlck-Bold-osf-ot1--base.tfm)
Provides:       tex(Ovrlck-Bold-osf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Bold-osf-ot1.tfm)
Provides:       tex(Ovrlck-Bold-osf-ot1.vf)
Provides:       tex(Ovrlck-Bold-osf-t1--base.tfm)
Provides:       tex(Ovrlck-Bold-osf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Bold-osf-t1.tfm)
Provides:       tex(Ovrlck-Bold-osf-t1.vf)
Provides:       tex(Ovrlck-Bold-osf-ts1--base.tfm)
Provides:       tex(Ovrlck-Bold-osf-ts1.tfm)
Provides:       tex(Ovrlck-Bold-osf-ts1.vf)
Provides:       tex(Ovrlck-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ly1.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ly1.vf)
Provides:       tex(Ovrlck-BoldItalic-lf-ot1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ot1.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ot1.vf)
Provides:       tex(Ovrlck-BoldItalic-lf-t1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-t1.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-t1.vf)
Provides:       tex(Ovrlck-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ts1.tfm)
Provides:       tex(Ovrlck-BoldItalic-lf-ts1.vf)
Provides:       tex(Ovrlck-BoldItalic-osf-ly1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ly1.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ly1.vf)
Provides:       tex(Ovrlck-BoldItalic-osf-ot1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ot1.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ot1.vf)
Provides:       tex(Ovrlck-BoldItalic-osf-t1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-t1.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-t1.vf)
Provides:       tex(Ovrlck-BoldItalic-osf-ts1--base.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ts1.tfm)
Provides:       tex(Ovrlck-BoldItalic-osf-ts1.vf)
Provides:       tex(Ovrlck-Italic-lf-ly1--base.tfm)
Provides:       tex(Ovrlck-Italic-lf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Italic-lf-ly1.tfm)
Provides:       tex(Ovrlck-Italic-lf-ly1.vf)
Provides:       tex(Ovrlck-Italic-lf-ot1--base.tfm)
Provides:       tex(Ovrlck-Italic-lf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Italic-lf-ot1.tfm)
Provides:       tex(Ovrlck-Italic-lf-ot1.vf)
Provides:       tex(Ovrlck-Italic-lf-t1--base.tfm)
Provides:       tex(Ovrlck-Italic-lf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Italic-lf-t1.tfm)
Provides:       tex(Ovrlck-Italic-lf-t1.vf)
Provides:       tex(Ovrlck-Italic-lf-ts1--base.tfm)
Provides:       tex(Ovrlck-Italic-lf-ts1.tfm)
Provides:       tex(Ovrlck-Italic-lf-ts1.vf)
Provides:       tex(Ovrlck-Italic-osf-ly1--base.tfm)
Provides:       tex(Ovrlck-Italic-osf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Italic-osf-ly1.tfm)
Provides:       tex(Ovrlck-Italic-osf-ly1.vf)
Provides:       tex(Ovrlck-Italic-osf-ot1--base.tfm)
Provides:       tex(Ovrlck-Italic-osf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Italic-osf-ot1.tfm)
Provides:       tex(Ovrlck-Italic-osf-ot1.vf)
Provides:       tex(Ovrlck-Italic-osf-t1--base.tfm)
Provides:       tex(Ovrlck-Italic-osf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Italic-osf-t1.tfm)
Provides:       tex(Ovrlck-Italic-osf-t1.vf)
Provides:       tex(Ovrlck-Italic-osf-ts1--base.tfm)
Provides:       tex(Ovrlck-Italic-osf-ts1.tfm)
Provides:       tex(Ovrlck-Italic-osf-ts1.vf)
Provides:       tex(Ovrlck-Regular-lf-ly1--base.tfm)
Provides:       tex(Ovrlck-Regular-lf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-lf-ly1.tfm)
Provides:       tex(Ovrlck-Regular-lf-ly1.vf)
Provides:       tex(Ovrlck-Regular-lf-ot1--base.tfm)
Provides:       tex(Ovrlck-Regular-lf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-lf-ot1.tfm)
Provides:       tex(Ovrlck-Regular-lf-ot1.vf)
Provides:       tex(Ovrlck-Regular-lf-sc-ly1--base.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-ly1.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-ly1.vf)
Provides:       tex(Ovrlck-Regular-lf-sc-ot1--base.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-ot1.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-ot1.vf)
Provides:       tex(Ovrlck-Regular-lf-sc-t1--base.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-t1.tfm)
Provides:       tex(Ovrlck-Regular-lf-sc-t1.vf)
Provides:       tex(Ovrlck-Regular-lf-t1--base.tfm)
Provides:       tex(Ovrlck-Regular-lf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-lf-t1.tfm)
Provides:       tex(Ovrlck-Regular-lf-t1.vf)
Provides:       tex(Ovrlck-Regular-lf-ts1--base.tfm)
Provides:       tex(Ovrlck-Regular-lf-ts1.tfm)
Provides:       tex(Ovrlck-Regular-lf-ts1.vf)
Provides:       tex(Ovrlck-Regular-osf-ly1--base.tfm)
Provides:       tex(Ovrlck-Regular-osf-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-osf-ly1.tfm)
Provides:       tex(Ovrlck-Regular-osf-ly1.vf)
Provides:       tex(Ovrlck-Regular-osf-ot1--base.tfm)
Provides:       tex(Ovrlck-Regular-osf-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-osf-ot1.tfm)
Provides:       tex(Ovrlck-Regular-osf-ot1.vf)
Provides:       tex(Ovrlck-Regular-osf-sc-ly1--base.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-ly1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-ly1.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-ly1.vf)
Provides:       tex(Ovrlck-Regular-osf-sc-ot1--base.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-ot1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-ot1.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-ot1.vf)
Provides:       tex(Ovrlck-Regular-osf-sc-t1--base.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-t1.tfm)
Provides:       tex(Ovrlck-Regular-osf-sc-t1.vf)
Provides:       tex(Ovrlck-Regular-osf-t1--base.tfm)
Provides:       tex(Ovrlck-Regular-osf-t1--lcdfj.tfm)
Provides:       tex(Ovrlck-Regular-osf-t1.tfm)
Provides:       tex(Ovrlck-Regular-osf-t1.vf)
Provides:       tex(Ovrlck-Regular-osf-ts1--base.tfm)
Provides:       tex(Ovrlck-Regular-osf-ts1.tfm)
Provides:       tex(Ovrlck-Regular-osf-ts1.vf)
Provides:       tex(T1Ovrlck-LF.fd)
Provides:       tex(T1Ovrlck-OsF.fd)
Provides:       tex(TS1Ovrlck-LF.fd)
Provides:       tex(TS1Ovrlck-OsF.fd)
Provides:       tex(overlock.map)
Provides:       tex(overlock.sty)
Provides:       tex(ovrlck_2sdgnb.enc)
Provides:       tex(ovrlck_325tkf.enc)
Provides:       tex(ovrlck_7l4e47.enc)
Provides:       tex(ovrlck_a4aghc.enc)
Provides:       tex(ovrlck_bhbhyo.enc)
Provides:       tex(ovrlck_cj365g.enc)
Provides:       tex(ovrlck_cr35rj.enc)
Provides:       tex(ovrlck_e3j4ia.enc)
Provides:       tex(ovrlck_fqfhhf.enc)
Provides:       tex(ovrlck_gmmlzo.enc)
Provides:       tex(ovrlck_irzqhk.enc)
Provides:       tex(ovrlck_j3mq5n.enc)
Provides:       tex(ovrlck_k2npiy.enc)
Provides:       tex(ovrlck_lhx5go.enc)
Provides:       tex(ovrlck_lqqrub.enc)
Provides:       tex(ovrlck_siy5zo.enc)
Provides:       tex(ovrlck_tmoia5.enc)
Provides:       tex(ovrlck_vvi6px.enc)
Provides:       tex(ovrlck_woxjio.enc)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source3:        overlock.tar.xz
Source4:        overlock.doc.tar.xz

%description -n texlive-overlock
The package provides the Overlock and OverlockSC families of
fonts, designed by Dario Manuel Muhafara of the TIPO foundry
(http://www.tipo.net.ar), "rounded" sans-serif fonts in three
weights (Regular, Bold, Black) with italic variants for each of
them. There are also small-caps and old-style figures in the
Regular weight.

%package -n texlive-overlock-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn56079
Release:        0
Summary:        Documentation for texlive-overlock
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-overlock-doc
This package includes the documentation for texlive-overlock

%package -n texlive-overlock-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn56079
Release:        0
Summary:        Severed fonts for texlive-overlock
License:        OFL-1.1
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-overlock-fonts
The  separated fonts package for texlive-overlock

%post -n texlive-overlock
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap overlock.map' >> /var/run/texlive/run-updmap

%postun -n texlive-overlock
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap overlock.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-overlock
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-overlock-fonts

%files -n texlive-overlock-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/overlock/OFL.txt
%{_texmfdistdir}/doc/fonts/overlock/README
%{_texmfdistdir}/doc/fonts/overlock/overlock-samples.pdf
%{_texmfdistdir}/doc/fonts/overlock/overlock-samples.tex

%files -n texlive-overlock
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_2sdgnb.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_325tkf.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_7l4e47.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_a4aghc.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_bhbhyo.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_cj365g.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_cr35rj.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_e3j4ia.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_fqfhhf.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_gmmlzo.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_irzqhk.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_j3mq5n.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_k2npiy.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_lhx5go.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_lqqrub.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_siy5zo.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_tmoia5.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_vvi6px.enc
%{_texmfdistdir}/fonts/enc/dvips/overlock/ovrlck_woxjio.enc
%{_texmfdistdir}/fonts/map/dvips/overlock/overlock.map
%verify(link) %{_texmfdistdir}/fonts/opentype/tipo/overlock/Overlock-Black-OTF.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/tipo/overlock/Overlock-BlackItalic-OTF.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/tipo/overlock/Overlock-Bold-OTF.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/tipo/overlock/Overlock-BoldItalic-OTF.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/tipo/overlock/Overlock-Italic-OTF.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/tipo/overlock/Overlock-Regular-OTF.otf
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Black-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BlackItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/tipo/overlock/Ovrlck-Regular-osf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-Black.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-BlackItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-BlackItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-BlackLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/tipo/overlock/Ovrlck-RegularLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-lf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-osf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-osf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Black-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-osf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BlackItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-osf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-osf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-osf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-lf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-osf-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/tipo/overlock/Ovrlck-Regular-osf-ts1.vf
%{_texmfdistdir}/tex/latex/overlock/LY1Ovrlck-LF.fd
%{_texmfdistdir}/tex/latex/overlock/LY1Ovrlck-OsF.fd
%{_texmfdistdir}/tex/latex/overlock/OT1Ovrlck-LF.fd
%{_texmfdistdir}/tex/latex/overlock/OT1Ovrlck-OsF.fd
%{_texmfdistdir}/tex/latex/overlock/T1Ovrlck-LF.fd
%{_texmfdistdir}/tex/latex/overlock/T1Ovrlck-OsF.fd
%{_texmfdistdir}/tex/latex/overlock/TS1Ovrlck-LF.fd
%{_texmfdistdir}/tex/latex/overlock/TS1Ovrlck-OsF.fd
%{_texmfdistdir}/tex/latex/overlock/overlock.sty

%files -n texlive-overlock-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-overlock
%{_datadir}/fontconfig/conf.avail/58-texlive-overlock.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-overlock.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-overlock.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-overlock/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-overlock/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-overlock/fonts.scale
%{_datadir}/fonts/texlive-overlock/Overlock-Black-OTF.otf
%{_datadir}/fonts/texlive-overlock/Overlock-BlackItalic-OTF.otf
%{_datadir}/fonts/texlive-overlock/Overlock-Bold-OTF.otf
%{_datadir}/fonts/texlive-overlock/Overlock-BoldItalic-OTF.otf
%{_datadir}/fonts/texlive-overlock/Overlock-Italic-OTF.otf
%{_datadir}/fonts/texlive-overlock/Overlock-Regular-OTF.otf
%{_datadir}/fonts/texlive-overlock/Ovrlck-Black.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-BlackItalic.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-BlackItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-BlackLCDFJ.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-Bold.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-BoldItalic.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-Italic.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-Regular.pfb
%{_datadir}/fonts/texlive-overlock/Ovrlck-RegularLCDFJ.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-overlock-fonts-%{texlive_version}.%{texlive_noarch}.svn56079-%{release}-zypper
%endif

%package -n texlive-overpic
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53889
Release:        0
License:        LPPL-1.0
Summary:        Combine LaTeX commands over included graphics
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-overpic-doc >= %{texlive_version}
Provides:       tex(overpic.sty)
Requires:       tex(epic.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source5:        overpic.tar.xz
Source6:        overpic.doc.tar.xz

%description -n texlive-overpic
The overpic environment is a cross between the LaTeX picture
environment and the \includegraphics command of graphicx. The
resulting picture environment has the same dimensions as the
included graphic. LaTeX commands can be placed on the graphic
at defined positions; a grid for orientation is available.

%package -n texlive-overpic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53889
Release:        0
Summary:        Documentation for texlive-overpic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-overpic-doc:de;en)

%description -n texlive-overpic-doc
This package includes the documentation for texlive-overpic

%post -n texlive-overpic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-overpic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-overpic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-overpic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/overpic/README.de.md
%{_texmfdistdir}/doc/latex/overpic/README.md
%{_texmfdistdir}/doc/latex/overpic/overpic.pdf

%files -n texlive-overpic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/overpic/overpic.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-overpic-%{texlive_version}.%{texlive_noarch}.1.3svn53889-%{release}-zypper
%endif

%package -n texlive-pacioli
Version:        %{texlive_version}.%{texlive_noarch}.svn24947
Release:        0
License:        LPPL-1.0
Summary:        Fonts designed by Fra Luca de Pacioli in 1497
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pacioli-doc >= %{texlive_version}
Provides:       tex(cpcr10.tfm)
Provides:       tex(cpcsl10.tfm)
Provides:       tex(ot1cpc.fd)
Provides:       tex(pacioli.sty)
Provides:       tex(t1cpc.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source7:        pacioli.tar.xz
Source8:        pacioli.doc.tar.xz

%description -n texlive-pacioli
Pacioli was a c.15 mathematician, and his font was designed
according to 'the divine proportion'. The font is uppercase
letters together with punctuation and some analphabetics; no
lowercase or digits. The Metafont source is distributed in a
.dtx file, together with LaTeX support.

%package -n texlive-pacioli-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn24947
Release:        0
Summary:        Documentation for texlive-pacioli
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pacioli-doc
This package includes the documentation for texlive-pacioli

%post -n texlive-pacioli
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pacioli
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pacioli
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pacioli-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/pacioli/README
%{_texmfdistdir}/doc/fonts/pacioli/tryfont.ps
%{_texmfdistdir}/doc/fonts/pacioli/tryfont.tex

%files -n texlive-pacioli
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/pacioli/cpclig.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcpunct.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcr10.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcromanp.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcromanu.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpcsl10.mf
%{_texmfdistdir}/fonts/source/public/pacioli/cpctitle.mf
%{_texmfdistdir}/fonts/tfm/public/pacioli/cpcr10.tfm
%{_texmfdistdir}/fonts/tfm/public/pacioli/cpcsl10.tfm
%{_texmfdistdir}/tex/latex/pacioli/ot1cpc.fd
%{_texmfdistdir}/tex/latex/pacioli/pacioli.sty
%{_texmfdistdir}/tex/latex/pacioli/t1cpc.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pacioli-%{texlive_version}.%{texlive_noarch}.svn24947-%{release}-zypper
%endif

%package -n texlive-padauk
Version:        %{texlive_version}.%{texlive_noarch}.3.002svn42617
Release:        0
License:        OFL-1.1
Summary:        A high-quality TrueType font that supports the many diverse languages that use the Myanmar script
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-padauk-fonts >= %{texlive_version}
Recommends:     texlive-padauk-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source9:        padauk.tar.xz
Source10:       padauk.doc.tar.xz

%description -n texlive-padauk
Padauk is a Unicode-based font family with broad support for
writing systems that use the Myanmar script.

%package -n texlive-padauk-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.002svn42617
Release:        0
Summary:        Documentation for texlive-padauk
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-padauk-doc
This package includes the documentation for texlive-padauk

%package -n texlive-padauk-fonts
Version:        %{texlive_version}.%{texlive_noarch}.3.002svn42617
Release:        0
Summary:        Severed fonts for texlive-padauk
License:        OFL-1.1
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-padauk-fonts
The  separated fonts package for texlive-padauk

%post -n texlive-padauk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-padauk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-padauk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-padauk-fonts

%files -n texlive-padauk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/padauk/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/padauk/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/padauk/OFL.txt
%{_texmfdistdir}/doc/fonts/padauk/README
%{_texmfdistdir}/doc/fonts/padauk/README.TEXLIVE

%files -n texlive-padauk
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/truetype/public/padauk/Padauk-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/padauk/Padauk-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/padauk/PadaukBook-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/padauk/PadaukBook-Regular.ttf

%files -n texlive-padauk-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-padauk
%{_datadir}/fontconfig/conf.avail/58-texlive-padauk.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-padauk/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-padauk/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-padauk/fonts.scale
%{_datadir}/fonts/texlive-padauk/Padauk-Bold.ttf
%{_datadir}/fonts/texlive-padauk/Padauk-Regular.ttf
%{_datadir}/fonts/texlive-padauk/PadaukBook-Bold.ttf
%{_datadir}/fonts/texlive-padauk/PadaukBook-Regular.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-padauk-fonts-%{texlive_version}.%{texlive_noarch}.3.002svn42617-%{release}-zypper
%endif

%package -n texlive-padcount
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn47621
Release:        0
License:        LPPL-1.0
Summary:        Pad numbers with arbitrary characters
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-padcount-doc >= %{texlive_version}
Provides:       tex(padcount.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source11:       padcount.tar.xz
Source12:       padcount.doc.tar.xz

%description -n texlive-padcount
This package provides some simple macros which will pad numbers
(or, indeed, any expanded token) with your choice of character
(defaulting to "0") to your choice of number of places
(defaults to "2"). This works not only on arabic numerals, but
on any expanded list of tokens passed to it. This makes it
suitable for, among other things, counters of all kinds.

%package -n texlive-padcount-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn47621
Release:        0
Summary:        Documentation for texlive-padcount
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-padcount-doc
This package includes the documentation for texlive-padcount

%post -n texlive-padcount
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-padcount
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-padcount
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-padcount-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/padcount/CHANGES
%{_texmfdistdir}/doc/latex/padcount/README
%{_texmfdistdir}/doc/latex/padcount/lppl.txt
%{_texmfdistdir}/doc/latex/padcount/padcount.pdf

%files -n texlive-padcount
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/padcount/padcount.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-padcount-%{texlive_version}.%{texlive_noarch}.1.0svn47621-%{release}-zypper
%endif

%package -n texlive-pagecolor
Version:        %{texlive_version}.%{texlive_noarch}.1.0isvn44487
Release:        0
License:        LPPL-1.0
Summary:        Interrogate page colour
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pagecolor-doc >= %{texlive_version}
Provides:       tex(pagecolor.sty)
Requires:       tex(color.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source13:       pagecolor.tar.xz
Source14:       pagecolor.doc.tar.xz

%description -n texlive-pagecolor
This package provides the command \thepagecolor, which gives
the current page (background) colour, i. e. the argument used
with the most recent call of \pagecolor{...}. The command
\thepagecolornone gives the same colour as \thepagecolor,
except when the page background colour is "none" (e.g., as a
result of using the \nopagecolor command). In that case
\thepagecolor is "white" and \thepagecolornone is "none".

%package -n texlive-pagecolor-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0isvn44487
Release:        0
Summary:        Documentation for texlive-pagecolor
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pagecolor-doc
This package includes the documentation for texlive-pagecolor

%post -n texlive-pagecolor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pagecolor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pagecolor
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pagecolor-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pagecolor/README
%{_texmfdistdir}/doc/latex/pagecolor/pagecolor-example.pdf
%{_texmfdistdir}/doc/latex/pagecolor/pagecolor-example.tex
%{_texmfdistdir}/doc/latex/pagecolor/pagecolor.pdf

%files -n texlive-pagecolor
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pagecolor/pagecolor.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pagecolor-%{texlive_version}.%{texlive_noarch}.1.0isvn44487-%{release}-zypper
%endif

%package -n texlive-pagecont
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        Page numbering that continues between documents
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pagecont-doc >= %{texlive_version}
Provides:       tex(pagecont.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source15:       pagecont.tar.xz
Source16:       pagecont.doc.tar.xz

%description -n texlive-pagecont
The package provides the facility that several documents can be
typeset independently with page numbers in sequence, as if they
were a single document.

%package -n texlive-pagecont-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-pagecont
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pagecont-doc
This package includes the documentation for texlive-pagecont

%post -n texlive-pagecont
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pagecont
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pagecont
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pagecont-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pagecont/README
%{_texmfdistdir}/doc/latex/pagecont/pagecont.pdf

%files -n texlive-pagecont
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pagecont/pagecont.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pagecont-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-pagenote
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn15878
Release:        0
License:        LPPL-1.0
Summary:        Notes at end of document
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pagenote-doc >= %{texlive_version}
Provides:       tex(pagenote.sty)
Requires:       tex(ifmtarg.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source17:       pagenote.tar.xz
Source18:       pagenote.doc.tar.xz

%description -n texlive-pagenote
The pagenote package provides tagged notes on a separate page
(also known as 'end notes'). Unless the memoir class is used,
the package requires the ifmtarg package.

%package -n texlive-pagenote-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn15878
Release:        0
Summary:        Documentation for texlive-pagenote
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pagenote-doc
This package includes the documentation for texlive-pagenote

%post -n texlive-pagenote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pagenote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pagenote
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pagenote-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pagenote/README
%{_texmfdistdir}/doc/latex/pagenote/pagenote.pdf

%files -n texlive-pagenote
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pagenote/pagenote.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pagenote-%{texlive_version}.%{texlive_noarch}.1.1asvn15878-%{release}-zypper
%endif

%package -n texlive-pagerange
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn16915
Release:        0
License:        LPPL-1.0
Summary:        Flexible and configurable page range typesetting
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pagerange-doc >= %{texlive_version}
Provides:       tex(pagerange-guide.cfg)
Provides:       tex(pagerange.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source19:       pagerange.tar.xz
Source20:       pagerange.doc.tar.xz

%description -n texlive-pagerange
The package defines a command \pagerange that typesets ranges
of page numbers, expanding them (e.g., adding first or last
page numbers) and standardising them.

%package -n texlive-pagerange-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn16915
Release:        0
Summary:        Documentation for texlive-pagerange
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pagerange-doc
This package includes the documentation for texlive-pagerange

%post -n texlive-pagerange
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pagerange
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pagerange
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pagerange-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pagerange/README
%{_texmfdistdir}/doc/latex/pagerange/pagerange-guide.pdf
%{_texmfdistdir}/doc/latex/pagerange/pagerange-guide.tex

%files -n texlive-pagerange
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pagerange/pagerange-guide.cfg
%{_texmfdistdir}/tex/latex/pagerange/pagerange.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pagerange-%{texlive_version}.%{texlive_noarch}.0.0.5svn16915-%{release}-zypper
%endif

%package -n texlive-pagesel
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn56105
Release:        0
License:        LPPL-1.0
Summary:        Select pages of a document for output
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pagesel-doc >= %{texlive_version}
Provides:       tex(pagesel-2016-05-16.sty)
Provides:       tex(pagesel.sty)
Requires:       tex(everyshi.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source21:       pagesel.tar.xz
Source22:       pagesel.doc.tar.xz

%description -n texlive-pagesel
Selects single pages, ranges of pages, odd pages or even pages
for output. The package is part of the oberdiek bundle.

%package -n texlive-pagesel-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10svn56105
Release:        0
Summary:        Documentation for texlive-pagesel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pagesel-doc:en)

%description -n texlive-pagesel-doc
This package includes the documentation for texlive-pagesel

%post -n texlive-pagesel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pagesel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pagesel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pagesel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pagesel/README.md
%{_texmfdistdir}/doc/latex/pagesel/pagesel.pdf

%files -n texlive-pagesel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pagesel/pagesel-2016-05-16.sty
%{_texmfdistdir}/tex/latex/pagesel/pagesel.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pagesel-%{texlive_version}.%{texlive_noarch}.1.10svn56105-%{release}-zypper
%endif

%package -n texlive-pageslts
Version:        %{texlive_version}.%{texlive_noarch}.1.2fsvn39164
Release:        0
License:        LPPL-1.0
Summary:        Variants of last page labels
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pageslts-doc >= %{texlive_version}
Provides:       tex(pageslts.sty)
Requires:       tex(alphalph.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(rerunfilecheck.sty)
Requires:       tex(undolabl.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source23:       pageslts.tar.xz
Source24:       pageslts.doc.tar.xz

%description -n texlive-pageslts
The package was designed as an extension of the lastpage
package -- as well as that package's LastPage label (created
\AtEndDocument) it adds a VeryLastPage (created
\AfterLastShipout). When more than one page numbering scheme is
in operation (as in a book class document with frontmatter),
the labels above do not give the total number of pages, so the
package also provides labels pagesLTS.<numbering scheme>, where
the numbering scheme is arabic, roman, etc. The package relies
on the undolabl package.

%package -n texlive-pageslts-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2fsvn39164
Release:        0
Summary:        Documentation for texlive-pageslts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pageslts-doc
This package includes the documentation for texlive-pageslts

%post -n texlive-pageslts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pageslts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pageslts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pageslts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pageslts/README
%{_texmfdistdir}/doc/latex/pageslts/pageslts-example.pdf
%{_texmfdistdir}/doc/latex/pageslts/pageslts-example.tex
%{_texmfdistdir}/doc/latex/pageslts/pageslts.pdf

%files -n texlive-pageslts
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pageslts/pageslts.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pageslts-%{texlive_version}.%{texlive_noarch}.1.2fsvn39164-%{release}-zypper
%endif

%package -n texlive-palatino
Version:        %{texlive_version}.%{texlive_noarch}.svn31835
Release:        0
License:        GPL-2.0-or-later
Summary:        URW "Base 35" font pack for LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-palatino-fonts >= %{texlive_version}
Provides:       tex(8rupl.fd)
Provides:       tex(eurbo10.tfm)
Provides:       tex(eurmo10.tfm)
Provides:       tex(omlupl.fd)
Provides:       tex(omsupl.fd)
Provides:       tex(ot1upl.fd)
Provides:       tex(pplb.tfm)
Provides:       tex(pplb.vf)
Provides:       tex(pplb7t.tfm)
Provides:       tex(pplb7t.vf)
Provides:       tex(pplb8c.tfm)
Provides:       tex(pplb8c.vf)
Provides:       tex(pplb8r.tfm)
Provides:       tex(pplb8t.tfm)
Provides:       tex(pplb8t.vf)
Provides:       tex(pplb9c.tfm)
Provides:       tex(pplb9c.vf)
Provides:       tex(pplb9d.tfm)
Provides:       tex(pplb9d.vf)
Provides:       tex(pplb9e.tfm)
Provides:       tex(pplb9e.vf)
Provides:       tex(pplb9o.tfm)
Provides:       tex(pplb9o.vf)
Provides:       tex(pplb9t.tfm)
Provides:       tex(pplb9t.vf)
Provides:       tex(pplbc.tfm)
Provides:       tex(pplbc.vf)
Provides:       tex(pplbc7t.tfm)
Provides:       tex(pplbc7t.vf)
Provides:       tex(pplbc8t.tfm)
Provides:       tex(pplbc8t.vf)
Provides:       tex(pplbi.tfm)
Provides:       tex(pplbi.vf)
Provides:       tex(pplbi7t.tfm)
Provides:       tex(pplbi7t.vf)
Provides:       tex(pplbi8c.tfm)
Provides:       tex(pplbi8c.vf)
Provides:       tex(pplbi8r.tfm)
Provides:       tex(pplbi8t.tfm)
Provides:       tex(pplbi8t.vf)
Provides:       tex(pplbi9c.tfm)
Provides:       tex(pplbi9c.vf)
Provides:       tex(pplbi9d.tfm)
Provides:       tex(pplbi9d.vf)
Provides:       tex(pplbi9e.tfm)
Provides:       tex(pplbi9e.vf)
Provides:       tex(pplbi9o.tfm)
Provides:       tex(pplbi9o.vf)
Provides:       tex(pplbi9t.tfm)
Provides:       tex(pplbi9t.vf)
Provides:       tex(pplbij8r.tfm)
Provides:       tex(pplbj8r.tfm)
Provides:       tex(pplbo.tfm)
Provides:       tex(pplbo.vf)
Provides:       tex(pplbo7t.tfm)
Provides:       tex(pplbo7t.vf)
Provides:       tex(pplbo8c.tfm)
Provides:       tex(pplbo8c.vf)
Provides:       tex(pplbo8r.tfm)
Provides:       tex(pplbo8t.tfm)
Provides:       tex(pplbo8t.vf)
Provides:       tex(pplbu.tfm)
Provides:       tex(pplbu.vf)
Provides:       tex(pplbu8r.tfm)
Provides:       tex(pplr.tfm)
Provides:       tex(pplr.vf)
Provides:       tex(pplr7t.tfm)
Provides:       tex(pplr7t.vf)
Provides:       tex(pplr8c.tfm)
Provides:       tex(pplr8c.vf)
Provides:       tex(pplr8r.tfm)
Provides:       tex(pplr8rn.tfm)
Provides:       tex(pplr8t.tfm)
Provides:       tex(pplr8t.vf)
Provides:       tex(pplr9c.tfm)
Provides:       tex(pplr9c.vf)
Provides:       tex(pplr9d.tfm)
Provides:       tex(pplr9d.vf)
Provides:       tex(pplr9e.tfm)
Provides:       tex(pplr9e.vf)
Provides:       tex(pplr9o.tfm)
Provides:       tex(pplr9o.vf)
Provides:       tex(pplr9t.tfm)
Provides:       tex(pplr9t.vf)
Provides:       tex(pplrc.tfm)
Provides:       tex(pplrc.vf)
Provides:       tex(pplrc7t.tfm)
Provides:       tex(pplrc7t.vf)
Provides:       tex(pplrc8r.tfm)
Provides:       tex(pplrc8t.tfm)
Provides:       tex(pplrc8t.vf)
Provides:       tex(pplrc9d.tfm)
Provides:       tex(pplrc9d.vf)
Provides:       tex(pplrc9e.tfm)
Provides:       tex(pplrc9e.vf)
Provides:       tex(pplrc9o.tfm)
Provides:       tex(pplrc9o.vf)
Provides:       tex(pplrc9t.tfm)
Provides:       tex(pplrc9t.vf)
Provides:       tex(pplri.tfm)
Provides:       tex(pplri.vf)
Provides:       tex(pplri7t.tfm)
Provides:       tex(pplri7t.vf)
Provides:       tex(pplri8c.tfm)
Provides:       tex(pplri8c.vf)
Provides:       tex(pplri8r.tfm)
Provides:       tex(pplri8t.tfm)
Provides:       tex(pplri8t.vf)
Provides:       tex(pplri9c.tfm)
Provides:       tex(pplri9c.vf)
Provides:       tex(pplri9d.tfm)
Provides:       tex(pplri9d.vf)
Provides:       tex(pplri9e.tfm)
Provides:       tex(pplri9e.vf)
Provides:       tex(pplri9o.tfm)
Provides:       tex(pplri9o.vf)
Provides:       tex(pplri9t.tfm)
Provides:       tex(pplri9t.vf)
Provides:       tex(pplrij8r.tfm)
Provides:       tex(pplro.tfm)
Provides:       tex(pplro.vf)
Provides:       tex(pplro7t.tfm)
Provides:       tex(pplro7t.vf)
Provides:       tex(pplro8c.tfm)
Provides:       tex(pplro8c.vf)
Provides:       tex(pplro8r.tfm)
Provides:       tex(pplro8t.tfm)
Provides:       tex(pplro8t.vf)
Provides:       tex(pplrr8re.tfm)
Provides:       tex(pplrre.tfm)
Provides:       tex(pplrre.vf)
Provides:       tex(pplrrn.tfm)
Provides:       tex(pplrrn.vf)
Provides:       tex(pplru.tfm)
Provides:       tex(pplru.vf)
Provides:       tex(pplru8r.tfm)
Provides:       tex(t1upl.fd)
Provides:       tex(ts1upl.fd)
Provides:       tex(upl.map)
Provides:       tex(uplb7t.tfm)
Provides:       tex(uplb7t.vf)
Provides:       tex(uplb8c.tfm)
Provides:       tex(uplb8c.vf)
Provides:       tex(uplb8r.tfm)
Provides:       tex(uplb8t.tfm)
Provides:       tex(uplb8t.vf)
Provides:       tex(uplbc7t.tfm)
Provides:       tex(uplbc7t.vf)
Provides:       tex(uplbc8t.tfm)
Provides:       tex(uplbc8t.vf)
Provides:       tex(uplbi7t.tfm)
Provides:       tex(uplbi7t.vf)
Provides:       tex(uplbi8c.tfm)
Provides:       tex(uplbi8c.vf)
Provides:       tex(uplbi8r.tfm)
Provides:       tex(uplbi8t.tfm)
Provides:       tex(uplbi8t.vf)
Provides:       tex(uplbo7t.tfm)
Provides:       tex(uplbo7t.vf)
Provides:       tex(uplbo8c.tfm)
Provides:       tex(uplbo8c.vf)
Provides:       tex(uplbo8r.tfm)
Provides:       tex(uplbo8t.tfm)
Provides:       tex(uplbo8t.vf)
Provides:       tex(uplr7t.tfm)
Provides:       tex(uplr7t.vf)
Provides:       tex(uplr8c.tfm)
Provides:       tex(uplr8c.vf)
Provides:       tex(uplr8r.tfm)
Provides:       tex(uplr8t.tfm)
Provides:       tex(uplr8t.vf)
Provides:       tex(uplrc7t.tfm)
Provides:       tex(uplrc7t.vf)
Provides:       tex(uplrc8t.tfm)
Provides:       tex(uplrc8t.vf)
Provides:       tex(uplri7t.tfm)
Provides:       tex(uplri7t.vf)
Provides:       tex(uplri8c.tfm)
Provides:       tex(uplri8c.vf)
Provides:       tex(uplri8r.tfm)
Provides:       tex(uplri8t.tfm)
Provides:       tex(uplri8t.vf)
Provides:       tex(uplro7t.tfm)
Provides:       tex(uplro7t.vf)
Provides:       tex(uplro8c.tfm)
Provides:       tex(uplro8c.vf)
Provides:       tex(uplro8r.tfm)
Provides:       tex(uplro8t.tfm)
Provides:       tex(uplro8t.vf)
Provides:       tex(zppleb7m.tfm)
Provides:       tex(zppleb7m.vf)
Provides:       tex(zppleb7t.tfm)
Provides:       tex(zppleb7t.vf)
Provides:       tex(zppleb7y.tfm)
Provides:       tex(zppleb7y.vf)
Provides:       tex(zppler7m.tfm)
Provides:       tex(zppler7m.vf)
Provides:       tex(zppler7t.tfm)
Provides:       tex(zppler7t.vf)
Provides:       tex(zppler7v.tfm)
Provides:       tex(zppler7v.vf)
Provides:       tex(zppler7y.tfm)
Provides:       tex(zppler7y.vf)
Requires:       tex(cmbsy10.tfm)
Requires:       tex(cmbx10.tfm)
Requires:       tex(cmex10.tfm)
Requires:       tex(cmmi10.tfm)
Requires:       tex(cmmib10.tfm)
Requires:       tex(cmr10.tfm)
Requires:       tex(cmsy10.tfm)
Requires:       tex(euex10.tfm)
Requires:       tex(eurb10.tfm)
Requires:       tex(eurm10.tfm)
Requires:       tex(eusb10.tfm)
Requires:       tex(eusm10.tfm)
Requires:       tex(fplmb.tfm)
Requires:       tex(fplmbi.tfm)
Requires:       tex(fplmr.tfm)
Requires:       tex(fplmri.tfm)
Requires:       tex(psyr.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source25:       palatino.tar.xz

%description -n texlive-palatino
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-palatino-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn31835
Release:        0
Summary:        Severed fonts for texlive-palatino
License:        GPL-2.0-or-later
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-palatino-fonts
The  separated fonts package for texlive-palatino

%post -n texlive-palatino
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap upl.map' >> /var/run/texlive/run-updmap

%postun -n texlive-palatino
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap upl.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-palatino
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-palatino-fonts

%files -n texlive-palatino
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/palatino/config.upl
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplbi8a.afm
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/palatino/pplri8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplb8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplbi8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplr8a.afm
%{_texmfdistdir}/fonts/afm/urw/palatino/uplri8a.afm
%{_texmfdistdir}/fonts/map/dvips/palatino/upl.map
%{_texmfdistdir}/fonts/tfm/adobe/palatino/eurbo10.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/eurmo10.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplb9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbi9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbij8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbj8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbu.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplbu8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplr9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrc9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9d.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9e.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9o.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplri9t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrij8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplro8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrr8re.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrre.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplrrn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplru.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/pplru8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppleb7m.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppleb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppleb7y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7m.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7v.tfm
%{_texmfdistdir}/fonts/tfm/adobe/palatino/zppler7y.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/palatino/uplro8t.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/palatino/uplb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplb8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/palatino/uplbi8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplbi8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/palatino/uplr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplr8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/palatino/uplri8a.pfb
%{_texmfdistdir}/fonts/type1/urw/palatino/uplri8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplb9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbc.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbi9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplbu.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplr9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrc9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9d.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9e.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9o.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplri9t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplro8t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrre.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplrrn.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/pplru.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppleb7m.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppleb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppleb7y.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7m.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7t.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7v.vf
%{_texmfdistdir}/fonts/vf/adobe/palatino/zppler7y.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/palatino/uplro8t.vf
%{_texmfdistdir}/tex/latex/palatino/8rupl.fd
%{_texmfdistdir}/tex/latex/palatino/omlupl.fd
%{_texmfdistdir}/tex/latex/palatino/omsupl.fd
%{_texmfdistdir}/tex/latex/palatino/ot1upl.fd
%{_texmfdistdir}/tex/latex/palatino/t1upl.fd
%{_texmfdistdir}/tex/latex/palatino/ts1upl.fd

%files -n texlive-palatino-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-palatino
%{_datadir}/fontconfig/conf.avail/58-texlive-palatino.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-palatino/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-palatino/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-palatino/fonts.scale
%{_datadir}/fonts/texlive-palatino/uplb8a.pfb
%{_datadir}/fonts/texlive-palatino/uplbi8a.pfb
%{_datadir}/fonts/texlive-palatino/uplr8a.pfb
%{_datadir}/fonts/texlive-palatino/uplri8a.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-palatino-fonts-%{texlive_version}.%{texlive_noarch}.svn31835-%{release}-zypper
%endif

%package -n texlive-paper
Version:        %{texlive_version}.%{texlive_noarch}.1.0lsvn34521
Release:        0
License:        GPL-2.0-or-later
Summary:        Versions of article class, tuned for scholarly publications
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-paper-doc >= %{texlive_version}
Provides:       tex(journal.cls)
Provides:       tex(journal.sty)
Provides:       tex(paper.cls)
Provides:       tex(paper.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source26:       paper.tar.xz
Source27:       paper.doc.tar.xz

%description -n texlive-paper
A pair of classes derived from article, tuned for producing
papers for journals. The classes introduce new layout options
and font commands for sections/parts, and define a new keywords
environment, subtitle and institution commands for the title
section and new commands for revisions.

%package -n texlive-paper-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0lsvn34521
Release:        0
Summary:        Documentation for texlive-paper
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-paper-doc:de)

%description -n texlive-paper-doc
This package includes the documentation for texlive-paper

%post -n texlive-paper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-paper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-paper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-paper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/paper/README
%{_texmfdistdir}/doc/latex/paper/install
%{_texmfdistdir}/doc/latex/paper/journal1.tex
%{_texmfdistdir}/doc/latex/paper/journal2.tex
%{_texmfdistdir}/doc/latex/paper/local.tex
%{_texmfdistdir}/doc/latex/paper/paper.pdf
%{_texmfdistdir}/doc/latex/paper/testj.tex
%{_texmfdistdir}/doc/latex/paper/testp.tex

%files -n texlive-paper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/paper/journal.cls
%{_texmfdistdir}/tex/latex/paper/journal.sty
%{_texmfdistdir}/tex/latex/paper/paper.cls
%{_texmfdistdir}/tex/latex/paper/paper.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-paper-%{texlive_version}.%{texlive_noarch}.1.0lsvn34521-%{release}-zypper
%endif

%package -n texlive-papercdcase
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Origami-style folding paper CD case
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-papercdcase-doc >= %{texlive_version}
Provides:       tex(papercdcase.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source28:       papercdcase.tar.xz
Source29:       papercdcase.doc.tar.xz

%description -n texlive-papercdcase
This package implements a LaTeX style file to produce
origami-style folding paper CD cases.

%package -n texlive-papercdcase-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-papercdcase
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-papercdcase-doc
This package includes the documentation for texlive-papercdcase

%post -n texlive-papercdcase
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-papercdcase
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-papercdcase
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-papercdcase-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/papercdcase/example.tex
%{_texmfdistdir}/doc/latex/papercdcase/interactive.tex
%{_texmfdistdir}/doc/latex/papercdcase/papercdcase.pdf

%files -n texlive-papercdcase
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/papercdcase/papercdcase.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-papercdcase-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-papermas
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn23667
Release:        0
License:        LPPL-1.0
Summary:        Compute the mass of a printed version of a document
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-papermas-doc >= %{texlive_version}
Provides:       tex(papermas.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pageslts.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source30:       papermas.tar.xz
Source31:       papermas.doc.tar.xz

%description -n texlive-papermas
The package computes the number of sheets of paper used by, and
hence the mass of a document. This is useful (for example) when
calculating postal charges.

%package -n texlive-papermas-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn23667
Release:        0
Summary:        Documentation for texlive-papermas
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-papermas-doc
This package includes the documentation for texlive-papermas

%post -n texlive-papermas
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-papermas
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-papermas
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-papermas-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/papermas/README
%{_texmfdistdir}/doc/latex/papermas/papermas-example.pdf
%{_texmfdistdir}/doc/latex/papermas/papermas-example.tex
%{_texmfdistdir}/doc/latex/papermas/papermas.pdf

%files -n texlive-papermas
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/papermas/papermas.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-papermas-%{texlive_version}.%{texlive_noarch}.1.0hsvn23667-%{release}-zypper
%endif

%package -n texlive-papertex
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn19230
Release:        0
License:        LPPL-1.0
Summary:        Class for newspapers, etcetera
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-papertex-doc >= %{texlive_version}
Provides:       tex(papertex.cls)
Requires:       tex(article.cls)
Requires:       tex(color.sty)
Requires:       tex(datetime.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyphenat.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multido.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(setspace.sty)
Requires:       tex(textpos.sty)
Requires:       tex(wrapfig.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source32:       papertex.tar.xz
Source33:       papertex.doc.tar.xz

%description -n texlive-papertex
This class allows LaTeX users to create a paperTeX newspaper.
The final document has a front page and as many inner pages as
desired. News items appear one after another and the user can
choose the number of columns, style and so on. The class allows
users to create newsletters too.

%package -n texlive-papertex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn19230
Release:        0
Summary:        Documentation for texlive-papertex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-papertex-doc
This package includes the documentation for texlive-papertex

%post -n texlive-papertex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-papertex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-papertex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-papertex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/papertex/CHANGES
%{_texmfdistdir}/doc/latex/papertex/README
%{_texmfdistdir}/doc/latex/papertex/example/example.pdf
%{_texmfdistdir}/doc/latex/papertex/example/example.tex
%{_texmfdistdir}/doc/latex/papertex/example/img/ireland.jpg
%{_texmfdistdir}/doc/latex/papertex/example/img/weather/clouds.jpg
%{_texmfdistdir}/doc/latex/papertex/example/img/weather/rain.jpg
%{_texmfdistdir}/doc/latex/papertex/example/img/weather/sun.jpg
%{_texmfdistdir}/doc/latex/papertex/papertex.pdf

%files -n texlive-papertex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/papertex/papertex.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-papertex-%{texlive_version}.%{texlive_noarch}.1.2bsvn19230-%{release}-zypper
%endif

%package -n texlive-paracol
Version:        %{texlive_version}.%{texlive_noarch}.1.35svn49560
Release:        0
License:        LPPL-1.0
Summary:        Multiple columns with texts "in parallel"
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-paracol-doc >= %{texlive_version}
Provides:       tex(paracol.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source34:       paracol.tar.xz
Source35:       paracol.doc.tar.xz

%description -n texlive-paracol
The package provides yet another multi-column typesetting
mechanism by which you produce multi-column (e.g., bilingual)
document switching and sychronizing each corresponding part in
"parallel".

%package -n texlive-paracol-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.35svn49560
Release:        0
Summary:        Documentation for texlive-paracol
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-paracol-doc
This package includes the documentation for texlive-paracol

%post -n texlive-paracol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-paracol
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-paracol
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-paracol-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/paracol/README
%{_texmfdistdir}/doc/latex/paracol/paracol-man.pdf
%{_texmfdistdir}/doc/latex/paracol/paracol-man.tex
%{_texmfdistdir}/doc/latex/paracol/paracol.pdf

%files -n texlive-paracol
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/paracol/paracol.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-paracol-%{texlive_version}.%{texlive_noarch}.1.35svn49560-%{release}-zypper
%endif

%package -n texlive-parades
Version:        %{texlive_version}.%{texlive_noarch}.svn40042
Release:        0
License:        LPPL-1.0
Summary:        Tabulators and space between paragraphs in galley approach
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-parades-doc >= %{texlive_version}
Provides:       tex(paravesp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source36:       parades.tar.xz
Source37:       parades.doc.tar.xz

%description -n texlive-parades
The LaTeX package paravesp controls the spaces above and below
paragraphs. The python script parades.py generates paragraph
styles with support of space above, space below and tabulators.
The system imposes the galley approach on the document.

%package -n texlive-parades-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn40042
Release:        0
Summary:        Documentation for texlive-parades
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-parades-doc
This package includes the documentation for texlive-parades

%post -n texlive-parades
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-parades
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-parades
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-parades-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/parades/README
%{_texmfdistdir}/doc/latex/parades/example/README.example
%{_texmfdistdir}/doc/latex/parades/example/SConstruct
%{_texmfdistdir}/doc/latex/parades/example/paras.py
%{_texmfdistdir}/doc/latex/parades/example/paras.sty
%{_texmfdistdir}/doc/latex/parades/example/udhr.pdf
%{_texmfdistdir}/doc/latex/parades/example/udhr.tex
%{_texmfdistdir}/doc/latex/parades/example/udhr.xsl
%{_texmfdistdir}/doc/latex/parades/example/udhr_eng.xml
%{_texmfdistdir}/doc/latex/parades/parades.pdf
%{_texmfdistdir}/doc/latex/parades/parades.py

%files -n texlive-parades
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/parades/paravesp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-parades-%{texlive_version}.%{texlive_noarch}.svn40042-%{release}-zypper
%endif

%package -n texlive-paralist
Version:        %{texlive_version}.%{texlive_noarch}.2.7svn43021
Release:        0
License:        LPPL-1.0
Summary:        Enumerate and itemize within paragraphs
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-paralist-doc >= %{texlive_version}
Provides:       tex(paralist.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source38:       paralist.tar.xz
Source39:       paralist.doc.tar.xz

%description -n texlive-paralist
Provides enumerate and itemize environments that can be used
within paragraphs to format the items either as running text or
as separate paragraphs with a preceding number or symbol. Also
provides compacted versions of enumerate and itemize.

%package -n texlive-paralist-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.7svn43021
Release:        0
Summary:        Documentation for texlive-paralist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-paralist-doc
This package includes the documentation for texlive-paralist

%post -n texlive-paralist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-paralist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-paralist
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-paralist-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/paralist/README
%{_texmfdistdir}/doc/latex/paralist/paralist.pdf

%files -n texlive-paralist
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/paralist/paralist.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-paralist-%{texlive_version}.%{texlive_noarch}.2.7svn43021-%{release}-zypper
%endif

%package -n texlive-parallel
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Typeset parallel texts
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-parallel-doc >= %{texlive_version}
Provides:       tex(parallel.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source40:       parallel.tar.xz
Source41:       parallel.doc.tar.xz

%description -n texlive-parallel
Provides a parallel environment which allows two potentially
different texts to be typeset in two columns, while maintaining
alignment. The two columns may be on the same page, or on
facing pages. This arrangement of text is commonly used when
typesetting translations, but it can have value when comparing
any two texts.

%package -n texlive-parallel-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-parallel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-parallel-doc
This package includes the documentation for texlive-parallel

%post -n texlive-parallel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-parallel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-parallel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-parallel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/parallel/example1.tex
%{_texmfdistdir}/doc/latex/parallel/example2.tex
%{_texmfdistdir}/doc/latex/parallel/parallel.pdf
%{_texmfdistdir}/doc/latex/parallel/readme

%files -n texlive-parallel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/parallel/parallel.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-parallel-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-paratype
Version:        %{texlive_version}.%{texlive_noarch}.svn32859
Release:        0
License:        LPPL-1.0
Summary:        LaTeX support for free fonts by ParaType
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-paratype-fonts >= %{texlive_version}
Recommends:     texlive-paratype-doc >= %{texlive_version}
Provides:       tex(IL2PTMono-TLF.fd)
Provides:       tex(IL2PTSans-TLF.fd)
Provides:       tex(IL2PTSansCaption-TLF.fd)
Provides:       tex(IL2PTSansNarrow-TLF.fd)
Provides:       tex(IL2PTSerif-TLF.fd)
Provides:       tex(IL2PTSerifCaption-TLF.fd)
Provides:       tex(OT1PTMono-TLF.fd)
Provides:       tex(OT1PTSans-TLF.fd)
Provides:       tex(OT1PTSansCaption-TLF.fd)
Provides:       tex(OT1PTSansNarrow-TLF.fd)
Provides:       tex(OT1PTSerif-TLF.fd)
Provides:       tex(OT1PTSerifCaption-TLF.fd)
Provides:       tex(OT2PTMono-TLF.fd)
Provides:       tex(OT2PTSans-TLF.fd)
Provides:       tex(OT2PTSansCaption-TLF.fd)
Provides:       tex(OT2PTSansNarrow-TLF.fd)
Provides:       tex(OT2PTSerif-TLF.fd)
Provides:       tex(OT2PTSerifCaption-TLF.fd)
Provides:       tex(PTMono-Bold-tlf-il2--base.tfm)
Provides:       tex(PTMono-Bold-tlf-il2.tfm)
Provides:       tex(PTMono-Bold-tlf-il2.vf)
Provides:       tex(PTMono-Bold-tlf-ot1--base.tfm)
Provides:       tex(PTMono-Bold-tlf-ot1.tfm)
Provides:       tex(PTMono-Bold-tlf-ot1.vf)
Provides:       tex(PTMono-Bold-tlf-ot2.tfm)
Provides:       tex(PTMono-Bold-tlf-t1--base.tfm)
Provides:       tex(PTMono-Bold-tlf-t1.tfm)
Provides:       tex(PTMono-Bold-tlf-t1.vf)
Provides:       tex(PTMono-Bold-tlf-t2a--base.tfm)
Provides:       tex(PTMono-Bold-tlf-t2a.tfm)
Provides:       tex(PTMono-Bold-tlf-t2a.vf)
Provides:       tex(PTMono-Bold-tlf-t2b--base.tfm)
Provides:       tex(PTMono-Bold-tlf-t2b.tfm)
Provides:       tex(PTMono-Bold-tlf-t2b.vf)
Provides:       tex(PTMono-Bold-tlf-t2c--base.tfm)
Provides:       tex(PTMono-Bold-tlf-t2c.tfm)
Provides:       tex(PTMono-Bold-tlf-t2c.vf)
Provides:       tex(PTMono-Bold-tlf-ts1--base.tfm)
Provides:       tex(PTMono-Bold-tlf-ts1.tfm)
Provides:       tex(PTMono-Bold-tlf-ts1.vf)
Provides:       tex(PTMono-Bold-tlf-x2--base.tfm)
Provides:       tex(PTMono-Bold-tlf-x2.tfm)
Provides:       tex(PTMono-Bold-tlf-x2.vf)
Provides:       tex(PTMono-BoldSlanted-tlf-il2.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-ot1.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-ot2.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t1--base.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t1.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t1.vf)
Provides:       tex(PTMono-BoldSlanted-tlf-t2a--base.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t2a.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t2a.vf)
Provides:       tex(PTMono-BoldSlanted-tlf-t2b--base.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t2b.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t2b.vf)
Provides:       tex(PTMono-BoldSlanted-tlf-t2c--base.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t2c.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-t2c.vf)
Provides:       tex(PTMono-BoldSlanted-tlf-ts1--base.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-ts1.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-ts1.vf)
Provides:       tex(PTMono-BoldSlanted-tlf-x2--base.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-x2.tfm)
Provides:       tex(PTMono-BoldSlanted-tlf-x2.vf)
Provides:       tex(PTMono-Regular-tlf-il2--base.tfm)
Provides:       tex(PTMono-Regular-tlf-il2.tfm)
Provides:       tex(PTMono-Regular-tlf-il2.vf)
Provides:       tex(PTMono-Regular-tlf-ot1--base.tfm)
Provides:       tex(PTMono-Regular-tlf-ot1.tfm)
Provides:       tex(PTMono-Regular-tlf-ot1.vf)
Provides:       tex(PTMono-Regular-tlf-ot2.tfm)
Provides:       tex(PTMono-Regular-tlf-t1--base.tfm)
Provides:       tex(PTMono-Regular-tlf-t1.tfm)
Provides:       tex(PTMono-Regular-tlf-t1.vf)
Provides:       tex(PTMono-Regular-tlf-t2a--base.tfm)
Provides:       tex(PTMono-Regular-tlf-t2a.tfm)
Provides:       tex(PTMono-Regular-tlf-t2a.vf)
Provides:       tex(PTMono-Regular-tlf-t2b--base.tfm)
Provides:       tex(PTMono-Regular-tlf-t2b.tfm)
Provides:       tex(PTMono-Regular-tlf-t2b.vf)
Provides:       tex(PTMono-Regular-tlf-t2c--base.tfm)
Provides:       tex(PTMono-Regular-tlf-t2c.tfm)
Provides:       tex(PTMono-Regular-tlf-t2c.vf)
Provides:       tex(PTMono-Regular-tlf-ts1--base.tfm)
Provides:       tex(PTMono-Regular-tlf-ts1.tfm)
Provides:       tex(PTMono-Regular-tlf-ts1.vf)
Provides:       tex(PTMono-Regular-tlf-x2--base.tfm)
Provides:       tex(PTMono-Regular-tlf-x2.tfm)
Provides:       tex(PTMono-Regular-tlf-x2.vf)
Provides:       tex(PTMono-Slanted-tlf-il2.tfm)
Provides:       tex(PTMono-Slanted-tlf-ot1.tfm)
Provides:       tex(PTMono-Slanted-tlf-ot2.tfm)
Provides:       tex(PTMono-Slanted-tlf-t1--base.tfm)
Provides:       tex(PTMono-Slanted-tlf-t1.tfm)
Provides:       tex(PTMono-Slanted-tlf-t1.vf)
Provides:       tex(PTMono-Slanted-tlf-t2a--base.tfm)
Provides:       tex(PTMono-Slanted-tlf-t2a.tfm)
Provides:       tex(PTMono-Slanted-tlf-t2a.vf)
Provides:       tex(PTMono-Slanted-tlf-t2b--base.tfm)
Provides:       tex(PTMono-Slanted-tlf-t2b.tfm)
Provides:       tex(PTMono-Slanted-tlf-t2b.vf)
Provides:       tex(PTMono-Slanted-tlf-t2c--base.tfm)
Provides:       tex(PTMono-Slanted-tlf-t2c.tfm)
Provides:       tex(PTMono-Slanted-tlf-t2c.vf)
Provides:       tex(PTMono-Slanted-tlf-ts1--base.tfm)
Provides:       tex(PTMono-Slanted-tlf-ts1.tfm)
Provides:       tex(PTMono-Slanted-tlf-ts1.vf)
Provides:       tex(PTMono-Slanted-tlf-x2--base.tfm)
Provides:       tex(PTMono-Slanted-tlf-x2.tfm)
Provides:       tex(PTMono-Slanted-tlf-x2.vf)
Provides:       tex(PTMono.sty)
Provides:       tex(PTSans-Bold-tlf-il2.tfm)
Provides:       tex(PTSans-Bold-tlf-ot1.tfm)
Provides:       tex(PTSans-Bold-tlf-ot2.tfm)
Provides:       tex(PTSans-Bold-tlf-t1--base.tfm)
Provides:       tex(PTSans-Bold-tlf-t1.tfm)
Provides:       tex(PTSans-Bold-tlf-t1.vf)
Provides:       tex(PTSans-Bold-tlf-t2a--base.tfm)
Provides:       tex(PTSans-Bold-tlf-t2a.tfm)
Provides:       tex(PTSans-Bold-tlf-t2a.vf)
Provides:       tex(PTSans-Bold-tlf-t2b--base.tfm)
Provides:       tex(PTSans-Bold-tlf-t2b.tfm)
Provides:       tex(PTSans-Bold-tlf-t2b.vf)
Provides:       tex(PTSans-Bold-tlf-t2c--base.tfm)
Provides:       tex(PTSans-Bold-tlf-t2c.tfm)
Provides:       tex(PTSans-Bold-tlf-t2c.vf)
Provides:       tex(PTSans-Bold-tlf-ts1--base.tfm)
Provides:       tex(PTSans-Bold-tlf-ts1.tfm)
Provides:       tex(PTSans-Bold-tlf-ts1.vf)
Provides:       tex(PTSans-Bold-tlf-x2--base.tfm)
Provides:       tex(PTSans-Bold-tlf-x2.tfm)
Provides:       tex(PTSans-Bold-tlf-x2.vf)
Provides:       tex(PTSans-BoldItalic-tlf-il2.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-ot1.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-ot2.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t1.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t1.vf)
Provides:       tex(PTSans-BoldItalic-tlf-t2a--base.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t2a.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t2a.vf)
Provides:       tex(PTSans-BoldItalic-tlf-t2b--base.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t2b.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t2b.vf)
Provides:       tex(PTSans-BoldItalic-tlf-t2c--base.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t2c.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-t2c.vf)
Provides:       tex(PTSans-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-ts1.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-ts1.vf)
Provides:       tex(PTSans-BoldItalic-tlf-x2--base.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-x2.tfm)
Provides:       tex(PTSans-BoldItalic-tlf-x2.vf)
Provides:       tex(PTSans-Caption-tlf-il2.tfm)
Provides:       tex(PTSans-Caption-tlf-ot1.tfm)
Provides:       tex(PTSans-Caption-tlf-ot2.tfm)
Provides:       tex(PTSans-Caption-tlf-t1--base.tfm)
Provides:       tex(PTSans-Caption-tlf-t1.tfm)
Provides:       tex(PTSans-Caption-tlf-t1.vf)
Provides:       tex(PTSans-Caption-tlf-t2a--base.tfm)
Provides:       tex(PTSans-Caption-tlf-t2a.tfm)
Provides:       tex(PTSans-Caption-tlf-t2a.vf)
Provides:       tex(PTSans-Caption-tlf-t2b--base.tfm)
Provides:       tex(PTSans-Caption-tlf-t2b.tfm)
Provides:       tex(PTSans-Caption-tlf-t2b.vf)
Provides:       tex(PTSans-Caption-tlf-t2c--base.tfm)
Provides:       tex(PTSans-Caption-tlf-t2c.tfm)
Provides:       tex(PTSans-Caption-tlf-t2c.vf)
Provides:       tex(PTSans-Caption-tlf-ts1--base.tfm)
Provides:       tex(PTSans-Caption-tlf-ts1.tfm)
Provides:       tex(PTSans-Caption-tlf-ts1.vf)
Provides:       tex(PTSans-Caption-tlf-x2--base.tfm)
Provides:       tex(PTSans-Caption-tlf-x2.tfm)
Provides:       tex(PTSans-Caption-tlf-x2.vf)
Provides:       tex(PTSans-CaptionBold-tlf-il2.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-ot1.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-ot2.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t1--base.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t1.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t1.vf)
Provides:       tex(PTSans-CaptionBold-tlf-t2a--base.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t2a.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t2a.vf)
Provides:       tex(PTSans-CaptionBold-tlf-t2b--base.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t2b.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t2b.vf)
Provides:       tex(PTSans-CaptionBold-tlf-t2c--base.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t2c.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-t2c.vf)
Provides:       tex(PTSans-CaptionBold-tlf-ts1--base.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-ts1.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-ts1.vf)
Provides:       tex(PTSans-CaptionBold-tlf-x2--base.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-x2.tfm)
Provides:       tex(PTSans-CaptionBold-tlf-x2.vf)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-il2.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ot1.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ot2.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t1--base.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t1.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t1.vf)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2a--base.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2a.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2a.vf)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2b--base.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2b.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2b.vf)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2c--base.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2c.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-t2c.vf)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ts1--base.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ts1.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-ts1.vf)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-x2--base.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-x2.tfm)
Provides:       tex(PTSans-CaptionBoldSlanted-tlf-x2.vf)
Provides:       tex(PTSans-CaptionSlanted-tlf-il2.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-ot1.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-ot2.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t1--base.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t1.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t1.vf)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2a--base.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2a.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2a.vf)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2b--base.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2b.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2b.vf)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2c--base.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2c.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-t2c.vf)
Provides:       tex(PTSans-CaptionSlanted-tlf-ts1--base.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-ts1.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-ts1.vf)
Provides:       tex(PTSans-CaptionSlanted-tlf-x2--base.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-x2.tfm)
Provides:       tex(PTSans-CaptionSlanted-tlf-x2.vf)
Provides:       tex(PTSans-Italic-tlf-il2.tfm)
Provides:       tex(PTSans-Italic-tlf-ot1.tfm)
Provides:       tex(PTSans-Italic-tlf-ot2.tfm)
Provides:       tex(PTSans-Italic-tlf-t1--base.tfm)
Provides:       tex(PTSans-Italic-tlf-t1.tfm)
Provides:       tex(PTSans-Italic-tlf-t1.vf)
Provides:       tex(PTSans-Italic-tlf-t2a--base.tfm)
Provides:       tex(PTSans-Italic-tlf-t2a.tfm)
Provides:       tex(PTSans-Italic-tlf-t2a.vf)
Provides:       tex(PTSans-Italic-tlf-t2b--base.tfm)
Provides:       tex(PTSans-Italic-tlf-t2b.tfm)
Provides:       tex(PTSans-Italic-tlf-t2b.vf)
Provides:       tex(PTSans-Italic-tlf-t2c--base.tfm)
Provides:       tex(PTSans-Italic-tlf-t2c.tfm)
Provides:       tex(PTSans-Italic-tlf-t2c.vf)
Provides:       tex(PTSans-Italic-tlf-ts1--base.tfm)
Provides:       tex(PTSans-Italic-tlf-ts1.tfm)
Provides:       tex(PTSans-Italic-tlf-ts1.vf)
Provides:       tex(PTSans-Italic-tlf-x2--base.tfm)
Provides:       tex(PTSans-Italic-tlf-x2.tfm)
Provides:       tex(PTSans-Italic-tlf-x2.vf)
Provides:       tex(PTSans-Narrow-tlf-il2.tfm)
Provides:       tex(PTSans-Narrow-tlf-ot1.tfm)
Provides:       tex(PTSans-Narrow-tlf-ot2.tfm)
Provides:       tex(PTSans-Narrow-tlf-t1--base.tfm)
Provides:       tex(PTSans-Narrow-tlf-t1.tfm)
Provides:       tex(PTSans-Narrow-tlf-t1.vf)
Provides:       tex(PTSans-Narrow-tlf-t2a--base.tfm)
Provides:       tex(PTSans-Narrow-tlf-t2a.tfm)
Provides:       tex(PTSans-Narrow-tlf-t2a.vf)
Provides:       tex(PTSans-Narrow-tlf-t2b--base.tfm)
Provides:       tex(PTSans-Narrow-tlf-t2b.tfm)
Provides:       tex(PTSans-Narrow-tlf-t2b.vf)
Provides:       tex(PTSans-Narrow-tlf-t2c--base.tfm)
Provides:       tex(PTSans-Narrow-tlf-t2c.tfm)
Provides:       tex(PTSans-Narrow-tlf-t2c.vf)
Provides:       tex(PTSans-Narrow-tlf-ts1--base.tfm)
Provides:       tex(PTSans-Narrow-tlf-ts1.tfm)
Provides:       tex(PTSans-Narrow-tlf-ts1.vf)
Provides:       tex(PTSans-Narrow-tlf-x2--base.tfm)
Provides:       tex(PTSans-Narrow-tlf-x2.tfm)
Provides:       tex(PTSans-Narrow-tlf-x2.vf)
Provides:       tex(PTSans-NarrowBold-tlf-il2.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-ot1.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-ot2.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t1--base.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t1.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t1.vf)
Provides:       tex(PTSans-NarrowBold-tlf-t2a--base.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t2a.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t2a.vf)
Provides:       tex(PTSans-NarrowBold-tlf-t2b--base.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t2b.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t2b.vf)
Provides:       tex(PTSans-NarrowBold-tlf-t2c--base.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t2c.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-t2c.vf)
Provides:       tex(PTSans-NarrowBold-tlf-ts1--base.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-ts1.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-ts1.vf)
Provides:       tex(PTSans-NarrowBold-tlf-x2--base.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-x2.tfm)
Provides:       tex(PTSans-NarrowBold-tlf-x2.vf)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-il2.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ot1.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ot2.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t1--base.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t1.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t1.vf)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2a--base.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2a.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2a.vf)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2b--base.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2b.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2b.vf)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2c--base.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2c.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-t2c.vf)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ts1--base.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ts1.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-ts1.vf)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-x2--base.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-x2.tfm)
Provides:       tex(PTSans-NarrowBoldSlanted-tlf-x2.vf)
Provides:       tex(PTSans-NarrowSlanted-tlf-il2.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-ot1.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-ot2.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t1--base.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t1.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t1.vf)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2a--base.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2a.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2a.vf)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2b--base.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2b.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2b.vf)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2c--base.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2c.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-t2c.vf)
Provides:       tex(PTSans-NarrowSlanted-tlf-ts1--base.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-ts1.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-ts1.vf)
Provides:       tex(PTSans-NarrowSlanted-tlf-x2--base.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-x2.tfm)
Provides:       tex(PTSans-NarrowSlanted-tlf-x2.vf)
Provides:       tex(PTSans-Regular-tlf-il2.tfm)
Provides:       tex(PTSans-Regular-tlf-ot1.tfm)
Provides:       tex(PTSans-Regular-tlf-ot2.tfm)
Provides:       tex(PTSans-Regular-tlf-t1--base.tfm)
Provides:       tex(PTSans-Regular-tlf-t1.tfm)
Provides:       tex(PTSans-Regular-tlf-t1.vf)
Provides:       tex(PTSans-Regular-tlf-t2a--base.tfm)
Provides:       tex(PTSans-Regular-tlf-t2a.tfm)
Provides:       tex(PTSans-Regular-tlf-t2a.vf)
Provides:       tex(PTSans-Regular-tlf-t2b--base.tfm)
Provides:       tex(PTSans-Regular-tlf-t2b.tfm)
Provides:       tex(PTSans-Regular-tlf-t2b.vf)
Provides:       tex(PTSans-Regular-tlf-t2c--base.tfm)
Provides:       tex(PTSans-Regular-tlf-t2c.tfm)
Provides:       tex(PTSans-Regular-tlf-t2c.vf)
Provides:       tex(PTSans-Regular-tlf-ts1--base.tfm)
Provides:       tex(PTSans-Regular-tlf-ts1.tfm)
Provides:       tex(PTSans-Regular-tlf-ts1.vf)
Provides:       tex(PTSans-Regular-tlf-x2--base.tfm)
Provides:       tex(PTSans-Regular-tlf-x2.tfm)
Provides:       tex(PTSans-Regular-tlf-x2.vf)
Provides:       tex(PTSans.sty)
Provides:       tex(PTSansCaption.sty)
Provides:       tex(PTSansNarrow.sty)
Provides:       tex(PTSerif-Bold-tlf-il2.tfm)
Provides:       tex(PTSerif-Bold-tlf-ot1.tfm)
Provides:       tex(PTSerif-Bold-tlf-ot2.tfm)
Provides:       tex(PTSerif-Bold-tlf-t1--base.tfm)
Provides:       tex(PTSerif-Bold-tlf-t1.tfm)
Provides:       tex(PTSerif-Bold-tlf-t1.vf)
Provides:       tex(PTSerif-Bold-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-Bold-tlf-t2a.tfm)
Provides:       tex(PTSerif-Bold-tlf-t2a.vf)
Provides:       tex(PTSerif-Bold-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-Bold-tlf-t2b.tfm)
Provides:       tex(PTSerif-Bold-tlf-t2b.vf)
Provides:       tex(PTSerif-Bold-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-Bold-tlf-t2c.tfm)
Provides:       tex(PTSerif-Bold-tlf-t2c.vf)
Provides:       tex(PTSerif-Bold-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-Bold-tlf-ts1.tfm)
Provides:       tex(PTSerif-Bold-tlf-ts1.vf)
Provides:       tex(PTSerif-Bold-tlf-x2--base.tfm)
Provides:       tex(PTSerif-Bold-tlf-x2.tfm)
Provides:       tex(PTSerif-Bold-tlf-x2.vf)
Provides:       tex(PTSerif-BoldItalic-tlf-il2.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-ot1.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-ot2.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t1.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t1.vf)
Provides:       tex(PTSerif-BoldItalic-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t2a.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t2a.vf)
Provides:       tex(PTSerif-BoldItalic-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t2b.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t2b.vf)
Provides:       tex(PTSerif-BoldItalic-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t2c.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-t2c.vf)
Provides:       tex(PTSerif-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-ts1.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-ts1.vf)
Provides:       tex(PTSerif-BoldItalic-tlf-x2--base.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-x2.tfm)
Provides:       tex(PTSerif-BoldItalic-tlf-x2.vf)
Provides:       tex(PTSerif-BoldSlanted-tlf-il2.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-ot1.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-ot2.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t1--base.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t1.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t1.vf)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2a.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2a.vf)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2b.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2b.vf)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2c.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-t2c.vf)
Provides:       tex(PTSerif-BoldSlanted-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-ts1.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-ts1.vf)
Provides:       tex(PTSerif-BoldSlanted-tlf-x2--base.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-x2.tfm)
Provides:       tex(PTSerif-BoldSlanted-tlf-x2.vf)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-il2.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ot1.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t1--base.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t1.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t1.vf)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2a.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2a.vf)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2b.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2b.vf)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2c.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-t2c.vf)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ts1.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-ts1.vf)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-x2--base.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-x2.tfm)
Provides:       tex(PTSerif-BoldUprightItalic-tlf-x2.vf)
Provides:       tex(PTSerif-Caption-tlf-il2.tfm)
Provides:       tex(PTSerif-Caption-tlf-ot1.tfm)
Provides:       tex(PTSerif-Caption-tlf-ot2.tfm)
Provides:       tex(PTSerif-Caption-tlf-t1--base.tfm)
Provides:       tex(PTSerif-Caption-tlf-t1.tfm)
Provides:       tex(PTSerif-Caption-tlf-t1.vf)
Provides:       tex(PTSerif-Caption-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-Caption-tlf-t2a.tfm)
Provides:       tex(PTSerif-Caption-tlf-t2a.vf)
Provides:       tex(PTSerif-Caption-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-Caption-tlf-t2b.tfm)
Provides:       tex(PTSerif-Caption-tlf-t2b.vf)
Provides:       tex(PTSerif-Caption-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-Caption-tlf-t2c.tfm)
Provides:       tex(PTSerif-Caption-tlf-t2c.vf)
Provides:       tex(PTSerif-Caption-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-Caption-tlf-ts1.tfm)
Provides:       tex(PTSerif-Caption-tlf-ts1.vf)
Provides:       tex(PTSerif-Caption-tlf-x2--base.tfm)
Provides:       tex(PTSerif-Caption-tlf-x2.tfm)
Provides:       tex(PTSerif-Caption-tlf-x2.vf)
Provides:       tex(PTSerif-CaptionItalic-tlf-il2.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-ot1.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-ot2.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t1--base.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t1.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t1.vf)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2a.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2a.vf)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2b.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2b.vf)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2c.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-t2c.vf)
Provides:       tex(PTSerif-CaptionItalic-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-ts1.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-ts1.vf)
Provides:       tex(PTSerif-CaptionItalic-tlf-x2--base.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-x2.tfm)
Provides:       tex(PTSerif-CaptionItalic-tlf-x2.vf)
Provides:       tex(PTSerif-CaptionSlanted-tlf-il2.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-ot1.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-ot2.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t1--base.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t1.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t1.vf)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2a.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2a.vf)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2b.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2b.vf)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2c.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-t2c.vf)
Provides:       tex(PTSerif-CaptionSlanted-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-ts1.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-ts1.vf)
Provides:       tex(PTSerif-CaptionSlanted-tlf-x2--base.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-x2.tfm)
Provides:       tex(PTSerif-CaptionSlanted-tlf-x2.vf)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-il2.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ot1.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t1--base.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t1.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t1.vf)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2a.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2a.vf)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2b.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2b.vf)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2c.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-t2c.vf)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ts1.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-ts1.vf)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-x2--base.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-x2.tfm)
Provides:       tex(PTSerif-CaptionUprightItalic-tlf-x2.vf)
Provides:       tex(PTSerif-Italic-tlf-il2.tfm)
Provides:       tex(PTSerif-Italic-tlf-ot1.tfm)
Provides:       tex(PTSerif-Italic-tlf-ot2.tfm)
Provides:       tex(PTSerif-Italic-tlf-t1--base.tfm)
Provides:       tex(PTSerif-Italic-tlf-t1.tfm)
Provides:       tex(PTSerif-Italic-tlf-t1.vf)
Provides:       tex(PTSerif-Italic-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-Italic-tlf-t2a.tfm)
Provides:       tex(PTSerif-Italic-tlf-t2a.vf)
Provides:       tex(PTSerif-Italic-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-Italic-tlf-t2b.tfm)
Provides:       tex(PTSerif-Italic-tlf-t2b.vf)
Provides:       tex(PTSerif-Italic-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-Italic-tlf-t2c.tfm)
Provides:       tex(PTSerif-Italic-tlf-t2c.vf)
Provides:       tex(PTSerif-Italic-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-Italic-tlf-ts1.tfm)
Provides:       tex(PTSerif-Italic-tlf-ts1.vf)
Provides:       tex(PTSerif-Italic-tlf-x2--base.tfm)
Provides:       tex(PTSerif-Italic-tlf-x2.tfm)
Provides:       tex(PTSerif-Italic-tlf-x2.vf)
Provides:       tex(PTSerif-Regular-tlf-il2.tfm)
Provides:       tex(PTSerif-Regular-tlf-ot1.tfm)
Provides:       tex(PTSerif-Regular-tlf-ot2.tfm)
Provides:       tex(PTSerif-Regular-tlf-t1--base.tfm)
Provides:       tex(PTSerif-Regular-tlf-t1.tfm)
Provides:       tex(PTSerif-Regular-tlf-t1.vf)
Provides:       tex(PTSerif-Regular-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-Regular-tlf-t2a.tfm)
Provides:       tex(PTSerif-Regular-tlf-t2a.vf)
Provides:       tex(PTSerif-Regular-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-Regular-tlf-t2b.tfm)
Provides:       tex(PTSerif-Regular-tlf-t2b.vf)
Provides:       tex(PTSerif-Regular-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-Regular-tlf-t2c.tfm)
Provides:       tex(PTSerif-Regular-tlf-t2c.vf)
Provides:       tex(PTSerif-Regular-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-Regular-tlf-ts1.tfm)
Provides:       tex(PTSerif-Regular-tlf-ts1.vf)
Provides:       tex(PTSerif-Regular-tlf-x2--base.tfm)
Provides:       tex(PTSerif-Regular-tlf-x2.tfm)
Provides:       tex(PTSerif-Regular-tlf-x2.vf)
Provides:       tex(PTSerif-Slanted-tlf-il2.tfm)
Provides:       tex(PTSerif-Slanted-tlf-ot1.tfm)
Provides:       tex(PTSerif-Slanted-tlf-ot2.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t1--base.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t1.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t1.vf)
Provides:       tex(PTSerif-Slanted-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t2a.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t2a.vf)
Provides:       tex(PTSerif-Slanted-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t2b.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t2b.vf)
Provides:       tex(PTSerif-Slanted-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t2c.tfm)
Provides:       tex(PTSerif-Slanted-tlf-t2c.vf)
Provides:       tex(PTSerif-Slanted-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-Slanted-tlf-ts1.tfm)
Provides:       tex(PTSerif-Slanted-tlf-ts1.vf)
Provides:       tex(PTSerif-Slanted-tlf-x2--base.tfm)
Provides:       tex(PTSerif-Slanted-tlf-x2.tfm)
Provides:       tex(PTSerif-Slanted-tlf-x2.vf)
Provides:       tex(PTSerif-UprightItalic-tlf-il2.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-ot1.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t1--base.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t1.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t1.vf)
Provides:       tex(PTSerif-UprightItalic-tlf-t2a--base.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t2a.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t2a.vf)
Provides:       tex(PTSerif-UprightItalic-tlf-t2b--base.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t2b.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t2b.vf)
Provides:       tex(PTSerif-UprightItalic-tlf-t2c--base.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t2c.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-t2c.vf)
Provides:       tex(PTSerif-UprightItalic-tlf-ts1--base.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-ts1.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-ts1.vf)
Provides:       tex(PTSerif-UprightItalic-tlf-x2--base.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-x2.tfm)
Provides:       tex(PTSerif-UprightItalic-tlf-x2.vf)
Provides:       tex(PTSerif.sty)
Provides:       tex(PTSerifCaption.sty)
Provides:       tex(T1PTMono-TLF.fd)
Provides:       tex(T1PTSans-TLF.fd)
Provides:       tex(T1PTSansCaption-TLF.fd)
Provides:       tex(T1PTSansNarrow-TLF.fd)
Provides:       tex(T1PTSerif-TLF.fd)
Provides:       tex(T1PTSerifCaption-TLF.fd)
Provides:       tex(T2APTMono-TLF.fd)
Provides:       tex(T2APTSans-TLF.fd)
Provides:       tex(T2APTSansCaption-TLF.fd)
Provides:       tex(T2APTSansNarrow-TLF.fd)
Provides:       tex(T2APTSerif-TLF.fd)
Provides:       tex(T2APTSerifCaption-TLF.fd)
Provides:       tex(T2BPTMono-TLF.fd)
Provides:       tex(T2BPTSans-TLF.fd)
Provides:       tex(T2BPTSansCaption-TLF.fd)
Provides:       tex(T2BPTSansNarrow-TLF.fd)
Provides:       tex(T2BPTSerif-TLF.fd)
Provides:       tex(T2BPTSerifCaption-TLF.fd)
Provides:       tex(T2CPTMono-TLF.fd)
Provides:       tex(T2CPTSans-TLF.fd)
Provides:       tex(T2CPTSansCaption-TLF.fd)
Provides:       tex(T2CPTSansNarrow-TLF.fd)
Provides:       tex(T2CPTSerif-TLF.fd)
Provides:       tex(T2CPTSerifCaption-TLF.fd)
Provides:       tex(TS1PTMono-TLF.fd)
Provides:       tex(TS1PTSans-TLF.fd)
Provides:       tex(TS1PTSansCaption-TLF.fd)
Provides:       tex(TS1PTSansNarrow-TLF.fd)
Provides:       tex(TS1PTSerif-TLF.fd)
Provides:       tex(TS1PTSerifCaption-TLF.fd)
Provides:       tex(X2PTMono-TLF.fd)
Provides:       tex(X2PTSans-TLF.fd)
Provides:       tex(X2PTSansCaption-TLF.fd)
Provides:       tex(X2PTSansNarrow-TLF.fd)
Provides:       tex(X2PTSerif-TLF.fd)
Provides:       tex(X2PTSerifCaption-TLF.fd)
Provides:       tex(paratype-truetype.map)
Provides:       tex(paratype-type1.map)
Provides:       tex(paratype.sty)
Provides:       tex(ptmono_il2.enc)
Provides:       tex(ptmono_ot1.enc)
Provides:       tex(ptmono_ot2.enc)
Provides:       tex(ptmono_t1.enc)
Provides:       tex(ptmono_t2a.enc)
Provides:       tex(ptmono_t2b.enc)
Provides:       tex(ptmono_t2c.enc)
Provides:       tex(ptmono_ts1.enc)
Provides:       tex(ptmono_x2.enc)
Provides:       tex(ptsans_il2.enc)
Provides:       tex(ptsans_ot1.enc)
Provides:       tex(ptsans_ot2.enc)
Provides:       tex(ptsans_t1.enc)
Provides:       tex(ptsans_t2a.enc)
Provides:       tex(ptsans_t2b.enc)
Provides:       tex(ptsans_t2c.enc)
Provides:       tex(ptsans_ts1.enc)
Provides:       tex(ptsans_x2.enc)
Provides:       tex(ptserif_il2.enc)
Provides:       tex(ptserif_ot1.enc)
Provides:       tex(ptserif_ot2.enc)
Provides:       tex(ptserif_t1.enc)
Provides:       tex(ptserif_t2a.enc)
Provides:       tex(ptserif_t2b.enc)
Provides:       tex(ptserif_t2c.enc)
Provides:       tex(ptserif_ts1.enc)
Provides:       tex(ptserif_x2.enc)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source42:       paratype.tar.xz
Source43:       paratype.doc.tar.xz

%description -n texlive-paratype
The package offers LaTeX support for the fonts PT Sans, PT
Serif and PT Mono developed by ParaType for the project "Public
Types of Russian Federation", and released under an open user
license. The fonts themselves are provided in both the TrueType
and Type 1 formats, both created by ParaType). The fonts
provide encodings OT1, T1, IL2, TS1, T2* and X2. The package
provides a convenient replacement of the two packages ptsans
and ptserif.

%package -n texlive-paratype-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn32859
Release:        0
Summary:        Documentation for texlive-paratype
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-paratype-doc
This package includes the documentation for texlive-paratype

%package -n texlive-paratype-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn32859
Release:        0
Summary:        Severed fonts for texlive-paratype
License:        LPPL-1.0
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-paratype-fonts
The  separated fonts package for texlive-paratype

%post -n texlive-paratype
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap paratype-type1.map' >> /var/run/texlive/run-updmap

%postun -n texlive-paratype
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap paratype-type1.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-paratype
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-paratype-fonts

%files -n texlive-paratype-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/paratype/CHANGELOG
%{_texmfdistdir}/doc/fonts/paratype/OT_TT_Install_E.txt
%{_texmfdistdir}/doc/fonts/paratype/OT_TT_Install_R.txt
%{_texmfdistdir}/doc/fonts/paratype/PT_Free_Font_License_eng_1.3.txt
%{_texmfdistdir}/doc/fonts/paratype/PT_Free_Font_License_rus_1.3.txt
%{_texmfdistdir}/doc/fonts/paratype/README
%{_texmfdistdir}/doc/fonts/paratype/manifest.txt
%{_texmfdistdir}/doc/fonts/paratype/paratype-sample.pdf
%{_texmfdistdir}/doc/fonts/paratype/paratype-sample.tex
%{_texmfdistdir}/doc/fonts/paratype/paratype.pdf
%{_texmfdistdir}/doc/fonts/paratype/paratype.tex

%files -n texlive-paratype
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/paratype/ptmono/PTM55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptmono/PTM55F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptmono/PTM75F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptmono/PTM75F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTC55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTC55F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTC75F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTC75F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTN57F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTN57F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTN77F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTN77F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS55F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS56F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS56F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS75F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS75F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS76F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS76F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF55F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF56F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF56F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF75F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF75F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF76F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF76F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTZ55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTZ55F.inf
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTZ56F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTZ56F.inf
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_ot2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptmono_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_ot2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_ot2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_x2.enc
%{_texmfdistdir}/fonts/map/dvips/paratype/paratype-truetype.map
%{_texmfdistdir}/fonts/map/dvips/paratype/paratype-type1.map
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-il2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-BoldSlanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-il2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Regular-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptmono/PTMono-Slanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionSlanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowSlanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldSlanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionSlanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-ot2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Slanted-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-UprightItalic-tlf-x2.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptmono/PTM55F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptmono/PTM75F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTC55F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTC75F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTN57F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTN77F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS55F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS56F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS75F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS76F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF55F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF56F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF75F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF76F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTZ55F.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTZ56F.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptmono/PTM55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptmono/PTM55F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptmono/PTM75F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptmono/PTM75F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTC55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTC55F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTC75F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTC75F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTN57F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTN57F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTN77F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTN77F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS55F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS56F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS56F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS75F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS75F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS76F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS76F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF55F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF56F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF56F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF75F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF75F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF76F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF76F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptserif/PTZ55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTZ55F.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/paratype/ptserif/PTZ56F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTZ56F.pfm
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-il2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Bold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-BoldSlanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-BoldSlanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-BoldSlanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-BoldSlanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-BoldSlanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-BoldSlanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-il2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Regular-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Slanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Slanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Slanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Slanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Slanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptmono/PTMono-Slanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBoldSlanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionSlanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionSlanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionSlanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionSlanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBoldSlanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowSlanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowSlanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowSlanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowSlanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldSlanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldSlanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldSlanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldSlanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldUprightItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionSlanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionSlanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionSlanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionUprightItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Slanted-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Slanted-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Slanted-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Slanted-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Slanted-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Slanted-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-UprightItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-UprightItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-UprightItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-UprightItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-UprightItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-UprightItalic-tlf-x2.vf
%{_texmfdistdir}/tex/latex/paratype/IL2PTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT2PTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT2PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT2PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT2PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT2PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT2PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/PTMono.sty
%{_texmfdistdir}/tex/latex/paratype/PTSans.sty
%{_texmfdistdir}/tex/latex/paratype/PTSansCaption.sty
%{_texmfdistdir}/tex/latex/paratype/PTSansNarrow.sty
%{_texmfdistdir}/tex/latex/paratype/PTSerif.sty
%{_texmfdistdir}/tex/latex/paratype/PTSerifCaption.sty
%{_texmfdistdir}/tex/latex/paratype/T1PTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTMono-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/paratype.sty

%files -n texlive-paratype-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-paratype
%{_datadir}/fontconfig/conf.avail/58-texlive-paratype.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-paratype.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-paratype.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-paratype/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-paratype/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-paratype/fonts.scale
%{_datadir}/fonts/texlive-paratype/PTM55F.ttf
%{_datadir}/fonts/texlive-paratype/PTM75F.ttf
%{_datadir}/fonts/texlive-paratype/PTC55F.ttf
%{_datadir}/fonts/texlive-paratype/PTC75F.ttf
%{_datadir}/fonts/texlive-paratype/PTN57F.ttf
%{_datadir}/fonts/texlive-paratype/PTN77F.ttf
%{_datadir}/fonts/texlive-paratype/PTS55F.ttf
%{_datadir}/fonts/texlive-paratype/PTS56F.ttf
%{_datadir}/fonts/texlive-paratype/PTS75F.ttf
%{_datadir}/fonts/texlive-paratype/PTS76F.ttf
%{_datadir}/fonts/texlive-paratype/PTF55F.ttf
%{_datadir}/fonts/texlive-paratype/PTF56F.ttf
%{_datadir}/fonts/texlive-paratype/PTF75F.ttf
%{_datadir}/fonts/texlive-paratype/PTF76F.ttf
%{_datadir}/fonts/texlive-paratype/PTZ55F.ttf
%{_datadir}/fonts/texlive-paratype/PTZ56F.ttf
%{_datadir}/fonts/texlive-paratype/PTM55F.pfb
%{_datadir}/fonts/texlive-paratype/PTM75F.pfb
%{_datadir}/fonts/texlive-paratype/PTC55F.pfb
%{_datadir}/fonts/texlive-paratype/PTC75F.pfb
%{_datadir}/fonts/texlive-paratype/PTN57F.pfb
%{_datadir}/fonts/texlive-paratype/PTN77F.pfb
%{_datadir}/fonts/texlive-paratype/PTS55F.pfb
%{_datadir}/fonts/texlive-paratype/PTS56F.pfb
%{_datadir}/fonts/texlive-paratype/PTS75F.pfb
%{_datadir}/fonts/texlive-paratype/PTS76F.pfb
%{_datadir}/fonts/texlive-paratype/PTF55F.pfb
%{_datadir}/fonts/texlive-paratype/PTF56F.pfb
%{_datadir}/fonts/texlive-paratype/PTF75F.pfb
%{_datadir}/fonts/texlive-paratype/PTF76F.pfb
%{_datadir}/fonts/texlive-paratype/PTZ55F.pfb
%{_datadir}/fonts/texlive-paratype/PTZ56F.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-paratype-fonts-%{texlive_version}.%{texlive_noarch}.svn32859-%{release}-zypper
%endif

%package -n texlive-paresse
Version:        %{texlive_version}.%{texlive_noarch}.5.0.1svn56621
Release:        0
License:        LPPL-1.0
Summary:        Define simple macros for greek letters
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-paresse-doc >= %{texlive_version}
Provides:       tex(paresse-old.sty)
Provides:       tex(paresse-utf8.sty)
Provides:       tex(paresse.sty)
Requires:       tex(expl3.sty)
Requires:       tex(iftex.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source44:       paresse.tar.xz
Source45:       paresse.doc.tar.xz

%description -n texlive-paresse
The package defines macros using SS to type greek letters so
that the user may (for example) type SSa to get the effect of
$\alpha$. However, it takes care only of letters which have a
macro name like \alpha or \Omega.

%package -n texlive-paresse-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.0.1svn56621
Release:        0
Summary:        Documentation for texlive-paresse
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-paresse-doc:fr)

%description -n texlive-paresse-doc
This package includes the documentation for texlive-paresse

%post -n texlive-paresse
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-paresse
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-paresse
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-paresse-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/paresse/LISEZMOI.md
%{_texmfdistdir}/doc/latex/paresse/MANIFEST.md
%{_texmfdistdir}/doc/latex/paresse/README.md
%{_texmfdistdir}/doc/latex/paresse/paresse-eng.pdf
%{_texmfdistdir}/doc/latex/paresse/paresse-eng.tex
%{_texmfdistdir}/doc/latex/paresse/paresse-fra.pdf
%{_texmfdistdir}/doc/latex/paresse/paresse-fra.tex
%{_texmfdistdir}/doc/latex/paresse/paresse.pdf

%files -n texlive-paresse
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/paresse/paresse-old.sty
%{_texmfdistdir}/tex/latex/paresse/paresse-utf8.sty
%{_texmfdistdir}/tex/latex/paresse/paresse.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-paresse-%{texlive_version}.%{texlive_noarch}.5.0.1svn56621-%{release}-zypper
%endif

%package -n texlive-parnotes
Version:        %{texlive_version}.%{texlive_noarch}.3bsvn51720
Release:        0
License:        LPPL-1.0
Summary:        Notes after every paragraph (or elsewhere)
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-parnotes-doc >= %{texlive_version}
Provides:       tex(parnotes.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source46:       parnotes.tar.xz
Source47:       parnotes.doc.tar.xz

%description -n texlive-parnotes
The package provides the \parnote command. The notes are set as
(normal) running paragraphs; placement is at the end of each
paragraph, or manually, using the \parnotes command.

%package -n texlive-parnotes-doc
Version:        %{texlive_version}.%{texlive_noarch}.3bsvn51720
Release:        0
Summary:        Documentation for texlive-parnotes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-parnotes-doc
This package includes the documentation for texlive-parnotes

%post -n texlive-parnotes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-parnotes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-parnotes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-parnotes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/parnotes/README.md
%{_texmfdistdir}/doc/latex/parnotes/parnotes.pdf
%{_texmfdistdir}/doc/latex/parnotes/parnotes.tex

%files -n texlive-parnotes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/parnotes/parnotes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-parnotes-%{texlive_version}.%{texlive_noarch}.3bsvn51720-%{release}-zypper
%endif

%package -n texlive-parrun
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Typesets (two) streams of text running parallel
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-parrun-doc >= %{texlive_version}
Provides:       tex(parrun.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source48:       parrun.tar.xz
Source49:       parrun.doc.tar.xz

%description -n texlive-parrun
For typesetting translated text and the original source,
parallel on the same page, one above the other.

%package -n texlive-parrun-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-parrun
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-parrun-doc
This package includes the documentation for texlive-parrun

%post -n texlive-parrun
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-parrun
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-parrun
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-parrun-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/parrun/parrun.pdf
%{_texmfdistdir}/doc/latex/parrun/readme

%files -n texlive-parrun
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/parrun/parrun.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-parrun-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-parsa
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn54840
Release:        0
License:        LPPL-1.0
Summary:        A XeLaTeX package for theses and dissertations at Iranian Universities
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-parsa-doc >= %{texlive_version}
Provides:       tex(parsa.sty)
Requires:       tex(adjustbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(multirow.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source50:       parsa.tar.xz
Source51:       parsa.doc.tar.xz

%description -n texlive-parsa
A package for preparing dissertations and theses for Iranian
universities as fast and as efficiently as possible. The
package depends on xparse, fancyhdr, graphicx, multirow, float,
and adjustbox.

%package -n texlive-parsa-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn54840
Release:        0
Summary:        Documentation for texlive-parsa
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-parsa-doc:fa)

%description -n texlive-parsa-doc
This package includes the documentation for texlive-parsa

%post -n texlive-parsa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-parsa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-parsa
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-parsa-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/parsa/README.md
%{_texmfdistdir}/doc/xelatex/parsa/parsa-doc.pdf
%{_texmfdistdir}/doc/xelatex/parsa/parsa-doc.tex

%files -n texlive-parsa
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xelatex/parsa/parsa.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-parsa-%{texlive_version}.%{texlive_noarch}.1.3svn54840-%{release}-zypper
%endif

%package -n texlive-parselines
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn21475
Release:        0
License:        LPPL-1.0
Summary:        Apply a macro to each line of an environment
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-parselines-doc >= %{texlive_version}
Provides:       tex(parselines.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source52:       parselines.tar.xz
Source53:       parselines.doc.tar.xz

%description -n texlive-parselines
The package defines an environment "parse lines" which
processes each line of an environment with a macro. An example
of shading the lines of an environment is given.

%package -n texlive-parselines-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn21475
Release:        0
Summary:        Documentation for texlive-parselines
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-parselines-doc
This package includes the documentation for texlive-parselines

%post -n texlive-parselines
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-parselines
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-parselines
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-parselines-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/parselines/README
%{_texmfdistdir}/doc/latex/parselines/parselines.pdf

%files -n texlive-parselines
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/parselines/parselines.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-parselines-%{texlive_version}.%{texlive_noarch}.1.4svn21475-%{release}-zypper
%endif

%package -n texlive-parskip
Version:        %{texlive_version}.%{texlive_noarch}.2.0hsvn58358
Release:        0
License:        LPPL-1.0
Summary:        Layout with zero \parindent, non-zero \parskip
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-parskip-doc >= %{texlive_version}
Provides:       tex(parskip-2001-04-09.sty)
Provides:       tex(parskip.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source54:       parskip.tar.xz
Source55:       parskip.doc.tar.xz

%description -n texlive-parskip
Simply changing \parskip and \parindent leaves a layout that is
untidy; this package (though it is no substitute for a
properly-designed class) helps alleviate this untidiness.

%package -n texlive-parskip-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0hsvn58358
Release:        0
Summary:        Documentation for texlive-parskip
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-parskip-doc
This package includes the documentation for texlive-parskip

%post -n texlive-parskip
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-parskip
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-parskip
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-parskip-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/parskip/MANIFEST.md
%{_texmfdistdir}/doc/latex/parskip/README.md
%{_texmfdistdir}/doc/latex/parskip/changes.txt
%{_texmfdistdir}/doc/latex/parskip/parskip-code.pdf
%{_texmfdistdir}/doc/latex/parskip/parskip-code.tex
%{_texmfdistdir}/doc/latex/parskip/parskip.pdf
%{_texmfdistdir}/doc/latex/parskip/parskip.tex

%files -n texlive-parskip
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/parskip/parskip-2001-04-09.sty
%{_texmfdistdir}/tex/latex/parskip/parskip.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-parskip-%{texlive_version}.%{texlive_noarch}.2.0hsvn58358-%{release}-zypper
%endif

%package -n texlive-pas-cours
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn55859
Release:        0
License:        LPPL-1.0
Summary:        Macros useful in preparing teaching material
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pas-cours-doc >= %{texlive_version}
Provides:       tex(pas-cours.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(auto-pst-pdf.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(ifplatform.sty)
Provides:       tex(macro-calculs.tex)
Provides:       tex(macro-patrons.tex)
Provides:       tex(macro-solides.tex)
Provides:       tex(macro-styles.tex)
Requires:       tex(numprint.sty)
Requires:       tex(pst-plot.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source56:       pas-cours.tar.xz
Source57:       pas-cours.doc.tar.xz

%description -n texlive-pas-cours
Several groups of macros cover different branches of
mathematics.

%package -n texlive-pas-cours-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn55859
Release:        0
Summary:        Documentation for texlive-pas-cours
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pas-cours-doc
This package includes the documentation for texlive-pas-cours

%post -n texlive-pas-cours
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pas-cours
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pas-cours
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pas-cours-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pas-cours/MiKTeX-screenshot01.png
%{_texmfdistdir}/doc/latex/pas-cours/MiKTeX-screenshot02.png
%{_texmfdistdir}/doc/latex/pas-cours/MiKTeX-screenshot03.png
%{_texmfdistdir}/doc/latex/pas-cours/README.TEXLIVE
%{_texmfdistdir}/doc/latex/pas-cours/README.txt
%{_texmfdistdir}/doc/latex/pas-cours/attention.png
%{_texmfdistdir}/doc/latex/pas-cours/coeur.png
%{_texmfdistdir}/doc/latex/pas-cours/pas-cours.tex
%{_texmfdistdir}/doc/latex/pas-cours/prerequis.png
%{_texmfdistdir}/doc/latex/pas-cours/warning-perso.png

%files -n texlive-pas-cours
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pas-cours/macro-calculs.tex
%{_texmfdistdir}/tex/latex/pas-cours/macro-patrons.tex
%{_texmfdistdir}/tex/latex/pas-cours/macro-solides.tex
%{_texmfdistdir}/tex/latex/pas-cours/macro-styles.tex
%{_texmfdistdir}/tex/latex/pas-cours/pas-cours.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pas-cours-%{texlive_version}.%{texlive_noarch}.1.9svn55859-%{release}-zypper
%endif

%package -n texlive-pas-crosswords
Version:        %{texlive_version}.%{texlive_noarch}.1.03svn32313
Release:        0
License:        LPPL-1.0
Summary:        Creating crossword grids, using TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pas-crosswords-doc >= %{texlive_version}
Provides:       tex(pas-crosswords.sty)
Requires:       tex(fp.sty)
Requires:       tex(multido.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source58:       pas-crosswords.tar.xz
Source59:       pas-crosswords.doc.tar.xz

%description -n texlive-pas-crosswords
The package produces crossword grids, using a wide variety of
colours and decorations of the grids and the text in them. The
package uses TikZ for its graphical output.

%package -n texlive-pas-crosswords-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.03svn32313
Release:        0
Summary:        Documentation for texlive-pas-crosswords
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pas-crosswords-doc:fr)

%description -n texlive-pas-crosswords-doc
This package includes the documentation for texlive-pas-crosswords

%post -n texlive-pas-crosswords
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pas-crosswords
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pas-crosswords
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pas-crosswords-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pas-crosswords/README
%{_texmfdistdir}/doc/latex/pas-crosswords/pas-crosswords.pdf
%{_texmfdistdir}/doc/latex/pas-crosswords/pas-crosswords.tex

%files -n texlive-pas-crosswords
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pas-crosswords/pas-crosswords.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pas-crosswords-%{texlive_version}.%{texlive_noarch}.1.03svn32313-%{release}-zypper
%endif

%package -n texlive-pas-cv
Version:        %{texlive_version}.%{texlive_noarch}.2.01svn32263
Release:        0
License:        LPPL-1.0
Summary:        Flexible typesetting of Curricula Vitae
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pas-cv-doc >= %{texlive_version}
Provides:       tex(macro-andromede.tex)
Provides:       tex(macro-architecte.tex)
Provides:       tex(macro-centaure.tex)
Provides:       tex(macro-dynamique.tex)
Provides:       tex(macro-gaia.tex)
Provides:       tex(macro-jupiter.tex)
Provides:       tex(macro-mars.tex)
Provides:       tex(macro-neptune.tex)
Provides:       tex(macro-orion.tex)
Provides:       tex(macro-pegase.tex)
Provides:       tex(macro-pluton.tex)
Provides:       tex(macro-saturne.tex)
Provides:       tex(macro-univers.tex)
Provides:       tex(macro-uranus.tex)
Provides:       tex(macro-venus.tex)
Provides:       tex(pas-cv.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(fp.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source60:       pas-cv.tar.xz
Source61:       pas-cv.doc.tar.xz

%description -n texlive-pas-cv
The package provides the framework for typesetting a Curriculum
Vitae (composed in French), together with a number of "themes"
that may be used with the package. (The use of the themes may
be seen in the package's examples/ collection.) The author
hints that conversion for use with other languages (than
French) should be possible.

%package -n texlive-pas-cv-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.01svn32263
Release:        0
Summary:        Documentation for texlive-pas-cv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pas-cv-doc:fr)

%description -n texlive-pas-cv-doc
This package includes the documentation for texlive-pas-cv

%post -n texlive-pas-cv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pas-cv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pas-cv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pas-cv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-andromede.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-andromede.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-architecte.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-architecte.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-centaure.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-centaure.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-dynamique.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-dynamique.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-gaia.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-gaia.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-jupiter.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-jupiter.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-mars.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-mars.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-neptune.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-neptune.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-orion.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-orion.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pegase.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pegase.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pluton.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-pluton.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-saturne.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-saturne.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-univers.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-univers.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-uranus.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-uranus.tex
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-venus.pdf
%{_texmfdistdir}/doc/latex/pas-cv/examples/cv-venus.tex
%{_texmfdistdir}/doc/latex/pas-cv/pas-cv.pdf
%{_texmfdistdir}/doc/latex/pas-cv/pas-cv.tex
%{_texmfdistdir}/doc/latex/pas-cv/photo.png

%files -n texlive-pas-cv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pas-cv/macro-andromede.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-architecte.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-centaure.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-dynamique.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-gaia.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-jupiter.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-mars.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-neptune.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-orion.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-pegase.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-pluton.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-saturne.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-univers.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-uranus.tex
%{_texmfdistdir}/tex/latex/pas-cv/macro-venus.tex
%{_texmfdistdir}/tex/latex/pas-cv/pas-cv.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pas-cv-%{texlive_version}.%{texlive_noarch}.2.01svn32263-%{release}-zypper
%endif

%package -n texlive-pas-tableur
Version:        %{texlive_version}.%{texlive_noarch}.2.01svn39542
Release:        0
License:        LPPL-1.0
Summary:        Create a spreadsheet layout
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pas-tableur-doc >= %{texlive_version}
Provides:       tex(pas-tableur.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source62:       pas-tableur.tar.xz
Source63:       pas-tableur.doc.tar.xz

%description -n texlive-pas-tableur
The package provides commands for creating a grid of
rectangles, and commands for populating locations in the grid.
PGF/TikZ is used for placement and population of the cells.

%package -n texlive-pas-tableur-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.01svn39542
Release:        0
Summary:        Documentation for texlive-pas-tableur
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pas-tableur-doc
This package includes the documentation for texlive-pas-tableur

%post -n texlive-pas-tableur
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pas-tableur
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pas-tableur
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pas-tableur-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pas-tableur/README
%{_texmfdistdir}/doc/latex/pas-tableur/README.TEXLIVE
%{_texmfdistdir}/doc/latex/pas-tableur/doc.codes.tex
%{_texmfdistdir}/doc/latex/pas-tableur/doc.styles.tex
%{_texmfdistdir}/doc/latex/pas-tableur/pas-tableur.tex

%files -n texlive-pas-tableur
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pas-tableur/pas-tableur.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pas-tableur-%{texlive_version}.%{texlive_noarch}.2.01svn39542-%{release}-zypper
%endif

%package -n texlive-passivetex
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Support package for XML/SGML typesetting
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       tex(dummyels.sty)
Provides:       tex(fotex.sty)
Provides:       tex(mlnames.sty)
Provides:       tex(teixml.sty)
Provides:       tex(teixmlslides.sty)
Provides:       tex(ucharacters.sty)
Provides:       tex(unicode.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(array.sty)
Requires:       tex(bm.sty)
Requires:       tex(color.sty)
Requires:       tex(eucal.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(multicol.sty)
Requires:       tex(nameref.sty)
Requires:       tex(pifont.sty)
Requires:       tex(rotating.sty)
Requires:       tex(stmaryrd.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(times.sty)
Requires:       tex(tipa.sty)
Requires:       tex(tone.sty)
Requires:       tex(ulem.sty)
Requires:       tex(url.sty)
Requires:       tex(wasysym.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source64:       passivetex.tar.xz

%description -n texlive-passivetex
Packages providing XML parsing, UTF-8 parsing, Unicode
entities, and common formatting object definitions for jadetex.

%post -n texlive-passivetex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-passivetex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-passivetex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-passivetex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/xmltex/passivetex/dummyels.sty
%{_texmfdistdir}/tex/xmltex/passivetex/fotex.sty
%{_texmfdistdir}/tex/xmltex/passivetex/fotex.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/mlnames.sty
%{_texmfdistdir}/tex/xmltex/passivetex/tei.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/teiprintslides.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/teislides.xmt
%{_texmfdistdir}/tex/xmltex/passivetex/teixml.sty
%{_texmfdistdir}/tex/xmltex/passivetex/teixmlslides.sty
%{_texmfdistdir}/tex/xmltex/passivetex/ucharacters.sty
%{_texmfdistdir}/tex/xmltex/passivetex/unicode.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-passivetex-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-patch
Version:        %{texlive_version}.%{texlive_noarch}.svn42428
Release:        0
License:        LPPL-1.0
Summary:        Patch loaded packages, etcetera
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source65:       patch.source.tar.xz

%description -n texlive-patch
The package defines macros that allow patching of existing
commands, specifying those parts of the existing macro to be
replaced, along with the replacements. Thus it provides more
sophisticated manipulation than a package like patchcmd, which
only permits modification by adding commands at the beginning
or end of an existing definition. The package is distributed in
a relative of LaTeX doc format: it will run unmodified, though
it benefits from docstrip treatment.

%post -n texlive-patch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-patch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-patch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-patch
%defattr(-,root,root,755)
%{_texmfdistdir}/source/generic/patch/patch.doc
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-patch-%{texlive_version}.%{texlive_noarch}.svn42428-%{release}-zypper
%endif

%package -n texlive-patchcmd
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn41379
Release:        0
License:        LPPL-1.0
Summary:        Change the definition of an existing command
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-patchcmd-doc >= %{texlive_version}
Provides:       tex(patchcmd.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source66:       patchcmd.tar.xz
Source67:       patchcmd.doc.tar.xz

%description -n texlive-patchcmd
The package provides a command \patchcommand that can be used
to add material at the beginning and/or the end of the
replacement text of an existing macro. It works for macros with
any number of normal arguments, including those that were
defined with \DeclareRobustCommand.

%package -n texlive-patchcmd-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn41379
Release:        0
Summary:        Documentation for texlive-patchcmd
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-patchcmd-doc
This package includes the documentation for texlive-patchcmd

%post -n texlive-patchcmd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-patchcmd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-patchcmd
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-patchcmd-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/patchcmd/README
%{_texmfdistdir}/doc/latex/patchcmd/patchcmd.pdf

%files -n texlive-patchcmd
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/patchcmd/patchcmd.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-patchcmd-%{texlive_version}.%{texlive_noarch}.1.05svn41379-%{release}-zypper
%endif

%package -n texlive-patgen
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn57972
Release:        0
License:        SUSE-Public-Domain
Summary:        Generate hyphenation patterns
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-kpathsea >= %{texlive_version}
#!BuildIgnore: texlive-kpathsea
Requires(pre):  texlive-patgen-bin >= %{texlive_version}
#!BuildIgnore: texlive-patgen-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       man(patgen.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source68:       patgen.doc.tar.xz

%description -n texlive-patgen
Patgen takes a list of hyphenated words and generates a set of
patterns that can be used by the TeX 82 hyphenation algorithm.
Patgen was originally written by Frank M. Liang as part of his
Stanford Ph.D. work, and has always been distributed alongside
the other programs coming from the Stanford TeX project. It was
updated in 1991 by Peter Breitenlohner for the new 8-bit
features of TeX version 3. (These updates related to
input/output and programming overhead; the actual pattern
generation algorithms were not changed.) Patgen is currently
maintained as part of TeX Live.

%post -n texlive-patgen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-patgen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-patgen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-patgen
%defattr(-,root,root,755)
%{_mandir}/man1/patgen.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-patgen-%{texlive_version}.%{texlive_noarch}.2.4svn57972-%{release}-zypper
%endif

%package -n texlive-patgen2-tutorial
Version:        %{texlive_version}.%{texlive_noarch}.svn16490
Release:        0
License:        GPL-2.0-or-later
Summary:        A tutorial on the use of Patgen 2
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source69:       patgen2-tutorial.doc.tar.xz

%description -n texlive-patgen2-tutorial
This document describes the use of Patgen 2 to create
hyphenation patterns for wide ranges of languages.

%post -n texlive-patgen2-tutorial
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-patgen2-tutorial
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-patgen2-tutorial
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-patgen2-tutorial
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/patgen2-tutorial/patgen2.pdf
%{_texmfdistdir}/doc/support/patgen2-tutorial/patgen2.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-patgen2-tutorial-%{texlive_version}.%{texlive_noarch}.svn16490-%{release}-zypper
%endif

%package -n texlive-path
Version:        %{texlive_version}.%{texlive_noarch}.3.05svn22045
Release:        0
License:        LPPL-1.0
Summary:        Typeset paths, making them breakable
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-path-doc >= %{texlive_version}
Provides:       tex(path.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source70:       path.tar.xz
Source71:       path.doc.tar.xz

%description -n texlive-path
Defines a macro \path|...|, similar to the LaTeX \verb|...|,
that sets the text in typewriter font and allows hyphen-less
breaks at punctuation characters. The set of characters to be
regarded as punctuation may be changed from the package's
default.

%package -n texlive-path-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.05svn22045
Release:        0
Summary:        Documentation for texlive-path
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-path-doc
This package includes the documentation for texlive-path

%post -n texlive-path
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-path
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-path
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-path-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/path/path-doc.pdf
%{_texmfdistdir}/doc/generic/path/path-doc.tex

%files -n texlive-path
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/path/path.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-path-%{texlive_version}.%{texlive_noarch}.3.05svn22045-%{release}-zypper
%endif

%package -n texlive-pauldoc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn16005
Release:        0
License:        LPPL-1.0
Summary:        German LaTeX package documentation
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pauldoc-doc >= %{texlive_version}
Provides:       tex(pauldoc.sty)
Requires:       tex(babel.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(inputenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source72:       pauldoc.tar.xz
Source73:       pauldoc.doc.tar.xz

%description -n texlive-pauldoc
The package provides helpers for German language package
documentation.

%package -n texlive-pauldoc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn16005
Release:        0
Summary:        Documentation for texlive-pauldoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pauldoc-doc:de)

%description -n texlive-pauldoc-doc
This package includes the documentation for texlive-pauldoc

%post -n texlive-pauldoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pauldoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pauldoc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pauldoc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pauldoc/README
%{_texmfdistdir}/doc/latex/pauldoc/pauldoc.pdf

%files -n texlive-pauldoc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pauldoc/pauldoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pauldoc-%{texlive_version}.%{texlive_noarch}.0.0.5svn16005-%{release}-zypper
%endif

%package -n texlive-pawpict
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21629
Release:        0
License:        GPL-2.0-or-later
Summary:        Using graphics from PAW
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pawpict-doc >= %{texlive_version}
Provides:       tex(pawpict.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source74:       pawpict.tar.xz
Source75:       pawpict.doc.tar.xz

%description -n texlive-pawpict
Support for the easy inclusion of graphics made by PAW (Physics
Analysis Workstation). You need to have PAW installed on your
system to benefit from this package.

%package -n texlive-pawpict-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21629
Release:        0
Summary:        Documentation for texlive-pawpict
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pawpict-doc
This package includes the documentation for texlive-pawpict

%post -n texlive-pawpict
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pawpict
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pawpict
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pawpict-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pawpict/README

%files -n texlive-pawpict
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pawpict/pawpict.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pawpict-%{texlive_version}.%{texlive_noarch}.1.0svn21629-%{release}-zypper
%endif

%package -n texlive-pax
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1lsvn54512
Release:        0
License:        LPPL-1.0
Summary:        Extract and reinsert PDF annotations with pdfTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pax-bin >= %{texlive_version}
#!BuildIgnore: texlive-pax-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pax-doc >= %{texlive_version}
Requires:       perl(File::Which)
#!BuildIgnore:  perl(File::Which)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Provides:       tex(pax.jar)
Provides:       tex(pax.sty)
Requires:       java
Requires:       tex(auxhook.sty)
Requires:       tex(etexcmds.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(ltxcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source76:       pax.tar.xz
Source77:       pax.doc.tar.xz

%description -n texlive-pax
If PDF files are included using pdfTeX, PDF annotations are
stripped. The pax project offers a solution without altering
pdfTeX. A Java program (pax.jar) parses the PDF file that will
later be included. The program then writes the data of the
annotations into a file that can be read by TeX. The LaTeX
package pax extends the graphics package to support the scheme:
if a PDF file is included, the package looks for the file with
the annotation data, reads them and puts the annotations in the
right place. Project status: experimental

%package -n texlive-pax-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1lsvn54512
Release:        0
Summary:        Documentation for texlive-pax
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pax-doc
This package includes the documentation for texlive-pax

%post -n texlive-pax
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pax
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pax
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pax-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pax/README

%files -n texlive-pax
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pax/pax.jar
%{_texmfdistdir}/scripts/pax/pdfannotextractor.pl
%{_texmfdistdir}/tex/latex/pax/pax.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pax-%{texlive_version}.%{texlive_noarch}.0.0.1lsvn54512-%{release}-zypper
%endif

%package -n texlive-pb-diagram
Version:        %{texlive_version}.%{texlive_noarch}.5.0svn15878
Release:        0
License:        LPPL-1.0
Summary:        A commutative diagram package using LAMSTeX or Xy-pic fonts
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pb-diagram-doc >= %{texlive_version}
Provides:       tex(lamsarrow.sty)
Provides:       tex(pb-diagram.sty)
Provides:       tex(pb-lams.sty)
Provides:       tex(pb-xy.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source78:       pb-diagram.tar.xz
Source79:       pb-diagram.doc.tar.xz

%description -n texlive-pb-diagram
The pb-diagram package

%package -n texlive-pb-diagram-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.0svn15878
Release:        0
Summary:        Documentation for texlive-pb-diagram
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pb-diagram-doc
This package includes the documentation for texlive-pb-diagram

%post -n texlive-pb-diagram
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pb-diagram
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pb-diagram
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pb-diagram-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pb-diagram/COPYING
%{_texmfdistdir}/doc/latex/pb-diagram/README
%{_texmfdistdir}/doc/latex/pb-diagram/pb-examples.tex
%{_texmfdistdir}/doc/latex/pb-diagram/pb-manual.pdf
%{_texmfdistdir}/doc/latex/pb-diagram/pb-manual.tex

%files -n texlive-pb-diagram
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pb-diagram/lamsarrow.sty
%{_texmfdistdir}/tex/latex/pb-diagram/pb-diagram.sty
%{_texmfdistdir}/tex/latex/pb-diagram/pb-lams.sty
%{_texmfdistdir}/tex/latex/pb-diagram/pb-xy.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pb-diagram-%{texlive_version}.%{texlive_noarch}.5.0svn15878-%{release}-zypper
%endif

%package -n texlive-pbalance
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn57161
Release:        0
License:        LPPL-1.0
Summary:        Balance last page in two-column mode
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pbalance-doc >= %{texlive_version}
Provides:       tex(pbalance.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(balance.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(zref-abspage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source80:       pbalance.tar.xz
Source81:       pbalance.doc.tar.xz

%description -n texlive-pbalance
This package balances the columns on the last page of a
two-column document. If the page is "simple" (no footnotes,
floats, or marginpars), is uses the balance package; otherwise,
it uses \enlargethispage to make the left column shorter,
balancing the columns.

%package -n texlive-pbalance-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.1svn57161
Release:        0
Summary:        Documentation for texlive-pbalance
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pbalance-doc
This package includes the documentation for texlive-pbalance

%post -n texlive-pbalance
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pbalance
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pbalance
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pbalance-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pbalance/LICENSE
%{_texmfdistdir}/doc/latex/pbalance/README.md
%{_texmfdistdir}/doc/latex/pbalance/pbalance.pdf

%files -n texlive-pbalance
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pbalance/pbalance.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pbalance-%{texlive_version}.%{texlive_noarch}.1.0.1svn57161-%{release}-zypper
%endif

%package -n texlive-pbibtex-base
Version:        %{texlive_version}.%{texlive_noarch}.svn40986
Release:        0
License:        BSD-3-Clause
Summary:        Bibliography styles and miscellaneous files for pBibTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pbibtex-base-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source82:       pbibtex-base.tar.xz
Source83:       pbibtex-base.doc.tar.xz

%description -n texlive-pbibtex-base
These are miscellaneous files, including bibliography styles
(.bst), for pBibTeX, which is a Japanese extended version of
BibTeX contained in TeX Live. The bundle is a redistribution
derived from the ptex-texmf distribution by ASCII MEDIA WORKS.

%package -n texlive-pbibtex-base-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn40986
Release:        0
Summary:        Documentation for texlive-pbibtex-base
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pbibtex-base-doc
This package includes the documentation for texlive-pbibtex-base

%post -n texlive-pbibtex-base
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pbibtex-base
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pbibtex-base
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pbibtex-base-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/ptex/pbibtex/LICENSE
%{_texmfdistdir}/doc/ptex/pbibtex/README.md
%{_texmfdistdir}/doc/ptex/pbibtex/README_original
%{_texmfdistdir}/doc/ptex/pbibtex/cpp.awk
%{_texmfdistdir}/doc/ptex/pbibtex/generate.sh
%{_texmfdistdir}/doc/ptex/pbibtex/jbibtex.bib
%{_texmfdistdir}/doc/ptex/pbibtex/jbibtex.pdf
%{_texmfdistdir}/doc/ptex/pbibtex/jbibtex.tex
%{_texmfdistdir}/doc/ptex/pbibtex/jbtxbst.doc
%{_texmfdistdir}/doc/ptex/pbibtex/jbtxdoc.bib
%{_texmfdistdir}/doc/ptex/pbibtex/jbtxdoc.pdf
%{_texmfdistdir}/doc/ptex/pbibtex/jbtxdoc.tex
%{_texmfdistdir}/doc/ptex/pbibtex/jbtxhak.pdf
%{_texmfdistdir}/doc/ptex/pbibtex/jbtxhak.tex

%files -n texlive-pbibtex-base
%defattr(-,root,root,755)
%{_texmfdistdir}/pbibtex/bib/jxampl.bib
%{_texmfdistdir}/pbibtex/bst/jabbrv.bst
%{_texmfdistdir}/pbibtex/bst/jalpha.bst
%{_texmfdistdir}/pbibtex/bst/jipsj.bst
%{_texmfdistdir}/pbibtex/bst/jname.bst
%{_texmfdistdir}/pbibtex/bst/jorsj.bst
%{_texmfdistdir}/pbibtex/bst/jplain.bst
%{_texmfdistdir}/pbibtex/bst/junsrt.bst
%{_texmfdistdir}/pbibtex/bst/tieice.bst
%{_texmfdistdir}/pbibtex/bst/tipsj.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pbibtex-base-%{texlive_version}.%{texlive_noarch}.svn40986-%{release}-zypper
%endif

%package -n texlive-pbox
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn24807
Release:        0
License:        GPL-2.0-or-later
Summary:        A variable-width \parbox command
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pbox-doc >= %{texlive_version}
Provides:       tex(pbox.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source84:       pbox.tar.xz
Source85:       pbox.doc.tar.xz

%description -n texlive-pbox
Defines a command \pbox{<max width>}{<text>} which adjusts its
width to that of the enclosed text, up to the maximum width
given. The package also defines some associated length
commands.

%package -n texlive-pbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn24807
Release:        0
Summary:        Documentation for texlive-pbox
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pbox-doc
This package includes the documentation for texlive-pbox

%post -n texlive-pbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pbox/AUTHORS
%{_texmfdistdir}/doc/latex/pbox/COPYING
%{_texmfdistdir}/doc/latex/pbox/ChangeLog
%{_texmfdistdir}/doc/latex/pbox/INSTALL
%{_texmfdistdir}/doc/latex/pbox/Makefile
%{_texmfdistdir}/doc/latex/pbox/README
%{_texmfdistdir}/doc/latex/pbox/pbox.pdf

%files -n texlive-pbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pbox/pbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pbox-%{texlive_version}.%{texlive_noarch}.1.2svn24807-%{release}-zypper
%endif

%package -n texlive-pbsheet
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn24830
Release:        0
License:        LPPL-1.0
Summary:        Problem sheet class
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pbsheet-doc >= %{texlive_version}
Provides:       tex(pbsheet.cls)
Requires:       tex(aeguill.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(babel.sty)
Requires:       tex(color.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(listings.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(rotating.sty)
Requires:       tex(url.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source86:       pbsheet.tar.xz
Source87:       pbsheet.doc.tar.xz

%description -n texlive-pbsheet
This class is designed to simplify the typesetting of problem
sheets with Mathematics and Computer Science content. It is
currently customised towards teaching in French (and the
examples are in French).

%package -n texlive-pbsheet-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn24830
Release:        0
Summary:        Documentation for texlive-pbsheet
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pbsheet-doc:fr)

%description -n texlive-pbsheet-doc
This package includes the documentation for texlive-pbsheet

%post -n texlive-pbsheet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pbsheet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pbsheet
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pbsheet-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pbsheet/LPPL
%{_texmfdistdir}/doc/latex/pbsheet/README
%{_texmfdistdir}/doc/latex/pbsheet/pbsheet.pdf
%{_texmfdistdir}/doc/latex/pbsheet/xpl/GNUmakefile
%{_texmfdistdir}/doc/latex/pbsheet/xpl/img/simbin.eps
%{_texmfdistdir}/doc/latex/pbsheet/xpl/img/simbin.pdf
%{_texmfdistdir}/doc/latex/pbsheet/xpl/pbsheet.cls
%{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/probadis.m
%{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/rdiscr.m
%{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/rint.m
%{_texmfdistdir}/doc/latex/pbsheet/xpl/pgm/simbin.m
%{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.bib
%{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.dvi
%{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.pdf
%{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.ps
%{_texmfdistdir}/doc/latex/pbsheet/xpl/xpl-fr.tex

%files -n texlive-pbsheet
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pbsheet/pbsheet.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pbsheet-%{texlive_version}.%{texlive_noarch}.0.0.1svn24830-%{release}-zypper
%endif

%package -n texlive-pdf-trans
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn32809
Release:        0
License:        SUSE-Public-Domain
Summary:        A set of macros for various transformations of TeX boxes
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdf-trans-doc >= %{texlive_version}
Provides:       tex(pdf-trans.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source88:       pdf-trans.tar.xz
Source89:       pdf-trans.doc.tar.xz

%description -n texlive-pdf-trans
pdf-trans is a set of macros offering various transformations
of TeX boxes (based on plain and pdfeTeX primitives). It was
initially inspired by trans.tex, remade to work with pdfTeX.

%package -n texlive-pdf-trans-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn32809
Release:        0
Summary:        Documentation for texlive-pdf-trans
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdf-trans-doc
This package includes the documentation for texlive-pdf-trans

%post -n texlive-pdf-trans
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdf-trans
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdf-trans
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdf-trans-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pdf-trans/example.pdf
%{_texmfdistdir}/doc/generic/pdf-trans/example.tex

%files -n texlive-pdf-trans
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pdf-trans/pdf-trans.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdf-trans-%{texlive_version}.%{texlive_noarch}.2.4svn32809-%{release}-zypper
%endif

%package -n texlive-pdf14
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn17583
Release:        0
License:        LPPL-1.0
Summary:        Restore PDF 1.4 to a TeX live 2010 format
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdf14-doc >= %{texlive_version}
Provides:       tex(pdf14.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source90:       pdf14.tar.xz
Source91:       pdf14.doc.tar.xz

%description -n texlive-pdf14
Starting with TeX Live 2010, the various formats, that directly
generate PDF, default to generating PDF 1.5. This is generally
a good thing, but it can lead to compatibility issues with some
older PDF viewers. This package changes the version of PDF
generated with formats (based on pdfTeX or LuaTeX in PDF mode),
back to 1.4 for documents that need to achieve maximal
compatibility with old viewers.

%package -n texlive-pdf14-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn17583
Release:        0
Summary:        Documentation for texlive-pdf14
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdf14-doc
This package includes the documentation for texlive-pdf14

%post -n texlive-pdf14
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdf14
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdf14
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdf14-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdf14/README
%{_texmfdistdir}/doc/latex/pdf14/pdf14.pdf
%{_texmfdistdir}/doc/latex/pdf14/test-pdf14.tex

%files -n texlive-pdf14
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdf14/pdf14.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdf14-%{texlive_version}.%{texlive_noarch}.0.0.1svn17583-%{release}-zypper
%endif

%package -n texlive-pdfarticle
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn51127
Release:        0
License:        LPPL-1.0
Summary:        Class for pdf publications
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfarticle-doc >= %{texlive_version}
Provides:       tex(pdfArticle.cls)
Requires:       tex(adjustbox.sty)
Requires:       tex(alphalph.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(array.sty)
Requires:       tex(changepage.sty)
Requires:       tex(contour.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(extarticle.cls)
Requires:       tex(fancyvrb.sty)
Requires:       tex(fifo-stack.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(fvextra.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(minted.sty)
Requires:       tex(overpic.sty)
Requires:       tex(pbox.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(setspace.sty)
Requires:       tex(shadowtext.sty)
Requires:       tex(tabto.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(ulem.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(wrapfig.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source92:       pdfarticle.tar.xz
Source93:       pdfarticle.doc.tar.xz

%description -n texlive-pdfarticle
pdfArticle is simple document class dedicated for creating pdf
documents with LuaLaTeX.

%package -n texlive-pdfarticle-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn51127
Release:        0
Summary:        Documentation for texlive-pdfarticle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfarticle-doc
This package includes the documentation for texlive-pdfarticle

%post -n texlive-pdfarticle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfarticle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfarticle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfarticle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/pdfarticle/README
%{_texmfdistdir}/doc/lualatex/pdfarticle/pdfArticle.pdf
%{_texmfdistdir}/doc/lualatex/pdfarticle/pdfArticle.tex

%files -n texlive-pdfarticle
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/pdfarticle/pdfArticle.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfarticle-%{texlive_version}.%{texlive_noarch}.1.0svn51127-%{release}-zypper
%endif

%package -n texlive-pdfbook2
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn53521
Release:        0
License:        GPL-2.0-or-later
Summary:        Create booklets from PDF files
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfbook2-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdfbook2-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfbook2-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source94:       pdfbook2.tar.xz
Source95:       pdfbook2.doc.tar.xz

%description -n texlive-pdfbook2
This python program creates print-ready PDF files from some
input PDF files for booklet printing. The resulting files need
to be printed in landscape/long edge double sided printing. The
default paper format depends on the locale and is chosen by
pdfjam. It can be chosen using the --paper option. Before the
pdf is composed, the input file is cropped to the relevant area
in order to discard unnecessary white spaces. In this process,
all pages are cropped to the same dimensions. Extra margins can
be defined at the edges of the booklet and in the middle where
the binding occurs. The output is written to INPUT-book.pdf.
Existing files will be overwritten. All input files are
processed seperately.

%package -n texlive-pdfbook2-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn53521
Release:        0
Summary:        Documentation for texlive-pdfbook2
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(pdfbook2.1)

%description -n texlive-pdfbook2-doc
This package includes the documentation for texlive-pdfbook2

%post -n texlive-pdfbook2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfbook2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfbook2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfbook2-doc
%defattr(-,root,root,755)
%{_mandir}/man1/pdfbook2.1*
%{_texmfdistdir}/doc/support/pdfbook2/README

%files -n texlive-pdfbook2
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pdfbook2/pdfbook2
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfbook2-%{texlive_version}.%{texlive_noarch}.1.4svn53521-%{release}-zypper
%endif

%package -n texlive-pdfcolmk
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn52912
Release:        0
License:        LPPL-1.0
Summary:        Improved colour support under pdfTeX (legacy stub)
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfcolmk-doc >= %{texlive_version}
Provides:       tex(pdfcolmk.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source96:       pdfcolmk.tar.xz
Source97:       pdfcolmk.doc.tar.xz

%description -n texlive-pdfcolmk
The package used to provide macros that emulated the 'colour
stack' functionality of dvips. The colour stack deals with
colour manipulations when asynchronous events (like
page-breaking) occur. At the time the package was written,
pdfTeX did not (yet) have such a stack, though dvips had had
one for a long time. This package was an experimental solution
to the problem, and worked best with pdfeTeX. For current
releases of pdfTeX (later than version 1.40.0, released in
2007), this package is not needed, since "real" colour stacks
are available. The present pdfcolmk is therefore just an empty
stub that does nothing at all, just in case there are still
documents that reference it. The documented source of the
original package is still available at the github repository.

%package -n texlive-pdfcolmk-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn52912
Release:        0
Summary:        Documentation for texlive-pdfcolmk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfcolmk-doc
This package includes the documentation for texlive-pdfcolmk

%post -n texlive-pdfcolmk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfcolmk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfcolmk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfcolmk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfcolmk/README.md

%files -n texlive-pdfcolmk
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfcolmk/pdfcolmk.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfcolmk-%{texlive_version}.%{texlive_noarch}.2.0svn52912-%{release}-zypper
%endif

%package -n texlive-pdfcomment
Version:        %{texlive_version}.%{texlive_noarch}.2.4asvn49047
Release:        0
License:        LPPL-1.0
Summary:        A user-friendly interface to pdf annotations
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfcomment-doc >= %{texlive_version}
Provides:       tex(pdfcomment.sty)
Requires:       tex(calc.sty)
Requires:       tex(datetime2.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(luatex85.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(refcount.sty)
Requires:       tex(soulpos.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(zref-savepos.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source98:       pdfcomment.tar.xz
Source99:       pdfcomment.doc.tar.xz

%description -n texlive-pdfcomment
For a long time pdfLaTeX has offered the command \pdfannot for
inserting arbitrary PDF annotations. However, the command is
presented in a form where additional knowledge of the
definition of the PDF format is indispensable. This package is
an answer to the - occasional - questions in newsgroups, about
how one could use the comment function of Adobe Reader. At
least for the writer of LaTeX code, the package offers a
convenient and user-friendly means of using \pdfannot to
provide comments in PDF files. Since version v1.1,
pdfcomment.sty also supports LaTeX - dvips - ps2pdf, LaTeX -
dvipdfmx, XeLaTeX and LuaLaTeX. Unfortunately, support of PDF
annotations by PDF viewers may vary. The reference viewer for
the development of this package is Adobe Reader.

%package -n texlive-pdfcomment-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4asvn49047
Release:        0
Summary:        Documentation for texlive-pdfcomment
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pdfcomment-doc:en;de)

%description -n texlive-pdfcomment-doc
This package includes the documentation for texlive-pdfcomment

%post -n texlive-pdfcomment
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfcomment
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfcomment
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfcomment-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfcomment/CHANGES
%{_texmfdistdir}/doc/latex/pdfcomment/INSTALL
%{_texmfdistdir}/doc/latex/pdfcomment/README.md
%{_texmfdistdir}/doc/latex/pdfcomment/example.pdf
%{_texmfdistdir}/doc/latex/pdfcomment/example.tex
%{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvipdfmx.pdf
%{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvipdfmx.tex
%{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvips_ps2pdf.pdf
%{_texmfdistdir}/doc/latex/pdfcomment/example_latex_dvips_ps2pdf.tex
%{_texmfdistdir}/doc/latex/pdfcomment/example_math_markup.pdf
%{_texmfdistdir}/doc/latex/pdfcomment/example_math_markup.tex
%{_texmfdistdir}/doc/latex/pdfcomment/example_xelatex.pdf
%{_texmfdistdir}/doc/latex/pdfcomment/example_xelatex.tex
%{_texmfdistdir}/doc/latex/pdfcomment/manifest.txt
%{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment.pdf
%{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment.tex
%{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment_de.pdf
%{_texmfdistdir}/doc/latex/pdfcomment/pdfcomment_de.tex

%files -n texlive-pdfcomment
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfcomment/pdfcomment.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfcomment-%{texlive_version}.%{texlive_noarch}.2.4asvn49047-%{release}-zypper
%endif

%package -n texlive-pdfcprot
Version:        %{texlive_version}.%{texlive_noarch}.1.7asvn18735
Release:        0
License:        LPPL-1.0
Summary:        Activating and setting of character protruding using pdfLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfcprot-doc >= %{texlive_version}
Provides:       tex(pdfcprot.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(textcomp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source100:      pdfcprot.tar.xz
Source101:      pdfcprot.doc.tar.xz

%description -n texlive-pdfcprot
This package provides an easy interface to adjust the character
protrusion for different fonts and choosing the right
adjustment automatically depending on the font. The package is
largely superseded by microtype.

%package -n texlive-pdfcprot-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7asvn18735
Release:        0
Summary:        Documentation for texlive-pdfcprot
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfcprot-doc
This package includes the documentation for texlive-pdfcprot

%post -n texlive-pdfcprot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfcprot
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfcprot
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfcprot-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfcprot/00CONTEN
%{_texmfdistdir}/doc/latex/pdfcprot/00README
%{_texmfdistdir}/doc/latex/pdfcprot/INSTALL.txt
%{_texmfdistdir}/doc/latex/pdfcprot/LEGAL.txt
%{_texmfdistdir}/doc/latex/pdfcprot/Makefile.unx
%{_texmfdistdir}/doc/latex/pdfcprot/README.txt
%{_texmfdistdir}/doc/latex/pdfcprot/TODO
%{_texmfdistdir}/doc/latex/pdfcprot/pdfcprot.pdf

%files -n texlive-pdfcprot
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfcprot/pdfcprot.sty
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnOT1.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnOT2.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnT1.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnT2A.cpa
%{_texmfdistdir}/tex/latex/pdfcprot/pplmnTS1.cpa
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfcprot-%{texlive_version}.%{texlive_noarch}.1.7asvn18735-%{release}-zypper
%endif

%package -n texlive-pdfcrop
Version:        %{texlive_version}.%{texlive_noarch}.1.40svn55435
Release:        0
License:        LPPL-1.0
Summary:        Crop PDF graphics
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfcrop-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdfcrop-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfcrop-doc >= %{texlive_version}
Requires:       perl(Config)
#!BuildIgnore:  perl(Config)
Requires:       perl(File::Copy)
#!BuildIgnore:  perl(File::Copy)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(File::Spec::Functions)
#!BuildIgnore:  perl(File::Spec::Functions)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source102:      pdfcrop.tar.xz
Source103:      pdfcrop.doc.tar.xz

%description -n texlive-pdfcrop
A Perl script that can either trim pages of any whitespace
border, or trim them of a fixed border.

%package -n texlive-pdfcrop-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.40svn55435
Release:        0
Summary:        Documentation for texlive-pdfcrop
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfcrop-doc
This package includes the documentation for texlive-pdfcrop

%post -n texlive-pdfcrop
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfcrop
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfcrop
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfcrop-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/pdfcrop/LICENCE
%{_texmfdistdir}/doc/support/pdfcrop/README.md

%files -n texlive-pdfcrop
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pdfcrop/pdfcrop.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfcrop-%{texlive_version}.%{texlive_noarch}.1.40svn55435-%{release}-zypper
%endif

%package -n texlive-pdfescape
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn53082
Release:        0
License:        LPPL-1.0
Summary:        Implements pdfTeX's escape features using TeX or e-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfescape-doc >= %{texlive_version}
Provides:       tex(pdfescape.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source104:      pdfescape.tar.xz
Source105:      pdfescape.doc.tar.xz

%description -n texlive-pdfescape
This package implements pdfTeX's escape features
(\pdfescapehex, \pdfunescapehex, \pdfescapename,
\pdfescapestring) using TeX or e-TeX.

%package -n texlive-pdfescape-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn53082
Release:        0
Summary:        Documentation for texlive-pdfescape
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfescape-doc
This package includes the documentation for texlive-pdfescape

%post -n texlive-pdfescape
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfescape
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfescape
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfescape-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfescape/README.md
%{_texmfdistdir}/doc/latex/pdfescape/pdfescape.pdf

%files -n texlive-pdfescape
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pdfescape/pdfescape.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfescape-%{texlive_version}.%{texlive_noarch}.1.15svn53082-%{release}-zypper
%endif

%package -n texlive-pdfjam
Version:        %{texlive_version}.%{texlive_noarch}.3.03svn56991
Release:        0
License:        GPL-2.0-or-later
Summary:        Shell scripts interfacing to pdfpages
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfjam-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdfjam-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfjam-doc >= %{texlive_version}
Requires:       texlive-pdfpages >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source106:      pdfjam.tar.xz
Source107:      pdfjam.doc.tar.xz

%description -n texlive-pdfjam
The package makes available the pdfjam shell script that
provides a simple interface to much of the functionality of the
excellent pdfpages package (by Andreas Matthias) for LaTeX. The
pdfjam script takes one or more PDF files (and/or JPG/PNG
graphics files) as input, and produces one or more PDF files as
output. It is useful for joining files together, selecting
pages, reducing several source pages onto one output page,
etc., etc.

%package -n texlive-pdfjam-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.03svn56991
Release:        0
Summary:        Documentation for texlive-pdfjam
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(pdfjam.1)

%description -n texlive-pdfjam-doc
This package includes the documentation for texlive-pdfjam

%post -n texlive-pdfjam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfjam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfjam
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfjam-doc
%defattr(-,root,root,755)
%{_mandir}/man1/pdfjam.1*
%{_texmfdistdir}/doc/support/pdfjam/COPYING
%{_texmfdistdir}/doc/support/pdfjam/README.md
%{_texmfdistdir}/doc/support/pdfjam/VERSION
%{_texmfdistdir}/doc/support/pdfjam/pdfjam.conf
%{_texmfdistdir}/doc/support/pdfjam/tests.zip

%files -n texlive-pdfjam
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pdfjam/pdfjam
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfjam-%{texlive_version}.%{texlive_noarch}.3.03svn56991-%{release}-zypper
%endif

%package -n texlive-pdflatexpicscale
Version:        %{texlive_version}.%{texlive_noarch}.0.0.32svn46617
Release:        0
License:        LPPL-1.0
Summary:        Support software for downscaling graphics to be included by pdfLaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdflatexpicscale-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdflatexpicscale-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdflatexpicscale-doc >= %{texlive_version}
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Copy)
#!BuildIgnore:  perl(File::Copy)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source108:      pdflatexpicscale.tar.xz
Source109:      pdflatexpicscale.doc.tar.xz

%description -n texlive-pdflatexpicscale
The package provides a script to scale pictures down to a
target resolution before creating a PDF document with pdfLaTeX.

%package -n texlive-pdflatexpicscale-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.32svn46617
Release:        0
Summary:        Documentation for texlive-pdflatexpicscale
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdflatexpicscale-doc
This package includes the documentation for texlive-pdflatexpicscale

%post -n texlive-pdflatexpicscale
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdflatexpicscale
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdflatexpicscale
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdflatexpicscale-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/pdflatexpicscale/README
%{_texmfdistdir}/doc/support/pdflatexpicscale/pdflatexpicscale.pdf
%{_texmfdistdir}/doc/support/pdflatexpicscale/pdflatexpicscale.tex
%{_texmfdistdir}/doc/support/pdflatexpicscale/testprinter.ps

%files -n texlive-pdflatexpicscale
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pdflatexpicscale/pdflatexpicscale.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdflatexpicscale-%{texlive_version}.%{texlive_noarch}.0.0.32svn46617-%{release}-zypper
%endif

%package -n texlive-pdflscape
Version:        %{texlive_version}.%{texlive_noarch}.0.0.12svn53047
Release:        0
License:        LPPL-1.0
Summary:        Make landscape pages display as landscape
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdflscape-doc >= %{texlive_version}
Provides:       tex(pdflscape.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(iftex.sty)
Requires:       tex(lscape.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source110:      pdflscape.tar.xz
Source111:      pdflscape.doc.tar.xz

%description -n texlive-pdflscape
The package adds PDF support to the landscape environment of
package lscape, by setting the PDF /Rotate page attribute.
Pages with this attribute will be displayed in landscape
orientation by conforming PDF viewers.

%package -n texlive-pdflscape-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.12svn53047
Release:        0
Summary:        Documentation for texlive-pdflscape
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdflscape-doc
This package includes the documentation for texlive-pdflscape

%post -n texlive-pdflscape
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdflscape
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdflscape
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdflscape-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdflscape/README.md
%{_texmfdistdir}/doc/latex/pdflscape/pdflscape.pdf

%files -n texlive-pdflscape
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdflscape/pdflscape.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdflscape-%{texlive_version}.%{texlive_noarch}.0.0.12svn53047-%{release}-zypper
%endif

%package -n texlive-pdfmanagement-testphase
Version:        %{texlive_version}.%{texlive_noarch}.0.0.95csvn58511
Release:        0
License:        LPPL-1.0
Summary:        LaTeX PDF management testphase bundle
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfmanagement-testphase-doc >= %{texlive_version}
Provides:       tex(color-ltx.sty)
Provides:       tex(hgeneric-testphase.def)
Provides:       tex(hyperref-colorschemes.def)
Provides:       tex(hyperxmp-patches-tmp-ltx.sty)
Provides:       tex(l3backend-testphase-dvipdfmx.def)
Provides:       tex(l3backend-testphase-dvips.def)
Provides:       tex(l3backend-testphase-dvisvgm.def)
Provides:       tex(l3backend-testphase-luatex.def)
Provides:       tex(l3backend-testphase-pdftex.def)
Provides:       tex(l3backend-testphase-xetex.def)
Provides:       tex(l3pdffield-testphase.sty)
Provides:       tex(l3ref-tmp.sty)
Provides:       tex(pdflscape-ltx.sty)
Provides:       tex(pdfmanagement-firstaid.sty)
Provides:       tex(pdfmanagement-testphase.sty)
Provides:       tex(transparent-ltx.sty)
Provides:       tex(xcolor-patches-tmp-ltx.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(lscape.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source112:      pdfmanagement-testphase.tar.xz
Source113:      pdfmanagement-testphase.doc.tar.xz

%description -n texlive-pdfmanagement-testphase
This is a temporary package, which is used during a test phase
to load the new PDF management code of LaTeX. The new PDF
management code offers backend independent interfaces to
central PDF dictionaries, tools to create annotations, form
Xobjects, to embed files, and to handle PDF standards. The code
is provided during a testphase as independent package to allow
users and package authors to safely test the code. At a later
stage it will be integrated into the LaTeX kernel (or in parts
into permanent support packages), and the current testphase
bundle will be removed.

%package -n texlive-pdfmanagement-testphase-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.95csvn58511
Release:        0
Summary:        Documentation for texlive-pdfmanagement-testphase
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfmanagement-testphase-doc
This package includes the documentation for texlive-pdfmanagement-testphase

%post -n texlive-pdfmanagement-testphase
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfmanagement-testphase
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfmanagement-testphase
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfmanagement-testphase-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/CHANGELOG.md
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/README.md
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/hyperref-generic.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3backend-testphase.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdfannot.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdfdict.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdffield.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdffile.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdfmanagement.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdfmeta.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdftools.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/l3pdfxform.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/ltdocinit.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/pdfmanagement-firstaid.pdf
%{_texmfdistdir}/doc/latex/pdfmanagement-testphase/pdfmanagement-testphase.pdf

%files -n texlive-pdfmanagement-testphase
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/color-ltx.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/hgeneric-testphase.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/hyperref-colorschemes.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/hyperxmp-patches-tmp-ltx.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3backend-testphase-dvipdfmx.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3backend-testphase-dvips.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3backend-testphase-dvisvgm.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3backend-testphase-luatex.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3backend-testphase-pdftex.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3backend-testphase-xetex.def
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3backend-testphase.lua
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3pdffield-testphase.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/l3ref-tmp.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/pdflscape-ltx.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/pdfmanagement-firstaid.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/pdfmanagement-testphase.ltx
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/pdfmanagement-testphase.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/transparent-ltx.sty
%{_texmfdistdir}/tex/latex/pdfmanagement-testphase/xcolor-patches-tmp-ltx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfmanagement-testphase-%{texlive_version}.%{texlive_noarch}.0.0.95csvn58511-%{release}-zypper
%endif

%package -n texlive-pdfmarginpar
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn23492
Release:        0
License:        GPL-2.0-or-later
Summary:        Generate marginpar-equivalent PDF annotations
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfmarginpar-doc >= %{texlive_version}
Provides:       tex(pdfmarginpar.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source114:      pdfmarginpar.tar.xz
Source115:      pdfmarginpar.doc.tar.xz

%description -n texlive-pdfmarginpar
The package provides the \pdfmarginpar command which is similar
in spirit to \marginpar. However, it creates PDF annotations
which may be viewed with Adobe Reader in place of marginal
texts. Small icons indicate the in-text position where the
message originates, popups provide the messages themselves.
Thus bugfixes and other such communications are clearly visible
together when viewing the document, while the document itself
is not obscured.

%package -n texlive-pdfmarginpar-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn23492
Release:        0
Summary:        Documentation for texlive-pdfmarginpar
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfmarginpar-doc
This package includes the documentation for texlive-pdfmarginpar

%post -n texlive-pdfmarginpar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfmarginpar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfmarginpar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfmarginpar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfmarginpar/README
%{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginpar.pdf
%{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginpar.tex
%{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginparexample.pdf
%{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginparexample.png
%{_texmfdistdir}/doc/latex/pdfmarginpar/pdfmarginparexample.tex
%{_texmfdistdir}/doc/latex/pdfmarginpar/pgfmanual-en-macros.tex
%{_texmfdistdir}/doc/latex/pdfmarginpar/pgfplots-macros.tex

%files -n texlive-pdfmarginpar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfmarginpar/pdfmarginpar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfmarginpar-%{texlive_version}.%{texlive_noarch}.0.0.92svn23492-%{release}-zypper
%endif

%package -n texlive-pdfoverlay
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn57923
Release:        0
License:        LPPL-1.0
Summary:        A LaTeX style for overlaying text on a PDF
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfoverlay-doc >= %{texlive_version}
Provides:       tex(pdfoverlay.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source116:      pdfoverlay.tar.xz
Source117:      pdfoverlay.doc.tar.xz

%description -n texlive-pdfoverlay
It is often desirable to take an exisiting PDF and easily add
annotations or text overlaying the PDF. This might arise if you
wish to add comments to a PDF, fill in a PDF form, or add text
to a PDF where space has been left for notes. This package
provides a simple interface to do this without having to resort
to inserting one page at a time. Some or all of the pages of
the PDF can be included and not all pages of the PDF need have
overlayed text. It is also possible to include text between
pages of the PDF. Another advantage of this package is that the
overlayed text can be set as normal flowing from one page to
another or with manual page breaks if you wish. It is also
possible to use any standard method to position text at
arbitrary places on a given page.

%package -n texlive-pdfoverlay-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn57923
Release:        0
Summary:        Documentation for texlive-pdfoverlay
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfoverlay-doc
This package includes the documentation for texlive-pdfoverlay

%post -n texlive-pdfoverlay
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfoverlay
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfoverlay
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfoverlay-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfoverlay/README.md
%{_texmfdistdir}/doc/latex/pdfoverlay/pdfoverlay.pdf

%files -n texlive-pdfoverlay
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfoverlay/pdfoverlay.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfoverlay-%{texlive_version}.%{texlive_noarch}.1.2asvn57923-%{release}-zypper
%endif

%package -n texlive-pdfpagediff
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn37946
Release:        0
License:        LPPL-1.0
Summary:        Find difference between two PDF's
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfpagediff-doc >= %{texlive_version}
Provides:       tex(pdfpagediff.sty)
Requires:       tex(color.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(substr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source118:      pdfpagediff.tar.xz
Source119:      pdfpagediff.doc.tar.xz

%description -n texlive-pdfpagediff
Find difference between two PDF's

%package -n texlive-pdfpagediff-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn37946
Release:        0
Summary:        Documentation for texlive-pdfpagediff
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfpagediff-doc
This package includes the documentation for texlive-pdfpagediff

%post -n texlive-pdfpagediff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfpagediff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfpagediff
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfpagediff-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfpagediff/README
%{_texmfdistdir}/doc/latex/pdfpagediff/doc/Makefile
%{_texmfdistdir}/doc/latex/pdfpagediff/doc/ar1.png
%{_texmfdistdir}/doc/latex/pdfpagediff/doc/ar2.png
%{_texmfdistdir}/doc/latex/pdfpagediff/doc/ar3.png
%{_texmfdistdir}/doc/latex/pdfpagediff/doc/pdfpagediff-doc.pdf
%{_texmfdistdir}/doc/latex/pdfpagediff/doc/pdfpagediff-doc.sty
%{_texmfdistdir}/doc/latex/pdfpagediff/doc/pdfpagediff-doc.tex
%{_texmfdistdir}/doc/latex/pdfpagediff/example/file1.pdf
%{_texmfdistdir}/doc/latex/pdfpagediff/example/file2.pdf
%{_texmfdistdir}/doc/latex/pdfpagediff/example/ltest.pdf
%{_texmfdistdir}/doc/latex/pdfpagediff/example/ltest.tex
%{_texmfdistdir}/doc/latex/pdfpagediff/manifest.txt

%files -n texlive-pdfpagediff
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfpagediff/pdfpagediff.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfpagediff-%{texlive_version}.%{texlive_noarch}.1.4svn37946-%{release}-zypper
%endif

%package -n texlive-pdfpages
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5tsvn58212
Release:        0
License:        LPPL-1.0
Summary:        Include PDF documents in LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-eso-pic >= %{texlive_version}
#!BuildIgnore: texlive-eso-pic
Requires:       texlive-graphics >= %{texlive_version}
#!BuildIgnore: texlive-graphics
Requires:       texlive-oberdiek >= %{texlive_version}
#!BuildIgnore: texlive-oberdiek
Requires:       texlive-tools >= %{texlive_version}
#!BuildIgnore: texlive-tools
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfpages-doc >= %{texlive_version}
Provides:       tex(pdfpages.sty)
Provides:       tex(ppdvipdfmx.def)
Provides:       tex(ppdvips.def)
Provides:       tex(ppluatex.def)
Provides:       tex(ppnull.def)
Provides:       tex(pppdftex.def)
Provides:       tex(ppvtex.def)
Provides:       tex(ppxetex.def)
Requires:       tex(calc.sty)
Requires:       tex(count1to.sty)
Requires:       tex(dvipdfmx.def)
Requires:       tex(eso-pic.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pdflscape.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source120:      pdfpages.tar.xz
Source121:      pdfpages.doc.tar.xz

%description -n texlive-pdfpages
This package simplifies the inclusion of external multi-page
PDF documents in LaTeX documents. Pages may be freely selected
and similar to psnup it is possible to put several logical
pages onto each sheet of paper. Furthermore a lot of hypertext
features like hyperlinks and article threads are provided. The
package supports pdfTeX (pdfLaTeX) and VTeX. With VTeX it is
even possible to use this package to insert PostScript files,
in addition to PDF files.

%package -n texlive-pdfpages-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5tsvn58212
Release:        0
Summary:        Documentation for texlive-pdfpages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfpages-doc
This package includes the documentation for texlive-pdfpages

%post -n texlive-pdfpages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfpages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfpages
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfpages-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfpages/dummy-l.pdf
%{_texmfdistdir}/doc/latex/pdfpages/dummy.pdf
%{_texmfdistdir}/doc/latex/pdfpages/pdf-ex.tex
%{_texmfdistdir}/doc/latex/pdfpages/pdf-hyp.tex
%{_texmfdistdir}/doc/latex/pdfpages/pdf-toc.tex
%{_texmfdistdir}/doc/latex/pdfpages/pdfpages.pdf

%files -n texlive-pdfpages
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfpages/pdfpages.sty
%{_texmfdistdir}/tex/latex/pdfpages/ppdvipdfmx.def
%{_texmfdistdir}/tex/latex/pdfpages/ppdvips.def
%{_texmfdistdir}/tex/latex/pdfpages/ppluatex.def
%{_texmfdistdir}/tex/latex/pdfpages/ppnull.def
%{_texmfdistdir}/tex/latex/pdfpages/pppdftex.def
%{_texmfdistdir}/tex/latex/pdfpages/ppvtex.def
%{_texmfdistdir}/tex/latex/pdfpages/ppxetex.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfpages-%{texlive_version}.%{texlive_noarch}.0.0.5tsvn58212-%{release}-zypper
%endif

%package -n texlive-pdfpc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6.0svn57735
Release:        0
License:        GPL-2.0-or-later
Summary:        Define data for the pdfpc presentation viewer
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfpc-doc >= %{texlive_version}
Provides:       tex(pdfpc.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(iftex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source122:      pdfpc.tar.xz
Source123:      pdfpc.doc.tar.xz

%description -n texlive-pdfpc
This packages allows to define additional meta data within the
PDF file which can be interpreted by the PDF presenter console
(pdfpc) program. pdfpc depends on kvoptions, xstring, iftex,
and hyperxmp.

%package -n texlive-pdfpc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6.0svn57735
Release:        0
Summary:        Documentation for texlive-pdfpc
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfpc-doc
This package includes the documentation for texlive-pdfpc

%post -n texlive-pdfpc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfpc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfpc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfpc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfpc/README.md
%{_texmfdistdir}/doc/latex/pdfpc/pdfpc-doc.pdf
%{_texmfdistdir}/doc/latex/pdfpc/pdfpc-doc.tex

%files -n texlive-pdfpc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfpc/pdfpc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfpc-%{texlive_version}.%{texlive_noarch}.0.0.6.0svn57735-%{release}-zypper
%endif

%package -n texlive-pdfpc-movie
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn48245
Release:        0
License:        LPPL-1.0
Summary:        Pdfpc viewer-compatible hyperlinks to movies
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfpc-movie-doc >= %{texlive_version}
Provides:       tex(pdfpc-movie.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source124:      pdfpc-movie.tar.xz
Source125:      pdfpc-movie.doc.tar.xz

%description -n texlive-pdfpc-movie
This LaTeX2e package provides a command \pdfpcmovie for
embedding (hyperlinking) movies in a way compatible with the
PDF Presenter Console (pdfpc), a GPL2-licensed multi-monitor
PDF presentation viewer application available on GitHub and
shipped with some LINUX distributions such as Debian, Fedora,
and Arch. The package depends on etoolbox, hyperref, and
pgfkeys.

%package -n texlive-pdfpc-movie-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn48245
Release:        0
Summary:        Documentation for texlive-pdfpc-movie
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfpc-movie-doc
This package includes the documentation for texlive-pdfpc-movie

%post -n texlive-pdfpc-movie
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfpc-movie
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfpc-movie
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfpc-movie-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfpc-movie/README.md
%{_texmfdistdir}/doc/latex/pdfpc-movie/pdfpc-movie-doc.pdf

%files -n texlive-pdfpc-movie
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfpc-movie/pdfpc-movie.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfpc-movie-%{texlive_version}.%{texlive_noarch}.1.0svn48245-%{release}-zypper
%endif

%package -n texlive-pdfprivacy
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn45985
Release:        0
License:        LPPL-1.0
Summary:        A LaTeX package to remove or suppress pdf meta-data
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfprivacy-doc >= %{texlive_version}
Provides:       tex(pdfprivacy.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source126:      pdfprivacy.tar.xz
Source127:      pdfprivacy.doc.tar.xz

%description -n texlive-pdfprivacy
Creating pdfs with pdfLaTeX populates several pdf meta-data
fields such as date/time of creation/modification, information
about the LaTeX installation (e.g., pdfTeX version), and the
relative paths of included pdfs. The pdfprivacy package
provides support for emptying several of these pdf meta-data
fields as well as suppressing some pdfTeX meta-data entries in
the resulting pdf.

%package -n texlive-pdfprivacy-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn45985
Release:        0
Summary:        Documentation for texlive-pdfprivacy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfprivacy-doc
This package includes the documentation for texlive-pdfprivacy

%post -n texlive-pdfprivacy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfprivacy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfprivacy
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfprivacy-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfprivacy/LICENSE
%{_texmfdistdir}/doc/latex/pdfprivacy/README.md
%{_texmfdistdir}/doc/latex/pdfprivacy/pdfprivacy.pdf

%files -n texlive-pdfprivacy
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfprivacy/pdfprivacy.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfprivacy-%{texlive_version}.%{texlive_noarch}.1.0svn45985-%{release}-zypper
%endif

%package -n texlive-pdfreview
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn50100
Release:        0
License:        LPPL-1.0
Summary:        Annotate PDF files with margin notes
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfreview-doc >= %{texlive_version}
Provides:       tex(pdfreview.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(geometry.sty)
Requires:       tex(grffile.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ulem.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source128:      pdfreview.tar.xz
Source129:      pdfreview.doc.tar.xz

%description -n texlive-pdfreview
This package lets you add comments in the page margins of PDF
files, e.g. when reviewing manuscripts or grading reports. The
PDF file to be annotated is included, one page at a time, as
graphics, in a manner similar to the pdfpages package. Notes
are placed in the margin next to the included graphics using a
grid of help lines. Alternatively, only numbers are placed in
the page margins, and the notes are collected into a numbered
list at the end of the document. Note that this package is not
intended for adding notes directly to the LaTeX source of the
document that is being reviewed; instead, the document
undergoing review is already in PDF format and remains
unchanged. Also note that this package does not produce the
usual PDF "sticky notes" that must be opened by clicking on
them; instead, the notes are simply shown as text. This package
depends on the following other LaTeX package: adjustbox, calc,
geometry, graphicx, grffile, ifthen, kvoptions, tikz, ulem, and
xstring.

%package -n texlive-pdfreview-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn50100
Release:        0
Summary:        Documentation for texlive-pdfreview
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfreview-doc
This package includes the documentation for texlive-pdfreview

%post -n texlive-pdfreview
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfreview
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfreview
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfreview-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfreview/README.md
%{_texmfdistdir}/doc/latex/pdfreview/lorem-ipsum.pdf
%{_texmfdistdir}/doc/latex/pdfreview/pdfreview.pdf
%{_texmfdistdir}/doc/latex/pdfreview/pdfreview.sh
%{_texmfdistdir}/doc/latex/pdfreview/pdfreview.tex
%{_texmfdistdir}/doc/latex/pdfreview/pdfshrink.sh
%{_texmfdistdir}/doc/latex/pdfreview/sample.pdf
%{_texmfdistdir}/doc/latex/pdfreview/sample.tex

%files -n texlive-pdfreview
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfreview/pdfreview.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfreview-%{texlive_version}.%{texlive_noarch}.1.2svn50100-%{release}-zypper
%endif

%package -n texlive-pdfscreen
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn42428
Release:        0
License:        LPPL-1.0
Summary:        Support screen-based document design
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfscreen-doc >= %{texlive_version}
Provides:       tex(pdfscreen.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(comment.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(shortvrb.sty)
Requires:       tex(truncate.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source130:      pdfscreen.tar.xz
Source131:      pdfscreen.doc.tar.xz

%description -n texlive-pdfscreen
An extension of the hyperref package to provide a screen-based
document design. This package helps to generate pdf documents
that are readable on screen and will fit the screen's aspect
ratio. Also it can be used with various options to produce
regular print versions of the same document without any extra
effort.

%package -n texlive-pdfscreen-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn42428
Release:        0
Summary:        Documentation for texlive-pdfscreen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfscreen-doc
This package includes the documentation for texlive-pdfscreen

%post -n texlive-pdfscreen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfscreen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfscreen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfscreen-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfscreen/logo.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/manual-print.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/manual-screen.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/manual.tex
%{_texmfdistdir}/doc/latex/pdfscreen/nopanel.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/pdfscreen.cfg.specimen
%{_texmfdistdir}/doc/latex/pdfscreen/portrait.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/print.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/slide.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/slide.tex
%{_texmfdistdir}/doc/latex/pdfscreen/square.pdf
%{_texmfdistdir}/doc/latex/pdfscreen/tex.png
%{_texmfdistdir}/doc/latex/pdfscreen/widepanel.pdf

%files -n texlive-pdfscreen
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfscreen/but.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/button.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/left.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay0.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay1.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay10.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay2.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay3.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay4.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay5.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay6.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay7.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay8.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay9.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/pdfscreen.sty
%{_texmfdistdir}/tex/latex/pdfscreen/right.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfscreen-%{texlive_version}.%{texlive_noarch}.1.5svn42428-%{release}-zypper
%endif

%package -n texlive-pdfslide
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Presentation slides using pdfTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfslide-doc >= %{texlive_version}
Provides:       tex(pdfslide.cfg)
Provides:       tex(pdfslide.sty)
Provides:       tex(slide.clo)
Requires:       tex(amsbsy.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source132:      pdfslide.tar.xz
Source133:      pdfslide.doc.tar.xz

%description -n texlive-pdfslide
This is a package for use with pdfTeX, to make nice
presentation slides. Its aims are: to devise a method for
easier technical presentation; to help the mix of mathematical
formulae with text and graphics which other present day
document processing tools fail to accomplish; to exploit the
platform independence of TeX so that presentation documents
become portable; and to offer the freedom and possibilities of
using various backgrounds and other embellishments that a user
can imagine to have in as presentation. The package can make
use of the facilities of the PPower4 post-processor.

%package -n texlive-pdfslide-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-pdfslide
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfslide-doc
This package includes the documentation for texlive-pdfslide

%post -n texlive-pdfslide
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfslide
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfslide
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfslide-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfslide/demo.pdf
%{_texmfdistdir}/doc/latex/pdfslide/manual.tex
%{_texmfdistdir}/doc/latex/pdfslide/meta.mp
%{_texmfdistdir}/doc/latex/pdfslide/mpgraph.pdf

%files -n texlive-pdfslide
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfslide/bg.jpg
%{_texmfdistdir}/tex/latex/pdfslide/d12.jpg
%{_texmfdistdir}/tex/latex/pdfslide/metablue.pdf
%{_texmfdistdir}/tex/latex/pdfslide/metagray.pdf
%{_texmfdistdir}/tex/latex/pdfslide/metagreen.pdf
%{_texmfdistdir}/tex/latex/pdfslide/metalgray.pdf
%{_texmfdistdir}/tex/latex/pdfslide/pdfslide.cfg
%{_texmfdistdir}/tex/latex/pdfslide/pdfslide.sty
%{_texmfdistdir}/tex/latex/pdfslide/slide.clo
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfslide-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-pdfsync
Version:        %{texlive_version}.%{texlive_noarch}.svn20373
Release:        0
License:        LPPL-1.0
Summary:        Provide links between source and PDF
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfsync-doc >= %{texlive_version}
Provides:       tex(pdfsync.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source134:      pdfsync.tar.xz
Source135:      pdfsync.doc.tar.xz

%description -n texlive-pdfsync
The package runs with pdfTeX or XeTeX, and creates an auxiliary
file with geometrical information to permit references back and
forth between source and PDF, assuming a conforming editor and
PDF viewer.

%package -n texlive-pdfsync-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20373
Release:        0
Summary:        Documentation for texlive-pdfsync
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfsync-doc
This package includes the documentation for texlive-pdfsync

%post -n texlive-pdfsync
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfsync
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfsync
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfsync-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfsync/README
%{_texmfdistdir}/doc/latex/pdfsync/pdfsync-doc.pdf
%{_texmfdistdir}/doc/latex/pdfsync/pdfsync-doc.tex

%files -n texlive-pdfsync
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfsync/pdfsync.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfsync-%{texlive_version}.%{texlive_noarch}.svn20373-%{release}-zypper
%endif

%package -n texlive-pdftex
Version:        %{texlive_version}.%{texlive_noarch}.svn57973
Release:        0
License:        GPL-2.0-or-later
Summary:        A TeX extension for direct creation of PDF
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Recommends:     texlive-collection-basic >= %{texlive_version}
Recommends:     texlive-collection-fontsrecommended >= %{texlive_version}
Recommends:     texlive-collection-genericrecommended >= %{texlive_version}
Requires:       texlive-cm >= %{texlive_version}
Requires:       tex(load-unicode-data.tex)
Requires:       tex(pdftexconfig.tex)
#!BuildIgnore: texlive-cm
Requires:       texlive-dehyph >= %{texlive_version}
#!BuildIgnore: texlive-dehyph
Requires:       texlive-etex >= %{texlive_version}
#!BuildIgnore: texlive-etex
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
Requires:       texlive-knuth-lib >= %{texlive_version}
#!BuildIgnore: texlive-knuth-lib
Requires:       texlive-kpathsea >= %{texlive_version}
#!BuildIgnore: texlive-kpathsea
Requires(pre):  texlive-pdftex-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdftex-bin
Requires:       texlive-plain >= %{texlive_version}
#!BuildIgnore: texlive-plain
Requires:       texlive-tex-ini-files >= %{texlive_version}
#!BuildIgnore: texlive-tex-ini-files
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
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
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(language.dat)
Requires(postun):tex(language.def)
Requires(postun):tex(language.dat.lua)
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-pdftex-fonts >= %{texlive_version}
Recommends:     texlive-pdftex-doc >= %{texlive_version}
Requires(posttrans):texlive-graphics-def >= %{texlive_version}
Provides:       tex(dummy-space.map)
Provides:       tex(dummy-space.tfm)
Provides:       tex(glyphtounicode.tex)
Provides:       tex(pdfcolor.tex)
Provides:       tex(pdftex-dvi.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source136:      pdftex.tar.xz
Source137:      pdftex.doc.tar.xz

%description -n texlive-pdftex
An extension of TeX which can directly generate PDF documents
as well as DVI output. All current free TeX distributions
including TeX Live, MacTeX and MiKTeX include pdfTeX (Plain
TeX) and pdfLaTeX (LaTeX), among many other formats based on
the pdfTeX engine.

%package -n texlive-pdftex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn57973
Release:        0
Summary:        Documentation for texlive-pdftex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(pdfetex.1)
Provides:       man(pdftex.1)

%description -n texlive-pdftex-doc
This package includes the documentation for texlive-pdftex

%package -n texlive-pdftex-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn57973
Release:        0
Summary:        Severed fonts for texlive-pdftex
License:        GPL-2.0-or-later
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-pdftex-fonts
The  separated fonts package for texlive-pdftex

%post -n texlive-pdftex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.etex
sed -ri 's/^\#\![[= =]]+etex\b.*/etex pdftex language.def -translate-file=cp227.tcx *etex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
> /var/run/texlive/run-fmtutil.pdfetex
sed -ri 's/^\#\![[= =]]+pdfetex\b.*/pdfetex pdftex language.def -translate-file=cp227.tcx *pdfetex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
> /var/run/texlive/run-fmtutil.pdftex
sed -ri 's/^\#\![[= =]]+pdftex\b.*/pdftex pdftex language.def -translate-file=cp227.tcx *pdfetex.ini/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
echo 'addMap dummy-space.map' >> /var/run/texlive/run-updmap

%postun -n texlive-pdftex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    sed -ri 's/^(etex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/pdftex/etex.*
    sed -ri 's/^(pdfetex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/pdftex/pdfetex.*
    sed -ri 's/^(pdftex\b)/\#\!\ \1/' %{_texmfconfdir}/web2c/fmtutil.cnf || :
    rm -f %{_texmfvardir}/web2c/pdftex/pdftex.*
    echo 'deleteMap dummy-space.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%triggerin -n texlive-pdftex -- texlive-cm
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-cm
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerin -n texlive-pdftex -- texlive-dehyph
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-dehyph
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerin -n texlive-pdftex -- texlive-etex
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-etex
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerin -n texlive-pdftex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-hyph-utf8
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerin -n texlive-pdftex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-hyphen-base
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerin -n texlive-pdftex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-knuth-lib
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerin -n texlive-pdftex -- texlive-plain
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-plain
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerin -n texlive-pdftex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%triggerun -n texlive-pdftex -- texlive-tex-ini-files
> /var/run/texlive/run-fmtutil.etex
> /var/run/texlive/run-fmtutil.pdfetex
> /var/run/texlive/run-fmtutil.pdftex

%posttrans -n texlive-pdftex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-pdftex-fonts

%files -n texlive-pdftex-doc
%defattr(-,root,root,755)
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pdftex.1*
%{_texmfdistdir}/doc/pdftex/NEWS
%{_texmfdistdir}/doc/pdftex/README
%{_texmfdistdir}/doc/pdftex/manual/ChangeLog
%{_texmfdistdir}/doc/pdftex/manual/Makefile
%{_texmfdistdir}/doc/pdftex/manual/README
%{_texmfdistdir}/doc/pdftex/manual/makefiles.cmd
%{_texmfdistdir}/doc/pdftex/manual/pdftex-a.pdf
%{_texmfdistdir}/doc/pdftex/manual/pdftex-i.tex
%{_texmfdistdir}/doc/pdftex/manual/pdftex-syntax.txt
%{_texmfdistdir}/doc/pdftex/manual/pdftex-t.tex
%{_texmfdistdir}/doc/pdftex/manual/pdftex-w.tex
%{_texmfdistdir}/doc/pdftex/manual/syntaxform.awk
%{_texmfdistdir}/doc/pdftex/manual/syntaxform.pl
%{_texmfdistdir}/doc/pdftex/samplepdftex/cmr10.103
%{_texmfdistdir}/doc/pdftex/samplepdftex/obj.dat
%{_texmfdistdir}/doc/pdftex/samplepdftex/pdfcolor.tex
%{_texmfdistdir}/doc/pdftex/samplepdftex/pic.eps
%{_texmfdistdir}/doc/pdftex/samplepdftex/pic.jpg
%{_texmfdistdir}/doc/pdftex/samplepdftex/pic.mps
%{_texmfdistdir}/doc/pdftex/samplepdftex/pic.pdf
%{_texmfdistdir}/doc/pdftex/samplepdftex/pic.png
%{_texmfdistdir}/doc/pdftex/samplepdftex/pic16.png
%{_texmfdistdir}/doc/pdftex/samplepdftex/rgb.icc
%{_texmfdistdir}/doc/pdftex/samplepdftex/samplepdf.0
%{_texmfdistdir}/doc/pdftex/samplepdftex/samplepdf.1
%{_texmfdistdir}/doc/pdftex/samplepdftex/samplepdf.tex
%{_texmfdistdir}/doc/pdftex/samplepdftex/supp-mis.tex
%{_texmfdistdir}/doc/pdftex/samplepdftex/supp-pdf.tex
%{_texmfdistdir}/doc/pdftex/samplepdftex/tmp.pdf
%{_texmfdistdir}/doc/pdftex/tests/01-fake-interword-space/Makefile
%{_texmfdistdir}/doc/pdftex/tests/01-fake-interword-space/dummy-space.pfb
%{_texmfdistdir}/doc/pdftex/tests/01-fake-interword-space/dummy-space.tfm
%{_texmfdistdir}/doc/pdftex/tests/01-fake-interword-space/fake-interword-space.tex
%{_texmfdistdir}/doc/pdftex/tests/02-pdfmatch/Makefile
%{_texmfdistdir}/doc/pdftex/tests/02-pdfmatch/test-pdfmatch.tex
%{_texmfdistdir}/doc/pdftex/tests/03-deterministic-output/Makefile
%{_texmfdistdir}/doc/pdftex/tests/03-deterministic-output/test-SOURCE_DATE_EPOCH.tex
%{_texmfdistdir}/doc/pdftex/tests/03-deterministic-output/test-fixed-date-id.tex
%{_texmfdistdir}/doc/pdftex/tests/03-deterministic-output/test-no-date-id.tex
%{_texmfdistdir}/doc/pdftex/tests/03-deterministic-output/test-prim.tex
%{_texmfdistdir}/doc/pdftex/tests/04-pdfsuppressptexinfo/Makefile
%{_texmfdistdir}/doc/pdftex/tests/04-pdfsuppressptexinfo/abc.tex
%{_texmfdistdir}/doc/pdftex/tests/04-pdfsuppressptexinfo/test-pdfinfoomitdate.tex
%{_texmfdistdir}/doc/pdftex/tests/04-pdfsuppressptexinfo/test-pdfsuppressptexinfo.tex
%{_texmfdistdir}/doc/pdftex/tests/04-pdfsuppressptexinfo/test-pdftrailer.tex
%{_texmfdistdir}/doc/pdftex/tests/05-mediabox/Makefile
%{_texmfdistdir}/doc/pdftex/tests/05-mediabox/test-normal.tex
%{_texmfdistdir}/doc/pdftex/tests/05-mediabox/test-omit-mediabox.tex
%{_texmfdistdir}/doc/pdftex/tests/06-pkmap/Makefile
%{_texmfdistdir}/doc/pdftex/tests/06-pkmap/cmb10.72pk
%{_texmfdistdir}/doc/pdftex/tests/06-pkmap/cmr10.360pk
%{_texmfdistdir}/doc/pdftex/tests/06-pkmap/cmr10.72pk
%{_texmfdistdir}/doc/pdftex/tests/06-pkmap/prepatch.pdf
%{_texmfdistdir}/doc/pdftex/tests/06-pkmap/test-pkmap.tex
%{_texmfdistdir}/doc/pdftex/tests/07-mapwarn/Makefile
%{_texmfdistdir}/doc/pdftex/tests/07-mapwarn/test-mapwarn.tex
%{_texmfdistdir}/doc/pdftex/tests/08-pdfprimitive/Makefile
%{_texmfdistdir}/doc/pdftex/tests/08-pdfprimitive/test-pdfprimitive-non.tex
%{_texmfdistdir}/doc/pdftex/tests/08-pdfprimitive/test-pdfprimitive-ok.tex
%{_texmfdistdir}/doc/pdftex/tests/08-pdfprimitive/test-pdfprimitive-post.tex
%{_texmfdistdir}/doc/pdftex/tests/09-fontobjnum/Makefile
%{_texmfdistdir}/doc/pdftex/tests/09-fontobjnum/test-fontobjnum.tex
%{_texmfdistdir}/doc/pdftex/tests/10-moddate/Makefile
%{_texmfdistdir}/doc/pdftex/tests/10-moddate/test-moddate-abs.tex
%{_texmfdistdir}/doc/pdftex/tests/10-moddate/test-moddate.tex
%{_texmfdistdir}/doc/pdftex/tests/11-omitcharset/Makefile
%{_texmfdistdir}/doc/pdftex/tests/11-omitcharset/test-omitcharset.tex
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/Makefile
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/incl1.tex
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/incl2.tex
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/test-compress2.tex
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/test-doc1incl2.tex
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/test-doc2incl1.tex
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/test-doc2incl2.tex
%{_texmfdistdir}/doc/pdftex/tests/12-pdf2/test-pdfmajor.tex
%{_texmfdistdir}/doc/pdftex/tests/Common.mak

%files -n texlive-pdftex
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/dummy-space/dummy-space.map
%{_texmfdistdir}/fonts/tfm/public/pdftex/dummy-space.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pdftex/dummy-space.pfb
%{_texmfdistdir}/scripts/simpdftex/simpdftex
%{_texmfdistdir}/tex/generic/config/pdftex-dvi.tex
%{_texmfdistdir}/tex/generic/pdftex/glyphtounicode.tex
%{_texmfdistdir}/tex/generic/pdftex/pdfcolor.tex

%files -n texlive-pdftex-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-pdftex
%{_datadir}/fontconfig/conf.avail/58-texlive-pdftex.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pdftex/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pdftex/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pdftex/fonts.scale
%{_datadir}/fonts/texlive-pdftex/dummy-space.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdftex-fonts-%{texlive_version}.%{texlive_noarch}.svn57973-%{release}-zypper
%endif

%package -n texlive-pdftex-quiet
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn49169
Release:        0
License:        GPL-2.0-or-later
Summary:        A bash wrapper for pdfTeX limiting its output to relevant errors
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdftex-quiet-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdftex-quiet-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdftex-quiet-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source138:      pdftex-quiet.tar.xz
Source139:      pdftex-quiet.doc.tar.xz

%description -n texlive-pdftex-quiet
This package provides a bash script aiming at reducing pdfTeX's
output to relevant errors, which are displayed in a red bold
font. The project originally started as a TeX StackExchange
answer.

%package -n texlive-pdftex-quiet-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.0svn49169
Release:        0
Summary:        Documentation for texlive-pdftex-quiet
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdftex-quiet-doc
This package includes the documentation for texlive-pdftex-quiet

%post -n texlive-pdftex-quiet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdftex-quiet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdftex-quiet
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdftex-quiet-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/pdftex-quiet/LICENCE
%{_texmfdistdir}/doc/support/pdftex-quiet/README.md
%{_texmfdistdir}/doc/support/pdftex-quiet/VERSION

%files -n texlive-pdftex-quiet
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pdftex-quiet/pdftex-quiet
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdftex-quiet-%{texlive_version}.%{texlive_noarch}.1.1.0svn49169-%{release}-zypper
%endif

%package -n texlive-pdftexcmds
Version:        %{texlive_version}.%{texlive_noarch}.0.0.33svn55777
Release:        0
License:        LPPL-1.0
Summary:        LuaTeX support for pdfTeX utility functions
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdftexcmds-doc >= %{texlive_version}
Provides:       tex(pdftexcmds.sty)
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source140:      pdftexcmds.tar.xz
Source141:      pdftexcmds.doc.tar.xz

%description -n texlive-pdftexcmds
LuaTeX provides most of the commands of pdfTeX 1.40. However, a
number of utility functions are not available. This package
tries to fill the gap and implements some of the missing
primitives using Lua.

%package -n texlive-pdftexcmds-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.33svn55777
Release:        0
Summary:        Documentation for texlive-pdftexcmds
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdftexcmds-doc
This package includes the documentation for texlive-pdftexcmds

%post -n texlive-pdftexcmds
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdftexcmds
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdftexcmds
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdftexcmds-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pdftexcmds/README.md
%{_texmfdistdir}/doc/generic/pdftexcmds/pdftexcmds.bib
%{_texmfdistdir}/doc/generic/pdftexcmds/pdftexcmds.pdf

%files -n texlive-pdftexcmds
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pdftexcmds/pdftexcmds.lua
%{_texmfdistdir}/tex/generic/pdftexcmds/pdftexcmds.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdftexcmds-%{texlive_version}.%{texlive_noarch}.0.0.33svn55777-%{release}-zypper
%endif

%package -n texlive-pdftosrc
Version:        %{texlive_version}.%{texlive_noarch}.svn57972
Release:        0
License:        LPPL-1.0
Summary:        Extract source file or stream from PDF file
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdftosrc-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdftosrc-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       man(pdftosrc.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source142:      pdftosrc.doc.tar.xz

%description -n texlive-pdftosrc
Extracts an embedded source file, or extracts and uncompresses
a PDF stream given by object number. Developed as part of the
pdfTeX source tree.

%post -n texlive-pdftosrc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdftosrc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdftosrc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdftosrc
%defattr(-,root,root,755)
%{_mandir}/man1/pdftosrc.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdftosrc-%{texlive_version}.%{texlive_noarch}.svn57972-%{release}-zypper
%endif

%package -n texlive-pdftricks
Version:        %{texlive_version}.%{texlive_noarch}.1.16svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Support for PSTricks in pdfTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdftricks-doc >= %{texlive_version}
Provides:       tex(pdftricks.sty)
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(moreverb.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source143:      pdftricks.tar.xz
Source144:      pdftricks.doc.tar.xz

%description -n texlive-pdftricks
The PSTricks macros cannot be used (directly) with pdfTeX,
since PSTricks uses PostScript arithmetic, which isn't part of
PDF. This package circumvents this limitation so that the
extensive facilities offered by the powerful PSTricks package
can be made use of in a pdfTeX document. This is done using the
shell escape function available in current TeX implementations.
The package may also be used in support of other
'PostScript-output-only' packages, such as PSfrag. For
alternatives, users may care to review the discussion in the
PSTricks online documentation.

%package -n texlive-pdftricks-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.16svn15878
Release:        0
Summary:        Documentation for texlive-pdftricks
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdftricks-doc
This package includes the documentation for texlive-pdftricks

%post -n texlive-pdftricks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdftricks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdftricks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdftricks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdftricks/makefile
%{_texmfdistdir}/doc/latex/pdftricks/manual.pdf
%{_texmfdistdir}/doc/latex/pdftricks/pst2pdf
%{_texmfdistdir}/doc/latex/pdftricks/test.pdf
%{_texmfdistdir}/doc/latex/pdftricks/test.tex

%files -n texlive-pdftricks
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdftricks/pdftricks.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdftricks-%{texlive_version}.%{texlive_noarch}.1.16svn15878-%{release}-zypper
%endif

%package -n texlive-pdftricks2
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn31016
Release:        0
License:        GPL-2.0-or-later
Summary:        Use PSTricks in pdfTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdftricks2-doc >= %{texlive_version}
Provides:       tex(pdftricks2.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source145:      pdftricks2.tar.xz
Source146:      pdftricks2.doc.tar.xz

%description -n texlive-pdftricks2
The package provides the means of processing documents (that
contain pstricks graphics specifications. The package is
inspired by pdftricks

%package -n texlive-pdftricks2-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn31016
Release:        0
Summary:        Documentation for texlive-pdftricks2
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdftricks2-doc
This package includes the documentation for texlive-pdftricks2

%post -n texlive-pdftricks2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdftricks2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdftricks2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdftricks2-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdftricks2/README
%{_texmfdistdir}/doc/latex/pdftricks2/pdftricks2-doc.pdf
%{_texmfdistdir}/doc/latex/pdftricks2/pdftricks2-doc.tex

%files -n texlive-pdftricks2
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdftricks2/pdftricks2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdftricks2-%{texlive_version}.%{texlive_noarch}.1.01svn31016-%{release}-zypper
%endif

%package -n texlive-pdfwin
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
License:        LPPL-1.0
Summary:        Customizable windows for screen viewing of TeX documents
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfwin-doc >= %{texlive_version}
Provides:       tex(pdfwin.cfg)
Provides:       tex(pdfwin.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(truncate.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source147:      pdfwin.tar.xz
Source148:      pdfwin.doc.tar.xz

%description -n texlive-pdfwin
Inspired by the pdfscreen package.

%package -n texlive-pdfwin-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Documentation for texlive-pdfwin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfwin-doc
This package includes the documentation for texlive-pdfwin

%post -n texlive-pdfwin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfwin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfwin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfwin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfwin/BucResampling.pdf
%{_texmfdistdir}/doc/latex/pdfwin/BucSystem1.pdf
%{_texmfdistdir}/doc/latex/pdfwin/BucSystem2.pdf
%{_texmfdistdir}/doc/latex/pdfwin/BucSystem3.pdf
%{_texmfdistdir}/doc/latex/pdfwin/BucSystem4.pdf
%{_texmfdistdir}/doc/latex/pdfwin/BucSystem5.pdf
%{_texmfdistdir}/doc/latex/pdfwin/BucSystem6.pdf
%{_texmfdistdir}/doc/latex/pdfwin/Bucuresti2003.tex
%{_texmfdistdir}/doc/latex/pdfwin/JWGU-Logo.png
%{_texmfdistdir}/doc/latex/pdfwin/Thumbs.db
%{_texmfdistdir}/doc/latex/pdfwin/marble.png
%{_texmfdistdir}/doc/latex/pdfwin/normprot.tex
%{_texmfdistdir}/doc/latex/pdfwin/shortvec.tex

%files -n texlive-pdfwin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfwin/pdfwin.cfg
%{_texmfdistdir}/tex/latex/pdfwin/pdfwin.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfwin-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif

%package -n texlive-pdfx
Version:        %{texlive_version}.%{texlive_noarch}.1.6.3svn50338
Release:        0
License:        LPPL-1.0
Summary:        PDF/X and PDF/A support for pdfTeX, LuaTeX and XeTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfx-doc >= %{texlive_version}
Provides:       tex(8bit.def)
Provides:       tex(AdobeColorProfiles.tex)
Provides:       tex(AdobeExternalProfiles.tex)
Provides:       tex(CallasColorProfiles.tex)
Provides:       tex(glyphtounicode-cmr.tex)
Provides:       tex(glyphtounicode-ntx.tex)
Provides:       tex(l8u-penc.def)
Provides:       tex(l8uarb-penc.def)
Provides:       tex(l8uarm-penc.def)
Provides:       tex(l8ucyr-penc.def)
Provides:       tex(l8udev-penc.def)
Provides:       tex(l8ugrk-penc.def)
Provides:       tex(l8uheb-penc.def)
Provides:       tex(l8ulat-penc.def)
Provides:       tex(l8umath-penc.def)
Provides:       tex(pdfx.sty)
Provides:       tex(text89.def)
Requires:       tex(colorprofiles.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(glyphtounicode.tex)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(luatex85.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(stringenc.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xmpincl.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source149:      pdfx.tar.xz
Source150:      pdfx.doc.tar.xz

%description -n texlive-pdfx
The package helps LaTeX users to create PDF/X, PFD/A and other
standards-compliant PDF documents with pdfTeX, LuaTeX and
XeTeX.

%package -n texlive-pdfx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6.3svn50338
Release:        0
Summary:        Documentation for texlive-pdfx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pdfx-doc
This package includes the documentation for texlive-pdfx

%post -n texlive-pdfx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pdfx/Armenian-example-UTF8.png
%{_texmfdistdir}/doc/latex/pdfx/MANIFEST
%{_texmfdistdir}/doc/latex/pdfx/README
%{_texmfdistdir}/doc/latex/pdfx/TL-POL-meta.png
%{_texmfdistdir}/doc/latex/pdfx/TL-RU-LICRs.png
%{_texmfdistdir}/doc/latex/pdfx/TL-RU-metadata.png
%{_texmfdistdir}/doc/latex/pdfx/TL-RU-toc.png
%{_texmfdistdir}/doc/latex/pdfx/arm-start.tex
%{_texmfdistdir}/doc/latex/pdfx/armtex-meta.png
%{_texmfdistdir}/doc/latex/pdfx/koi8-example.tex
%{_texmfdistdir}/doc/latex/pdfx/koi8-example2.tex
%{_texmfdistdir}/doc/latex/pdfx/latin2-example.tex
%{_texmfdistdir}/doc/latex/pdfx/manifest.txt
%{_texmfdistdir}/doc/latex/pdfx/math-assign5.png
%{_texmfdistdir}/doc/latex/pdfx/pdfx.pdf
%{_texmfdistdir}/doc/latex/pdfx/pdfx.xmpdata
%{_texmfdistdir}/doc/latex/pdfx/sample.tex
%{_texmfdistdir}/doc/latex/pdfx/small2e-pdfx.tex
%{_texmfdistdir}/doc/latex/pdfx/usage-meta.png

%files -n texlive-pdfx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pdfx/8bit.def
%{_texmfdistdir}/tex/latex/pdfx/AdobeColorProfiles.tex
%{_texmfdistdir}/tex/latex/pdfx/AdobeExternalProfiles.tex
%{_texmfdistdir}/tex/latex/pdfx/CallasColorProfiles.tex
%{_texmfdistdir}/tex/latex/pdfx/armglyphs.dfu
%{_texmfdistdir}/tex/latex/pdfx/glyphtounicode-cmr.tex
%{_texmfdistdir}/tex/latex/pdfx/glyphtounicode-ntx.tex
%{_texmfdistdir}/tex/latex/pdfx/l8u-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8uarb-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8uarm-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8ucyr-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8udev-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8ugrk-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8uheb-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8ulat-penc.def
%{_texmfdistdir}/tex/latex/pdfx/l8umath-penc.def
%{_texmfdistdir}/tex/latex/pdfx/pdfa.xmp
%{_texmfdistdir}/tex/latex/pdfx/pdfe.xmp
%{_texmfdistdir}/tex/latex/pdfx/pdfvt.xmp
%{_texmfdistdir}/tex/latex/pdfx/pdfx.sty
%{_texmfdistdir}/tex/latex/pdfx/pdfx.xmp
%{_texmfdistdir}/tex/latex/pdfx/text89.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfx-%{texlive_version}.%{texlive_noarch}.1.6.3svn50338-%{release}-zypper
%endif

%package -n texlive-pdfxup
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn57166
Release:        0
License:        LPPL-1.0
Summary:        Create n-up PDF pages with minimal margins
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pdfxup-bin >= %{texlive_version}
#!BuildIgnore: texlive-pdfxup-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pdfxup-doc >= %{texlive_version}
Provides:       tex(pdfxup-template.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source151:      pdfxup.tar.xz
Source152:      pdfxup.doc.tar.xz

%description -n texlive-pdfxup
pdfxup is a Unix/Linux shell script that creates a PDF document
where each page is obtained by combining several pages of a PDF
file given as output. pdfxup uses ghostscript for computing the
maximal bounding box of (some of) the pages of the document,
and then uses pdflatex (with the graphicx package) in order to
produce the new document.

%package -n texlive-pdfxup-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.00svn57166
Release:        0
Summary:        Documentation for texlive-pdfxup
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(pdfxup.1)

%description -n texlive-pdfxup-doc
This package includes the documentation for texlive-pdfxup

%post -n texlive-pdfxup
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pdfxup
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pdfxup
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pdfxup-doc
%defattr(-,root,root,755)
%{_mandir}/man1/pdfxup.1*
%{_texmfdistdir}/doc/support/pdfxup/README
%{_texmfdistdir}/doc/support/pdfxup/RELEASES
%{_texmfdistdir}/doc/support/pdfxup/pdfxup.pdf

%files -n texlive-pdfxup
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pdfxup/pdfxup
%{_texmfdistdir}/tex/latex/pdfxup/beamer2.xup
%{_texmfdistdir}/tex/latex/pdfxup/beamer4.xup
%{_texmfdistdir}/tex/latex/pdfxup/pdfxup-template.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pdfxup-%{texlive_version}.%{texlive_noarch}.2.00svn57166-%{release}-zypper
%endif

%package -n texlive-pecha
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
License:        GPL-2.0-or-later
Summary:        Print Tibetan text in the classic pecha layout style
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pecha-doc >= %{texlive_version}
Provides:       tex(ctibmantra.sty)
Provides:       tex(pecha.cls)
Requires:       tex(calc.sty)
Requires:       tex(ctib.sty)
Requires:       tex(relsize.sty)
Requires:       tex(rotating.sty)
Requires:       tex(times.sty)
Requires:       tex(twoopt.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source153:      pecha.tar.xz
Source154:      pecha.doc.tar.xz

%description -n texlive-pecha
The pecha class provides an environment for writing Tibetan on
LaTeX2e in the traditional Tibetan Pecha layout used for
spiritual or philosophical texts, using the cTib4TeX package by
Oliver Corff. It provides features like headers in different
languages, page numbering in Tibetan and more.

%package -n texlive-pecha-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-pecha
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pecha-doc
This package includes the documentation for texlive-pecha

%post -n texlive-pecha
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pecha
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pecha
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pecha-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pecha/CHANGES
%{_texmfdistdir}/doc/latex/pecha/COPYING
%{_texmfdistdir}/doc/latex/pecha/README
%{_texmfdistdir}/doc/latex/pecha/example.pdf
%{_texmfdistdir}/doc/latex/pecha/example.tex
%{_texmfdistdir}/doc/latex/pecha/pecha_docu.pdf
%{_texmfdistdir}/doc/latex/pecha/pecha_docu.tex

%files -n texlive-pecha
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pecha/ctibmantra.sty
%{_texmfdistdir}/tex/latex/pecha/pecha.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pecha-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif

%package -n texlive-pedigree-perl
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn31990
Release:        0
License:        GPL-2.0-or-later
Summary:        Generate TeX pedigree files from CSV files
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pedigree-perl-bin >= %{texlive_version}
#!BuildIgnore: texlive-pedigree-perl-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pedigree-perl-doc >= %{texlive_version}
Requires:       perl(FileHandle)
#!BuildIgnore:  perl(FileHandle)
Requires:       perl(Getopt::Std)
#!BuildIgnore:  perl(Getopt::Std)
Requires:       perl(Pedigree)
#!BuildIgnore:  perl(Pedigree)
Requires:       perl(Pedigree::AbortionNode)
#!BuildIgnore:  perl(Pedigree::AbortionNode)
Requires:       perl(Pedigree::Area)
#!BuildIgnore:  perl(Pedigree::Area)
Requires:       perl(Pedigree::ChildlessNode)
#!BuildIgnore:  perl(Pedigree::ChildlessNode)
Requires:       perl(Pedigree::Language)
#!BuildIgnore:  perl(Pedigree::Language)
Requires:       perl(Pedigree::MarriageNode)
#!BuildIgnore:  perl(Pedigree::MarriageNode)
Requires:       perl(Pedigree::Node)
#!BuildIgnore:  perl(Pedigree::Node)
Requires:       perl(Pedigree::Parser)
#!BuildIgnore:  perl(Pedigree::Parser)
Requires:       perl(Pedigree::PersonNode)
#!BuildIgnore:  perl(Pedigree::PersonNode)
Requires:       perl(Pedigree::TwinsNode)
#!BuildIgnore:  perl(Pedigree::TwinsNode)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(vars)
#!BuildIgnore:  perl(vars)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source155:      pedigree-perl.tar.xz
Source156:      pedigree-perl.doc.tar.xz

%description -n texlive-pedigree-perl
This program generates TeX commands to typeset pedigrees --
either TeX fragments or full LaTeX files, to be processed by
the authors' pst-pdgr package. The program has support for
multilanguage pedigrees (at the present moment the English and
Russian languages are supported).

%package -n texlive-pedigree-perl-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn31990
Release:        0
Summary:        Documentation for texlive-pedigree-perl
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(pedigree.1)

%description -n texlive-pedigree-perl-doc
This package includes the documentation for texlive-pedigree-perl

%post -n texlive-pedigree-perl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pedigree-perl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pedigree-perl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pedigree-perl-doc
%defattr(-,root,root,755)
%{_mandir}/man1/pedigree.1*
%{_texmfdistdir}/doc/support/pedigree-perl/LICENSE
%{_texmfdistdir}/doc/support/pedigree-perl/Makefile
%{_texmfdistdir}/doc/support/pedigree-perl/NEWS
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/AbortionNode.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Area.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/ChildlessNode.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Language.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Makefile
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/MarriageNode.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Node.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/Parser.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/PersonNode.3
%{_texmfdistdir}/doc/support/pedigree-perl/Pedigree/TwinsNode.3
%{_texmfdistdir}/doc/support/pedigree-perl/README
%{_texmfdistdir}/doc/support/pedigree-perl/doc/Makefile
%{_texmfdistdir}/doc/support/pedigree-perl/doc/abortions.tex
%{_texmfdistdir}/doc/support/pedigree-perl/doc/english.tex
%{_texmfdistdir}/doc/support/pedigree-perl/doc/english1.tex
%{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.bib
%{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.pdf
%{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.ps
%{_texmfdistdir}/doc/support/pedigree-perl/doc/pedigree.tex
%{_texmfdistdir}/doc/support/pedigree-perl/doc/russian.tex
%{_texmfdistdir}/doc/support/pedigree-perl/examples/abortions.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/badsort.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/childlessness.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/consanguinic.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/english.cfg
%{_texmfdistdir}/doc/support/pedigree-perl/examples/english.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/english1.cfg
%{_texmfdistdir}/doc/support/pedigree-perl/examples/english_short.cfg
%{_texmfdistdir}/doc/support/pedigree-perl/examples/pedigree.cfg
%{_texmfdistdir}/doc/support/pedigree-perl/examples/russian.cfg
%{_texmfdistdir}/doc/support/pedigree-perl/examples/russian.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/sort1.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/sort2.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/sort3.csv
%{_texmfdistdir}/doc/support/pedigree-perl/examples/twins.csv

%files -n texlive-pedigree-perl
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/AbortionNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Area.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/ChildlessNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Language.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/MarriageNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Node.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/Parser.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/PersonNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/Pedigree/TwinsNode.pm
%{_texmfdistdir}/scripts/pedigree-perl/pedigree.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pedigree-perl-%{texlive_version}.%{texlive_noarch}.1.0svn31990-%{release}-zypper
%endif

%package -n texlive-penrose
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn57508
Release:        0
License:        LPPL-1.0
Summary:        A TikZ library for producing Penrose tilings
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-penrose-doc >= %{texlive_version}
Provides:       tex(tikzlibrarypenrose.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source157:      penrose.tar.xz
Source158:      penrose.doc.tar.xz

%description -n texlive-penrose
This package provides a TikZ library for drawing Penrose tiles.
It currently supports the kite/dart, rhombus, and pentagon tile
sets. There are two main methods for their placement: one that
automatically generates a tiling, and one that allows for "by
hand" placement. Furthermore, the tiles themselves can be
deformed and will still (hopefully!) fit together in the
correct fashion.

%package -n texlive-penrose-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn57508
Release:        0
Summary:        Documentation for texlive-penrose
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-penrose-doc
This package includes the documentation for texlive-penrose

%post -n texlive-penrose
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-penrose
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-penrose
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-penrose-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/penrose/README
%{_texmfdistdir}/doc/latex/penrose/README.txt
%{_texmfdistdir}/doc/latex/penrose/penrose.pdf
%{_texmfdistdir}/doc/latex/penrose/penrose.tex
%{_texmfdistdir}/doc/latex/penrose/penrose_code.pdf

%files -n texlive-penrose
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/penrose/tikzlibrarypenrose.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-penrose-%{texlive_version}.%{texlive_noarch}.1.4svn57508-%{release}-zypper
%endif

%package -n texlive-perception
Version:        %{texlive_version}.%{texlive_noarch}.svn48861
Release:        0
License:        LPPL-1.0
Summary:        BibTeX style for the journal Perception
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-perception-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source159:      perception.tar.xz
Source160:      perception.doc.tar.xz

%description -n texlive-perception
A product of custom-bib, provided simply to save others' time.

%package -n texlive-perception-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn48861
Release:        0
Summary:        Documentation for texlive-perception
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-perception-doc
This package includes the documentation for texlive-perception

%post -n texlive-perception
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-perception
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-perception
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-perception-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/perception/README

%files -n texlive-perception
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/perception/perception.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-perception-%{texlive_version}.%{texlive_noarch}.svn48861-%{release}-zypper
%endif

%package -n texlive-perfectcut
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn54080
Release:        0
License:        LPPL-1.0
Summary:        Nested delimiters that consistently grow regardless of the contents
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-perfectcut-doc >= %{texlive_version}
Provides:       tex(perfectcut.sty)
Requires:       tex(calc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(mathstyle.sty)
Requires:       tex(scalerel.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source161:      perfectcut.tar.xz
Source162:      perfectcut.doc.tar.xz

%description -n texlive-perfectcut
This package defines the command \perfectcut#1#2 which displays
a bracket <#1||#2>. Various other delimiters are similarly
defined (parentheses, square brackets ...). The effect of these
commands is to let the delimiters grow according to the number
of nested \perfectcommands (regardless of the size of the
contents). The package was originally intended for solving a
notational issue for direct-style continuation calculi in proof
theory. For general use, the package also defines commands for
defining other sorts of delimiters which will behave in the
same way (see example in the documentation). The package also
offers a robust reimplementation of \big, \bigg, etc.

%package -n texlive-perfectcut-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn54080
Release:        0
Summary:        Documentation for texlive-perfectcut
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-perfectcut-doc
This package includes the documentation for texlive-perfectcut

%post -n texlive-perfectcut
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-perfectcut
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-perfectcut
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-perfectcut-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/perfectcut/README
%{_texmfdistdir}/doc/latex/perfectcut/perfectcut.pdf
%{_texmfdistdir}/doc/latex/perfectcut/perfectcut.tex

%files -n texlive-perfectcut
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/perfectcut/perfectcut.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-perfectcut-%{texlive_version}.%{texlive_noarch}.2.3svn54080-%{release}-zypper
%endif

%package -n texlive-perltex
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn52162
Release:        0
License:        LPPL-1.0
Summary:        Define LaTeX macros in terms of Perl code
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-perltex-bin >= %{texlive_version}
#!BuildIgnore: texlive-perltex-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-perltex-doc >= %{texlive_version}
Requires:       perl(Fcntl)
#!BuildIgnore:  perl(Fcntl)
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(IO::Handle)
#!BuildIgnore:  perl(IO::Handle)
Requires:       perl(Opcode)
#!BuildIgnore:  perl(Opcode)
Requires:       perl(POSIX)
#!BuildIgnore:  perl(POSIX)
Requires:       perl(Pod::Usage)
#!BuildIgnore:  perl(Pod::Usage)
Requires:       perl(Safe)
#!BuildIgnore:  perl(Safe)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
Provides:       tex(perltex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source163:      perltex.tar.xz
Source164:      perltex.doc.tar.xz

%description -n texlive-perltex
PerlTeX is a combination Perl script (perltex.pl) and LaTeX2e
package (perltex.sty) that, together, give the user the ability
to define LaTeX macros in terms of Perl code. Once defined, a
Perl macro becomes indistinguishable from any other LaTeX
macro. PerlTeX thereby combines LaTeX's typesetting power with
Perl's programmability. PerlTeX will make use of persistent
named pipes, and thereby run more efficiently, on operating
systems that offer them (mostly Unix-like systems). Also
provided is a switch to generate a PerlTeX-free,
document-specific, noperltex.sty that is useful when
distributing a document to places where PerlTeX is not
available.

%package -n texlive-perltex-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn52162
Release:        0
Summary:        Documentation for texlive-perltex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(perltex.1)

%description -n texlive-perltex-doc
This package includes the documentation for texlive-perltex

%post -n texlive-perltex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-perltex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-perltex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-perltex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/perltex/README
%{_texmfdistdir}/doc/latex/perltex/example.tex
%{_texmfdistdir}/doc/latex/perltex/perltex.pdf
%{_mandir}/man1/perltex.1*

%files -n texlive-perltex
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/perltex/perltex.pl
%{_texmfdistdir}/tex/latex/perltex/perltex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-perltex-%{texlive_version}.%{texlive_noarch}.2.2svn52162-%{release}-zypper
%endif

%package -n texlive-permute
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Support for symmetric groups
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-permute-doc >= %{texlive_version}
Provides:       tex(permute.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source165:      permute.tar.xz
Source166:      permute.doc.tar.xz

%description -n texlive-permute
A package for symmetric groups, allowing you to input, output,
and calculate with them.

%package -n texlive-permute-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-permute
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-permute-doc
This package includes the documentation for texlive-permute

%post -n texlive-permute
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-permute
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-permute
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-permute-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/permute/permute.pdf

%files -n texlive-permute
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/permute/permute.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-permute-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-persian-bib
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn37297
Release:        0
License:        LPPL-1.0
Summary:        Persian translations of classic BibTeX styles
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-persian-bib-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source167:      persian-bib.tar.xz
Source168:      persian-bib.doc.tar.xz

%description -n texlive-persian-bib
Currently 9 files: acm-fa.bst, asa-fa.bst, chicago-fa.bst,
ieeetr-fa.bst, plain-fa-inLTR-beamer.bst, plain-fa-inLTR.bst,
plain-fa.bst, plainnat-fa.bst and unsrt-fa.bst are modified for
Persian documents prepared with XePersian (which the present
package depends on). The Persian .bst files can simultaneously
handle both Latin and Persian references. A file cp1256fa.csf
is provided for correct sorting of Persian references and three
fields LANGUAGE, TRANSLATOR and AUTHORFA are defined.

%package -n texlive-persian-bib-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn37297
Release:        0
Summary:        Documentation for texlive-persian-bib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-persian-bib-doc:fa)

%description -n texlive-persian-bib-doc
This package includes the documentation for texlive-persian-bib

%post -n texlive-persian-bib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-persian-bib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-persian-bib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-persian-bib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/persian-bib/MyReferences.bib
%{_texmfdistdir}/doc/xelatex/persian-bib/Persian-bib-userguide.pdf
%{_texmfdistdir}/doc/xelatex/persian-bib/Persian-bib-userguide.tex
%{_texmfdistdir}/doc/xelatex/persian-bib/README
%{_texmfdistdir}/doc/xelatex/persian-bib/bibtex-example.tex
%{_texmfdistdir}/doc/xelatex/persian-bib/gen_pdf.pl

%files -n texlive-persian-bib
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/persian-bib/acm-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/asa-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/chicago-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/ieeetr-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/plain-fa-inLTR-beamer.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/plain-fa-inLTR.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/plain-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/plainnat-fa.bst
%{_texmfdistdir}/bibtex/bst/persian-bib/unsrt-fa.bst
%{_texmfdistdir}/bibtex/csf/persian-bib/cp1256fa.csf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-persian-bib-%{texlive_version}.%{texlive_noarch}.0.0.9svn37297-%{release}-zypper
%endif

%package -n texlive-petiteannonce
Version:        %{texlive_version}.%{texlive_noarch}.1.0001svn25915
Release:        0
License:        LPPL-1.0
Summary:        A class for small advertisements
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-petiteannonce-doc >= %{texlive_version}
Provides:       tex(petiteannonce.cls)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source169:      petiteannonce.tar.xz
Source170:      petiteannonce.doc.tar.xz

%description -n texlive-petiteannonce
The class enables you to create the sort of adverts that you
pin on a noticeboard, with tear-off strips at the bottom where
you can place contact details.

%package -n texlive-petiteannonce-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0001svn25915
Release:        0
Summary:        Documentation for texlive-petiteannonce
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-petiteannonce-doc
This package includes the documentation for texlive-petiteannonce

%post -n texlive-petiteannonce
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-petiteannonce
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-petiteannonce
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-petiteannonce-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/petiteannonce/baignoire.JPG
%{_texmfdistdir}/doc/latex/petiteannonce/petiteannonce.doc.pdf
%{_texmfdistdir}/doc/latex/petiteannonce/petiteannonce.doc.tex
%{_texmfdistdir}/doc/latex/petiteannonce/petiteannonceexample.pdf
%{_texmfdistdir}/doc/latex/petiteannonce/petiteannonceexample.tex

%files -n texlive-petiteannonce
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/petiteannonce/petiteannonce.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-petiteannonce-%{texlive_version}.%{texlive_noarch}.1.0001svn25915-%{release}-zypper
%endif

%package -n texlive-petri-nets
Version:        %{texlive_version}.%{texlive_noarch}.svn39165
Release:        0
License:        GPL-2.0-or-later
Summary:        A set TeX/LaTeX packages for drawing Petri nets
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-petri-nets-bin >= %{texlive_version}
#!BuildIgnore: texlive-petri-nets-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-petri-nets-doc >= %{texlive_version}
Requires:       perl(Digest::MD5)
#!BuildIgnore:  perl(Digest::MD5)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Provides:       tex(pndraw.sty)
Provides:       tex(pndraw.tex)
Provides:       tex(pnets.sty)
Provides:       tex(pnets.tex)
Provides:       tex(pntext.sty)
Provides:       tex(pntext.tex)
Provides:       tex(pnversion.tex)
Requires:       tex(amsfonts.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source171:      petri-nets.tar.xz
Source172:      petri-nets.doc.tar.xz

%description -n texlive-petri-nets
Petri-nets offers a set of TeX/LaTeX packages about Petri nets
and related models. Three packages are available: the first
allows the user to draw Petri-nets in PostScript documents; the
second defines macros related to PBC, M-nets and B(PN) models;
and a third that combines the other two.

%package -n texlive-petri-nets-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn39165
Release:        0
Summary:        Documentation for texlive-petri-nets
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-petri-nets-doc
This package includes the documentation for texlive-petri-nets

%post -n texlive-petri-nets
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-petri-nets
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-petri-nets
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-petri-nets-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/petri-nets/COPYING
%{_texmfdistdir}/doc/generic/petri-nets/ChangeLog
%{_texmfdistdir}/doc/generic/petri-nets/README
%{_texmfdistdir}/doc/generic/petri-nets/pndoc.pdf
%{_texmfdistdir}/doc/generic/petri-nets/pndoc.tex

%files -n texlive-petri-nets
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/petri-nets/pn2pdf
%{_texmfdistdir}/tex/generic/petri-nets/pndraw.sty
%{_texmfdistdir}/tex/generic/petri-nets/pndraw.tex
%{_texmfdistdir}/tex/generic/petri-nets/pnets.sty
%{_texmfdistdir}/tex/generic/petri-nets/pnets.tex
%{_texmfdistdir}/tex/generic/petri-nets/pntext.sty
%{_texmfdistdir}/tex/generic/petri-nets/pntext.tex
%{_texmfdistdir}/tex/generic/petri-nets/pnversion.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-petri-nets-%{texlive_version}.%{texlive_noarch}.svn39165-%{release}-zypper
%endif

%package -n texlive-pfarrei
Version:        %{texlive_version}.%{texlive_noarch}.r36svn31934
Release:        0
License:        LPPL-1.0
Summary:        LaTeX support of pastors' and priests' work
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pfarrei-bin >= %{texlive_version}
#!BuildIgnore: texlive-pfarrei-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pfarrei-doc >= %{texlive_version}
Provides:       tex(a5toa4.tex)
Provides:       tex(pfarrei.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(x.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source173:      pfarrei.tar.xz
Source174:      pfarrei.doc.tar.xz

%description -n texlive-pfarrei
In "Die TeXnische Komodie" (issue 1/2013) Christian Justen
described his use of LaTeX in his work as priest (similar
requirements may be encountered in the work of pastors and
other ministers of religion). One point was to arrange A5 pages
onto A4 landscape paper, either side-by-side or as a booklet.
Justen made two bash scripts for this job; the package provides
one texlua script for both requirements. (Note that file
a5toa4.tlu should have execute permissions in any
installation.)

%package -n texlive-pfarrei-doc
Version:        %{texlive_version}.%{texlive_noarch}.r36svn31934
Release:        0
Summary:        Documentation for texlive-pfarrei
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pfarrei-doc:de)

%description -n texlive-pfarrei-doc
This package includes the documentation for texlive-pfarrei

%post -n texlive-pfarrei
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pfarrei
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pfarrei
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pfarrei-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pfarrei/pfarrei.pdf

%files -n texlive-pfarrei
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pfarrei/a5toa4.tlu
%{_texmfdistdir}/scripts/pfarrei/pfarrei.tlu
%{_texmfdistdir}/tex/latex/pfarrei/a5toa4.tex
%{_texmfdistdir}/tex/latex/pfarrei/pfarrei.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pfarrei-%{texlive_version}.%{texlive_noarch}.r36svn31934-%{release}-zypper
%endif

%package -n texlive-pgf
Version:        %{texlive_version}.%{texlive_noarch}.3.1.8bsvn57240
Release:        0
License:        LPPL-1.0
Summary:        Create PostScript and PDF graphics in TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-atveryend >= %{texlive_version}
#!BuildIgnore: texlive-atveryend
Requires:       texlive-fp >= %{texlive_version}
#!BuildIgnore: texlive-fp
Requires:       texlive-graphics >= %{texlive_version}
#!BuildIgnore: texlive-graphics
Requires:       texlive-ms >= %{texlive_version}
#!BuildIgnore: texlive-ms
Requires:       texlive-pdftexcmds >= %{texlive_version}
#!BuildIgnore: texlive-pdftexcmds
Requires:       texlive-xcolor >= %{texlive_version}
#!BuildIgnore: texlive-xcolor
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-doc >= %{texlive_version}
Requires:       tex(atbegshi.sty)
Provides:       tex(pgf.cfg)
Provides:       tex(pgf.revision.tex)
Provides:       tex(pgf.sty)
Provides:       tex(pgf.tex)
Provides:       tex(pgfarrows.sty)
Provides:       tex(pgfautomata.sty)
Provides:       tex(pgfbaseimage.sty)
Provides:       tex(pgfbaseimage.tex)
Provides:       tex(pgfbaselayers.sty)
Provides:       tex(pgfbaselayers.tex)
Provides:       tex(pgfbasematrix.sty)
Provides:       tex(pgfbasematrix.tex)
Provides:       tex(pgfbasepatterns.sty)
Provides:       tex(pgfbasepatterns.tex)
Provides:       tex(pgfbaseplot.sty)
Provides:       tex(pgfbaseplot.tex)
Provides:       tex(pgfbaseshapes.sty)
Provides:       tex(pgfbaseshapes.tex)
Provides:       tex(pgfbasesnakes.sty)
Provides:       tex(pgfbasesnakes.tex)
Provides:       tex(pgfcalendar.code.tex)
Provides:       tex(pgfcalendar.sty)
Provides:       tex(pgfcalendar.tex)
Provides:       tex(pgfcomp-version-0-65.sty)
Provides:       tex(pgfcomp-version-1-18.sty)
Provides:       tex(pgfcore.code.tex)
Provides:       tex(pgfcore.sty)
Provides:       tex(pgfcore.tex)
Provides:       tex(pgfcorearrows.code.tex)
Provides:       tex(pgfcoreexternal.code.tex)
Provides:       tex(pgfcoregraphicstate.code.tex)
Provides:       tex(pgfcoreimage.code.tex)
Provides:       tex(pgfcorelayers.code.tex)
Provides:       tex(pgfcoreobjects.code.tex)
Provides:       tex(pgfcorepathconstruct.code.tex)
Provides:       tex(pgfcorepathprocessing.code.tex)
Provides:       tex(pgfcorepathusage.code.tex)
Provides:       tex(pgfcorepatterns.code.tex)
Provides:       tex(pgfcorepoints.code.tex)
Provides:       tex(pgfcorequick.code.tex)
Provides:       tex(pgfcorerdf.code.tex)
Provides:       tex(pgfcorescopes.code.tex)
Provides:       tex(pgfcoreshade.code.tex)
Provides:       tex(pgfcoretransformations.code.tex)
Provides:       tex(pgfcoretransparency.code.tex)
Provides:       tex(pgfexternal.tex)
Provides:       tex(pgfexternalwithdepth.tex)
Provides:       tex(pgffor.code.tex)
Provides:       tex(pgffor.sty)
Provides:       tex(pgffor.tex)
Provides:       tex(pgfheaps.sty)
Provides:       tex(pgfint.code.tex)
Provides:       tex(pgfkeys.code.tex)
Provides:       tex(pgfkeys.sty)
Provides:       tex(pgfkeys.tex)
Provides:       tex(pgfkeysfiltered.code.tex)
Provides:       tex(pgflibraryarrows.code.tex)
Provides:       tex(pgflibraryarrows.meta.code.tex)
Provides:       tex(pgflibraryarrows.spaced.code.tex)
Provides:       tex(pgflibraryarrows.sty)
Provides:       tex(pgflibraryautomata.sty)
Provides:       tex(pgflibrarycurvilinear.code.tex)
Provides:       tex(pgflibrarydatavisualization.barcharts.code.tex)
Provides:       tex(pgflibrarydatavisualization.formats.functions.code.tex)
Provides:       tex(pgflibrarydatavisualization.polar.code.tex)
Provides:       tex(pgflibrarydecorations.footprints.code.tex)
Provides:       tex(pgflibrarydecorations.fractals.code.tex)
Provides:       tex(pgflibrarydecorations.markings.code.tex)
Provides:       tex(pgflibrarydecorations.pathmorphing.code.tex)
Provides:       tex(pgflibrarydecorations.pathreplacing.code.tex)
Provides:       tex(pgflibrarydecorations.shapes.code.tex)
Provides:       tex(pgflibrarydecorations.text.code.tex)
Provides:       tex(pgflibraryfadings.code.tex)
Provides:       tex(pgflibraryfixedpointarithmetic.code.tex)
Provides:       tex(pgflibraryfpu.code.tex)
Provides:       tex(pgflibrarygraphdrawing.circular.code.tex)
Provides:       tex(pgflibrarygraphdrawing.code.tex)
Provides:       tex(pgflibrarygraphdrawing.examples.code.tex)
Provides:       tex(pgflibrarygraphdrawing.force.code.tex)
Provides:       tex(pgflibrarygraphdrawing.layered.code.tex)
Provides:       tex(pgflibrarygraphdrawing.trees.code.tex)
Provides:       tex(pgflibraryintersections.code.tex)
Provides:       tex(pgflibrarylindenmayersystems.code.tex)
Provides:       tex(pgflibraryluamath.code.tex)
Provides:       tex(pgflibrarypatterns.code.tex)
Provides:       tex(pgflibrarypatterns.meta.code.tex)
Provides:       tex(pgflibraryplothandlers.code.tex)
Provides:       tex(pgflibraryplothandlers.sty)
Provides:       tex(pgflibraryplotmarks.code.tex)
Provides:       tex(pgflibraryplotmarks.sty)
Provides:       tex(pgflibraryprofiler.code.tex)
Provides:       tex(pgflibraryshadings.code.tex)
Provides:       tex(pgflibraryshapes.arrows.code.tex)
Provides:       tex(pgflibraryshapes.callouts.code.tex)
Provides:       tex(pgflibraryshapes.code.tex)
Provides:       tex(pgflibraryshapes.gates.ee.IEC.code.tex)
Provides:       tex(pgflibraryshapes.gates.ee.code.tex)
Provides:       tex(pgflibraryshapes.gates.logic.IEC.code.tex)
Provides:       tex(pgflibraryshapes.gates.logic.US.code.tex)
Provides:       tex(pgflibraryshapes.gates.logic.code.tex)
Provides:       tex(pgflibraryshapes.geometric.code.tex)
Provides:       tex(pgflibraryshapes.misc.code.tex)
Provides:       tex(pgflibraryshapes.multipart.code.tex)
Provides:       tex(pgflibraryshapes.sty)
Provides:       tex(pgflibraryshapes.symbols.code.tex)
Provides:       tex(pgflibrarysnakes.code.tex)
Provides:       tex(pgflibrarysnakes.sty)
Provides:       tex(pgflibrarysvg.path.code.tex)
Provides:       tex(pgflibrarytikzbackgrounds.sty)
Provides:       tex(pgflibrarytikztrees.sty)
Provides:       tex(pgflibrarytimelines.code.tex)
Provides:       tex(pgfmanual-en-macros.tex)
Provides:       tex(pgfmanual.code.tex)
Provides:       tex(pgfmanual.pdflinks.code.tex)
Provides:       tex(pgfmanual.prettyprinter.code.tex)
Provides:       tex(pgfmanual.sty)
Provides:       tex(pgfmath.code.tex)
Provides:       tex(pgfmath.sty)
Provides:       tex(pgfmath.tex)
Provides:       tex(pgfmathcalc.code.tex)
Provides:       tex(pgfmathfloat.code.tex)
Provides:       tex(pgfmathfunctions.base.code.tex)
Provides:       tex(pgfmathfunctions.basic.code.tex)
Provides:       tex(pgfmathfunctions.code.tex)
Provides:       tex(pgfmathfunctions.comparison.code.tex)
Provides:       tex(pgfmathfunctions.integerarithmetics.code.tex)
Provides:       tex(pgfmathfunctions.misc.code.tex)
Provides:       tex(pgfmathfunctions.random.code.tex)
Provides:       tex(pgfmathfunctions.round.code.tex)
Provides:       tex(pgfmathfunctions.trigonometric.code.tex)
Provides:       tex(pgfmathode.code.tex)
Provides:       tex(pgfmathparser.code.tex)
Provides:       tex(pgfmathutil.code.tex)
Provides:       tex(pgfmoduleanimations.code.tex)
Provides:       tex(pgfmodulebending.code.tex)
Provides:       tex(pgfmoduledatavisualization.code.tex)
Provides:       tex(pgfmoduledecorations.code.tex)
Provides:       tex(pgfmodulematrix.code.tex)
Provides:       tex(pgfmodulenonlineartransformations.code.tex)
Provides:       tex(pgfmoduleoo.code.tex)
Provides:       tex(pgfmoduleparser.code.tex)
Provides:       tex(pgfmoduleplot.code.tex)
Provides:       tex(pgfmoduleshapes.code.tex)
Provides:       tex(pgfmodulesnakes.code.tex)
Provides:       tex(pgfmodulesorting.code.tex)
Provides:       tex(pgfnodes.sty)
Provides:       tex(pgfpages.sty)
Provides:       tex(pgfparser.sty)
Provides:       tex(pgfpict2e.sty)
Provides:       tex(pgfrcs.code.tex)
Provides:       tex(pgfrcs.sty)
Provides:       tex(pgfrcs.tex)
Provides:       tex(pgfshade.sty)
Provides:       tex(pgfsys-common-pdf-via-dvi.def)
Provides:       tex(pgfsys-common-pdf.def)
Provides:       tex(pgfsys-common-postscript.def)
Provides:       tex(pgfsys-common-svg.def)
Provides:       tex(pgfsys-dvi.def)
Provides:       tex(pgfsys-dvipdfm.def)
Provides:       tex(pgfsys-dvipdfmx.def)
Provides:       tex(pgfsys-dvips.def)
Provides:       tex(pgfsys-dvisvgm.def)
Provides:       tex(pgfsys-dvisvgm4ht.def)
Provides:       tex(pgfsys-luatex.def)
Provides:       tex(pgfsys-pdftex.def)
Provides:       tex(pgfsys-tex4ht.def)
Provides:       tex(pgfsys-textures.def)
Provides:       tex(pgfsys-vtex.def)
Provides:       tex(pgfsys-xetex.def)
Provides:       tex(pgfsys.code.tex)
Provides:       tex(pgfsys.sty)
Provides:       tex(pgfsys.tex)
Provides:       tex(pgfsysanimations.code.tex)
Provides:       tex(pgfsysprotocol.code.tex)
Provides:       tex(pgfsyssoftpath.code.tex)
Provides:       tex(pgfutil-common-lists.tex)
Provides:       tex(pgfutil-common.tex)
Provides:       tex(pgfutil-context.def)
Provides:       tex(pgfutil-latex.def)
Provides:       tex(pgfutil-plain.def)
Provides:       tex(t-pgf.tex)
Provides:       tex(t-pgfbim.tex)
Provides:       tex(t-pgfbla.tex)
Provides:       tex(t-pgfbma.tex)
Provides:       tex(t-pgfbpl.tex)
Provides:       tex(t-pgfbpt.tex)
Provides:       tex(t-pgfbsh.tex)
Provides:       tex(t-pgfbsn.tex)
Provides:       tex(t-pgfcal.tex)
Provides:       tex(t-pgfcor.tex)
Provides:       tex(t-pgffor.tex)
Provides:       tex(t-pgfkey.tex)
Provides:       tex(t-pgfmat.tex)
Provides:       tex(t-pgfmod.tex)
Provides:       tex(t-pgfrcs.tex)
Provides:       tex(t-pgfsys.tex)
Provides:       tex(t-tikz.tex)
Provides:       tex(tikz.code.tex)
Provides:       tex(tikz.sty)
Provides:       tex(tikz.tex)
Provides:       tex(tikzexternal.sty)
Provides:       tex(tikzexternalshared.code.tex)
Provides:       tex(tikzlibrary3d.code.tex)
Provides:       tex(tikzlibraryangles.code.tex)
Provides:       tex(tikzlibraryanimations.code.tex)
Provides:       tex(tikzlibraryarrows.code.tex)
Provides:       tex(tikzlibraryautomata.code.tex)
Provides:       tex(tikzlibrarybabel.code.tex)
Provides:       tex(tikzlibrarybackgrounds.code.tex)
Provides:       tex(tikzlibrarybending.code.tex)
Provides:       tex(tikzlibrarycalc.code.tex)
Provides:       tex(tikzlibrarycalendar.code.tex)
Provides:       tex(tikzlibrarychains.code.tex)
Provides:       tex(tikzlibrarycircuits.code.tex)
Provides:       tex(tikzlibrarycircuits.ee.IEC.code.tex)
Provides:       tex(tikzlibrarycircuits.ee.code.tex)
Provides:       tex(tikzlibrarycircuits.logic.CDH.code.tex)
Provides:       tex(tikzlibrarycircuits.logic.IEC.code.tex)
Provides:       tex(tikzlibrarycircuits.logic.US.code.tex)
Provides:       tex(tikzlibrarycircuits.logic.code.tex)
Provides:       tex(tikzlibrarydatavisualization.3d.code.tex)
Provides:       tex(tikzlibrarydatavisualization.barcharts.code.tex)
Provides:       tex(tikzlibrarydatavisualization.code.tex)
Provides:       tex(tikzlibrarydatavisualization.formats.functions.code.tex)
Provides:       tex(tikzlibrarydatavisualization.polar.code.tex)
Provides:       tex(tikzlibrarydatavisualization.sparklines.code.tex)
Provides:       tex(tikzlibrarydecorations.code.tex)
Provides:       tex(tikzlibrarydecorations.footprints.code.tex)
Provides:       tex(tikzlibrarydecorations.fractals.code.tex)
Provides:       tex(tikzlibrarydecorations.markings.code.tex)
Provides:       tex(tikzlibrarydecorations.pathmorphing.code.tex)
Provides:       tex(tikzlibrarydecorations.pathreplacing.code.tex)
Provides:       tex(tikzlibrarydecorations.shapes.code.tex)
Provides:       tex(tikzlibrarydecorations.text.code.tex)
Provides:       tex(tikzlibraryer.code.tex)
Provides:       tex(tikzlibraryexternal.code.tex)
Provides:       tex(tikzlibraryfadings.code.tex)
Provides:       tex(tikzlibraryfit.code.tex)
Provides:       tex(tikzlibraryfixedpointarithmetic.code.tex)
Provides:       tex(tikzlibraryfolding.code.tex)
Provides:       tex(tikzlibraryfpu.code.tex)
Provides:       tex(tikzlibrarygraphdrawing.code.tex)
Provides:       tex(tikzlibrarygraphdrawing.evolving.code.tex)
Provides:       tex(tikzlibrarygraphs.code.tex)
Provides:       tex(tikzlibrarygraphs.standard.code.tex)
Provides:       tex(tikzlibraryintersections.code.tex)
Provides:       tex(tikzlibrarylindenmayersystems.code.tex)
Provides:       tex(tikzlibrarymath.code.tex)
Provides:       tex(tikzlibrarymatrix.code.tex)
Provides:       tex(tikzlibrarymindmap.code.tex)
Provides:       tex(tikzlibrarypatterns.code.tex)
Provides:       tex(tikzlibrarypatterns.meta.code.tex)
Provides:       tex(tikzlibraryperspective.code.tex)
Provides:       tex(tikzlibrarypetri.code.tex)
Provides:       tex(tikzlibraryplothandlers.code.tex)
Provides:       tex(tikzlibraryplotmarks.code.tex)
Provides:       tex(tikzlibrarypositioning.code.tex)
Provides:       tex(tikzlibraryquotes.code.tex)
Provides:       tex(tikzlibraryrdf.code.tex)
Provides:       tex(tikzlibraryscopes.code.tex)
Provides:       tex(tikzlibraryshadings.code.tex)
Provides:       tex(tikzlibraryshadows.code.tex)
Provides:       tex(tikzlibraryshapes.arrows.code.tex)
Provides:       tex(tikzlibraryshapes.callouts.code.tex)
Provides:       tex(tikzlibraryshapes.code.tex)
Provides:       tex(tikzlibraryshapes.gates.logic.IEC.code.tex)
Provides:       tex(tikzlibraryshapes.gates.logic.US.code.tex)
Provides:       tex(tikzlibraryshapes.geometric.code.tex)
Provides:       tex(tikzlibraryshapes.misc.code.tex)
Provides:       tex(tikzlibraryshapes.multipart.code.tex)
Provides:       tex(tikzlibraryshapes.symbols.code.tex)
Provides:       tex(tikzlibrarysnakes.code.tex)
Provides:       tex(tikzlibraryspy.code.tex)
Provides:       tex(tikzlibrarysvg.path.code.tex)
Provides:       tex(tikzlibrarythrough.code.tex)
Provides:       tex(tikzlibrarytopaths.code.tex)
Provides:       tex(tikzlibrarytrees.code.tex)
Provides:       tex(tikzlibraryturtle.code.tex)
Provides:       tex(tikzlibraryviews.code.tex)
Provides:       tex(xxcolor.sty)
Requires:       tex(calc.sty)
Requires:       tex(everyshi.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source175:      pgf.tar.xz
Source176:      pgf.doc.tar.xz

%description -n texlive-pgf
PGF is a macro package for creating graphics. It is platform-
and format-independent and works together with the most
important TeX backend drivers, including pdfTeX and dvips. It
comes with a user-friendly syntax layer called TikZ. Its usage
is similar to pstricks and the standard picture environment.
PGF works with plain (pdf-)TeX, (pdf-)LaTeX, and ConTeXt.
Unlike pstricks, it can produce either PostScript or PDF
output.

%package -n texlive-pgf-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1.8bsvn57240
Release:        0
Summary:        Documentation for texlive-pgf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-doc
This package includes the documentation for texlive-pgf

%post -n texlive-pgf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pgf/ChangeLog
%{_texmfdistdir}/doc/generic/pgf/FILES
%{_texmfdistdir}/doc/generic/pgf/INSTALL
%{_texmfdistdir}/doc/generic/pgf/RELEASE_NOTES.md
%{_texmfdistdir}/doc/generic/pgf/description.html
%{_texmfdistdir}/doc/generic/pgf/extract.lua
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo-mask.bb
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo-mask.eps
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo-mask.jpg
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.bb
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.eps
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.25.jpg
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.bb
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.eps
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.jpg
%{_texmfdistdir}/doc/generic/pgf/images/brave-gnu-world-logo.xbb
%{_texmfdistdir}/doc/generic/pgf/images/pgfmanual-mindmap-1.pdf
%{_texmfdistdir}/doc/generic/pgf/images/pgfmanual-mindmap-2.pdf
%{_texmfdistdir}/doc/generic/pgf/licenses/LICENSE
%{_texmfdistdir}/doc/generic/pgf/licenses/gnu-free-documentation-license-1.2.txt
%{_texmfdistdir}/doc/generic/pgf/licenses/gnu-public-license-2.txt
%{_texmfdistdir}/doc/generic/pgf/licenses/latex-project-public-license-1.3c.txt
%{_texmfdistdir}/doc/generic/pgf/licenses/manifest-code.txt
%{_texmfdistdir}/doc/generic/pgf/licenses/manifest-documentation.txt
%{_texmfdistdir}/doc/generic/pgf/pgfmanual.pdf
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-actions.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-animations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-arrows.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-decorations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-design.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-external.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-images.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-internalregisters.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-layers.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-matrices.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-nodes.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-paths.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-patterns.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-plots.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-points.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-quick.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-scopes.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-shadings.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-transformations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-base-transparency.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-drivers.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-axes.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-backend.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-examples.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-formats.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-introduction.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-main.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-polar.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-stylesheets.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-dv-visualizers.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-algorithm-layer.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-algorithms-in-c.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-binding-layer.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-circular.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-display-layer.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-edge-routing.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-examples.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-force.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-layered.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-misc.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-ogdf.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-overview.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-phylogenetics.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-trees.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-usage-pgf.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-gd-usage-tikz.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-guidelines.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-installation.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-introduction.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-3d.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-angles.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-arrows.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-automata.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-babel.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-backgrounds.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-calc.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-calendar.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-chains.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-circuits.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-decorations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-edges.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-er.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-external.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fadings.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fit.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fixedpoint.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-folding.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-fpu.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-lsystems.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-math.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-matrices.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-mindmaps.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-patterns.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-perspective.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-petri.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-plot-handlers.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-plot-marks.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-profiler.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-rdf.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-shadings.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-shadows.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-shapes.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-spy.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-svg-path.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-through.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-trees.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-turtle.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-library-views.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-license.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-main-body.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-main-preamble.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-main.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-algorithms.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-commands.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-design.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-numberprinting.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-math-parsing.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-module-parser.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-oo.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pages.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfcalendar.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgffor.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfkeys.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfkeysfiltered.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-animations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-commands.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-overview.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-paths.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-pgfsys-protocol.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-actions.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-animations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-arrows.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-coordinates.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-decorations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-design.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-graphs.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-matrices.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-paths.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-pics.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-plots.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-scopes.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-shapes.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-transformations.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-transparency.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tikz-trees.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-Euclid.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-chains.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-map.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial-nodes.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-tutorial.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/pgfmanual-en-xxcolor.tex
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/text-en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-parametric-example-cut.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfm/pgfmanual-dvipdfm.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/pgfmanual-test.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-parametric-example-cut.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-parametric-example-cut.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvipdfmx/pgfmanual-dvipdfmx.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/pgfmanual-test.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-parametric-example-cut.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvips/pgfmanual-dvips.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/color.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/pgfmanual-test.html
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/pgfmanual-test.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/pgfmanual.html
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-parametric-example-cut.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-dvisvgm/pgfmanual-dvisvgm.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/pgfmanual-test.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-parametric-example-cut.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-parametric-example-cut.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-luatex/pgfmanual-luatex.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-parametric-example-cut.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-pdftex/pgfmanual-pdftex.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-tex4ht/pgfmanual-tex4ht.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-vtex/pgfmanual-vtex.cfg
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/Makefile
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/pgfmanual.tex
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-asymptotic-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-asymptotic-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-exp.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-exp.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-parametric-example-cut.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-parametric-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-parametric-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-sin.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-sin.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-tan-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-tan-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-x.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgf-x.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgfmanual-sine.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgfmanual-sine.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgfplotgnuplot-example.gnuplot
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/en/plots/pgfplotgnuplot-example.table
%{_texmfdistdir}/doc/generic/pgf/version-for-xetex/pgfmanual-xetex.cfg

%files -n texlive-pgf
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pgf/Makefile.pgf_release
%{_texmfdistdir}/scripts/pgf/pgfrevisionfile.sh
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgf.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbim.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbla.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbma.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbpl.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbpt.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbsh.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfbsn.tex
%{_texmfdistdir}/tex/context/third/pgf/basiclayer/t-pgfcor.tex
%{_texmfdistdir}/tex/context/third/pgf/frontendlayer/t-tikz.tex
%{_texmfdistdir}/tex/context/third/pgf/math/t-pgfmat.tex
%{_texmfdistdir}/tex/context/third/pgf/systemlayer/t-pgfsys.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfcal.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgffor.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfkey.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfmod.tex
%{_texmfdistdir}/tex/context/third/pgf/utilities/t-pgfrcs.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcore.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorearrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreexternal.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoregraphicstate.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreimage.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorelayers.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreobjects.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepathconstruct.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepathprocessing.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepathusage.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepatterns.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorepoints.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorequick.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorerdf.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcorescopes.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoreshade.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoretransformations.code.tex
%{_texmfdistdir}/tex/generic/pgf/basiclayer/pgfcoretransparency.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.ee.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.CDH.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.US.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/circuits/tikzlibrarycircuits.logic.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.3d.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.barcharts.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.formats.functions.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.polar.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/datavisualization/tikzlibrarydatavisualization.sparklines.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/graphs/tikzlibrarygraphs.standard.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzexternalshared.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrary3d.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryangles.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryanimations.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryarrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryautomata.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybabel.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybackgrounds.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarybending.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalc.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarycalendar.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarychains.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.footprints.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.fractals.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.markings.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathmorphing.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.pathreplacing.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.shapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarydecorations.text.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryer.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfit.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfixedpointarithmetic.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfolding.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryfpu.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryintersections.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarylindenmayersystems.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymath.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymatrix.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarymindmap.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypatterns.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypatterns.meta.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryperspective.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypetri.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryplotmarks.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarypositioning.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryquotes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryrdf.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryscopes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshadows.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.arrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.callouts.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.gates.logic.US.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.geometric.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.misc.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.multipart.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryshapes.symbols.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysnakes.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryspy.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarysvg.path.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarythrough.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytopaths.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibrarytrees.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryturtle.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/libraries/tikzlibraryviews.code.tex
%{_texmfdistdir}/tex/generic/pgf/frontendlayer/tikz/tikz.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/LUA_CODING_STYLE
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings/Binding.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/bindings/BindingToPGF.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/Tantau2012.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/doc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/circular/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Anchoring.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentAlign.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentDirection.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentDistance.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/ComponentOrder.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Components.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Distances.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/FineTune.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/LayoutPipeline.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/NodeAnchors.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Orientation.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/Sublayouts.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/doc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/control/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Cluster.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Edge.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Graph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Iterators.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Node.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/deprecated/Vector.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/FMMMLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/FastMultipoleEmbedder.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/GEMLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/MultilevelLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderFR.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderFRExact.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/SpringEmbedderKK.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/BarycenterPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/CirclePlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/EdgeCoverMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/IndependentSetMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/LocalBiconnectedMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/MatchingMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/MedianPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/RandomMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/RandomPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/SolarMerger.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/SolarPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/energybased/multilevelmixer/ZeroPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/BarycenterHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/CoffmanGrahamRanking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/DfsAcyclicSubgraph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/FastHierarchyLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/FastSimpleHierarchyLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/GreedyCycleRemoval.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/GreedyInsertHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/LongestPathRanking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/MedianHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/OptimalRanking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SiftingHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SplitHeuristic.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/layered/SugiyamaLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout/BalloonLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/misclayout/CircularLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/AcyclicSubgraphModule.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/HierarchyLayoutModule.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/InitialPlacer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/MultilevelBuilder.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/RankingModule.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/module/TwoLayerCrossMin.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/planarity.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/doc/ogdf/planarity/PlanarizationLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/ASCIIDisplayer.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/BindingToASCII.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleDemo.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleEdgeDemo.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/SimpleHuffman.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/example_graph_for_ascii_displayer.txt
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/examples/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/GraphAnimationCoordination.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/GreedyTemporalCycleRemoval.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/Skambath2016.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/Supergraph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/SupergraphVertexSplitOptimization.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/TimeSpec.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/doc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/layered.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/experimental/evolving/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/CoarseGraph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlCoarsening.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlDeclare.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlElectric.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlIteration.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlSprings.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/ControlStart.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/QuadTree.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalHu2006.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalLayouts.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringElectricalWalshaw2000.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringHu2006.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/SpringLayouts.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/FruchtermanReingold.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/HuSpringElectricalFW.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/SimpleSpring.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/SocialGravityCloseness.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/algorithms/SocialGravityDegree.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/CoarseGraphFW.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/ForceController.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/ForceTemplate.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/InitialTemplate.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/PathLengthsFW.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/base/Preprocessing.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/doc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceAbsoluteValue.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceCanvasDistance.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceCanvasPosition.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForceGraphDistance.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForcePullToGrid.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/forcetypes/ForcePullToPoint.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/initialpositioning/CircularInitialPositioning.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/initialpositioning/GridInitialPositioning.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/initialpositioning/RandomInitialPositioning.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/jedi/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/force/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceCore.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToAlgorithms.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToC.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/InterfaceToDisplay.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/interface/Scope.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CrossingMinimizationGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalBergerS1990a.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalBergerS1990b.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalEadesLS1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/CycleRemovalGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/EdgeRoutingGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NetworkSimplex.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodePositioningGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodeRankingGansnerKNV1993.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/NodeRankingMinimumHeight.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/Ranking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/Sugiyama.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/crossing_minimization.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/cycle_removal.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/edge_routing.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/node_positioning.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/layered/node_ranking.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Bezier.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/DepthFirstSearch.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Direct.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Event.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/LookupTable.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/PathLengths.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/PriorityQueue.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Simplifiers.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Stack.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Storage.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/lib/Transform.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Arc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Collection.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Coordinate.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Digraph.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Edge.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Hyperedge.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Path.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Path_arced.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/Vertex.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/model/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/ogdf.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/ogdf/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/pedigrees.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/pedigrees/Koerner2015.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/pedigrees/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/AuthorDefinedPhylogeny.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/BalancedMinimumEvolution.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/BalancedNearestNeighbourInterchange.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/DistanceMatrix.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/Maeusle2012.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/PhylogeneticTree.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/SokalMichener1958.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/phylogenetics/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/BoyerMyrvold2004.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/Embedding.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/LinkedList.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/List.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/PDP.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/PlanarLayout.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/ShiftMethod.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/planar/parameters.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing/Hints.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing/NecklaceRouting.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/routing/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/tools/make_gd_wrap.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/ChildSpec.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/ReingoldTilford1981.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/SpanningTreeComputation.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/doc.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/lua/pgf/gd/trees/library.lua
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/experimental/tikzlibrarygraphdrawing.evolving.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.circular.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.examples.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.force.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.layered.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/pgflibrarygraphdrawing.trees.code.tex
%{_texmfdistdir}/tex/generic/pgf/graphdrawing/tex/tikzlibrarygraphdrawing.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.barcharts.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.formats.functions.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/datavisualization/pgflibrarydatavisualization.polar.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.footprints.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.fractals.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.markings.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathmorphing.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.pathreplacing.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.shapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/decorations/pgflibrarydecorations.text.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/luamath/pgf/luamath/functions.lua
%{_texmfdistdir}/tex/generic/pgf/libraries/luamath/pgf/luamath/parser.lua
%{_texmfdistdir}/tex/generic/pgf/libraries/luamath/pgflibraryluamath.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryarrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryarrows.meta.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryarrows.spaced.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarycurvilinear.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryfadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryfixedpointarithmetic.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryfpu.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryintersections.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarylindenmayersystems.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarypatterns.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarypatterns.meta.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryplotmarks.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryprofiler.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibraryshadings.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarysnakes.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarysvg.path.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/pgflibrarytimelines.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.ee.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.IEC.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.US.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/circuits/pgflibraryshapes.gates.logic.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.arrows.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.callouts.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.geometric.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.misc.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.multipart.code.tex
%{_texmfdistdir}/tex/generic/pgf/libraries/shapes/pgflibraryshapes.symbols.code.tex
%{_texmfdistdir}/tex/generic/pgf/lua/pgf/manual.lua
%{_texmfdistdir}/tex/generic/pgf/lua/pgf/manual/DocumentParser.lua
%{_texmfdistdir}/tex/generic/pgf/math/pgfint.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmath.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathcalc.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfloat.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.base.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.basic.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.comparison.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.integerarithmetics.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.misc.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.random.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.round.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathfunctions.trigonometric.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathode.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathparser.code.tex
%{_texmfdistdir}/tex/generic/pgf/math/pgfmathutil.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleanimations.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulebending.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduledatavisualization.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduledecorations.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulematrix.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulenonlineartransformations.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleoo.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleparser.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleplot.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmoduleshapes.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulesnakes.code.tex
%{_texmfdistdir}/tex/generic/pgf/modules/pgfmodulesorting.code.tex
%{_texmfdistdir}/tex/generic/pgf/pgf.revision.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgf.cfg
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-pdf-via-dvi.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-pdf.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-postscript.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-common-svg.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvi.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvipdfm.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvipdfmx.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvips.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvisvgm.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-dvisvgm4ht.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-luatex.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-pdftex.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-tex4ht.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-textures.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-vtex.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys-xetex.def
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsys.code.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsysanimations.code.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsysprotocol.code.tex
%{_texmfdistdir}/tex/generic/pgf/systemlayer/pgfsyssoftpath.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfcalendar.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfexternal.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfexternalwithdepth.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgffor.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfkeys.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfkeysfiltered.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfrcs.code.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-common-lists.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-common.tex
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-context.def
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-latex.def
%{_texmfdistdir}/tex/generic/pgf/utilities/pgfutil-plain.def
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgf.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaseimage.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaselayers.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbasematrix.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbasepatterns.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaseplot.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbaseshapes.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfbasesnakes.sty
%{_texmfdistdir}/tex/latex/pgf/basiclayer/pgfcore.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfarrows.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfautomata.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfcomp-version-0-65.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfcomp-version-1-18.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfheaps.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryarrows.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryautomata.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryplothandlers.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryplotmarks.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibraryshapes.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibrarysnakes.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibrarytikzbackgrounds.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgflibrarytikztrees.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfnodes.sty
%{_texmfdistdir}/tex/latex/pgf/compatibility/pgfshade.sty
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual-en-macros.tex
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.code.tex
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.pdflinks.code.tex
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.prettyprinter.code.tex
%{_texmfdistdir}/tex/latex/pgf/doc/pgfmanual.sty
%{_texmfdistdir}/tex/latex/pgf/frontendlayer/libraries/tikzlibraryexternal.code.tex
%{_texmfdistdir}/tex/latex/pgf/frontendlayer/pgfpict2e.sty
%{_texmfdistdir}/tex/latex/pgf/frontendlayer/tikz.sty
%{_texmfdistdir}/tex/latex/pgf/math/pgfmath.sty
%{_texmfdistdir}/tex/latex/pgf/systemlayer/pgfsys.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfcalendar.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgffor.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfkeys.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfpages.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfparser.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/pgfrcs.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/tikzexternal.sty
%{_texmfdistdir}/tex/latex/pgf/utilities/xxcolor.sty
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgf.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaseimage.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaselayers.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbasematrix.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbasepatterns.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaseplot.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbaseshapes.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfbasesnakes.tex
%{_texmfdistdir}/tex/plain/pgf/basiclayer/pgfcore.tex
%{_texmfdistdir}/tex/plain/pgf/frontendlayer/tikz.tex
%{_texmfdistdir}/tex/plain/pgf/math/pgfmath.tex
%{_texmfdistdir}/tex/plain/pgf/systemlayer/pgfsys.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgfcalendar.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgffor.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgfkeys.tex
%{_texmfdistdir}/tex/plain/pgf/utilities/pgfrcs.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-%{texlive_version}.%{texlive_noarch}.3.1.8bsvn57240-%{release}-zypper
%endif

%package -n texlive-pgf-blur
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn54512
Release:        0
License:        LPPL-1.0
Summary:        PGF/TikZ package for "blurred" shadows
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-blur-doc >= %{texlive_version}
Provides:       tex(tikzlibraryshadows.blur.code.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source177:      pgf-blur.tar.xz
Source178:      pgf-blur.doc.tar.xz

%description -n texlive-pgf-blur
The package adds blurred/faded/fuzzy shadows to PGF/TikZ
pictures. It is configured as a TikZ/PGF library module. The
method is similar to that of the author's pst-blur package for
PSTricks.

%package -n texlive-pgf-blur-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn54512
Release:        0
Summary:        Documentation for texlive-pgf-blur
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-blur-doc
This package includes the documentation for texlive-pgf-blur

%post -n texlive-pgf-blur
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf-blur
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf-blur
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-blur-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgf-blur/README.md
%{_texmfdistdir}/doc/latex/pgf-blur/pgf-blur.pdf

%files -n texlive-pgf-blur
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgf-blur/tikzlibraryshadows.blur.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-blur-%{texlive_version}.%{texlive_noarch}.1.02svn54512-%{release}-zypper
%endif

%package -n texlive-pgf-cmykshadings
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn52635
Release:        0
License:        LPPL-1.0
Summary:        Support for CMYK and grayscale shadings in PGF/TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-cmykshadings-doc >= %{texlive_version}
Provides:       tex(pgf-cmykshadings.sty)
Provides:       tex(pgfsys-cmykshadings-common-postscript.def)
Provides:       tex(pgfsys-cmykshadings-dvipdfm.def)
Provides:       tex(pgfsys-cmykshadings-dvipdfmx.def)
Provides:       tex(pgfsys-cmykshadings-dvips.def)
Provides:       tex(pgfsys-cmykshadings-luatex.def)
Provides:       tex(pgfsys-cmykshadings-pdftex.def)
Provides:       tex(pgfsys-cmykshadings-textures.def)
Provides:       tex(pgfsys-cmykshadings-vtex.def)
Provides:       tex(pgfsys-cmykshadings-xetex.def)
Requires:       tex(pgf.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source179:      pgf-cmykshadings.tar.xz
Source180:      pgf-cmykshadings.doc.tar.xz

%description -n texlive-pgf-cmykshadings
This package provides support for CMYK and grayscale shadings
for the pgf package. By default pgf only supports RGB shadings.
The package attempts to produce shadings consistent with the
currently selected xcolor colour model. The rgb, cmyk, and gray
colour models from the xcolor package are supported. Note: This
package is deprecated since pgf version 3.1.3, since CMYK and
grayscale shadings are now directly supported.

%package -n texlive-pgf-cmykshadings-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn52635
Release:        0
Summary:        Documentation for texlive-pgf-cmykshadings
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-cmykshadings-doc
This package includes the documentation for texlive-pgf-cmykshadings

%post -n texlive-pgf-cmykshadings
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf-cmykshadings
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf-cmykshadings
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-cmykshadings-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgf-cmykshadings/README.md
%{_texmfdistdir}/doc/latex/pgf-cmykshadings/pgf-cmykshadings.pdf

%files -n texlive-pgf-cmykshadings
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgf-cmykshadings.sty
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-common-postscript.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-dvipdfm.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-dvipdfmx.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-dvips.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-luatex.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-pdftex.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-textures.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-vtex.def
%{_texmfdistdir}/tex/latex/pgf-cmykshadings/pgfsys-cmykshadings-xetex.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-cmykshadings-%{texlive_version}.%{texlive_noarch}.1.2svn52635-%{release}-zypper
%endif

%package -n texlive-pgf-pie
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn55342
Release:        0
License:        GPL-2.0-or-later
Summary:        Draw pie charts, using PGF
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-carlisle >= %{texlive_version}
#!BuildIgnore: texlive-carlisle
Requires:       texlive-latex >= %{texlive_version}
#!BuildIgnore: texlive-latex
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-pie-doc >= %{texlive_version}
Provides:       tex(pgf-pie.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(scalefnt.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source181:      pgf-pie.tar.xz
Source182:      pgf-pie.doc.tar.xz

%description -n texlive-pgf-pie
The package provides the means to draw pie (and variant)
charts, using PGF/TikZ. The license of the package is MIT as
mentioned here: https://code.google.com/archive/p/pgf-pie/.

%package -n texlive-pgf-pie-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn55342
Release:        0
Summary:        Documentation for texlive-pgf-pie
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-pie-doc
This package includes the documentation for texlive-pgf-pie

%post -n texlive-pgf-pie
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf-pie
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf-pie
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-pie-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgf-pie/COPYING
%{_texmfdistdir}/doc/latex/pgf-pie/LICENSE-GPL2.txt
%{_texmfdistdir}/doc/latex/pgf-pie/LICENSE-LPPL1.3c.txt
%{_texmfdistdir}/doc/latex/pgf-pie/README
%{_texmfdistdir}/doc/latex/pgf-pie/before-after-number.tex
%{_texmfdistdir}/doc/latex/pgf-pie/cloud.svg
%{_texmfdistdir}/doc/latex/pgf-pie/cloud.tex
%{_texmfdistdir}/doc/latex/pgf-pie/color.tex
%{_texmfdistdir}/doc/latex/pgf-pie/colorwheel.tex
%{_texmfdistdir}/doc/latex/pgf-pie/explode.tex
%{_texmfdistdir}/doc/latex/pgf-pie/first-pie.svg
%{_texmfdistdir}/doc/latex/pgf-pie/first-pie.tex
%{_texmfdistdir}/doc/latex/pgf-pie/hide-number.tex
%{_texmfdistdir}/doc/latex/pgf-pie/legend.tex
%{_texmfdistdir}/doc/latex/pgf-pie/logo.png
%{_texmfdistdir}/doc/latex/pgf-pie/pgf-pie-manual.pdf
%{_texmfdistdir}/doc/latex/pgf-pie/pgf-pie-manual.tex
%{_texmfdistdir}/doc/latex/pgf-pie/polar.svg
%{_texmfdistdir}/doc/latex/pgf-pie/polar.tex
%{_texmfdistdir}/doc/latex/pgf-pie/population.tex
%{_texmfdistdir}/doc/latex/pgf-pie/radius.tex
%{_texmfdistdir}/doc/latex/pgf-pie/scalefont.tex
%{_texmfdistdir}/doc/latex/pgf-pie/shadow.tex
%{_texmfdistdir}/doc/latex/pgf-pie/square.svg
%{_texmfdistdir}/doc/latex/pgf-pie/square.tex
%{_texmfdistdir}/doc/latex/pgf-pie/sum.tex
%{_texmfdistdir}/doc/latex/pgf-pie/text-inside.tex
%{_texmfdistdir}/doc/latex/pgf-pie/text.tex

%files -n texlive-pgf-pie
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgf-pie/pgf-pie.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-pie-%{texlive_version}.%{texlive_noarch}.0.0.3svn55342-%{release}-zypper
%endif

%package -n texlive-pgf-soroban
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32269
Release:        0
License:        LPPL-1.0
Summary:        Create images of the soroban using TikZ/PGF
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-soroban-doc >= %{texlive_version}
Provides:       tex(pgf-soroban.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source183:      pgf-soroban.tar.xz
Source184:      pgf-soroban.doc.tar.xz

%description -n texlive-pgf-soroban
The package makes it possible to create pictures of the soroban
(Japanese abacus) using PGF/TikZ

%package -n texlive-pgf-soroban-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32269
Release:        0
Summary:        Documentation for texlive-pgf-soroban
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-soroban-doc
This package includes the documentation for texlive-pgf-soroban

%post -n texlive-pgf-soroban
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf-soroban
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf-soroban
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-soroban-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgf-soroban/Changes
%{_texmfdistdir}/doc/latex/pgf-soroban/README
%{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.bib
%{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.pdf
%{_texmfdistdir}/doc/latex/pgf-soroban/pgf-soroban-doc.tex

%files -n texlive-pgf-soroban
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgf-soroban/pgf-soroban.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-soroban-%{texlive_version}.%{texlive_noarch}.1.1svn32269-%{release}-zypper
%endif

%package -n texlive-pgf-spectra
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn58467
Release:        0
License:        LPPL-1.0
Summary:        Draw continuous or discrete spectra using PGF/TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-spectra-doc >= %{texlive_version}
Provides:       tex(pgf-spectra.sty)
Provides:       tex(spectra.data.LSE.tex)
Provides:       tex(spectra.data.NIST.tex)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source185:      pgf-spectra.tar.xz
Source186:      pgf-spectra.doc.tar.xz

%description -n texlive-pgf-spectra
The purpose of this package is to draw the spectra of elements
in a simple way. It is based on the package pst-spectra,
supporting the same options, but also adding some new options.
It relies on PGF/TikZ for drawing the desired spectrum,
continuous or discrete. As in pst-spectra, there are data
available for the spectra of 99 elements and their ions (from
the NASA database). It also allows the user to draw spectra
using their own data.

%package -n texlive-pgf-spectra-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn58467
Release:        0
Summary:        Documentation for texlive-pgf-spectra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-spectra-doc
This package includes the documentation for texlive-pgf-spectra

%post -n texlive-pgf-spectra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf-spectra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf-spectra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-spectra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgf-spectra/README
%{_texmfdistdir}/doc/latex/pgf-spectra/pgf-spectraDataLSE.pdf
%{_texmfdistdir}/doc/latex/pgf-spectra/pgf-spectraDataNIST.pdf
%{_texmfdistdir}/doc/latex/pgf-spectra/pgf-spectraManual.pdf

%files -n texlive-pgf-spectra
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgf-spectra/pgf-spectra.sty
%{_texmfdistdir}/tex/latex/pgf-spectra/spectra.data.LSE.tex
%{_texmfdistdir}/tex/latex/pgf-spectra/spectra.data.NIST.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-spectra-%{texlive_version}.%{texlive_noarch}.2.0.0svn58467-%{release}-zypper
%endif

%package -n texlive-pgf-umlcd
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.1.1svn55342
Release:        0
License:        GPL-2.0-or-later
Summary:        Some LaTeX macros for UML Class Diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-latex >= %{texlive_version}
#!BuildIgnore: texlive-latex
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-umlcd-doc >= %{texlive_version}
Provides:       tex(pgf-umlcd.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source187:      pgf-umlcd.tar.xz
Source188:      pgf-umlcd.doc.tar.xz

%description -n texlive-pgf-umlcd
Some LaTeX macros for UML Class Diagrams.pgf

%package -n texlive-pgf-umlcd-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.1.1svn55342
Release:        0
Summary:        Documentation for texlive-pgf-umlcd
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-umlcd-doc
This package includes the documentation for texlive-pgf-umlcd

%post -n texlive-pgf-umlcd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf-umlcd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf-umlcd
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-umlcd-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgf-umlcd/COPYING
%{_texmfdistdir}/doc/latex/pgf-umlcd/README
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/abstract-class.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/abstract-factory.svg
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/abstract-factory.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/aggregation.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/association.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/class.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/composition.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/implement-interface.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/inheritance.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/interface.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/note.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/object-include-methods.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/object.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/package.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/unidirectional-association.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/demo/visibility.tex
%{_texmfdistdir}/doc/latex/pgf-umlcd/logo.png
%{_texmfdistdir}/doc/latex/pgf-umlcd/pgf-umlcd-manual.pdf
%{_texmfdistdir}/doc/latex/pgf-umlcd/pgf-umlcd-manual.tex

%files -n texlive-pgf-umlcd
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgf-umlcd/pgf-umlcd.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-umlcd-%{texlive_version}.%{texlive_noarch}.0.0.2.1.1svn55342-%{release}-zypper
%endif

%package -n texlive-pgf-umlsd
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn55342
Release:        0
License:        GPL-2.0-or-later
Summary:        Draw UML Sequence Diagrams
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-latex >= %{texlive_version}
#!BuildIgnore: texlive-latex
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgf-umlsd-doc >= %{texlive_version}
Provides:       tex(pgf-umlsd.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source189:      pgf-umlsd.tar.xz
Source190:      pgf-umlsd.doc.tar.xz

%description -n texlive-pgf-umlsd
LaTeX macros to draw UML diagrams using pgf

%package -n texlive-pgf-umlsd-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn55342
Release:        0
Summary:        Documentation for texlive-pgf-umlsd
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgf-umlsd-doc
This package includes the documentation for texlive-pgf-umlsd

%post -n texlive-pgf-umlsd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgf-umlsd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgf-umlsd
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgf-umlsd-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgf-umlsd/README
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/block.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/call.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/callself.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/customize.log
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/customize.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/distance.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/empty.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/instance.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/message.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/messcall.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/multi-threads-example.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/nested-call.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/no-thread-example.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/non-instantaneous-message.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/postlevel.log
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/postlevel.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/prelevel.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/single-thread-example.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/sync-clock.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/thread.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/threadbias.log
%{_texmfdistdir}/doc/latex/pgf-umlsd/demo/threadbias.tex
%{_texmfdistdir}/doc/latex/pgf-umlsd/diagrams.pdf
%{_texmfdistdir}/doc/latex/pgf-umlsd/logo.png
%{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-manual.pdf
%{_texmfdistdir}/doc/latex/pgf-umlsd/pgf-umlsd-manual.tex

%files -n texlive-pgf-umlsd
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgf-umlsd/pgf-umlsd.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgf-umlsd-%{texlive_version}.%{texlive_noarch}.0.0.7svn55342-%{release}-zypper
%endif

%package -n texlive-pgfgantt
Version:        %{texlive_version}.%{texlive_noarch}.5.0svn52662
Release:        0
License:        LPPL-1.0
Summary:        Draw Gantt charts with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfgantt-doc >= %{texlive_version}
Provides:       tex(pgfgantt.sty)
Requires:       tex(pgfcalendar.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source191:      pgfgantt.tar.xz
Source192:      pgfgantt.doc.tar.xz

%description -n texlive-pgfgantt
The package provides an environment for drawing Gantt charts
that contain various elements (titles, bars, milestones, groups
and links). Several keys customize the appearance of the chart
elements.

%package -n texlive-pgfgantt-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.0svn52662
Release:        0
Summary:        Documentation for texlive-pgfgantt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgfgantt-doc
This package includes the documentation for texlive-pgfgantt

%post -n texlive-pgfgantt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfgantt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfgantt
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfgantt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgfgantt/README
%{_texmfdistdir}/doc/latex/pgfgantt/pgfgantt.pdf

%files -n texlive-pgfgantt
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgfgantt/pgfgantt.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfgantt-%{texlive_version}.%{texlive_noarch}.5.0svn52662-%{release}-zypper
%endif

%package -n texlive-pgfkeyx
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.1svn26093
Release:        0
License:        LPPL-1.0
Summary:        Extended and more robust version of pgfkeys
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfkeyx-doc >= %{texlive_version}
Provides:       tex(pgfkeyx.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source193:      pgfkeyx.tar.xz
Source194:      pgfkeyx.doc.tar.xz

%description -n texlive-pgfkeyx
The package extends and improves the robustness of the pgfkeys
package. In particular, it can deal with active comma, equality
sign, and slash in key parsing. The difficulty with active
characters has long been a problem with the pgfkeys package.
The package also introduces handlers beyond those that pgfkeys
can offer.

%package -n texlive-pgfkeyx-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.1svn26093
Release:        0
Summary:        Documentation for texlive-pgfkeyx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgfkeyx-doc
This package includes the documentation for texlive-pgfkeyx

%post -n texlive-pgfkeyx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfkeyx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfkeyx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfkeyx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgfkeyx/README
%{_texmfdistdir}/doc/latex/pgfkeyx/pgfkeyx-test1.tex

%files -n texlive-pgfkeyx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgfkeyx/pgfkeyx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfkeyx-%{texlive_version}.%{texlive_noarch}.0.0.0.1svn26093-%{release}-zypper
%endif

%package -n texlive-pgfmolbio
Version:        %{texlive_version}.%{texlive_noarch}.0.0.21svn35152
Release:        0
License:        LPPL-1.0
Summary:        Draw graphs typically found in molecular biology texts
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfmolbio-doc >= %{texlive_version}
Provides:       tex(pgfmolbio.chromatogram.tex)
Provides:       tex(pgfmolbio.convert.tex)
Provides:       tex(pgfmolbio.domains.tex)
Provides:       tex(pgfmolbio.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(luatexbase-modutils.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source195:      pgfmolbio.tar.xz
Source196:      pgfmolbio.doc.tar.xz

%description -n texlive-pgfmolbio
The package draws graphs typically found in molecular biology
texts. Currently, the package contains modules for drawing DNA
sequencing chromatograms and protein domain diagrams.

%package -n texlive-pgfmolbio-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.21svn35152
Release:        0
Summary:        Documentation for texlive-pgfmolbio
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgfmolbio-doc
This package includes the documentation for texlive-pgfmolbio

%post -n texlive-pgfmolbio
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfmolbio
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfmolbio
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfmolbio-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/pgfmolbio/README
%{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleGff.gff
%{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleScf.scf
%{_texmfdistdir}/doc/lualatex/pgfmolbio/SampleUniprot.txt
%{_texmfdistdir}/doc/lualatex/pgfmolbio/pgfmolbio.pdf

%files -n texlive-pgfmolbio
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pgfmolbio/pgfmolbio.lua
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.chromatogram.lua
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.chromatogram.tex
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.convert.tex
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.domains.lua
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.domains.tex
%{_texmfdistdir}/tex/lualatex/pgfmolbio/pgfmolbio.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfmolbio-%{texlive_version}.%{texlive_noarch}.0.0.21svn35152-%{release}-zypper
%endif

%package -n texlive-pgfmorepages
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn54770
Release:        0
License:        LPPL-1.0
Summary:        Assemble multiple logical pages onto a physical page
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfmorepages-doc >= %{texlive_version}
Provides:       tex(pgfmorepages.sty)
Provides:       tex(pgfmorepageslayouts.code.tex)
Requires:       tex(calc.sty)
Requires:       tex(pgfcore.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source197:      pgfmorepages.tar.xz
Source198:      pgfmorepages.doc.tar.xz

%description -n texlive-pgfmorepages
This package replaces and extends the pgfpages sub-package of
the PGF system. It provides the capability to arrange multiple
"logical" pages on multiple "physical" pages, for example as
for arranging pages to make booklets.

%package -n texlive-pgfmorepages-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn54770
Release:        0
Summary:        Documentation for texlive-pgfmorepages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgfmorepages-doc
This package includes the documentation for texlive-pgfmorepages

%post -n texlive-pgfmorepages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfmorepages
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfmorepages
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfmorepages-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgfmorepages/README
%{_texmfdistdir}/doc/latex/pgfmorepages/pgfmorepages.pdf
%{_texmfdistdir}/doc/latex/pgfmorepages/pgfmorepages.tex

%files -n texlive-pgfmorepages
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgfmorepages/pgfmorepages.sty
%{_texmfdistdir}/tex/latex/pgfmorepages/pgfmorepageslayouts.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfmorepages-%{texlive_version}.%{texlive_noarch}.1.20svn54770-%{release}-zypper
%endif

%package -n texlive-pgfopts
Version:        %{texlive_version}.%{texlive_noarch}.2.1asvn56615
Release:        0
License:        LPPL-1.0
Summary:        LaTeX package options with pgfkeys
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfopts-doc >= %{texlive_version}
Provides:       tex(pgfopts.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source199:      pgfopts.tar.xz
Source200:      pgfopts.doc.tar.xz

%description -n texlive-pgfopts
The pgfkeys package (part of the pgf distribution) is a
well-designed way of defining and using large numbers of keys
for key-value syntaxes. However, pgfkeys itself does not offer
means of handling LaTeX class and package options. This package
adds such option handling to pgfkeys, in the same way that
kvoptions adds the same facility to the LaTeX standard keyval
package.

%package -n texlive-pgfopts-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1asvn56615
Release:        0
Summary:        Documentation for texlive-pgfopts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgfopts-doc
This package includes the documentation for texlive-pgfopts

%post -n texlive-pgfopts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfopts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfopts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfopts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgfopts/LICENSE
%{_texmfdistdir}/doc/latex/pgfopts/README
%{_texmfdistdir}/doc/latex/pgfopts/pgfopts.pdf

%files -n texlive-pgfopts
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgfopts/pgfopts.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfopts-%{texlive_version}.%{texlive_noarch}.2.1asvn56615-%{release}-zypper
%endif

%package -n texlive-pgfornament
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn55326
Release:        0
License:        LPPL-1.0
Summary:        Drawing of Vectorian ornaments with PGF/TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfornament-doc >= %{texlive_version}
Provides:       tex(pgflibraryam.code.tex)
Provides:       tex(pgflibrarypgfhan.code.tex)
Provides:       tex(pgflibraryvectorian.code.tex)
Provides:       tex(pgfornament.sty)
Provides:       tex(tikzrput.sty)
Requires:       tex(iftex.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source201:      pgfornament.tar.xz
Source202:      pgfornament.doc.tar.xz

%description -n texlive-pgfornament
This package allows the drawing of Vectorian ornaments (196)
with PGF/TikZ. The documentation presents the syntax and
parameters of the macro "pgfornament".

%package -n texlive-pgfornament-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn55326
Release:        0
Summary:        Documentation for texlive-pgfornament
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgfornament-doc
This package includes the documentation for texlive-pgfornament

%post -n texlive-pgfornament
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfornament
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfornament
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfornament-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgfornament/README.md
%{_texmfdistdir}/doc/latex/pgfornament/TeX_box.png
%{_texmfdistdir}/doc/latex/pgfornament/baseline.png
%{_texmfdistdir}/doc/latex/pgfornament/ornaments.pdf
%{_texmfdistdir}/doc/latex/pgfornament/ornaments.png
%{_texmfdistdir}/doc/latex/pgfornament/ornaments.tex
%{_texmfdistdir}/doc/latex/pgfornament/tikzrput.pdf
%{_texmfdistdir}/doc/latex/pgfornament/tikzrput.tex
%{_texmfdistdir}/doc/latex/pgfornament/usefulcommands.tex

%files -n texlive-pgfornament
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pgfornament/am/am1.pgf
%{_texmfdistdir}/tex/generic/pgfornament/am/am2.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan1.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan10.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan11.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan12.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan13.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan14.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan15.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan16.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan17.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan18.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan19.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan2.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan20.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan21.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan22.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan23.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan24.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan25.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan26.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan27.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan28.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan29.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan3.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan30.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan31.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan32.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan33.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan34.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan35.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan36.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan37.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan38.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan39.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan4.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan40.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan41.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan42.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan43.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan44.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan45.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan46.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan47.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan48.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan49.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan5.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan50.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan51.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan52.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan53.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan54.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan55.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan56.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan57.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan58.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan59.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan6.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan60.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan61.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan62.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan63.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan64.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan65.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan66.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan67.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan68.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan69.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan7.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan70.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan71.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan72.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan73.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan74.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan75.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan76.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan77.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan78.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan8.pgf
%{_texmfdistdir}/tex/generic/pgfornament/pgfhan/pgfhan9.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian1.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian10.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian100.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian101.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian102.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian103.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian104.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian105.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian106.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian107.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian108.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian109.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian11.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian110.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian111.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian112.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian113.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian114.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian115.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian116.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian117.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian118.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian119.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian12.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian120.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian121.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian122.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian123.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian124.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian125.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian126.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian127.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian128.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian129.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian13.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian130.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian131.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian132.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian133.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian134.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian135.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian136.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian137.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian138.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian139.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian14.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian140.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian141.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian142.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian143.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian144.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian145.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian146.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian147.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian148.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian149.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian15.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian150.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian151.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian152.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian153.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian154.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian155.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian156.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian157.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian158.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian159.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian16.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian160.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian161.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian162.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian163.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian164.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian165.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian166.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian167.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian168.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian169.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian17.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian170.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian171.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian172.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian173.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian174.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian175.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian176.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian177.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian178.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian179.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian18.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian180.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian181.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian182.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian183.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian184.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian185.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian186.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian187.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian188.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian189.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian19.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian190.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian191.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian192.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian193.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian194.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian195.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian196.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian2.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian20.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian21.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian22.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian23.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian24.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian25.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian26.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian27.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian28.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian29.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian3.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian30.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian31.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian32.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian33.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian34.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian35.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian36.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian37.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian38.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian39.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian4.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian40.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian41.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian42.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian43.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian44.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian45.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian46.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian47.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian48.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian49.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian5.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian50.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian51.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian52.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian53.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian54.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian55.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian56.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian57.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian58.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian59.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian6.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian60.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian61.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian62.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian63.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian64.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian65.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian66.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian67.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian68.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian69.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian7.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian70.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian71.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian72.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian73.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian74.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian75.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian76.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian77.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian78.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian79.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian8.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian80.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian81.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian82.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian83.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian84.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian85.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian86.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian87.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian88.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian89.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian9.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian90.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian91.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian92.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian93.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian94.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian95.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian96.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian97.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian98.pgf
%{_texmfdistdir}/tex/generic/pgfornament/vectorian/vectorian99.pgf
%{_texmfdistdir}/tex/latex/pgfornament/pgflibraryam.code.tex
%{_texmfdistdir}/tex/latex/pgfornament/pgflibrarypgfhan.code.tex
%{_texmfdistdir}/tex/latex/pgfornament/pgflibraryvectorian.code.tex
%{_texmfdistdir}/tex/latex/pgfornament/pgfornament.sty
%{_texmfdistdir}/tex/latex/pgfornament/tikzrput.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfornament-%{texlive_version}.%{texlive_noarch}.1.2svn55326-%{release}-zypper
%endif

%package -n texlive-pgfornament-han
Version:        %{texlive_version}.%{texlive_noarch}.svn54191
Release:        0
License:        LPPL-1.0
Summary:        Pgfornament library for Chinese traditional motifs and patterns
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfornament-han-doc >= %{texlive_version}
Provides:       tex(beamerthemeHeavenlyClouds.sty)
Provides:       tex(beamerthemeXiaoshan.sty)
Provides:       tex(cncolours.sty)
Provides:       tex(pgflibraryhan.code.tex)
Provides:       tex(pgfornament-han.sty)
Requires:       tex(calc.sty)
Requires:       tex(needspace.sty)
Requires:       tex(pgfmath.sty)
Requires:       tex(pgfornament.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source203:      pgfornament-han.tar.xz
Source204:      pgfornament-han.doc.tar.xz

%description -n texlive-pgfornament-han
This package provides a pgfornament library for Chinese
traditional motifs and patterns. The command \pgfornamenthan
takes the same options as \pgfornament from the pgfornament
package, but renders Chinese traditional motifs instead. The
list of supported motifs, as well as some examples, can be
found in the accompanying documentation. Yi pgfornament Hong
Bao De Ji Zhi ,Shi Xian Hui Zhi Yi Feng Tu Wen .
\pgfornamenthan He \pgfornament De Can Shu Shi Yi Yang De ;Bian
Yi De Chu Lai De Dang Ran Shi Yi Feng Wen Yang Liao . Hong Bao
Shou Ce Li You Wan Zheng De Wen Yang Lie Biao Yi Ji Shi Yong
Fan Li .

%package -n texlive-pgfornament-han-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54191
Release:        0
Summary:        Documentation for texlive-pgfornament-han
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pgfornament-han-doc:zh)

%description -n texlive-pgfornament-han-doc
This package includes the documentation for texlive-pgfornament-han

%post -n texlive-pgfornament-han
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfornament-han
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfornament-han
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfornament-han-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pgfornament-han/README.md
%{_texmfdistdir}/doc/latex/pgfornament-han/heavenlyclouds-sample.pdf
%{_texmfdistdir}/doc/latex/pgfornament-han/heavenlyclouds-sample.tex
%{_texmfdistdir}/doc/latex/pgfornament-han/lppl-1-3c.txt
%{_texmfdistdir}/doc/latex/pgfornament-han/pgfornament-han_manual.pdf
%{_texmfdistdir}/doc/latex/pgfornament-han/pgfornament-han_manual.tex
%{_texmfdistdir}/doc/latex/pgfornament-han/xiaoshan-sample.pdf
%{_texmfdistdir}/doc/latex/pgfornament-han/xiaoshan-sample.tex

%files -n texlive-pgfornament-han
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pgfornament-han/beamerthemeHeavenlyClouds.sty
%{_texmfdistdir}/tex/latex/pgfornament-han/beamerthemeXiaoshan.sty
%{_texmfdistdir}/tex/latex/pgfornament-han/cncolours.sty
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han1.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han10.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han11.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han12.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han13.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han14.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han15.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han16.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han17.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han18.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han19.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han2.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han20.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han21.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han22.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han23.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han24.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han25.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han26.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han27.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han28.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han29.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han3.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han30.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han31.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han32.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han33.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han34.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han35.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han36.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han37.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han38.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han39.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han4.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han40.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han41.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han42.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han43.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han44.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han45.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han46.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han47.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han48.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han49.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han5.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han50.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han51.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han52.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han53.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han54.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han55.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han56.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han57.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han58.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han59.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han6.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han60.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han61.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han62.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han63.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han64.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han65.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han66.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han67.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han68.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han69.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han7.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han70.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han71.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han72.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han73.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han74.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han75.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han76.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han77.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han78.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han8.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/han/han9.pgf
%{_texmfdistdir}/tex/latex/pgfornament-han/pgflibraryhan.code.tex
%{_texmfdistdir}/tex/latex/pgfornament-han/pgfornament-han.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfornament-han-%{texlive_version}.%{texlive_noarch}.svn54191-%{release}-zypper
%endif

%package -n texlive-pgfplots
Version:        %{texlive_version}.%{texlive_noarch}.1.17svn54080
Release:        0
License:        GPL-2.0-or-later
Summary:        Create normal/logarithmic plots in two and three dimensions
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-pgf >= %{texlive_version}
#!BuildIgnore: texlive-pgf
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pgfplots-doc >= %{texlive_version}
Provides:       tex(bugtracker.sty)
Provides:       tex(pgflibraryfillbetween.code.tex)
Provides:       tex(pgflibrarypgfplots.colorbrewer.code.tex)
Provides:       tex(pgflibrarypgfplots.colortol.code.tex)
Provides:       tex(pgflibrarypgfplots.surfshading.code.tex)
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-dvipdfmx.def)
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-dvips.def)
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-luatex.def)
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-luatexpatch.def)
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-pdftex.def)
Provides:       tex(pgflibrarypgfplots.surfshading.pgfsys-xetex.def)
Provides:       tex(pgfplots.assert.code.tex)
Provides:       tex(pgfplots.assert.sty)
Provides:       tex(pgfplots.code.tex)
Provides:       tex(pgfplots.errorbars.code.tex)
Provides:       tex(pgfplots.markers.code.tex)
Provides:       tex(pgfplots.paths.code.tex)
Provides:       tex(pgfplots.revision.tex)
Provides:       tex(pgfplots.scaling.code.tex)
Provides:       tex(pgfplots.sty)
Provides:       tex(pgfplots.tex)
Provides:       tex(pgfplotsarray.code.tex)
Provides:       tex(pgfplotsbinary.code.tex)
Provides:       tex(pgfplotsbinary.data.code.tex)
Provides:       tex(pgfplotscolor.code.tex)
Provides:       tex(pgfplotscolormap.code.tex)
Provides:       tex(pgfplotscoordprocessing.code.tex)
Provides:       tex(pgfplotscore.code.tex)
Provides:       tex(pgfplotsdeque.code.tex)
Provides:       tex(pgfplotslibrary.code.tex)
Provides:       tex(pgfplotsliststructure.code.tex)
Provides:       tex(pgfplotsliststructureext.code.tex)
Provides:       tex(pgfplotsmatrix.code.tex)
Provides:       tex(pgfplotsmeshplothandler.code.tex)
Provides:       tex(pgfplotsmeshplotimage.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_leq.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_loader.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_misc.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfcoreexternal.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfcoreimage.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfcorelayers.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfcorescopes.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfkeys.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfkeysfiltered.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryfpu.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryintersections.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryluamath.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgflibraryplothandlers.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.pdflinks.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfmanual.prettyprinter.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfmathfloat.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_pgfutil-common-lists.tex)
Provides:       tex(pgfplotsoldpgfsupp_tikzexternal.sty)
Provides:       tex(pgfplotsoldpgfsupp_tikzexternalshared.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_tikzlibraryexternal.code.tex)
Provides:       tex(pgfplotsoldpgfsupp_trig_format.code.tex)
Provides:       tex(pgfplotsplothandlers.code.tex)
Provides:       tex(pgfplotsstackedplots.code.tex)
Provides:       tex(pgfplotssysgeneric.code.tex)
Provides:       tex(pgfplotstable.code.tex)
Provides:       tex(pgfplotstable.coltype.code.tex)
Provides:       tex(pgfplotstable.sty)
Provides:       tex(pgfplotstable.tex)
Provides:       tex(pgfplotstableshared.code.tex)
Provides:       tex(pgfplotsticks.code.tex)
Provides:       tex(pgfplotsutil.code.tex)
Provides:       tex(pgfplotsutil.verb.code.tex)
Provides:       tex(pgfregressiontest.sty)
Provides:       tex(pgfsys-luatexpatch.def)
Provides:       tex(t-pgfplots.tex)
Provides:       tex(t-pgfplotstable.tex)
Provides:       tex(tikzlibrarycolorbrewer.code.tex)
Provides:       tex(tikzlibrarycolortol.code.tex)
Provides:       tex(tikzlibrarydateplot.code.tex)
Provides:       tex(tikzlibrarydecorations.softclip.code.tex)
Provides:       tex(tikzlibraryfillbetween.code.tex)
Provides:       tex(tikzlibrarypgfplots.clickable.code.tex)
Provides:       tex(tikzlibrarypgfplots.colormaps.code.tex)
Provides:       tex(tikzlibrarypgfplots.dateplot.code.tex)
Provides:       tex(tikzlibrarypgfplots.decorations.softclip.code.tex)
Provides:       tex(tikzlibrarypgfplots.external.code.tex)
Provides:       tex(tikzlibrarypgfplots.fillbetween.code.tex)
Provides:       tex(tikzlibrarypgfplots.groupplots.code.tex)
Provides:       tex(tikzlibrarypgfplots.patchplots.code.tex)
Provides:       tex(tikzlibrarypgfplots.polar.code.tex)
Provides:       tex(tikzlibrarypgfplots.smithchart.code.tex)
Provides:       tex(tikzlibrarypgfplots.statistics.code.tex)
Provides:       tex(tikzlibrarypgfplots.ternary.code.tex)
Provides:       tex(tikzlibrarypgfplots.units.code.tex)
Provides:       tex(tikzlibrarypgfplotsclickable.code.tex)
Requires:       tex(array.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(listings.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(pgfsys-common-pdf.def)
Requires:       tex(pgfsys-pdftex.def)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source205:      pgfplots.tar.xz
Source206:      pgfplots.doc.tar.xz

%description -n texlive-pgfplots
PGFPlots draws high-quality function plots in normal or
logarithmic scaling with a user-friendly interface directly in
TeX. The user supplies axis labels, legend entries and the plot
coordinates for one or more plots and PGFPlots applies axis
scaling, computes any logarithms and axis ticks and draws the
plots, supporting line plots, scatter plots, piecewise constant
plots, bar plots, area plots, mesh-- and surface plots and some
more. Pgfplots is based on PGF/TikZ (PGF); it runs equally for
LaTeX/TeX/ConTeXt.

%package -n texlive-pgfplots-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.17svn54080
Release:        0
Summary:        Documentation for texlive-pgfplots
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pgfplots-doc
This package includes the documentation for texlive-pgfplots

%post -n texlive-pgfplots
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pgfplots
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pgfplots
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pgfplots-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/context/third/pgfplots/Makefile
%{_texmfdistdir}/doc/context/third/pgfplots/pgfplotsexample-context.pdf
%{_texmfdistdir}/doc/context/third/pgfplots/pgfplotsexample-context.tex
%{_texmfdistdir}/doc/generic/pgfplots/README
%{_texmfdistdir}/doc/latex/pgfplots/TeX-programming-notes.pdf
%{_texmfdistdir}/doc/latex/pgfplots/pgfplots.doc.src.tar.bz2
%{_texmfdistdir}/doc/latex/pgfplots/pgfplots.pdf
%{_texmfdistdir}/doc/latex/pgfplots/pgfplotsexample.pdf
%{_texmfdistdir}/doc/latex/pgfplots/pgfplotsexample.tex
%{_texmfdistdir}/doc/latex/pgfplots/pgfplotstable.pdf
%{_texmfdistdir}/doc/latex/pgfplots/pgfplotstodo.pdf
%{_texmfdistdir}/doc/plain/pgfplots/pgfplotsexample-plain.pdf
%{_texmfdistdir}/doc/plain/pgfplots/pgfplotsexample-plain.tex

%files -n texlive-pgfplots
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pgfplots/matlab2pgfplots.m
%{_texmfdistdir}/scripts/pgfplots/matlab2pgfplots.sh
%{_texmfdistdir}/scripts/pgfplots/pgf2pdf.sh
%{_texmfdistdir}/scripts/pgfplots/pgfplots.py
%{_texmfdistdir}/tex/context/third/pgfplots/t-pgfplots.tex
%{_texmfdistdir}/tex/context/third/pgfplots/t-pgfplotstable.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/pgflibrarypgfplots.colorbrewer.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/pgflibrarypgfplots.colortol.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/pgflibrarypgfplots.surfshading.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/pgfplotslibrary.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarycolorbrewer.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarycolortol.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.colormaps.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.dateplot.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.decorations.softclip.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.external.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.fillbetween.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.groupplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.patchplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.polar.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.smithchart.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.statistics.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.ternary.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/libs/tikzlibrarypgfplots.units.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsarray.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsdeque.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsliststructure.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsliststructureext.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/liststructure/pgfplotsmatrix.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/binary.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/colormap.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/meshplothandler.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/pgfplotstexio.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/pgfplotsutil.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/plothandler.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/statistics.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplots/streamer.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplotsoldpgfsupp/luamath/functions.lua
%{_texmfdistdir}/tex/generic/pgfplots/lua/pgfplotsoldpgfsupp/luamath/parser.lua
%{_texmfdistdir}/tex/generic/pgfplots/numtable/pgfplotstable.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/numtable/pgfplotstable.coltype.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/numtable/pgfplotstableshared.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_leq.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_loader.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_misc.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcoreexternal.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcoreimage.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcorelayers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfcorescopes.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfkeys.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfkeysfiltered.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgflibraryfpu.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgflibraryintersections.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgflibraryluamath.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgflibraryplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmanual.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmanual.pdflinks.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmanual.prettyprinter.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfmathfloat.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_pgfutil-common-lists.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_tikzexternal.sty
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_tikzexternalshared.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_tikzlibraryexternal.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfplotsoldpgfsupp_trig_format.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfcompatib/pgfsys-luatexpatch.def
%{_texmfdistdir}/tex/generic/pgfplots/oldpgfplotscompatib/tikzlibrarydateplot.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfcontrib/pgflibraryfillbetween.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfcontrib/tikzlibrarydecorations.softclip.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfcontrib/tikzlibraryfillbetween.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.errorbars.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.markers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.paths.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.revision.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplots.scaling.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotscoordprocessing.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotscore.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsmeshplothandler.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsmeshplotimage.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsplothandlers.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsstackedplots.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/pgfplotsticks.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-dvipdfmx.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-dvips.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-luatex.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-luatexpatch.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-pdftex.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgflibrarypgfplots.surfshading.pgfsys-xetex.def
%{_texmfdistdir}/tex/generic/pgfplots/sys/pgfplotssysgeneric.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/test/pgfplots.assert.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/test/pgfplots.assert.sty
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsbinary.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsbinary.data.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotscolor.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotscolormap.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsutil.code.tex
%{_texmfdistdir}/tex/generic/pgfplots/util/pgfplotsutil.verb.code.tex
%{_texmfdistdir}/tex/latex/pgfplots/bugtracker.sty
%{_texmfdistdir}/tex/latex/pgfplots/libs/tikzlibrarypgfplots.clickable.code.tex
%{_texmfdistdir}/tex/latex/pgfplots/libs/tikzlibrarypgfplotsclickable.code.tex
%{_texmfdistdir}/tex/latex/pgfplots/pgfplots.sty
%{_texmfdistdir}/tex/latex/pgfplots/pgfplotstable.sty
%{_texmfdistdir}/tex/latex/pgfplots/pgfregressiontest.sty
%{_texmfdistdir}/tex/plain/pgfplots/pgfplots.tex
%{_texmfdistdir}/tex/plain/pgfplots/pgfplotstable.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pgfplots-%{texlive_version}.%{texlive_noarch}.1.17svn54080-%{release}-zypper
%endif

%package -n texlive-phaistos
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18651
Release:        0
License:        LPPL-1.0
Summary:        Disk of Phaistos font
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-phaistos-fonts >= %{texlive_version}
Recommends:     texlive-phaistos-doc >= %{texlive_version}
Provides:       tex(phaistos.map)
Provides:       tex(phaistos.sty)
Provides:       tex(phaistos.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source207:      phaistos.tar.xz
Source208:      phaistos.doc.tar.xz

%description -n texlive-phaistos
A font that contains all the symbols of the famous Disc of
Phaistos, together with a LaTeX package. The disc was 'printed'
by stamping the wet clay with some sort of punches, probably
around 1700 BCE. The font is available in Adobe Type 1 and
OpenType formats (the latter using the Unicode positions for
the symbols). There are those who believe that this Cretan
script was used to 'write' Greek (it is known, for example,
that the rather later Cretan Linear B script was used to write
Greek), but arguments for other languages have been presented.

%package -n texlive-phaistos-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18651
Release:        0
Summary:        Documentation for texlive-phaistos
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phaistos-doc
This package includes the documentation for texlive-phaistos

%package -n texlive-phaistos-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn18651
Release:        0
Summary:        Severed fonts for texlive-phaistos
License:        LPPL-1.0
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-phaistos-fonts
The  separated fonts package for texlive-phaistos

%post -n texlive-phaistos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap phaistos.map' >> /var/run/texlive/run-updmap

%postun -n texlive-phaistos
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap phaistos.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-phaistos
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-phaistos-fonts

%files -n texlive-phaistos-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/phaistos/getglyphs
%{_texmfdistdir}/doc/fonts/phaistos/glyphTable.pdf

%files -n texlive-phaistos
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/phaistos/phaistos.afm
%{_texmfdistdir}/fonts/map/dvips/phaistos/phaistos.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/phaistos/Phaistos.otf
%{_texmfdistdir}/fonts/tfm/public/phaistos/phaistos.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/phaistos/phaistos.pfb
%{_texmfdistdir}/tex/latex/phaistos/phaistos.sty

%files -n texlive-phaistos-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-phaistos
%{_datadir}/fontconfig/conf.avail/58-texlive-phaistos.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-phaistos.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-phaistos.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-phaistos/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-phaistos/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-phaistos/fonts.scale
%{_datadir}/fonts/texlive-phaistos/Phaistos.otf
%{_datadir}/fonts/texlive-phaistos/phaistos.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phaistos-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn18651-%{release}-zypper
%endif

%package -n texlive-phffullpagefigure
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41857
Release:        0
License:        LPPL-1.0
Summary:        Figures which fill up a whole page
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phffullpagefigure-doc >= %{texlive_version}
Provides:       tex(phffullpagefigure.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifoddpage.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(placeins.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source209:      phffullpagefigure.tar.xz
Source210:      phffullpagefigure.doc.tar.xz

%description -n texlive-phffullpagefigure
This package defines a figure environment which provides the
figure content on its own page, with the corresponding caption
reading for example "Figure 3 (on next page): <caption>".

%package -n texlive-phffullpagefigure-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41857
Release:        0
Summary:        Documentation for texlive-phffullpagefigure
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phffullpagefigure-doc
This package includes the documentation for texlive-phffullpagefigure

%post -n texlive-phffullpagefigure
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phffullpagefigure
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phffullpagefigure
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phffullpagefigure-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phffullpagefigure/Makefile
%{_texmfdistdir}/doc/latex/phffullpagefigure/README.md
%{_texmfdistdir}/doc/latex/phffullpagefigure/phffullpagefigure.pdf
%{_texmfdistdir}/doc/latex/phffullpagefigure/pkg.mk

%files -n texlive-phffullpagefigure
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phffullpagefigure/phffullpagefigure.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phffullpagefigure-%{texlive_version}.%{texlive_noarch}.1.0svn41857-%{release}-zypper
%endif

%package -n texlive-phfnote
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41858
Release:        0
License:        LPPL-1.0
Summary:        Basic formatting for short documents
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phfnote-doc >= %{texlive_version}
Provides:       tex(phfnote.sty)
Requires:       tex(MnSymbol.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(bbm.sty)
Requires:       tex(caption.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(dsfont.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fourier.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hypdoc.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(microtype.sty)
Requires:       tex(opensans.sty)
Requires:       tex(sectsty.sty)
Requires:       tex(setspace.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(url.sty)
Requires:       tex(verbdef.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source211:      phfnote.tar.xz
Source212:      phfnote.doc.tar.xz

%description -n texlive-phfnote
This package provides basic formatting for short documents such
as notes on a specific topic, short documentation, or quick
memos. It aims to cover all basic needs for such purposes:
include a standard set of relevant packages, a nice title which
doesn't take up too much space, better page margin sizes, and
some basic styling to make the note look nicer. At the same
time, it is highly flexible and customizable.

%package -n texlive-phfnote-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41858
Release:        0
Summary:        Documentation for texlive-phfnote
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phfnote-doc
This package includes the documentation for texlive-phfnote

%post -n texlive-phfnote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phfnote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phfnote
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phfnote-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phfnote/Makefile
%{_texmfdistdir}/doc/latex/phfnote/README.md
%{_texmfdistdir}/doc/latex/phfnote/phfnote.pdf
%{_texmfdistdir}/doc/latex/phfnote/pkg.mk

%files -n texlive-phfnote
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/phfnote/naturemagdoi.bst
%{_texmfdistdir}/tex/latex/phfnote/phfnote.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phfnote-%{texlive_version}.%{texlive_noarch}.1.0svn41858-%{release}-zypper
%endif

%package -n texlive-phfparen
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41859
Release:        0
License:        LPPL-1.0
Summary:        Parenthetic math expressions made simpler and less redundant
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phfparen-doc >= %{texlive_version}
Provides:       tex(phfparen.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source213:      phfparen.tar.xz
Source214:      phfparen.doc.tar.xz

%description -n texlive-phfparen
This package provides a more condensed and flexible syntax for
parenthesis-delimited expressions in math mode which also
allows for an easier switching of brace sizes. For example, the
syntax " `\big( a + b ) " can be used to replace "\bigl( a + b
\bigr)".

%package -n texlive-phfparen-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41859
Release:        0
Summary:        Documentation for texlive-phfparen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phfparen-doc
This package includes the documentation for texlive-phfparen

%post -n texlive-phfparen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phfparen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phfparen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phfparen-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phfparen/Makefile
%{_texmfdistdir}/doc/latex/phfparen/README.md
%{_texmfdistdir}/doc/latex/phfparen/phfparen.pdf
%{_texmfdistdir}/doc/latex/phfparen/pkg.mk

%files -n texlive-phfparen
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phfparen/phfparen.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phfparen-%{texlive_version}.%{texlive_noarch}.1.0svn41859-%{release}-zypper
%endif

%package -n texlive-phfqit
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn45084
Release:        0
License:        LPPL-1.0
Summary:        Macros for typesetting Quantum Information Theory
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phfqit-doc >= %{texlive_version}
Provides:       tex(phfqit.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(calc.sty)
Requires:       tex(dsfont.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source215:      phfqit.tar.xz
Source216:      phfqit.doc.tar.xz

%description -n texlive-phfqit
This package provides macros to typeset some general
mathematical operators (identity operator, trace, diagonal,
rank, ...), a powerful implementation of the bra-ket notation
(kets, bras, brakets, matrix elements etc. which can be sized
as required), delimited expressions such as averages and norms,
and some basic Lie algebra/group names. Macros for entropy
measures for quantum information theory (smooth min- and
max-entropy, smooth relative entropies, etc.) are also
provided.

%package -n texlive-phfqit-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn45084
Release:        0
Summary:        Documentation for texlive-phfqit
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phfqit-doc
This package includes the documentation for texlive-phfqit

%post -n texlive-phfqit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phfqit
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phfqit
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phfqit-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phfqit/Makefile
%{_texmfdistdir}/doc/latex/phfqit/README.md
%{_texmfdistdir}/doc/latex/phfqit/phfqit.pdf
%{_texmfdistdir}/doc/latex/phfqit/pkg.mk

%files -n texlive-phfqit
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phfqit/phfqit.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phfqit-%{texlive_version}.%{texlive_noarch}.2.0svn45084-%{release}-zypper
%endif

%package -n texlive-phfquotetext
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41869
Release:        0
License:        LPPL-1.0
Summary:        Quote verbatim text without white space formatting
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phfquotetext-doc >= %{texlive_version}
Provides:       tex(phfquotetext.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source217:      phfquotetext.tar.xz
Source218:      phfquotetext.doc.tar.xz

%description -n texlive-phfquotetext
This package provides an environment for displaying block text
with special characters, such as verbatim quotes from a referee
report which may contain pseudo-(La)TeX code. This behaves like
a verbatim environment, except that it displays its content as
normal paragraph content, ignoring any white space
preformatting.

%package -n texlive-phfquotetext-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41869
Release:        0
Summary:        Documentation for texlive-phfquotetext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phfquotetext-doc
This package includes the documentation for texlive-phfquotetext

%post -n texlive-phfquotetext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phfquotetext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phfquotetext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phfquotetext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phfquotetext/Makefile
%{_texmfdistdir}/doc/latex/phfquotetext/README.md
%{_texmfdistdir}/doc/latex/phfquotetext/phfquotetext.pdf
%{_texmfdistdir}/doc/latex/phfquotetext/pkg.mk

%files -n texlive-phfquotetext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phfquotetext/phfquotetext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phfquotetext-%{texlive_version}.%{texlive_noarch}.1.0svn41869-%{release}-zypper
%endif

%package -n texlive-phfsvnwatermark
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41870
Release:        0
License:        LPPL-1.0
Summary:        Watermarks with version control information from SVN
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phfsvnwatermark-doc >= %{texlive_version}
Provides:       tex(phfsvnwatermark.sty)
Requires:       tex(calc.sty)
Requires:       tex(currfile.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(svn-multi.sty)
Requires:       tex(svn.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source219:      phfsvnwatermark.tar.xz
Source220:      phfsvnwatermark.doc.tar.xz

%description -n texlive-phfsvnwatermark
This package allows you to add version control information as a
gray watermark on each page of your document. The SVN info is
read from keyword tags such as $Id$, $Date$, and $Author$ via
the svn or svn-multi packages.

%package -n texlive-phfsvnwatermark-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41870
Release:        0
Summary:        Documentation for texlive-phfsvnwatermark
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phfsvnwatermark-doc
This package includes the documentation for texlive-phfsvnwatermark

%post -n texlive-phfsvnwatermark
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phfsvnwatermark
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phfsvnwatermark
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phfsvnwatermark-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phfsvnwatermark/Makefile
%{_texmfdistdir}/doc/latex/phfsvnwatermark/README.md
%{_texmfdistdir}/doc/latex/phfsvnwatermark/phfsvnwatermark.pdf
%{_texmfdistdir}/doc/latex/phfsvnwatermark/pkg.mk

%files -n texlive-phfsvnwatermark
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phfsvnwatermark/phfsvnwatermark.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phfsvnwatermark-%{texlive_version}.%{texlive_noarch}.1.0svn41870-%{release}-zypper
%endif

%package -n texlive-phfthm
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41871
Release:        0
License:        LPPL-1.0
Summary:        Goodies for theorems and proofs
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phfthm-doc >= %{texlive_version}
Provides:       tex(phfthm.sty)
Requires:       tex(aliascnt.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source221:      phfthm.tar.xz
Source222:      phfthm.doc.tar.xz

%description -n texlive-phfthm
This package provides enhanced theorem and proof environments
based on the amsthm original versions. It allows for hooks to
be placed, adds some default goodies and is highly
customizable. In particular, it can connect theorems to proofs,
automatically producing text such as "See proof on page XYZ"
and "Proof of Theorem 4: ...".

%package -n texlive-phfthm-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn41871
Release:        0
Summary:        Documentation for texlive-phfthm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phfthm-doc
This package includes the documentation for texlive-phfthm

%post -n texlive-phfthm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phfthm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phfthm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phfthm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phfthm/Makefile
%{_texmfdistdir}/doc/latex/phfthm/README.md
%{_texmfdistdir}/doc/latex/phfthm/phfthm.pdf
%{_texmfdistdir}/doc/latex/phfthm/pkg.mk

%files -n texlive-phfthm
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phfthm/phfthm.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phfthm-%{texlive_version}.%{texlive_noarch}.1.0svn41871-%{release}-zypper
%endif

%package -n texlive-philex
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn36396
Release:        0
License:        LPPL-1.0
Summary:        Cross references for named and numbered environments
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-philex-doc >= %{texlive_version}
Provides:       tex(philex.sty)
Requires:       tex(calc.sty)
Requires:       tex(cgloss4e.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(linguex.sty)
Requires:       tex(suffix.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source223:      philex.tar.xz
Source224:      philex.doc.tar.xz

%description -n texlive-philex
Philex provides means for creating and cross-referencing named
or numbered environments. Possible uses would be equations,
example sentences (as in linguistics or philosophy) or named
principles. Cross references may refer either to the number, or
to a short name of the target environment, or to the contents
of the environment. Philex builds on the facilities of the
linguex package.

%package -n texlive-philex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn36396
Release:        0
Summary:        Documentation for texlive-philex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-philex-doc
This package includes the documentation for texlive-philex

%post -n texlive-philex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-philex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-philex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-philex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/philex/README
%{_texmfdistdir}/doc/latex/philex/philexmanual.pdf
%{_texmfdistdir}/doc/latex/philex/philexmanual.tex

%files -n texlive-philex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/philex/philex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-philex-%{texlive_version}.%{texlive_noarch}.1.3svn36396-%{release}-zypper
%endif

%package -n texlive-philokalia
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn45356
Release:        0
License:        LPPL-1.0
Summary:        A font to typeset the Philokalia Books
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-philokalia-fonts >= %{texlive_version}
Recommends:     texlive-philokalia-doc >= %{texlive_version}
Provides:       tex(philokalia.sty)
Provides:       tex(tuplk.fd)
Requires:       tex(lettrine.sty)
Requires:       tex(xltxtra.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source225:      philokalia.tar.xz
Source226:      philokalia.doc.tar.xz

%description -n texlive-philokalia
The philokalia package has been designed to ease the use of the
Philokalia-Regular OpenType font with XeLaTeX. The font started
as a project to digitize the typeface used to typeset the
Philokalia books.

%package -n texlive-philokalia-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn45356
Release:        0
Summary:        Documentation for texlive-philokalia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-philokalia-doc
This package includes the documentation for texlive-philokalia

%package -n texlive-philokalia-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn45356
Release:        0
Summary:        Severed fonts for texlive-philokalia
License:        LPPL-1.0
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-philokalia-fonts
The  separated fonts package for texlive-philokalia

%post -n texlive-philokalia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-philokalia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-philokalia
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-philokalia-fonts

%files -n texlive-philokalia-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/xelatex/philokalia/README
%{_texmfdistdir}/doc/xelatex/philokalia/philokalia.pdf

%files -n texlive-philokalia
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/philokalia/Philokalia-Regular.otf
%{_texmfdistdir}/tex/xelatex/philokalia/philokalia.sty
%{_texmfdistdir}/tex/xelatex/philokalia/tuplk.fd

%files -n texlive-philokalia-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-philokalia
%{_datadir}/fontconfig/conf.avail/58-texlive-philokalia.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-philokalia/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-philokalia/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-philokalia/fonts.scale
%{_datadir}/fonts/texlive-philokalia/Philokalia-Regular.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-philokalia-fonts-%{texlive_version}.%{texlive_noarch}.1.2svn45356-%{release}-zypper
%endif

%package -n texlive-philosophersimprint
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn56954
Release:        0
License:        LPPL-1.0
Summary:        Typesetting articles for "Philosophers' Imprint"
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-philosophersimprint-doc >= %{texlive_version}
Provides:       tex(philosophersimprint.cls)
Requires:       tex(article.cls)
Requires:       tex(color.sty)
Requires:       tex(courier.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(flushend.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(mathpazo.sty)
Requires:       tex(microtype.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(trajan.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source227:      philosophersimprint.tar.xz
Source228:      philosophersimprint.doc.tar.xz

%description -n texlive-philosophersimprint
In its mission statement we read "Philosophers' Imprint is a
refereed series of original papers in philosophy, edited by
philosophy faculty at the University of Michigan, with the
advice of an international Board of Editors, and published on
the World Wide Web by the University of Michigan Digital
Library. The mission of the Imprint is to promote a future in
which funds currently spent on journal subscriptions are
redirected to the dissemination of scholarship for free, via
the Internet". The class helps authors to typeset their own
articles in "Web-ready" format. No assumption is made about the
fonts available to the author: the class itself is restricted
to freely available and freely distributed fonts, only.

%package -n texlive-philosophersimprint-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn56954
Release:        0
Summary:        Documentation for texlive-philosophersimprint
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-philosophersimprint-doc
This package includes the documentation for texlive-philosophersimprint

%post -n texlive-philosophersimprint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-philosophersimprint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-philosophersimprint
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-philosophersimprint-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/philosophersimprint/README
%{_texmfdistdir}/doc/latex/philosophersimprint/philosophersimprint.bib
%{_texmfdistdir}/doc/latex/philosophersimprint/philosophersimprint.pdf
%{_texmfdistdir}/doc/latex/philosophersimprint/sample.pdf
%{_texmfdistdir}/doc/latex/philosophersimprint/sample.tex

%files -n texlive-philosophersimprint
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/philosophersimprint/philosophersimprint.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-philosophersimprint-%{texlive_version}.%{texlive_noarch}.1.5svn56954-%{release}-zypper
%endif

%package -n texlive-phonenumbers
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn51933
Release:        0
License:        LPPL-1.0
Summary:        Typesetting telephone numbers with LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phonenumbers-doc >= %{texlive_version}
Provides:       tex(phn-AT_Ortsnamen.tex)
Provides:       tex(phn-AT_Vorwahlen.tex)
Provides:       tex(phn-DE_Ortsnamen.tex)
Provides:       tex(phn-DE_Vorwahlen.tex)
Provides:       tex(phn-FR_Ortsnamen.tex)
Provides:       tex(phn-FR_Vorwahlen.tex)
Provides:       tex(phn-Landeskennzahlen.tex)
Provides:       tex(phn-UK_Ortsnamen.tex)
Provides:       tex(phn-UK_Vorwahlen.tex)
Provides:       tex(phn-US_Ortsnamen.tex)
Provides:       tex(phn-US_Vorwahlen.tex)
Provides:       tex(phonenumbers.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source229:      phonenumbers.tar.xz
Source230:      phonenumbers.doc.tar.xz

%description -n texlive-phonenumbers
The phonenumbers package makes it possible to typeset telephone
numbers according to different national conventions. German,
Austrian, French, British and North American phone numbers are
supported. Phone numbers from other countries are supported
rudimentarily. The user can select from various formatting
options, including the additional output of the country calling
code. The package is able to check if a phone number is valid
according to the national rules. It also allows to link phone
numbers using the hyperref package.

%package -n texlive-phonenumbers-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn51933
Release:        0
Summary:        Documentation for texlive-phonenumbers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-phonenumbers-doc:de;en-gb)

%description -n texlive-phonenumbers-doc
This package includes the documentation for texlive-phonenumbers

%post -n texlive-phonenumbers
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phonenumbers
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phonenumbers
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phonenumbers-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phonenumbers/Literatur.bib
%{_texmfdistdir}/doc/latex/phonenumbers/README
%{_texmfdistdir}/doc/latex/phonenumbers/phonenumbers-de.pdf
%{_texmfdistdir}/doc/latex/phonenumbers/phonenumbers-de.tex
%{_texmfdistdir}/doc/latex/phonenumbers/phonenumbers-en.pdf
%{_texmfdistdir}/doc/latex/phonenumbers/phonenumbers-en.tex

%files -n texlive-phonenumbers
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phonenumbers/phn-AT_Ortsnamen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-AT_Vorwahlen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-DE_Ortsnamen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-DE_Vorwahlen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-FR_Ortsnamen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-FR_Vorwahlen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-Landeskennzahlen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-UK_Ortsnamen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-UK_Vorwahlen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-US_Ortsnamen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phn-US_Vorwahlen.tex
%{_texmfdistdir}/tex/latex/phonenumbers/phonenumbers.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phonenumbers-%{texlive_version}.%{texlive_noarch}.2.2svn51933-%{release}-zypper
%endif

%package -n texlive-phonetic
Version:        %{texlive_version}.%{texlive_noarch}.svn56468
Release:        0
License:        LPPL-1.0
Summary:        Metafont Phonetic fonts, based on Computer Modern
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phonetic-doc >= %{texlive_version}
Provides:       tex(Uphon.fd)
Provides:       tex(cmph10.tfm)
Provides:       tex(cmph5.tfm)
Provides:       tex(cmph6.tfm)
Provides:       tex(cmph7.tfm)
Provides:       tex(cmph8.tfm)
Provides:       tex(cmph9.tfm)
Provides:       tex(cmphb10.tfm)
Provides:       tex(cmphi10.tfm)
Provides:       tex(cmphi7.tfm)
Provides:       tex(cmphi8.tfm)
Provides:       tex(cmphi9.tfm)
Provides:       tex(phonetic.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source231:      phonetic.tar.xz
Source232:      phonetic.doc.tar.xz

%description -n texlive-phonetic
The fonts are based on Computer Modern, and specified in
Metafont. Macros for the fonts' use are provided, both for
LaTeX 2.09 and for current LaTeX.

%package -n texlive-phonetic-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn56468
Release:        0
Summary:        Documentation for texlive-phonetic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phonetic-doc
This package includes the documentation for texlive-phonetic

%post -n texlive-phonetic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phonetic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phonetic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phonetic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/phonetic/209/phonetic-table.tex
%{_texmfdistdir}/doc/fonts/phonetic/209/phonetic.sty
%{_texmfdistdir}/doc/fonts/phonetic/README
%{_texmfdistdir}/doc/fonts/phonetic/makefile
%{_texmfdistdir}/doc/fonts/phonetic/phonetic-table.pdf
%{_texmfdistdir}/doc/fonts/phonetic/phonetic-table.tex

%files -n texlive-phonetic
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/phonetic/cmph10.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph5.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph6.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph7.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph8.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmph9.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphb10.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi10.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi7.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi8.mf
%{_texmfdistdir}/fonts/source/public/phonetic/cmphi9.mf
%{_texmfdistdir}/fonts/source/public/phonetic/local.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phochar.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phoital.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phoitchar.mf
%{_texmfdistdir}/fonts/source/public/phonetic/phosym.mf
%{_texmfdistdir}/fonts/source/public/phonetic/symchar.mf
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph10.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph5.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph6.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph7.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph8.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmph9.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphb10.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi10.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi7.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi8.tfm
%{_texmfdistdir}/fonts/tfm/public/phonetic/cmphi9.tfm
%{_texmfdistdir}/tex/latex/phonetic/Uphon.fd
%{_texmfdistdir}/tex/latex/phonetic/phonetic.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phonetic-%{texlive_version}.%{texlive_noarch}.svn56468-%{release}-zypper
%endif

%package -n texlive-phonrule
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn43963
Release:        0
License:        LPPL-1.0
Summary:        Typeset linear phonological rules
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-phonrule-doc >= %{texlive_version}
Provides:       tex(phonrule.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source233:      phonrule.tar.xz
Source234:      phonrule.doc.tar.xz

%description -n texlive-phonrule
The package provides macros for typesetting phonological rules
like those in 'Sound Pattern of English' (Chomsky and Halle
1968).

%package -n texlive-phonrule-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn43963
Release:        0
Summary:        Documentation for texlive-phonrule
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-phonrule-doc
This package includes the documentation for texlive-phonrule

%post -n texlive-phonrule
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-phonrule
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-phonrule
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-phonrule-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/phonrule/README.md
%{_texmfdistdir}/doc/latex/phonrule/phonrule-doc.pdf
%{_texmfdistdir}/doc/latex/phonrule/phonrule-doc.tex

%files -n texlive-phonrule
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/phonrule/phonrule.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-phonrule-%{texlive_version}.%{texlive_noarch}.1.3.2svn43963-%{release}-zypper
%endif

%package -n texlive-photo
Version:        %{texlive_version}.%{texlive_noarch}.svn18739
Release:        0
License:        LPPL-1.0
Summary:        A float environment for photographs
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-photo-doc >= %{texlive_version}
Provides:       tex(photo.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source235:      photo.tar.xz
Source236:      photo.doc.tar.xz

%description -n texlive-photo
This package introduces a new float type called photo which
works similar to the float types table and figure. Various
options exist for placing photos, captions, and a
"photographer" line. In twocolumn documents, a possibility
exists to generate double-column floats automatically if the
photo does not fit into one column. Photos do not have to be
placed as floats, they can also be placed as boxes, with
captions and photographer line still being available.

%package -n texlive-photo-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn18739
Release:        0
Summary:        Documentation for texlive-photo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-photo-doc
This package includes the documentation for texlive-photo

%post -n texlive-photo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-photo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-photo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-photo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/photo/Makefile
%{_texmfdistdir}/doc/latex/photo/photo.pdf
%{_texmfdistdir}/doc/latex/photo/photo_test.tex

%files -n texlive-photo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/photo/photo.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-photo-%{texlive_version}.%{texlive_noarch}.svn18739-%{release}-zypper
%endif

%package -n texlive-physconst
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn58727
Release:        0
License:        LPPL-1.0
Summary:        Macros for commonly used physical constants
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-physconst-doc >= %{texlive_version}
Provides:       tex(physconst.sty)
Requires:       tex(physunits.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source237:      physconst.tar.xz
Source238:      physconst.doc.tar.xz

%description -n texlive-physconst
This package consists of several macros that are shorthand for
a variety of physical constants, e.g. the speed of light. The
package developed out of physics and astronomy classes that the
author has taught and wanted to ensure that he had correct
values for each constant and did not wish to retype them every
time he uses them. The constants can be used in two forms, the
most accurate available values, or versions that are rounded to
3 significant digits for use in typical classroom settings,
homework assignments, etc. Most constants are taken from CODATA
2018, with the exception of the astronomical objects, whose
values are taken from International Astronomical Union
specified values. Constants that are derived from true
constants, e.g. the fine structure constant, have been
calculated using the accepted values of the fundamental
constants.

%package -n texlive-physconst-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn58727
Release:        0
Summary:        Documentation for texlive-physconst
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-physconst-doc
This package includes the documentation for texlive-physconst

%post -n texlive-physconst
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-physconst
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-physconst
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-physconst-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/physconst/CHANGELOG.md
%{_texmfdistdir}/doc/latex/physconst/README.md
%{_texmfdistdir}/doc/latex/physconst/makefile
%{_texmfdistdir}/doc/latex/physconst/physconst.pdf

%files -n texlive-physconst
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/physconst/physconst.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-physconst-%{texlive_version}.%{texlive_noarch}.1.1.2svn58727-%{release}-zypper
%endif

%package -n texlive-physics
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn28590
Release:        0
License:        LPPL-1.0
Summary:        Macros supporting the Mathematics of Physics
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-physics-doc >= %{texlive_version}
Provides:       tex(physics.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source239:      physics.tar.xz
Source240:      physics.doc.tar.xz

%description -n texlive-physics
The package defines simple and flexible macros for typesetting
equations in the languages of vector calculus and linear
algebra, using Dirac notation.

%package -n texlive-physics-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn28590
Release:        0
Summary:        Documentation for texlive-physics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-physics-doc
This package includes the documentation for texlive-physics

%post -n texlive-physics
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-physics
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-physics
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-physics-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/physics/README
%{_texmfdistdir}/doc/latex/physics/physics.pdf
%{_texmfdistdir}/doc/latex/physics/physics.tex

%files -n texlive-physics
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/physics/physics.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-physics-%{texlive_version}.%{texlive_noarch}.1.3svn28590-%{release}-zypper
%endif

%package -n texlive-physunits
Version:        %{texlive_version}.%{texlive_noarch}.1.2.0svn58728
Release:        0
License:        LPPL-1.0
Summary:        Macros for commonly used physical units
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-physunits-doc >= %{texlive_version}
Provides:       tex(physunits.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source241:      physunits.tar.xz
Source242:      physunits.doc.tar.xz

%description -n texlive-physunits
This package provides a collection of macros to simplify using
physical units (e.g. m for meters, J for joules, etc.),
especially in math mode. All major SI units are included, as
well as some cgs units used in astronomy.

%package -n texlive-physunits-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2.0svn58728
Release:        0
Summary:        Documentation for texlive-physunits
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-physunits-doc
This package includes the documentation for texlive-physunits

%post -n texlive-physunits
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-physunits
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-physunits
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-physunits-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/physunits/CHANGELOG.md
%{_texmfdistdir}/doc/latex/physunits/README.md
%{_texmfdistdir}/doc/latex/physunits/makefile
%{_texmfdistdir}/doc/latex/physunits/physunits.pdf

%files -n texlive-physunits
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/physunits/physunits.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-physunits-%{texlive_version}.%{texlive_noarch}.1.2.0svn58728-%{release}-zypper
%endif

%package -n texlive-piano
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21574
Release:        0
License:        LPPL-1.0
Summary:        Typeset a basic 2-octave piano diagram
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-piano-doc >= %{texlive_version}
Provides:       tex(piano.sty)
Requires:       tex(color.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xargs.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source243:      piano.tar.xz
Source244:      piano.doc.tar.xz

%description -n texlive-piano
This package adds the \keyboard[1][2]..[7] command to your
project. When used, it draws a small 2 octaves piano keyboard
on your document, with up to 7 keys highlighted. Keys go : Co,
Cso, Do, Dso, Eo, Fo, Fso, Go, Gso, Ao, Aso, Bo, Ct, Cst, Dt,
Dst, Et, Ft, Fst, Gt, Gst, At, Ast and Bt. (A working example
is included in the README file.)

%package -n texlive-piano-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21574
Release:        0
Summary:        Documentation for texlive-piano
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-piano-doc
This package includes the documentation for texlive-piano

%post -n texlive-piano
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-piano
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-piano
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-piano-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/piano/README

%files -n texlive-piano
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/piano/piano.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-piano-%{texlive_version}.%{texlive_noarch}.1.0svn21574-%{release}-zypper
%endif

%package -n texlive-picinpar
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn57349
Release:        0
License:        GPL-2.0-or-later
Summary:        Insert pictures into paragraphs
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-picinpar-doc >= %{texlive_version}
Provides:       tex(picinpar.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source245:      picinpar.tar.xz
Source246:      picinpar.doc.tar.xz

%description -n texlive-picinpar
A legacy package for creating 'windows' in paragraphs, for
inserting graphics, etc. (including "dropped capitals"). Users
should note that Pieter van Oostrum (in a published review of
packages of this sort) does not recommend this package; Picins
is recommended instead.

%package -n texlive-picinpar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn57349
Release:        0
Summary:        Documentation for texlive-picinpar
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-picinpar-doc:de;en)

%description -n texlive-picinpar-doc
This package includes the documentation for texlive-picinpar

%post -n texlive-picinpar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-picinpar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-picinpar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-picinpar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/picinpar/picinpar-de.pdf
%{_texmfdistdir}/doc/latex/picinpar/picinpar-de.tex
%{_texmfdistdir}/doc/latex/picinpar/picinpar-en.pdf
%{_texmfdistdir}/doc/latex/picinpar/picinpar-en.tex

%files -n texlive-picinpar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/picinpar/picinpar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-picinpar-%{texlive_version}.%{texlive_noarch}.1.2asvn57349-%{release}-zypper
%endif

%package -n texlive-pict2e
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4bsvn56504
Release:        0
License:        LPPL-1.0
Summary:        New implementation of picture commands
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pict2e-doc >= %{texlive_version}
Provides:       tex(p2e-dvipdfm.def)
Provides:       tex(p2e-dvipdfmx.def)
Provides:       tex(p2e-dvips.def)
Provides:       tex(p2e-luatex.def)
Provides:       tex(p2e-pctex32.def)
Provides:       tex(p2e-pctexps.def)
Provides:       tex(p2e-pdftex.def)
Provides:       tex(p2e-textures.def)
Provides:       tex(p2e-vtex.def)
Provides:       tex(p2e-xetex.def)
Provides:       tex(pict2e.cfg)
Provides:       tex(pict2e.sty)
Requires:       tex(trig.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source247:      pict2e.tar.xz
Source248:      pict2e.doc.tar.xz

%description -n texlive-pict2e
This package was described in the 2nd edition of 'LaTeX: A
Document Preparation System', but the LaTeX project team
declined to produce the package. For a long time, LaTeX
included a 'pict2e package' that merely produced an apologetic
error message. The new package extends the existing LaTeX
picture environment, using the familiar technique (cf. the
graphics and color packages) of driver files (at present,
drivers for dvips, pdfTeX, LuaTeX, XeTeX, VTeX, dvipdfm, and
dvipdfmx are available). The package documentation has a fair
number of examples of use, showing where things are improved by
comparison with the LaTeX picture environment.

%package -n texlive-pict2e-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4bsvn56504
Release:        0
Summary:        Documentation for texlive-pict2e
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pict2e-doc
This package includes the documentation for texlive-pict2e

%post -n texlive-pict2e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pict2e
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pict2e
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pict2e-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pict2e/README.md
%{_texmfdistdir}/doc/latex/pict2e/manifest.txt
%{_texmfdistdir}/doc/latex/pict2e/p2e-drivers.pdf
%{_texmfdistdir}/doc/latex/pict2e/pict2e.pdf

%files -n texlive-pict2e
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pict2e/p2e-dvipdfm.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-dvipdfmx.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-dvips.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-luatex.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-pctex32.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-pctexps.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-pdftex.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-textures.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-vtex.def
%{_texmfdistdir}/tex/latex/pict2e/p2e-xetex.def
%{_texmfdistdir}/tex/latex/pict2e/pict2e.cfg
%{_texmfdistdir}/tex/latex/pict2e/pict2e.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pict2e-%{texlive_version}.%{texlive_noarch}.0.0.4bsvn56504-%{release}-zypper
%endif

%package -n texlive-pictex
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn21943
Release:        0
License:        LPPL-1.0
Summary:        Picture drawing macros for TeX and LaTeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pictex-doc >= %{texlive_version}
Provides:       tex(errorbars.tex)
Provides:       tex(latexpicobjs.tex)
Provides:       tex(piccorr.sty)
Provides:       tex(picmore.tex)
Provides:       tex(pictex.sty)
Provides:       tex(pictex.tex)
Provides:       tex(pictexwd.sty)
Provides:       tex(pictexwd.tex)
Provides:       tex(pointers.tex)
Provides:       tex(postpictex.tex)
Provides:       tex(prepictex.tex)
Provides:       tex(texpictex.tex)
Provides:       tex(tree.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source249:      pictex.tar.xz
Source250:      pictex.doc.tar.xz

%description -n texlive-pictex
PicTeX is an early, and very comprehensive drawing package,
that mostly draws by placing myriads of small dots to make up
pictures. It has a tendency to run out of space, most
especially of allowable dimensions registers; packages m-pictex
and pictexwd deal with the register problem, in different ways.
Note that full documentation may be bought via the PC-TeX site,
though a command summary is available as free software.
Alternatively, a front-end package such as mathsPiC, which
covers all of PicTeX and has a complete and free manual, could
be used.

%package -n texlive-pictex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn21943
Release:        0
Summary:        Documentation for texlive-pictex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pictex-doc
This package includes the documentation for texlive-pictex

%post -n texlive-pictex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pictex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pictex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pictex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/pictex/00index
%{_texmfdistdir}/doc/generic/pictex/README
%{_texmfdistdir}/doc/generic/pictex/pictexzusatz.txt
%{_texmfdistdir}/doc/generic/pictex/readme.errorbars

%files -n texlive-pictex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/pictex/errorbars.tex
%{_texmfdistdir}/tex/generic/pictex/latexpicobjs.tex
%{_texmfdistdir}/tex/generic/pictex/piccorr.sty
%{_texmfdistdir}/tex/generic/pictex/picmore.tex
%{_texmfdistdir}/tex/generic/pictex/pictex.sty
%{_texmfdistdir}/tex/generic/pictex/pictex.tex
%{_texmfdistdir}/tex/generic/pictex/pictexwd.sty
%{_texmfdistdir}/tex/generic/pictex/pictexwd.tex
%{_texmfdistdir}/tex/generic/pictex/pointers.tex
%{_texmfdistdir}/tex/generic/pictex/postpictex.tex
%{_texmfdistdir}/tex/generic/pictex/prepictex.tex
%{_texmfdistdir}/tex/generic/pictex/texpictex.tex
%{_texmfdistdir}/tex/generic/pictex/tree.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pictex-%{texlive_version}.%{texlive_noarch}.1.1svn21943-%{release}-zypper
%endif

%package -n texlive-pictex2
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
License:        LPPL-1.0
Summary:        Adds relative coordinates and improves the \plot command
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       tex(pictex2.sty)
Requires:       tex(pictex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source251:      pictex2.tar.xz

%description -n texlive-pictex2
Adds two user commands to standard PiCTeX. One command uses
relative coordinates, thus eliminating the need to calculate
the coordinate of every point manually as in standard PiCTeX.
The other command modifies \plot to use a rule instead of dots
if the line segment is horizontal or vertical.

%post -n texlive-pictex2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pictex2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pictex2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pictex2
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pictex2/pictex2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pictex2-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-pictexsum
Version:        %{texlive_version}.%{texlive_noarch}.svn24965
Release:        0
License:        LPPL-1.0
Summary:        A summary of PicTeX commands
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source252:      pictexsum.doc.tar.xz

%description -n texlive-pictexsum
The document summarises the commands of PicTeX. While it is no
substitute for the PicTeX manual itself (available from
Personal TeX inc.), the document is a useful aide-memoire for
those who have read the manual.

%post -n texlive-pictexsum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pictexsum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pictexsum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pictexsum
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pictexsum/Makefile
%{_texmfdistdir}/doc/latex/pictexsum/README
%{_texmfdistdir}/doc/latex/pictexsum/a4mod.sty
%{_texmfdistdir}/doc/latex/pictexsum/pictexsum.pdf
%{_texmfdistdir}/doc/latex/pictexsum/pictexsum.tex
%{_texmfdistdir}/doc/latex/pictexsum/useful.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pictexsum-%{texlive_version}.%{texlive_noarch}.svn24965-%{release}-zypper
%endif

%package -n texlive-picture
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn54867
Release:        0
License:        LPPL-1.0
Summary:        Dimens for picture macros
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-picture-doc >= %{texlive_version}
Provides:       tex(picture.sty)
Requires:       tex(calc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source253:      picture.tar.xz
Source254:      picture.doc.tar.xz

%description -n texlive-picture
There are macro and environment arguments that expect numbers
that will internally be multiplied by \unitlength. This package
extends the syntax of these arguments, so that dimensions with
calculation support may be used for these arguments.

%package -n texlive-picture-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn54867
Release:        0
Summary:        Documentation for texlive-picture
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-picture-doc
This package includes the documentation for texlive-picture

%post -n texlive-picture
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-picture
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-picture
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-picture-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/picture/README.md
%{_texmfdistdir}/doc/latex/picture/picture-example.tex
%{_texmfdistdir}/doc/latex/picture/picture.pdf

%files -n texlive-picture
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/picture/picture.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-picture-%{texlive_version}.%{texlive_noarch}.1.6svn54867-%{release}-zypper
%endif

%package -n texlive-piechartmp
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn19440
Release:        0
License:        LPPL-1.0
Summary:        Draw pie-charts using MetaPost
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-piechartmp-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source255:      piechartmp.tar.xz
Source256:      piechartmp.doc.tar.xz

%description -n texlive-piechartmp
The piechartmp package is an easy way to draw pie-charts with
MetaPost. The package implements an interface that enables
users with little MetaPost experience to draw charts. A
highlight of the package is the possibility of suppressing some
segments of the chart, thus creating the possibility of several
charts from the same data.

%package -n texlive-piechartmp-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn19440
Release:        0
Summary:        Documentation for texlive-piechartmp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-piechartmp-doc
This package includes the documentation for texlive-piechartmp

%post -n texlive-piechartmp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-piechartmp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-piechartmp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-piechartmp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/piechartmp/INSTALL
%{_texmfdistdir}/doc/metapost/piechartmp/LEGAL
%{_texmfdistdir}/doc/metapost/piechartmp/README
%{_texmfdistdir}/doc/metapost/piechartmp/README.TEXLIVE
%{_texmfdistdir}/doc/metapost/piechartmp/examples/wec-mfun.mp
%{_texmfdistdir}/doc/metapost/piechartmp/examples/wec-mfun.pdf
%{_texmfdistdir}/doc/metapost/piechartmp/examples/wec.mp
%{_texmfdistdir}/doc/metapost/piechartmp/examples/wec.pdf
%{_texmfdistdir}/doc/metapost/piechartmp/examples/worldmap.jpg

%files -n texlive-piechartmp
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/piechartmp/piechartmp.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-piechartmp-%{texlive_version}.%{texlive_noarch}.0.0.3.0svn19440-%{release}-zypper
%endif

%package -n texlive-piff
Version:        %{texlive_version}.%{texlive_noarch}.svn21894
Release:        0
License:        SUSE-Public-Domain
Summary:        Macro tools by Mike Piff
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-piff-doc >= %{texlive_version}
Provides:       tex(duplicat.sty)
Provides:       tex(newproof.sty)
Provides:       tex(onepagem.sty)
Provides:       tex(time.sty)
Requires:       tex(amsfonts.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source257:      piff.tar.xz
Source258:      piff.doc.tar.xz

%description -n texlive-piff
The set (now) consists of: a small package for dealing with
duplicate-numbered output pages; newproof, for defining
mathematical proof structures; onepagem for omitting the page
number in one-page documents and time, which prints a 12-hour
format time.

%package -n texlive-piff-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn21894
Release:        0
Summary:        Documentation for texlive-piff
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-piff-doc
This package includes the documentation for texlive-piff

%post -n texlive-piff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-piff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-piff
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-piff-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/piff/README
%{_texmfdistdir}/doc/latex/piff/duplicat-doc.pdf
%{_texmfdistdir}/doc/latex/piff/duplicat-doc.tex
%{_texmfdistdir}/doc/latex/piff/newproof-doc.pdf
%{_texmfdistdir}/doc/latex/piff/newproof-doc.tex
%{_texmfdistdir}/doc/latex/piff/onepagem-doc.pdf
%{_texmfdistdir}/doc/latex/piff/onepagem-doc.tex
%{_texmfdistdir}/doc/latex/piff/time-doc.pdf
%{_texmfdistdir}/doc/latex/piff/time-doc.tex

%files -n texlive-piff
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/piff/duplicat.sty
%{_texmfdistdir}/tex/latex/piff/newproof.sty
%{_texmfdistdir}/tex/latex/piff/onepagem.sty
%{_texmfdistdir}/tex/latex/piff/time.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-piff-%{texlive_version}.%{texlive_noarch}.svn21894-%{release}-zypper
%endif

%package -n texlive-pigpen
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
License:        LPPL-1.0
Summary:        A font for the pigpen (or masonic) cipher
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-pigpen-fonts >= %{texlive_version}
Recommends:     texlive-pigpen-doc >= %{texlive_version}
Provides:       tex(pigpen.map)
Provides:       tex(pigpen.sty)
Provides:       tex(pigpen.tex)
Provides:       tex(pigpen.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source259:      pigpen.tar.xz
Source260:      pigpen.doc.tar.xz

%description -n texlive-pigpen
The Pigpen cipher package provides the font and the necessary
wrappers (style file, etc.) in order to write Pigpen ciphers, a
simple substitution cipher. The package provides a font
(available both as Metafont source, and as an Adobe Type 1
file), and macros for its use.

%package -n texlive-pigpen-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Documentation for texlive-pigpen
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pigpen-doc
This package includes the documentation for texlive-pigpen

%package -n texlive-pigpen-fonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Severed fonts for texlive-pigpen
License:        LPPL-1.0
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-pigpen-fonts
The  separated fonts package for texlive-pigpen

%post -n texlive-pigpen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap pigpen.map' >> /var/run/texlive/run-updmap

%postun -n texlive-pigpen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap pigpen.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-pigpen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-pigpen-fonts

%files -n texlive-pigpen-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pigpen/README
%{_texmfdistdir}/doc/latex/pigpen/pigpendoc.pdf
%{_texmfdistdir}/doc/latex/pigpen/pigpendoc.tex

%files -n texlive-pigpen
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/pigpen/pigpen.map
%{_texmfdistdir}/fonts/source/public/pigpen/pigpen.mf
%{_texmfdistdir}/fonts/tfm/public/pigpen/pigpen.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pigpen/pigpen.pfa
%{_texmfdistdir}/tex/latex/pigpen/pigpen.sty
%{_texmfdistdir}/tex/latex/pigpen/pigpen.tex

%files -n texlive-pigpen-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-pigpen
%{_datadir}/fontconfig/conf.avail/58-texlive-pigpen.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pigpen/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pigpen/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pigpen/fonts.scale
%{_datadir}/fonts/texlive-pigpen/pigpen.pfa
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pigpen-fonts-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif

%package -n texlive-pinlabel
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn24769
Release:        0
License:        LPPL-1.0
Summary:        A TeX labelling package
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pinlabel-doc >= %{texlive_version}
Provides:       tex(pinlabel.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source261:      pinlabel.tar.xz
Source262:      pinlabel.doc.tar.xz

%description -n texlive-pinlabel
Pinlabel is a labelling package for attaching perfectly
formatted TeX labels to figures and diagrams in both eps and
pdf formats. It is suitable both for labelling a new diagram
and for relabelling an existing diagram. The package uses
coordinates derived from GhostView (or gv) and labels are
placed with automatic and consistent spacing relative to the
object labelled.

%package -n texlive-pinlabel-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn24769
Release:        0
Summary:        Documentation for texlive-pinlabel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pinlabel-doc
This package includes the documentation for texlive-pinlabel

%post -n texlive-pinlabel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pinlabel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pinlabel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pinlabel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pinlabel/pinlabdoc.pdf
%{_texmfdistdir}/doc/latex/pinlabel/src/fig3.pdf
%{_texmfdistdir}/doc/latex/pinlabel/src/fig6.pdf
%{_texmfdistdir}/doc/latex/pinlabel/src/gtpart.cls
%{_texmfdistdir}/doc/latex/pinlabel/src/pinlabdoc.tex
%{_texmfdistdir}/doc/latex/pinlabel/src/put.fig
%{_texmfdistdir}/doc/latex/pinlabel/src/put.pdf
%{_texmfdistdir}/doc/latex/pinlabel/src/put2.fig
%{_texmfdistdir}/doc/latex/pinlabel/src/put2.pdf
%{_texmfdistdir}/doc/latex/pinlabel/src/screen.pdf

%files -n texlive-pinlabel
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pinlabel/pinlabel.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pinlabel-%{texlive_version}.%{texlive_noarch}.1.2svn24769-%{release}-zypper
%endif

%package -n texlive-pinoutikz
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn55966
Release:        0
License:        LPPL-1.0
Summary:        Draw chip pinouts with TikZ
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pinoutikz-doc >= %{texlive_version}
Provides:       tex(pinoutikz.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(arrayjob.sty)
Requires:       tex(forarray.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
Requires:       tex(upquote.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source263:      pinoutikz.tar.xz
Source264:      pinoutikz.doc.tar.xz

%description -n texlive-pinoutikz
The package provides a set of macros for typesetting electronic
chip pinouts. It is designed as a tool that is easy to use,
with a lean syntax, native to LaTeX, and directly supporting
PDF output format. It has therefore been based on the very
impressive TikZ package.

%package -n texlive-pinoutikz-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn55966
Release:        0
Summary:        Documentation for texlive-pinoutikz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pinoutikz-doc
This package includes the documentation for texlive-pinoutikz

%post -n texlive-pinoutikz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pinoutikz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pinoutikz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pinoutikz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pinoutikz/README.md
%{_texmfdistdir}/doc/latex/pinoutikz/pinoutikz_doc_en.pdf
%{_texmfdistdir}/doc/latex/pinoutikz/pinoutikz_doc_en.tex

%files -n texlive-pinoutikz
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pinoutikz/pinoutikz.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pinoutikz-%{texlive_version}.%{texlive_noarch}.1.1.2svn55966-%{release}-zypper
%endif

%package -n texlive-pitex
Version:        %{texlive_version}.%{texlive_noarch}.svn24731
Release:        0
License:        LPPL-1.0
Summary:        Documentation macros
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pitex-doc >= %{texlive_version}
Provides:       tex(pitex.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source265:      pitex.tar.xz
Source266:      pitex.doc.tar.xz

%description -n texlive-pitex
The bundle provides macros that the author uses when writing
documentation (for example, that of the texapi and yax
packages). The tools could be used by anyone, but there is no
documentation, and the macros are subject to change without
notice.

%package -n texlive-pitex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn24731
Release:        0
Summary:        Documentation for texlive-pitex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pitex-doc
This package includes the documentation for texlive-pitex

%post -n texlive-pitex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pitex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pitex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pitex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/pitex/README
%{_texmfdistdir}/doc/plain/pitex/foundry-settings.lua
%{_texmfdistdir}/doc/plain/pitex/i-pitex.lua
%{_texmfdistdir}/doc/plain/pitex/pitex-doc.pdf
%{_texmfdistdir}/doc/plain/pitex/pitex-doc.tex
%{_texmfdistdir}/doc/plain/pitex/pitex-doc.txt

%files -n texlive-pitex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/pitex/base.ptxlua
%{_texmfdistdir}/tex/plain/pitex/blocks.ptx
%{_texmfdistdir}/tex/plain/pitex/files.ptx
%{_texmfdistdir}/tex/plain/pitex/fonts.ptx
%{_texmfdistdir}/tex/plain/pitex/fonts.ptxlua
%{_texmfdistdir}/tex/plain/pitex/inserts.ptx
%{_texmfdistdir}/tex/plain/pitex/lua.ptx
%{_texmfdistdir}/tex/plain/pitex/output.ptx
%{_texmfdistdir}/tex/plain/pitex/pitex.tex
%{_texmfdistdir}/tex/plain/pitex/references.ptx
%{_texmfdistdir}/tex/plain/pitex/sections.ptx
%{_texmfdistdir}/tex/plain/pitex/verbatim.ptx
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pitex-%{texlive_version}.%{texlive_noarch}.svn24731-%{release}-zypper
%endif

%package -n texlive-pittetd
Version:        %{texlive_version}.%{texlive_noarch}.1.618svn15878
Release:        0
License:        LPPL-1.0
Summary:        Electronic Theses and Dissertations at Pitt
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pittetd-doc >= %{texlive_version}
Provides:       tex(pitetd10.clo)
Provides:       tex(pitetd11.clo)
Provides:       tex(pitetd12.clo)
Provides:       tex(pittetd.cls)
Requires:       tex(hyperref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source267:      pittetd.tar.xz
Source268:      pittetd.doc.tar.xz

%description -n texlive-pittetd
A document class for theses and dissertations. Provides patch
files that enable pittetd to use files prepared for use with
the pittdiss or pitthesis classes. The manual provides a
detailed guide for users who wish to use the class to prepare
their thesis or dissertation.

%package -n texlive-pittetd-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.618svn15878
Release:        0
Summary:        Documentation for texlive-pittetd
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pittetd-doc
This package includes the documentation for texlive-pittetd

%post -n texlive-pittetd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pittetd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pittetd
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pittetd-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pittetd/achicago.pit
%{_texmfdistdir}/doc/latex/pittetd/pittdiss.pit
%{_texmfdistdir}/doc/latex/pittetd/pittetd.pdf
%{_texmfdistdir}/doc/latex/pittetd/pitthesis.pit

%files -n texlive-pittetd
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pittetd/pitetd10.clo
%{_texmfdistdir}/tex/latex/pittetd/pitetd11.clo
%{_texmfdistdir}/tex/latex/pittetd/pitetd12.clo
%{_texmfdistdir}/tex/latex/pittetd/pittetd.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pittetd-%{texlive_version}.%{texlive_noarch}.1.618svn15878-%{release}-zypper
%endif

%package -n texlive-pixelart
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn57508
Release:        0
License:        LPPL-1.0
Summary:        A package to draw pixel-art pictures
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pixelart-doc >= %{texlive_version}
Provides:       tex(pixelart.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pgf.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source269:      pixelart.tar.xz
Source270:      pixelart.doc.tar.xz

%description -n texlive-pixelart
A LaTeX package to draw single-color pixel-art pictures using
TikZ.

%package -n texlive-pixelart-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2.0svn57508
Release:        0
Summary:        Documentation for texlive-pixelart
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pixelart-doc
This package includes the documentation for texlive-pixelart

%post -n texlive-pixelart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pixelart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pixelart
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pixelart-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pixelart/CHANGELOG.md
%{_texmfdistdir}/doc/latex/pixelart/LICENSE.txt
%{_texmfdistdir}/doc/latex/pixelart/README.md
%{_texmfdistdir}/doc/latex/pixelart/pixelart.pdf

%files -n texlive-pixelart
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pixelart/pixelart.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pixelart-%{texlive_version}.%{texlive_noarch}.0.0.2.0svn57508-%{release}-zypper
%endif

%package -n texlive-pkfix
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn26032
Release:        0
License:        LPPL-1.0
Summary:        Replace pk fonts in PostScript with Type 1 fonts
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pkfix-bin >= %{texlive_version}
#!BuildIgnore: texlive-pkfix-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pkfix-doc >= %{texlive_version}
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source271:      pkfix.tar.xz
Source272:      pkfix.doc.tar.xz

%description -n texlive-pkfix
The perl script pkfix looks for DVIPSBitmapFont comments in
PostScript files, generated by 'not too old' dvips, and
replaces them by type 1 versions of the fonts, if possible.

%package -n texlive-pkfix-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn26032
Release:        0
Summary:        Documentation for texlive-pkfix
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pkfix-doc
This package includes the documentation for texlive-pkfix

%post -n texlive-pkfix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pkfix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pkfix
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pkfix-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/pkfix/README

%files -n texlive-pkfix
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pkfix/pkfix.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pkfix-%{texlive_version}.%{texlive_noarch}.1.7svn26032-%{release}-zypper
%endif

%package -n texlive-pkfix-helper
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn56061
Release:        0
License:        LPPL-1.0
Summary:        Make PostScript files accessible to pkfix
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-pkfix-helper-bin >= %{texlive_version}
#!BuildIgnore: texlive-pkfix-helper-bin
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pkfix-helper-doc >= %{texlive_version}
Requires:       perl(File::Basename)
#!BuildIgnore:  perl(File::Basename)
Requires:       perl(File::Spec)
#!BuildIgnore:  perl(File::Spec)
Requires:       perl(File::Temp)
#!BuildIgnore:  perl(File::Temp)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(Pod::Usage)
#!BuildIgnore:  perl(Pod::Usage)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source273:      pkfix-helper.tar.xz
Source274:      pkfix-helper.doc.tar.xz

%description -n texlive-pkfix-helper
Pkfix is a useful utility for replacing resolution-dependent
bitmapped fonts in a dvips-produced PostScript file with the
corresponding resolution-independent vector fonts.
Unfortunately, pkfix needs to parse certain PostScript comments
that appear only in files produced by dvips versions later than
5.58 (ca. 1996); it fails to work on PostScript files produced
by older versions of dvips. Pkfix-helper is a program that
attempts to insert newer-dvips comments into an older-dvips
PostScript file, thereby making the file suitable for
processing by pkfix. pkfix-helper can sometimes process
documents fully autonomously but does require the user to
verify and, if needed, correct its decisions.

%package -n texlive-pkfix-helper-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn56061
Release:        0
Summary:        Documentation for texlive-pkfix-helper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(pkfix-helper.1)

%description -n texlive-pkfix-helper-doc
This package includes the documentation for texlive-pkfix-helper

%post -n texlive-pkfix-helper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pkfix-helper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pkfix-helper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pkfix-helper-doc
%defattr(-,root,root,755)
%{_mandir}/man1/pkfix-helper.1*
%{_texmfdistdir}/doc/support/pkfix-helper/README
%{_texmfdistdir}/doc/support/pkfix-helper/encoding-samples.pdf
%{_texmfdistdir}/doc/support/pkfix-helper/encoding-samples.tex

%files -n texlive-pkfix-helper
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/pkfix-helper/pkfix-helper
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pkfix-helper-%{texlive_version}.%{texlive_noarch}.1.6svn56061-%{release}-zypper
%endif

%package -n texlive-pkgloader
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn47486
Release:        0
License:        LPPL-1.0
Summary:        Manage the options and loading order of other packages
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pkgloader-doc >= %{texlive_version}
Provides:       tex(pkgloader-cls-pkg.sty)
Provides:       tex(pkgloader-dry.sty)
Provides:       tex(pkgloader-early.sty)
Provides:       tex(pkgloader-error.sty)
Provides:       tex(pkgloader-false.sty)
Provides:       tex(pkgloader-late.sty)
Provides:       tex(pkgloader-recommended.sty)
Provides:       tex(pkgloader-true.sty)
Provides:       tex(pkgloader.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(lt3graph.sty)
Requires:       tex(withargs.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source275:      pkgloader.tar.xz
Source276:      pkgloader.doc.tar.xz

%description -n texlive-pkgloader
The package seeks to address the frustration caused by package
conflicts. It is in an early stage of its development, and
should probably not be used as a matter of course; however the
author welcomes feedback via the home page link given in this
catalogue entry. Nevertheless, the author urges users to try
the package and to report issues (or whatever) via the
package's repository. To use pkgloader you need, apart from
packages installed by default, the lt3graph package.

%package -n texlive-pkgloader-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7.0svn47486
Release:        0
Summary:        Documentation for texlive-pkgloader
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pkgloader-doc
This package includes the documentation for texlive-pkgloader

%post -n texlive-pkgloader
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pkgloader
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pkgloader
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pkgloader-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pkgloader/README
%{_texmfdistdir}/doc/latex/pkgloader/pkgloader-packagedoc.cls
%{_texmfdistdir}/doc/latex/pkgloader/pkgloader.pdf
%{_texmfdistdir}/doc/latex/pkgloader/pkgloader.tex

%files -n texlive-pkgloader
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-cls-pkg.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-dry.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-early.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-error.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-false.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-late.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-recommended.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader-true.sty
%{_texmfdistdir}/tex/latex/pkgloader/pkgloader.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pkgloader-%{texlive_version}.%{texlive_noarch}.0.0.7.0svn47486-%{release}-zypper
%endif

%package -n texlive-pkuthss
Version:        %{texlive_version}.%{texlive_noarch}.1.9.0svn58729
Release:        0
License:        LPPL-1.0
Summary:        LaTeX template for dissertations in Peking University
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-pkuthss-doc >= %{texlive_version}
Provides:       tex(pkuthss-gbk.def)
Provides:       tex(pkuthss-utf8.def)
Provides:       tex(pkuthss.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(caption.sty)
Requires:       tex(ctexbook.cls)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(keyval.sty)
Requires:       tex(latexsym.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(scrextend.sty)
Requires:       tex(setspace.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(ulem.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source277:      pkuthss.tar.xz
Source278:      pkuthss.doc.tar.xz

%description -n texlive-pkuthss
The package provides a simple, clear and flexible LaTeX
template for dissertations in Peking University.

%package -n texlive-pkuthss-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9.0svn58729
Release:        0
Summary:        Documentation for texlive-pkuthss
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-pkuthss-doc:zh)

%description -n texlive-pkuthss-doc
This package includes the documentation for texlive-pkuthss

%post -n texlive-pkuthss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-pkuthss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-pkuthss
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-pkuthss-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/pkuthss/README.txt
%{_texmfdistdir}/doc/latex/pkuthss/example.pdf
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/abs.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/ack.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/chap1.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/chap2.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/chap3.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/copy.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/encl1.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/chap/origin.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/ctex-fontset-pkuthss.def
%{_texmfdistdir}/doc/latex/pkuthss/example/ctexopts.cfg
%{_texmfdistdir}/doc/latex/pkuthss/example/latexmkrc
%{_texmfdistdir}/doc/latex/pkuthss/example/spine.tex
%{_texmfdistdir}/doc/latex/pkuthss/example/thesis.bib
%{_texmfdistdir}/doc/latex/pkuthss/example/thesis.tex
%{_texmfdistdir}/doc/latex/pkuthss/pkuthss.pdf
%{_texmfdistdir}/doc/latex/pkuthss/readme/ChangeLog-upto-1.3.txt
%{_texmfdistdir}/doc/latex/pkuthss/readme/ChangeLog.txt
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/origin.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-abs.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-ack.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-chap1.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-chap2.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-chap3.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-concl.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-copy.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-encl1.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/chap/pkuthss-intro.tex
%{_texmfdistdir}/doc/latex/pkuthss/readme/latexmkrc
%{_texmfdistdir}/doc/latex/pkuthss/readme/pkuthss-english.patch
%{_texmfdistdir}/doc/latex/pkuthss/readme/pkuthss.bib
%{_texmfdistdir}/doc/latex/pkuthss/readme/pkuthss.tex

%files -n texlive-pkuthss
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/pkuthss/pkulogo.eps
%{_texmfdistdir}/tex/latex/pkuthss/pkulogo.pdf
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-gbk.def
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-utf8.def
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss.cls
%{_texmfdistdir}/tex/latex/pkuthss/pkuword.eps
%{_texmfdistdir}/tex/latex/pkuthss/pkuword.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pkuthss-%{texlive_version}.%{texlive_noarch}.1.9.0svn58729-%{release}-zypper
%endif

%package -n texlive-pl
Version:        %{texlive_version}.%{texlive_noarch}.1.09asvn58661
Release:        0
License:        SUSE-Public-Domain
Summary:        Polish extension of Computer Modern fonts
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun):findutils
Requires(postun):grep
Requires(postun):sed
Requires(postun):texlive >= %{texlive_version}
Requires(postun):tex(updmap.cfg)
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Requires:       texlive-pl-fonts >= %{texlive_version}
Recommends:     texlive-pl-doc >= %{texlive_version}
Provides:       tex(plb10.tfm)
Provides:       tex(plbsy10.tfm)
Provides:       tex(plbsy5.tfm)
Provides:       tex(plbsy7.tfm)
Provides:       tex(plbx10.tfm)
Provides:       tex(plbx12.tfm)
Provides:       tex(plbx5.tfm)
Provides:       tex(plbx6.tfm)
Provides:       tex(plbx7.tfm)
Provides:       tex(plbx8.tfm)
Provides:       tex(plbx9.tfm)
Provides:       tex(plbxsl10.tfm)
Provides:       tex(plbxti10.tfm)
Provides:       tex(plcsc10.tfm)
Provides:       tex(pldunh10.tfm)
Provides:       tex(plex10.tfm)
Provides:       tex(plex9.tfm)
Provides:       tex(plff10.tfm)
Provides:       tex(plfi10.tfm)
Provides:       tex(plfib8.tfm)
Provides:       tex(plin.enc)
Provides:       tex(plinch.tfm)
Provides:       tex(plit.enc)
Provides:       tex(plitt.enc)
Provides:       tex(plitt10.tfm)
Provides:       tex(plme.enc)
Provides:       tex(plmi.enc)
Provides:       tex(plmi10.tfm)
Provides:       tex(plmi12.tfm)
Provides:       tex(plmi5.tfm)
Provides:       tex(plmi6.tfm)
Provides:       tex(plmi7.tfm)
Provides:       tex(plmi8.tfm)
Provides:       tex(plmi9.tfm)
Provides:       tex(plmib10.tfm)
Provides:       tex(plmib5.tfm)
Provides:       tex(plmib7.tfm)
Provides:       tex(plms.enc)
Provides:       tex(plother.map)
Provides:       tex(plr10.tfm)
Provides:       tex(plr12.tfm)
Provides:       tex(plr17.tfm)
Provides:       tex(plr5.tfm)
Provides:       tex(plr6.tfm)
Provides:       tex(plr7.tfm)
Provides:       tex(plr8.tfm)
Provides:       tex(plr9.tfm)
Provides:       tex(plrm.enc)
Provides:       tex(plsc.enc)
Provides:       tex(plsl10.tfm)
Provides:       tex(plsl12.tfm)
Provides:       tex(plsl8.tfm)
Provides:       tex(plsl9.tfm)
Provides:       tex(plsltt10.tfm)
Provides:       tex(plss10.tfm)
Provides:       tex(plss12.tfm)
Provides:       tex(plss17.tfm)
Provides:       tex(plss8.tfm)
Provides:       tex(plss9.tfm)
Provides:       tex(plssbi10.tfm)
Provides:       tex(plssbx10.tfm)
Provides:       tex(plssdc10.tfm)
Provides:       tex(plssi10.tfm)
Provides:       tex(plssi12.tfm)
Provides:       tex(plssi17.tfm)
Provides:       tex(plssi8.tfm)
Provides:       tex(plssi9.tfm)
Provides:       tex(plssq8.tfm)
Provides:       tex(plssqi8.tfm)
Provides:       tex(plsy10.tfm)
Provides:       tex(plsy5.tfm)
Provides:       tex(plsy6.tfm)
Provides:       tex(plsy7.tfm)
Provides:       tex(plsy8.tfm)
Provides:       tex(plsy9.tfm)
Provides:       tex(pltcsc10.tfm)
Provides:       tex(plte.enc)
Provides:       tex(pltex10.tfm)
Provides:       tex(pltex8.tfm)
Provides:       tex(pltex9.tfm)
Provides:       tex(pltext.map)
Provides:       tex(plti10.tfm)
Provides:       tex(plti12.tfm)
Provides:       tex(plti7.tfm)
Provides:       tex(plti8.tfm)
Provides:       tex(plti9.tfm)
Provides:       tex(pltt.enc)
Provides:       tex(pltt10.tfm)
Provides:       tex(pltt12.tfm)
Provides:       tex(pltt8.tfm)
Provides:       tex(pltt9.tfm)
Provides:       tex(plu10.tfm)
Provides:       tex(plvtt10.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source279:      pl.tar.xz
Source280:      pl.doc.tar.xz

%description -n texlive-pl
The Polish extension of the Computer Modern fonts (compatible
with CM itself) for use with Polish TeX formats. The fonts were
originally a part of the MeX distribution (and they are still
available that way).

%package -n texlive-pl-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.09asvn58661
Release:        0
Summary:        Documentation for texlive-pl
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-pl-doc
This package includes the documentation for texlive-pl

%package -n texlive-pl-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.09asvn58661
Release:        0
Summary:        Severed fonts for texlive-pl
License:        SUSE-Public-Domain
URL:            http://www.tug.org/texlive/
Group:          Productivity/Publishing/TeX/Fonts
%reconfigure_fonts_prereq
Requires(posttrans):fontconfig
Requires(posttrans):ghostscript-fonts-std
Requires(posttrans):mkfontdir
Requires(posttrans):mkfontscale
Requires(posttrans):xorg-x11-fonts-core

%description -n texlive-pl-fonts
The  separated fonts package for texlive-pl

%post -n texlive-pl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap plother.map' >> /var/run/texlive/run-updmap
echo 'addMixedMap pltext.map' >> /var/run/texlive/run-updmap

%postun -n texlive-pl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap plother.map' >> /var/run/texlive/run-updmap
    echo 'deleteMixedMap pltext.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-pl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-pl-fonts

%files -n texlive-pl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/pl/README-T1.ENG
%{_texmfdistdir}/doc/fonts/pl/README-T1.POL
%{_texmfdistdir}/doc/fonts/pl/README.ENG
%{_texmfdistdir}/doc/fonts/pl/README.POL
%{_texmfdistdir}/doc/fonts/pl/plsample.tex

%files -n texlive-pl
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/pl/config.pl
%{_texmfdistdir}/fonts/afm/public/pl/plb10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbsy10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbx9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbxsl10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plbxti10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plcsc10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pldunh10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plex10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plex9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plff10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plfi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plfib8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plinch.afm
%{_texmfdistdir}/fonts/afm/public/pl/plitt10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmi9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plmib10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr17.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plr9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsl9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsltt10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss17.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plss9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssbi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssbx10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssdc10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi17.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssi9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssq8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plssqi8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy5.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy6.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plsy9.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltcsc10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltex10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltex8.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltex9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti12.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti7.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti8.afm
%{_texmfdistdir}/fonts/afm/public/pl/plti9.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt10.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt12.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt8.afm
%{_texmfdistdir}/fonts/afm/public/pl/pltt9.afm
%{_texmfdistdir}/fonts/afm/public/pl/plu10.afm
%{_texmfdistdir}/fonts/afm/public/pl/plvtt10.afm
%{_texmfdistdir}/fonts/enc/dvips/pl/plin.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plit.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plitt.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plme.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plmi.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plms.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plrm.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plsc.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/plte.enc
%{_texmfdistdir}/fonts/enc/dvips/pl/pltt.enc
%{_texmfdistdir}/fonts/map/dvips/pl/plother.map
%{_texmfdistdir}/fonts/map/dvips/pl/pltext.map
%{_texmfdistdir}/fonts/source/public/pl/cmssbi10.mf
%{_texmfdistdir}/fonts/source/public/pl/dlr10.mf
%{_texmfdistdir}/fonts/source/public/pl/fik_mik.mf
%{_texmfdistdir}/fonts/source/public/pl/pl.mft
%{_texmfdistdir}/fonts/source/public/pl/pl_cud.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_dl.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_dod.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_ml.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_mlk.mf
%{_texmfdistdir}/fonts/source/public/pl/pl_sym.mf
%{_texmfdistdir}/fonts/source/public/pl/plb10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbsy10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbsy5.mf
%{_texmfdistdir}/fonts/source/public/pl/plbsy7.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx12.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx5.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx6.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx7.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx8.mf
%{_texmfdistdir}/fonts/source/public/pl/plbx9.mf
%{_texmfdistdir}/fonts/source/public/pl/plbxsl10.mf
%{_texmfdistdir}/fonts/source/public/pl/plbxti10.mf
%{_texmfdistdir}/fonts/source/public/pl/plcsc10.mf
%{_texmfdistdir}/fonts/source/public/pl/pldunh10.mf
%{_texmfdistdir}/fonts/source/public/pl/plex10.mf
%{_texmfdistdir}/fonts/source/public/pl/plff10.mf
%{_texmfdistdir}/fonts/source/public/pl/plfi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plfib8.mf
%{_texmfdistdir}/fonts/source/public/pl/plinch.mf
%{_texmfdistdir}/fonts/source/public/pl/plitt10.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi12.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi5.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi6.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi7.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi8.mf
%{_texmfdistdir}/fonts/source/public/pl/plmi9.mf
%{_texmfdistdir}/fonts/source/public/pl/plmib10.mf
%{_texmfdistdir}/fonts/source/public/pl/plmib5.mf
%{_texmfdistdir}/fonts/source/public/pl/plmib7.mf
%{_texmfdistdir}/fonts/source/public/pl/plr10.mf
%{_texmfdistdir}/fonts/source/public/pl/plr12.mf
%{_texmfdistdir}/fonts/source/public/pl/plr17.mf
%{_texmfdistdir}/fonts/source/public/pl/plr5.mf
%{_texmfdistdir}/fonts/source/public/pl/plr6.mf
%{_texmfdistdir}/fonts/source/public/pl/plr7.mf
%{_texmfdistdir}/fonts/source/public/pl/plr8.mf
%{_texmfdistdir}/fonts/source/public/pl/plr9.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl10.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl12.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl8.mf
%{_texmfdistdir}/fonts/source/public/pl/plsl9.mf
%{_texmfdistdir}/fonts/source/public/pl/plsltt10.mf
%{_texmfdistdir}/fonts/source/public/pl/plss10.mf
%{_texmfdistdir}/fonts/source/public/pl/plss12.mf
%{_texmfdistdir}/fonts/source/public/pl/plss17.mf
%{_texmfdistdir}/fonts/source/public/pl/plss8.mf
%{_texmfdistdir}/fonts/source/public/pl/plss9.mf
%{_texmfdistdir}/fonts/source/public/pl/plssbi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssbx10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssdc10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi10.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi12.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi17.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi8.mf
%{_texmfdistdir}/fonts/source/public/pl/plssi9.mf
%{_texmfdistdir}/fonts/source/public/pl/plssq8.mf
%{_texmfdistdir}/fonts/source/public/pl/plssqi8.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy10.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy5.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy6.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy7.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy8.mf
%{_texmfdistdir}/fonts/source/public/pl/plsy9.mf
%{_texmfdistdir}/fonts/source/public/pl/pltcsc10.mf
%{_texmfdistdir}/fonts/source/public/pl/pltex10.mf
%{_texmfdistdir}/fonts/source/public/pl/pltex8.mf
%{_texmfdistdir}/fonts/source/public/pl/pltex9.mf
%{_texmfdistdir}/fonts/source/public/pl/plti10.mf
%{_texmfdistdir}/fonts/source/public/pl/plti12.mf
%{_texmfdistdir}/fonts/source/public/pl/plti7.mf
%{_texmfdistdir}/fonts/source/public/pl/plti8.mf
%{_texmfdistdir}/fonts/source/public/pl/plti9.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt10.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt12.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt8.mf
%{_texmfdistdir}/fonts/source/public/pl/pltt9.mf
%{_texmfdistdir}/fonts/source/public/pl/plu10.mf
%{_texmfdistdir}/fonts/source/public/pl/plvtt10.mf
%{_texmfdistdir}/fonts/source/public/pl/polan.mf
%{_texmfdistdir}/fonts/source/public/pl/polkap.mf
%{_texmfdistdir}/fonts/source/public/pl/polkur.mf
%{_texmfdistdir}/fonts/source/public/pl/polmat.mf
%{_texmfdistdir}/fonts/source/public/pl/poltyt.mf
%{_texmfdistdir}/fonts/tfm/public/pl/plb10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pldunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plex10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plex9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plff10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plfi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plinch.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmi9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmib10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmib5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plmib7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr17.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plr9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss17.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plss9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy5.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy6.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plsy9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltex10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltex8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltex9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti7.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plti9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt12.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt8.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/pltt9.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plu10.tfm
%{_texmfdistdir}/fonts/tfm/public/pl/plvtt10.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plb10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plb10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbsy10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbsy10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbx10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbx12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbx5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx5.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbx6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbx7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx7.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbx8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbx9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbx9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbxsl10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbxsl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plbxti10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plbxti10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plcsc10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plcsc10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pldunh10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pldunh10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plex10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plex10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plex9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plex9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plff10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plff10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plfi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plfi10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plfib8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plfib8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plinch.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plinch.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plitt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plitt10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmi12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmi5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi5.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmi6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmi7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi7.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmi8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmi9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmi9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plmib10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plmib10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr17.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr5.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr7.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plr9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plr9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsl10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsl12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsl8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsl9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsl9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsltt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsltt10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plss10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plss12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plss17.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plss8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plss9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plss9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssbi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssbi10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssbx10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssbx10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssdc10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssdc10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssi10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssi12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssi17.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi17.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssi8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssi9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssi9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssq8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssq8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plssqi8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plssqi8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsy10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsy5.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy5.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsy6.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy6.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsy7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy7.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsy8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plsy9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plsy9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltcsc10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltcsc10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltex10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltex10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltex8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltex8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltex9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltex9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plti10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plti12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plti7.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti7.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plti8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plti9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plti9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltt12.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt12.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltt8.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt8.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/pltt9.pfb
%{_texmfdistdir}/fonts/type1/public/pl/pltt9.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plu10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plu10.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/pl/plvtt10.pfb
%{_texmfdistdir}/fonts/type1/public/pl/plvtt10.pfm

%files -n texlive-pl-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-pl
%{_datadir}/fontconfig/conf.avail/58-texlive-pl.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pl/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pl/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-pl/fonts.scale
%{_datadir}/fonts/texlive-pl/plb10.pfb
%{_datadir}/fonts/texlive-pl/plbsy10.pfb
%{_datadir}/fonts/texlive-pl/plbx10.pfb
%{_datadir}/fonts/texlive-pl/plbx12.pfb
%{_datadir}/fonts/texlive-pl/plbx5.pfb
%{_datadir}/fonts/texlive-pl/plbx6.pfb
%{_datadir}/fonts/texlive-pl/plbx7.pfb
%{_datadir}/fonts/texlive-pl/plbx8.pfb
%{_datadir}/fonts/texlive-pl/plbx9.pfb
%{_datadir}/fonts/texlive-pl/plbxsl10.pfb
%{_datadir}/fonts/texlive-pl/plbxti10.pfb
%{_datadir}/fonts/texlive-pl/plcsc10.pfb
%{_datadir}/fonts/texlive-pl/pldunh10.pfb
%{_datadir}/fonts/texlive-pl/plex10.pfb
%{_datadir}/fonts/texlive-pl/plex9.pfb
%{_datadir}/fonts/texlive-pl/plff10.pfb
%{_datadir}/fonts/texlive-pl/plfi10.pfb
%{_datadir}/fonts/texlive-pl/plfib8.pfb
%{_datadir}/fonts/texlive-pl/plinch.pfb
%{_datadir}/fonts/texlive-pl/plitt10.pfb
%{_datadir}/fonts/texlive-pl/plmi10.pfb
%{_datadir}/fonts/texlive-pl/plmi12.pfb
%{_datadir}/fonts/texlive-pl/plmi5.pfb
%{_datadir}/fonts/texlive-pl/plmi6.pfb
%{_datadir}/fonts/texlive-pl/plmi7.pfb
%{_datadir}/fonts/texlive-pl/plmi8.pfb
%{_datadir}/fonts/texlive-pl/plmi9.pfb
%{_datadir}/fonts/texlive-pl/plmib10.pfb
%{_datadir}/fonts/texlive-pl/plr10.pfb
%{_datadir}/fonts/texlive-pl/plr12.pfb
%{_datadir}/fonts/texlive-pl/plr17.pfb
%{_datadir}/fonts/texlive-pl/plr5.pfb
%{_datadir}/fonts/texlive-pl/plr6.pfb
%{_datadir}/fonts/texlive-pl/plr7.pfb
%{_datadir}/fonts/texlive-pl/plr8.pfb
%{_datadir}/fonts/texlive-pl/plr9.pfb
%{_datadir}/fonts/texlive-pl/plsl10.pfb
%{_datadir}/fonts/texlive-pl/plsl12.pfb
%{_datadir}/fonts/texlive-pl/plsl8.pfb
%{_datadir}/fonts/texlive-pl/plsl9.pfb
%{_datadir}/fonts/texlive-pl/plsltt10.pfb
%{_datadir}/fonts/texlive-pl/plss10.pfb
%{_datadir}/fonts/texlive-pl/plss12.pfb
%{_datadir}/fonts/texlive-pl/plss17.pfb
%{_datadir}/fonts/texlive-pl/plss8.pfb
%{_datadir}/fonts/texlive-pl/plss9.pfb
%{_datadir}/fonts/texlive-pl/plssbi10.pfb
%{_datadir}/fonts/texlive-pl/plssbx10.pfb
%{_datadir}/fonts/texlive-pl/plssdc10.pfb
%{_datadir}/fonts/texlive-pl/plssi10.pfb
%{_datadir}/fonts/texlive-pl/plssi12.pfb
%{_datadir}/fonts/texlive-pl/plssi17.pfb
%{_datadir}/fonts/texlive-pl/plssi8.pfb
%{_datadir}/fonts/texlive-pl/plssi9.pfb
%{_datadir}/fonts/texlive-pl/plssq8.pfb
%{_datadir}/fonts/texlive-pl/plssqi8.pfb
%{_datadir}/fonts/texlive-pl/plsy10.pfb
%{_datadir}/fonts/texlive-pl/plsy5.pfb
%{_datadir}/fonts/texlive-pl/plsy6.pfb
%{_datadir}/fonts/texlive-pl/plsy7.pfb
%{_datadir}/fonts/texlive-pl/plsy8.pfb
%{_datadir}/fonts/texlive-pl/plsy9.pfb
%{_datadir}/fonts/texlive-pl/pltcsc10.pfb
%{_datadir}/fonts/texlive-pl/pltex10.pfb
%{_datadir}/fonts/texlive-pl/pltex8.pfb
%{_datadir}/fonts/texlive-pl/pltex9.pfb
%{_datadir}/fonts/texlive-pl/plti10.pfb
%{_datadir}/fonts/texlive-pl/plti12.pfb
%{_datadir}/fonts/texlive-pl/plti7.pfb
%{_datadir}/fonts/texlive-pl/plti8.pfb
%{_datadir}/fonts/texlive-pl/plti9.pfb
%{_datadir}/fonts/texlive-pl/pltt10.pfb
%{_datadir}/fonts/texlive-pl/pltt12.pfb
%{_datadir}/fonts/texlive-pl/pltt8.pfb
%{_datadir}/fonts/texlive-pl/pltt9.pfb
%{_datadir}/fonts/texlive-pl/plu10.pfb
%{_datadir}/fonts/texlive-pl/plvtt10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-pl-fonts-%{texlive_version}.%{texlive_noarch}.1.09asvn58661-%{release}-zypper
%endif

%package -n texlive-placeat
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1d1svn45145
Release:        0
License:        LPPL-1.0
Summary:        Absolute content positioning
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-placeat-doc >= %{texlive_version}
Provides:       tex(placeat.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(luacode.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source281:      placeat.tar.xz
Source282:      placeat.doc.tar.xz

%description -n texlive-placeat
The package provides commands so that the user of LuaLaTeX may
position arbitrary content at any position specified by
absolute coordinates on the page. The package draws a grid on
each page of the document, to aid positioning (the grid may be
disabled, for 'final copy' using the command \placeatsetup).

%package -n texlive-placeat-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1d1svn45145
Release:        0
Summary:        Documentation for texlive-placeat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-placeat-doc
This package includes the documentation for texlive-placeat

%post -n texlive-placeat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-placeat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-placeat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-placeat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/placeat/README.md
%{_texmfdistdir}/doc/lualatex/placeat/placeat.pdf
%{_texmfdistdir}/doc/lualatex/placeat/placeat.tex

%files -n texlive-placeat
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/placeat/placeat.lua
%{_texmfdistdir}/tex/lualatex/placeat/placeat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-placeat-%{texlive_version}.%{texlive_noarch}.0.0.1d1svn45145-%{release}-zypper
%endif

%package -n texlive-placeins
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn19848
Release:        0
License:        SUSE-Public-Domain
Summary:        Control float placement
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-placeins-doc >= %{texlive_version}
Provides:       tex(placeins.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source283:      placeins.tar.xz
Source284:      placeins.doc.tar.xz

%description -n texlive-placeins
Defines a \FloatBarrier command, beyond which floats may not
pass; useful, for example, to ensure all floats for a section
appear before the next \section command.

%package -n texlive-placeins-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn19848
Release:        0
Summary:        Documentation for texlive-placeins
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-placeins-doc
This package includes the documentation for texlive-placeins

%post -n texlive-placeins
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-placeins
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-placeins
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-placeins-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/placeins/placeins-doc.pdf
%{_texmfdistdir}/doc/latex/placeins/placeins-doc.tex
%{_texmfdistdir}/doc/latex/placeins/placeins.txt

%files -n texlive-placeins
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/placeins/placeins.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-placeins-%{texlive_version}.%{texlive_noarch}.2.2svn19848-%{release}-zypper
%endif

%package -n texlive-placeins-plain
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
License:        SUSE-Public-Domain
Summary:        Insertions that keep their place
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       tex(placeins.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source285:      placeins-plain.tar.xz

%description -n texlive-placeins-plain
This TeX file provides various mechanisms (for plain TeX and
close relatives) to let insertions (footnotes, topins, pageins,
etc.) float within their appropriate section, but to prevent
them from intruding into the following section, even when
sections do not normally begin a new page. (If your sections
normally begin a new page, just use \supereject to flush out
insertions.)

%post -n texlive-placeins-plain
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-placeins-plain
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-placeins-plain
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-placeins-plain
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/placeins-plain/placeins.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-placeins-plain-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif

%package -n texlive-plain
Version:        %{texlive_version}.%{texlive_noarch}.3.141592653svn57963
Release:        0
License:        SUSE-TeX
Summary:        The Plain TeX format
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Provides:       tex(fontchart.tex)
Provides:       tex(gkpmac.tex)
Provides:       tex(letterformat.tex)
Provides:       tex(list-latin.tex)
Provides:       tex(list.tex)
Provides:       tex(llist-latin.tex)
Provides:       tex(llist.tex)
Provides:       tex(mptmac.tex)
Provides:       tex(pdftexmagfix.tex)
Provides:       tex(picmac.tex)
Provides:       tex(plain.tex)
Provides:       tex(wlist.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source286:      plain.tar.xz

%description -n texlive-plain
Contains files used to build the Plain TeX format, as described
in the TeXbook, together with various supporting files (some
also discussed in the book).

%post -n texlive-plain
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plain
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plain
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plain
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/plain/plaintex.ist
%{_texmfdistdir}/tex/plain/base/fontchart.tex
%{_texmfdistdir}/tex/plain/base/gkpmac.tex
%{_texmfdistdir}/tex/plain/base/letterformat.tex
%{_texmfdistdir}/tex/plain/base/list-latin.tex
%{_texmfdistdir}/tex/plain/base/list.tex
%{_texmfdistdir}/tex/plain/base/llist-latin.tex
%{_texmfdistdir}/tex/plain/base/llist.tex
%{_texmfdistdir}/tex/plain/base/mptmac.tex
%{_texmfdistdir}/tex/plain/base/picmac.tex
%{_texmfdistdir}/tex/plain/base/plain.tex
%{_texmfdistdir}/tex/plain/base/wlist.tex
%{_texmfdistdir}/tex/plain/config/aleph.ini
%{_texmfdistdir}/tex/plain/config/bplain.ini
%{_texmfdistdir}/tex/plain/config/etex.ini
%{_texmfdistdir}/tex/plain/config/omega.ini
%{_texmfdistdir}/tex/plain/config/pdfbplain.ini
%{_texmfdistdir}/tex/plain/config/pdfetex.ini
%{_texmfdistdir}/tex/plain/config/pdftexmagfix.tex
%{_texmfdistdir}/tex/plain/config/tex.ini
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-plain-%{texlive_version}.%{texlive_noarch}.3.141592653svn57963-%{release}-zypper
%endif

%package -n texlive-plain-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn28424
Release:        0
License:        SUSE-Public-Domain
Summary:        A list of plain.tex cs names
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source287:      plain-doc.doc.tar.xz

%description -n texlive-plain-doc
The document constitutes a list of every control sequence name
(csname) described in the TeXbook, together with an indication
of whether the csname is a primitive TeX command, or is defined
in plain.tex

%post -n texlive-plain-doc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plain-doc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plain-doc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plain-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/plain-doc/csname.txt
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-plain-doc-%{texlive_version}.%{texlive_noarch}.svn28424-%{release}-zypper
%endif

%package -n texlive-plainpkg
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn27765
Release:        0
License:        LPPL-1.0
Summary:        A minimal method for making generic packages
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-plainpkg-doc >= %{texlive_version}
Provides:       tex(plainpkg.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source288:      plainpkg.tar.xz
Source289:      plainpkg.doc.tar.xz

%description -n texlive-plainpkg
The package provides a minimal method for making generic (i.e.,
TeX-format-independent) packaged, combining maybeload
functionality, fallback definitions for LaTeX \ProvidesPackage
and \RequirePackage functionality, and handling of arbitrary
(multiple) "private letters" (analagous LaTeX packages' use of
"@") in nested package files. The documentation contains a
central reference for making and using generic packages based
on the package.

%package -n texlive-plainpkg-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn27765
Release:        0
Summary:        Documentation for texlive-plainpkg
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-plainpkg-doc
This package includes the documentation for texlive-plainpkg

%post -n texlive-plainpkg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plainpkg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plainpkg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plainpkg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/plainpkg/README
%{_texmfdistdir}/doc/generic/plainpkg/SrcFILEs.txt
%{_texmfdistdir}/doc/generic/plainpkg/plainpkg-doc.pdf

%files -n texlive-plainpkg
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/plainpkg/plainpkg.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-plainpkg-%{texlive_version}.%{texlive_noarch}.0.0.4asvn27765-%{release}-zypper
%endif

%package -n texlive-plainyr
Version:        %{texlive_version}.%{texlive_noarch}.svn52783
Release:        0
License:        LPPL-1.0
Summary:        Plain bibliography style, sorted by year first
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source290:      plainyr.tar.xz

%description -n texlive-plainyr
This is a version of the standard plain BibTeX style, modified
to sort chronologically (by year) first, then by author, title,
etc. (The style's name isn't what the author submitted: it was
renamed for clarity.)

%post -n texlive-plainyr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plainyr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plainyr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plainyr
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/plainyr/plainyr.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-plainyr-%{texlive_version}.%{texlive_noarch}.svn52783-%{release}-zypper
%endif

%package -n texlive-plantslabels
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn29803
Release:        0
License:        LPPL-1.0
Summary:        Write labels for plants
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-plantslabels-doc >= %{texlive_version}
Provides:       tex(plantslabels.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(labels.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source291:      plantslabels.tar.xz
Source292:      plantslabels.doc.tar.xz

%description -n texlive-plantslabels
The package defines a command \plant, which has three mandatory
and seven optional argument. The package uses the labels

%package -n texlive-plantslabels-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn29803
Release:        0
Summary:        Documentation for texlive-plantslabels
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-plantslabels-doc
This package includes the documentation for texlive-plantslabels

%post -n texlive-plantslabels
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plantslabels
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plantslabels
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plantslabels-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/plantslabels/README
%{_texmfdistdir}/doc/latex/plantslabels/doc/pdf/plantslabels.pdf
%{_texmfdistdir}/doc/latex/plantslabels/doc/tex/Makefile
%{_texmfdistdir}/doc/latex/plantslabels/doc/tex/perso.ist
%{_texmfdistdir}/doc/latex/plantslabels/doc/tex/plantslabels.forlisting
%{_texmfdistdir}/doc/latex/plantslabels/doc/tex/plantslabels.tex
%{_texmfdistdir}/doc/latex/plantslabels/example/pdf/example.pdf
%{_texmfdistdir}/doc/latex/plantslabels/example/tex/cactus.eps
%{_texmfdistdir}/doc/latex/plantslabels/example/tex/example.tex

%files -n texlive-plantslabels
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/plantslabels/plantslabels.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-plantslabels-%{texlive_version}.%{texlive_noarch}.1.0svn29803-%{release}-zypper
%endif

%package -n texlive-plantuml
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.1svn55214
Release:        0
License:        LPPL-1.0
Summary:        Support for rendering UML diagrams using the syntax and tool of PlantUML
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre):  texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun):coreutils
Requires(postun):texlive >= %{texlive_version}
Requires(postun):texlive-filesystem >= %{texlive_version}
Requires(postun):texlive-kpathsea-bin >= %{texlive_version}
Requires(postun):texlive-kpathsea >= %{texlive_version}
Requires(postun):texlive-scripts-bin >= %{texlive_version}
Requires(postun):texlive-scripts >= %{texlive_version}
Requires(posttrans):coreutils
Requires(posttrans):ed
Requires(posttrans):findutils
Requires(posttrans):grep
Requires(posttrans):sed
Requires(posttrans):texlive >= %{texlive_version}
Requires(posttrans):texlive-filesystem >= %{texlive_version}
Requires(posttrans):texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans):texlive-kpathsea >= %{texlive_version}
Requires(posttrans):texlive-scripts-bin >= %{texlive_version}
Requires(posttrans):texlive-scripts >= %{texlive_version}
Recommends:     texlive-plantuml-doc >= %{texlive_version}
Provides:       tex(plantuml.sty)
Requires:       tex(adjustbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(luacode.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(pythontex.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20210325
Source293:      plantuml.tar.xz
Source294:      plantuml.doc.tar.xz

%description -n texlive-plantuml
The package provides support for rendering UML diagrams using
the syntax and tools of PlantUML. The PlantUML syntax is very
short and thus enables quickly specifying UML diagrams. Using
dot, PlantUML layouts the diagrams.

%package -n texlive-plantuml-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.1svn55214
Release:        0
Summary:        Documentation for texlive-plantuml
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-plantuml-doc
This package includes the documentation for texlive-plantuml

%post -n texlive-plantuml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-plantuml
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-plantuml
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-plantuml-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/plantuml/CHANGELOG.md
%{_texmfdistdir}/doc/lualatex/plantuml/README.md
%{_texmfdistdir}/doc/lualatex/plantuml/example-class-relations--latex.tex
%{_texmfdistdir}/doc/lualatex/plantuml/example-class-relations--svg.png
%{_texmfdistdir}/doc/lualatex/plantuml/example-class-relations--svg.tex
%{_texmfdistdir}/doc/lualatex/plantuml/example-component-diagram.tex
%{_texmfdistdir}/doc/lualatex/plantuml/example-minimal.png
%{_texmfdistdir}/doc/lualatex/plantuml/example-minimal.tex
%{_texmfdistdir}/doc/lualatex/plantuml/plantuml.pdf
%{_texmfdistdir}/doc/lualatex/plantuml/release.sh

%files -n texlive-plantuml
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/lualatex/plantuml/plantuml.lua
%{_texmfdistdir}/tex/lualatex/plantuml/plantuml.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-plantuml-%{texlive_version}.%{texlive_noarch}.0.0.3.1svn55214-%{release}-zypper
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
       %{buildroot}/var/adm/update-scripts/texlive-overlays-%{texlive_version}.%{texlive_noarch}.2.12svn57866-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-overlock-fonts-%{texlive_version}.%{texlive_noarch}.svn56079-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-overlock
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/tipo/overlock/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/tipo/overlock/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-overlock
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-overlock/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-overlock/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-overlock/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-overlock/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-overlock.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-overlock    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-overlock/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-overlock.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-overlock/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-overlock.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-overlock.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-overpic-%{texlive_version}.%{texlive_noarch}.1.3svn53889-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pacioli-%{texlive_version}.%{texlive_noarch}.svn24947-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-padauk-fonts-%{texlive_version}.%{texlive_noarch}.3.002svn42617-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-padauk
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/padauk/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-padauk
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-padauk/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-padauk/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-padauk/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-padauk/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-padauk.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-padauk    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-padauk/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-padcount-%{texlive_version}.%{texlive_noarch}.1.0svn47621-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pagecolor-%{texlive_version}.%{texlive_noarch}.1.0isvn44487-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pagecont-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pagenote-%{texlive_version}.%{texlive_noarch}.1.1asvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pagerange-%{texlive_version}.%{texlive_noarch}.0.0.5svn16915-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pagesel-%{texlive_version}.%{texlive_noarch}.1.10svn56105-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pageslts-%{texlive_version}.%{texlive_noarch}.1.2fsvn39164-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-palatino-fonts-%{texlive_version}.%{texlive_noarch}.svn31835-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-palatino
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/urw/palatino/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-palatino
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-palatino/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-palatino/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-palatino/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-palatino/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-palatino.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-palatino    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-palatino/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-paper-%{texlive_version}.%{texlive_noarch}.1.0lsvn34521-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-papercdcase-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-papermas-%{texlive_version}.%{texlive_noarch}.1.0hsvn23667-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-papertex-%{texlive_version}.%{texlive_noarch}.1.2bsvn19230-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-paracol-%{texlive_version}.%{texlive_noarch}.1.35svn49560-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-parades-%{texlive_version}.%{texlive_noarch}.svn40042-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-paralist-%{texlive_version}.%{texlive_noarch}.2.7svn43021-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-parallel-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-paratype-fonts-%{texlive_version}.%{texlive_noarch}.svn32859-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-paratype
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/paratype/ptmono/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/truetype/paratype/ptsans/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/truetype/paratype/ptserif/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/paratype/ptmono/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/paratype/ptsans/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/paratype/ptserif/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-paratype
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-paratype/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-paratype/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-paratype/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-paratype/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-paratype.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-paratype    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-paratype/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-paratype.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-paratype/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-paratype.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-paratype.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-paresse-%{texlive_version}.%{texlive_noarch}.5.0.1svn56621-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-parnotes-%{texlive_version}.%{texlive_noarch}.3bsvn51720-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-parrun-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-parsa-%{texlive_version}.%{texlive_noarch}.1.3svn54840-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-parselines-%{texlive_version}.%{texlive_noarch}.1.4svn21475-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-parskip-%{texlive_version}.%{texlive_noarch}.2.0hsvn58358-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pas-cours-%{texlive_version}.%{texlive_noarch}.1.9svn55859-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mv -vf %{buildroot}%{_texmfdistdir}/doc/latex/pas-cours/macro-solides.tex %{buildroot}%{_texmfdistdir}/tex/latex/pas-cours/macro-solides.tex
    mv -vf %{buildroot}%{_texmfdistdir}/doc/latex/pas-cours/macro-patrons.tex %{buildroot}%{_texmfdistdir}/tex/latex/pas-cours/macro-patrons.tex
    mv -vf %{buildroot}%{_texmfdistdir}/doc/latex/pas-cours/macro-styles.tex %{buildroot}%{_texmfdistdir}/tex/latex/pas-cours/macro-styles.tex
    mv -vf %{buildroot}%{_texmfdistdir}/doc/latex/pas-cours/macro-calculs.tex %{buildroot}%{_texmfdistdir}/tex/latex/pas-cours/macro-calculs.tex
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pas-crosswords-%{texlive_version}.%{texlive_noarch}.1.03svn32313-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pas-cv-%{texlive_version}.%{texlive_noarch}.2.01svn32263-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pas-tableur-%{texlive_version}.%{texlive_noarch}.2.01svn39542-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-passivetex-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-patch-%{texlive_version}.%{texlive_noarch}.svn42428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-patchcmd-%{texlive_version}.%{texlive_noarch}.1.05svn41379-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-patgen-%{texlive_version}.%{texlive_noarch}.2.4svn57972-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-patgen2-tutorial-%{texlive_version}.%{texlive_noarch}.svn16490-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-path-%{texlive_version}.%{texlive_noarch}.3.05svn22045-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pauldoc-%{texlive_version}.%{texlive_noarch}.0.0.5svn16005-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pawpict-%{texlive_version}.%{texlive_noarch}.1.0svn21629-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pax-%{texlive_version}.%{texlive_noarch}.0.0.1lsvn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pax/pdfannotextractor.pl
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
       %{buildroot}/var/adm/update-scripts/texlive-pb-diagram-%{texlive_version}.%{texlive_noarch}.5.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pbalance-%{texlive_version}.%{texlive_noarch}.1.0.1svn57161-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pbibtex-base-%{texlive_version}.%{texlive_noarch}.svn40986-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/ptex/pbibtex/generate.sh
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pbox-%{texlive_version}.%{texlive_noarch}.1.2svn24807-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pbsheet-%{texlive_version}.%{texlive_noarch}.0.0.1svn24830-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdf-trans-%{texlive_version}.%{texlive_noarch}.2.4svn32809-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdf14-%{texlive_version}.%{texlive_noarch}.0.0.1svn17583-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfarticle-%{texlive_version}.%{texlive_noarch}.1.0svn51127-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfbook2-%{texlive_version}.%{texlive_noarch}.1.4svn53521-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pdfbook2/pdfbook2
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
       %{buildroot}/var/adm/update-scripts/texlive-pdfcolmk-%{texlive_version}.%{texlive_noarch}.2.0svn52912-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfcomment-%{texlive_version}.%{texlive_noarch}.2.4asvn49047-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfcprot-%{texlive_version}.%{texlive_noarch}.1.7asvn18735-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfcrop-%{texlive_version}.%{texlive_noarch}.1.40svn55435-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pdfcrop/pdfcrop.pl
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
       %{buildroot}/var/adm/update-scripts/texlive-pdfescape-%{texlive_version}.%{texlive_noarch}.1.15svn53082-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfjam-%{texlive_version}.%{texlive_noarch}.3.03svn56991-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdflatexpicscale-%{texlive_version}.%{texlive_noarch}.0.0.32svn46617-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdflscape-%{texlive_version}.%{texlive_noarch}.0.0.12svn53047-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfmanagement-testphase-%{texlive_version}.%{texlive_noarch}.0.0.95csvn58511-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfmarginpar-%{texlive_version}.%{texlive_noarch}.0.0.92svn23492-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfoverlay-%{texlive_version}.%{texlive_noarch}.1.2asvn57923-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfpagediff-%{texlive_version}.%{texlive_noarch}.1.4svn37946-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfpages-%{texlive_version}.%{texlive_noarch}.0.0.5tsvn58212-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfpc-%{texlive_version}.%{texlive_noarch}.0.0.6.0svn57735-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfpc-movie-%{texlive_version}.%{texlive_noarch}.1.0svn48245-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfprivacy-%{texlive_version}.%{texlive_noarch}.1.0svn45985-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfreview-%{texlive_version}.%{texlive_noarch}.1.2svn50100-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfscreen-%{texlive_version}.%{texlive_noarch}.1.5svn42428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfslide-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfsync-%{texlive_version}.%{texlive_noarch}.svn20373-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdftex-fonts-%{texlive_version}.%{texlive_noarch}.svn57973-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/pdftex/manual/syntaxform.pl
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
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-pdftex
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/pdftex/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-pdftex
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-pdftex/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-pdftex/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pdftex/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pdftex/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-pdftex.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-pdftex    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-pdftex/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdftex-quiet-%{texlive_version}.%{texlive_noarch}.1.1.0svn49169-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdftexcmds-%{texlive_version}.%{texlive_noarch}.0.0.33svn55777-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdftosrc-%{texlive_version}.%{texlive_noarch}.svn57972-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdftricks-%{texlive_version}.%{texlive_noarch}.1.16svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdftricks2-%{texlive_version}.%{texlive_noarch}.1.01svn31016-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfwin-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfx-%{texlive_version}.%{texlive_noarch}.1.6.3svn50338-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pdfxup-%{texlive_version}.%{texlive_noarch}.2.00svn57166-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pecha-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pedigree-perl-%{texlive_version}.%{texlive_noarch}.1.0svn31990-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pedigree-perl/pedigree.pl
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
       %{buildroot}/var/adm/update-scripts/texlive-penrose-%{texlive_version}.%{texlive_noarch}.1.4svn57508-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-perception-%{texlive_version}.%{texlive_noarch}.svn48861-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-perfectcut-%{texlive_version}.%{texlive_noarch}.2.3svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-perltex-%{texlive_version}.%{texlive_noarch}.2.2svn52162-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/perltex/perltex.pl
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
       %{buildroot}/var/adm/update-scripts/texlive-permute-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-persian-bib-%{texlive_version}.%{texlive_noarch}.0.0.9svn37297-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-petiteannonce-%{texlive_version}.%{texlive_noarch}.1.0001svn25915-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-petri-nets-%{texlive_version}.%{texlive_noarch}.svn39165-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pfarrei-%{texlive_version}.%{texlive_noarch}.r36svn31934-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pfarrei/a5toa4.tlu \
	       %{_texmfdistdir}/scripts/pfarrei/pfarrei.tlu
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
       %{buildroot}/var/adm/update-scripts/texlive-pgf-%{texlive_version}.%{texlive_noarch}.3.1.8bsvn57240-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgf-blur-%{texlive_version}.%{texlive_noarch}.1.02svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgf-cmykshadings-%{texlive_version}.%{texlive_noarch}.1.2svn52635-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgf-pie-%{texlive_version}.%{texlive_noarch}.0.0.3svn55342-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgf-soroban-%{texlive_version}.%{texlive_noarch}.1.1svn32269-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgf-spectra-%{texlive_version}.%{texlive_noarch}.2.0.0svn58467-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgf-umlcd-%{texlive_version}.%{texlive_noarch}.0.0.2.1.1svn55342-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgf-umlsd-%{texlive_version}.%{texlive_noarch}.0.0.7svn55342-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgfgantt-%{texlive_version}.%{texlive_noarch}.5.0svn52662-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgfkeyx-%{texlive_version}.%{texlive_noarch}.0.0.0.1svn26093-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgfmolbio-%{texlive_version}.%{texlive_noarch}.0.0.21svn35152-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/pgfmolbio/pgfmolbio.lua
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
       %{buildroot}/var/adm/update-scripts/texlive-pgfmorepages-%{texlive_version}.%{texlive_noarch}.1.20svn54770-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgfopts-%{texlive_version}.%{texlive_noarch}.2.1asvn56615-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgfornament-%{texlive_version}.%{texlive_noarch}.1.2svn55326-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgfornament-han-%{texlive_version}.%{texlive_noarch}.svn54191-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pgfplots-%{texlive_version}.%{texlive_noarch}.1.17svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phaistos-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn18651-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-phaistos
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/phaistos/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/phaistos/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-phaistos
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-phaistos/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-phaistos/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-phaistos/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-phaistos/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-phaistos.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-phaistos    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-phaistos/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-phaistos.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-phaistos/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-phaistos.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-phaistos.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phffullpagefigure-%{texlive_version}.%{texlive_noarch}.1.0svn41857-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phfnote-%{texlive_version}.%{texlive_noarch}.1.0svn41858-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phfparen-%{texlive_version}.%{texlive_noarch}.1.0svn41859-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phfqit-%{texlive_version}.%{texlive_noarch}.2.0svn45084-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phfquotetext-%{texlive_version}.%{texlive_noarch}.1.0svn41869-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phfsvnwatermark-%{texlive_version}.%{texlive_noarch}.1.0svn41870-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phfthm-%{texlive_version}.%{texlive_noarch}.1.0svn41871-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-philex-%{texlive_version}.%{texlive_noarch}.1.3svn36396-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-philokalia-fonts-%{texlive_version}.%{texlive_noarch}.1.2svn45356-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-philokalia
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/philokalia/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-philokalia
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-philokalia/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-philokalia/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-philokalia/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-philokalia/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-philokalia.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-philokalia    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-philokalia/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-philosophersimprint-%{texlive_version}.%{texlive_noarch}.1.5svn56954-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phonenumbers-%{texlive_version}.%{texlive_noarch}.2.2svn51933-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phonetic-%{texlive_version}.%{texlive_noarch}.svn56468-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-phonrule-%{texlive_version}.%{texlive_noarch}.1.3.2svn43963-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-photo-%{texlive_version}.%{texlive_noarch}.svn18739-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-physconst-%{texlive_version}.%{texlive_noarch}.1.1.2svn58727-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-physics-%{texlive_version}.%{texlive_noarch}.1.3svn28590-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-physunits-%{texlive_version}.%{texlive_noarch}.1.2.0svn58728-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-piano-%{texlive_version}.%{texlive_noarch}.1.0svn21574-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-picinpar-%{texlive_version}.%{texlive_noarch}.1.2asvn57349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pict2e-%{texlive_version}.%{texlive_noarch}.0.0.4bsvn56504-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pictex-%{texlive_version}.%{texlive_noarch}.1.1svn21943-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pictex2-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pictexsum-%{texlive_version}.%{texlive_noarch}.svn24965-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-picture-%{texlive_version}.%{texlive_noarch}.1.6svn54867-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-piechartmp-%{texlive_version}.%{texlive_noarch}.0.0.3.0svn19440-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-piff-%{texlive_version}.%{texlive_noarch}.svn21894-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pigpen-fonts-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-pigpen
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/pigpen/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-pigpen
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-pigpen/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-pigpen/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pigpen/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pigpen/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-pigpen.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-pigpen    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-pigpen/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pinlabel-%{texlive_version}.%{texlive_noarch}.1.2svn24769-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pinoutikz-%{texlive_version}.%{texlive_noarch}.1.1.2svn55966-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pitex-%{texlive_version}.%{texlive_noarch}.svn24731-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pittetd-%{texlive_version}.%{texlive_noarch}.1.618svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pixelart-%{texlive_version}.%{texlive_noarch}.0.0.2.0svn57508-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pkfix-%{texlive_version}.%{texlive_noarch}.1.7svn26032-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive
    # Correct wrong perl scripts if any
    for scr in %{_texmfdistdir}/scripts/pkfix/pkfix.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		1,/\sif 0;$/d
		1
		i
		#! /usr/bin/perl
		.
		w
		1,3p
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pkfix-helper-%{texlive_version}.%{texlive_noarch}.1.6svn56061-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/pkfix-helper/pkfix-helper
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
       %{buildroot}/var/adm/update-scripts/texlive-pkgloader-%{texlive_version}.%{texlive_noarch}.0.0.7.0svn47486-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pkuthss-%{texlive_version}.%{texlive_noarch}.1.9.0svn58729-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:277} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:278} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/pkuthss/example/Make.bat
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-pl-fonts-%{texlive_version}.%{texlive_noarch}.1.09asvn58661-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:279} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:280} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-pl
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/pl/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-pl
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-pl/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-pl/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pl/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-pl/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-pl.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-pl    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-pl/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-placeat-%{texlive_version}.%{texlive_noarch}.0.0.1d1svn45145-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:281} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:282} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/scripts/placeat/placeat.lua
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
       %{buildroot}/var/adm/update-scripts/texlive-placeins-%{texlive_version}.%{texlive_noarch}.2.2svn19848-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:283} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:284} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-placeins-plain-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:285} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-plain-%{texlive_version}.%{texlive_noarch}.3.141592653svn57963-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:286} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-plain-doc-%{texlive_version}.%{texlive_noarch}.svn28424-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:287} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-plainpkg-%{texlive_version}.%{texlive_noarch}.0.0.4asvn27765-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:288} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:289} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-plainyr-%{texlive_version}.%{texlive_noarch}.svn52783-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:290} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-plantslabels-%{texlive_version}.%{texlive_noarch}.1.0svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:291} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:292} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-plantuml-%{texlive_version}.%{texlive_noarch}.0.0.3.1svn55214-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:293} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:294} -C %{buildroot}%{_datadir}/texlive/texmf-dist
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
