#
# spec file for package texlive-specs-k
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

Name:           texlive-specs-k
Version:        2020
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for k
License:        Apache-1.0 and GPL-2.0+ and LGPL-2.1+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-k-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-gitfile-info
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn51928
Release:        0
Summary:        Get git metadata for a specific file
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
Recommends:     texlive-gitfile-info-doc >= %{texlive_version}
Provides:       tex(gitfile-info.sty)
Requires:       tex(currfile.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source1:        gitfile-info.tar.xz
Source2:        gitfile-info.doc.tar.xz

%description -n texlive-gitfile-info
If you are using git to control versions of LaTeX-files, you
may want to show yourself or other users or devs the current
version of the file, information about the author and last
edited date. All packages for git known make that kind of
information available for the whole repository. But sometimes
you have a lot of files within the same repository in different
versions, from different authors etc. Perhaps you also split up
a big project in small files and want to show within the
document who had edited what. This package gives you the
opportunity to do so.

%package -n texlive-gitfile-info-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn51928
Release:        0
Summary:        Documentation for texlive-gitfile-info
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gitfile-info-doc
This package includes the documentation for texlive-gitfile-info

%post -n texlive-gitfile-info
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gitfile-info 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gitfile-info
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gitfile-info-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/gitfile-info/README
%{_texmfdistdir}/doc/support/gitfile-info/gfi-run.py
%{_texmfdistdir}/doc/support/gitfile-info/gitfile-info.gfi
%{_texmfdistdir}/doc/support/gitfile-info/gitfile-info.pdf
%{_texmfdistdir}/doc/support/gitfile-info/post-commit.py
%{_texmfdistdir}/doc/support/gitfile-info/post-merge.py

%files -n texlive-gitfile-info
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gitfile-info/gitfile-info.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gitfile-info-%{texlive_version}.%{texlive_noarch}.0.0.5svn51928-%{release}-zypper
%endif

%package -n texlive-gitinfo
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn34049
Release:        0
Summary:        Access metadata from the git distributed version control system
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
Recommends:     texlive-gitinfo-doc >= %{texlive_version}
Provides:       tex(gitinfo.sty)
Provides:       tex(gitsetinfo.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source3:        gitinfo.tar.xz
Source4:        gitinfo.doc.tar.xz

%description -n texlive-gitinfo
The package makes it possible to incorporate git version
control metadata into documents. For memoir users, the package
provides the means to tailor page headers and footers to use
the metadata. Note this version is now deprecated, but is kept
on the archive, pro tem, for continuity for existing users. All
new repositories should use gitinfo2.

%package -n texlive-gitinfo-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn34049
Release:        0
Summary:        Documentation for texlive-gitinfo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gitinfo-doc
This package includes the documentation for texlive-gitinfo

%post -n texlive-gitinfo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gitinfo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gitinfo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gitinfo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gitinfo/README
%{_texmfdistdir}/doc/latex/gitinfo/gitHeadInfo.gin
%{_texmfdistdir}/doc/latex/gitinfo/gitinfo.pdf
%{_texmfdistdir}/doc/latex/gitinfo/gitinfo.tex
%{_texmfdistdir}/doc/latex/gitinfo/post-xxx-sample.txt

%files -n texlive-gitinfo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gitinfo/gitinfo.sty
%{_texmfdistdir}/tex/latex/gitinfo/gitsetinfo.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gitinfo-%{texlive_version}.%{texlive_noarch}.1.0svn34049-%{release}-zypper
%endif

%package -n texlive-gitinfo2
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn38913
Release:        0
Summary:        Access metadata from the git distributed version control system
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
Recommends:     texlive-gitinfo2-doc >= %{texlive_version}
Provides:       tex(gitexinfo.sty)
Provides:       tex(gitinfo2.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source5:        gitinfo2.tar.xz
Source6:        gitinfo2.doc.tar.xz

%description -n texlive-gitinfo2
The package makes it possible to incorporate git version
control metadata into documents. For memoir users, the package
provides the means to tailor page headers and footers to use
the metadata. gitinfo2 is a new release of gitinfo. The changes
to version 2 are not backward-compatible, and the package name
has been changed to avoid impact on existing users'
repositories. All new repositories should use this version of
the package.

%package -n texlive-gitinfo2-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.7svn38913
Release:        0
Summary:        Documentation for texlive-gitinfo2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gitinfo2-doc
This package includes the documentation for texlive-gitinfo2

%post -n texlive-gitinfo2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gitinfo2 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gitinfo2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gitinfo2-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gitinfo2/README
%{_texmfdistdir}/doc/latex/gitinfo2/gitHeadLocal.gin
%{_texmfdistdir}/doc/latex/gitinfo2/gitinfo2.pdf
%{_texmfdistdir}/doc/latex/gitinfo2/gitinfo2.tex
%{_texmfdistdir}/doc/latex/gitinfo2/gitinfotest.tex
%{_texmfdistdir}/doc/latex/gitinfo2/post-xxx-sample.txt

%files -n texlive-gitinfo2
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gitinfo2/gitexinfo.sty
%{_texmfdistdir}/tex/latex/gitinfo2/gitinfo2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gitinfo2-%{texlive_version}.%{texlive_noarch}.2.0.7svn38913-%{release}-zypper
%endif

%package -n texlive-gitlog
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.betasvn38932
Release:        0
Summary:        Typesetting git changelogs
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
Recommends:     texlive-gitlog-doc >= %{texlive_version}
Provides:       tex(gitlog.bbx)
Provides:       tex(gitlog.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source7:        gitlog.tar.xz
Source8:        gitlog.doc.tar.xz

%description -n texlive-gitlog
This package allows git change log history to be incorporated
into LaTeX documents; the log data is obtained from the git
distributed version control system. The current release
(0.0.beta) is a proof-of-concept release to allow users an
early evaluation and to attract ideas and support. Requests and
suggestions, as well as code contributions are welcome.

%package -n texlive-gitlog-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.betasvn38932
Release:        0
Summary:        Documentation for texlive-gitlog
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gitlog-doc
This package includes the documentation for texlive-gitlog

%post -n texlive-gitlog
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gitlog 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gitlog
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gitlog-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gitlog/README.md
%{_texmfdistdir}/doc/latex/gitlog/gitHeadLocal.gin
%{_texmfdistdir}/doc/latex/gitlog/gitlog.pdf
%{_texmfdistdir}/doc/latex/gitlog/gitlog.sample.bib
%{_texmfdistdir}/doc/latex/gitlog/gitlog.tex

%files -n texlive-gitlog
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gitlog/gitlog.bbx
%{_texmfdistdir}/tex/latex/gitlog/gitlog.dbx
%{_texmfdistdir}/tex/latex/gitlog/gitlog.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gitlog-%{texlive_version}.%{texlive_noarch}.0.0.0.betasvn38932-%{release}-zypper
%endif

%package -n texlive-gitver
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49980
Release:        0
Summary:        Get the current git hash of a project and typeset it in the document
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
Recommends:     texlive-gitver-doc >= %{texlive_version}
Provides:       tex(gitver.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(datetime.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source9:        gitver.tar.xz
Source10:       gitver.doc.tar.xz

%description -n texlive-gitver
This package will get a description of the current git version
of the document and store it in a command \gitVer. If memoir or
fancyhdr are in use, it will also add this to the document
footers unless the option "noheader" is passed. The package
also defines a command \versionBox which outputs a box
containing the version and date of compilation.

%package -n texlive-gitver-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49980
Release:        0
Summary:        Documentation for texlive-gitver
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gitver-doc
This package includes the documentation for texlive-gitver

%post -n texlive-gitver
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gitver 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gitver
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gitver-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gitver/COPYING
%{_texmfdistdir}/doc/latex/gitver/ChangeLog
%{_texmfdistdir}/doc/latex/gitver/README.md
%{_texmfdistdir}/doc/latex/gitver/gitver.pdf
%{_texmfdistdir}/doc/latex/gitver/gitver.tex

%files -n texlive-gitver
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gitver/gitver.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gitver-%{texlive_version}.%{texlive_noarch}.1.0svn49980-%{release}-zypper
%endif

%package -n texlive-globalvals
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49962
Release:        0
Summary:        Declare global variables
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
Recommends:     texlive-globalvals-doc >= %{texlive_version}
Provides:       tex(globalvals.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source11:       globalvals.tar.xz
Source12:       globalvals.doc.tar.xz

%description -n texlive-globalvals
This package allows the user to declare a variable which can
then be used anywhere else in a document, including before it
was declared.

%package -n texlive-globalvals-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49962
Release:        0
Summary:        Documentation for texlive-globalvals
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-globalvals-doc
This package includes the documentation for texlive-globalvals

%post -n texlive-globalvals
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-globalvals 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-globalvals
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-globalvals-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/globalvals/COPYING
%{_texmfdistdir}/doc/latex/globalvals/ChangeLog
%{_texmfdistdir}/doc/latex/globalvals/README.md
%{_texmfdistdir}/doc/latex/globalvals/globalvals.pdf
%{_texmfdistdir}/doc/latex/globalvals/globalvals.tex

%files -n texlive-globalvals
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/globalvals/globalvals.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-globalvals-%{texlive_version}.%{texlive_noarch}.1.1svn49962-%{release}-zypper
%endif

%package -n texlive-glosmathtools
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn54558
Release:        0
Summary:        Mathematical nomenclature tools based on the glossaries package
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
Recommends:     texlive-glosmathtools-doc >= %{texlive_version}
Provides:       tex(glosmathtools.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(glossaries.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source13:       glosmathtools.tar.xz
Source14:       glosmathtools.doc.tar.xz

%description -n texlive-glosmathtools
This package can be used to generate a mathematical
nomenclature (also called "list of symbols" or "notation"). It
is based on the glossaries package. Its main features are:
symbol categories (e.g.: latin, greek) automatic but
customizable symbol sorting easy subscript management easy
accentuation management abbreviation support (with first use
definition) bilingual nomenclatures (for bilingual documents)
bilingual abbreviations The documentation is based on the
ulthese class. The package itself depends on glossaries,
amsmath, amsfonts, and etoolbox.

%package -n texlive-glosmathtools-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn54558
Release:        0
Summary:        Documentation for texlive-glosmathtools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-glosmathtools-doc:fr)

%description -n texlive-glosmathtools-doc
This package includes the documentation for texlive-glosmathtools

%post -n texlive-glosmathtools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glosmathtools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glosmathtools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glosmathtools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glosmathtools/README.md
%{_texmfdistdir}/doc/latex/glosmathtools/sample_glosmathtools_en.pdf
%{_texmfdistdir}/doc/latex/glosmathtools/sample_glosmathtools_en.tex
%{_texmfdistdir}/doc/latex/glosmathtools/sample_glosmathtools_fr.pdf
%{_texmfdistdir}/doc/latex/glosmathtools/sample_glosmathtools_fr.tex
%{_texmfdistdir}/doc/latex/glosmathtools/sample_glosmathtools_glos.tex

%files -n texlive-glosmathtools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glosmathtools/glosmathtools.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glosmathtools-%{texlive_version}.%{texlive_noarch}.1.0.0svn54558-%{release}-zypper
%endif

%package -n texlive-gloss
Version:        %{texlive_version}.%{texlive_noarch}.1.5.2svn15878
Release:        0
Summary:        Create glossaries using BibTeX
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
Recommends:     texlive-gloss-doc >= %{texlive_version}
Provides:       tex(gloss.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source15:       gloss.tar.xz
Source16:       gloss.doc.tar.xz

%description -n texlive-gloss
A glossary package using BibTeX with \cite replaced by \gloss.

%package -n texlive-gloss-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5.2svn15878
Release:        0
Summary:        Documentation for texlive-gloss
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gloss-doc
This package includes the documentation for texlive-gloss

%post -n texlive-gloss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gloss 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gloss
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gloss-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gloss/README
%{_texmfdistdir}/doc/latex/gloss/gloss.pdf
%{_texmfdistdir}/doc/latex/gloss/gloss.tex
%{_texmfdistdir}/doc/latex/gloss/sample.tex

%files -n texlive-gloss
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/gloss/glsbase.bib
%{_texmfdistdir}/bibtex/bib/gloss/sample.bib
%{_texmfdistdir}/bibtex/bst/gloss/glsplain.bst
%{_texmfdistdir}/bibtex/bst/gloss/glsshort.bst
%{_texmfdistdir}/tex/latex/gloss/gloss.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gloss-%{texlive_version}.%{texlive_noarch}.1.5.2svn15878-%{release}-zypper
%endif

%package -n texlive-gloss-occitan
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn52593
Release:        0
Summary:        Polyglossia support for Occitan
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
Recommends:     texlive-gloss-occitan-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source17:       gloss-occitan.source.tar.xz
Source18:       gloss-occitan.doc.tar.xz

%description -n texlive-gloss-occitan
Occitan language description file for polyglossia

%package -n texlive-gloss-occitan-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn52593
Release:        0
Summary:        Documentation for texlive-gloss-occitan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gloss-occitan-doc
This package includes the documentation for texlive-gloss-occitan

%post -n texlive-gloss-occitan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gloss-occitan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gloss-occitan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gloss-occitan-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gloss-occitan/README
%{_texmfdistdir}/doc/latex/gloss-occitan/gloss-occitan.pdf

%files -n texlive-gloss-occitan
%defattr(-,root,root,755)
%{_texmfdistdir}/source/latex/gloss-occitan/gloss-occitan.dtx
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gloss-occitan-%{texlive_version}.%{texlive_noarch}.0.0.1svn52593-%{release}-zypper
%endif

%package -n texlive-glossaries
Version:        %{texlive_version}.%{texlive_noarch}.4.46svn54402
Release:        0
Summary:        Create glossaries and lists of acronyms
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-glossaries-bin >= %{texlive_version}
#!BuildIgnore: texlive-glossaries-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-glossaries-doc >= %{texlive_version}
Requires:       perl(Getopt::Std)
#!BuildIgnore:  perl(Getopt::Std)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(vars)
#!BuildIgnore:  perl(vars)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
Provides:       tex(example-glossaries-acronym-desc.tex)
Provides:       tex(example-glossaries-acronym.tex)
Provides:       tex(example-glossaries-acronyms-lang.tex)
Provides:       tex(example-glossaries-brief.tex)
Provides:       tex(example-glossaries-childnoname.tex)
Provides:       tex(example-glossaries-cite.tex)
Provides:       tex(example-glossaries-images.tex)
Provides:       tex(example-glossaries-long.tex)
Provides:       tex(example-glossaries-multipar.tex)
Provides:       tex(example-glossaries-parent.tex)
Provides:       tex(example-glossaries-symbolnames.tex)
Provides:       tex(example-glossaries-symbols.tex)
Provides:       tex(example-glossaries-url.tex)
Provides:       tex(glossaries-accsupp.sty)
Provides:       tex(glossaries-babel.sty)
Provides:       tex(glossaries-compatible-207.sty)
Provides:       tex(glossaries-compatible-307.sty)
Provides:       tex(glossaries-polyglossia.sty)
Provides:       tex(glossaries-prefix.sty)
Provides:       tex(glossaries.sty)
Provides:       tex(glossary-hypernav.sty)
Provides:       tex(glossary-inline.sty)
Provides:       tex(glossary-list.sty)
Provides:       tex(glossary-long.sty)
Provides:       tex(glossary-longbooktabs.sty)
Provides:       tex(glossary-longragged.sty)
Provides:       tex(glossary-mcols.sty)
Provides:       tex(glossary-super.sty)
Provides:       tex(glossary-superragged.sty)
Provides:       tex(glossary-tree.sty)
Requires:       tex(accsupp.sty)
Requires:       tex(amsgen.sty)
Requires:       tex(array.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(datatool-base.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mfirstuc.sty)
Requires:       tex(multicol.sty)
Requires:       tex(supertabular.sty)
Requires:       tex(textcase.sty)
Requires:       tex(tracklang.sty)
Requires:       tex(translator.sty)
Requires:       tex(xfor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source19:       glossaries.tar.xz
Source20:       glossaries.doc.tar.xz

%description -n texlive-glossaries
The glossaries package supports acronyms and multiple
glossaries, and has provision for operation in several
languages (using the facilities of either babel or
polyglossia). New entries are defined to have a name and
description (and optionally an associated symbol). Support for
multiple languages is offered, and plural forms of terms may be
specified. An additional package, glossaries-accsupp, can make
use of the accsupp package mechanisms for accessibility support
for PDF files containing glossaries. The user may define new
glossary styles, and preambles and postambles can be specified.
There is provision for loading a database of terms, but only
terms used in the text will be added to the relevant glossary.
The package uses an indexing program to provide the actual
glossary; either makeindex or xindy may serve this purpose, and
a Perl script is provided to serve as interface. This package
requires the mfirstuc package. The package supersedes the
author's glossary package (which is now obsolete).

%package -n texlive-glossaries-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.46svn54402
Release:        0
Summary:        Documentation for texlive-glossaries
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(makeglossaries-lite.1)
Provides:       man(makeglossaries.1)

%description -n texlive-glossaries-doc
This package includes the documentation for texlive-glossaries

%post -n texlive-glossaries
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries/CHANGES
%{_texmfdistdir}/doc/latex/glossaries/INSTALL
%{_texmfdistdir}/doc/latex/glossaries/README.md
%{_texmfdistdir}/doc/latex/glossaries/glossaries-code.pdf
%{_texmfdistdir}/doc/latex/glossaries/glossaries-user.html
%{_texmfdistdir}/doc/latex/glossaries/glossaries-user.pdf
%{_texmfdistdir}/doc/latex/glossaries/glossaries-user.tex
%{_texmfdistdir}/doc/latex/glossaries/glossariesbegin.html
%{_texmfdistdir}/doc/latex/glossaries/glossariesbegin.pdf
%{_texmfdistdir}/doc/latex/glossaries/glossariesbegin.tex
%{_texmfdistdir}/doc/latex/glossaries/glossary2glossaries.html
%{_texmfdistdir}/doc/latex/glossaries/glossary2glossaries.pdf
%{_texmfdistdir}/doc/latex/glossaries/glossary2glossaries.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/README-samples
%{_texmfdistdir}/doc/latex/glossaries/samples/database1.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/database2.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/glossary-lipsum-examples.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/glossary-lipsum-examples.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/minimalgls.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/minimalgls.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/mwe-acr-desc.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/mwe-acr-desc.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/mwe-acr.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/mwe-acr.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/mwe-gls.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/mwe-gls.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-FnDesc.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-FnDesc.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-chap-hyperfirst.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-chap-hyperfirst.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-crossref.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-crossref.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-custom-acronym.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-custom-acronym.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-dot-abbr.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-dot-abbr.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-dual.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-dual.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-entrycount.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-entrycount.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-entryfmt.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-entryfmt.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-font-abbr.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-font-abbr.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-ignored.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-ignored.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-index.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-index.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-inline.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-inline.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-langdict.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-langdict.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-newkeys.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-newkeys.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-noidxapp-utf8.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-noidxapp-utf8.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-noidxapp.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-noidxapp.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-nomathhyper.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-nomathhyper.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-numberlist.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-numberlist.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-prefix.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-prefix.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-si.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-si.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-storage-abbr-desc.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-storage-abbr-desc.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-storage-abbr.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample-storage-abbr.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sample4col.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sample4col.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcr.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcr.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcrDesc.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleAcrDesc.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleCustomAcr.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleCustomAcr.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleDB.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleDB.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleDesc.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleDesc.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleEq.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleEq.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleEqPg.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleEqPg.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleFnAcrDesc.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleFnAcrDesc.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleNtn.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleNtn.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/samplePeople.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/samplePeople.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleSec.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleSec.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleSort.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleSort.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleaccsupp.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleaccsupp.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleacronyms.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleacronyms.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampletree.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampletree.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleutf8.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/sampleutf8.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy-mc.xdy
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy-mc207.xdy
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy2.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy2.tex
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy3.pdf
%{_texmfdistdir}/doc/latex/glossaries/samples/samplexdy3.tex
%{_mandir}/man1/makeglossaries-lite.1*
%{_mandir}/man1/makeglossaries.1*

%files -n texlive-glossaries
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/glossaries/glossaries.perl
%{_texmfdistdir}/scripts/glossaries/makeglossaries
%{_texmfdistdir}/scripts/glossaries/makeglossaries-lite.lua
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-babel.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-compatible-207.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-compatible-307.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-polyglossia.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries-prefix.sty
%{_texmfdistdir}/tex/latex/glossaries/base/glossaries.sty
%{_texmfdistdir}/tex/latex/glossaries/expl/glossaries-accsupp.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-hypernav.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-inline.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-list.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-long.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-longbooktabs.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-longragged.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-mcols.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-super.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-superragged.sty
%{_texmfdistdir}/tex/latex/glossaries/styles/glossary-tree.sty
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-acronym-desc.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-acronym.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-acronyms-lang.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-brief.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-childnoname.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-cite.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-images.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-long.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-multipar.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-parent.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-symbolnames.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-symbols.tex
%{_texmfdistdir}/tex/latex/glossaries/test-entries/example-glossaries-url.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-%{texlive_version}.%{texlive_noarch}.4.46svn54402-%{release}-zypper
%endif

%package -n texlive-glossaries-danish
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Danish language module for glossaries package
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
Recommends:     texlive-glossaries-danish-doc >= %{texlive_version}
Provides:       tex(glossaries-danish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source21:       glossaries-danish.tar.xz
Source22:       glossaries-danish.doc.tar.xz

%description -n texlive-glossaries-danish
Danish language module for glossaries package.

%package -n texlive-glossaries-danish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-danish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-danish-doc
This package includes the documentation for texlive-glossaries-danish

%post -n texlive-glossaries-danish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-danish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-danish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-danish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-danish/README
%{_texmfdistdir}/doc/latex/glossaries-danish/glossaries-danish.pdf
%{_texmfdistdir}/doc/latex/glossaries-danish/glossaries-dictionary-Danish.dict

%files -n texlive-glossaries-danish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-danish/glossaries-danish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-danish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-dutch
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn35685
Release:        0
Summary:        Dutch language module for glossaries package
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
Recommends:     texlive-glossaries-dutch-doc >= %{texlive_version}
Provides:       tex(glossaries-dutch.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source23:       glossaries-dutch.tar.xz
Source24:       glossaries-dutch.doc.tar.xz

%description -n texlive-glossaries-dutch
Dutch language module for glossariesr package.

%package -n texlive-glossaries-dutch-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn35685
Release:        0
Summary:        Documentation for texlive-glossaries-dutch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-dutch-doc
This package includes the documentation for texlive-glossaries-dutch

%post -n texlive-glossaries-dutch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-dutch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-dutch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-dutch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-dutch/README
%{_texmfdistdir}/doc/latex/glossaries-dutch/glossaries-dictionary-Dutch.dict
%{_texmfdistdir}/doc/latex/glossaries-dutch/glossaries-dutch.pdf

%files -n texlive-glossaries-dutch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-dutch/glossaries-dutch.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-dutch-%{texlive_version}.%{texlive_noarch}.1.1svn35685-%{release}-zypper
%endif

%package -n texlive-glossaries-english
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        English language module for glossaries package
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
Recommends:     texlive-glossaries-english-doc >= %{texlive_version}
Provides:       tex(glossaries-english.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source25:       glossaries-english.tar.xz
Source26:       glossaries-english.doc.tar.xz

%description -n texlive-glossaries-english
English language module for glossariesr package.

%package -n texlive-glossaries-english-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-english
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-english-doc
This package includes the documentation for texlive-glossaries-english

%post -n texlive-glossaries-english
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-english 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-english
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-english-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-english/README
%{_texmfdistdir}/doc/latex/glossaries-english/glossaries-dictionary-English.dict
%{_texmfdistdir}/doc/latex/glossaries-english/glossaries-english.pdf

%files -n texlive-glossaries-english
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-english/glossaries-english.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-english-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-estonian
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49928
Release:        0
Summary:        Estonian language module for glossaries package
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
Recommends:     texlive-glossaries-estonian-doc >= %{texlive_version}
Provides:       tex(glossaries-estonian-ascii.ldf)
Provides:       tex(glossaries-estonian-utf8.ldf)
Provides:       tex(glossaries-estonian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source27:       glossaries-estonian.tar.xz
Source28:       glossaries-estonian.doc.tar.xz

%description -n texlive-glossaries-estonian
This package provides the Estonian language module for the
glossaries package.

%package -n texlive-glossaries-estonian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn49928
Release:        0
Summary:        Documentation for texlive-glossaries-estonian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-estonian-doc
This package includes the documentation for texlive-glossaries-estonian

%post -n texlive-glossaries-estonian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-estonian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-estonian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-estonian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-estonian/README
%{_texmfdistdir}/doc/latex/glossaries-estonian/glossaries-dictionary-Estonian.dict
%{_texmfdistdir}/doc/latex/glossaries-estonian/glossaries-estonian.pdf

%files -n texlive-glossaries-estonian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-estonian/glossaries-estonian-ascii.ldf
%{_texmfdistdir}/tex/latex/glossaries-estonian/glossaries-estonian-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-estonian/glossaries-estonian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-estonian-%{texlive_version}.%{texlive_noarch}.1.0svn49928-%{release}-zypper
%endif

%package -n texlive-glossaries-extra
Version:        %{texlive_version}.%{texlive_noarch}.1.45svn54688
Release:        0
Summary:        An extension to the glossaries package
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
Recommends:     texlive-glossaries-extra-doc >= %{texlive_version}
Provides:       tex(example-glossaries-xr.tex)
Provides:       tex(glossaries-extra-bib2gls.sty)
Provides:       tex(glossaries-extra-stylemods.sty)
Provides:       tex(glossaries-extra.sty)
Provides:       tex(glossary-bookindex.sty)
Provides:       tex(glossary-longextra.sty)
Provides:       tex(glossary-topic.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(glossaries-accsupp.sty)
Requires:       tex(glossaries-prefix.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(glossary-inline.sty)
Requires:       tex(glossary-list.sty)
Requires:       tex(glossary-long.sty)
Requires:       tex(glossary-longbooktabs.sty)
Requires:       tex(glossary-longragged.sty)
Requires:       tex(glossary-mcols.sty)
Requires:       tex(glossary-super.sty)
Requires:       tex(glossary-superragged.sty)
Requires:       tex(glossary-tree.sty)
Requires:       tex(multicol.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source29:       glossaries-extra.tar.xz
Source30:       glossaries-extra.doc.tar.xz

%description -n texlive-glossaries-extra
This package provides improvements and extra features to the
glossaries package. Some of the default glossaries.sty
behaviour is changed by glossaries-extra.sty. See the user
manual glossaries-extra-manual.pdf for further details.
glossaries-extra.sty requires the glossaries package and,
naturally, all packages required by glossaries.sty.

%package -n texlive-glossaries-extra-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.45svn54688
Release:        0
Summary:        Documentation for texlive-glossaries-extra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-extra-doc
This package includes the documentation for texlive-glossaries-extra

%post -n texlive-glossaries-extra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-extra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-extra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-extra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-extra/CHANGES
%{_texmfdistdir}/doc/latex/glossaries-extra/README
%{_texmfdistdir}/doc/latex/glossaries-extra/glossaries-extra-code.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/glossaries-extra-manual.html
%{_texmfdistdir}/doc/latex/glossaries-extra/glossaries-extra-manual.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/glossaries-extra-manual.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-abbr-styles.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-abbr-styles.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-abbrv.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-abbrv.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-accsupp.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-accsupp.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-acronym-desc.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-acronym-desc.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-acronym.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-acronym.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alias.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alias.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-altmodifier.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-altmodifier.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alttree-marginpar.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alttree-marginpar.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alttree-sym.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alttree-sym.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alttree.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-alttree.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-autoindex-hyp.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-autoindex-hyp.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-autoindex.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-autoindex.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-crossref.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-crossref.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-crossref2.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-crossref2.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-docdef.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-docdef.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-entrycount.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-entrycount.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-external.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-external.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-fmt.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-fmt.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-footnote.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-footnote.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-header.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-header.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-indexhook.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-indexhook.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-initialisms.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-initialisms.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-linkcount.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-linkcount.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-mixed-abbrv-styles.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-mixed-abbrv-styles.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-mixedsort.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-mixedsort.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-mixture.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-mixture.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-name-font.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-name-font.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-nested.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-nested.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-noidx-restricteddocdefs.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-noidx-restricteddocdefs.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onelink.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onelink.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onthefly-utf8.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onthefly-utf8.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onthefly-xetex.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onthefly-xetex.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onthefly.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-onthefly.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-pages.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-pages.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-postdot.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-postdot.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-postlink.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-postlink.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-prefix.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-prefix.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-record-nameref.glstex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-record-nameref.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-record-nameref.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-record.glstex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-record.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-record.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-restricteddocdefs.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-restricteddocdefs.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl-hyp.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl-hyp.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl-main-hyp.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl-main-hyp.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl-main.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl-main.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-suppl.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-trans.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-trans.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-undef.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-undef.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-unitentrycount.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample-unitentrycount.tex
%{_texmfdistdir}/doc/latex/glossaries-extra/sample.pdf
%{_texmfdistdir}/doc/latex/glossaries-extra/sample.tex

%files -n texlive-glossaries-extra
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-acronym-desc.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-acronym.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-acronyms-lang.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-brief.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-childnoname.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-cite.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-images.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-long.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-multipar.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-parent.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-symbolnames.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-symbols.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-url.bib
%{_texmfdistdir}/bibtex/bib/glossaries-extra/example-glossaries-xr.bib
%{_texmfdistdir}/tex/latex/glossaries-extra/example-glossaries-xr.tex
%{_texmfdistdir}/tex/latex/glossaries-extra/glossaries-extra-bib2gls.sty
%{_texmfdistdir}/tex/latex/glossaries-extra/glossaries-extra-stylemods.sty
%{_texmfdistdir}/tex/latex/glossaries-extra/glossaries-extra.sty
%{_texmfdistdir}/tex/latex/glossaries-extra/glossary-bookindex.sty
%{_texmfdistdir}/tex/latex/glossaries-extra/glossary-longextra.sty
%{_texmfdistdir}/tex/latex/glossaries-extra/glossary-topic.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-extra-%{texlive_version}.%{texlive_noarch}.1.45svn54688-%{release}-zypper
%endif

%package -n texlive-glossaries-finnish
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Finnish language module for glossaries package
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
Recommends:     texlive-glossaries-finnish-doc >= %{texlive_version}
Provides:       tex(glossaries-finnish-ascii.ldf)
Provides:       tex(glossaries-finnish-utf8.ldf)
Provides:       tex(glossaries-finnish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source31:       glossaries-finnish.tar.xz
Source32:       glossaries-finnish.doc.tar.xz

%description -n texlive-glossaries-finnish
Finnish language module for glossaries package.

%package -n texlive-glossaries-finnish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Documentation for texlive-glossaries-finnish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-finnish-doc
This package includes the documentation for texlive-glossaries-finnish

%post -n texlive-glossaries-finnish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-finnish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-finnish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-finnish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-finnish/README
%{_texmfdistdir}/doc/latex/glossaries-finnish/glossaries-dictionary-Finnish.dict
%{_texmfdistdir}/doc/latex/glossaries-finnish/glossaries-finnish.pdf

%files -n texlive-glossaries-finnish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-finnish/glossaries-finnish-ascii.ldf
%{_texmfdistdir}/tex/latex/glossaries-finnish/glossaries-finnish-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-finnish/glossaries-finnish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-finnish-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif

%package -n texlive-glossaries-french
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn42873
Release:        0
Summary:        French language module for glossaries package
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
Recommends:     texlive-glossaries-french-doc >= %{texlive_version}
Provides:       tex(glossaries-french.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source33:       glossaries-french.tar.xz
Source34:       glossaries-french.doc.tar.xz

%description -n texlive-glossaries-french
French language module for glossaries package.

%package -n texlive-glossaries-french-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn42873
Release:        0
Summary:        Documentation for texlive-glossaries-french
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-french-doc
This package includes the documentation for texlive-glossaries-french

%post -n texlive-glossaries-french
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-french 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-french
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-french-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-french/README
%{_texmfdistdir}/doc/latex/glossaries-french/glossaries-dictionary-French.dict
%{_texmfdistdir}/doc/latex/glossaries-french/glossaries-french.pdf

%files -n texlive-glossaries-french
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-french/glossaries-french.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-french-%{texlive_version}.%{texlive_noarch}.1.1svn42873-%{release}-zypper
%endif

%package -n texlive-glossaries-german
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        German language module for glossaries package
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
Recommends:     texlive-glossaries-german-doc >= %{texlive_version}
Provides:       tex(glossaries-german.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source35:       glossaries-german.tar.xz
Source36:       glossaries-german.doc.tar.xz

%description -n texlive-glossaries-german
German language module for the glossaries package.

%package -n texlive-glossaries-german-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-german
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-german-doc
This package includes the documentation for texlive-glossaries-german

%post -n texlive-glossaries-german
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-german 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-german
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-german-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-german/README
%{_texmfdistdir}/doc/latex/glossaries-german/glossaries-dictionary-German.dict
%{_texmfdistdir}/doc/latex/glossaries-german/glossaries-german.pdf

%files -n texlive-glossaries-german
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-german/glossaries-german.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-german-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-irish
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Irish language module for glossaries package
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
Recommends:     texlive-glossaries-irish-doc >= %{texlive_version}
Provides:       tex(glossaries-irish-noenc.ldf)
Provides:       tex(glossaries-irish-utf8.ldf)
Provides:       tex(glossaries-irish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source37:       glossaries-irish.tar.xz
Source38:       glossaries-irish.doc.tar.xz

%description -n texlive-glossaries-irish
Irish language module for glossariesr package.

%package -n texlive-glossaries-irish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-irish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-irish-doc
This package includes the documentation for texlive-glossaries-irish

%post -n texlive-glossaries-irish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-irish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-irish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-irish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-irish/README
%{_texmfdistdir}/doc/latex/glossaries-irish/glossaries-dictionary-Irish.dict
%{_texmfdistdir}/doc/latex/glossaries-irish/glossaries-irish.pdf

%files -n texlive-glossaries-irish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-irish/glossaries-irish-noenc.ldf
%{_texmfdistdir}/tex/latex/glossaries-irish/glossaries-irish-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-irish/glossaries-irish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-irish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-italian
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Italian language module for glossaries package
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
Recommends:     texlive-glossaries-italian-doc >= %{texlive_version}
Provides:       tex(glossaries-italian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source39:       glossaries-italian.tar.xz
Source40:       glossaries-italian.doc.tar.xz

%description -n texlive-glossaries-italian
Italian language module for glossaries package.

%package -n texlive-glossaries-italian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-italian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-italian-doc
This package includes the documentation for texlive-glossaries-italian

%post -n texlive-glossaries-italian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-italian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-italian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-italian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-italian/README
%{_texmfdistdir}/doc/latex/glossaries-italian/glossaries-dictionary-Italian.dict
%{_texmfdistdir}/doc/latex/glossaries-italian/glossaries-italian.pdf

%files -n texlive-glossaries-italian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-italian/glossaries-italian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-italian-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-magyar
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Magyar language module for glossaries package
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
Recommends:     texlive-glossaries-magyar-doc >= %{texlive_version}
Provides:       tex(glossaries-magyar-noenc.ldf)
Provides:       tex(glossaries-magyar-utf8.ldf)
Provides:       tex(glossaries-magyar.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source41:       glossaries-magyar.tar.xz
Source42:       glossaries-magyar.doc.tar.xz

%description -n texlive-glossaries-magyar
Magyar language module for glossariesr package.

%package -n texlive-glossaries-magyar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-magyar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-magyar-doc
This package includes the documentation for texlive-glossaries-magyar

%post -n texlive-glossaries-magyar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-magyar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-magyar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-magyar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-magyar/README
%{_texmfdistdir}/doc/latex/glossaries-magyar/glossaries-dictionary-Magyar.dict
%{_texmfdistdir}/doc/latex/glossaries-magyar/glossaries-magyar.pdf

%files -n texlive-glossaries-magyar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-magyar/glossaries-magyar-noenc.ldf
%{_texmfdistdir}/tex/latex/glossaries-magyar/glossaries-magyar-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-magyar/glossaries-magyar.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-magyar-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-polish
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Polish language module for glossaries package
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
Recommends:     texlive-glossaries-polish-doc >= %{texlive_version}
Provides:       tex(glossaries-polish-noenc.ldf)
Provides:       tex(glossaries-polish-utf8.ldf)
Provides:       tex(glossaries-polish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source43:       glossaries-polish.tar.xz
Source44:       glossaries-polish.doc.tar.xz

%description -n texlive-glossaries-polish
Polish language module for the glossaries package.

%package -n texlive-glossaries-polish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-polish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-polish-doc
This package includes the documentation for texlive-glossaries-polish

%post -n texlive-glossaries-polish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-polish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-polish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-polish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-polish/README
%{_texmfdistdir}/doc/latex/glossaries-polish/glossaries-dictionary-Polish.dict
%{_texmfdistdir}/doc/latex/glossaries-polish/glossaries-polish.pdf

%files -n texlive-glossaries-polish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-polish/glossaries-polish-noenc.ldf
%{_texmfdistdir}/tex/latex/glossaries-polish/glossaries-polish-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-polish/glossaries-polish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-polish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-portuges
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn36064
Release:        0
Summary:        Portuges language module for glossaries package
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
Recommends:     texlive-glossaries-portuges-doc >= %{texlive_version}
Provides:       tex(glossaries-portuges-noenc.ldf)
Provides:       tex(glossaries-portuges-utf8.ldf)
Provides:       tex(glossaries-portuges.ldf)
Provides:       tex(glossaries-pt-BR.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source45:       glossaries-portuges.tar.xz
Source46:       glossaries-portuges.doc.tar.xz

%description -n texlive-glossaries-portuges
Portuges language module for glossaries package.

%package -n texlive-glossaries-portuges-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn36064
Release:        0
Summary:        Documentation for texlive-glossaries-portuges
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-portuges-doc
This package includes the documentation for texlive-glossaries-portuges

%post -n texlive-glossaries-portuges
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-portuges 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-portuges
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-portuges-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-portuges/README
%{_texmfdistdir}/doc/latex/glossaries-portuges/glossaries-dictionary-Brazilian.dict
%{_texmfdistdir}/doc/latex/glossaries-portuges/glossaries-portuges.pdf

%files -n texlive-glossaries-portuges
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-portuges/glossaries-portuges-noenc.ldf
%{_texmfdistdir}/tex/latex/glossaries-portuges/glossaries-portuges-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-portuges/glossaries-portuges.ldf
%{_texmfdistdir}/tex/latex/glossaries-portuges/glossaries-pt-BR.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-portuges-%{texlive_version}.%{texlive_noarch}.1.1svn36064-%{release}-zypper
%endif

%package -n texlive-glossaries-serbian
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Serbian language module for glossaries package
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
Recommends:     texlive-glossaries-serbian-doc >= %{texlive_version}
Provides:       tex(glossaries-serbian-noenc.ldf)
Provides:       tex(glossaries-serbian-utf8.ldf)
Provides:       tex(glossaries-serbian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source47:       glossaries-serbian.tar.xz
Source48:       glossaries-serbian.doc.tar.xz

%description -n texlive-glossaries-serbian
Serbian language module for glossaries package.

%package -n texlive-glossaries-serbian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-serbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-serbian-doc
This package includes the documentation for texlive-glossaries-serbian

%post -n texlive-glossaries-serbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-serbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-serbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-serbian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-serbian/README
%{_texmfdistdir}/doc/latex/glossaries-serbian/glossaries-dictionary-Serbian.dict
%{_texmfdistdir}/doc/latex/glossaries-serbian/glossaries-serbian.pdf

%files -n texlive-glossaries-serbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-serbian/glossaries-serbian-noenc.ldf
%{_texmfdistdir}/tex/latex/glossaries-serbian/glossaries-serbian-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-serbian/glossaries-serbian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-serbian-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glossaries-slovene
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn51211
Release:        0
Summary:        Slovene language module for glossaries package
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
Recommends:     texlive-glossaries-slovene-doc >= %{texlive_version}
Provides:       tex(glossaries-slovene.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source49:       glossaries-slovene.tar.xz
Source50:       glossaries-slovene.doc.tar.xz

%description -n texlive-glossaries-slovene
Slovene language module for glossaries package.

%package -n texlive-glossaries-slovene-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn51211
Release:        0
Summary:        Documentation for texlive-glossaries-slovene
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-slovene-doc
This package includes the documentation for texlive-glossaries-slovene

%post -n texlive-glossaries-slovene
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-slovene 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-slovene
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-slovene-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-slovene/README
%{_texmfdistdir}/doc/latex/glossaries-slovene/glossaries-dictionary-slovene.dict
%{_texmfdistdir}/doc/latex/glossaries-slovene/glossaries-slovene.pdf

%files -n texlive-glossaries-slovene
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-slovene/glossaries-slovene.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-slovene-%{texlive_version}.%{texlive_noarch}.1.0svn51211-%{release}-zypper
%endif

%package -n texlive-glossaries-spanish
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Spanish language module for glossaries package
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
Recommends:     texlive-glossaries-spanish-doc >= %{texlive_version}
Provides:       tex(glossaries-spanish-noenc.ldf)
Provides:       tex(glossaries-spanish-utf8.ldf)
Provides:       tex(glossaries-spanish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source51:       glossaries-spanish.tar.xz
Source52:       glossaries-spanish.doc.tar.xz

%description -n texlive-glossaries-spanish
Spanish language module for glossaries package.

%package -n texlive-glossaries-spanish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn35665
Release:        0
Summary:        Documentation for texlive-glossaries-spanish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-glossaries-spanish-doc
This package includes the documentation for texlive-glossaries-spanish

%post -n texlive-glossaries-spanish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glossaries-spanish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glossaries-spanish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glossaries-spanish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/glossaries-spanish/README
%{_texmfdistdir}/doc/latex/glossaries-spanish/glossaries-dictionary-Spanish.dict
%{_texmfdistdir}/doc/latex/glossaries-spanish/glossaries-spanish.pdf

%files -n texlive-glossaries-spanish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/glossaries-spanish/glossaries-spanish-noenc.ldf
%{_texmfdistdir}/tex/latex/glossaries-spanish/glossaries-spanish-utf8.ldf
%{_texmfdistdir}/tex/latex/glossaries-spanish/glossaries-spanish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glossaries-spanish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif

%package -n texlive-glyphlist
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Adobe Glyph List and TeX extensions
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
Source53:       glyphlist.tar.xz

%description -n texlive-glyphlist
Map between traditional Adobe glyph names and Unicode points,
maintained by Adobe. The additional texglyphlist.txt is
maintained as part of lcdf-typetools.
%post -n texlive-glyphlist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-glyphlist 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-glyphlist
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-glyphlist
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/glyphlist/glyphlist.txt
%{_texmfdistdir}/fonts/map/glyphlist/pdfglyphlist.txt
%{_texmfdistdir}/fonts/map/glyphlist/texglyphlist.txt
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-glyphlist-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif

%package -n texlive-gmdoc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.993svn21292
Release:        0
Summary:        Documentation of LaTeX packages
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
Recommends:     texlive-gmdoc-doc >= %{texlive_version}
Provides:       tex(gmdoc.sty)
Provides:       tex(gmdocc.cls)
Provides:       tex(gmoldcomm.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(article.cls)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(gmiflink.sty)
Requires:       tex(gmutils.sty)
Requires:       tex(gmverb.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(multicol.sty)
Requires:       tex(tikz.sty)
Requires:       tex(trace.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source54:       gmdoc.tar.xz
Source55:       gmdoc.doc.tar.xz

%description -n texlive-gmdoc
A LaTeX package and an example class for documenting (La)TeX
packages, document classes, .dtx etc., providing hyperlinks.
The package is believed to be compatible with doc and permits
minimal markup of code (the macrocode environment is no longer
necessary). The package provides automatic detection of
definitions (detecting such things as \def, \newcommand,
\DeclareOption etc.). The package needs hyperref and the
author's three 'basic' packages: gmutils, gmverb and gmiflink.
As a bonus (and as an example of doc compatibility) driver
files are provided that may be used to typeset the LaTeX Base.

%package -n texlive-gmdoc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.993svn21292
Release:        0
Summary:        Documentation for texlive-gmdoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gmdoc-doc
This package includes the documentation for texlive-gmdoc

%post -n texlive-gmdoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gmdoc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gmdoc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gmdoc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gmdoc/README
%{_texmfdistdir}/doc/latex/gmdoc/basedrivers/doc_gmdoc.tex
%{_texmfdistdir}/doc/latex/gmdoc/basedrivers/docstrip_gmdoc.tex
%{_texmfdistdir}/doc/latex/gmdoc/basedrivers/source2e_gmdoc.tex
%{_texmfdistdir}/doc/latex/gmdoc/gmdoc.pdf

%files -n texlive-gmdoc
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/gmdoc/gmglo.ist
%{_texmfdistdir}/tex/latex/gmdoc/gmdoc.sty
%{_texmfdistdir}/tex/latex/gmdoc/gmdocc.cls
%{_texmfdistdir}/tex/latex/gmdoc/gmoldcomm.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gmdoc-%{texlive_version}.%{texlive_noarch}.0.0.993svn21292-%{release}-zypper
%endif

%package -n texlive-gmdoc-enhance
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Some enhancements to the gmdoc package
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
Recommends:     texlive-gmdoc-enhance-doc >= %{texlive_version}
Provides:       tex(gmdoc-enhance.sty)
Requires:       tex(gmdoc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source56:       gmdoc-enhance.tar.xz
Source57:       gmdoc-enhance.doc.tar.xz

%description -n texlive-gmdoc-enhance
This package provides some enhancements for the gmdoc package:
nicer formatting for multiple line inline comments, an ability
to "comment out" some code, and a macro to input other files in
"normal" LaTeX mode.

%package -n texlive-gmdoc-enhance-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn15878
Release:        0
Summary:        Documentation for texlive-gmdoc-enhance
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gmdoc-enhance-doc
This package includes the documentation for texlive-gmdoc-enhance

%post -n texlive-gmdoc-enhance
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gmdoc-enhance 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gmdoc-enhance
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gmdoc-enhance-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gmdoc-enhance/README
%{_texmfdistdir}/doc/latex/gmdoc-enhance/gmdoc-enhance.pdf

%files -n texlive-gmdoc-enhance
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gmdoc-enhance/gmdoc-enhance.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gmdoc-enhance-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif

%package -n texlive-gmiflink
Version:        %{texlive_version}.%{texlive_noarch}.0.0.97svn15878
Release:        0
Summary:        Simplify usage of \hypertarget and \hyperlink
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
Recommends:     texlive-gmiflink-doc >= %{texlive_version}
Provides:       tex(gmiflink.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source58:       gmiflink.tar.xz
Source59:       gmiflink.doc.tar.xz

%description -n texlive-gmiflink
Three hyperref-based macros that simplify usage of \hypertarget
and \hyperlink: one argument instead of the same one twice.
Also \gmiflink and \gmifref which typeset plain text instead of
generating an error or printing '??' if there is no respective
hypertarget or label.

%package -n texlive-gmiflink-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.97svn15878
Release:        0
Summary:        Documentation for texlive-gmiflink
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gmiflink-doc
This package includes the documentation for texlive-gmiflink

%post -n texlive-gmiflink
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gmiflink 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gmiflink
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gmiflink-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gmiflink/README
%{_texmfdistdir}/doc/latex/gmiflink/gmiflink.pdf

%files -n texlive-gmiflink
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gmiflink/gmiflink.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gmiflink-%{texlive_version}.%{texlive_noarch}.0.0.97svn15878-%{release}-zypper
%endif

%package -n texlive-gmp
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21691
Release:        0
Summary:        Enable integration between MetaPost pictures and LaTeX
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
Recommends:     texlive-gmp-doc >= %{texlive_version}
Provides:       tex(gmp.sty)
Requires:       tex(environ.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source60:       gmp.tar.xz
Source61:       gmp.doc.tar.xz

%description -n texlive-gmp
The package allows integration between MetaPost pictures and
LaTeX. The main feature is that passing parameters to the
MetaPost pictures is possible and the picture code can be put
inside arguments to commands, including \newcommand.

%package -n texlive-gmp-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21691
Release:        0
Summary:        Documentation for texlive-gmp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gmp-doc
This package includes the documentation for texlive-gmp

%post -n texlive-gmp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gmp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gmp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gmp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gmp/README
%{_texmfdistdir}/doc/latex/gmp/gmp.pdf

%files -n texlive-gmp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gmp/gmp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gmp-%{texlive_version}.%{texlive_noarch}.1.0svn21691-%{release}-zypper
%endif

%package -n texlive-gmutils
Version:        %{texlive_version}.%{texlive_noarch}.0.0.996svn24287
Release:        0
Summary:        Support macros for other packages
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
Recommends:     texlive-gmutils-doc >= %{texlive_version}
Provides:       tex(gmRCS.sty)
Provides:       tex(gmampulex.sty)
Provides:       tex(gmbase.sty)
Provides:       tex(gmcommand.sty)
Provides:       tex(gmenvir.sty)
Provides:       tex(gmlogos.sty)
Provides:       tex(gmmeta.sty)
Provides:       tex(gmmw.sty)
Provides:       tex(gmnotonlypream.sty)
Provides:       tex(gmparts.sty)
Provides:       tex(gmrelsize.sty)
Provides:       tex(gmtypos.sty)
Provides:       tex(gmurl.sty)
Provides:       tex(gmutils.sty)
Requires:       tex(calc.sty)
Requires:       tex(expl3.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(multicol.sty)
Requires:       tex(polski.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source62:       gmutils.tar.xz
Source63:       gmutils.doc.tar.xz

%description -n texlive-gmutils
Miscellaneous macros used by others of the author's packages.
Contents of the package: \newgif and other globals; \@ifnextcat
and \@ifXeTeX; \(Re)storeMacro(s) to override redefinitions;
\afterfi and friends; commands from relsize, etc.; "almost an
environment" or redefinition of \begin (\begin* doesn't check
if the argument environment is defined).

%package -n texlive-gmutils-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.996svn24287
Release:        0
Summary:        Documentation for texlive-gmutils
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gmutils-doc
This package includes the documentation for texlive-gmutils

%post -n texlive-gmutils
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gmutils 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gmutils
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gmutils-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gmutils/README
%{_texmfdistdir}/doc/latex/gmutils/gmutils.pdf

%files -n texlive-gmutils
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gmutils/gmRCS.sty
%{_texmfdistdir}/tex/latex/gmutils/gmampulex.sty
%{_texmfdistdir}/tex/latex/gmutils/gmbase.sty
%{_texmfdistdir}/tex/latex/gmutils/gmcommand.sty
%{_texmfdistdir}/tex/latex/gmutils/gmenvir.sty
%{_texmfdistdir}/tex/latex/gmutils/gmlogos.sty
%{_texmfdistdir}/tex/latex/gmutils/gmmeta.sty
%{_texmfdistdir}/tex/latex/gmutils/gmmw.sty
%{_texmfdistdir}/tex/latex/gmutils/gmnotonlypream.sty
%{_texmfdistdir}/tex/latex/gmutils/gmparts.sty
%{_texmfdistdir}/tex/latex/gmutils/gmrelsize.sty
%{_texmfdistdir}/tex/latex/gmutils/gmtypos.sty
%{_texmfdistdir}/tex/latex/gmutils/gmurl.sty
%{_texmfdistdir}/tex/latex/gmutils/gmutils.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gmutils-%{texlive_version}.%{texlive_noarch}.0.0.996svn24287-%{release}-zypper
%endif

%package -n texlive-gmverb
Version:        %{texlive_version}.%{texlive_noarch}.0.0.98svn24288
Release:        0
Summary:        A variant of LaTeX \verb, verbatim and shortvrb
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
Recommends:     texlive-gmverb-doc >= %{texlive_version}
Provides:       tex(gmverb.sty)
Requires:       tex(eufrak.sty)
Requires:       tex(gmcommand.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source64:       gmverb.tar.xz
Source65:       gmverb.doc.tar.xz

%description -n texlive-gmverb
A redefinition of \verb and verbatim so that long lines are
breakable before \ and after { with % as 'hyphen'. Allows you
to define your own verbatim-like environments (subject to a
size limit) and allows you to declare any single character as a
shorthand as in the \MakeShortVerb command of the shortvrb
package of the LaTeX distribution. The package depends on the
gmutils package.

%package -n texlive-gmverb-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.98svn24288
Release:        0
Summary:        Documentation for texlive-gmverb
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gmverb-doc
This package includes the documentation for texlive-gmverb

%post -n texlive-gmverb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gmverb 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gmverb
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gmverb-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gmverb/README
%{_texmfdistdir}/doc/latex/gmverb/gmverb.pdf

%files -n texlive-gmverb
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gmverb/gmverb.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gmverb-%{texlive_version}.%{texlive_noarch}.0.0.98svn24288-%{release}-zypper
%endif

%package -n texlive-gmverse
Version:        %{texlive_version}.%{texlive_noarch}.0.0.73svn29803
Release:        0
Summary:        A package for typesetting (short) poems
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
Recommends:     texlive-gmverse-doc >= %{texlive_version}
Provides:       tex(gmverse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source66:       gmverse.tar.xz
Source67:       gmverse.doc.tar.xz

%description -n texlive-gmverse
A redefinition of the verse environment to make the \\ command
optional for line ends and to give it a possibility of optical
centering and `right-hanging' alignment of lines broken because
of length.

%package -n texlive-gmverse-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.73svn29803
Release:        0
Summary:        Documentation for texlive-gmverse
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gmverse-doc
This package includes the documentation for texlive-gmverse

%post -n texlive-gmverse
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gmverse 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gmverse
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gmverse-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gmverse/README
%{_texmfdistdir}/doc/latex/gmverse/gmverse.pdf

%files -n texlive-gmverse
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gmverse/gmverse.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gmverse-%{texlive_version}.%{texlive_noarch}.0.0.73svn29803-%{release}-zypper
%endif

%package -n texlive-gnu-freefont
Version:        %{texlive_version}.%{texlive_noarch}.svn29349
Release:        0
Summary:        A Unicode font, with rather wide coverage
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
Requires:       texlive-gnu-freefont-fonts >= %{texlive_version}
Recommends:     texlive-gnu-freefont-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source68:       gnu-freefont.tar.xz
Source69:       gnu-freefont.doc.tar.xz

%description -n texlive-gnu-freefont
The package provides a set of outline (i.e. OpenType) fonts
covering as much as possible of the Unicode character set. The
set consists of three typefaces: one monospaced and two
proportional (one with uniform and one with modulated stroke).

%package -n texlive-gnu-freefont-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn29349
Release:        0
Summary:        Documentation for texlive-gnu-freefont
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gnu-freefont-doc
This package includes the documentation for texlive-gnu-freefont


%package -n texlive-gnu-freefont-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn29349
Release:        0
Summary:        Severed fonts for texlive-gnu-freefont
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gnu-freefont-fonts
The  separated fonts package for texlive-gnu-freefont
%post -n texlive-gnu-freefont
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gnu-freefont 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gnu-freefont
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gnu-freefont-fonts
%files -n texlive-gnu-freefont-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gnu-freefont/AUTHORS
%{_texmfdistdir}/doc/fonts/gnu-freefont/BUILDING
%{_texmfdistdir}/doc/fonts/gnu-freefont/COPYING
%{_texmfdistdir}/doc/fonts/gnu-freefont/CREDITS
%{_texmfdistdir}/doc/fonts/gnu-freefont/ChangeLog
%{_texmfdistdir}/doc/fonts/gnu-freefont/INSTALL
%{_texmfdistdir}/doc/fonts/gnu-freefont/Makefile
%{_texmfdistdir}/doc/fonts/gnu-freefont/README
%{_texmfdistdir}/doc/fonts/gnu-freefont/TROUBLESHOOTING
%{_texmfdistdir}/doc/fonts/gnu-freefont/USAGE
%{_texmfdistdir}/doc/fonts/gnu-freefont/notes/README-downloads.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/notes/building.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/notes/features.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/notes/maintenance.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/notes/troubleshooting.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/notes/usage.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/notes/webfont_guidelines.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/MacTT
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/OpenType
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/TrueType
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/WOFF
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/buildutils.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/buildutils.pyc
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/OS2UnicodeRange
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/OpenType/UnicodeRanges.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/OpenType/__init__.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/kernclasses.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/ligatureLookups.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/private_use.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/range_report.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/script-menu/nameBySlot.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/script-menu/unnameBySlot.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/CheckConformance.pl
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-1.lst
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-1.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-2.lst
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-2.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-3B.lst
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-3B.txt
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/WGL4.lst
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/mes-list-expand.pl
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/checkGlyphNumbers.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/findBackLayers.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/isMonoMono.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/ranges/Arabic/arabic_test.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/ranges/Arabic/generate_arabic_shaping.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/ranges/Arabic/unicode_joining.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/validate.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/KerningNumerals.pl
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/fontforge-interp.sh
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/freefont-ttf.spec
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/hex_range.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/metafont/bulk_eps_import.py
%{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/special-purpose/makeBraille.py

%files -n texlive-gnu-freefont
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMono.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMonoBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMonoBoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMonoOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSans.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSansBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSansBoldOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSansOblique.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerif.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerifBold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerifBoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerifItalic.otf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMono.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMonoBold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMonoBoldOblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMonoOblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSans.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSansBold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSansBoldOblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSansOblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerif.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerifBold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerifBoldItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerifItalic.ttf

%files -n texlive-gnu-freefont-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gnu-freefont
%{_datadir}/fontconfig/conf.avail/58-texlive-gnu-freefont.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gnu-freefont/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gnu-freefont/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gnu-freefont/fonts.scale
%{_datadir}/fonts/texlive-gnu-freefont/FreeMono.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeMonoBold.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeMonoBoldOblique.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeMonoOblique.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSans.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSansBold.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSansBoldOblique.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSansOblique.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerif.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerifBold.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerifBoldItalic.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerifItalic.otf
%{_datadir}/fonts/texlive-gnu-freefont/FreeMono.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeMonoBold.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeMonoBoldOblique.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeMonoOblique.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSans.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSansBold.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSansBoldOblique.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSansOblique.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerif.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerifBold.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerifBoldItalic.ttf
%{_datadir}/fonts/texlive-gnu-freefont/FreeSerifItalic.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gnu-freefont-fonts-%{texlive_version}.%{texlive_noarch}.svn29349-%{release}-zypper
%endif

%package -n texlive-gnuplottex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.5svn54758
Release:        0
Summary:        Embed Gnuplot commands in LaTeX documents
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
Recommends:     texlive-gnuplottex-doc >= %{texlive_version}
Provides:       tex(gnuplottex.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(moreverb.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source70:       gnuplottex.tar.xz
Source71:       gnuplottex.doc.tar.xz

%description -n texlive-gnuplottex
This package allows you to include Gnuplot graphs in your LaTeX
documents. The gnuplot code is extracted from the document and
written to .gnuplot files. Then, if shell escape is used, the
graph files are automatically processed to graphics or LaTeX
code files which will then be included in the document. If
shell escape isn't used, the user will have to manually convert
the files by running gnuplot on the extracted .gnuplot files.

%package -n texlive-gnuplottex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.5svn54758
Release:        0
Summary:        Documentation for texlive-gnuplottex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gnuplottex-doc
This package includes the documentation for texlive-gnuplottex

%post -n texlive-gnuplottex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gnuplottex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gnuplottex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gnuplottex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gnuplottex/README
%{_texmfdistdir}/doc/latex/gnuplottex/SomeValuesForGnuplot.txt
%{_texmfdistdir}/doc/latex/gnuplottex/example-pdf.tex
%{_texmfdistdir}/doc/latex/gnuplottex/example.gnuplot
%{_texmfdistdir}/doc/latex/gnuplottex/gnuplottex.pdf
%{_texmfdistdir}/doc/latex/gnuplottex/gpl.txt

%files -n texlive-gnuplottex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gnuplottex/gnuplottex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gnuplottex-%{texlive_version}.%{texlive_noarch}.0.0.9.5svn54758-%{release}-zypper
%endif

%package -n texlive-go
Version:        %{texlive_version}.%{texlive_noarch}.svn28628
Release:        0
Summary:        Fonts and macros for typesetting go games
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
Recommends:     texlive-go-doc >= %{texlive_version}
Provides:       tex(go.sty)
Provides:       tex(go10.tfm)
Provides:       tex(go15.tfm)
Provides:       tex(go1bla10.tfm)
Provides:       tex(go1bla15.tfm)
Provides:       tex(go1bla20.tfm)
Provides:       tex(go1whi10.tfm)
Provides:       tex(go1whi15.tfm)
Provides:       tex(go1whi20.tfm)
Provides:       tex(go20.tfm)
Provides:       tex(go2bla10.tfm)
Provides:       tex(go2bla15.tfm)
Provides:       tex(go2bla20.tfm)
Provides:       tex(go2whi10.tfm)
Provides:       tex(go2whi15.tfm)
Provides:       tex(go2whi20.tfm)
Provides:       tex(gosign50.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source72:       go.tar.xz
Source73:       go.doc.tar.xz

%description -n texlive-go
The macros provide for nothing more complicated than the
standard 19x19 board; the fonts are written in Metafont.

%package -n texlive-go-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn28628
Release:        0
Summary:        Documentation for texlive-go
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-go-doc
This package includes the documentation for texlive-go

%post -n texlive-go
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-go 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-go
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-go-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/go/gomaps.ltx

%files -n texlive-go
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/go/go.mf
%{_texmfdistdir}/fonts/source/public/go/go10.mf
%{_texmfdistdir}/fonts/source/public/go/go15.mf
%{_texmfdistdir}/fonts/source/public/go/go1bla10.mf
%{_texmfdistdir}/fonts/source/public/go/go1bla15.mf
%{_texmfdistdir}/fonts/source/public/go/go1bla20.mf
%{_texmfdistdir}/fonts/source/public/go/go1black.mf
%{_texmfdistdir}/fonts/source/public/go/go1whi10.mf
%{_texmfdistdir}/fonts/source/public/go/go1whi15.mf
%{_texmfdistdir}/fonts/source/public/go/go1whi20.mf
%{_texmfdistdir}/fonts/source/public/go/go1white.mf
%{_texmfdistdir}/fonts/source/public/go/go20.mf
%{_texmfdistdir}/fonts/source/public/go/go2bla10.mf
%{_texmfdistdir}/fonts/source/public/go/go2bla15.mf
%{_texmfdistdir}/fonts/source/public/go/go2bla20.mf
%{_texmfdistdir}/fonts/source/public/go/go2black.mf
%{_texmfdistdir}/fonts/source/public/go/go2whi10.mf
%{_texmfdistdir}/fonts/source/public/go/go2whi15.mf
%{_texmfdistdir}/fonts/source/public/go/go2whi20.mf
%{_texmfdistdir}/fonts/source/public/go/go2white.mf
%{_texmfdistdir}/fonts/source/public/go/gosign50.mf
%{_texmfdistdir}/fonts/tfm/public/go/go10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1bla10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1bla15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1bla20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1whi10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1whi15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1whi20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2bla10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2bla15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2bla20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2whi10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2whi15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2whi20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/gosign50.tfm
%{_texmfdistdir}/tex/latex/go/go.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-go-%{texlive_version}.%{texlive_noarch}.svn28628-%{release}-zypper
%endif

%package -n texlive-gobble
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn49608
Release:        0
Summary:        More gobble macros for PlainTeX and LaTeX
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
Recommends:     texlive-gobble-doc >= %{texlive_version}
Provides:       tex(gobble-user.sty)
Provides:       tex(gobble.sty)
Provides:       tex(gobble.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source74:       gobble.tar.xz
Source75:       gobble.doc.tar.xz

%description -n texlive-gobble
The LaTeX package gobble includes several gobble macros not
included in the LaTeX kernel. These macros remove a number of
arguments after them, a feature regulary used inside other
macros. This includes gobble macros for optional arguments. The
LaTeX package gobble-user provides these macros at the user
level, i.e. using names without @ so that these can be used
without \makeatletter and \makeatother. The same macros are
provided inside .tex files for use with plain-TeX or other TeX
formats. However, the gobble macros for optional macros require
\@ifnextchar to be defined.

%package -n texlive-gobble-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn49608
Release:        0
Summary:        Documentation for texlive-gobble
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gobble-doc
This package includes the documentation for texlive-gobble

%post -n texlive-gobble
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gobble 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gobble
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gobble-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/gobble/README
%{_texmfdistdir}/doc/generic/gobble/gobble-user.tex
%{_texmfdistdir}/doc/generic/gobble/gobble.pdf

%files -n texlive-gobble
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/gobble/gobble-user.sty
%{_texmfdistdir}/tex/generic/gobble/gobble.sty
%{_texmfdistdir}/tex/generic/gobble/gobble.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gobble-%{texlive_version}.%{texlive_noarch}.0.0.2svn49608-%{release}-zypper
%endif

%package -n texlive-gofonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        GoSans and GoMono fonts with LaTeX support
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
Requires:       texlive-gofonts-fonts >= %{texlive_version}
Recommends:     texlive-gofonts-doc >= %{texlive_version}
Provides:       tex(Go-Bold-Italic-tlf-lgr--base.tfm)
Provides:       tex(Go-Bold-Italic-tlf-lgr.tfm)
Provides:       tex(Go-Bold-Italic-tlf-lgr.vf)
Provides:       tex(Go-Bold-Italic-tlf-ly1--base.tfm)
Provides:       tex(Go-Bold-Italic-tlf-ly1.tfm)
Provides:       tex(Go-Bold-Italic-tlf-ly1.vf)
Provides:       tex(Go-Bold-Italic-tlf-ot1.tfm)
Provides:       tex(Go-Bold-Italic-tlf-t1--base.tfm)
Provides:       tex(Go-Bold-Italic-tlf-t1.tfm)
Provides:       tex(Go-Bold-Italic-tlf-t1.vf)
Provides:       tex(Go-Bold-Italic-tlf-ts1--base.tfm)
Provides:       tex(Go-Bold-Italic-tlf-ts1.tfm)
Provides:       tex(Go-Bold-Italic-tlf-ts1.vf)
Provides:       tex(Go-Bold-tlf-lgr--base.tfm)
Provides:       tex(Go-Bold-tlf-lgr.tfm)
Provides:       tex(Go-Bold-tlf-lgr.vf)
Provides:       tex(Go-Bold-tlf-ly1--base.tfm)
Provides:       tex(Go-Bold-tlf-ly1.tfm)
Provides:       tex(Go-Bold-tlf-ly1.vf)
Provides:       tex(Go-Bold-tlf-ot1.tfm)
Provides:       tex(Go-Bold-tlf-t1--base.tfm)
Provides:       tex(Go-Bold-tlf-t1.tfm)
Provides:       tex(Go-Bold-tlf-t1.vf)
Provides:       tex(Go-Bold-tlf-ts1--base.tfm)
Provides:       tex(Go-Bold-tlf-ts1.tfm)
Provides:       tex(Go-Bold-tlf-ts1.vf)
Provides:       tex(Go-Medium-Italic-tlf-lgr--base.tfm)
Provides:       tex(Go-Medium-Italic-tlf-lgr.tfm)
Provides:       tex(Go-Medium-Italic-tlf-lgr.vf)
Provides:       tex(Go-Medium-Italic-tlf-ly1--base.tfm)
Provides:       tex(Go-Medium-Italic-tlf-ly1.tfm)
Provides:       tex(Go-Medium-Italic-tlf-ly1.vf)
Provides:       tex(Go-Medium-Italic-tlf-ot1.tfm)
Provides:       tex(Go-Medium-Italic-tlf-t1--base.tfm)
Provides:       tex(Go-Medium-Italic-tlf-t1.tfm)
Provides:       tex(Go-Medium-Italic-tlf-t1.vf)
Provides:       tex(Go-Medium-Italic-tlf-ts1--base.tfm)
Provides:       tex(Go-Medium-Italic-tlf-ts1.tfm)
Provides:       tex(Go-Medium-Italic-tlf-ts1.vf)
Provides:       tex(Go-Medium-tlf-lgr--base.tfm)
Provides:       tex(Go-Medium-tlf-lgr.tfm)
Provides:       tex(Go-Medium-tlf-lgr.vf)
Provides:       tex(Go-Medium-tlf-ly1--base.tfm)
Provides:       tex(Go-Medium-tlf-ly1.tfm)
Provides:       tex(Go-Medium-tlf-ly1.vf)
Provides:       tex(Go-Medium-tlf-ot1.tfm)
Provides:       tex(Go-Medium-tlf-t1--base.tfm)
Provides:       tex(Go-Medium-tlf-t1.tfm)
Provides:       tex(Go-Medium-tlf-t1.vf)
Provides:       tex(Go-Medium-tlf-ts1--base.tfm)
Provides:       tex(Go-Medium-tlf-ts1.tfm)
Provides:       tex(Go-Medium-tlf-ts1.vf)
Provides:       tex(Go-Regular-Italic-tlf-lgr--base.tfm)
Provides:       tex(Go-Regular-Italic-tlf-lgr.tfm)
Provides:       tex(Go-Regular-Italic-tlf-lgr.vf)
Provides:       tex(Go-Regular-Italic-tlf-ly1--base.tfm)
Provides:       tex(Go-Regular-Italic-tlf-ly1.tfm)
Provides:       tex(Go-Regular-Italic-tlf-ly1.vf)
Provides:       tex(Go-Regular-Italic-tlf-ot1.tfm)
Provides:       tex(Go-Regular-Italic-tlf-t1--base.tfm)
Provides:       tex(Go-Regular-Italic-tlf-t1.tfm)
Provides:       tex(Go-Regular-Italic-tlf-t1.vf)
Provides:       tex(Go-Regular-Italic-tlf-ts1--base.tfm)
Provides:       tex(Go-Regular-Italic-tlf-ts1.tfm)
Provides:       tex(Go-Regular-Italic-tlf-ts1.vf)
Provides:       tex(Go-Regular-tlf-lgr--base.tfm)
Provides:       tex(Go-Regular-tlf-lgr.tfm)
Provides:       tex(Go-Regular-tlf-lgr.vf)
Provides:       tex(Go-Regular-tlf-ly1--base.tfm)
Provides:       tex(Go-Regular-tlf-ly1.tfm)
Provides:       tex(Go-Regular-tlf-ly1.vf)
Provides:       tex(Go-Regular-tlf-ot1.tfm)
Provides:       tex(Go-Regular-tlf-t1--base.tfm)
Provides:       tex(Go-Regular-tlf-t1.tfm)
Provides:       tex(Go-Regular-tlf-t1.vf)
Provides:       tex(Go-Regular-tlf-ts1--base.tfm)
Provides:       tex(Go-Regular-tlf-ts1.tfm)
Provides:       tex(Go-Regular-tlf-ts1.vf)
Provides:       tex(GoMono-Bold-tlf-lgr--base.tfm)
Provides:       tex(GoMono-Bold-tlf-lgr.tfm)
Provides:       tex(GoMono-Bold-tlf-lgr.vf)
Provides:       tex(GoMono-Bold-tlf-ly1--base.tfm)
Provides:       tex(GoMono-Bold-tlf-ly1.tfm)
Provides:       tex(GoMono-Bold-tlf-ly1.vf)
Provides:       tex(GoMono-Bold-tlf-ot1.tfm)
Provides:       tex(GoMono-Bold-tlf-t1--base.tfm)
Provides:       tex(GoMono-Bold-tlf-t1.tfm)
Provides:       tex(GoMono-Bold-tlf-t1.vf)
Provides:       tex(GoMono-Bold-tlf-ts1--base.tfm)
Provides:       tex(GoMono-Bold-tlf-ts1.tfm)
Provides:       tex(GoMono-Bold-tlf-ts1.vf)
Provides:       tex(GoMono-BoldItalic-tlf-lgr--base.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-lgr.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-lgr.vf)
Provides:       tex(GoMono-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-ly1.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-ly1.vf)
Provides:       tex(GoMono-BoldItalic-tlf-ot1.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-t1.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-t1.vf)
Provides:       tex(GoMono-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-ts1.tfm)
Provides:       tex(GoMono-BoldItalic-tlf-ts1.vf)
Provides:       tex(GoMono-Italic-tlf-lgr--base.tfm)
Provides:       tex(GoMono-Italic-tlf-lgr.tfm)
Provides:       tex(GoMono-Italic-tlf-lgr.vf)
Provides:       tex(GoMono-Italic-tlf-ly1--base.tfm)
Provides:       tex(GoMono-Italic-tlf-ly1.tfm)
Provides:       tex(GoMono-Italic-tlf-ly1.vf)
Provides:       tex(GoMono-Italic-tlf-ot1.tfm)
Provides:       tex(GoMono-Italic-tlf-t1--base.tfm)
Provides:       tex(GoMono-Italic-tlf-t1.tfm)
Provides:       tex(GoMono-Italic-tlf-t1.vf)
Provides:       tex(GoMono-Italic-tlf-ts1--base.tfm)
Provides:       tex(GoMono-Italic-tlf-ts1.tfm)
Provides:       tex(GoMono-Italic-tlf-ts1.vf)
Provides:       tex(GoMono-tlf-lgr--base.tfm)
Provides:       tex(GoMono-tlf-lgr.tfm)
Provides:       tex(GoMono-tlf-lgr.vf)
Provides:       tex(GoMono-tlf-ly1--base.tfm)
Provides:       tex(GoMono-tlf-ly1.tfm)
Provides:       tex(GoMono-tlf-ly1.vf)
Provides:       tex(GoMono-tlf-ot1.tfm)
Provides:       tex(GoMono-tlf-t1--base.tfm)
Provides:       tex(GoMono-tlf-t1.tfm)
Provides:       tex(GoMono-tlf-t1.vf)
Provides:       tex(GoMono-tlf-ts1--base.tfm)
Provides:       tex(GoMono-tlf-ts1.tfm)
Provides:       tex(GoMono-tlf-ts1.vf)
Provides:       tex(GoMono.sty)
Provides:       tex(GoSans.sty)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-lgr--base.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-lgr.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-lgr.vf)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ly1--base.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ly1.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ly1.vf)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ot1--base.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ot1.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ot1.vf)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-t1--base.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-t1.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-t1.vf)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ts1--base.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ts1.tfm)
Provides:       tex(GoSmallcaps-Italic-tlf-sc-ts1.vf)
Provides:       tex(GoSmallcaps-tlf-sc-lgr--base.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-lgr.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-lgr.vf)
Provides:       tex(GoSmallcaps-tlf-sc-ly1--base.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-ly1.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-ly1.vf)
Provides:       tex(GoSmallcaps-tlf-sc-ot1--base.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-ot1.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-ot1.vf)
Provides:       tex(GoSmallcaps-tlf-sc-t1--base.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-t1.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-t1.vf)
Provides:       tex(GoSmallcaps-tlf-sc-ts1--base.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-ts1.tfm)
Provides:       tex(GoSmallcaps-tlf-sc-ts1.vf)
Provides:       tex(LGRGo-TLF.fd)
Provides:       tex(LGRGoMono-TLF.fd)
Provides:       tex(LY1Go-TLF.fd)
Provides:       tex(LY1GoMono-TLF.fd)
Provides:       tex(OT1Go-TLF.fd)
Provides:       tex(OT1GoMono-TLF.fd)
Provides:       tex(T1Go-TLF.fd)
Provides:       tex(T1GoMono-TLF.fd)
Provides:       tex(TS1Go-TLF.fd)
Provides:       tex(TS1GoMono-TLF.fd)
Provides:       tex(go.map)
Provides:       tex(go_2qimm2.enc)
Provides:       tex(go_4whde3.enc)
Provides:       tex(go_73mlya.enc)
Provides:       tex(go_c3licl.enc)
Provides:       tex(go_dhlxve.enc)
Provides:       tex(go_icpxvt.enc)
Provides:       tex(go_iypgt7.enc)
Provides:       tex(go_zwiz3b.enc)
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
Source76:       gofonts.tar.xz
Source77:       gofonts.doc.tar.xz

%description -n texlive-gofonts
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the GoSans and GoMono families of fonts designed by
the Bigelow & Holmes foundry for the Go project. GoSans is
available in three weights: Regular, Medium, and Bold (with
corresponding italics). GoMono is available in regular and
bold, with italics. Notes on the design may be found at
https://blog.golang.org/go-fonts.

%package -n texlive-gofonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Documentation for texlive-gofonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gofonts-doc
This package includes the documentation for texlive-gofonts


%package -n texlive-gofonts-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Severed fonts for texlive-gofonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gofonts-fonts
The  separated fonts package for texlive-gofonts
%post -n texlive-gofonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap go.map' >> /var/run/texlive/run-updmap

%postun -n texlive-gofonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap go.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-gofonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gofonts-fonts
%files -n texlive-gofonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gofonts/License
%{_texmfdistdir}/doc/fonts/gofonts/README
%{_texmfdistdir}/doc/fonts/gofonts/go-samples.pdf
%{_texmfdistdir}/doc/fonts/gofonts/go-samples.tex
%{_texmfdistdir}/doc/fonts/gofonts/gofonts.pdf

%files -n texlive-gofonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_2qimm2.enc
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_4whde3.enc
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_73mlya.enc
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_c3licl.enc
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_dhlxve.enc
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_icpxvt.enc
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_iypgt7.enc
%{_texmfdistdir}/fonts/enc/dvips/gofonts/go_zwiz3b.enc
%{_texmfdistdir}/fonts/map/dvips/gofonts/go.map
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Medium-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/Go-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoMono-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ts1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-lgr.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/bh/gofonts/GoSmallcaps-tlf-sc-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/Go-Bold-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/Go-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/Go-Medium-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/Go-Medium.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/Go-Regular-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/Go-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/GoMono-Bold-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/GoMono-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/GoMono-Regular-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/GoMono-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/GoSmallcaps-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/bh/gofonts/GoSmallcaps.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/Go-Bold-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/Go-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/Go-Medium-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/Go-Medium.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/Go-Regular-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/Go-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/GoMono-Bold-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/GoMono-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/GoMono-Regular-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/GoMono-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/GoSmallcaps-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/bh/gofonts/GoSmallcaps.pfb
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-Italic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-Italic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Medium-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-Italic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/Go-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Bold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-BoldItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Italic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoMono-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-Italic-tlf-sc-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-Italic-tlf-sc-ts1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-tlf-sc-lgr.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/bh/gofonts/GoSmallcaps-tlf-sc-ts1.vf
%{_texmfdistdir}/tex/latex/gofonts/GoMono.sty
%{_texmfdistdir}/tex/latex/gofonts/GoSans.sty
%{_texmfdistdir}/tex/latex/gofonts/LGRGo-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/LGRGoMono-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/LY1Go-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/LY1GoMono-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/OT1Go-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/OT1GoMono-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/T1Go-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/T1GoMono-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/TS1Go-TLF.fd
%{_texmfdistdir}/tex/latex/gofonts/TS1GoMono-TLF.fd

%files -n texlive-gofonts-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gofonts
%{_datadir}/fontconfig/conf.avail/58-texlive-gofonts.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-gofonts.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-gofonts.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gofonts/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gofonts/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gofonts/fonts.scale
%{_datadir}/fonts/texlive-gofonts/Go-Bold-Italic.ttf
%{_datadir}/fonts/texlive-gofonts/Go-Bold.ttf
%{_datadir}/fonts/texlive-gofonts/Go-Medium-Italic.ttf
%{_datadir}/fonts/texlive-gofonts/Go-Medium.ttf
%{_datadir}/fonts/texlive-gofonts/Go-Regular-Italic.ttf
%{_datadir}/fonts/texlive-gofonts/Go-Regular.ttf
%{_datadir}/fonts/texlive-gofonts/GoMono-Bold-Italic.ttf
%{_datadir}/fonts/texlive-gofonts/GoMono-Bold.ttf
%{_datadir}/fonts/texlive-gofonts/GoMono-Regular-Italic.ttf
%{_datadir}/fonts/texlive-gofonts/GoMono-Regular.ttf
%{_datadir}/fonts/texlive-gofonts/GoSmallcaps-Italic.ttf
%{_datadir}/fonts/texlive-gofonts/GoSmallcaps.ttf
%{_datadir}/fonts/texlive-gofonts/Go-Bold-Italic.pfb
%{_datadir}/fonts/texlive-gofonts/Go-Bold.pfb
%{_datadir}/fonts/texlive-gofonts/Go-Medium-Italic.pfb
%{_datadir}/fonts/texlive-gofonts/Go-Medium.pfb
%{_datadir}/fonts/texlive-gofonts/Go-Regular-Italic.pfb
%{_datadir}/fonts/texlive-gofonts/Go-Regular.pfb
%{_datadir}/fonts/texlive-gofonts/GoMono-Bold-Italic.pfb
%{_datadir}/fonts/texlive-gofonts/GoMono-Bold.pfb
%{_datadir}/fonts/texlive-gofonts/GoMono-Regular-Italic.pfb
%{_datadir}/fonts/texlive-gofonts/GoMono-Regular.pfb
%{_datadir}/fonts/texlive-gofonts/GoSmallcaps-Italic.pfb
%{_datadir}/fonts/texlive-gofonts/GoSmallcaps.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gofonts-fonts-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif

%package -n texlive-gost
Version:        %{texlive_version}.%{texlive_noarch}.1.2isvn44131
Release:        0
Summary:        BibTeX styles to format according to GOST
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
Recommends:     texlive-gost-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source78:       gost.tar.xz
Source79:       gost.doc.tar.xz

%description -n texlive-gost
BibTeX styles to format bibliographies in English, Russian or
Ukrainian according to GOST 7.0.5-2008 or GOST 7.1-2003. Both
8-bit and Unicode (UTF-8) versions of each BibTeX style, in
each case offering a choice of sorted and unsorted. Further, a
set of three styles (which do not conform to current standards)
are retained for backwards compatibility.

%package -n texlive-gost-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2isvn44131
Release:        0
Summary:        Documentation for texlive-gost
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-gost-doc:en)

%description -n texlive-gost-doc
This package includes the documentation for texlive-gost

%post -n texlive-gost
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gost 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gost
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gost-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/gost/README.md
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex01.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex02.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex03.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex04.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex05.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex06.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex06a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex07.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex08.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex09.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex10.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex11.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex12.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex13.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex14.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex14a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex15.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex16.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex17.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex17a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex17b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex18.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex19.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex20.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex20a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex20b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex20c.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex21.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex21a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex21b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex23.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex24.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex24a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex24b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex25.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex26.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex27a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex27b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex27c.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex28.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex28a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex29.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex30.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/ex31.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/bib/examples.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2003.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2003.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008-customized.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008-customized.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008l.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008l.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008n.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008n.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008ns.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost2008ns.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost780.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/gost780.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/cp1251/make-examples-on-win-cp1251.cmd
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex01.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex02.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex03.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex04.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex05.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex06.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex06a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex07.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex08.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex09.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex10.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex11.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex12.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex13.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex14.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex14a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex15.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex16.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex17.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex17a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex17b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex18.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex19.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex20.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex20a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex20b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex20c.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex21.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex21a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex21b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex22.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex22a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex23.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex24.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex24a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex24b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex25.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex26.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex27a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex27b.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex27c.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex28.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex28a.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex29.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex30.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/ex31.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/bib/examples.bib
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/make-examples-on-win-utf8.cmd
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2003.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2003.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008-customized.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008-customized.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008l.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008l.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008n.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008n.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008ns.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008ns.tex
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008s.pdf
%{_texmfdistdir}/doc/bibtex/gost/examples/utf8/ugost2008s.tex
%{_texmfdistdir}/doc/bibtex/gost/gost.pdf

%files -n texlive-gost
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/gost/gost2003.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2003s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008l.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008ls.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008n.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008ns.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780s.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2003.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2003s.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008l.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008ls.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008n.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008ns.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008s.bst
%{_texmfdistdir}/bibtex/csf/gost/cp1251.csf
%{_texmfdistdir}/bibtex/csf/gost/koi8u.csf
%{_texmfdistdir}/bibtex/csf/gost/ruscii.csf
%{_texmfdistdir}/bibtex/csf/gost/utf8cyrillic.csf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gost-%{texlive_version}.%{texlive_noarch}.1.2isvn44131-%{release}-zypper
%endif

%package -n texlive-gothic
Version:        %{texlive_version}.%{texlive_noarch}.svn49869
Release:        0
Summary:        A collection of old German-style fonts
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
Recommends:     texlive-gothic-doc >= %{texlive_version}
Provides:       tex(cmfrak.tfm)
Provides:       tex(schwell.tfm)
Provides:       tex(suet14.tfm)
Provides:       tex(yfrak.tfm)
Provides:       tex(ygoth.tfm)
Provides:       tex(yinit.tfm)
Provides:       tex(ysmfrak.tfm)
Provides:       tex(yswab.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source80:       gothic.tar.xz
Source81:       gothic.doc.tar.xz

%description -n texlive-gothic
A collection of fonts that reproduce those used in "old German"
printing and handwriting. The set comprises Gothic, Schwabacher
and Fraktur fonts, a pair of handwriting fonts, Sutterlin and
Schwell, and a font containing decorative initials. In
addition, there are two re-encoding packages for Haralambous's
fonts, providing T1, using virtual fonts, and OT1 and T1, using
Metafont.

%package -n texlive-gothic-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn49869
Release:        0
Summary:        Documentation for texlive-gothic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gothic-doc
This package includes the documentation for texlive-gothic

%post -n texlive-gothic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gothic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gothic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gothic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/gothic/00readme_fraktur.msg
%{_texmfdistdir}/doc/fonts/gothic/README.sueterlin
%{_texmfdistdir}/doc/fonts/gothic/README.yinit
%{_texmfdistdir}/doc/fonts/gothic/suet.pdf
%{_texmfdistdir}/doc/fonts/gothic/suet.tex
%{_texmfdistdir}/doc/fonts/gothic/yinit.pdf

%files -n texlive-gothic
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/gothic/cmfrabase.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfraklow.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrakmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfraknum.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrakoth.mf
%{_texmfdistdir}/fonts/source/public/gothic/cmfrakupp.mf
%{_texmfdistdir}/fonts/source/public/gothic/dcfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/schwell.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-lig.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-low.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-spec.mf
%{_texmfdistdir}/fonts/source/public/gothic/su-upp.mf
%{_texmfdistdir}/fonts/source/public/gothic/suet14.mf
%{_texmfdistdir}/fonts/source/public/gothic/xxfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrabase.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfraklow.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrakmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfraknum.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrakoth.mf
%{_texmfdistdir}/fonts/source/public/gothic/yfrakupp.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygotbase.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygoth.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothgen.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothlig.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothlow.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothnum.mf
%{_texmfdistdir}/fonts/source/public/gothic/ygothupp.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinit.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitA.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitB.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitC.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitD.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitE.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitF.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitG.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitH.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitJ.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitK.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitL.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitM.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitN.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitO.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitP.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitQ.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitR.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitS.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitT.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitU.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitV.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitW.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitX.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitY.mf
%{_texmfdistdir}/fonts/source/public/gothic/yinitZ.mf
%{_texmfdistdir}/fonts/source/public/gothic/yintbase.mf
%{_texmfdistdir}/fonts/source/public/gothic/ysmfrak.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswab.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabase.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswablow.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabmis.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabnum.mf
%{_texmfdistdir}/fonts/source/public/gothic/yswabupp.mf
%{_texmfdistdir}/fonts/tfm/public/gothic/cmfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/schwell.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/suet14.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/ygoth.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yinit.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/ysmfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/gothic/yswab.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gothic-%{texlive_version}.%{texlive_noarch}.svn49869-%{release}-zypper
%endif

%package -n texlive-gotoh
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44764
Release:        0
Summary:        An implementation of the Gotoh sequence alignment algorithm
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
Recommends:     texlive-gotoh-doc >= %{texlive_version}
Provides:       tex(gotoh.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source82:       gotoh.tar.xz
Source83:       gotoh.doc.tar.xz

%description -n texlive-gotoh
This package calculates biological sequence alignment with the
Gotoh algorithm. The package also provides an interface to
control various settings including algorithm parameters.

%package -n texlive-gotoh-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn44764
Release:        0
Summary:        Documentation for texlive-gotoh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gotoh-doc
This package includes the documentation for texlive-gotoh

%post -n texlive-gotoh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gotoh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gotoh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gotoh-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gotoh/LICENSE
%{_texmfdistdir}/doc/latex/gotoh/README.md
%{_texmfdistdir}/doc/latex/gotoh/gotoh.pdf

%files -n texlive-gotoh
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gotoh/gotoh.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gotoh-%{texlive_version}.%{texlive_noarch}.1.1svn44764-%{release}-zypper
%endif

%package -n texlive-grabbox
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51052
Release:        0
Summary:        Read an argument into a box and execute the code afterwards
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
Recommends:     texlive-grabbox-doc >= %{texlive_version}
Provides:       tex(grabbox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source84:       grabbox.tar.xz
Source85:       grabbox.doc.tar.xz

%description -n texlive-grabbox
The package provides the command \grabbox, which grabs an
argument into a box and executes the code afterwards.

%package -n texlive-grabbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51052
Release:        0
Summary:        Documentation for texlive-grabbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grabbox-doc
This package includes the documentation for texlive-grabbox

%post -n texlive-grabbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grabbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grabbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grabbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grabbox/README.md
%{_texmfdistdir}/doc/latex/grabbox/grabbox.pdf

%files -n texlive-grabbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grabbox/grabbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grabbox-%{texlive_version}.%{texlive_noarch}.1.4svn51052-%{release}-zypper
%endif

%package -n texlive-gradientframe
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn21387
Release:        0
Summary:        Simple gradient frames around objects
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
Recommends:     texlive-gradientframe-doc >= %{texlive_version}
Provides:       tex(gradientframe.sty)
Requires:       tex(color.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source86:       gradientframe.tar.xz
Source87:       gradientframe.doc.tar.xz

%description -n texlive-gradientframe
The package provides a means of drawing graded frames around
objects. The gradients of the frames are drawn using the color
package.

%package -n texlive-gradientframe-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn21387
Release:        0
Summary:        Documentation for texlive-gradientframe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gradientframe-doc
This package includes the documentation for texlive-gradientframe

%post -n texlive-gradientframe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gradientframe 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gradientframe
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gradientframe-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gradientframe/README
%{_texmfdistdir}/doc/latex/gradientframe/gradientframe.pdf

%files -n texlive-gradientframe
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gradientframe/gradientframe.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gradientframe-%{texlive_version}.%{texlive_noarch}.0.0.2svn21387-%{release}-zypper
%endif

%package -n texlive-gradstudentresume
Version:        %{texlive_version}.%{texlive_noarch}.svn38832
Release:        0
Summary:        A generic template for graduate student resumes
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
Recommends:     texlive-gradstudentresume-doc >= %{texlive_version}
Provides:       tex(gradstudentresume.cls)
Requires:       tex(anysize.sty)
Requires:       tex(hyperref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source88:       gradstudentresume.tar.xz
Source89:       gradstudentresume.doc.tar.xz

%description -n texlive-gradstudentresume
The package offers a template for graduate students writing an
academic CV. The goal is to create a flexible template that can
be customized based on each specific individual's needs.

%package -n texlive-gradstudentresume-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn38832
Release:        0
Summary:        Documentation for texlive-gradstudentresume
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gradstudentresume-doc
This package includes the documentation for texlive-gradstudentresume

%post -n texlive-gradstudentresume
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gradstudentresume 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gradstudentresume
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gradstudentresume-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gradstudentresume/README.txt
%{_texmfdistdir}/doc/latex/gradstudentresume/example.tex

%files -n texlive-gradstudentresume
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gradstudentresume/gradstudentresume.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gradstudentresume-%{texlive_version}.%{texlive_noarch}.svn38832-%{release}-zypper
%endif

%package -n texlive-grafcet
Version:        %{texlive_version}.%{texlive_noarch}.1.3.5svn22509
Release:        0
Summary:        Draw Grafcet/SFC with TikZ
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
Recommends:     texlive-grafcet-doc >= %{texlive_version}
Provides:       tex(grafcet.sty)
Requires:       tex(ifsym.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source90:       grafcet.tar.xz
Source91:       grafcet.doc.tar.xz

%description -n texlive-grafcet
The package provides a library (GRAFCET) that can draw Grafcet
Sequential Function Chart (SFC) diagrams, in accordance with EN
60848, using Pgf/TikZ. L'objectif de la librairie GRAFCET est
de permettre le trace de grafcet selon la norme EN 60848 a
partir de Pgf/TikZ.

%package -n texlive-grafcet-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.5svn22509
Release:        0
Summary:        Documentation for texlive-grafcet
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-grafcet-doc:fr)

%description -n texlive-grafcet-doc
This package includes the documentation for texlive-grafcet

%post -n texlive-grafcet
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grafcet 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grafcet
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grafcet-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grafcet/README
%{_texmfdistdir}/doc/latex/grafcet/grafcet.pdf
%{_texmfdistdir}/doc/latex/grafcet/grafcet.tex

%files -n texlive-grafcet
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grafcet/grafcet.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grafcet-%{texlive_version}.%{texlive_noarch}.1.3.5svn22509-%{release}-zypper
%endif

%package -n texlive-grant
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.3svn41905
Release:        0
Summary:        Classes for formatting federal grant proposals
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
Recommends:     texlive-grant-doc >= %{texlive_version}
Provides:       tex(grant-arl.cls)
Provides:       tex(grant-darpa.cls)
Provides:       tex(grant-doe.cls)
Provides:       tex(grant-nih.cls)
Provides:       tex(grant-nrl.cls)
Provides:       tex(grant-nsf.cls)
Provides:       tex(grant-onr.cls)
Provides:       tex(grant.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(book.cls)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(chappg.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(hyphenat.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lineno.sty)
Requires:       tex(longtable.sty)
Requires:       tex(ltxtable.sty)
Requires:       tex(multicol.sty)
Requires:       tex(paralist.sty)
Requires:       tex(pdfcomment.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(placeins.sty)
Requires:       tex(setspace.sty)
Requires:       tex(soul.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(ulem.sty)
Requires:       tex(wrapfig.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source92:       grant.tar.xz
Source93:       grant.doc.tar.xz

%description -n texlive-grant
LaTeX classes for formatting federal grant proposals: grant:
Base class for formatting grant proposals grant-arl: Army
Research Laboratory grant-darpa: Defense Advanced Research
Projects Agency grant-doe: Department of Energy grant-nih:
National Institutes of Health grant-nrl: Naval Research
Laboratory grant-nsf: National Science Foundation grant-onr:
Office of Naval Research

%package -n texlive-grant-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.3svn41905
Release:        0
Summary:        Documentation for texlive-grant
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grant-doc
This package includes the documentation for texlive-grant

%post -n texlive-grant
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grant 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grant
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grant-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grant/LICENSE
%{_texmfdistdir}/doc/latex/grant/README.md
%{_texmfdistdir}/doc/latex/grant/VERSION
%{_texmfdistdir}/doc/latex/grant/grant.pdf

%files -n texlive-grant
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grant/grant-arl.cls
%{_texmfdistdir}/tex/latex/grant/grant-darpa.cls
%{_texmfdistdir}/tex/latex/grant/grant-doe.cls
%{_texmfdistdir}/tex/latex/grant/grant-nih.cls
%{_texmfdistdir}/tex/latex/grant/grant-nrl.cls
%{_texmfdistdir}/tex/latex/grant/grant-nsf.cls
%{_texmfdistdir}/tex/latex/grant/grant-onr.cls
%{_texmfdistdir}/tex/latex/grant/grant.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grant-%{texlive_version}.%{texlive_noarch}.0.0.0.3svn41905-%{release}-zypper
%endif

%package -n texlive-graph35
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn47522
Release:        0
Summary:        Draw keys and screen items of several Casio calculators
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
Recommends:     texlive-graph35-doc >= %{texlive_version}
Provides:       tex(graph35-keys.sty)
Provides:       tex(graph35-pixelart.sty)
Provides:       tex(graph35.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(letterspace.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(pixelart.sty)
Requires:       tex(sansmath.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source94:       graph35.tar.xz
Source95:       graph35.doc.tar.xz

%description -n texlive-graph35
This package defines commands to draw the Casio Graph 35 /
fx-9750GII calculator (and other models). It can draw the whole
calculator, or parts of it (individual keys, part of the
screen, etc.). It was written to typeset documents instructing
stundents how to use their calculator.

%package -n texlive-graph35-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn47522
Release:        0
Summary:        Documentation for texlive-graph35
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graph35-doc
This package includes the documentation for texlive-graph35

%post -n texlive-graph35
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graph35 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graph35
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graph35-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graph35/CHANGELOG.md
%{_texmfdistdir}/doc/latex/graph35/LICENSE.txt
%{_texmfdistdir}/doc/latex/graph35/README.md
%{_texmfdistdir}/doc/latex/graph35/graph35-en.pdf
%{_texmfdistdir}/doc/latex/graph35/graph35-fr.pdf

%files -n texlive-graph35
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graph35/graph35-keys.sty
%{_texmfdistdir}/tex/latex/graph35/graph35-pixelart.sty
%{_texmfdistdir}/tex/latex/graph35/graph35.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graph35-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn47522-%{release}-zypper
%endif

%package -n texlive-graphbox
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46360
Release:        0
Summary:        Extend graphicx to improve placement of graphics
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
Recommends:     texlive-graphbox-doc >= %{texlive_version}
Provides:       tex(graphbox.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source96:       graphbox.tar.xz
Source97:       graphbox.doc.tar.xz

%description -n texlive-graphbox
Graphbox is an extension of the standard graphicx LaTeX2e
package to allow the placement of graphics relative to the
"current position" using additional optional arguments of
\includegraphics. For example, changing the vertical alignment
is convenient for using graphics as elements of (mathematical)
formulae. Options for shifting, smashing and hiding the
graphics may be useful in support, for example, of the beamer
framework.

%package -n texlive-graphbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46360
Release:        0
Summary:        Documentation for texlive-graphbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphbox-doc
This package includes the documentation for texlive-graphbox

%post -n texlive-graphbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphbox/README.txt
%{_texmfdistdir}/doc/latex/graphbox/gboxsamp.mps
%{_texmfdistdir}/doc/latex/graphbox/gboxsamp.tex
%{_texmfdistdir}/doc/latex/graphbox/graphbox.pdf

%files -n texlive-graphbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphbox/graphbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphbox-%{texlive_version}.%{texlive_noarch}.1.1svn46360-%{release}-zypper
%endif

%package -n texlive-graphics
Version:        %{texlive_version}.%{texlive_noarch}.svn53640
Release:        0
Summary:        The LaTeX standard graphics bundle
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-graphics-cfg >= %{texlive_version}
Requires:       tex(color.cfg)
#!BuildIgnore: texlive-graphics-cfg
Requires:       texlive-graphics-def >= %{texlive_version}
#!BuildIgnore: texlive-graphics-def
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-graphics-doc >= %{texlive_version}
Provides:       tex(color.sty)
Provides:       tex(dvipdf.def)
Provides:       tex(dvipsnam.def)
Provides:       tex(dvipsone.def)
Provides:       tex(dviwin.def)
Provides:       tex(emtex.def)
Provides:       tex(epsfig.sty)
Provides:       tex(graphics-2017-06-25.sty)
Provides:       tex(graphics.sty)
Provides:       tex(graphicx.sty)
Provides:       tex(keyval.sty)
Provides:       tex(lscape.sty)
Provides:       tex(pctex32.def)
Provides:       tex(pctexhp.def)
Provides:       tex(pctexps.def)
Provides:       tex(pctexwin.def)
Provides:       tex(rotating.sty)
Provides:       tex(tcidvi.def)
Provides:       tex(trig.sty)
Provides:       tex(truetex.def)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source98:       graphics.tar.xz
Source99:       graphics.doc.tar.xz

%description -n texlive-graphics
This is a collection of LaTeX packages for: producing colour
including graphics (eg PostScript) files rotation and scaling
of text in LaTeX documents. It comprises the packages color,
graphics, graphicx, trig, epsfig, keyval, and lscape.

%package -n texlive-graphics-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn53640
Release:        0
Summary:        Documentation for texlive-graphics
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphics-doc
This package includes the documentation for texlive-graphics

%post -n texlive-graphics
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphics 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphics
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphics-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphics/README.md
%{_texmfdistdir}/doc/latex/graphics/cat.eps
%{_texmfdistdir}/doc/latex/graphics/changes.txt
%{_texmfdistdir}/doc/latex/graphics/color.pdf
%{_texmfdistdir}/doc/latex/graphics/drivers.pdf
%{_texmfdistdir}/doc/latex/graphics/epsfig.pdf
%{_texmfdistdir}/doc/latex/graphics/graphics.pdf
%{_texmfdistdir}/doc/latex/graphics/graphicx.pdf
%{_texmfdistdir}/doc/latex/graphics/grfguide.pdf
%{_texmfdistdir}/doc/latex/graphics/grfguide.tex
%{_texmfdistdir}/doc/latex/graphics/keyval.pdf
%{_texmfdistdir}/doc/latex/graphics/lscape.pdf
%{_texmfdistdir}/doc/latex/graphics/rotating.pdf
%{_texmfdistdir}/doc/latex/graphics/rotex.pdf
%{_texmfdistdir}/doc/latex/graphics/rotex.tex
%{_texmfdistdir}/doc/latex/graphics/trig.pdf

%files -n texlive-graphics
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphics/color.sty
%{_texmfdistdir}/tex/latex/graphics/dvipdf.def
%{_texmfdistdir}/tex/latex/graphics/dvipsnam.def
%{_texmfdistdir}/tex/latex/graphics/dvipsone.def
%{_texmfdistdir}/tex/latex/graphics/dviwin.def
%{_texmfdistdir}/tex/latex/graphics/emtex.def
%{_texmfdistdir}/tex/latex/graphics/epsfig.sty
%{_texmfdistdir}/tex/latex/graphics/graphics-2017-06-25.sty
%{_texmfdistdir}/tex/latex/graphics/graphics.sty
%{_texmfdistdir}/tex/latex/graphics/graphicx.sty
%{_texmfdistdir}/tex/latex/graphics/keyval.sty
%{_texmfdistdir}/tex/latex/graphics/lscape.sty
%{_texmfdistdir}/tex/latex/graphics/pctex32.def
%{_texmfdistdir}/tex/latex/graphics/pctexhp.def
%{_texmfdistdir}/tex/latex/graphics/pctexps.def
%{_texmfdistdir}/tex/latex/graphics/pctexwin.def
%{_texmfdistdir}/tex/latex/graphics/rotating.sty
%{_texmfdistdir}/tex/latex/graphics/tcidvi.def
%{_texmfdistdir}/tex/latex/graphics/trig.sty
%{_texmfdistdir}/tex/latex/graphics/truetex.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphics-%{texlive_version}.%{texlive_noarch}.svn53640-%{release}-zypper
%endif

%package -n texlive-graphics-cfg
Version:        %{texlive_version}.%{texlive_noarch}.svn41448
Release:        0
Summary:        Sample configuration files for LaTeX color and graphics
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
Recommends:     texlive-graphics-cfg-doc >= %{texlive_version}
Provides:       tex(color.cfg)
Provides:       tex(graphics.cfg)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source100:      graphics-cfg.tar.xz
Source101:      graphics-cfg.doc.tar.xz

%description -n texlive-graphics-cfg
This bundle includes color.cfg and graphics.cfg files that set
default "driver" options for the color and graphics packages.
It contains support for defaulting the new LuaTeX option which
was added to graphics and color in the 2016-02-01 release. The
LuaTeX option is only used for LuaTeX versions from 0.87, older
versions use the pdfTeX option as before.

%package -n texlive-graphics-cfg-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn41448
Release:        0
Summary:        Documentation for texlive-graphics-cfg
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphics-cfg-doc
This package includes the documentation for texlive-graphics-cfg

%post -n texlive-graphics-cfg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphics-cfg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphics-cfg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphics-cfg-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphics-cfg/README.md

%files -n texlive-graphics-cfg
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphics-cfg/color.cfg
%{_texmfdistdir}/tex/latex/graphics-cfg/graphics.cfg
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphics-cfg-%{texlive_version}.%{texlive_noarch}.svn41448-%{release}-zypper
%endif

%package -n texlive-graphics-def
Version:        %{texlive_version}.%{texlive_noarch}.svn54522
Release:        0
Summary:        Colour and graphics option files
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
Recommends:     texlive-graphics-def-doc >= %{texlive_version}
Provides:       tex(dvipdfmx.def)
Provides:       tex(dvips.def)
Provides:       tex(dvisvgm.def)
Provides:       tex(luatex.def)
Provides:       tex(pdftex.def)
Provides:       tex(xetex.def)
Requires:       tex(epstopdf-base.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source102:      graphics-def.tar.xz
Source103:      graphics-def.doc.tar.xz

%description -n texlive-graphics-def
This bundle is a combined distribution consisting of dvips.def,
pdftex.def, luatex.def, xetex.def, dvipdfmx.def, and
dvisvgm.def driver option files for the LaTeX graphics and
color packages. It is hoped that by combining their source
repositories at https://github.com/latex3/graphics-def it will
be easier to coordinate updates.

%package -n texlive-graphics-def-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54522
Release:        0
Summary:        Documentation for texlive-graphics-def
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphics-def-doc
This package includes the documentation for texlive-graphics-def

%post -n texlive-graphics-def
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphics-def 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphics-def
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphics-def-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphics-def/CONTRIBUTING.md
%{_texmfdistdir}/doc/latex/graphics-def/README.md

%files -n texlive-graphics-def
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphics-def/dvipdfmx.def
%{_texmfdistdir}/tex/latex/graphics-def/dvips.def
%{_texmfdistdir}/tex/latex/graphics-def/dvisvgm.def
%{_texmfdistdir}/tex/latex/graphics-def/luatex.def
%{_texmfdistdir}/tex/latex/graphics-def/pdftex.def
%{_texmfdistdir}/tex/latex/graphics-def/xetex.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphics-def-%{texlive_version}.%{texlive_noarch}.svn54522-%{release}-zypper
%endif

%package -n texlive-graphics-pln
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        LaTeX-style graphics for Plain TeX users
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
Recommends:     texlive-graphics-pln-doc >= %{texlive_version}
Provides:       tex(autopict.sty)
Provides:       tex(color.tex)
Provides:       tex(graphicx.tex)
Provides:       tex(miniltx.tex)
Provides:       tex(picture.tex)
Provides:       tex(psfrag.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source104:      graphics-pln.tar.xz
Source105:      graphics-pln.doc.tar.xz

%description -n texlive-graphics-pln
The Plain TeX graphics package is mostly a thin shell around
the LaTeX graphicx and color packages, with support of the
LaTeX-isms in those packages provided by miniltx (which is the
largest part of the bundle). The bundle also contains a file
"picture.tex", which is a wrapper around the autopict.sty, and
provides the LaTeX picture mode to Plain TeX users.

%package -n texlive-graphics-pln-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54080
Release:        0
Summary:        Documentation for texlive-graphics-pln
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphics-pln-doc
This package includes the documentation for texlive-graphics-pln

%post -n texlive-graphics-pln
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphics-pln 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphics-pln
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphics-pln-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/graphics-pln/README.md
%{_texmfdistdir}/doc/plain/graphics-pln/exmplcol.tex
%{_texmfdistdir}/doc/plain/graphics-pln/exmplgrf.tex
%{_texmfdistdir}/doc/plain/graphics-pln/exmplpfg.tex
%{_texmfdistdir}/doc/plain/graphics-pln/exmplpic.tex

%files -n texlive-graphics-pln
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/graphics-pln/autopict.sty
%{_texmfdistdir}/tex/plain/graphics-pln/color.tex
%{_texmfdistdir}/tex/plain/graphics-pln/graphicx.tex
%{_texmfdistdir}/tex/plain/graphics-pln/miniltx.tex
%{_texmfdistdir}/tex/plain/graphics-pln/picture.tex
%{_texmfdistdir}/tex/plain/graphics-pln/psfrag.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphics-pln-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif

%package -n texlive-graphicx-psmin
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Reduce size of PostScript files by not repeating images
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
Recommends:     texlive-graphicx-psmin-doc >= %{texlive_version}
Provides:       tex(graphicx-psmin.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source106:      graphicx-psmin.tar.xz
Source107:      graphicx-psmin.doc.tar.xz

%description -n texlive-graphicx-psmin
The package is an extension of the standard latex-graphics
bundle and provides a way to include repeated PostScript
graphics (ps, eps) only once in a PostScript document. This
leads to smaller PostScript documents when having, for
instance, a logo on every page. The package only works when
post-processed with dvips, which should be version 5.95b or
later. The difference for a resulting distilled PDF file is
minimal (as Ghostscript and Adobe Distiller only include a
single copy of each graphics file, anyway).

%package -n texlive-graphicx-psmin-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Documentation for texlive-graphicx-psmin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphicx-psmin-doc
This package includes the documentation for texlive-graphicx-psmin

%post -n texlive-graphicx-psmin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphicx-psmin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphicx-psmin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphicx-psmin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphicx-psmin/README
%{_texmfdistdir}/doc/latex/graphicx-psmin/graphicx-psmin.pdf

%files -n texlive-graphicx-psmin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphicx-psmin/graphicx-psmin.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphicx-psmin-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif

%package -n texlive-graphicxbox
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn32630
Release:        0
Summary:        Insert a graphical image as a background
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
Recommends:     texlive-graphicxbox-doc >= %{texlive_version}
Provides:       tex(graphicxbox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source108:      graphicxbox.tar.xz
Source109:      graphicxbox.doc.tar.xz

%description -n texlive-graphicxbox
The package defines two new commands \graphicxbox and
\fgraphicxbox, which are companions to \colorbox and \fcolorbox
of the Standard LaTeX color package. The \graphicxbox command
inserts a graphical image as a background rather than a
background color, while \fgraphicxbox does the same thing, but
also draws a colored frame around the box.

%package -n texlive-graphicxbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn32630
Release:        0
Summary:        Documentation for texlive-graphicxbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphicxbox-doc
This package includes the documentation for texlive-graphicxbox

%post -n texlive-graphicxbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphicxbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphicxbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphicxbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphicxbox/README
%{_texmfdistdir}/doc/latex/graphicxbox/doc/graphicxbox.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/IndianBlanket.eps
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/IndianBlanket.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/Wood-Brown.eps
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/Wood-Brown.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/bg_cle_tile.eps
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/grandcanyon.eps
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/grandcanyon.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/news_bgr.eps
%{_texmfdistdir}/doc/latex/graphicxbox/examples/graphics/news_bgr.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst.tex
%{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_indians.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_indians.tex
%{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_sp.pdf
%{_texmfdistdir}/doc/latex/graphicxbox/examples/grfxbox_tst_sp.tex

%files -n texlive-graphicxbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphicxbox/graphicxbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphicxbox-%{texlive_version}.%{texlive_noarch}.1.0svn32630-%{release}-zypper
%endif

%package -n texlive-graphicxpsd
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46477
Release:        0
Summary:        Adobe Photoshop Data format (PSD) support for graphicx package
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
Recommends:     texlive-graphicxpsd-doc >= %{texlive_version}
Provides:       tex(graphicxpsd.sty)
Requires:       tex(shellesc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source110:      graphicxpsd.tar.xz
Source111:      graphicxpsd.doc.tar.xz

%description -n texlive-graphicxpsd
This package provides Adobe Photoshop Data format (PSD) support
for graphicx package with sips (Darwin/macOS) / convert
(ImageMagick) command.

%package -n texlive-graphicxpsd-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn46477
Release:        0
Summary:        Documentation for texlive-graphicxpsd
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphicxpsd-doc
This package includes the documentation for texlive-graphicxpsd

%post -n texlive-graphicxpsd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphicxpsd 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphicxpsd
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphicxpsd-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphicxpsd/LICENSE
%{_texmfdistdir}/doc/latex/graphicxpsd/README.md
%{_texmfdistdir}/doc/latex/graphicxpsd/graphicxpsd.pdf
%{_texmfdistdir}/doc/latex/graphicxpsd/graphicxpsd.tex
%{_texmfdistdir}/doc/latex/graphicxpsd/test-gin-rule-psd.tex
%{_texmfdistdir}/doc/latex/graphicxpsd/tigerpsdfmt.psd

%files -n texlive-graphicxpsd
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphicxpsd/graphicxpsd.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphicxpsd-%{texlive_version}.%{texlive_noarch}.1.1svn46477-%{release}-zypper
%endif

%package -n texlive-graphviz
Version:        %{texlive_version}.%{texlive_noarch}.0.0.94svn31517
Release:        0
Summary:        Write graphviz (dot+neato) inline in LaTeX documents
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
Recommends:     texlive-graphviz-doc >= %{texlive_version}
Provides:       tex(graphviz.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(psfrag.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source112:      graphviz.tar.xz
Source113:      graphviz.doc.tar.xz

%description -n texlive-graphviz
The package allows inline use of graphviz code, in a LaTeX
document.

%package -n texlive-graphviz-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.94svn31517
Release:        0
Summary:        Documentation for texlive-graphviz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-graphviz-doc
This package includes the documentation for texlive-graphviz

%post -n texlive-graphviz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-graphviz 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-graphviz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-graphviz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/graphviz/LICENSE
%{_texmfdistdir}/doc/latex/graphviz/Makefile
%{_texmfdistdir}/doc/latex/graphviz/README
%{_texmfdistdir}/doc/latex/graphviz/README.md
%{_texmfdistdir}/doc/latex/graphviz/graphviz.pdf
%{_texmfdistdir}/doc/latex/graphviz/test/Makefile
%{_texmfdistdir}/doc/latex/graphviz/test/body.tex
%{_texmfdistdir}/doc/latex/graphviz/test/pdf-singlefile-tmpdir.tex
%{_texmfdistdir}/doc/latex/graphviz/test/pdf-singlefile.tex
%{_texmfdistdir}/doc/latex/graphviz/test/pdf-tmpdir.tex
%{_texmfdistdir}/doc/latex/graphviz/test/pdf.tex
%{_texmfdistdir}/doc/latex/graphviz/test/ps.tex

%files -n texlive-graphviz
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/graphviz/graphviz.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-graphviz-%{texlive_version}.%{texlive_noarch}.0.0.94svn31517-%{release}-zypper
%endif

%package -n texlive-grayhints
Version:        %{texlive_version}.%{texlive_noarch}.svn49052
Release:        0
Summary:        Produce 'gray hints' to a variable text field
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
Recommends:     texlive-grayhints-doc >= %{texlive_version}
Provides:       tex(grayhints.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source114:      grayhints.tar.xz
Source115:      grayhints.doc.tar.xz

%description -n texlive-grayhints
The package provides JavaScript code snippets to create 'gray
hints'. Gray hints, as the author terms them, are text that
appears initially in a text field that gives a short hint as to
what the contents of the text field should be. For example, a
text field might contain the hint 'First Name', or a date field
might read 'yyyy/mm/dd'. As soon as the field comes into focus,
the hint disappears. It reappears when the field is blurred and
the user did not enter any text into the field. The package
works for dvips/Distiller, pdfLaTeX, LuaLaTeX, and XeLaTeX.

%package -n texlive-grayhints-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn49052
Release:        0
Summary:        Documentation for texlive-grayhints
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grayhints-doc
This package includes the documentation for texlive-grayhints

%post -n texlive-grayhints
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grayhints 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grayhints
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grayhints-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grayhints/README.md
%{_texmfdistdir}/doc/latex/grayhints/doc/grayhints.pdf
%{_texmfdistdir}/doc/latex/grayhints/doc/grayhints_man.pdf
%{_texmfdistdir}/doc/latex/grayhints/doc/grayhints_man.tex
%{_texmfdistdir}/doc/latex/grayhints/examples/gh-eforms.pdf
%{_texmfdistdir}/doc/latex/grayhints/examples/gh-eforms.tex
%{_texmfdistdir}/doc/latex/grayhints/examples/gh-fmts-eforms.tex
%{_texmfdistdir}/doc/latex/grayhints/examples/gh-fmts-hyperref.tex
%{_texmfdistdir}/doc/latex/grayhints/examples/gh-hyperref.tex

%files -n texlive-grayhints
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grayhints/grayhints.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grayhints-%{texlive_version}.%{texlive_noarch}.svn49052-%{release}-zypper
%endif

%package -n texlive-greek-fontenc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn53955
Release:        0
Summary:        LICR macros and encoding definition files for Greek
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
Recommends:     texlive-greek-fontenc-doc >= %{texlive_version}
Provides:       tex(alphabeta-lgr.def)
Provides:       tex(alphabeta-tuenc.def)
Provides:       tex(alphabeta.sty)
Provides:       tex(greek-euenc.def)
Provides:       tex(greek-fontenc.def)
Provides:       tex(lgrenc.def)
Provides:       tex(textalpha.sty)
Provides:       tex(tuenc-greek.def)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source116:      greek-fontenc.tar.xz
Source117:      greek-fontenc.doc.tar.xz

%description -n texlive-greek-fontenc
The package provides Greek LICR macro definitions and encoding
definition files for Greek text font encodings for use with
fontenc.

%package -n texlive-greek-fontenc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.14svn53955
Release:        0
Summary:        Documentation for texlive-greek-fontenc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-greek-fontenc-doc
This package includes the documentation for texlive-greek-fontenc

%post -n texlive-greek-fontenc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-greek-fontenc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-greek-fontenc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-greek-fontenc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/greek-fontenc/README
%{_texmfdistdir}/doc/latex/greek-fontenc/README.html
%{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-doc.pdf
%{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-doc.tex
%{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-lgr.def.html
%{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-tuenc.def.html
%{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-tuenc.html
%{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta.sty.html
%{_texmfdistdir}/doc/latex/greek-fontenc/diacritics.pdf
%{_texmfdistdir}/doc/latex/greek-fontenc/diacritics.tex
%{_texmfdistdir}/doc/latex/greek-fontenc/greek-fontenc.def.html
%{_texmfdistdir}/doc/latex/greek-fontenc/greekhyperref.pdf
%{_texmfdistdir}/doc/latex/greek-fontenc/greekhyperref.tex
%{_texmfdistdir}/doc/latex/greek-fontenc/lgr2licr.lua
%{_texmfdistdir}/doc/latex/greek-fontenc/lgr2licr.lua.html
%{_texmfdistdir}/doc/latex/greek-fontenc/lgrenc-test.pdf
%{_texmfdistdir}/doc/latex/greek-fontenc/lgrenc-test.tex
%{_texmfdistdir}/doc/latex/greek-fontenc/lgrenc.def.html
%{_texmfdistdir}/doc/latex/greek-fontenc/test-nameclashes.pdf
%{_texmfdistdir}/doc/latex/greek-fontenc/test-nameclashes.tex
%{_texmfdistdir}/doc/latex/greek-fontenc/textalpha-doc.pdf
%{_texmfdistdir}/doc/latex/greek-fontenc/textalpha-doc.tex
%{_texmfdistdir}/doc/latex/greek-fontenc/textalpha.sty.html
%{_texmfdistdir}/doc/latex/greek-fontenc/tuenc-greek-doc.pdf
%{_texmfdistdir}/doc/latex/greek-fontenc/tuenc-greek-doc.tex
%{_texmfdistdir}/doc/latex/greek-fontenc/tuenc-greek.def.html

%files -n texlive-greek-fontenc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/greek-fontenc/alphabeta-lgr.def
%{_texmfdistdir}/tex/latex/greek-fontenc/alphabeta-tuenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/alphabeta.sty
%{_texmfdistdir}/tex/latex/greek-fontenc/greek-euenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/greek-fontenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/lgrenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/textalpha.sty
%{_texmfdistdir}/tex/latex/greek-fontenc/tuenc-greek.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-greek-fontenc-%{texlive_version}.%{texlive_noarch}.0.0.14svn53955-%{release}-zypper
%endif

%package -n texlive-greek-inputenc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn51612
Release:        0
Summary:        Greek encoding support for inputenc
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
Recommends:     texlive-greek-inputenc-doc >= %{texlive_version}
Provides:       tex(iso-8859-7.def)
Provides:       tex(macgreek.def)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source118:      greek-inputenc.tar.xz
Source119:      greek-inputenc.doc.tar.xz

%description -n texlive-greek-inputenc
The bundle provides UTF-8, Macintosh Greek encoding and ISO
8859-7 definition files for use with inputenc.

%package -n texlive-greek-inputenc-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.7svn51612
Release:        0
Summary:        Documentation for texlive-greek-inputenc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-greek-inputenc-doc
This package includes the documentation for texlive-greek-inputenc

%post -n texlive-greek-inputenc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-greek-inputenc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-greek-inputenc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-greek-inputenc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/greek-inputenc/README
%{_texmfdistdir}/doc/latex/greek-inputenc/README.html
%{_texmfdistdir}/doc/latex/greek-inputenc/greek-utf8-minimal.pdf
%{_texmfdistdir}/doc/latex/greek-inputenc/greek-utf8-minimal.tex
%{_texmfdistdir}/doc/latex/greek-inputenc/greek-utf8.pdf
%{_texmfdistdir}/doc/latex/greek-inputenc/greek-utf8.tex
%{_texmfdistdir}/doc/latex/greek-inputenc/inputenc-iso-8859-7.pdf
%{_texmfdistdir}/doc/latex/greek-inputenc/inputenc-iso-8859-7.tex
%{_texmfdistdir}/doc/latex/greek-inputenc/lgrenc.dfu.html
%{_texmfdistdir}/doc/latex/greek-inputenc/unicode-licr.txt

%files -n texlive-greek-inputenc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/greek-inputenc/iso-8859-7.def
%{_texmfdistdir}/tex/latex/greek-inputenc/lgrenc.dfu
%{_texmfdistdir}/tex/latex/greek-inputenc/macgreek.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-greek-inputenc-%{texlive_version}.%{texlive_noarch}.1.7svn51612-%{release}-zypper
%endif

%package -n texlive-greekdates
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Provides ancient Greek day and month names, dates, etcetera
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
Recommends:     texlive-greekdates-doc >= %{texlive_version}
Provides:       tex(greekdates.sty)
Requires:       tex(calc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source120:      greekdates.tar.xz
Source121:      greekdates.doc.tar.xz

%description -n texlive-greekdates
The package provides easy access to ancient Greek names of days
and months of various regions of Greece. In case the historical
information about a region is not complete, we use the Athenian
name of the month. Moreover commands and options are provided,
in order to completely switch to the "ancient way", commands
such as \today.

%package -n texlive-greekdates-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-greekdates
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-greekdates-doc
This package includes the documentation for texlive-greekdates

%post -n texlive-greekdates
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-greekdates 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-greekdates
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-greekdates-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/greekdates/README
%{_texmfdistdir}/doc/latex/greekdates/greekdates.pdf

%files -n texlive-greekdates
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/greekdates/greekdates.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-greekdates-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-greektex
Version:        %{texlive_version}.%{texlive_noarch}.svn28327
Release:        0
Summary:        Fonts for typesetting Greek/English documents
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
Recommends:     texlive-greektex-doc >= %{texlive_version}
Provides:       tex(greektex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source122:      greektex.tar.xz
Source123:      greektex.doc.tar.xz

%description -n texlive-greektex
The fonts are based on Silvio Levy's classical Greek fonts;
macros and Greek hyphenation patterns for the fonts' encoding
are also provided.

%package -n texlive-greektex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn28327
Release:        0
Summary:        Documentation for texlive-greektex
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-greektex-doc:el)

%description -n texlive-greektex-doc
This package includes the documentation for texlive-greektex

%post -n texlive-greektex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-greektex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-greektex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-greektex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/greektex/README
%{_texmfdistdir}/doc/fonts/greektex/gehyphw.gr
%{_texmfdistdir}/doc/fonts/greektex/greektexdoc.pdf
%{_texmfdistdir}/doc/fonts/greektex/greektexdoc.tex
%{_texmfdistdir}/doc/fonts/greektex/ywcl.zip

%files -n texlive-greektex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/greektex/greektex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-greektex-%{texlive_version}.%{texlive_noarch}.svn28327-%{release}-zypper
%endif

%package -n texlive-greektonoi
Version:        %{texlive_version}.%{texlive_noarch}.svn39419
Release:        0
Summary:        Facilitates writing/editing of multiaccented greek
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
Recommends:     texlive-greektonoi-doc >= %{texlive_version}
Provides:       tex(greektonoi.map)
Provides:       tex(greektonoi.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source124:      greektonoi.tar.xz
Source125:      greektonoi.doc.tar.xz

%description -n texlive-greektonoi
The greektonoi mapping extends the betababel package or the
babel polutonikogreek option to provide a simple way to insert
ancient Greek texts with diacritical characters into your
document using a similar method to the commonly used Beta Code
transliteration, but with much more freedom. It is designed
especially for the XeTeX engine and it could also be used for
fast and easy modification of monotonic greek texts to
polytonic. The output text is natively encoded in Unicode, so
it can be reused in any possible way. The greektonoi package
provides, in addition to inserting greek accents and
breathings, many other symbols used in greek numbers and
arithmetic or in the greek archaic period. It could be used
with greektonoi mapping or indepedently.

%package -n texlive-greektonoi-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn39419
Release:        0
Summary:        Documentation for texlive-greektonoi
License:        LGPL-2.1-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-greektonoi-doc:el)

%description -n texlive-greektonoi-doc
This package includes the documentation for texlive-greektonoi

%post -n texlive-greektonoi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-greektonoi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-greektonoi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-greektonoi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/greektonoi/README.txt
%{_texmfdistdir}/doc/latex/greektonoi/greektonoi-en.pdf
%{_texmfdistdir}/doc/latex/greektonoi/greektonoi-en.tex
%{_texmfdistdir}/doc/latex/greektonoi/greektonoi.pdf
%{_texmfdistdir}/doc/latex/greektonoi/greektonoi.tex

%files -n texlive-greektonoi
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/greektonoi/greektonoi.map
%{_texmfdistdir}/fonts/map/dvips/greektonoi/greektonoi.tec
%{_texmfdistdir}/tex/latex/greektonoi/greektonoi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-greektonoi-%{texlive_version}.%{texlive_noarch}.svn39419-%{release}-zypper
%endif

%package -n texlive-greenpoint
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        The Green Point logo
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
Recommends:     texlive-greenpoint-doc >= %{texlive_version}
Provides:       tex(greenpoint.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source126:      greenpoint.tar.xz
Source127:      greenpoint.doc.tar.xz

%description -n texlive-greenpoint
A Metafont-implementation of the logo commonly known as 'Der
Grune Punkt' ('The Green Point'). In Austria, it can be found
on nearly every bottle. It should not be confused with the
'Recycle'-logo, implemented by Ian Green.

%package -n texlive-greenpoint-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-greenpoint
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-greenpoint-doc
This package includes the documentation for texlive-greenpoint

%post -n texlive-greenpoint
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-greenpoint 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-greenpoint
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-greenpoint-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/greenpoint/ChangeLog
%{_texmfdistdir}/doc/fonts/greenpoint/README

%files -n texlive-greenpoint
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/greenpoint/greenpoint.mf
%{_texmfdistdir}/fonts/tfm/public/greenpoint/greenpoint.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-greenpoint-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-gregoriotex
Version:        %{texlive_version}.%{texlive_noarch}.5.2.1svn51029
Release:        0
Summary:        Engraving Gregorian Chant scores
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-gregoriotex-bin >= %{texlive_version}
#!BuildIgnore: texlive-gregoriotex-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-gregoriotex-fonts >= %{texlive_version}
Recommends:     texlive-gregoriotex-doc >= %{texlive_version}
Provides:       tex(gregorio-vowels.dat)
Provides:       tex(gregoriosyms.sty)
Provides:       tex(gregoriotex-chars.tex)
Provides:       tex(gregoriotex-common.tex)
Provides:       tex(gregoriotex-main.tex)
Provides:       tex(gregoriotex-nabc.tex)
Provides:       tex(gregoriotex-signs.tex)
Provides:       tex(gregoriotex-spaces.tex)
Provides:       tex(gregoriotex-syllable.tex)
Provides:       tex(gregoriotex-symbols.tex)
Provides:       tex(gregoriotex.sty)
Provides:       tex(gregoriotex.tex)
Provides:       tex(gsp-default.tex)
Requires:       tex(graphicx.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(luamplib.sty)
Requires:       tex(luaotfload.sty)
Requires:       tex(luatexbase.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source128:      gregoriotex.tar.xz
Source129:      gregoriotex.doc.tar.xz

%description -n texlive-gregoriotex
Gregorio is a software application for engraving Gregorian
Chant scores on a computer. Gregorio's main job is to convert a
gabc file (simple text representation of a score) into a
GregorioTeX file, which makes TeX able to create a PDF of your
score.

%package -n texlive-gregoriotex-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.2.1svn51029
Release:        0
Summary:        Documentation for texlive-gregoriotex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gregoriotex-doc
This package includes the documentation for texlive-gregoriotex


%package -n texlive-gregoriotex-fonts
Version:        %{texlive_version}.%{texlive_noarch}.5.2.1svn51029
Release:        0
Summary:        Severed fonts for texlive-gregoriotex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-gregoriotex-fonts
The  separated fonts package for texlive-gregoriotex
%post -n texlive-gregoriotex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gregoriotex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gregoriotex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-gregoriotex-fonts
%files -n texlive-gregoriotex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/gregoriotex/Appendix_Font_Tables.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/Command_Index_User.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/Command_Index_gregorio.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/Command_Index_internal.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/Gabc.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/GregorioNabcRef.pdf
%{_texmfdistdir}/doc/luatex/gregoriotex/GregorioNabcRef.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/GregorioRef.lua
%{_texmfdistdir}/doc/luatex/gregoriotex/GregorioRef.pdf
%{_texmfdistdir}/doc/luatex/gregoriotex/GregorioRef.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/doc_README.md
%{_texmfdistdir}/doc/luatex/gregoriotex/examples/FactusEst.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/examples/PopulusSion.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/examples/debugging.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/examples/main-lualatex.tex
%{_texmfdistdir}/doc/luatex/gregoriotex/factus.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/omnes.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/pitches2.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/pitches3.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/pitches4.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/pitches5.gabc
%{_texmfdistdir}/doc/luatex/gregoriotex/veni.gabc

%files -n texlive-gregoriotex
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/gregoriotex/convertsfdtottf.py
%{_texmfdistdir}/fonts/source/gregoriotex/fonts_README.md
%{_texmfdistdir}/fonts/source/gregoriotex/greciliae-base.sfd
%{_texmfdistdir}/fonts/source/gregoriotex/greextra.sfd
%{_texmfdistdir}/fonts/source/gregoriotex/gregall.sfd
%{_texmfdistdir}/fonts/source/gregoriotex/gresgmodern.sfd
%{_texmfdistdir}/fonts/source/gregoriotex/squarize.py
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/greciliae-hole.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/greciliae-hollow.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/greciliae-op-hole.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/greciliae-op-hollow.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/greciliae-op.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/greciliae.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/greextra.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/gregall.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/grelaon.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/gregoriotex/gresgmodern.ttf
%{_texmfdistdir}/scripts/gregoriotex/uninstall-gtex.sh
%{_texmfdistdir}/tex/lualatex/gregoriotex/gregoriosyms.sty
%{_texmfdistdir}/tex/lualatex/gregoriotex/gregoriotex.sty
%{_texmfdistdir}/tex/luatex/gregoriotex/gregorio-vowels.dat
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-chars.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-common.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-main.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-nabc.lua
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-nabc.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-signs.lua
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-signs.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-spaces.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-syllable.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-symbols.lua
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex-symbols.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex.lua
%{_texmfdistdir}/tex/luatex/gregoriotex/gregoriotex.tex
%{_texmfdistdir}/tex/luatex/gregoriotex/gsp-default.tex

%files -n texlive-gregoriotex-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-gregoriotex
%{_datadir}/fontconfig/conf.avail/58-texlive-gregoriotex.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gregoriotex/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gregoriotex/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-gregoriotex/fonts.scale
%{_datadir}/fonts/texlive-gregoriotex/greciliae-hole.ttf
%{_datadir}/fonts/texlive-gregoriotex/greciliae-hollow.ttf
%{_datadir}/fonts/texlive-gregoriotex/greciliae-op-hole.ttf
%{_datadir}/fonts/texlive-gregoriotex/greciliae-op-hollow.ttf
%{_datadir}/fonts/texlive-gregoriotex/greciliae-op.ttf
%{_datadir}/fonts/texlive-gregoriotex/greciliae.ttf
%{_datadir}/fonts/texlive-gregoriotex/greextra.ttf
%{_datadir}/fonts/texlive-gregoriotex/gregall.ttf
%{_datadir}/fonts/texlive-gregoriotex/grelaon.ttf
%{_datadir}/fonts/texlive-gregoriotex/gresgmodern.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gregoriotex-fonts-%{texlive_version}.%{texlive_noarch}.5.2.1svn51029-%{release}-zypper
%endif

%package -n texlive-grfext
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53024
Release:        0
Summary:        Manipulate the graphics package's list of extensions
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
Recommends:     texlive-grfext-doc >= %{texlive_version}
Provides:       tex(grfext.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(kvdefinekeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source130:      grfext.tar.xz
Source131:      grfext.doc.tar.xz

%description -n texlive-grfext
This package provides macros for adding to, and reordering the
list of graphics file extensions recognised by package
graphics.

%package -n texlive-grfext-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn53024
Release:        0
Summary:        Documentation for texlive-grfext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grfext-doc
This package includes the documentation for texlive-grfext

%post -n texlive-grfext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grfext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grfext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grfext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grfext/README.md
%{_texmfdistdir}/doc/latex/grfext/grfext.pdf

%files -n texlive-grfext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grfext/grfext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grfext-%{texlive_version}.%{texlive_noarch}.1.3svn53024-%{release}-zypper
%endif

%package -n texlive-grffile
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn52756
Release:        0
Summary:        Extended file name support for graphics (legacy package)
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
Recommends:     texlive-grffile-doc >= %{texlive_version}
Provides:       tex(grffile-2017-06-30.sty)
Provides:       tex(grffile.sty)
Requires:       tex(graphics.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(stringenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source132:      grffile.tar.xz
Source133:      grffile.doc.tar.xz

%description -n texlive-grffile
The original package extended the file name processing of
package graphics to support a larger range of file names. The
base LaTeX code now supports multiple dots and spaces, and this
package by default is a stub that just loads graphicx. However,
\usepackage{grffile}[=v1] may be used to access version 1(.18)
of the package if that is needed.

%package -n texlive-grffile-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn52756
Release:        0
Summary:        Documentation for texlive-grffile
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grffile-doc
This package includes the documentation for texlive-grffile

%post -n texlive-grffile
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grffile 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grffile
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grffile-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grffile/README.md
%{_texmfdistdir}/doc/latex/grffile/grffile.pdf

%files -n texlive-grffile
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grffile/grffile-2017-06-30.sty
%{_texmfdistdir}/tex/latex/grffile/grffile.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grffile-%{texlive_version}.%{texlive_noarch}.2.1svn52756-%{release}-zypper
%endif

%package -n texlive-grfpaste
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn17354
Release:        0
Summary:        Include fragments of a dvi file
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
Recommends:     texlive-grfpaste-doc >= %{texlive_version}
Provides:       tex(grfpaste.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source134:      grfpaste.tar.xz
Source135:      grfpaste.doc.tar.xz

%description -n texlive-grfpaste
Provides a mechanism to include fragments of dvi files with the
graphicx package, so that you can use \includegraphics to
include dvi files. The package requires the dvipaste program.

%package -n texlive-grfpaste-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn17354
Release:        0
Summary:        Documentation for texlive-grfpaste
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grfpaste-doc
This package includes the documentation for texlive-grfpaste

%post -n texlive-grfpaste
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grfpaste 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grfpaste
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grfpaste-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grfpaste/doc/grfpaste.pdf
%{_texmfdistdir}/doc/latex/grfpaste/doc/grfpaste.tex
%{_texmfdistdir}/doc/latex/grfpaste/dvipaste.txt
%{_texmfdistdir}/doc/latex/grfpaste/grfp1.tex
%{_texmfdistdir}/doc/latex/grfpaste/grfp2.tex
%{_texmfdistdir}/doc/latex/grfpaste/grfp3.tex

%files -n texlive-grfpaste
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grfpaste/grfpaste.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grfpaste-%{texlive_version}.%{texlive_noarch}.0.0.2svn17354-%{release}-zypper
%endif

%package -n texlive-grid
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Grid typesetting in LaTeX
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
Recommends:     texlive-grid-doc >= %{texlive_version}
Provides:       tex(grid.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source136:      grid.tar.xz
Source137:      grid.doc.tar.xz

%description -n texlive-grid
The package helps to enables grid typesetting in double column
documents. Grid typesetting (vertical aligning of lines of text
in adjacent columns) is a difficult task in LaTeX, and the
present package is no more than an attempt to help users to
achieve it in a limited way. An example document, grid.tex, is
provided with simple instructions to typeset it using the
package. The package needs a lot more work: this is only a
beginning...

%package -n texlive-grid-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-grid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grid-doc
This package includes the documentation for texlive-grid

%post -n texlive-grid
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grid 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grid
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grid-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grid/README
%{_texmfdistdir}/doc/latex/grid/grid.pdf
%{_texmfdistdir}/doc/latex/grid/grid.tex
%{_texmfdistdir}/doc/latex/grid/manifest.txt
%{_texmfdistdir}/doc/latex/grid/rvdtx.sty

%files -n texlive-grid
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grid/grid.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grid-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-grid-system
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn32981
Release:        0
Summary:        Page organisation, modelled on CSS facilities
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-grid-system-doc >= %{texlive_version}
Provides:       tex(grid-system.sty)
Requires:       tex(calc.sty)
Requires:       tex(environ.sty)
Requires:       tex(forloop.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source138:      grid-system.tar.xz
Source139:      grid-system.doc.tar.xz

%description -n texlive-grid-system
The package provides the means for LaTeX to implement a grid
system as known from CSS grid systems. The facility is useful
for creating box layouts as used in brochures.

%package -n texlive-grid-system-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.0svn32981
Release:        0
Summary:        Documentation for texlive-grid-system
License:        Apache-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grid-system-doc
This package includes the documentation for texlive-grid-system

%post -n texlive-grid-system
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grid-system 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grid-system
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grid-system-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grid-system/LICENSE
%{_texmfdistdir}/doc/latex/grid-system/README
%{_texmfdistdir}/doc/latex/grid-system/grid-system.pdf
%{_texmfdistdir}/doc/latex/grid-system/grid-system.tex

%files -n texlive-grid-system
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grid-system/grid-system.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grid-system-%{texlive_version}.%{texlive_noarch}.0.0.3.0svn32981-%{release}-zypper
%endif

%package -n texlive-gridset
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn53762
Release:        0
Summary:        Grid, a.k.a. in-register, setting
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
Recommends:     texlive-gridset-doc >= %{texlive_version}
Provides:       tex(gridset.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source140:      gridset.tar.xz
Source141:      gridset.doc.tar.xz

%description -n texlive-gridset
Grid setting -- also known as strict in-register setting -- is
something, that should be done for a lot of documents but is
not easy using LaTeX. The package helps to get the information
needed for grid setting. It does not implement auto grid
setting, but there is a command \vskipnextgrid, that moves to
the next grid position. This may be enough under some
circumstances, but in other circumstances it may fail. Thus
gridset is only one more step for grid setting, not a complete
solution.

%package -n texlive-gridset-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn53762
Release:        0
Summary:        Documentation for texlive-gridset
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gridset-doc
This package includes the documentation for texlive-gridset

%post -n texlive-gridset
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gridset 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gridset
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gridset-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gridset/LICENSE.md
%{_texmfdistdir}/doc/latex/gridset/README.md
%{_texmfdistdir}/doc/latex/gridset/gridset.pdf

%files -n texlive-gridset
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gridset/gridset.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gridset-%{texlive_version}.%{texlive_noarch}.0.0.3svn53762-%{release}-zypper
%endif

%package -n texlive-gridslides
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn54512
Release:        0
Summary:        Free form slides with blocks placed on a grid
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
Recommends:     texlive-gridslides-doc >= %{texlive_version}
Provides:       tex(gridslides.cls)
Provides:       tex(gridslides.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(braket.sty)
Requires:       tex(dsfont.sty)
Requires:       tex(enumerate.sty)
Requires:       tex(environ.sty)
Requires:       tex(geometry.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(microtype.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source142:      gridslides.tar.xz
Source143:      gridslides.doc.tar.xz

%description -n texlive-gridslides
This package allows creating free form slides with blocks
placed on a grid. The blocks can be filled with text,
equations, figures etc. The resulting slides are similar to the
ones produced with LaTeX beamer, but more flexible. Sequential
unconvering of elements is supported. A compiler script is
provided which compiles each slide separately, this way
avoiding long compile times.

%package -n texlive-gridslides-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn54512
Release:        0
Summary:        Documentation for texlive-gridslides
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gridslides-doc
This package includes the documentation for texlive-gridslides

%post -n texlive-gridslides
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gridslides 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gridslides
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gridslides-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gridslides/Makefile
%{_texmfdistdir}/doc/latex/gridslides/README.md
%{_texmfdistdir}/doc/latex/gridslides/compile.pl
%{_texmfdistdir}/doc/latex/gridslides/example.pdf
%{_texmfdistdir}/doc/latex/gridslides/example.tex
%{_texmfdistdir}/doc/latex/gridslides/figures/band02.png
%{_texmfdistdir}/doc/latex/gridslides/figures/band08.png
%{_texmfdistdir}/doc/latex/gridslides/figures/cnontrivial.pdf
%{_texmfdistdir}/doc/latex/gridslides/figures/ctrivial.pdf
%{_texmfdistdir}/doc/latex/gridslides/figures/qahe.pdf
%{_texmfdistdir}/doc/latex/gridslides/figures/qshe.pdf
%{_texmfdistdir}/doc/latex/gridslides/figures/skyrmion.pdf
%{_texmfdistdir}/doc/latex/gridslides/figures/trivial.pdf
%{_texmfdistdir}/doc/latex/gridslides/gridslides.pdf

%files -n texlive-gridslides
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gridslides/gridslides.cls
%{_texmfdistdir}/tex/latex/gridslides/gridslides.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gridslides-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn54512-%{release}-zypper
%endif

%package -n texlive-grotesq
Version:        %{texlive_version}.%{texlive_noarch}.svn35859
Release:        0
Summary:        URW Grotesq font pack for LaTeX
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
Requires:       texlive-grotesq-fonts >= %{texlive_version}
Recommends:     texlive-grotesq-doc >= %{texlive_version}
Provides:       tex(ot1ugq.fd)
Provides:       tex(t1ugq.fd)
Provides:       tex(ts1ugq.fd)
Provides:       tex(ugq.map)
Provides:       tex(ugqb7t.tfm)
Provides:       tex(ugqb7t.vf)
Provides:       tex(ugqb8a.tfm)
Provides:       tex(ugqb8c.tfm)
Provides:       tex(ugqb8c.vf)
Provides:       tex(ugqb8r.tfm)
Provides:       tex(ugqb8t.tfm)
Provides:       tex(ugqb8t.vf)
Provides:       tex(ugqbo7t.tfm)
Provides:       tex(ugqbo7t.vf)
Provides:       tex(ugqbo8c.tfm)
Provides:       tex(ugqbo8c.vf)
Provides:       tex(ugqbo8r.tfm)
Provides:       tex(ugqbo8t.tfm)
Provides:       tex(ugqbo8t.vf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source144:      grotesq.tar.xz
Source145:      grotesq.doc.tar.xz

%description -n texlive-grotesq
The directory contains a copy of the Type 1 font "URW Grotesq
2031 Bold' released under the GPL by URW, with supporting files
for use with (La)TeX.

%package -n texlive-grotesq-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn35859
Release:        0
Summary:        Documentation for texlive-grotesq
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grotesq-doc
This package includes the documentation for texlive-grotesq


%package -n texlive-grotesq-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn35859
Release:        0
Summary:        Severed fonts for texlive-grotesq
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-grotesq-fonts
The  separated fonts package for texlive-grotesq
%post -n texlive-grotesq
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap ugq.map' >> /var/run/texlive/run-updmap

%postun -n texlive-grotesq 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap ugq.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-grotesq
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-grotesq-fonts
%files -n texlive-grotesq-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/grotesq/grotesq.txt
%{_texmfdistdir}/doc/fonts/grotesq/readme.grotesq
%{_texmfdistdir}/doc/fonts/grotesq/ugq.txt

%files -n texlive-grotesq
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/urw/grotesq/ugqb8a.afm
%{_texmfdistdir}/fonts/afm/urw/grotesq/ugqb8a.afm.org
%{_texmfdistdir}/fonts/map/dvips/grotesq/ugq.map
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8a.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo8t.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/grotesq/ugqb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/grotesq/ugqb8a.pfm
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqb7t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqb8c.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqb8t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbo7t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbo8c.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbo8t.vf
%{_texmfdistdir}/tex/latex/grotesq/ot1ugq.fd
%{_texmfdistdir}/tex/latex/grotesq/t1ugq.fd
%{_texmfdistdir}/tex/latex/grotesq/ts1ugq.fd

%files -n texlive-grotesq-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-grotesq
%{_datadir}/fontconfig/conf.avail/58-texlive-grotesq.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-grotesq/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-grotesq/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-grotesq/fonts.scale
%{_datadir}/fonts/texlive-grotesq/ugqb8a.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grotesq-fonts-%{texlive_version}.%{texlive_noarch}.svn35859-%{release}-zypper
%endif

%package -n texlive-grundgesetze
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn34439
Release:        0
Summary:        Typeset Frege's Grundgesetze der Arithmetik
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
Recommends:     texlive-grundgesetze-doc >= %{texlive_version}
Provides:       tex(grundgesetze.sty)
Requires:       tex(bguq.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source146:      grundgesetze.tar.xz
Source147:      grundgesetze.doc.tar.xz

%description -n texlive-grundgesetze
The package defines maths mode commands for typesetting Gottlob
Frege's concept-script in the style of his "Grundgesetze der
Arithmetik" (Basic Laws of Arithmetic).

%package -n texlive-grundgesetze-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn34439
Release:        0
Summary:        Documentation for texlive-grundgesetze
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-grundgesetze-doc
This package includes the documentation for texlive-grundgesetze

%post -n texlive-grundgesetze
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-grundgesetze 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-grundgesetze
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-grundgesetze-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/grundgesetze/README
%{_texmfdistdir}/doc/latex/grundgesetze/grundgesetze.pdf

%files -n texlive-grundgesetze
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/grundgesetze/grundgesetze.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-grundgesetze-%{texlive_version}.%{texlive_noarch}.1.02svn34439-%{release}-zypper
%endif

%package -n texlive-gsemthesis
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.4svn36244
Release:        0
Summary:        Geneva School of Economics and Management PhD thesis format
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
Recommends:     texlive-gsemthesis-doc >= %{texlive_version}
Provides:       tex(gsemthesis.cls)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(babel.sty)
Requires:       tex(book.cls)
Requires:       tex(csquotes.sty)
Requires:       tex(datetime.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(setspace.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source148:      gsemthesis.tar.xz
Source149:      gsemthesis.doc.tar.xz

%description -n texlive-gsemthesis
The class provides a PhD thesis template for the Geneva School
of Economics and Management (GSEM), University of Geneva,
Switzerland. The class provides utilities to easily set up the
cover page, the front matter pages, the page headers, etc.,
conformant to the official guidelines of the GSEM Faculty for
writing PhD dissertations.

%package -n texlive-gsemthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.4svn36244
Release:        0
Summary:        Documentation for texlive-gsemthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gsemthesis-doc
This package includes the documentation for texlive-gsemthesis

%post -n texlive-gsemthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gsemthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gsemthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gsemthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gsemthesis/README
%{_texmfdistdir}/doc/latex/gsemthesis/gsemthesis.pdf

%files -n texlive-gsemthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gsemthesis/gsemthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gsemthesis-%{texlive_version}.%{texlive_noarch}.0.0.9.4svn36244-%{release}-zypper
%endif

%package -n texlive-gsftopk
Version:        %{texlive_version}.%{texlive_noarch}.1.19.2svn52851
Release:        0
Summary:        Convert "Ghostscript fonts" to PK files
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-gsftopk-bin >= %{texlive_version}
#!BuildIgnore: texlive-gsftopk-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-gsftopk-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source150:      gsftopk.tar.xz
Source151:      gsftopk.doc.tar.xz

%description -n texlive-gsftopk
Designed for use with xdvi and dvips this utility converts
Adobe Type 1 fonts to PK bitmap format. It should not
ordinarily be much used nowadays, since both its target
applications are now capable of dealing with Type 1 fonts,
direct.

%package -n texlive-gsftopk-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.19.2svn52851
Release:        0
Summary:        Documentation for texlive-gsftopk
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(gsftopk.1)

%description -n texlive-gsftopk-doc
This package includes the documentation for texlive-gsftopk

%post -n texlive-gsftopk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gsftopk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gsftopk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gsftopk-doc
%defattr(-,root,root,755)
%{_mandir}/man1/gsftopk.1*

%files -n texlive-gsftopk
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/gsftopk/render.ps
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gsftopk-%{texlive_version}.%{texlive_noarch}.1.19.2svn52851-%{release}-zypper
%endif

%package -n texlive-gtl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn49527
Release:        0
Summary:        Manipulating generalized token lists
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
Recommends:     texlive-gtl-doc >= %{texlive_version}
Provides:       tex(gtl.sty)
Requires:       tex(expl3-generic.tex)
Requires:       tex(expl3.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source152:      gtl.tar.xz
Source153:      gtl.doc.tar.xz

%description -n texlive-gtl
The package provides tools for simple operations on lists of
tokens which are not necessarily balanced. It is in particular
used a lot in the unravel package, to go through tokens one at
a time rather than having to work with entire braced groups at
a time. The package requires up-to-date versions of the
l3kernel, l3kpackages, and l3experimental bundles.

%package -n texlive-gtl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn49527
Release:        0
Summary:        Documentation for texlive-gtl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gtl-doc
This package includes the documentation for texlive-gtl

%post -n texlive-gtl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gtl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gtl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gtl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/gtl/README.md
%{_texmfdistdir}/doc/generic/gtl/gtl.pdf

%files -n texlive-gtl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/gtl/gtl.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gtl-%{texlive_version}.%{texlive_noarch}.0.0.5svn49527-%{release}-zypper
%endif

%package -n texlive-gtrcrd
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32484
Release:        0
Summary:        Add chords to lyrics
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
Recommends:     texlive-gtrcrd-doc >= %{texlive_version}
Provides:       tex(gtrcrd.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source154:      gtrcrd.tar.xz
Source155:      gtrcrd.doc.tar.xz

%description -n texlive-gtrcrd
The package provides the means to specify guitar chords to be
played with each part of the lyrics of a song. The syntax of
the macros reduces the chance of failing to provide a chord
where one is needed, and the structure of the macros ensures
that the chord specification appears immediately above the
start of the lyric.

%package -n texlive-gtrcrd-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32484
Release:        0
Summary:        Documentation for texlive-gtrcrd
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gtrcrd-doc
This package includes the documentation for texlive-gtrcrd

%post -n texlive-gtrcrd
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gtrcrd 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gtrcrd
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gtrcrd-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gtrcrd/README
%{_texmfdistdir}/doc/latex/gtrcrd/gtrcrd-doc.pdf
%{_texmfdistdir}/doc/latex/gtrcrd/gtrcrd-doc.tex

%files -n texlive-gtrcrd
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gtrcrd/gtrcrd.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gtrcrd-%{texlive_version}.%{texlive_noarch}.1.1svn32484-%{release}-zypper
%endif

%package -n texlive-gtrlib-largetrees
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn49062
Release:        0
Summary:        Library for genealogytree aiming at large trees
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
Recommends:     texlive-gtrlib-largetrees-doc >= %{texlive_version}
Provides:       tex(gtrlib.largetrees.code.tex)
Provides:       tex(gtrlib.largetrees.sty)
Requires:       tex(genealogytree.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source156:      gtrlib-largetrees.tar.xz
Source157:      gtrlib-largetrees.doc.tar.xz

%description -n texlive-gtrlib-largetrees
The main goal of this package is to offer additional database
fields and formats for the genealogytree package, particularly
for typesetting large trees. The package depends on
genealogytree and etoolbox.

%package -n texlive-gtrlib-largetrees-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn49062
Release:        0
Summary:        Documentation for texlive-gtrlib-largetrees
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gtrlib-largetrees-doc
This package includes the documentation for texlive-gtrlib-largetrees

%post -n texlive-gtrlib-largetrees
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gtrlib-largetrees 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gtrlib-largetrees
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gtrlib-largetrees-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gtrlib-largetrees/README.md
%{_texmfdistdir}/doc/latex/gtrlib-largetrees/gtrlib.largetrees.pdf

%files -n texlive-gtrlib-largetrees
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gtrlib-largetrees/gtrlib.largetrees.code.tex
%{_texmfdistdir}/tex/latex/gtrlib-largetrees/gtrlib.largetrees.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gtrlib-largetrees-%{texlive_version}.%{texlive_noarch}.1.2bsvn49062-%{release}-zypper
%endif

%package -n texlive-gu
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Typeset crystallographic group-subgroup-schemes
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
Recommends:     texlive-gu-doc >= %{texlive_version}
Provides:       tex(gu.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pict2e.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source158:      gu.tar.xz
Source159:      gu.doc.tar.xz

%description -n texlive-gu
The package simplifies typesetting of simple crystallographic
group-subgroup-schemes in the Barnighausen formalism. It
defines a new environment stammbaum, wherein all elements of
the scheme are defined. Afterwards all necessary dimensions are
calculated and the scheme is drawn. Currently two steps of
symmetry reduction are supported.

%package -n texlive-gu-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-gu
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-gu-doc:de)

%description -n texlive-gu-doc
This package includes the documentation for texlive-gu

%post -n texlive-gu
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gu 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gu
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gu-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gu/README
%{_texmfdistdir}/doc/latex/gu/gudemo.tex
%{_texmfdistdir}/doc/latex/gu/gudoc.pdf
%{_texmfdistdir}/doc/latex/gu/gudoc.tex

%files -n texlive-gu
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gu/gu.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gu-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-guide-to-latex
Version:        %{texlive_version}.%{texlive_noarch}.svn45712
Release:        0
Summary:        Examples and more from Guide to LaTeX, by Kopka and Daly
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
Source160:      guide-to-latex.doc.tar.xz

%description -n texlive-guide-to-latex
The guide-to-latex package
%post -n texlive-guide-to-latex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-guide-to-latex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-guide-to-latex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-guide-to-latex
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/guide-to-latex/README.txt
%{_texmfdistdir}/doc/latex/guide-to-latex/demo.eps
%{_texmfdistdir}/doc/latex/guide-to-latex/demo.pdf
%{_texmfdistdir}/doc/latex/guide-to-latex/demodoc.pdf
%{_texmfdistdir}/doc/latex/guide-to-latex/demodoc.ps
%{_texmfdistdir}/doc/latex/guide-to-latex/demodoc.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-10.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-4.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-5.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-6.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-7.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-8.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap10/exer10-9.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-4.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer11-5.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap11/exer3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-4.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-5.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-6.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap15/exer15-7.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-3a.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-3b.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap2/exer2-3c.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-10.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-11.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-12.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-12.toc
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-1a.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-1b.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-4a.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-4b.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-5a.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-5b.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-6.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-7a.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-7b.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-8a.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-8b.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap3/exer3-9.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-10.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-4.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-5.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-6.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-7.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-8.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap4/exer4-9.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap5/exer5-4.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-4.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap6/exer6-5.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-10.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-11.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-12.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-13.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-14.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-15.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-16.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-17.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-18.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-19.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-20.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-21a.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-21b.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-4.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-5.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-6.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-7.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-8.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap7/exer7-9.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap8/exer8-1.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap8/exer8-2.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/exercises/chap8/exer8-3.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/mpletter.cls
%{_texmfdistdir}/doc/latex/guide-to-latex/palette.pdf
%{_texmfdistdir}/doc/latex/guide-to-latex/palette.ps
%{_texmfdistdir}/doc/latex/guide-to-latex/palette.tex
%{_texmfdistdir}/doc/latex/guide-to-latex/seminar.con
%{_texmfdistdir}/doc/latex/guide-to-latex/sempdftx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-guide-to-latex-%{texlive_version}.%{texlive_noarch}.svn45712-%{release}-zypper
%endif

%package -n texlive-guitar
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn32258
Release:        0
Summary:        Guitar chords and song texts
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
Recommends:     texlive-guitar-doc >= %{texlive_version}
Provides:       tex(guitar.sty)
Requires:       tex(toolbox.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source161:      guitar.tar.xz
Source162:      guitar.doc.tar.xz

%description -n texlive-guitar
(La)TeX macros for typesetting guitar chords over song texts.
The toolbox package is required. Note that this package only
places arbitrary TeX code over the lyrics. To typeset the
chords graphically (and not only by name), the author
recommends use of an additional package such as gchords by K.
Peeters.

%package -n texlive-guitar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn32258
Release:        0
Summary:        Documentation for texlive-guitar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-guitar-doc
This package includes the documentation for texlive-guitar

%post -n texlive-guitar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-guitar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-guitar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-guitar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/guitar/README
%{_texmfdistdir}/doc/latex/guitar/guitar.pdf
%{_texmfdistdir}/doc/latex/guitar/guitar.tex
%{_texmfdistdir}/doc/latex/guitar/guitar.txt

%files -n texlive-guitar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/guitar/guitar.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-guitar-%{texlive_version}.%{texlive_noarch}.1.6svn32258-%{release}-zypper
%endif

%package -n texlive-guitarchordschemes
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn54512
Release:        0
Summary:        Guitar Chord and Scale Tablatures
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
Recommends:     texlive-guitarchordschemes-doc >= %{texlive_version}
Provides:       tex(guitarchordschemes.sty)
Requires:       tex(cnltx-base.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source163:      guitarchordschemes.tar.xz
Source164:      guitarchordschemes.doc.tar.xz

%description -n texlive-guitarchordschemes
This package provides two commands (\chordscheme and \scales).
With those commands it is possible to draw schematic diagrams
of guitar chord tablatures and scale tablatures. Both commands
know a range of options that allow wide customization of the
output. The package's drawing is done with the help of TikZ.

%package -n texlive-guitarchordschemes-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.7svn54512
Release:        0
Summary:        Documentation for texlive-guitarchordschemes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-guitarchordschemes-doc:en)

%description -n texlive-guitarchordschemes-doc
This package includes the documentation for texlive-guitarchordschemes

%post -n texlive-guitarchordschemes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-guitarchordschemes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-guitarchordschemes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-guitarchordschemes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/guitarchordschemes/README
%{_texmfdistdir}/doc/latex/guitarchordschemes/guitarchordschemes_en.pdf
%{_texmfdistdir}/doc/latex/guitarchordschemes/guitarchordschemes_en.tex

%files -n texlive-guitarchordschemes
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/guitarchordschemes/guitarchordschemes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-guitarchordschemes-%{texlive_version}.%{texlive_noarch}.0.0.7svn54512-%{release}-zypper
%endif

%package -n texlive-guitartabs
Version:        %{texlive_version}.%{texlive_noarch}.svn48102
Release:        0
Summary:        A class for drawing guitar tablatures easily
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
Recommends:     texlive-guitartabs-doc >= %{texlive_version}
Provides:       tex(guitartabs.cls)
Requires:       tex(article.cls)
Requires:       tex(geometry.sty)
Requires:       tex(harmony.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(musixtex.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source165:      guitartabs.tar.xz
Source166:      guitartabs.doc.tar.xz

%description -n texlive-guitartabs
This package provides is a simple LaTeX2e class that allows
guitarists to create basic guitar tablatures using LaTeX.
Create music and do not be bothered with macro programming. The
class depends on the LaTeX packages geometry, harmony,
inputenc, intcalc, musixtex, tikz, and xifthen, as well as the
article class.

%package -n texlive-guitartabs-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn48102
Release:        0
Summary:        Documentation for texlive-guitartabs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-guitartabs-doc
This package includes the documentation for texlive-guitartabs

%post -n texlive-guitartabs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-guitartabs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-guitartabs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-guitartabs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/guitartabs/README.md
%{_texmfdistdir}/doc/latex/guitartabs/guitartabs-doc.pdf
%{_texmfdistdir}/doc/latex/guitartabs/guitartabs-doc.tex
%{_texmfdistdir}/doc/latex/guitartabs/nothingelsematters.pdf
%{_texmfdistdir}/doc/latex/guitartabs/nothingelsematters.tex

%files -n texlive-guitartabs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/guitartabs/guitartabs.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-guitartabs-%{texlive_version}.%{texlive_noarch}.svn48102-%{release}-zypper
%endif

%package -n texlive-guitlogo
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0_alpha.3svn51582
Release:        0
Summary:        Macros for typesetting the GuIT logo
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
Recommends:     texlive-guitlogo-doc >= %{texlive_version}
Provides:       tex(guit.cfg)
Provides:       tex(guit.sty)
Requires:       tex(graphics.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source167:      guitlogo.tar.xz
Source168:      guitlogo.doc.tar.xz

%description -n texlive-guitlogo
This package provides some commands useful to correctly write
the logo of "Gruppo Utilizzatori Italiani di TeX" (Italian TeX
User Group), using the default document color or any other
color the user may ever choose, in conformity with the logo's
scheme as seen on the group's website https://www.guitex.org.
Likewise, commands are provided that simplify the writing of
the GuIT acronym's complete expansion, of the addresses of the
group's internet site and public forum, and the meeting
'GuITmeeting' and the magazine Ars TeXnica's logo. Optionally,
using hyperref, the outputs of the above cited commands can
become hyperlinks to the group's website
https://www.guitex.org. The Documentation is available in
Italian only.

%package -n texlive-guitlogo-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0_alpha.3svn51582
Release:        0
Summary:        Documentation for texlive-guitlogo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-guitlogo-doc:it)

%description -n texlive-guitlogo-doc
This package includes the documentation for texlive-guitlogo

%post -n texlive-guitlogo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-guitlogo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-guitlogo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-guitlogo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/guitlogo/README
%{_texmfdistdir}/doc/latex/guitlogo/guit.pdf
%{_texmfdistdir}/doc/latex/guitlogo/guittest.pdf
%{_texmfdistdir}/doc/latex/guitlogo/guittest.tex

%files -n texlive-guitlogo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/guitlogo/guit.cfg
%{_texmfdistdir}/tex/latex/guitlogo/guit.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-guitlogo-%{texlive_version}.%{texlive_noarch}.1.0.0_alpha.3svn51582-%{release}-zypper
%endif

%package -n texlive-gustlib
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Plain macros for much core and extra functionality, from GUST
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
Recommends:     texlive-gustlib-doc >= %{texlive_version}
Provides:       tex(biblotex.tex)
Provides:       tex(infr-ex.tex)
Provides:       tex(infram.tex)
Provides:       tex(map.tex)
Provides:       tex(mcol-ex.tex)
Provides:       tex(meashor.tex)
Provides:       tex(mimulcol.tex)
Provides:       tex(plidxmac.tex)
Provides:       tex(przyklad.tex)
Provides:       tex(rbox-ex.tex)
Provides:       tex(roundbox.tex)
Provides:       tex(split.tex)
Provides:       tex(tp-crf.tex)
Provides:       tex(tsp.tex)
Provides:       tex(tun.tex)
Provides:       tex(verbatim-dek.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source169:      gustlib.tar.xz
Source170:      gustlib.doc.tar.xz

%description -n texlive-gustlib
Includes bibliography support, token manipulation,
cross-references, verbatim, determining length of a paragraph's
last line, multicolumn output, Polish bibliography and index
styles, prepress and color separation, graphics manipulation,
tables.

%package -n texlive-gustlib-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Documentation for texlive-gustlib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-gustlib-doc
This package includes the documentation for texlive-gustlib

%post -n texlive-gustlib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gustlib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gustlib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gustlib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/gustlib/README
%{_texmfdistdir}/doc/plain/gustlib/readme.biblotex
%{_texmfdistdir}/doc/plain/gustlib/readme.plbtx993
%{_texmfdistdir}/doc/plain/gustlib/readme.plmac218

%files -n texlive-gustlib
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/gustlib/plbib.bib
%{_texmfdistdir}/bibtex/bst/gustlib/plabbrv.bst
%{_texmfdistdir}/bibtex/bst/gustlib/plalpha.bst
%{_texmfdistdir}/bibtex/bst/gustlib/plplain.bst
%{_texmfdistdir}/bibtex/bst/gustlib/plunsrt.bst
%{_texmfdistdir}/tex/plain/gustlib/biblotex/biblotex.tex
%{_texmfdistdir}/tex/plain/gustlib/infr-ex.tex
%{_texmfdistdir}/tex/plain/gustlib/infram.tex
%{_texmfdistdir}/tex/plain/gustlib/licz/licz-tst.mex
%{_texmfdistdir}/tex/plain/gustlib/licz/licz.mex
%{_texmfdistdir}/tex/plain/gustlib/map/map.tex
%{_texmfdistdir}/tex/plain/gustlib/map/split.tex
%{_texmfdistdir}/tex/plain/gustlib/map/tsp-tst.mex
%{_texmfdistdir}/tex/plain/gustlib/map/tsp.tex
%{_texmfdistdir}/tex/plain/gustlib/map/tun-test.mex
%{_texmfdistdir}/tex/plain/gustlib/map/tun.tex
%{_texmfdistdir}/tex/plain/gustlib/mcol-ex.tex
%{_texmfdistdir}/tex/plain/gustlib/meashor.tex
%{_texmfdistdir}/tex/plain/gustlib/mimulcol.tex
%{_texmfdistdir}/tex/plain/gustlib/plbtx993/plbtxbst.doc
%{_texmfdistdir}/tex/plain/gustlib/plbtx993/test.mex
%{_texmfdistdir}/tex/plain/gustlib/plmac218/plidxmac.tex
%{_texmfdistdir}/tex/plain/gustlib/plmac218/przyklad.tex
%{_texmfdistdir}/tex/plain/gustlib/rbox-ex.tex
%{_texmfdistdir}/tex/plain/gustlib/roundbox.tex
%{_texmfdistdir}/tex/plain/gustlib/tp-crf.tex
%{_texmfdistdir}/tex/plain/gustlib/verbatim-dek.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gustlib-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif

%package -n texlive-gustprog
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Utility programs for Polish users of TeX
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
Source171:      gustprog.doc.tar.xz

%description -n texlive-gustprog
Provided as sources, not installed in the bin directories.
%post -n texlive-gustprog
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gustprog 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gustprog
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gustprog
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/gustprog/README
%{_texmfdistdir}/doc/support/gustprog/l2h-examples.zip
%{_texmfdistdir}/doc/support/gustprog/normtext.awk
%{_texmfdistdir}/doc/support/gustprog/plmindex.zip
%{_texmfdistdir}/doc/support/gustprog/porzadki.pl
%{_texmfdistdir}/doc/support/gustprog/slim.zip
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gustprog-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif

%package -n texlive-gzt
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn54390
Release:        0
Summary:        Bundle of classes for "La Gazette des Mathematiciens"
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
Recommends:     texlive-gzt-doc >= %{texlive_version}
Provides:       tex(gzt.cfg)
Provides:       tex(gzt.cls)
Provides:       tex(gzt.lbx)
Provides:       tex(gztarticle.cls)
Requires:       tex(adjustbox.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(amsthm.sty)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(datatool.sty)
Requires:       tex(datetime.sty)
Requires:       tex(draftwatermark.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(epigraph.sty)
Requires:       tex(esvect.sty)
Requires:       tex(etoc.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(everypage.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iflang.sty)
Requires:       tex(import.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kpfonts.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(mwe.sty)
Requires:       tex(nccparskip.sty)
Requires:       tex(pagegrid.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(placeins.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(rsfso.sty)
Requires:       tex(silence.sty)
Requires:       tex(standalone.sty)
Requires:       tex(tableof.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textcase.sty)
Requires:       tex(thmtools.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tikzpagenodes.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(translator.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xspace.sty)
Requires:       tex(zref-totpages.sty)
Requires:       tex(zref-xr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source172:      gzt.tar.xz
Source173:      gzt.doc.tar.xz

%description -n texlive-gzt
This bundle provides two classes and BibLaTeX styles for the
French journal "La Gazette des Mathematiciens": gzt for the
complete issues of the journal, aimed at the Gazette's team,
gztarticle, intended for authors who wish to publish an article
in the Gazette. This class's goals are to faithfully reproduce
the layout of the Gazette, thus enabling the authors to be able
to work their document in actual conditions, and provide a
number of tools (commands and environments) to facilitate the
drafting of documents, in particular those containing
mathematical formulas.

%package -n texlive-gzt-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn54390
Release:        0
Summary:        Documentation for texlive-gzt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-gzt-doc:fr)

%description -n texlive-gzt-doc
This package includes the documentation for texlive-gzt

%post -n texlive-gzt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-gzt 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-gzt
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-gzt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/gzt/CHANGELOG.md
%{_texmfdistdir}/doc/latex/gzt/README.md
%{_texmfdistdir}/doc/latex/gzt/english/README-TRANSLATION.md
%{_texmfdistdir}/doc/latex/gzt/french/denis.png
%{_texmfdistdir}/doc/latex/gzt/french/gzt-fr.bib
%{_texmfdistdir}/doc/latex/gzt/french/gzt-fr.pdf
%{_texmfdistdir}/doc/latex/gzt/french/gzt-fr.tex
%{_texmfdistdir}/doc/latex/gzt/french/latexmkrc
%{_texmfdistdir}/doc/latex/gzt/french/sections/fixed-footnotes.tex
%{_texmfdistdir}/doc/latex/gzt/french/sections/gztarticle.tex
%{_texmfdistdir}/doc/latex/gzt/french/sections/notations.tex
%{_texmfdistdir}/doc/latex/gzt/french/sections/packages-charges.tex
%{_texmfdistdir}/doc/latex/gzt/french/sections/todo.tex

%files -n texlive-gzt
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/gzt/gzt.cfg
%{_texmfdistdir}/tex/latex/gzt/gzt.cls
%{_texmfdistdir}/tex/latex/gzt/gzt.dbx
%{_texmfdistdir}/tex/latex/gzt/gzt.lbx
%{_texmfdistdir}/tex/latex/gzt/gztarticle.cls
%{_texmfdistdir}/tex/latex/gzt/images/README-PICTOGRAMS.md
%{_texmfdistdir}/tex/latex/gzt/images/gzt-logo.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-gzt-%{texlive_version}.%{texlive_noarch}.1.0.0svn54390-%{release}-zypper
%endif

%package -n texlive-h2020proposal
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn38428
Release:        0
Summary:        LaTeX class and template for EU H2020 RIA proposal
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
Recommends:     texlive-h2020proposal-doc >= %{texlive_version}
Provides:       tex(h2020proposal.cls)
Requires:       tex(colortbl.sty)
Requires:       tex(coolstr.sty)
Requires:       tex(longtable.sty)
Requires:       tex(memoir.cls)
Requires:       tex(morewrites.sty)
Requires:       tex(rotating.sty)
Requires:       tex(showkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source174:      h2020proposal.tar.xz
Source175:      h2020proposal.doc.tar.xz

%description -n texlive-h2020proposal
This package consists of a class file as well as FET and ICT
proposal templates for writing EU H2020 RIA proposals and
generating automatically the many cross-referenced tables that
are required.

%package -n texlive-h2020proposal-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn38428
Release:        0
Summary:        Documentation for texlive-h2020proposal
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-h2020proposal-doc
This package includes the documentation for texlive-h2020proposal

%post -n texlive-h2020proposal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-h2020proposal 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-h2020proposal
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-h2020proposal-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/h2020proposal/README.txt
%{_texmfdistdir}/doc/latex/h2020proposal/gpl.txt
%{_texmfdistdir}/doc/latex/h2020proposal/manual/h2020proposal.pdf
%{_texmfdistdir}/doc/latex/h2020proposal/manual/h2020proposal.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/abstract.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/appendix.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/ethics.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/excellence.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/gantt.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/impact.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/implementation.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/members.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/template-fet.pdf
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/template-fet.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/wp-develop.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/wp-management.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-fet/wp-test.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/abstract.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/appendix.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/ethics.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/excellence.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/gantt.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/impact.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/implementation.pdf
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/implementation.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/members.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/template-ict.pdf
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/template-ict.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/wp-develop.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/wp-management.tex
%{_texmfdistdir}/doc/latex/h2020proposal/template-ict/wp-test.tex

%files -n texlive-h2020proposal
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/h2020proposal/h2020proposal.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-h2020proposal-%{texlive_version}.%{texlive_noarch}.1.0svn38428-%{release}-zypper
%endif

%package -n texlive-hackthefootline
Version:        %{texlive_version}.%{texlive_noarch}.svn46494
Release:        0
Summary:        Footline selection and configuration for LaTeX beamer's standard themes
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
Recommends:     texlive-hackthefootline-doc >= %{texlive_version}
Provides:       tex(hackthefootline.sty)
Requires:       tex(appendixnumberbeamer.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(numprint.sty)
Requires:       tex(pgfkeys.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source176:      hackthefootline.tar.xz
Source177:      hackthefootline.doc.tar.xz

%description -n texlive-hackthefootline
This package is taking over, defining and redefining different
footlines. Configuration is provided via using key-value
syntax. It depends on the pgfkeys used for providing the
configuration keys. Optional features require the following
LaTeX packages: appendixnumberbeamer, calc, etoolbox, and
numprint.

%package -n texlive-hackthefootline-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn46494
Release:        0
Summary:        Documentation for texlive-hackthefootline
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hackthefootline-doc
This package includes the documentation for texlive-hackthefootline

%post -n texlive-hackthefootline
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hackthefootline 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hackthefootline
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hackthefootline-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hackthefootline/README.md
%{_texmfdistdir}/doc/latex/hackthefootline/doc/hackthefootline-doc.pdf
%{_texmfdistdir}/doc/latex/hackthefootline/doc/hackthefootline-doc.tex
%{_texmfdistdir}/doc/latex/hackthefootline/doc/hackthefootline-examples.pdf
%{_texmfdistdir}/doc/latex/hackthefootline/doc/hackthefootline-examples.tex

%files -n texlive-hackthefootline
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hackthefootline/hackthefootline.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hackthefootline-%{texlive_version}.%{texlive_noarch}.svn46494-%{release}-zypper
%endif

%package -n texlive-hacm
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27671
Release:        0
Summary:        Font support for the Arka language
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
Requires:       texlive-hacm-fonts >= %{texlive_version}
Recommends:     texlive-hacm-doc >= %{texlive_version}
Provides:       tex(alblant.tfm)
Provides:       tex(alblant.vf)
Provides:       tex(defans.tfm)
Provides:       tex(defans.vf)
Provides:       tex(fenlil.tfm)
Provides:       tex(fenlil.vf)
Provides:       tex(fialis.tfm)
Provides:       tex(fialis.vf)
Provides:       tex(hacm.map)
Provides:       tex(hacm.sty)
Provides:       tex(inje.tfm)
Provides:       tex(inje.vf)
Provides:       tex(kardinal.tfm)
Provides:       tex(kardinal.vf)
Provides:       tex(lantia.tfm)
Provides:       tex(lantia.vf)
Provides:       tex(nalnia.tfm)
Provides:       tex(nalnia.vf)
Provides:       tex(olivia.tfm)
Provides:       tex(olivia.vf)
Provides:       tex(ot1halb.fd)
Provides:       tex(ot1hdef.fd)
Provides:       tex(ot1hfen.fd)
Provides:       tex(ot1hfia.fd)
Provides:       tex(ot1hinj.fd)
Provides:       tex(ot1hkar.fd)
Provides:       tex(ot1hlan.fd)
Provides:       tex(ralblant.tfm)
Provides:       tex(rdefans.tfm)
Provides:       tex(rfenlil.tfm)
Provides:       tex(rfialis.tfm)
Provides:       tex(rinje.tfm)
Provides:       tex(rkardinal.tfm)
Provides:       tex(rlantia.tfm)
Provides:       tex(rnalnia.tfm)
Provides:       tex(rolivia.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source178:      hacm.tar.xz
Source179:      hacm.doc.tar.xz

%description -n texlive-hacm
The package supports typesetting hacm, the alphabet of the
constructed language Arka. The bundle provides nine official
fonts, in Adobe Type 1 format.

%package -n texlive-hacm-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27671
Release:        0
Summary:        Documentation for texlive-hacm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hacm-doc
This package includes the documentation for texlive-hacm


%package -n texlive-hacm-fonts
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn27671
Release:        0
Summary:        Severed fonts for texlive-hacm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-hacm-fonts
The  separated fonts package for texlive-hacm
%post -n texlive-hacm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap hacm.map' >> /var/run/texlive/run-updmap

%postun -n texlive-hacm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap hacm.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-hacm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-hacm-fonts
%files -n texlive-hacm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/hacm/README
%{_texmfdistdir}/doc/fonts/hacm/hacmdoc.pdf
%{_texmfdistdir}/doc/fonts/hacm/hacmdoc.tex

%files -n texlive-hacm
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/hacm/hacm.map
%{_texmfdistdir}/fonts/tfm/public/hacm/alblant.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/defans.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/fenlil.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/fialis.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/inje.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/kardinal.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/lantia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/nalnia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/olivia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/ralblant.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rdefans.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rfenlil.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rfialis.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rinje.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rkardinal.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rlantia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rnalnia.tfm
%{_texmfdistdir}/fonts/tfm/public/hacm/rolivia.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/alblant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/defans.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/fenlil.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/fialis.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/inje.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/kardinal.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/lantia.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/nalnia.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hacm/olivia.pfb
%{_texmfdistdir}/fonts/vf/public/hacm/alblant.vf
%{_texmfdistdir}/fonts/vf/public/hacm/defans.vf
%{_texmfdistdir}/fonts/vf/public/hacm/fenlil.vf
%{_texmfdistdir}/fonts/vf/public/hacm/fialis.vf
%{_texmfdistdir}/fonts/vf/public/hacm/inje.vf
%{_texmfdistdir}/fonts/vf/public/hacm/kardinal.vf
%{_texmfdistdir}/fonts/vf/public/hacm/lantia.vf
%{_texmfdistdir}/fonts/vf/public/hacm/nalnia.vf
%{_texmfdistdir}/fonts/vf/public/hacm/olivia.vf
%{_texmfdistdir}/tex/latex/hacm/hacm.sty
%{_texmfdistdir}/tex/latex/hacm/ot1halb.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hdef.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hfen.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hfia.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hinj.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hkar.fd
%{_texmfdistdir}/tex/latex/hacm/ot1hlan.fd

%files -n texlive-hacm-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-hacm
%{_datadir}/fontconfig/conf.avail/58-texlive-hacm.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hacm/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hacm/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hacm/fonts.scale
%{_datadir}/fonts/texlive-hacm/alblant.pfb
%{_datadir}/fonts/texlive-hacm/defans.pfb
%{_datadir}/fonts/texlive-hacm/fenlil.pfb
%{_datadir}/fonts/texlive-hacm/fialis.pfb
%{_datadir}/fonts/texlive-hacm/inje.pfb
%{_datadir}/fonts/texlive-hacm/kardinal.pfb
%{_datadir}/fonts/texlive-hacm/lantia.pfb
%{_datadir}/fonts/texlive-hacm/nalnia.pfb
%{_datadir}/fonts/texlive-hacm/olivia.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hacm-fonts-%{texlive_version}.%{texlive_noarch}.0.0.1svn27671-%{release}-zypper
%endif

%package -n texlive-hagenberg-thesis
Version:        %{texlive_version}.%{texlive_noarch}.svn51150
Release:        0
Summary:        A Collection of LaTeX classes, style files, and example documents for academic manuscripts
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
Recommends:     texlive-hagenberg-thesis-doc >= %{texlive_version}
Provides:       tex(hgb.sty)
Provides:       tex(hgbabbrev.sty)
Provides:       tex(hgbalgo.sty)
Provides:       tex(hgbarticle.cls)
Provides:       tex(hgbbib.sty)
Provides:       tex(hgbheadings.sty)
Provides:       tex(hgblistings.sty)
Provides:       tex(hgbmath.sty)
Provides:       tex(hgbreport.cls)
Provides:       tex(hgbthesis.cls)
Requires:       tex(abstract.sty)
Requires:       tex(algorithm.sty)
Requires:       tex(algpseudocode.sty)
Requires:       tex(amsbsy.sty)
Requires:       tex(amsfonts.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(book.cls)
Requires:       tex(breakurl.sty)
Requires:       tex(calc.sty)
Requires:       tex(caption.sty)
Requires:       tex(cmap.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(datetime.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(epstopdf.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(exscale.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hypcap.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(listingsutf8.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(overpic.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pict2e.sty)
Requires:       tex(report.cls)
Requires:       tex(subdepth.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titling.sty)
Requires:       tex(tocbasic.sty)
Requires:       tex(upquote.sty)
Requires:       tex(url.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source180:      hagenberg-thesis.tar.xz
Source181:      hagenberg-thesis.doc.tar.xz

%description -n texlive-hagenberg-thesis
This bundle contains a collection of modern LaTeX classes,
style files, and example documents for authoring Bachelor,
Master, or Diploma theses and related academic manuscripts in
English and German. Includes a comprehensive tutorial (in
German) with detailed instructions and authoring guidelines.

%package -n texlive-hagenberg-thesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn51150
Release:        0
Summary:        Documentation for texlive-hagenberg-thesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hagenberg-thesis-doc:de)

%description -n texlive-hagenberg-thesis-doc
This package includes the documentation for texlive-hagenberg-thesis

%post -n texlive-hagenberg-thesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hagenberg-thesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hagenberg-thesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hagenberg-thesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hagenberg-thesis/README.md
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbArticle/images/cola-public-domain-photo-p.jpg
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbArticle/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbArticle/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbArticle/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbArticle/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbInternshipReport/images/logo.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbInternshipReport/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbInternshipReport/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbInternshipReport/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbInternshipReport/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportDE/images/screenshot-clean.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportDE/images/screenshot-dirty.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportDE/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportDE/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportDE/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportDE/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportEN/images/screenshot-clean.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportEN/images/screenshot-dirty.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportEN/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportEN/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportEN/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbLabReportEN/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbTermReport/images/PLACE_IMAGES_HERE.txt
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbTermReport/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbTermReport/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbTermReport/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbTermReport/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/back/anhang_a.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/back/anhang_b.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/back/anhang_c.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/back/anhang_d.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/back/messbox.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/abbildungen.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/abschlussarbeit.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/drucken.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/einleitung.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/latex.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/literatur.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/mathematik.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/chapters/schluss.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/front/abstract.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/front/kurzfassung.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/front/vorwort.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/images/logo.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisDE/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/back/appendix_a.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/back/appendix_b.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/back/appendix_c.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/back/appendix_d.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/back/printbox.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/closing.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/figures.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/introduction.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/latex.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/literature.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/mathematics.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/printing.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/chapters/thethesis.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/front/abstract.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/front/kurzfassung.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/front/preface.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/images/logo.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisEN/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/back/anhang_a.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/back/anhang_b.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/back/anhang_c.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/back/anhang_d.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/back/messbox.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/abbildungen.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/abschlussarbeit.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/drucken.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/einleitung.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/latex.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/literatur.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/mathematik.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/chapters/schluss.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/front/abstract.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/front/kurzfassung.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/front/vorwort.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/ball-bearing-1.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/ball-bearing-2.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/cola-public-domain-photo-p.jpg
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/ellipse-parameters-1.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/ellipse-parameters-2.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/ellipse-parameters.ai
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/ellipse-parameters.fh11.zip
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/fragebogen.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/freehand-export-screen-setup.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/ibm-360-color.jpg
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/inkscape-pdf-save-screenhot.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/inkscape-template-orig.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/inkscape-template.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/inkscape-template.pdf_tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/inkscape-template.svg
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/logo.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/mathematica-example.nb
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/mathematica-example.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/overhang-mounting.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/photoshop-eps-screen.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/screenshot-clean.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/screenshot-dirty.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/straddle-mounting.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/techniccenter-profile-dvi-26.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/techniccenter-profile-dvips-26.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/workflow-cm.fh11.zip
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/workflow-cm.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/images/yap-inverse-search-settings.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial-smartquotes/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/back/anhang_a.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/back/anhang_b.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/back/anhang_c.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/back/anhang_d.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/back/messbox.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/abbildungen.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/abschlussarbeit.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/drucken.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/einleitung.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/latex.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/literatur.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/mathematik.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/chapters/schluss.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/front/abstract.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/front/kurzfassung.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/front/vorwort.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/ball-bearing-1.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/ball-bearing-2.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/cola-public-domain-photo-p.jpg
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/ellipse-parameters-1.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/ellipse-parameters-2.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/ellipse-parameters.ai
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/ellipse-parameters.fh11.zip
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/fragebogen.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/freehand-export-screen-setup.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/ibm-360-color.jpg
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/inkscape-pdf-save-screenhot.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/inkscape-template-orig.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/inkscape-template.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/inkscape-template.pdf_tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/inkscape-template.svg
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/logo.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/mathematica-example.nb
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/mathematica-example.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/overhang-mounting.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/photoshop-eps-screen.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/screenshot-clean.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/screenshot-dirty.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/straddle-mounting.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/techniccenter-profile-dvi-26.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/techniccenter-profile-dvips-26.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/workflow-cm.fh11.zip
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/workflow-cm.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/images/yap-inverse-search-settings.png
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/HgbThesisTutorial/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/Manual/main.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/Manual/main.tcp
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/Manual/main.tex
%{_texmfdistdir}/doc/latex/hagenberg-thesis/examples/Manual/references.bib
%{_texmfdistdir}/doc/latex/hagenberg-thesis/hagenberg-thesis-tutorial.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/hagenberg-thesis.pdf
%{_texmfdistdir}/doc/latex/hagenberg-thesis/hagenberg-thesis.tex

%files -n texlive-hagenberg-thesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgb.sty
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbabbrev.sty
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbalgo.sty
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbarticle.cls
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbbib.sty
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbheadings.sty
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgblistings.sty
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbmath.sty
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbreport.cls
%{_texmfdistdir}/tex/latex/hagenberg-thesis/hgbthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hagenberg-thesis-%{texlive_version}.%{texlive_noarch}.svn51150-%{release}-zypper
%endif

%package -n texlive-halloweenmath
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn52602
Release:        0
Summary:        Scary and creepy math symbols with AMS-LaTeX integration
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
Recommends:     texlive-halloweenmath-doc >= %{texlive_version}
Provides:       tex(halloweenmath.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(pict2e.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source182:      halloweenmath.tar.xz
Source183:      halloweenmath.doc.tar.xz

%description -n texlive-halloweenmath
The package defines a handful of commands for typesetting
mathematical symbols of various kinds, ranging from 'large'
operators to extensible arrow-like relations and growing
arrow-like math accents that all draw from the classic
Halloween-related iconography (pumpkins, witches, ghosts, cats,
and so on) while being, at the same time, seamlessly integrated
within the rest of the mathematics produced by (AmS-)LaTeX.

%package -n texlive-halloweenmath-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn52602
Release:        0
Summary:        Documentation for texlive-halloweenmath
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-halloweenmath-doc
This package includes the documentation for texlive-halloweenmath

%post -n texlive-halloweenmath
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-halloweenmath 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-halloweenmath
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-halloweenmath-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/halloweenmath/00readme.txt
%{_texmfdistdir}/doc/latex/halloweenmath/README
%{_texmfdistdir}/doc/latex/halloweenmath/halloweenmath-doc.pdf
%{_texmfdistdir}/doc/latex/halloweenmath/halloweenmath-man.pdf
%{_texmfdistdir}/doc/latex/halloweenmath/halloweenmath-man.tex
%{_texmfdistdir}/doc/latex/halloweenmath/manifest.txt

%files -n texlive-halloweenmath
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/halloweenmath/halloweenmath.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-halloweenmath-%{texlive_version}.%{texlive_noarch}.0.0.11svn52602-%{release}-zypper
%endif

%package -n texlive-handin
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn48255
Release:        0
Summary:        Light weight template for creating school submissions using LaTeX
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
Recommends:     texlive-handin-doc >= %{texlive_version}
Provides:       tex(handin.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(bm.sty)
Requires:       tex(esint.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iflang.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(pgfopts.sty)
Requires:       tex(scrextend.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source184:      handin.tar.xz
Source185:      handin.doc.tar.xz

%description -n texlive-handin
This package is for students creating school submissions using
LaTeX. It is especially suitable for math, physics, statistics
and the like. It can easily be used for creating exercises,
too.

%package -n texlive-handin-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1.1svn48255
Release:        0
Summary:        Documentation for texlive-handin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-handin-doc
This package includes the documentation for texlive-handin

%post -n texlive-handin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-handin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-handin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-handin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/handin/README.txt
%{_texmfdistdir}/doc/latex/handin/example.pdf
%{_texmfdistdir}/doc/latex/handin/example.tex
%{_texmfdistdir}/doc/latex/handin/handin-doc.pdf
%{_texmfdistdir}/doc/latex/handin/handin-doc.tex
%{_texmfdistdir}/doc/latex/handin/layout.pdf

%files -n texlive-handin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/handin/handin.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-handin-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn48255-%{release}-zypper
%endif

%package -n texlive-handout
Version:        %{texlive_version}.%{texlive_noarch}.1.6.0svn43962
Release:        0
Summary:        Create handout for auditors of a talk
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
Recommends:     texlive-handout-doc >= %{texlive_version}
Provides:       tex(handout.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(suffix.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source186:      handout.tar.xz
Source187:      handout.doc.tar.xz

%description -n texlive-handout
In some fields of scholarship, a beamer does not offer good
support when giving a talk in a proceeding. For example, in
classical philology, the main sources are text, and it will be
better to distribute a handout to the audience with extracts of
the texts about which we will talk. The package supports
preparation of such handouts when writing the talk.

%package -n texlive-handout-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6.0svn43962
Release:        0
Summary:        Documentation for texlive-handout
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-handout-doc
This package includes the documentation for texlive-handout

%post -n texlive-handout
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-handout 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-handout
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-handout-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/handout/README
%{_texmfdistdir}/doc/latex/handout/examples/example.bib
%{_texmfdistdir}/doc/latex/handout/examples/example1-minimal.pdf
%{_texmfdistdir}/doc/latex/handout/examples/example1-minimal.tex
%{_texmfdistdir}/doc/latex/handout/examples/example2-cancel-quotation.pdf
%{_texmfdistdir}/doc/latex/handout/examples/example2-cancel-quotation.tex
%{_texmfdistdir}/doc/latex/handout/examples/example3-defined-path.pdf
%{_texmfdistdir}/doc/latex/handout/examples/example3-defined-path.tex
%{_texmfdistdir}/doc/latex/handout/examples/example4-sectioning.pdf
%{_texmfdistdir}/doc/latex/handout/examples/example4-sectioning.tex
%{_texmfdistdir}/doc/latex/handout/examples/example5-numbering.pdf
%{_texmfdistdir}/doc/latex/handout/examples/example5-numbering.tex
%{_texmfdistdir}/doc/latex/handout/examples/example6-not-and-only.pdf
%{_texmfdistdir}/doc/latex/handout/examples/example6-not-and-only.tex
%{_texmfdistdir}/doc/latex/handout/examples/example7-biblatex.pdf
%{_texmfdistdir}/doc/latex/handout/examples/example7-biblatex.tex
%{_texmfdistdir}/doc/latex/handout/examples/latexmkrc
%{_texmfdistdir}/doc/latex/handout/examples/makefile
%{_texmfdistdir}/doc/latex/handout/examples/txt/Preau1583-not-and-only.tex
%{_texmfdistdir}/doc/latex/handout/examples/txt/Preau1583.tex
%{_texmfdistdir}/doc/latex/handout/examples/txt/Preau1583b.tex
%{_texmfdistdir}/doc/latex/handout/examples/txt/Richard_Simon_NT.tex
%{_texmfdistdir}/doc/latex/handout/handout.pdf
%{_texmfdistdir}/doc/latex/handout/handout.tex
%{_texmfdistdir}/doc/latex/handout/latexmkrc
%{_texmfdistdir}/doc/latex/handout/makefile

%files -n texlive-handout
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/handout/handout.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-handout-%{texlive_version}.%{texlive_noarch}.1.6.0svn43962-%{release}-zypper
%endif

%package -n texlive-hands
Version:        %{texlive_version}.%{texlive_noarch}.svn13293
Release:        0
Summary:        Pointing hand font
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
Provides:       tex(hands.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source188:      hands.tar.xz

%description -n texlive-hands
Provides right- and left-pointing hands in both black-on-white
and white-on-black realisation. The font is distributed as
Metafont source.
%post -n texlive-hands
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hands 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hands
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hands
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/hands/hands.mf
%{_texmfdistdir}/fonts/source/public/hands/handsdef.mf
%{_texmfdistdir}/fonts/source/public/hands/mirror.mf
%{_texmfdistdir}/fonts/source/public/hands/reverse.mf
%{_texmfdistdir}/fonts/source/public/hands/rvmirror.mf
%{_texmfdistdir}/fonts/tfm/public/hands/hands.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hands-%{texlive_version}.%{texlive_noarch}.svn13293-%{release}-zypper
%endif

%package -n texlive-hang
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn43280
Release:        0
Summary:        Environments for hanging paragraphs and list items
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
Recommends:     texlive-hang-doc >= %{texlive_version}
Provides:       tex(hang.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source189:      hang.tar.xz
Source190:      hang.doc.tar.xz

%description -n texlive-hang
This package provides environments for hanging paragraphs and
list items. In addition, it defines environments for labeled
paragraphs and list items.

%package -n texlive-hang-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn43280
Release:        0
Summary:        Documentation for texlive-hang
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hang-doc
This package includes the documentation for texlive-hang

%post -n texlive-hang
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hang 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hang
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hang-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hang/COPYING
%{_texmfdistdir}/doc/latex/hang/ChangeLog
%{_texmfdistdir}/doc/latex/hang/README
%{_texmfdistdir}/doc/latex/hang/hang.pdf
%{_texmfdistdir}/doc/latex/hang/hang.tex
%{_texmfdistdir}/doc/latex/hang/sample.pdf
%{_texmfdistdir}/doc/latex/hang/sample.tex

%files -n texlive-hang
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hang/hang.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hang-%{texlive_version}.%{texlive_noarch}.2.1svn43280-%{release}-zypper
%endif

%package -n texlive-hanging
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn15878
Release:        0
Summary:        Hanging paragraphs
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
Recommends:     texlive-hanging-doc >= %{texlive_version}
Provides:       tex(hanging.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source191:      hanging.tar.xz
Source192:      hanging.doc.tar.xz

%description -n texlive-hanging
The hanging package facilitates the typesetting of hanging
paragraphs. The package also enables typesetting with hanging
punctuation, by making punctuation characters active. This
facility is best suppressed (it can interfere with other
packages) -- there are package options for suppressing each
individual punctuation character. 'Real' attempts at hanging
punction should nowadays use the microtype package, which takes
advantage of the support offered in recent versions of pdfTeX.

%package -n texlive-hanging-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2bsvn15878
Release:        0
Summary:        Documentation for texlive-hanging
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hanging-doc
This package includes the documentation for texlive-hanging

%post -n texlive-hanging
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hanging 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hanging
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hanging-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hanging/README
%{_texmfdistdir}/doc/latex/hanging/hanging.pdf

%files -n texlive-hanging
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hanging/hanging.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hanging-%{texlive_version}.%{texlive_noarch}.1.2bsvn15878-%{release}-zypper
%endif

%package -n texlive-hanoi
Version:        %{texlive_version}.%{texlive_noarch}.20120101svn25019
Release:        0
Summary:        Tower of Hanoi in TeX
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
Provides:       tex(hanoi.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source193:      hanoi.tar.xz

%description -n texlive-hanoi
The Plain TeX program (typed in the shape of the towers of
Hanoi) serves both as a game and as a TeX programming exercise.
As a game it will solve the towers with (up to) 15 discs (with
15 discs, 32767 moves are needed).
%post -n texlive-hanoi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hanoi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hanoi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hanoi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/hanoi/hanoi.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hanoi-%{texlive_version}.%{texlive_noarch}.20120101svn25019-%{release}-zypper
%endif

%package -n texlive-happy4th
Version:        %{texlive_version}.%{texlive_noarch}.20120102svn25020
Release:        0
Summary:        A firework display in obfuscated TeX
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
Source194:      happy4th.doc.tar.xz

%description -n texlive-happy4th
The output PDF file gives an amusing display, as the reader
pages through it.
%post -n texlive-happy4th
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-happy4th 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-happy4th
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-happy4th
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/happy4th/happy4th.pdf
%{_texmfdistdir}/doc/plain/happy4th/happy4th.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-happy4th-%{texlive_version}.%{texlive_noarch}.20120102svn25020-%{release}-zypper
%endif

%package -n texlive-har2nat
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Replace the harvard package with natbib
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
Recommends:     texlive-har2nat-doc >= %{texlive_version}
Provides:       tex(har2nat.sty)
Requires:       tex(natbib.sty)
Requires:       tex(suffix.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source195:      har2nat.tar.xz
Source196:      har2nat.doc.tar.xz

%description -n texlive-har2nat
This small package allows a LaTeX document containing the
citation commands provided by the Harvard package to be
compiled using the natbib package. Migration from harvard to
natbib thus can be achieved simply by replacing
\usepackage{harvard} with usepackage{natbib}
usepackage{har2nat} It is important that har2nat be loaded
after natbib, since it modifies natbib commands.

%package -n texlive-har2nat-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Documentation for texlive-har2nat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-har2nat-doc
This package includes the documentation for texlive-har2nat

%post -n texlive-har2nat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-har2nat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-har2nat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-har2nat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/har2nat/README
%{_texmfdistdir}/doc/latex/har2nat/har2nat.pdf
%{_texmfdistdir}/doc/latex/har2nat/har2nat.tex

%files -n texlive-har2nat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/har2nat/har2nat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-har2nat-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif

%package -n texlive-haranoaji
Version:        %{texlive_version}.%{texlive_noarch}.20200418svn54784
Release:        0
Summary:        Harano Aji Fonts
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(post): perl = %{perl_version}
Requires(post): perl(TeXLive::TLUtils)
Requires(post): tex(texmf.cnf)
Requires(post): texlive-kpathsea-bin >= %{texlive_version}
Requires(post): texlive-texlive.infra >= %{texlive_version}
#!BuildIgnore: texlive-kpathsea
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-haranoaji-fonts >= %{texlive_version}
Recommends:     texlive-haranoaji-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source197:      haranoaji.tar.xz
Source198:      haranoaji.doc.tar.xz

%description -n texlive-haranoaji
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are
fonts obtained by replacing Adobe-Identity-0 (AI0) CIDs of
Source Han fonts (Source Han Serif and Source Han Sans) with
Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7 weights each for
Mincho and Gothic.

%package -n texlive-haranoaji-doc
Version:        %{texlive_version}.%{texlive_noarch}.20200418svn54784
Release:        0
Summary:        Documentation for texlive-haranoaji
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-haranoaji-doc
This package includes the documentation for texlive-haranoaji


%package -n texlive-haranoaji-fonts
Version:        %{texlive_version}.%{texlive_noarch}.20200418svn54784
Release:        0
Summary:        Severed fonts for texlive-haranoaji
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-haranoaji-fonts
The  separated fonts package for texlive-haranoaji
%post -n texlive-haranoaji
mkdir -p /var/run/texlive
mkdir -p /var/run/texlive/scriptlets
cat > /var/run/texlive/scriptlets/haranoaji << 'EOF'
/usr/bin/perl %{_texmfmaindir}/tlpkg/tlpostcode/haranoaji-tlpost.pl install %{_texmfmaindir}
EOF
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-haranoaji 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-haranoaji
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-haranoaji-fonts
%files -n texlive-haranoaji-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/haranoaji/LICENSE
%{_texmfdistdir}/doc/fonts/haranoaji/README

%files -n texlive-haranoaji
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji/HaranoAjiGothic-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji/HaranoAjiGothic-Heavy.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji/HaranoAjiGothic-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji/HaranoAjiGothic-Regular.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji/HaranoAjiMincho-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji/HaranoAjiMincho-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji/HaranoAjiMincho-Regular.otf
%{_texmfdistdir}/tex/latex/haranoaji/HaranoAjiGothic.fontspec
%{_texmfdistdir}/tex/latex/haranoaji/HaranoAjiMincho.fontspec
%{_texmfmaindir}/tlpkg/tlpostcode/haranoaji-tlpost.pl

%files -n texlive-haranoaji-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-haranoaji
%{_datadir}/fontconfig/conf.avail/58-texlive-haranoaji.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-haranoaji/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-haranoaji/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-haranoaji/fonts.scale
%{_datadir}/fonts/texlive-haranoaji/HaranoAjiGothic-Bold.otf
%{_datadir}/fonts/texlive-haranoaji/HaranoAjiGothic-Heavy.otf
%{_datadir}/fonts/texlive-haranoaji/HaranoAjiGothic-Medium.otf
%{_datadir}/fonts/texlive-haranoaji/HaranoAjiGothic-Regular.otf
%{_datadir}/fonts/texlive-haranoaji/HaranoAjiMincho-Bold.otf
%{_datadir}/fonts/texlive-haranoaji/HaranoAjiMincho-Light.otf
%{_datadir}/fonts/texlive-haranoaji/HaranoAjiMincho-Regular.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-haranoaji-fonts-%{texlive_version}.%{texlive_noarch}.20200418svn54784-%{release}-zypper
%endif

%package -n texlive-haranoaji-extra
Version:        %{texlive_version}.%{texlive_noarch}.20200418svn54783
Release:        0
Summary:        Harano Aji Fonts
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
Requires:       texlive-haranoaji-extra-fonts >= %{texlive_version}
Recommends:     texlive-haranoaji-extra-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source199:      haranoaji-extra.tar.xz
Source200:      haranoaji-extra.doc.tar.xz

%description -n texlive-haranoaji-extra
Harano Aji Fonts (Harano Aji Mincho and Harano Aji Gothic) are
fonts obtained by replacing Adobe-Identity-0 (AI0) CIDs of
Source Han fonts (Source Han Serif and Source Han Sans) with
Adobe-Japan1 (AJ1) CIDs. There are 14 fonts, 7 weights each for
Mincho and Gothic.

%package -n texlive-haranoaji-extra-doc
Version:        %{texlive_version}.%{texlive_noarch}.20200418svn54783
Release:        0
Summary:        Documentation for texlive-haranoaji-extra
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-haranoaji-extra-doc
This package includes the documentation for texlive-haranoaji-extra


%package -n texlive-haranoaji-extra-fonts
Version:        %{texlive_version}.%{texlive_noarch}.20200418svn54783
Release:        0
Summary:        Severed fonts for texlive-haranoaji-extra
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-haranoaji-extra-fonts
The  separated fonts package for texlive-haranoaji-extra
%post -n texlive-haranoaji-extra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-haranoaji-extra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-haranoaji-extra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-haranoaji-extra-fonts
%files -n texlive-haranoaji-extra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/haranoaji-extra/LICENSE
%{_texmfdistdir}/doc/fonts/haranoaji-extra/README

%files -n texlive-haranoaji-extra
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/HaranoAjiGothic-ExtraLight.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/HaranoAjiGothic-Light.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/HaranoAjiGothic-Normal.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/HaranoAjiMincho-ExtraLight.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/HaranoAjiMincho-Heavy.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/HaranoAjiMincho-Medium.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/HaranoAjiMincho-SemiBold.otf

%files -n texlive-haranoaji-extra-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-haranoaji-extra
%{_datadir}/fontconfig/conf.avail/58-texlive-haranoaji-extra.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-haranoaji-extra/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-haranoaji-extra/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-haranoaji-extra/fonts.scale
%{_datadir}/fonts/texlive-haranoaji-extra/HaranoAjiGothic-ExtraLight.otf
%{_datadir}/fonts/texlive-haranoaji-extra/HaranoAjiGothic-Light.otf
%{_datadir}/fonts/texlive-haranoaji-extra/HaranoAjiGothic-Normal.otf
%{_datadir}/fonts/texlive-haranoaji-extra/HaranoAjiMincho-ExtraLight.otf
%{_datadir}/fonts/texlive-haranoaji-extra/HaranoAjiMincho-Heavy.otf
%{_datadir}/fonts/texlive-haranoaji-extra/HaranoAjiMincho-Medium.otf
%{_datadir}/fonts/texlive-haranoaji-extra/HaranoAjiMincho-SemiBold.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-haranoaji-extra-fonts-%{texlive_version}.%{texlive_noarch}.20200418svn54783-%{release}-zypper
%endif

%package -n texlive-hardwrap
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn21396
Release:        0
Summary:        Hard wrap text to a certain character length
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
Recommends:     texlive-hardwrap-doc >= %{texlive_version}
Provides:       tex(hardwrap.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source201:      hardwrap.tar.xz
Source202:      hardwrap.doc.tar.xz

%description -n texlive-hardwrap
The package facilitates wrapping text to a specific character
width, breaking lines by words rather than, as done by TeX, by
characters. The primary use for these facilities is to aid the
generation of messages sent to the log file or console output
to display messages to the user. Package authors may also find
this useful when writing out arbitary text to an external file.

%package -n texlive-hardwrap-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn21396
Release:        0
Summary:        Documentation for texlive-hardwrap
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hardwrap-doc
This package includes the documentation for texlive-hardwrap

%post -n texlive-hardwrap
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hardwrap 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hardwrap
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hardwrap-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hardwrap/README
%{_texmfdistdir}/doc/latex/hardwrap/hardwrap.pdf

%files -n texlive-hardwrap
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hardwrap/hardwrap.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hardwrap-%{texlive_version}.%{texlive_noarch}.0.0.2svn21396-%{release}-zypper
%endif

%package -n texlive-harmony
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Typeset harmony symbols, etc., for musicology
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
Recommends:     texlive-harmony-doc >= %{texlive_version}
Provides:       tex(harmony.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source203:      harmony.tar.xz
Source204:      harmony.doc.tar.xz

%description -n texlive-harmony
The package harmony.sty uses the packages ifthen and amssymb
from the amsfonts bundle, together with the LaTeX font
lcirclew10 and the font musix13 from musixtex.

%package -n texlive-harmony-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-harmony
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-harmony-doc
This package includes the documentation for texlive-harmony

%post -n texlive-harmony
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-harmony 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-harmony
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-harmony-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/harmony/README
%{_texmfdistdir}/doc/latex/harmony/harmony.pdf
%{_texmfdistdir}/doc/latex/harmony/harmony.tex

%files -n texlive-harmony
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/harmony/harmony.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-harmony-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-harnon-cv
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn26543
Release:        0
Summary:        A CV document class with a vertical timeline for experience
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
Recommends:     texlive-harnon-cv-doc >= %{texlive_version}
Provides:       tex(harnon-cv.cls)
Requires:       tex(article.cls)
Requires:       tex(cantarell.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(framed.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(nopageno.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source205:      harnon-cv.tar.xz
Source206:      harnon-cv.doc.tar.xz

%description -n texlive-harnon-cv
The class offers another modern, neat, design, and provides a
simple means of adding an 'experience timeline'.

%package -n texlive-harnon-cv-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn26543
Release:        0
Summary:        Documentation for texlive-harnon-cv
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-harnon-cv-doc
This package includes the documentation for texlive-harnon-cv

%post -n texlive-harnon-cv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-harnon-cv 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-harnon-cv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-harnon-cv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/harnon-cv/README
%{_texmfdistdir}/doc/latex/harnon-cv/sample.pdf
%{_texmfdistdir}/doc/latex/harnon-cv/sample.tex

%files -n texlive-harnon-cv
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/harnon-cv/harnon-cv.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-harnon-cv-%{texlive_version}.%{texlive_noarch}.1.0svn26543-%{release}-zypper
%endif

%package -n texlive-harpoon
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21327
Release:        0
Summary:        Extra harpoons, using the graphics package
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
Recommends:     texlive-harpoon-doc >= %{texlive_version}
Provides:       tex(harpoon.sty)
Requires:       tex(graphics.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source207:      harpoon.tar.xz
Source208:      harpoon.doc.tar.xz

%description -n texlive-harpoon
Provides over- and under-harpoon symbol commands; the harpoons
may point in either direction, with the hook pointing up or
down. The covered object is provided as an argument to the
commands, so that they have the look of accent commands.

%package -n texlive-harpoon-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21327
Release:        0
Summary:        Documentation for texlive-harpoon
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-harpoon-doc
This package includes the documentation for texlive-harpoon

%post -n texlive-harpoon
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-harpoon 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-harpoon
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-harpoon-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/harpoon/harpoon.pdf
%{_texmfdistdir}/doc/latex/harpoon/harpoon.tex

%files -n texlive-harpoon
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/harpoon/harpoon.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-harpoon-%{texlive_version}.%{texlive_noarch}.1.0svn21327-%{release}-zypper
%endif

%package -n texlive-harvard
Version:        %{texlive_version}.%{texlive_noarch}.2.0.5svn15878
Release:        0
Summary:        Harvard citation package for use with LaTeX 2e
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
Recommends:     texlive-harvard-doc >= %{texlive_version}
Provides:       tex(harvard.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source209:      harvard.tar.xz
Source210:      harvard.doc.tar.xz

%description -n texlive-harvard
This is a re-implementation, for LaTeX 2e, of the original
Harvard package. The bundle contains the LaTeX package, several
BibTeX styles, and a 'Perl package' for use with LaTeX2HTML.
Harvard is an author-year citation style (all but the first
author are suppressed in second and subsequent citations of the
same entry); the package defines several variant styles:
apsr.bst for the American Political Science Review; agsm.bst
for Australian Government publications; dcu.bst from the Design
Computing Unit of the University of Sydney; kluwer.bstwhich
aims at the format preferred in Kluwer publications;
nederlands.bst which deals with sorting Dutch names with
prefixes (such as van) according to Dutch rules, together with
several styles whose authors offer no description of their
behaviour.

%package -n texlive-harvard-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.5svn15878
Release:        0
Summary:        Documentation for texlive-harvard
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-harvard-doc
This package includes the documentation for texlive-harvard

%post -n texlive-harvard
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-harvard 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-harvard
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-harvard-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/harvard/INSTALL
%{_texmfdistdir}/doc/latex/harvard/README
%{_texmfdistdir}/doc/latex/harvard/harvard.pdf
%{_texmfdistdir}/doc/latex/harvard/harvard.perl
%{_texmfdistdir}/doc/latex/harvard/harvard.tex
%{_texmfdistdir}/doc/latex/harvard/manifest.txt

%files -n texlive-harvard
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/harvard/harvard.bib
%{_texmfdistdir}/bibtex/bst/harvard/agsm.bst
%{_texmfdistdir}/bibtex/bst/harvard/apsr.bst
%{_texmfdistdir}/bibtex/bst/harvard/dcu.bst
%{_texmfdistdir}/bibtex/bst/harvard/jmr.bst
%{_texmfdistdir}/bibtex/bst/harvard/jphysicsB.bst
%{_texmfdistdir}/bibtex/bst/harvard/kluwer.bst
%{_texmfdistdir}/bibtex/bst/harvard/nederlands.bst
%{_texmfdistdir}/tex/latex/harvard/harvard.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-harvard-%{texlive_version}.%{texlive_noarch}.2.0.5svn15878-%{release}-zypper
%endif

%package -n texlive-harveyballs
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32003
Release:        0
Summary:        Create Harvey Balls using TikZ
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
Recommends:     texlive-harveyballs-doc >= %{texlive_version}
Provides:       tex(harveyballs.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source211:      harveyballs.tar.xz
Source212:      harveyballs.doc.tar.xz

%description -n texlive-harveyballs
The package provides 5 commands (giving symbols that indicate
values from "none" to "full").

%package -n texlive-harveyballs-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32003
Release:        0
Summary:        Documentation for texlive-harveyballs
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-harveyballs-doc
This package includes the documentation for texlive-harveyballs

%post -n texlive-harveyballs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-harveyballs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-harveyballs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-harveyballs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/harveyballs/README
%{_texmfdistdir}/doc/latex/harveyballs/harveyballs-Manual.pdf
%{_texmfdistdir}/doc/latex/harveyballs/harveyballs-Manual.tex

%files -n texlive-harveyballs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/harveyballs/harveyballs.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-harveyballs-%{texlive_version}.%{texlive_noarch}.1.1svn32003-%{release}-zypper
%endif

%package -n texlive-harvmac
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Macros for scientific articles
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
Recommends:     texlive-harvmac-doc >= %{texlive_version}
Provides:       tex(harvmac.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source213:      harvmac.tar.xz
Source214:      harvmac.doc.tar.xz

%description -n texlive-harvmac
Known as 'Harvard macros', since written at that University.

%package -n texlive-harvmac-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-harvmac
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-harvmac-doc
This package includes the documentation for texlive-harvmac

%post -n texlive-harvmac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-harvmac 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-harvmac
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-harvmac-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/plain/harvmac/README
%{_texmfdistdir}/doc/plain/harvmac/harvsamp.tex

%files -n texlive-harvmac
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/plain/harvmac/harvmac.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-harvmac-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-hatching
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn23818
Release:        0
Summary:        MetaPost macros for hatching interior of closed paths
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
Recommends:     texlive-hatching-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source215:      hatching.tar.xz
Source216:      hatching.doc.tar.xz

%description -n texlive-hatching
The file hatching.mp contains a set of MetaPost macros for
hatching interior of closed paths. Examples of usage are
included.

%package -n texlive-hatching-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn23818
Release:        0
Summary:        Documentation for texlive-hatching
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hatching-doc
This package includes the documentation for texlive-hatching

%post -n texlive-hatching
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hatching 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hatching
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hatching-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/hatching/README
%{_texmfdistdir}/doc/metapost/hatching/htchuse.mp
%{_texmfdistdir}/doc/metapost/hatching/htchuse_.tex

%files -n texlive-hatching
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/hatching/hatching.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hatching-%{texlive_version}.%{texlive_noarch}.0.0.11svn23818-%{release}-zypper
%endif

%package -n texlive-hausarbeit-jura
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn50762
Release:        0
Summary:        Class for writing "juristische Hausarbeiten" at German Universities
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
Recommends:     texlive-hausarbeit-jura-doc >= %{texlive_version}
Provides:       tex(hausarbeit-jura.cls)
Requires:       tex(babel.sty)
Requires:       tex(courier.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(ellipsis.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(geometry.sty)
Requires:       tex(helvet.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(jurabib.sty)
Requires:       tex(jurabook.cls)
Requires:       tex(latexrelease.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(microtype.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(tgcursor.sty)
Requires:       tex(tgheros.sty)
Requires:       tex(tgtermes.sty)
Requires:       tex(varioref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source217:      hausarbeit-jura.tar.xz
Source218:      hausarbeit-jura.doc.tar.xz

%description -n texlive-hausarbeit-jura
The class was developed for use by students writing legal
essays ("juristische Hausarbeit") at German Universities. It is
based on jurabook and jurabib and makes it easy for LaTeX
beginners to get a correct and nicely formatted paper.

%package -n texlive-hausarbeit-jura-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn50762
Release:        0
Summary:        Documentation for texlive-hausarbeit-jura
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hausarbeit-jura-doc:de)

%description -n texlive-hausarbeit-jura-doc
This package includes the documentation for texlive-hausarbeit-jura

%post -n texlive-hausarbeit-jura
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hausarbeit-jura 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hausarbeit-jura
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hausarbeit-jura-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hausarbeit-jura/README.md
%{_texmfdistdir}/doc/latex/hausarbeit-jura/hausarbeit-demo.bib
%{_texmfdistdir}/doc/latex/hausarbeit-jura/hausarbeit-demo.tex
%{_texmfdistdir}/doc/latex/hausarbeit-jura/hausarbeit-jura.pdf

%files -n texlive-hausarbeit-jura
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hausarbeit-jura/hausarbeit-jura.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hausarbeit-jura-%{texlive_version}.%{texlive_noarch}.2.0svn50762-%{release}-zypper
%endif

%package -n texlive-havannah
Version:        %{texlive_version}.%{texlive_noarch}.svn36348
Release:        0
Summary:        Diagrams of board positions in the games of Havannah and Hex
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
Recommends:     texlive-havannah-doc >= %{texlive_version}
Provides:       tex(havannah.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source219:      havannah.tar.xz
Source220:      havannah.doc.tar.xz

%description -n texlive-havannah
This package defines macros for typesetting diagrams of board
positions in the games of Havannah and Hex.

%package -n texlive-havannah-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn36348
Release:        0
Summary:        Documentation for texlive-havannah
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-havannah-doc
This package includes the documentation for texlive-havannah

%post -n texlive-havannah
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-havannah 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-havannah
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-havannah-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/havannah/README
%{_texmfdistdir}/doc/latex/havannah/havannah.pdf

%files -n texlive-havannah
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/havannah/havannah.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-havannah-%{texlive_version}.%{texlive_noarch}.svn36348-%{release}-zypper
%endif

%package -n texlive-hc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Replacement for the LaTeX classes
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
Recommends:     texlive-hc-doc >= %{texlive_version}
Provides:       tex(hcart.cls)
Provides:       tex(hcletter.cls)
Provides:       tex(hcreport.cls)
Provides:       tex(hcslides.cls)
Requires:       tex(babel.sty)
Requires:       tex(fancybox.sty)
Requires:       tex(fancyref.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(mathpple.sty)
Requires:       tex(multicol.sty)
Requires:       tex(natbib.sty)
Requires:       tex(palatino.sty)
Requires:       tex(pifont.sty)
Requires:       tex(truncate.sty)
Requires:       tex(typearea.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source221:      hc.tar.xz
Source222:      hc.doc.tar.xz

%description -n texlive-hc
A set of replacements for the default LaTeX classes, based upon
the Koma-Script bundle and the seminar class. Includes hcart,
hcreport, hcletter, and hcslides.

%package -n texlive-hc-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-hc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hc-doc
This package includes the documentation for texlive-hc

%post -n texlive-hc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hc/COPYING
%{_texmfdistdir}/doc/latex/hc/FILES
%{_texmfdistdir}/doc/latex/hc/README
%{_texmfdistdir}/doc/latex/hc/hc.ps

%files -n texlive-hc
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/hc/hc-de.bst
%{_texmfdistdir}/bibtex/bst/hc/hc-en.bst
%{_texmfdistdir}/tex/latex/hc/german.hld
%{_texmfdistdir}/tex/latex/hc/hcart.cls
%{_texmfdistdir}/tex/latex/hc/hcletter.cls
%{_texmfdistdir}/tex/latex/hc/hcreport.cls
%{_texmfdistdir}/tex/latex/hc/hcslides.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hc-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-he-she
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn41359
Release:        0
Summary:        Alternating pronouns to aid gender-neutral writing
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
Recommends:     texlive-he-she-doc >= %{texlive_version}
Provides:       tex(he-she.sty)
Requires:       tex(everyhook.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source223:      he-she.tar.xz
Source224:      he-she.doc.tar.xz

%description -n texlive-he-she
The package implements a version of semi-automatic pronoun
switching for writing gender-neutral (and possibly annoying)
prose. It has upper- and lowercase versions of switching
pronouns for all case forms, plus anaphoric versions that
reflect the current gender choice.

%package -n texlive-he-she-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn41359
Release:        0
Summary:        Documentation for texlive-he-she
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-he-she-doc
This package includes the documentation for texlive-he-she

%post -n texlive-he-she
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-he-she 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-he-she
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-he-she-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/he-she/README
%{_texmfdistdir}/doc/latex/he-she/he-she.pdf
%{_texmfdistdir}/doc/latex/he-she/he-she.tex

%files -n texlive-he-she
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/he-she/he-she.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-he-she-%{texlive_version}.%{texlive_noarch}.1.3svn41359-%{release}-zypper
%endif

%package -n texlive-hecthese
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn50590
Release:        0
Summary:        A class for dissertations and theses at HEC Montreal
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
Recommends:     texlive-hecthese-doc >= %{texlive_version}
Provides:       tex(hecthese.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(babel.sty)
Requires:       tex(calc.sty)
Requires:       tex(chapterbib.sty)
Requires:       tex(color.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(memoir.cls)
Requires:       tex(natbib.sty)
Requires:       tex(numprint.sty)
Requires:       tex(tocvsec2.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source225:      hecthese.tar.xz
Source226:      hecthese.doc.tar.xz

%description -n texlive-hecthese
This package provides the hecthese class, a class based on
memoir and compatible with LaTeX. Using this class,
postgraduate students at HEC Montreal will be able to write
their dissertation or thesis while complying with all the
presentation standards required by the University. This class
is meant to be as flexible as possible; in particular, there
are very few hardcoded features except those that take care of
the document's layout. Dissertations and theses at HEC Montreal
can be written on a per-chapter or per-article basis. Documents
that are written on a per-article basis require a bibliography
for each of the included articles and a general bibliography
for the entire document. The hecthese class takes care of these
requirements. The class depends on babel, color, enumitem,
fontawesome, framed, numprint, url, and hyperref.

%package -n texlive-hecthese-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3.2svn50590
Release:        0
Summary:        Documentation for texlive-hecthese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hecthese-doc:en;fr)

%description -n texlive-hecthese-doc
This package includes the documentation for texlive-hecthese

%post -n texlive-hecthese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hecthese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hecthese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hecthese-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hecthese/README.md
%{_texmfdistdir}/doc/latex/hecthese/abstract-english.tex
%{_texmfdistdir}/doc/latex/hecthese/abstract-french.tex
%{_texmfdistdir}/doc/latex/hecthese/acknowledgements.tex
%{_texmfdistdir}/doc/latex/hecthese/acronym-list.tex
%{_texmfdistdir}/doc/latex/hecthese/annexe.tex
%{_texmfdistdir}/doc/latex/hecthese/appendix.tex
%{_texmfdistdir}/doc/latex/hecthese/article-1.tex
%{_texmfdistdir}/doc/latex/hecthese/article-2.tex
%{_texmfdistdir}/doc/latex/hecthese/article-3.tex
%{_texmfdistdir}/doc/latex/hecthese/avant-propos.tex
%{_texmfdistdir}/doc/latex/hecthese/cadre-theorique.tex
%{_texmfdistdir}/doc/latex/hecthese/chapitre-1.tex
%{_texmfdistdir}/doc/latex/hecthese/chapitre-2.tex
%{_texmfdistdir}/doc/latex/hecthese/chapitre-3.tex
%{_texmfdistdir}/doc/latex/hecthese/chapter-1.tex
%{_texmfdistdir}/doc/latex/hecthese/chapter-2.tex
%{_texmfdistdir}/doc/latex/hecthese/chapter-3.tex
%{_texmfdistdir}/doc/latex/hecthese/conclusion.tex
%{_texmfdistdir}/doc/latex/hecthese/dedicace.tex
%{_texmfdistdir}/doc/latex/hecthese/dedication.tex
%{_texmfdistdir}/doc/latex/hecthese/gabarit-memoire-articles.tex
%{_texmfdistdir}/doc/latex/hecthese/gabarit-memoire-classique.tex
%{_texmfdistdir}/doc/latex/hecthese/gabarit-these-articles.tex
%{_texmfdistdir}/doc/latex/hecthese/gabarit-these-classique.tex
%{_texmfdistdir}/doc/latex/hecthese/hecthese-en.pdf
%{_texmfdistdir}/doc/latex/hecthese/hecthese.pdf
%{_texmfdistdir}/doc/latex/hecthese/introduction.tex
%{_texmfdistdir}/doc/latex/hecthese/liste-abreviations.tex
%{_texmfdistdir}/doc/latex/hecthese/literature-review.tex
%{_texmfdistdir}/doc/latex/hecthese/preface.tex
%{_texmfdistdir}/doc/latex/hecthese/remerciements.tex
%{_texmfdistdir}/doc/latex/hecthese/resume-anglais.tex
%{_texmfdistdir}/doc/latex/hecthese/resume-francais.tex
%{_texmfdistdir}/doc/latex/hecthese/revue-litterature.tex
%{_texmfdistdir}/doc/latex/hecthese/template-msc-articles.tex
%{_texmfdistdir}/doc/latex/hecthese/template-msc-classic.tex
%{_texmfdistdir}/doc/latex/hecthese/template-phd-articles.tex
%{_texmfdistdir}/doc/latex/hecthese/template-phd-classic.tex
%{_texmfdistdir}/doc/latex/hecthese/theoretical-framework.tex

%files -n texlive-hecthese
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hecthese/hecthese.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hecthese-%{texlive_version}.%{texlive_noarch}.1.3.2svn50590-%{release}-zypper
%endif

%package -n texlive-helvetic
Version:        %{texlive_version}.%{texlive_noarch}.svn31835
Release:        0
Summary:        URW "Base 35" font pack for LaTeX
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
Requires:       texlive-helvetic-fonts >= %{texlive_version}
Provides:       tex(8ruhv.fd)
Provides:       tex(arb10u.tfm)
Provides:       tex(arb2n.tfm)
Provides:       tex(arb7j.tfm)
Provides:       tex(arb8u.tfm)
Provides:       tex(arb9t.tfm)
Provides:       tex(ari10u.tfm)
Provides:       tex(ari2n.tfm)
Provides:       tex(ari7j.tfm)
Provides:       tex(ari8u.tfm)
Provides:       tex(ari9t.tfm)
Provides:       tex(arj10u.tfm)
Provides:       tex(arj2n.tfm)
Provides:       tex(arj7j.tfm)
Provides:       tex(arj8u.tfm)
Provides:       tex(arj9t.tfm)
Provides:       tex(arr10u.tfm)
Provides:       tex(arr2n.tfm)
Provides:       tex(arr7j.tfm)
Provides:       tex(arr8u.tfm)
Provides:       tex(arr9t.tfm)
Provides:       tex(mhvb.tfm)
Provides:       tex(mhvb.vf)
Provides:       tex(mhvb8t.tfm)
Provides:       tex(mhvb8t.vf)
Provides:       tex(mhvbi.tfm)
Provides:       tex(mhvbi.vf)
Provides:       tex(mhvbi8t.tfm)
Provides:       tex(mhvbi8t.vf)
Provides:       tex(mhvr.tfm)
Provides:       tex(mhvr.vf)
Provides:       tex(mhvr8t.tfm)
Provides:       tex(mhvr8t.vf)
Provides:       tex(mhvri.tfm)
Provides:       tex(mhvri.vf)
Provides:       tex(mhvri8t.tfm)
Provides:       tex(mhvri8t.vf)
Provides:       tex(omluhv.fd)
Provides:       tex(omsuhv.fd)
Provides:       tex(ot1uhv.fd)
Provides:       tex(phvb.tfm)
Provides:       tex(phvb.vf)
Provides:       tex(phvb7t.tfm)
Provides:       tex(phvb7t.vf)
Provides:       tex(phvb7tn.tfm)
Provides:       tex(phvb7tn.vf)
Provides:       tex(phvb8c.tfm)
Provides:       tex(phvb8c.vf)
Provides:       tex(phvb8cn.tfm)
Provides:       tex(phvb8cn.vf)
Provides:       tex(phvb8r.tfm)
Provides:       tex(phvb8rn.tfm)
Provides:       tex(phvb8t.tfm)
Provides:       tex(phvb8t.vf)
Provides:       tex(phvb8tn.tfm)
Provides:       tex(phvb8tn.vf)
Provides:       tex(phvbc.tfm)
Provides:       tex(phvbc.vf)
Provides:       tex(phvbc7t.tfm)
Provides:       tex(phvbc7t.vf)
Provides:       tex(phvbc7tn.tfm)
Provides:       tex(phvbc7tn.vf)
Provides:       tex(phvbc8t.tfm)
Provides:       tex(phvbc8t.vf)
Provides:       tex(phvbc8tn.tfm)
Provides:       tex(phvbc8tn.vf)
Provides:       tex(phvbo.tfm)
Provides:       tex(phvbo.vf)
Provides:       tex(phvbo7t.tfm)
Provides:       tex(phvbo7t.vf)
Provides:       tex(phvbo7tn.tfm)
Provides:       tex(phvbo7tn.vf)
Provides:       tex(phvbo8c.tfm)
Provides:       tex(phvbo8c.vf)
Provides:       tex(phvbo8cn.tfm)
Provides:       tex(phvbo8cn.vf)
Provides:       tex(phvbo8r.tfm)
Provides:       tex(phvbo8rn.tfm)
Provides:       tex(phvbo8t.tfm)
Provides:       tex(phvbo8t.vf)
Provides:       tex(phvbo8tn.tfm)
Provides:       tex(phvbo8tn.vf)
Provides:       tex(phvbon.tfm)
Provides:       tex(phvbon.vf)
Provides:       tex(phvbrn.tfm)
Provides:       tex(phvbrn.vf)
Provides:       tex(phvr.tfm)
Provides:       tex(phvr.vf)
Provides:       tex(phvr7t.tfm)
Provides:       tex(phvr7t.vf)
Provides:       tex(phvr7tn.tfm)
Provides:       tex(phvr7tn.vf)
Provides:       tex(phvr8c.tfm)
Provides:       tex(phvr8c.vf)
Provides:       tex(phvr8cn.tfm)
Provides:       tex(phvr8cn.vf)
Provides:       tex(phvr8r.tfm)
Provides:       tex(phvr8rn.tfm)
Provides:       tex(phvr8t.tfm)
Provides:       tex(phvr8t.vf)
Provides:       tex(phvr8tn.tfm)
Provides:       tex(phvr8tn.vf)
Provides:       tex(phvrc.tfm)
Provides:       tex(phvrc.vf)
Provides:       tex(phvrc7t.tfm)
Provides:       tex(phvrc7t.vf)
Provides:       tex(phvrc7tn.tfm)
Provides:       tex(phvrc7tn.vf)
Provides:       tex(phvrc8t.tfm)
Provides:       tex(phvrc8t.vf)
Provides:       tex(phvrc8tn.tfm)
Provides:       tex(phvrc8tn.vf)
Provides:       tex(phvro.tfm)
Provides:       tex(phvro.vf)
Provides:       tex(phvro7t.tfm)
Provides:       tex(phvro7t.vf)
Provides:       tex(phvro7tn.tfm)
Provides:       tex(phvro7tn.vf)
Provides:       tex(phvro8c.tfm)
Provides:       tex(phvro8c.vf)
Provides:       tex(phvro8cn.tfm)
Provides:       tex(phvro8cn.vf)
Provides:       tex(phvro8r.tfm)
Provides:       tex(phvro8rn.tfm)
Provides:       tex(phvro8t.tfm)
Provides:       tex(phvro8t.vf)
Provides:       tex(phvro8tn.tfm)
Provides:       tex(phvro8tn.vf)
Provides:       tex(phvron.tfm)
Provides:       tex(phvron.vf)
Provides:       tex(phvrrn.tfm)
Provides:       tex(phvrrn.vf)
Provides:       tex(t1uhv.fd)
Provides:       tex(ts1uhv.fd)
Provides:       tex(uhv.map)
Provides:       tex(uhvb7t.tfm)
Provides:       tex(uhvb7t.vf)
Provides:       tex(uhvb7tn.tfm)
Provides:       tex(uhvb7tn.vf)
Provides:       tex(uhvb8c.tfm)
Provides:       tex(uhvb8c.vf)
Provides:       tex(uhvb8cn.tfm)
Provides:       tex(uhvb8cn.vf)
Provides:       tex(uhvb8r.tfm)
Provides:       tex(uhvb8rn.tfm)
Provides:       tex(uhvb8t.tfm)
Provides:       tex(uhvb8t.vf)
Provides:       tex(uhvb8tn.tfm)
Provides:       tex(uhvb8tn.vf)
Provides:       tex(uhvbc7t.tfm)
Provides:       tex(uhvbc7t.vf)
Provides:       tex(uhvbc7tn.tfm)
Provides:       tex(uhvbc7tn.vf)
Provides:       tex(uhvbc8t.tfm)
Provides:       tex(uhvbc8t.vf)
Provides:       tex(uhvbc8tn.tfm)
Provides:       tex(uhvbc8tn.vf)
Provides:       tex(uhvbi7t.tfm)
Provides:       tex(uhvbi7t.vf)
Provides:       tex(uhvbi8c.tfm)
Provides:       tex(uhvbi8c.vf)
Provides:       tex(uhvbi8r.tfm)
Provides:       tex(uhvbi8t.tfm)
Provides:       tex(uhvbi8t.vf)
Provides:       tex(uhvbo7t.tfm)
Provides:       tex(uhvbo7t.vf)
Provides:       tex(uhvbo7tn.tfm)
Provides:       tex(uhvbo7tn.vf)
Provides:       tex(uhvbo8c.tfm)
Provides:       tex(uhvbo8c.vf)
Provides:       tex(uhvbo8cn.tfm)
Provides:       tex(uhvbo8cn.vf)
Provides:       tex(uhvbo8r.tfm)
Provides:       tex(uhvbo8rn.tfm)
Provides:       tex(uhvbo8t.tfm)
Provides:       tex(uhvbo8t.vf)
Provides:       tex(uhvbo8tn.tfm)
Provides:       tex(uhvbo8tn.vf)
Provides:       tex(uhvr7t.tfm)
Provides:       tex(uhvr7t.vf)
Provides:       tex(uhvr7tn.tfm)
Provides:       tex(uhvr7tn.vf)
Provides:       tex(uhvr8c.tfm)
Provides:       tex(uhvr8c.vf)
Provides:       tex(uhvr8cn.tfm)
Provides:       tex(uhvr8cn.vf)
Provides:       tex(uhvr8r.tfm)
Provides:       tex(uhvr8rn.tfm)
Provides:       tex(uhvr8t.tfm)
Provides:       tex(uhvr8t.vf)
Provides:       tex(uhvr8tn.tfm)
Provides:       tex(uhvr8tn.vf)
Provides:       tex(uhvrc7t.tfm)
Provides:       tex(uhvrc7t.vf)
Provides:       tex(uhvrc7tn.tfm)
Provides:       tex(uhvrc7tn.vf)
Provides:       tex(uhvrc8t.tfm)
Provides:       tex(uhvrc8t.vf)
Provides:       tex(uhvrc8tn.tfm)
Provides:       tex(uhvrc8tn.vf)
Provides:       tex(uhvri7t.tfm)
Provides:       tex(uhvri7t.vf)
Provides:       tex(uhvri7tn.tfm)
Provides:       tex(uhvri7tn.vf)
Provides:       tex(uhvri8c.tfm)
Provides:       tex(uhvri8c.vf)
Provides:       tex(uhvri8cn.tfm)
Provides:       tex(uhvri8cn.vf)
Provides:       tex(uhvri8r.tfm)
Provides:       tex(uhvri8rn.tfm)
Provides:       tex(uhvri8t.tfm)
Provides:       tex(uhvri8t.vf)
Provides:       tex(uhvri8tn.tfm)
Provides:       tex(uhvri8tn.vf)
Provides:       tex(uhvro7t.tfm)
Provides:       tex(uhvro7t.vf)
Provides:       tex(uhvro7tn.tfm)
Provides:       tex(uhvro7tn.vf)
Provides:       tex(uhvro8c.tfm)
Provides:       tex(uhvro8c.vf)
Provides:       tex(uhvro8cn.tfm)
Provides:       tex(uhvro8cn.vf)
Provides:       tex(uhvro8r.tfm)
Provides:       tex(uhvro8rn.tfm)
Provides:       tex(uhvro8t.tfm)
Provides:       tex(uhvro8t.vf)
Provides:       tex(uhvro8tn.tfm)
Provides:       tex(uhvro8tn.vf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source227:      helvetic.tar.xz

%description -n texlive-helvetic
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

%package -n texlive-helvetic-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn31835
Release:        0
Summary:        Severed fonts for texlive-helvetic
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-helvetic-fonts
The  separated fonts package for texlive-helvetic
%post -n texlive-helvetic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap uhv.map' >> /var/run/texlive/run-updmap

%postun -n texlive-helvetic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap uhv.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-helvetic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-helvetic-fonts
%files -n texlive-helvetic
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/helvetic/config.uhv
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvb8an.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvbo8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvbo8an.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvr8an.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvro8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvro8an.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvb8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvb8ac.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvbo8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvbo8ac.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvr8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvr8ac.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvro8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvro8ac.afm
%{_texmfdistdir}/fonts/map/dvips/helvetic/uhv.map
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbon.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbrn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvron.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrrn.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvb.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvb8t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvbi.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvbi8t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvr.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvr8t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvri.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8tn.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8ac.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8ac.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8a-105.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8ac.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8a-105.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8ac.pfm
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbon.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbrn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvron.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrrn.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvb.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvb8t.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvbi.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvbi8t.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvr.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvr8t.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvri.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8tn.vf
%{_texmfdistdir}/tex/latex/helvetic/8ruhv.fd
%{_texmfdistdir}/tex/latex/helvetic/omluhv.fd
%{_texmfdistdir}/tex/latex/helvetic/omsuhv.fd
%{_texmfdistdir}/tex/latex/helvetic/ot1uhv.fd
%{_texmfdistdir}/tex/latex/helvetic/t1uhv.fd
%{_texmfdistdir}/tex/latex/helvetic/ts1uhv.fd

%files -n texlive-helvetic-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-helvetic
%{_datadir}/fontconfig/conf.avail/58-texlive-helvetic.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-helvetic/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-helvetic/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-helvetic/fonts.scale
%{_datadir}/fonts/texlive-helvetic/uhvb8a.pfb
%{_datadir}/fonts/texlive-helvetic/uhvb8ac.pfb
%{_datadir}/fonts/texlive-helvetic/uhvbo8a.pfb
%{_datadir}/fonts/texlive-helvetic/uhvbo8ac.pfb
%{_datadir}/fonts/texlive-helvetic/uhvr8a-105.pfb
%{_datadir}/fonts/texlive-helvetic/uhvr8a.pfb
%{_datadir}/fonts/texlive-helvetic/uhvr8ac.pfb
%{_datadir}/fonts/texlive-helvetic/uhvro8a-105.pfb
%{_datadir}/fonts/texlive-helvetic/uhvro8a.pfb
%{_datadir}/fonts/texlive-helvetic/uhvro8ac.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-helvetic-fonts-%{texlive_version}.%{texlive_noarch}.svn31835-%{release}-zypper
%endif

%package -n texlive-hep
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        A "convenience wrapper" for High Energy Physics packages
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
Recommends:     texlive-hep-doc >= %{texlive_version}
Provides:       tex(hep.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(braket.sty)
Requires:       tex(cancel.sty)
Requires:       tex(caption.sty)
Requires:       tex(ccaption.sty)
Requires:       tex(cite.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(feynmf.sty)
Requires:       tex(hepnicenames.sty)
Requires:       tex(hepunits.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(morefloats.sty)
Requires:       tex(setspace.sty)
Requires:       tex(slashed.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(tocbibind.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source228:      hep.tar.xz
Source229:      hep.doc.tar.xz

%description -n texlive-hep
Loads the author's hepunits and hepnicenames packages, and a
selection of others that are useful in High Energy Physics
papers, etc.

%package -n texlive-hep-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-hep
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hep-doc
This package includes the documentation for texlive-hep

%post -n texlive-hep
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hep 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hep
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hep-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hep/ChangeLog
%{_texmfdistdir}/doc/latex/hep/README

%files -n texlive-hep
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hep/hep.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hep-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-hep-paper
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn54300
Release:        0
Summary:        Publications in High Energy Physics
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
Recommends:     texlive-hep-paper-doc >= %{texlive_version}
Provides:       tex(hep-paper.sty)
Requires:       tex(alphabeta.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(authblk.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(everyhook.sty)
Requires:       tex(fixmath.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(foreign.sty)
Requires:       tex(geometry.sty)
Requires:       tex(glossaries-extra.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(microtype.sty)
Requires:       tex(multirow.sty)
Requires:       tex(parskip.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(physics.sty)
Requires:       tex(picture.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(relsize.sty)
Requires:       tex(sfmath.sty)
Requires:       tex(slashed.sty)
Requires:       tex(soul.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(units.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source230:      hep-paper.tar.xz
Source231:      hep-paper.doc.tar.xz

%description -n texlive-hep-paper
This package aims to provide a single style file containing
most configurations and macros necessary to write appealing
publications in High Energy Physics. Instead of reinventing the
wheel by introducing newly created macros, hep-paper preferably
loads third party packages as long as they are light-weight
enough. For usual publications it suffices to load the
hep-paper package, without optional arguments, in addition to
the article class.

%package -n texlive-hep-paper-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn54300
Release:        0
Summary:        Documentation for texlive-hep-paper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hep-paper-doc
This package includes the documentation for texlive-hep-paper

%post -n texlive-hep-paper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hep-paper 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hep-paper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hep-paper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hep-paper/README.md
%{_texmfdistdir}/doc/latex/hep-paper/bibliography.bib
%{_texmfdistdir}/doc/latex/hep-paper/hep-paper.pdf
%{_texmfdistdir}/doc/latex/hep-paper/license.md

%files -n texlive-hep-paper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hep-paper/hep-paper.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hep-paper-%{texlive_version}.%{texlive_noarch}.1.2svn54300-%{release}-zypper
%endif

%package -n texlive-hepnames
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn35722
Release:        0
Summary:        Pre-defined high energy particle names
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
Recommends:     texlive-hepnames-doc >= %{texlive_version}
Provides:       tex(hepnames.sty)
Provides:       tex(hepnicenames.sty)
Provides:       tex(heppennames.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(hepparticles.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source232:      hepnames.tar.xz
Source233:      hepnames.doc.tar.xz

%description -n texlive-hepnames
Hepnames provides a pair of LaTeX packages, heppennames and
hepnicenames, providing a large set of pre-defined high energy
physics particle names built with the hepparticles package. The
packages are based on pennames.sty by Michel Goosens and Eric
van Herwijnen. Heppennames re-implements the particle names in
pennames.sty, with some additions and alterations and greater
flexibility and robustness due to the hepparticles structures,
which were written for this purpose. Hepnicenames provides the
main non-resonant particle names from heppennames with more
"friendly" names.

%package -n texlive-hepnames-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn35722
Release:        0
Summary:        Documentation for texlive-hepnames
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hepnames-doc
This package includes the documentation for texlive-hepnames

%post -n texlive-hepnames
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hepnames 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hepnames
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hepnames-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hepnames/ChangeLog
%{_texmfdistdir}/doc/latex/hepnames/Makefile
%{_texmfdistdir}/doc/latex/hepnames/README
%{_texmfdistdir}/doc/latex/hepnames/hepnames.pdf
%{_texmfdistdir}/doc/latex/hepnames/hepnames.tex
%{_texmfdistdir}/doc/latex/hepnames/hepnicenames-it.pdf
%{_texmfdistdir}/doc/latex/hepnames/hepnicenames-it.tex
%{_texmfdistdir}/doc/latex/hepnames/hepnicenames-macros.tex
%{_texmfdistdir}/doc/latex/hepnames/hepnicenames-rm.pdf
%{_texmfdistdir}/doc/latex/hepnames/hepnicenames-rm.tex
%{_texmfdistdir}/doc/latex/hepnames/heppennames-it.pdf
%{_texmfdistdir}/doc/latex/hepnames/heppennames-it.tex
%{_texmfdistdir}/doc/latex/hepnames/heppennames-macros.tex
%{_texmfdistdir}/doc/latex/hepnames/heppennames-rm.pdf
%{_texmfdistdir}/doc/latex/hepnames/heppennames-rm.tex
%{_texmfdistdir}/doc/latex/hepnames/mkmacrotables

%files -n texlive-hepnames
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hepnames/hepnames.sty
%{_texmfdistdir}/tex/latex/hepnames/hepnicenames.sty
%{_texmfdistdir}/tex/latex/hepnames/heppennames.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hepnames-%{texlive_version}.%{texlive_noarch}.2.0svn35722-%{release}-zypper
%endif

%package -n texlive-hepparticles
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn35723
Release:        0
Summary:        Macros for typesetting high energy physics particle names
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
Recommends:     texlive-hepparticles-doc >= %{texlive_version}
Provides:       tex(hepparticles.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(subdepth.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source234:      hepparticles.tar.xz
Source235:      hepparticles.doc.tar.xz

%description -n texlive-hepparticles
HEPparticles is a set of macros for typesetting high energy
particle names, to meet the following criteria: 1. The main
particle name is a Roman or Greek symbol, to be typeset in
upright font in normal contexts. 2. Additionally a superscript
and/or subscript may follow the main symbol. 3. Particle
resonances may also have a resonance specifier which is typeset
in parentheses following the main symbol. In general the
parentheses may also be followed by sub- and superscripts. 4.
The particle names are expected to be used both in and out of
mathematical contexts. 5. If the surrounding text is bold or
italic then the particle name should adapt to that context as
best as possible (this may not be possible for Greek symbols).
A consequence of point 5 is that the well-known problems with
boldness of particle names in section titles, headers and
tables of contents automatically disappear if these macros are
used.

%package -n texlive-hepparticles-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn35723
Release:        0
Summary:        Documentation for texlive-hepparticles
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hepparticles-doc
This package includes the documentation for texlive-hepparticles

%post -n texlive-hepparticles
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hepparticles 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hepparticles
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hepparticles-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hepparticles/ChangeLog
%{_texmfdistdir}/doc/latex/hepparticles/README
%{_texmfdistdir}/doc/latex/hepparticles/hepparticles.pdf
%{_texmfdistdir}/doc/latex/hepparticles/hepparticles.tex
%{_texmfdistdir}/doc/latex/hepparticles/testhepparticles.pdf
%{_texmfdistdir}/doc/latex/hepparticles/testhepparticles.tex

%files -n texlive-hepparticles
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hepparticles/hepparticles.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hepparticles-%{texlive_version}.%{texlive_noarch}.2.0svn35723-%{release}-zypper
%endif

%package -n texlive-hepthesis
Version:        %{texlive_version}.%{texlive_noarch}.1.5.2svn46054
Release:        0
Summary:        A class for academic reports, especially PhD theses
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
Recommends:     texlive-hepthesis-doc >= %{texlive_version}
Provides:       tex(hepthesis.cls)
Requires:       tex(a4wide.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(changepage.sty)
Requires:       tex(comment.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(draftcopy.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(hep.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(lineno.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(microtype.sty)
Requires:       tex(rotating.sty)
Requires:       tex(scrbook.cls)
Requires:       tex(setspace.sty)
Requires:       tex(titling.sty)
Requires:       tex(tocbibind.sty)
Requires:       tex(varwidth.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source236:      hepthesis.tar.xz
Source237:      hepthesis.doc.tar.xz

%description -n texlive-hepthesis
Hepthesis is a LaTeX class for typesetting large academic
reports, in particular PhD theses. It was originally developed
for typesetting the author's high-energy physics PhD thesis and
includes some features specifically tailored to such an
application. In particular, hepthesis offers: Attractive
semantic environments for various rubric sections; Extensive
options for draft production, screen viewing and binding-ready
output; Helpful extensions of existing environments, including
equation and tabular; and Support for quotations at the start
of the thesis and each chapter. The class is based on scrbook,
from the KOMA-Script bundle.

%package -n texlive-hepthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5.2svn46054
Release:        0
Summary:        Documentation for texlive-hepthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hepthesis-doc
This package includes the documentation for texlive-hepthesis

%post -n texlive-hepthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hepthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hepthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hepthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hepthesis/ChangeLog
%{_texmfdistdir}/doc/latex/hepthesis/Makefile
%{_texmfdistdir}/doc/latex/hepthesis/README
%{_texmfdistdir}/doc/latex/hepthesis/TODO
%{_texmfdistdir}/doc/latex/hepthesis/example/Makefile
%{_texmfdistdir}/doc/latex/hepthesis/example/appendices.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/backmatter.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/chap1.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/chap2.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/chap3.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/ckmfitter-alpha-combined.pdf
%{_texmfdistdir}/doc/latex/hepthesis/example/example.pdf
%{_texmfdistdir}/doc/latex/hepthesis/example/example.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/extrastyles.zip
%{_texmfdistdir}/doc/latex/hepthesis/example/frontmatter.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/getNewBibtex
%{_texmfdistdir}/doc/latex/hepthesis/example/h-physrev.bst
%{_texmfdistdir}/doc/latex/hepthesis/example/lhcb-detector-cross-section.pdf
%{_texmfdistdir}/doc/latex/hepthesis/example/mwe.tex
%{_texmfdistdir}/doc/latex/hepthesis/example/mythesis.bib
%{_texmfdistdir}/doc/latex/hepthesis/example/mythesismath.sty
%{_texmfdistdir}/doc/latex/hepthesis/example/preamble.tex
%{_texmfdistdir}/doc/latex/hepthesis/hepthesis.pdf
%{_texmfdistdir}/doc/latex/hepthesis/hepthesis.tex

%files -n texlive-hepthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hepthesis/hepthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hepthesis-%{texlive_version}.%{texlive_noarch}.1.5.2svn46054-%{release}-zypper
%endif

%package -n texlive-hepunits
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn54758
Release:        0
Summary:        A set of units useful in high energy physics applications
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
Recommends:     texlive-hepunits-doc >= %{texlive_version}
Provides:       tex(hepunits.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(siunitx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source238:      hepunits.tar.xz
Source239:      hepunits.doc.tar.xz

%description -n texlive-hepunits
Hepunits is a LaTeX package built on the SIunits package which
adds a collection of useful HEP units to the existing SIunits
set. These include the energy units \MeV, \GeV, \TeV and the
derived momentum and mass units \MeVoverc, \MeVovercsq and so
on.

%package -n texlive-hepunits-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.0svn54758
Release:        0
Summary:        Documentation for texlive-hepunits
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hepunits-doc
This package includes the documentation for texlive-hepunits

%post -n texlive-hepunits
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hepunits 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hepunits
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hepunits-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hepunits/ChangeLog
%{_texmfdistdir}/doc/latex/hepunits/README
%{_texmfdistdir}/doc/latex/hepunits/hepunits.pdf
%{_texmfdistdir}/doc/latex/hepunits/hepunits.tex

%files -n texlive-hepunits
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hepunits/hepunits.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hepunits-%{texlive_version}.%{texlive_noarch}.2.0.0svn54758-%{release}-zypper
%endif

%package -n texlive-here
Version:        %{texlive_version}.%{texlive_noarch}.svn16135
Release:        0
Summary:        Emulation of obsolete package for "here" floats
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
Recommends:     texlive-here-doc >= %{texlive_version}
Provides:       tex(here.sty)
Requires:       tex(float.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source240:      here.tar.xz
Source241:      here.doc.tar.xz

%description -n texlive-here
Provides the H option for floats in LaTeX to signify that the
environment is not really a float (and should therefore be
placed "here" and not float at all). The package emulates an
older package of the same name, which has long been suppressed
by its author. The job is done by nothing more than loading the
float package, which has long provided the option in an
acceptable framework.

%package -n texlive-here-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn16135
Release:        0
Summary:        Documentation for texlive-here
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-here-doc
This package includes the documentation for texlive-here

%post -n texlive-here
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-here 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-here
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-here-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/here/README

%files -n texlive-here
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/here/here.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-here-%{texlive_version}.%{texlive_noarch}.svn16135-%{release}-zypper
%endif

%package -n texlive-heuristica
Version:        %{texlive_version}.%{texlive_noarch}.1.092svn51362
Release:        0
Summary:        Fonts extending Utopia, with LaTeX support files
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
Requires:       texlive-heuristica-fonts >= %{texlive_version}
Recommends:     texlive-heuristica-doc >= %{texlive_version}
Provides:       tex(Heuristica-Bold-inf-ly1.tfm)
Provides:       tex(Heuristica-Bold-inf-t1--base.tfm)
Provides:       tex(Heuristica-Bold-inf-t1.tfm)
Provides:       tex(Heuristica-Bold-inf-t1.vf)
Provides:       tex(Heuristica-Bold-inf-t2a.tfm)
Provides:       tex(Heuristica-Bold-inf-t2b.tfm)
Provides:       tex(Heuristica-Bold-inf-t2c.tfm)
Provides:       tex(Heuristica-Bold-sup-ly1.tfm)
Provides:       tex(Heuristica-Bold-sup-t1--base.tfm)
Provides:       tex(Heuristica-Bold-sup-t1.tfm)
Provides:       tex(Heuristica-Bold-sup-t1.vf)
Provides:       tex(Heuristica-Bold-sup-t2a.tfm)
Provides:       tex(Heuristica-Bold-sup-t2b.tfm)
Provides:       tex(Heuristica-Bold-sup-t2c.tfm)
Provides:       tex(Heuristica-Bold-tlf-ly1.tfm)
Provides:       tex(Heuristica-Bold-tlf-t1--base.tfm)
Provides:       tex(Heuristica-Bold-tlf-t1.tfm)
Provides:       tex(Heuristica-Bold-tlf-t1.vf)
Provides:       tex(Heuristica-Bold-tlf-t2a.tfm)
Provides:       tex(Heuristica-Bold-tlf-t2b.tfm)
Provides:       tex(Heuristica-Bold-tlf-t2c.tfm)
Provides:       tex(Heuristica-Bold-tlf-ts1--base.tfm)
Provides:       tex(Heuristica-Bold-tlf-ts1.tfm)
Provides:       tex(Heuristica-Bold-tlf-ts1.vf)
Provides:       tex(Heuristica-Bold-tosf-ly1.tfm)
Provides:       tex(Heuristica-Bold-tosf-t1--base.tfm)
Provides:       tex(Heuristica-Bold-tosf-t1.tfm)
Provides:       tex(Heuristica-Bold-tosf-t1.vf)
Provides:       tex(Heuristica-Bold-tosf-t2a.tfm)
Provides:       tex(Heuristica-Bold-tosf-t2b.tfm)
Provides:       tex(Heuristica-Bold-tosf-t2c.tfm)
Provides:       tex(Heuristica-Bold-tosf-ts1--base.tfm)
Provides:       tex(Heuristica-Bold-tosf-ts1.tfm)
Provides:       tex(Heuristica-Bold-tosf-ts1.vf)
Provides:       tex(Heuristica-BoldItalic-inf-ly1.tfm)
Provides:       tex(Heuristica-BoldItalic-inf-t1--base.tfm)
Provides:       tex(Heuristica-BoldItalic-inf-t1.tfm)
Provides:       tex(Heuristica-BoldItalic-inf-t1.vf)
Provides:       tex(Heuristica-BoldItalic-inf-t2a.tfm)
Provides:       tex(Heuristica-BoldItalic-inf-t2b.tfm)
Provides:       tex(Heuristica-BoldItalic-inf-t2c.tfm)
Provides:       tex(Heuristica-BoldItalic-sup-ly1.tfm)
Provides:       tex(Heuristica-BoldItalic-sup-t1--base.tfm)
Provides:       tex(Heuristica-BoldItalic-sup-t1.tfm)
Provides:       tex(Heuristica-BoldItalic-sup-t1.vf)
Provides:       tex(Heuristica-BoldItalic-sup-t2a.tfm)
Provides:       tex(Heuristica-BoldItalic-sup-t2b.tfm)
Provides:       tex(Heuristica-BoldItalic-sup-t2c.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-ly1.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-t1.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-t1.vf)
Provides:       tex(Heuristica-BoldItalic-tlf-t2a.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-t2b.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-t2c.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-ts1.tfm)
Provides:       tex(Heuristica-BoldItalic-tlf-ts1.vf)
Provides:       tex(Heuristica-BoldItalic-tosf-ly1.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-t1.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-t1.vf)
Provides:       tex(Heuristica-BoldItalic-tosf-t2a.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-t2b.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-t2c.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-ts1.tfm)
Provides:       tex(Heuristica-BoldItalic-tosf-ts1.vf)
Provides:       tex(Heuristica-Italic-inf-ly1.tfm)
Provides:       tex(Heuristica-Italic-inf-t1--base.tfm)
Provides:       tex(Heuristica-Italic-inf-t1.tfm)
Provides:       tex(Heuristica-Italic-inf-t1.vf)
Provides:       tex(Heuristica-Italic-inf-t2a.tfm)
Provides:       tex(Heuristica-Italic-inf-t2b.tfm)
Provides:       tex(Heuristica-Italic-inf-t2c.tfm)
Provides:       tex(Heuristica-Italic-sup-ly1.tfm)
Provides:       tex(Heuristica-Italic-sup-t1--base.tfm)
Provides:       tex(Heuristica-Italic-sup-t1.tfm)
Provides:       tex(Heuristica-Italic-sup-t1.vf)
Provides:       tex(Heuristica-Italic-sup-t2a.tfm)
Provides:       tex(Heuristica-Italic-sup-t2b.tfm)
Provides:       tex(Heuristica-Italic-sup-t2c.tfm)
Provides:       tex(Heuristica-Italic-tlf-ly1.tfm)
Provides:       tex(Heuristica-Italic-tlf-t1--base.tfm)
Provides:       tex(Heuristica-Italic-tlf-t1.tfm)
Provides:       tex(Heuristica-Italic-tlf-t1.vf)
Provides:       tex(Heuristica-Italic-tlf-t2a.tfm)
Provides:       tex(Heuristica-Italic-tlf-t2b.tfm)
Provides:       tex(Heuristica-Italic-tlf-t2c.tfm)
Provides:       tex(Heuristica-Italic-tlf-ts1--base.tfm)
Provides:       tex(Heuristica-Italic-tlf-ts1.tfm)
Provides:       tex(Heuristica-Italic-tlf-ts1.vf)
Provides:       tex(Heuristica-Italic-tosf-ly1.tfm)
Provides:       tex(Heuristica-Italic-tosf-t1--base.tfm)
Provides:       tex(Heuristica-Italic-tosf-t1.tfm)
Provides:       tex(Heuristica-Italic-tosf-t1.vf)
Provides:       tex(Heuristica-Italic-tosf-t2a.tfm)
Provides:       tex(Heuristica-Italic-tosf-t2b.tfm)
Provides:       tex(Heuristica-Italic-tosf-t2c.tfm)
Provides:       tex(Heuristica-Italic-tosf-ts1--base.tfm)
Provides:       tex(Heuristica-Italic-tosf-ts1.tfm)
Provides:       tex(Heuristica-Italic-tosf-ts1.vf)
Provides:       tex(Heuristica-Regular-inf-ly1.tfm)
Provides:       tex(Heuristica-Regular-inf-t1--base.tfm)
Provides:       tex(Heuristica-Regular-inf-t1.tfm)
Provides:       tex(Heuristica-Regular-inf-t1.vf)
Provides:       tex(Heuristica-Regular-inf-t2a.tfm)
Provides:       tex(Heuristica-Regular-inf-t2b.tfm)
Provides:       tex(Heuristica-Regular-inf-t2c.tfm)
Provides:       tex(Heuristica-Regular-sup-ly1.tfm)
Provides:       tex(Heuristica-Regular-sup-t1--base.tfm)
Provides:       tex(Heuristica-Regular-sup-t1.tfm)
Provides:       tex(Heuristica-Regular-sup-t1.vf)
Provides:       tex(Heuristica-Regular-sup-t2a.tfm)
Provides:       tex(Heuristica-Regular-sup-t2b.tfm)
Provides:       tex(Heuristica-Regular-sup-t2c.tfm)
Provides:       tex(Heuristica-Regular-tlf-ly1.tfm)
Provides:       tex(Heuristica-Regular-tlf-sc-ly1--base.tfm)
Provides:       tex(Heuristica-Regular-tlf-sc-ly1.tfm)
Provides:       tex(Heuristica-Regular-tlf-sc-ly1.vf)
Provides:       tex(Heuristica-Regular-tlf-sc-t1--base.tfm)
Provides:       tex(Heuristica-Regular-tlf-sc-t1.tfm)
Provides:       tex(Heuristica-Regular-tlf-sc-t1.vf)
Provides:       tex(Heuristica-Regular-tlf-sc-t2a.tfm)
Provides:       tex(Heuristica-Regular-tlf-sc-t2b.tfm)
Provides:       tex(Heuristica-Regular-tlf-sc-t2c.tfm)
Provides:       tex(Heuristica-Regular-tlf-t1--base.tfm)
Provides:       tex(Heuristica-Regular-tlf-t1.tfm)
Provides:       tex(Heuristica-Regular-tlf-t1.vf)
Provides:       tex(Heuristica-Regular-tlf-t2a.tfm)
Provides:       tex(Heuristica-Regular-tlf-t2b.tfm)
Provides:       tex(Heuristica-Regular-tlf-t2c.tfm)
Provides:       tex(Heuristica-Regular-tlf-ts1--base.tfm)
Provides:       tex(Heuristica-Regular-tlf-ts1.tfm)
Provides:       tex(Heuristica-Regular-tlf-ts1.vf)
Provides:       tex(Heuristica-Regular-tosf-ly1.tfm)
Provides:       tex(Heuristica-Regular-tosf-sc-ly1--base.tfm)
Provides:       tex(Heuristica-Regular-tosf-sc-ly1.tfm)
Provides:       tex(Heuristica-Regular-tosf-sc-ly1.vf)
Provides:       tex(Heuristica-Regular-tosf-sc-t1--base.tfm)
Provides:       tex(Heuristica-Regular-tosf-sc-t1.tfm)
Provides:       tex(Heuristica-Regular-tosf-sc-t1.vf)
Provides:       tex(Heuristica-Regular-tosf-sc-t2a.tfm)
Provides:       tex(Heuristica-Regular-tosf-sc-t2b.tfm)
Provides:       tex(Heuristica-Regular-tosf-sc-t2c.tfm)
Provides:       tex(Heuristica-Regular-tosf-t1--base.tfm)
Provides:       tex(Heuristica-Regular-tosf-t1.tfm)
Provides:       tex(Heuristica-Regular-tosf-t1.vf)
Provides:       tex(Heuristica-Regular-tosf-t2a.tfm)
Provides:       tex(Heuristica-Regular-tosf-t2b.tfm)
Provides:       tex(Heuristica-Regular-tosf-t2c.tfm)
Provides:       tex(Heuristica-Regular-tosf-ts1--base.tfm)
Provides:       tex(Heuristica-Regular-tosf-ts1.tfm)
Provides:       tex(Heuristica-Regular-tosf-ts1.vf)
Provides:       tex(Heuristica.map)
Provides:       tex(LY1Heuristica-Inf.fd)
Provides:       tex(LY1Heuristica-Sup.fd)
Provides:       tex(LY1Heuristica-TLF.fd)
Provides:       tex(LY1Heuristica-TOsF.fd)
Provides:       tex(T1Heuristica-Inf.fd)
Provides:       tex(T1Heuristica-Sup.fd)
Provides:       tex(T1Heuristica-TLF.fd)
Provides:       tex(T1Heuristica-TOsF.fd)
Provides:       tex(T2AHeuristica-Inf.fd)
Provides:       tex(T2AHeuristica-Sup.fd)
Provides:       tex(T2AHeuristica-TLF.fd)
Provides:       tex(T2AHeuristica-TOsF.fd)
Provides:       tex(T2BHeuristica-Inf.fd)
Provides:       tex(T2BHeuristica-Sup.fd)
Provides:       tex(T2BHeuristica-TLF.fd)
Provides:       tex(T2BHeuristica-TOsF.fd)
Provides:       tex(T2CHeuristica-Inf.fd)
Provides:       tex(T2CHeuristica-Sup.fd)
Provides:       tex(T2CHeuristica-TLF.fd)
Provides:       tex(T2CHeuristica-TOsF.fd)
Provides:       tex(TS1Heuristica-TLF.fd)
Provides:       tex(TS1Heuristica-TOsF.fd)
Provides:       tex(heuristica.sty)
Provides:       tex(zut_5b7xz5.enc)
Provides:       tex(zut_bavnqe.enc)
Provides:       tex(zut_ckaykl.enc)
Provides:       tex(zut_cq6rqq.enc)
Provides:       tex(zut_cvig5d.enc)
Provides:       tex(zut_d3dvo4.enc)
Provides:       tex(zut_dcwkkw.enc)
Provides:       tex(zut_dhvb6d.enc)
Provides:       tex(zut_dvh2xl.enc)
Provides:       tex(zut_e7tlds.enc)
Provides:       tex(zut_edf5gu.enc)
Provides:       tex(zut_etrbro.enc)
Provides:       tex(zut_evgarn.enc)
Provides:       tex(zut_f5n2rf.enc)
Provides:       tex(zut_fc3mov.enc)
Provides:       tex(zut_flhghs.enc)
Provides:       tex(zut_g4w54e.enc)
Provides:       tex(zut_geqeyh.enc)
Provides:       tex(zut_hbxdik.enc)
Provides:       tex(zut_hln2hy.enc)
Provides:       tex(zut_hvy566.enc)
Provides:       tex(zut_ijw3px.enc)
Provides:       tex(zut_it5nv3.enc)
Provides:       tex(zut_j3hjx2.enc)
Provides:       tex(zut_k42udk.enc)
Provides:       tex(zut_n2gc2n.enc)
Provides:       tex(zut_nvi5ys.enc)
Provides:       tex(zut_qy67bk.enc)
Provides:       tex(zut_rhmrtx.enc)
Provides:       tex(zut_rutxxy.enc)
Provides:       tex(zut_tfeu3y.enc)
Provides:       tex(zut_thxlbm.enc)
Provides:       tex(zut_tsvs4d.enc)
Provides:       tex(zut_u7pc6m.enc)
Provides:       tex(zut_ul3ofd.enc)
Provides:       tex(zut_v7it2w.enc)
Provides:       tex(zut_vaioc2.enc)
Provides:       tex(zut_vtjod4.enc)
Provides:       tex(zut_ysltpx.enc)
Provides:       tex(zut_zk7stm.enc)
Provides:       tex(zut_zl5g24.enc)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source242:      heuristica.tar.xz
Source243:      heuristica.doc.tar.xz

%description -n texlive-heuristica
The fonts extend the utopia set with Cyrillic glyphs,
additional figure styles, ligatures and Small Caps in Regular
style only. Macro support, and maths fonts that match the
Utopia family, are provided by the Fourier and the Mathdesign
font packages.

%package -n texlive-heuristica-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.092svn51362
Release:        0
Summary:        Documentation for texlive-heuristica
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-heuristica-doc
This package includes the documentation for texlive-heuristica


%package -n texlive-heuristica-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.092svn51362
Release:        0
Summary:        Severed fonts for texlive-heuristica
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-heuristica-fonts
The  separated fonts package for texlive-heuristica
%post -n texlive-heuristica
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap Heuristica.map' >> /var/run/texlive/run-updmap

%postun -n texlive-heuristica 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap Heuristica.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-heuristica
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-heuristica-fonts
%files -n texlive-heuristica-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/heuristica/FontLog.txt
%{_texmfdistdir}/doc/fonts/heuristica/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/heuristica/OFL.txt
%{_texmfdistdir}/doc/fonts/heuristica/README
%{_texmfdistdir}/doc/fonts/heuristica/heuristica-doc.pdf
%{_texmfdistdir}/doc/fonts/heuristica/heuristica-doc.tex

%files -n texlive-heuristica
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_5b7xz5.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_bavnqe.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_ckaykl.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_cq6rqq.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_cvig5d.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_d3dvo4.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_dcwkkw.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_dhvb6d.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_dvh2xl.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_e7tlds.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_edf5gu.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_etrbro.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_evgarn.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_f5n2rf.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_fc3mov.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_flhghs.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_g4w54e.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_geqeyh.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_hbxdik.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_hln2hy.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_hvy566.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_ijw3px.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_it5nv3.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_j3hjx2.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_k42udk.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_n2gc2n.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_nvi5ys.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_qy67bk.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_rhmrtx.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_rutxxy.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_tfeu3y.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_thxlbm.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_tsvs4d.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_u7pc6m.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_ul3ofd.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_v7it2w.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_vaioc2.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_vtjod4.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_ysltpx.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_zk7stm.enc
%{_texmfdistdir}/fonts/enc/dvips/heuristica/zut_zl5g24.enc
%{_texmfdistdir}/fonts/map/dvips/heuristica/Heuristica.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/heuristica/Heuristica-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-sc-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-sc-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/heuristica/Heuristica-Regular-tosf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/heuristica/Heuristica-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/heuristica/Heuristica-Regular-tosf-ts1.vf
%{_texmfdistdir}/tex/latex/heuristica/LY1Heuristica-Inf.fd
%{_texmfdistdir}/tex/latex/heuristica/LY1Heuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/LY1Heuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/LY1Heuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T1Heuristica-Inf.fd
%{_texmfdistdir}/tex/latex/heuristica/T1Heuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T1Heuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T1Heuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2AHeuristica-Inf.fd
%{_texmfdistdir}/tex/latex/heuristica/T2AHeuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T2AHeuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2AHeuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2BHeuristica-Inf.fd
%{_texmfdistdir}/tex/latex/heuristica/T2BHeuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T2BHeuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2BHeuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2CHeuristica-Inf.fd
%{_texmfdistdir}/tex/latex/heuristica/T2CHeuristica-Sup.fd
%{_texmfdistdir}/tex/latex/heuristica/T2CHeuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/T2CHeuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/TS1Heuristica-TLF.fd
%{_texmfdistdir}/tex/latex/heuristica/TS1Heuristica-TOsF.fd
%{_texmfdistdir}/tex/latex/heuristica/heuristica.fontspec
%{_texmfdistdir}/tex/latex/heuristica/heuristica.sty

%files -n texlive-heuristica-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-heuristica
%{_datadir}/fontconfig/conf.avail/58-texlive-heuristica.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-heuristica.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-heuristica.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-heuristica/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-heuristica/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-heuristica/fonts.scale
%{_datadir}/fonts/texlive-heuristica/Heuristica-Bold.otf
%{_datadir}/fonts/texlive-heuristica/Heuristica-BoldItalic.otf
%{_datadir}/fonts/texlive-heuristica/Heuristica-Italic.otf
%{_datadir}/fonts/texlive-heuristica/Heuristica-Regular.otf
%{_datadir}/fonts/texlive-heuristica/Heuristica-Bold.pfb
%{_datadir}/fonts/texlive-heuristica/Heuristica-BoldItalic.pfb
%{_datadir}/fonts/texlive-heuristica/Heuristica-Italic.pfb
%{_datadir}/fonts/texlive-heuristica/Heuristica-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-heuristica-fonts-%{texlive_version}.%{texlive_noarch}.1.092svn51362-%{release}-zypper
%endif

%package -n texlive-hexgame
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Provide an environment to draw a hexgame-board
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
Recommends:     texlive-hexgame-doc >= %{texlive_version}
Provides:       tex(hexgame.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-poly.sty)
Requires:       tex(pstcol.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source244:      hexgame.tar.xz
Source245:      hexgame.doc.tar.xz

%description -n texlive-hexgame
Hex is a mathematical game invented by the Danish mathematician
Piet Hein and independently by the mathematician John Nash.
This package defines an environment that enables the user to
draw such a game in a trivial way.

%package -n texlive-hexgame-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-hexgame
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hexgame-doc
This package includes the documentation for texlive-hexgame

%post -n texlive-hexgame
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hexgame 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hexgame
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hexgame-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hexgame/README
%{_texmfdistdir}/doc/latex/hexgame/hexgame.pdf
%{_texmfdistdir}/doc/latex/hexgame/hexgame.tex

%files -n texlive-hexgame
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hexgame/hexgame.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hexgame-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-hf-tikz
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3asvn34733
Release:        0
Summary:        A simple way to highlight formulas and formula parts
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
Recommends:     texlive-hf-tikz-doc >= %{texlive_version}
Provides:       tex(hf-tikz.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source246:      hf-tikz.tar.xz
Source247:      hf-tikz.doc.tar.xz

%description -n texlive-hf-tikz
The package provides a way to highlight formulas and formula
parts in both documents and presentations, us TikZ.

%package -n texlive-hf-tikz-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3asvn34733
Release:        0
Summary:        Documentation for texlive-hf-tikz
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hf-tikz-doc
This package includes the documentation for texlive-hf-tikz

%post -n texlive-hf-tikz
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hf-tikz 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hf-tikz
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hf-tikz-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hf-tikz/README
%{_texmfdistdir}/doc/latex/hf-tikz/hf-tikz.pdf

%files -n texlive-hf-tikz
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hf-tikz/hf-tikz.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hf-tikz-%{texlive_version}.%{texlive_noarch}.0.0.3asvn34733-%{release}-zypper
%endif

%package -n texlive-hfbright
Version:        %{texlive_version}.%{texlive_noarch}.svn29349
Release:        0
Summary:        The hfbright fonts
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
Requires:       texlive-hfbright-fonts >= %{texlive_version}
Recommends:     texlive-hfbright-doc >= %{texlive_version}
Provides:       tex(hfbright.map)
Provides:       tex(hfmital.enc)
Provides:       tex(hfmsa.enc)
Provides:       tex(hfmsb.enc)
Provides:       tex(hfmsym.enc)
Provides:       tex(hfot1.enc)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source248:      hfbright.tar.xz
Source249:      hfbright.doc.tar.xz

%description -n texlive-hfbright
These are Adobe Type 1 versions of the OT1-encoded and maths
parts of the Computer Modern Bright fonts.

%package -n texlive-hfbright-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn29349
Release:        0
Summary:        Documentation for texlive-hfbright
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hfbright-doc
This package includes the documentation for texlive-hfbright


%package -n texlive-hfbright-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn29349
Release:        0
Summary:        Severed fonts for texlive-hfbright
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-hfbright-fonts
The  separated fonts package for texlive-hfbright
%post -n texlive-hfbright
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMixedMap hfbright.map' >> /var/run/texlive/run-updmap

%postun -n texlive-hfbright 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMixedMap hfbright.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-hfbright
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-hfbright-fonts
%files -n texlive-hfbright-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/hfbright/README
%{_texmfdistdir}/doc/fonts/hfbright/config.hfbright
%{_texmfdistdir}/doc/fonts/hfbright/generate.sh
%{_texmfdistdir}/doc/fonts/hfbright/install.sh
%{_texmfdistdir}/doc/fonts/hfbright/simplify-rename.pe

%files -n texlive-hfbright
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr17.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbr9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbras10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbras8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbras9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbs10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbs8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbs9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrbx10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmb10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmi10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmi8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrmi9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl17.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsl9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsy10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsy8.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfbrsy9.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hfsltl10.afm
%{_texmfdistdir}/fonts/afm/public/hfbright/hftl10.afm
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmital.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmsa.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmsb.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfmsym.enc
%{_texmfdistdir}/fonts/enc/dvips/hfbright/hfot1.enc
%{_texmfdistdir}/fonts/map/dvips/hfbright/hfbright.map
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbr10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbr17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbr8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbr9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbras10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbras8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbras9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbs8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbs9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmi8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrmi9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsl9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsy10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsy8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfbrsy9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hfsltl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/hfbright/hftl10.pfb

%files -n texlive-hfbright-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-hfbright
%{_datadir}/fontconfig/conf.avail/58-texlive-hfbright.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hfbright/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hfbright/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hfbright/fonts.scale
%{_datadir}/fonts/texlive-hfbright/hfbr10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbr17.pfb
%{_datadir}/fonts/texlive-hfbright/hfbr8.pfb
%{_datadir}/fonts/texlive-hfbright/hfbr9.pfb
%{_datadir}/fonts/texlive-hfbright/hfbras10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbras8.pfb
%{_datadir}/fonts/texlive-hfbright/hfbras9.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrbs10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrbs8.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrbs9.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrbx10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrmb10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrmi10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrmi8.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrmi9.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrsl10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrsl17.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrsl8.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrsl9.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrsy10.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrsy8.pfb
%{_datadir}/fonts/texlive-hfbright/hfbrsy9.pfb
%{_datadir}/fonts/texlive-hfbright/hfsltl10.pfb
%{_datadir}/fonts/texlive-hfbright/hftl10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hfbright-fonts-%{texlive_version}.%{texlive_noarch}.svn29349-%{release}-zypper
%endif

%package -n texlive-hfoldsty
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn29349
Release:        0
Summary:        Old style numerals with EC fonts
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
Recommends:     texlive-hfoldsty-doc >= %{texlive_version}
Provides:       tex(hfobi0500.tfm)
Provides:       tex(hfobi0500.vf)
Provides:       tex(hfobi0600.tfm)
Provides:       tex(hfobi0600.vf)
Provides:       tex(hfobi0700.tfm)
Provides:       tex(hfobi0700.vf)
Provides:       tex(hfobi0800.tfm)
Provides:       tex(hfobi0800.vf)
Provides:       tex(hfobi0900.tfm)
Provides:       tex(hfobi0900.vf)
Provides:       tex(hfobi1000.tfm)
Provides:       tex(hfobi1000.vf)
Provides:       tex(hfobi1095.tfm)
Provides:       tex(hfobi1095.vf)
Provides:       tex(hfobi1200.tfm)
Provides:       tex(hfobi1200.vf)
Provides:       tex(hfobi1440.tfm)
Provides:       tex(hfobi1440.vf)
Provides:       tex(hfobi1728.tfm)
Provides:       tex(hfobi1728.vf)
Provides:       tex(hfobi2074.tfm)
Provides:       tex(hfobi2074.vf)
Provides:       tex(hfobi2488.tfm)
Provides:       tex(hfobi2488.vf)
Provides:       tex(hfobi2986.tfm)
Provides:       tex(hfobi2986.vf)
Provides:       tex(hfobi3583.tfm)
Provides:       tex(hfobi3583.vf)
Provides:       tex(hfobl0500.tfm)
Provides:       tex(hfobl0500.vf)
Provides:       tex(hfobl0600.tfm)
Provides:       tex(hfobl0600.vf)
Provides:       tex(hfobl0700.tfm)
Provides:       tex(hfobl0700.vf)
Provides:       tex(hfobl0800.tfm)
Provides:       tex(hfobl0800.vf)
Provides:       tex(hfobl0900.tfm)
Provides:       tex(hfobl0900.vf)
Provides:       tex(hfobl1000.tfm)
Provides:       tex(hfobl1000.vf)
Provides:       tex(hfobl1095.tfm)
Provides:       tex(hfobl1095.vf)
Provides:       tex(hfobl1200.tfm)
Provides:       tex(hfobl1200.vf)
Provides:       tex(hfobl1440.tfm)
Provides:       tex(hfobl1440.vf)
Provides:       tex(hfobl1728.tfm)
Provides:       tex(hfobl1728.vf)
Provides:       tex(hfobl2074.tfm)
Provides:       tex(hfobl2074.vf)
Provides:       tex(hfobl2488.tfm)
Provides:       tex(hfobl2488.vf)
Provides:       tex(hfobl2986.tfm)
Provides:       tex(hfobl2986.vf)
Provides:       tex(hfobl3583.tfm)
Provides:       tex(hfobl3583.vf)
Provides:       tex(hfobx0500.tfm)
Provides:       tex(hfobx0500.vf)
Provides:       tex(hfobx0600.tfm)
Provides:       tex(hfobx0600.vf)
Provides:       tex(hfobx0700.tfm)
Provides:       tex(hfobx0700.vf)
Provides:       tex(hfobx0800.tfm)
Provides:       tex(hfobx0800.vf)
Provides:       tex(hfobx0900.tfm)
Provides:       tex(hfobx0900.vf)
Provides:       tex(hfobx1000.tfm)
Provides:       tex(hfobx1000.vf)
Provides:       tex(hfobx1095.tfm)
Provides:       tex(hfobx1095.vf)
Provides:       tex(hfobx1200.tfm)
Provides:       tex(hfobx1200.vf)
Provides:       tex(hfobx1440.tfm)
Provides:       tex(hfobx1440.vf)
Provides:       tex(hfobx1728.tfm)
Provides:       tex(hfobx1728.vf)
Provides:       tex(hfobx2074.tfm)
Provides:       tex(hfobx2074.vf)
Provides:       tex(hfobx2488.tfm)
Provides:       tex(hfobx2488.vf)
Provides:       tex(hfobx2986.tfm)
Provides:       tex(hfobx2986.vf)
Provides:       tex(hfobx3583.tfm)
Provides:       tex(hfobx3583.vf)
Provides:       tex(hfocc0500.tfm)
Provides:       tex(hfocc0500.vf)
Provides:       tex(hfocc0600.tfm)
Provides:       tex(hfocc0600.vf)
Provides:       tex(hfocc0700.tfm)
Provides:       tex(hfocc0700.vf)
Provides:       tex(hfocc0800.tfm)
Provides:       tex(hfocc0800.vf)
Provides:       tex(hfocc0900.tfm)
Provides:       tex(hfocc0900.vf)
Provides:       tex(hfocc1000.tfm)
Provides:       tex(hfocc1000.vf)
Provides:       tex(hfocc1095.tfm)
Provides:       tex(hfocc1095.vf)
Provides:       tex(hfocc1200.tfm)
Provides:       tex(hfocc1200.vf)
Provides:       tex(hfocc1440.tfm)
Provides:       tex(hfocc1440.vf)
Provides:       tex(hfocc1728.tfm)
Provides:       tex(hfocc1728.vf)
Provides:       tex(hfocc2074.tfm)
Provides:       tex(hfocc2074.vf)
Provides:       tex(hfocc2488.tfm)
Provides:       tex(hfocc2488.vf)
Provides:       tex(hfocc2986.tfm)
Provides:       tex(hfocc2986.vf)
Provides:       tex(hfocc3583.tfm)
Provides:       tex(hfocc3583.vf)
Provides:       tex(hfodh0500.tfm)
Provides:       tex(hfodh0500.vf)
Provides:       tex(hfodh0600.tfm)
Provides:       tex(hfodh0600.vf)
Provides:       tex(hfodh0700.tfm)
Provides:       tex(hfodh0700.vf)
Provides:       tex(hfodh0800.tfm)
Provides:       tex(hfodh0800.vf)
Provides:       tex(hfodh0900.tfm)
Provides:       tex(hfodh0900.vf)
Provides:       tex(hfodh1000.tfm)
Provides:       tex(hfodh1000.vf)
Provides:       tex(hfodh1095.tfm)
Provides:       tex(hfodh1095.vf)
Provides:       tex(hfodh1200.tfm)
Provides:       tex(hfodh1200.vf)
Provides:       tex(hfodh1440.tfm)
Provides:       tex(hfodh1440.vf)
Provides:       tex(hfodh1728.tfm)
Provides:       tex(hfodh1728.vf)
Provides:       tex(hfodh2074.tfm)
Provides:       tex(hfodh2074.vf)
Provides:       tex(hfodh2488.tfm)
Provides:       tex(hfodh2488.vf)
Provides:       tex(hfodh2986.tfm)
Provides:       tex(hfodh2986.vf)
Provides:       tex(hfodh3583.tfm)
Provides:       tex(hfodh3583.vf)
Provides:       tex(hfoit0600.tfm)
Provides:       tex(hfoit0600.vf)
Provides:       tex(hfoit0700.tfm)
Provides:       tex(hfoit0700.vf)
Provides:       tex(hfoit0800.tfm)
Provides:       tex(hfoit0800.vf)
Provides:       tex(hfoit0900.tfm)
Provides:       tex(hfoit0900.vf)
Provides:       tex(hfoit1000.tfm)
Provides:       tex(hfoit1000.vf)
Provides:       tex(hfoit1095.tfm)
Provides:       tex(hfoit1095.vf)
Provides:       tex(hfoit1200.tfm)
Provides:       tex(hfoit1200.vf)
Provides:       tex(hfoit1440.tfm)
Provides:       tex(hfoit1440.vf)
Provides:       tex(hfoit1728.tfm)
Provides:       tex(hfoit1728.vf)
Provides:       tex(hfoit2074.tfm)
Provides:       tex(hfoit2074.vf)
Provides:       tex(hfoit2488.tfm)
Provides:       tex(hfoit2488.vf)
Provides:       tex(hfoit2986.tfm)
Provides:       tex(hfoit2986.vf)
Provides:       tex(hfoit3583.tfm)
Provides:       tex(hfoit3583.vf)
Provides:       tex(hfoldsty.sty)
Provides:       tex(hfooc0500.tfm)
Provides:       tex(hfooc0500.vf)
Provides:       tex(hfooc0600.tfm)
Provides:       tex(hfooc0600.vf)
Provides:       tex(hfooc0700.tfm)
Provides:       tex(hfooc0700.vf)
Provides:       tex(hfooc0800.tfm)
Provides:       tex(hfooc0800.vf)
Provides:       tex(hfooc0900.tfm)
Provides:       tex(hfooc0900.vf)
Provides:       tex(hfooc1000.tfm)
Provides:       tex(hfooc1000.vf)
Provides:       tex(hfooc1095.tfm)
Provides:       tex(hfooc1095.vf)
Provides:       tex(hfooc1200.tfm)
Provides:       tex(hfooc1200.vf)
Provides:       tex(hfooc1440.tfm)
Provides:       tex(hfooc1440.vf)
Provides:       tex(hfooc1728.tfm)
Provides:       tex(hfooc1728.vf)
Provides:       tex(hfooc2074.tfm)
Provides:       tex(hfooc2074.vf)
Provides:       tex(hfooc2488.tfm)
Provides:       tex(hfooc2488.vf)
Provides:       tex(hfooc2986.tfm)
Provides:       tex(hfooc2986.vf)
Provides:       tex(hfooc3583.tfm)
Provides:       tex(hfooc3583.vf)
Provides:       tex(hforb0500.tfm)
Provides:       tex(hforb0500.vf)
Provides:       tex(hforb0600.tfm)
Provides:       tex(hforb0600.vf)
Provides:       tex(hforb0700.tfm)
Provides:       tex(hforb0700.vf)
Provides:       tex(hforb0800.tfm)
Provides:       tex(hforb0800.vf)
Provides:       tex(hforb0900.tfm)
Provides:       tex(hforb0900.vf)
Provides:       tex(hforb1000.tfm)
Provides:       tex(hforb1000.vf)
Provides:       tex(hforb1095.tfm)
Provides:       tex(hforb1095.vf)
Provides:       tex(hforb1200.tfm)
Provides:       tex(hforb1200.vf)
Provides:       tex(hforb1440.tfm)
Provides:       tex(hforb1440.vf)
Provides:       tex(hforb1728.tfm)
Provides:       tex(hforb1728.vf)
Provides:       tex(hforb2074.tfm)
Provides:       tex(hforb2074.vf)
Provides:       tex(hforb2488.tfm)
Provides:       tex(hforb2488.vf)
Provides:       tex(hforb2986.tfm)
Provides:       tex(hforb2986.vf)
Provides:       tex(hforb3583.tfm)
Provides:       tex(hforb3583.vf)
Provides:       tex(hform0500.tfm)
Provides:       tex(hform0500.vf)
Provides:       tex(hform0600.tfm)
Provides:       tex(hform0600.vf)
Provides:       tex(hform0700.tfm)
Provides:       tex(hform0700.vf)
Provides:       tex(hform0800.tfm)
Provides:       tex(hform0800.vf)
Provides:       tex(hform0900.tfm)
Provides:       tex(hform0900.vf)
Provides:       tex(hform1000.tfm)
Provides:       tex(hform1000.vf)
Provides:       tex(hform1095.tfm)
Provides:       tex(hform1095.vf)
Provides:       tex(hform1200.tfm)
Provides:       tex(hform1200.vf)
Provides:       tex(hform1440.tfm)
Provides:       tex(hform1440.vf)
Provides:       tex(hform1728.tfm)
Provides:       tex(hform1728.vf)
Provides:       tex(hform2074.tfm)
Provides:       tex(hform2074.vf)
Provides:       tex(hform2488.tfm)
Provides:       tex(hform2488.vf)
Provides:       tex(hform2986.tfm)
Provides:       tex(hform2986.vf)
Provides:       tex(hform3583.tfm)
Provides:       tex(hform3583.vf)
Provides:       tex(hfosc0500.tfm)
Provides:       tex(hfosc0500.vf)
Provides:       tex(hfosc0600.tfm)
Provides:       tex(hfosc0600.vf)
Provides:       tex(hfosc0700.tfm)
Provides:       tex(hfosc0700.vf)
Provides:       tex(hfosc0800.tfm)
Provides:       tex(hfosc0800.vf)
Provides:       tex(hfosc0900.tfm)
Provides:       tex(hfosc0900.vf)
Provides:       tex(hfosc1000.tfm)
Provides:       tex(hfosc1000.vf)
Provides:       tex(hfosc1095.tfm)
Provides:       tex(hfosc1095.vf)
Provides:       tex(hfosc1200.tfm)
Provides:       tex(hfosc1200.vf)
Provides:       tex(hfosc1440.tfm)
Provides:       tex(hfosc1440.vf)
Provides:       tex(hfosc1728.tfm)
Provides:       tex(hfosc1728.vf)
Provides:       tex(hfosc2074.tfm)
Provides:       tex(hfosc2074.vf)
Provides:       tex(hfosc2488.tfm)
Provides:       tex(hfosc2488.vf)
Provides:       tex(hfosc2986.tfm)
Provides:       tex(hfosc2986.vf)
Provides:       tex(hfosc3583.tfm)
Provides:       tex(hfosc3583.vf)
Provides:       tex(hfosi0500.tfm)
Provides:       tex(hfosi0500.vf)
Provides:       tex(hfosi0600.tfm)
Provides:       tex(hfosi0600.vf)
Provides:       tex(hfosi0700.tfm)
Provides:       tex(hfosi0700.vf)
Provides:       tex(hfosi0800.tfm)
Provides:       tex(hfosi0800.vf)
Provides:       tex(hfosi0900.tfm)
Provides:       tex(hfosi0900.vf)
Provides:       tex(hfosi1000.tfm)
Provides:       tex(hfosi1000.vf)
Provides:       tex(hfosi1095.tfm)
Provides:       tex(hfosi1095.vf)
Provides:       tex(hfosi1200.tfm)
Provides:       tex(hfosi1200.vf)
Provides:       tex(hfosi1440.tfm)
Provides:       tex(hfosi1440.vf)
Provides:       tex(hfosi1728.tfm)
Provides:       tex(hfosi1728.vf)
Provides:       tex(hfosi2074.tfm)
Provides:       tex(hfosi2074.vf)
Provides:       tex(hfosi2488.tfm)
Provides:       tex(hfosi2488.vf)
Provides:       tex(hfosi2986.tfm)
Provides:       tex(hfosi2986.vf)
Provides:       tex(hfosi3583.tfm)
Provides:       tex(hfosi3583.vf)
Provides:       tex(hfosl0500.tfm)
Provides:       tex(hfosl0500.vf)
Provides:       tex(hfosl0600.tfm)
Provides:       tex(hfosl0600.vf)
Provides:       tex(hfosl0700.tfm)
Provides:       tex(hfosl0700.vf)
Provides:       tex(hfosl0800.tfm)
Provides:       tex(hfosl0800.vf)
Provides:       tex(hfosl0900.tfm)
Provides:       tex(hfosl0900.vf)
Provides:       tex(hfosl1000.tfm)
Provides:       tex(hfosl1000.vf)
Provides:       tex(hfosl1095.tfm)
Provides:       tex(hfosl1095.vf)
Provides:       tex(hfosl1200.tfm)
Provides:       tex(hfosl1200.vf)
Provides:       tex(hfosl1440.tfm)
Provides:       tex(hfosl1440.vf)
Provides:       tex(hfosl1728.tfm)
Provides:       tex(hfosl1728.vf)
Provides:       tex(hfosl2074.tfm)
Provides:       tex(hfosl2074.vf)
Provides:       tex(hfosl2488.tfm)
Provides:       tex(hfosl2488.vf)
Provides:       tex(hfosl2986.tfm)
Provides:       tex(hfosl2986.vf)
Provides:       tex(hfosl3583.tfm)
Provides:       tex(hfosl3583.vf)
Provides:       tex(hfoso0500.tfm)
Provides:       tex(hfoso0500.vf)
Provides:       tex(hfoso0600.tfm)
Provides:       tex(hfoso0600.vf)
Provides:       tex(hfoso0700.tfm)
Provides:       tex(hfoso0700.vf)
Provides:       tex(hfoso0800.tfm)
Provides:       tex(hfoso0800.vf)
Provides:       tex(hfoso0900.tfm)
Provides:       tex(hfoso0900.vf)
Provides:       tex(hfoso1000.tfm)
Provides:       tex(hfoso1000.vf)
Provides:       tex(hfoso1095.tfm)
Provides:       tex(hfoso1095.vf)
Provides:       tex(hfoso1200.tfm)
Provides:       tex(hfoso1200.vf)
Provides:       tex(hfoso1440.tfm)
Provides:       tex(hfoso1440.vf)
Provides:       tex(hfoso1728.tfm)
Provides:       tex(hfoso1728.vf)
Provides:       tex(hfoso2074.tfm)
Provides:       tex(hfoso2074.vf)
Provides:       tex(hfoso2488.tfm)
Provides:       tex(hfoso2488.vf)
Provides:       tex(hfoso2986.tfm)
Provides:       tex(hfoso2986.vf)
Provides:       tex(hfoso3583.tfm)
Provides:       tex(hfoso3583.vf)
Provides:       tex(hfoss0500.tfm)
Provides:       tex(hfoss0500.vf)
Provides:       tex(hfoss0600.tfm)
Provides:       tex(hfoss0600.vf)
Provides:       tex(hfoss0700.tfm)
Provides:       tex(hfoss0700.vf)
Provides:       tex(hfoss0800.tfm)
Provides:       tex(hfoss0800.vf)
Provides:       tex(hfoss0900.tfm)
Provides:       tex(hfoss0900.vf)
Provides:       tex(hfoss1000.tfm)
Provides:       tex(hfoss1000.vf)
Provides:       tex(hfoss1095.tfm)
Provides:       tex(hfoss1095.vf)
Provides:       tex(hfoss1200.tfm)
Provides:       tex(hfoss1200.vf)
Provides:       tex(hfoss1440.tfm)
Provides:       tex(hfoss1440.vf)
Provides:       tex(hfoss1728.tfm)
Provides:       tex(hfoss1728.vf)
Provides:       tex(hfoss2074.tfm)
Provides:       tex(hfoss2074.vf)
Provides:       tex(hfoss2488.tfm)
Provides:       tex(hfoss2488.vf)
Provides:       tex(hfoss2986.tfm)
Provides:       tex(hfoss2986.vf)
Provides:       tex(hfoss3583.tfm)
Provides:       tex(hfoss3583.vf)
Provides:       tex(hfost0600.tfm)
Provides:       tex(hfost0600.vf)
Provides:       tex(hfost0700.tfm)
Provides:       tex(hfost0700.vf)
Provides:       tex(hfost0800.tfm)
Provides:       tex(hfost0800.vf)
Provides:       tex(hfost0900.tfm)
Provides:       tex(hfost0900.vf)
Provides:       tex(hfost1000.tfm)
Provides:       tex(hfost1000.vf)
Provides:       tex(hfost1095.tfm)
Provides:       tex(hfost1095.vf)
Provides:       tex(hfost1200.tfm)
Provides:       tex(hfost1200.vf)
Provides:       tex(hfost1440.tfm)
Provides:       tex(hfost1440.vf)
Provides:       tex(hfost1728.tfm)
Provides:       tex(hfost1728.vf)
Provides:       tex(hfost2074.tfm)
Provides:       tex(hfost2074.vf)
Provides:       tex(hfost2488.tfm)
Provides:       tex(hfost2488.vf)
Provides:       tex(hfost2986.tfm)
Provides:       tex(hfost2986.vf)
Provides:       tex(hfost3583.tfm)
Provides:       tex(hfost3583.vf)
Provides:       tex(hfosx0500.tfm)
Provides:       tex(hfosx0500.vf)
Provides:       tex(hfosx0600.tfm)
Provides:       tex(hfosx0600.vf)
Provides:       tex(hfosx0700.tfm)
Provides:       tex(hfosx0700.vf)
Provides:       tex(hfosx0800.tfm)
Provides:       tex(hfosx0800.vf)
Provides:       tex(hfosx0900.tfm)
Provides:       tex(hfosx0900.vf)
Provides:       tex(hfosx1000.tfm)
Provides:       tex(hfosx1000.vf)
Provides:       tex(hfosx1095.tfm)
Provides:       tex(hfosx1095.vf)
Provides:       tex(hfosx1200.tfm)
Provides:       tex(hfosx1200.vf)
Provides:       tex(hfosx1440.tfm)
Provides:       tex(hfosx1440.vf)
Provides:       tex(hfosx1728.tfm)
Provides:       tex(hfosx1728.vf)
Provides:       tex(hfosx2074.tfm)
Provides:       tex(hfosx2074.vf)
Provides:       tex(hfosx2488.tfm)
Provides:       tex(hfosx2488.vf)
Provides:       tex(hfosx2986.tfm)
Provides:       tex(hfosx2986.vf)
Provides:       tex(hfosx3583.tfm)
Provides:       tex(hfosx3583.vf)
Provides:       tex(hfotc0600.tfm)
Provides:       tex(hfotc0600.vf)
Provides:       tex(hfotc0700.tfm)
Provides:       tex(hfotc0700.vf)
Provides:       tex(hfotc0800.tfm)
Provides:       tex(hfotc0800.vf)
Provides:       tex(hfotc0900.tfm)
Provides:       tex(hfotc0900.vf)
Provides:       tex(hfotc1000.tfm)
Provides:       tex(hfotc1000.vf)
Provides:       tex(hfotc1095.tfm)
Provides:       tex(hfotc1095.vf)
Provides:       tex(hfotc1200.tfm)
Provides:       tex(hfotc1200.vf)
Provides:       tex(hfotc1440.tfm)
Provides:       tex(hfotc1440.vf)
Provides:       tex(hfotc1728.tfm)
Provides:       tex(hfotc1728.vf)
Provides:       tex(hfotc2074.tfm)
Provides:       tex(hfotc2074.vf)
Provides:       tex(hfotc2488.tfm)
Provides:       tex(hfotc2488.vf)
Provides:       tex(hfotc2986.tfm)
Provides:       tex(hfotc2986.vf)
Provides:       tex(hfotc3583.tfm)
Provides:       tex(hfotc3583.vf)
Provides:       tex(hfoti0500.tfm)
Provides:       tex(hfoti0500.vf)
Provides:       tex(hfoti0600.tfm)
Provides:       tex(hfoti0600.vf)
Provides:       tex(hfoti0700.tfm)
Provides:       tex(hfoti0700.vf)
Provides:       tex(hfoti0800.tfm)
Provides:       tex(hfoti0800.vf)
Provides:       tex(hfoti0900.tfm)
Provides:       tex(hfoti0900.vf)
Provides:       tex(hfoti1000.tfm)
Provides:       tex(hfoti1000.vf)
Provides:       tex(hfoti1095.tfm)
Provides:       tex(hfoti1095.vf)
Provides:       tex(hfoti1200.tfm)
Provides:       tex(hfoti1200.vf)
Provides:       tex(hfoti1440.tfm)
Provides:       tex(hfoti1440.vf)
Provides:       tex(hfoti1728.tfm)
Provides:       tex(hfoti1728.vf)
Provides:       tex(hfoti2074.tfm)
Provides:       tex(hfoti2074.vf)
Provides:       tex(hfoti2488.tfm)
Provides:       tex(hfoti2488.vf)
Provides:       tex(hfoti2986.tfm)
Provides:       tex(hfoti2986.vf)
Provides:       tex(hfoti3583.tfm)
Provides:       tex(hfoti3583.vf)
Provides:       tex(hfott0600.tfm)
Provides:       tex(hfott0600.vf)
Provides:       tex(hfott0700.tfm)
Provides:       tex(hfott0700.vf)
Provides:       tex(hfott0800.tfm)
Provides:       tex(hfott0800.vf)
Provides:       tex(hfott0900.tfm)
Provides:       tex(hfott0900.vf)
Provides:       tex(hfott1000.tfm)
Provides:       tex(hfott1000.vf)
Provides:       tex(hfott1095.tfm)
Provides:       tex(hfott1095.vf)
Provides:       tex(hfott1200.tfm)
Provides:       tex(hfott1200.vf)
Provides:       tex(hfott1440.tfm)
Provides:       tex(hfott1440.vf)
Provides:       tex(hfott1728.tfm)
Provides:       tex(hfott1728.vf)
Provides:       tex(hfott2074.tfm)
Provides:       tex(hfott2074.vf)
Provides:       tex(hfott2488.tfm)
Provides:       tex(hfott2488.vf)
Provides:       tex(hfott2986.tfm)
Provides:       tex(hfott2986.vf)
Provides:       tex(hfott3583.tfm)
Provides:       tex(hfott3583.vf)
Provides:       tex(hfoui0500.tfm)
Provides:       tex(hfoui0500.vf)
Provides:       tex(hfoui0600.tfm)
Provides:       tex(hfoui0600.vf)
Provides:       tex(hfoui0700.tfm)
Provides:       tex(hfoui0700.vf)
Provides:       tex(hfoui0800.tfm)
Provides:       tex(hfoui0800.vf)
Provides:       tex(hfoui0900.tfm)
Provides:       tex(hfoui0900.vf)
Provides:       tex(hfoui1000.tfm)
Provides:       tex(hfoui1000.vf)
Provides:       tex(hfoui1095.tfm)
Provides:       tex(hfoui1095.vf)
Provides:       tex(hfoui1200.tfm)
Provides:       tex(hfoui1200.vf)
Provides:       tex(hfoui1440.tfm)
Provides:       tex(hfoui1440.vf)
Provides:       tex(hfoui1728.tfm)
Provides:       tex(hfoui1728.vf)
Provides:       tex(hfoui2074.tfm)
Provides:       tex(hfoui2074.vf)
Provides:       tex(hfoui2488.tfm)
Provides:       tex(hfoui2488.vf)
Provides:       tex(hfoui2986.tfm)
Provides:       tex(hfoui2986.vf)
Provides:       tex(hfoui3583.tfm)
Provides:       tex(hfoui3583.vf)
Provides:       tex(hfovi0600.tfm)
Provides:       tex(hfovi0600.vf)
Provides:       tex(hfovi0700.tfm)
Provides:       tex(hfovi0700.vf)
Provides:       tex(hfovi0800.tfm)
Provides:       tex(hfovi0800.vf)
Provides:       tex(hfovi0900.tfm)
Provides:       tex(hfovi0900.vf)
Provides:       tex(hfovi1000.tfm)
Provides:       tex(hfovi1000.vf)
Provides:       tex(hfovi1095.tfm)
Provides:       tex(hfovi1095.vf)
Provides:       tex(hfovi1200.tfm)
Provides:       tex(hfovi1200.vf)
Provides:       tex(hfovi1440.tfm)
Provides:       tex(hfovi1440.vf)
Provides:       tex(hfovi1728.tfm)
Provides:       tex(hfovi1728.vf)
Provides:       tex(hfovi2074.tfm)
Provides:       tex(hfovi2074.vf)
Provides:       tex(hfovi2488.tfm)
Provides:       tex(hfovi2488.vf)
Provides:       tex(hfovi2986.tfm)
Provides:       tex(hfovi2986.vf)
Provides:       tex(hfovi3583.tfm)
Provides:       tex(hfovi3583.vf)
Provides:       tex(hfovt0600.tfm)
Provides:       tex(hfovt0600.vf)
Provides:       tex(hfovt0700.tfm)
Provides:       tex(hfovt0700.vf)
Provides:       tex(hfovt0800.tfm)
Provides:       tex(hfovt0800.vf)
Provides:       tex(hfovt0900.tfm)
Provides:       tex(hfovt0900.vf)
Provides:       tex(hfovt1000.tfm)
Provides:       tex(hfovt1000.vf)
Provides:       tex(hfovt1095.tfm)
Provides:       tex(hfovt1095.vf)
Provides:       tex(hfovt1200.tfm)
Provides:       tex(hfovt1200.vf)
Provides:       tex(hfovt1440.tfm)
Provides:       tex(hfovt1440.vf)
Provides:       tex(hfovt1728.tfm)
Provides:       tex(hfovt1728.vf)
Provides:       tex(hfovt2074.tfm)
Provides:       tex(hfovt2074.vf)
Provides:       tex(hfovt2488.tfm)
Provides:       tex(hfovt2488.vf)
Provides:       tex(hfovt2986.tfm)
Provides:       tex(hfovt2986.vf)
Provides:       tex(hfovt3583.tfm)
Provides:       tex(hfovt3583.vf)
Provides:       tex(hfoxc0500.tfm)
Provides:       tex(hfoxc0500.vf)
Provides:       tex(hfoxc0600.tfm)
Provides:       tex(hfoxc0600.vf)
Provides:       tex(hfoxc0700.tfm)
Provides:       tex(hfoxc0700.vf)
Provides:       tex(hfoxc0800.tfm)
Provides:       tex(hfoxc0800.vf)
Provides:       tex(hfoxc0900.tfm)
Provides:       tex(hfoxc0900.vf)
Provides:       tex(hfoxc1000.tfm)
Provides:       tex(hfoxc1000.vf)
Provides:       tex(hfoxc1095.tfm)
Provides:       tex(hfoxc1095.vf)
Provides:       tex(hfoxc1200.tfm)
Provides:       tex(hfoxc1200.vf)
Provides:       tex(hfoxc1440.tfm)
Provides:       tex(hfoxc1440.vf)
Provides:       tex(hfoxc1728.tfm)
Provides:       tex(hfoxc1728.vf)
Provides:       tex(hfoxc2074.tfm)
Provides:       tex(hfoxc2074.vf)
Provides:       tex(hfoxc2488.tfm)
Provides:       tex(hfoxc2488.vf)
Provides:       tex(hfoxc2986.tfm)
Provides:       tex(hfoxc2986.vf)
Provides:       tex(hfoxc3583.tfm)
Provides:       tex(hfoxc3583.vf)
Provides:       tex(omlhfor.fd)
Provides:       tex(omshfor.fd)
Provides:       tex(t1hfodh.fd)
Provides:       tex(t1hfor.fd)
Provides:       tex(t1hfoss.fd)
Provides:       tex(t1hfott.fd)
Provides:       tex(t1hfovt.fd)
Provides:       tex(ts1hfor.fd)
Provides:       tex(ts1hfoss.fd)
Provides:       tex(ts1hfott.fd)
Provides:       tex(ts1hfovtt.fd)
Requires:       tex(ecbi0500.tfm)
Requires:       tex(ecbi0600.tfm)
Requires:       tex(ecbi0700.tfm)
Requires:       tex(ecbi0800.tfm)
Requires:       tex(ecbi0900.tfm)
Requires:       tex(ecbi1000.tfm)
Requires:       tex(ecbi1095.tfm)
Requires:       tex(ecbi1200.tfm)
Requires:       tex(ecbi1440.tfm)
Requires:       tex(ecbi1728.tfm)
Requires:       tex(ecbi2074.tfm)
Requires:       tex(ecbi2488.tfm)
Requires:       tex(ecbi2986.tfm)
Requires:       tex(ecbi3583.tfm)
Requires:       tex(ecbl0500.tfm)
Requires:       tex(ecbl0600.tfm)
Requires:       tex(ecbl0700.tfm)
Requires:       tex(ecbl0800.tfm)
Requires:       tex(ecbl0900.tfm)
Requires:       tex(ecbl1000.tfm)
Requires:       tex(ecbl1095.tfm)
Requires:       tex(ecbl1200.tfm)
Requires:       tex(ecbl1440.tfm)
Requires:       tex(ecbl1728.tfm)
Requires:       tex(ecbl2074.tfm)
Requires:       tex(ecbl2488.tfm)
Requires:       tex(ecbl2986.tfm)
Requires:       tex(ecbl3583.tfm)
Requires:       tex(ecbx0500.tfm)
Requires:       tex(ecbx0600.tfm)
Requires:       tex(ecbx0700.tfm)
Requires:       tex(ecbx0800.tfm)
Requires:       tex(ecbx0900.tfm)
Requires:       tex(ecbx1000.tfm)
Requires:       tex(ecbx1095.tfm)
Requires:       tex(ecbx1200.tfm)
Requires:       tex(ecbx1440.tfm)
Requires:       tex(ecbx1728.tfm)
Requires:       tex(ecbx2074.tfm)
Requires:       tex(ecbx2488.tfm)
Requires:       tex(ecbx2986.tfm)
Requires:       tex(ecbx3583.tfm)
Requires:       tex(eccc0500.tfm)
Requires:       tex(eccc0600.tfm)
Requires:       tex(eccc0700.tfm)
Requires:       tex(eccc0800.tfm)
Requires:       tex(eccc0900.tfm)
Requires:       tex(eccc1000.tfm)
Requires:       tex(eccc1095.tfm)
Requires:       tex(eccc1200.tfm)
Requires:       tex(eccc1440.tfm)
Requires:       tex(eccc1728.tfm)
Requires:       tex(eccc2074.tfm)
Requires:       tex(eccc2488.tfm)
Requires:       tex(eccc2986.tfm)
Requires:       tex(eccc3583.tfm)
Requires:       tex(ecdh0500.tfm)
Requires:       tex(ecdh0600.tfm)
Requires:       tex(ecdh0700.tfm)
Requires:       tex(ecdh0800.tfm)
Requires:       tex(ecdh0900.tfm)
Requires:       tex(ecdh1000.tfm)
Requires:       tex(ecdh1095.tfm)
Requires:       tex(ecdh1200.tfm)
Requires:       tex(ecdh1440.tfm)
Requires:       tex(ecdh1728.tfm)
Requires:       tex(ecdh2074.tfm)
Requires:       tex(ecdh2488.tfm)
Requires:       tex(ecdh2986.tfm)
Requires:       tex(ecdh3583.tfm)
Requires:       tex(ecit0800.tfm)
Requires:       tex(ecit0900.tfm)
Requires:       tex(ecit1000.tfm)
Requires:       tex(ecit1095.tfm)
Requires:       tex(ecit1200.tfm)
Requires:       tex(ecit1440.tfm)
Requires:       tex(ecit1728.tfm)
Requires:       tex(ecit2074.tfm)
Requires:       tex(ecit2488.tfm)
Requires:       tex(ecit2986.tfm)
Requires:       tex(ecit3583.tfm)
Requires:       tex(ecoc0500.tfm)
Requires:       tex(ecoc0600.tfm)
Requires:       tex(ecoc0700.tfm)
Requires:       tex(ecoc0800.tfm)
Requires:       tex(ecoc0900.tfm)
Requires:       tex(ecoc1000.tfm)
Requires:       tex(ecoc1095.tfm)
Requires:       tex(ecoc1200.tfm)
Requires:       tex(ecoc1440.tfm)
Requires:       tex(ecoc1728.tfm)
Requires:       tex(ecoc2074.tfm)
Requires:       tex(ecoc2488.tfm)
Requires:       tex(ecoc2986.tfm)
Requires:       tex(ecoc3583.tfm)
Requires:       tex(ecrb0500.tfm)
Requires:       tex(ecrb0600.tfm)
Requires:       tex(ecrb0700.tfm)
Requires:       tex(ecrb0800.tfm)
Requires:       tex(ecrb0900.tfm)
Requires:       tex(ecrb1000.tfm)
Requires:       tex(ecrb1095.tfm)
Requires:       tex(ecrb1200.tfm)
Requires:       tex(ecrb1440.tfm)
Requires:       tex(ecrb1728.tfm)
Requires:       tex(ecrb2074.tfm)
Requires:       tex(ecrb2488.tfm)
Requires:       tex(ecrb2986.tfm)
Requires:       tex(ecrb3583.tfm)
Requires:       tex(ecrm0500.tfm)
Requires:       tex(ecrm0600.tfm)
Requires:       tex(ecrm0700.tfm)
Requires:       tex(ecrm0800.tfm)
Requires:       tex(ecrm0900.tfm)
Requires:       tex(ecrm1000.tfm)
Requires:       tex(ecrm1095.tfm)
Requires:       tex(ecrm1200.tfm)
Requires:       tex(ecrm1440.tfm)
Requires:       tex(ecrm1728.tfm)
Requires:       tex(ecrm2074.tfm)
Requires:       tex(ecrm2488.tfm)
Requires:       tex(ecrm2986.tfm)
Requires:       tex(ecrm3583.tfm)
Requires:       tex(ecsc0500.tfm)
Requires:       tex(ecsc0600.tfm)
Requires:       tex(ecsc0700.tfm)
Requires:       tex(ecsc0800.tfm)
Requires:       tex(ecsc0900.tfm)
Requires:       tex(ecsc1000.tfm)
Requires:       tex(ecsc1095.tfm)
Requires:       tex(ecsc1200.tfm)
Requires:       tex(ecsc1440.tfm)
Requires:       tex(ecsc1728.tfm)
Requires:       tex(ecsc2074.tfm)
Requires:       tex(ecsc2488.tfm)
Requires:       tex(ecsc2986.tfm)
Requires:       tex(ecsc3583.tfm)
Requires:       tex(ecsi0500.tfm)
Requires:       tex(ecsi0600.tfm)
Requires:       tex(ecsi0700.tfm)
Requires:       tex(ecsi0800.tfm)
Requires:       tex(ecsi0900.tfm)
Requires:       tex(ecsi1000.tfm)
Requires:       tex(ecsi1095.tfm)
Requires:       tex(ecsi1200.tfm)
Requires:       tex(ecsi1440.tfm)
Requires:       tex(ecsi1728.tfm)
Requires:       tex(ecsi2074.tfm)
Requires:       tex(ecsi2488.tfm)
Requires:       tex(ecsi2986.tfm)
Requires:       tex(ecsi3583.tfm)
Requires:       tex(ecsl0500.tfm)
Requires:       tex(ecsl0600.tfm)
Requires:       tex(ecsl0700.tfm)
Requires:       tex(ecsl0800.tfm)
Requires:       tex(ecsl0900.tfm)
Requires:       tex(ecsl1000.tfm)
Requires:       tex(ecsl1095.tfm)
Requires:       tex(ecsl1200.tfm)
Requires:       tex(ecsl1440.tfm)
Requires:       tex(ecsl1728.tfm)
Requires:       tex(ecsl2074.tfm)
Requires:       tex(ecsl2488.tfm)
Requires:       tex(ecsl2986.tfm)
Requires:       tex(ecsl3583.tfm)
Requires:       tex(ecso0500.tfm)
Requires:       tex(ecso0600.tfm)
Requires:       tex(ecso0700.tfm)
Requires:       tex(ecso0800.tfm)
Requires:       tex(ecso0900.tfm)
Requires:       tex(ecso1000.tfm)
Requires:       tex(ecso1095.tfm)
Requires:       tex(ecso1200.tfm)
Requires:       tex(ecso1440.tfm)
Requires:       tex(ecso1728.tfm)
Requires:       tex(ecso2074.tfm)
Requires:       tex(ecso2488.tfm)
Requires:       tex(ecso2986.tfm)
Requires:       tex(ecso3583.tfm)
Requires:       tex(ecss0500.tfm)
Requires:       tex(ecss0600.tfm)
Requires:       tex(ecss0700.tfm)
Requires:       tex(ecss0800.tfm)
Requires:       tex(ecss0900.tfm)
Requires:       tex(ecss1000.tfm)
Requires:       tex(ecss1095.tfm)
Requires:       tex(ecss1200.tfm)
Requires:       tex(ecss1440.tfm)
Requires:       tex(ecss1728.tfm)
Requires:       tex(ecss2074.tfm)
Requires:       tex(ecss2488.tfm)
Requires:       tex(ecss2986.tfm)
Requires:       tex(ecss3583.tfm)
Requires:       tex(ecst0800.tfm)
Requires:       tex(ecst0900.tfm)
Requires:       tex(ecst1000.tfm)
Requires:       tex(ecst1095.tfm)
Requires:       tex(ecst1200.tfm)
Requires:       tex(ecst1440.tfm)
Requires:       tex(ecst1728.tfm)
Requires:       tex(ecst2074.tfm)
Requires:       tex(ecst2488.tfm)
Requires:       tex(ecst2986.tfm)
Requires:       tex(ecst3583.tfm)
Requires:       tex(ecsx0500.tfm)
Requires:       tex(ecsx0600.tfm)
Requires:       tex(ecsx0700.tfm)
Requires:       tex(ecsx0800.tfm)
Requires:       tex(ecsx0900.tfm)
Requires:       tex(ecsx1000.tfm)
Requires:       tex(ecsx1095.tfm)
Requires:       tex(ecsx1200.tfm)
Requires:       tex(ecsx1440.tfm)
Requires:       tex(ecsx1728.tfm)
Requires:       tex(ecsx2074.tfm)
Requires:       tex(ecsx2488.tfm)
Requires:       tex(ecsx2986.tfm)
Requires:       tex(ecsx3583.tfm)
Requires:       tex(ectc0800.tfm)
Requires:       tex(ectc0900.tfm)
Requires:       tex(ectc1000.tfm)
Requires:       tex(ectc1095.tfm)
Requires:       tex(ectc1200.tfm)
Requires:       tex(ectc1440.tfm)
Requires:       tex(ectc1728.tfm)
Requires:       tex(ectc2074.tfm)
Requires:       tex(ectc2488.tfm)
Requires:       tex(ectc2986.tfm)
Requires:       tex(ectc3583.tfm)
Requires:       tex(ecti0500.tfm)
Requires:       tex(ecti0600.tfm)
Requires:       tex(ecti0700.tfm)
Requires:       tex(ecti0800.tfm)
Requires:       tex(ecti0900.tfm)
Requires:       tex(ecti1000.tfm)
Requires:       tex(ecti1095.tfm)
Requires:       tex(ecti1200.tfm)
Requires:       tex(ecti1440.tfm)
Requires:       tex(ecti1728.tfm)
Requires:       tex(ecti2074.tfm)
Requires:       tex(ecti2488.tfm)
Requires:       tex(ecti2986.tfm)
Requires:       tex(ecti3583.tfm)
Requires:       tex(ectt0800.tfm)
Requires:       tex(ectt0900.tfm)
Requires:       tex(ectt1000.tfm)
Requires:       tex(ectt1095.tfm)
Requires:       tex(ectt1200.tfm)
Requires:       tex(ectt1440.tfm)
Requires:       tex(ectt1728.tfm)
Requires:       tex(ectt2074.tfm)
Requires:       tex(ectt2488.tfm)
Requires:       tex(ectt2986.tfm)
Requires:       tex(ectt3583.tfm)
Requires:       tex(ecui0500.tfm)
Requires:       tex(ecui0600.tfm)
Requires:       tex(ecui0700.tfm)
Requires:       tex(ecui0800.tfm)
Requires:       tex(ecui0900.tfm)
Requires:       tex(ecui1000.tfm)
Requires:       tex(ecui1095.tfm)
Requires:       tex(ecui1200.tfm)
Requires:       tex(ecui1440.tfm)
Requires:       tex(ecui1728.tfm)
Requires:       tex(ecui2074.tfm)
Requires:       tex(ecui2488.tfm)
Requires:       tex(ecui2986.tfm)
Requires:       tex(ecui3583.tfm)
Requires:       tex(ecvi0800.tfm)
Requires:       tex(ecvi0900.tfm)
Requires:       tex(ecvi1000.tfm)
Requires:       tex(ecvi1095.tfm)
Requires:       tex(ecvi1200.tfm)
Requires:       tex(ecvi1440.tfm)
Requires:       tex(ecvi1728.tfm)
Requires:       tex(ecvi2074.tfm)
Requires:       tex(ecvi2488.tfm)
Requires:       tex(ecvi2986.tfm)
Requires:       tex(ecvi3583.tfm)
Requires:       tex(ecvt0800.tfm)
Requires:       tex(ecvt0900.tfm)
Requires:       tex(ecvt1000.tfm)
Requires:       tex(ecvt1095.tfm)
Requires:       tex(ecvt1200.tfm)
Requires:       tex(ecvt1440.tfm)
Requires:       tex(ecvt1728.tfm)
Requires:       tex(ecvt2074.tfm)
Requires:       tex(ecvt2488.tfm)
Requires:       tex(ecvt2986.tfm)
Requires:       tex(ecvt3583.tfm)
Requires:       tex(ecxc0500.tfm)
Requires:       tex(ecxc0600.tfm)
Requires:       tex(ecxc0700.tfm)
Requires:       tex(ecxc0800.tfm)
Requires:       tex(ecxc0900.tfm)
Requires:       tex(ecxc1000.tfm)
Requires:       tex(ecxc1095.tfm)
Requires:       tex(ecxc1200.tfm)
Requires:       tex(ecxc1440.tfm)
Requires:       tex(ecxc1728.tfm)
Requires:       tex(ecxc2074.tfm)
Requires:       tex(ecxc2488.tfm)
Requires:       tex(ecxc2986.tfm)
Requires:       tex(ecxc3583.tfm)
Requires:       tex(fix-cm.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tcbi0500.tfm)
Requires:       tex(tcbi0600.tfm)
Requires:       tex(tcbi0700.tfm)
Requires:       tex(tcbi0800.tfm)
Requires:       tex(tcbi0900.tfm)
Requires:       tex(tcbi1000.tfm)
Requires:       tex(tcbi1095.tfm)
Requires:       tex(tcbi1200.tfm)
Requires:       tex(tcbi1440.tfm)
Requires:       tex(tcbi1728.tfm)
Requires:       tex(tcbi2074.tfm)
Requires:       tex(tcbi2488.tfm)
Requires:       tex(tcbi2986.tfm)
Requires:       tex(tcbi3583.tfm)
Requires:       tex(tcbl0500.tfm)
Requires:       tex(tcbl0600.tfm)
Requires:       tex(tcbl0700.tfm)
Requires:       tex(tcbl0800.tfm)
Requires:       tex(tcbl0900.tfm)
Requires:       tex(tcbl1000.tfm)
Requires:       tex(tcbl1095.tfm)
Requires:       tex(tcbl1200.tfm)
Requires:       tex(tcbl1440.tfm)
Requires:       tex(tcbl1728.tfm)
Requires:       tex(tcbl2074.tfm)
Requires:       tex(tcbl2488.tfm)
Requires:       tex(tcbl2986.tfm)
Requires:       tex(tcbl3583.tfm)
Requires:       tex(tcbx0500.tfm)
Requires:       tex(tcbx0600.tfm)
Requires:       tex(tcbx0700.tfm)
Requires:       tex(tcbx0800.tfm)
Requires:       tex(tcbx0900.tfm)
Requires:       tex(tcbx1000.tfm)
Requires:       tex(tcbx1095.tfm)
Requires:       tex(tcbx1200.tfm)
Requires:       tex(tcbx1440.tfm)
Requires:       tex(tcbx1728.tfm)
Requires:       tex(tcbx2074.tfm)
Requires:       tex(tcbx2488.tfm)
Requires:       tex(tcbx2986.tfm)
Requires:       tex(tcbx3583.tfm)
Requires:       tex(tcit0800.tfm)
Requires:       tex(tcit0900.tfm)
Requires:       tex(tcit1000.tfm)
Requires:       tex(tcit1095.tfm)
Requires:       tex(tcit1200.tfm)
Requires:       tex(tcit1440.tfm)
Requires:       tex(tcit1728.tfm)
Requires:       tex(tcit2074.tfm)
Requires:       tex(tcit2488.tfm)
Requires:       tex(tcit2986.tfm)
Requires:       tex(tcit3583.tfm)
Requires:       tex(tcrb0500.tfm)
Requires:       tex(tcrb0600.tfm)
Requires:       tex(tcrb0700.tfm)
Requires:       tex(tcrb0800.tfm)
Requires:       tex(tcrb0900.tfm)
Requires:       tex(tcrb1000.tfm)
Requires:       tex(tcrb1095.tfm)
Requires:       tex(tcrb1200.tfm)
Requires:       tex(tcrb1440.tfm)
Requires:       tex(tcrb1728.tfm)
Requires:       tex(tcrb2074.tfm)
Requires:       tex(tcrb2488.tfm)
Requires:       tex(tcrb2986.tfm)
Requires:       tex(tcrb3583.tfm)
Requires:       tex(tcrm0500.tfm)
Requires:       tex(tcrm0600.tfm)
Requires:       tex(tcrm0700.tfm)
Requires:       tex(tcrm0800.tfm)
Requires:       tex(tcrm0900.tfm)
Requires:       tex(tcrm1000.tfm)
Requires:       tex(tcrm1095.tfm)
Requires:       tex(tcrm1200.tfm)
Requires:       tex(tcrm1440.tfm)
Requires:       tex(tcrm1728.tfm)
Requires:       tex(tcrm2074.tfm)
Requires:       tex(tcrm2488.tfm)
Requires:       tex(tcrm2986.tfm)
Requires:       tex(tcrm3583.tfm)
Requires:       tex(tcsi0500.tfm)
Requires:       tex(tcsi0600.tfm)
Requires:       tex(tcsi0700.tfm)
Requires:       tex(tcsi0800.tfm)
Requires:       tex(tcsi0900.tfm)
Requires:       tex(tcsi1000.tfm)
Requires:       tex(tcsi1095.tfm)
Requires:       tex(tcsi1200.tfm)
Requires:       tex(tcsi1440.tfm)
Requires:       tex(tcsi1728.tfm)
Requires:       tex(tcsi2074.tfm)
Requires:       tex(tcsi2488.tfm)
Requires:       tex(tcsi2986.tfm)
Requires:       tex(tcsi3583.tfm)
Requires:       tex(tcsl0500.tfm)
Requires:       tex(tcsl0600.tfm)
Requires:       tex(tcsl0700.tfm)
Requires:       tex(tcsl0800.tfm)
Requires:       tex(tcsl0900.tfm)
Requires:       tex(tcsl1000.tfm)
Requires:       tex(tcsl1095.tfm)
Requires:       tex(tcsl1200.tfm)
Requires:       tex(tcsl1440.tfm)
Requires:       tex(tcsl1728.tfm)
Requires:       tex(tcsl2074.tfm)
Requires:       tex(tcsl2488.tfm)
Requires:       tex(tcsl2986.tfm)
Requires:       tex(tcsl3583.tfm)
Requires:       tex(tcso0500.tfm)
Requires:       tex(tcso0600.tfm)
Requires:       tex(tcso0700.tfm)
Requires:       tex(tcso0800.tfm)
Requires:       tex(tcso0900.tfm)
Requires:       tex(tcso1000.tfm)
Requires:       tex(tcso1095.tfm)
Requires:       tex(tcso1200.tfm)
Requires:       tex(tcso1440.tfm)
Requires:       tex(tcso1728.tfm)
Requires:       tex(tcso2074.tfm)
Requires:       tex(tcso2488.tfm)
Requires:       tex(tcso2986.tfm)
Requires:       tex(tcso3583.tfm)
Requires:       tex(tcss0500.tfm)
Requires:       tex(tcss0600.tfm)
Requires:       tex(tcss0700.tfm)
Requires:       tex(tcss0800.tfm)
Requires:       tex(tcss0900.tfm)
Requires:       tex(tcss1000.tfm)
Requires:       tex(tcss1095.tfm)
Requires:       tex(tcss1200.tfm)
Requires:       tex(tcss1440.tfm)
Requires:       tex(tcss1728.tfm)
Requires:       tex(tcss2074.tfm)
Requires:       tex(tcss2488.tfm)
Requires:       tex(tcss2986.tfm)
Requires:       tex(tcss3583.tfm)
Requires:       tex(tcst0800.tfm)
Requires:       tex(tcst0900.tfm)
Requires:       tex(tcst1000.tfm)
Requires:       tex(tcst1095.tfm)
Requires:       tex(tcst1200.tfm)
Requires:       tex(tcst1440.tfm)
Requires:       tex(tcst1728.tfm)
Requires:       tex(tcst2074.tfm)
Requires:       tex(tcst2488.tfm)
Requires:       tex(tcst2986.tfm)
Requires:       tex(tcst3583.tfm)
Requires:       tex(tcsx0500.tfm)
Requires:       tex(tcsx0600.tfm)
Requires:       tex(tcsx0700.tfm)
Requires:       tex(tcsx0800.tfm)
Requires:       tex(tcsx0900.tfm)
Requires:       tex(tcsx1000.tfm)
Requires:       tex(tcsx1095.tfm)
Requires:       tex(tcsx1200.tfm)
Requires:       tex(tcsx1440.tfm)
Requires:       tex(tcsx1728.tfm)
Requires:       tex(tcsx2074.tfm)
Requires:       tex(tcsx2488.tfm)
Requires:       tex(tcsx2986.tfm)
Requires:       tex(tcsx3583.tfm)
Requires:       tex(tcti0500.tfm)
Requires:       tex(tcti0600.tfm)
Requires:       tex(tcti0700.tfm)
Requires:       tex(tcti0800.tfm)
Requires:       tex(tcti0900.tfm)
Requires:       tex(tcti1000.tfm)
Requires:       tex(tcti1095.tfm)
Requires:       tex(tcti1200.tfm)
Requires:       tex(tcti1440.tfm)
Requires:       tex(tcti1728.tfm)
Requires:       tex(tcti2074.tfm)
Requires:       tex(tcti2488.tfm)
Requires:       tex(tcti2986.tfm)
Requires:       tex(tcti3583.tfm)
Requires:       tex(tctt0800.tfm)
Requires:       tex(tctt0900.tfm)
Requires:       tex(tctt1000.tfm)
Requires:       tex(tctt1095.tfm)
Requires:       tex(tctt1200.tfm)
Requires:       tex(tctt1440.tfm)
Requires:       tex(tctt1728.tfm)
Requires:       tex(tctt2074.tfm)
Requires:       tex(tctt2488.tfm)
Requires:       tex(tctt2986.tfm)
Requires:       tex(tctt3583.tfm)
Requires:       tex(tcui0500.tfm)
Requires:       tex(tcui0600.tfm)
Requires:       tex(tcui0700.tfm)
Requires:       tex(tcui0800.tfm)
Requires:       tex(tcui0900.tfm)
Requires:       tex(tcui1000.tfm)
Requires:       tex(tcui1095.tfm)
Requires:       tex(tcui1200.tfm)
Requires:       tex(tcui1440.tfm)
Requires:       tex(tcui1728.tfm)
Requires:       tex(tcui2074.tfm)
Requires:       tex(tcui2488.tfm)
Requires:       tex(tcui2986.tfm)
Requires:       tex(tcui3583.tfm)
Requires:       tex(tcvi0800.tfm)
Requires:       tex(tcvi0900.tfm)
Requires:       tex(tcvi1000.tfm)
Requires:       tex(tcvi1095.tfm)
Requires:       tex(tcvi1200.tfm)
Requires:       tex(tcvi1440.tfm)
Requires:       tex(tcvi1728.tfm)
Requires:       tex(tcvi2074.tfm)
Requires:       tex(tcvi2488.tfm)
Requires:       tex(tcvi2986.tfm)
Requires:       tex(tcvi3583.tfm)
Requires:       tex(tcvt0800.tfm)
Requires:       tex(tcvt0900.tfm)
Requires:       tex(tcvt1000.tfm)
Requires:       tex(tcvt1095.tfm)
Requires:       tex(tcvt1200.tfm)
Requires:       tex(tcvt1440.tfm)
Requires:       tex(tcvt1728.tfm)
Requires:       tex(tcvt2074.tfm)
Requires:       tex(tcvt2488.tfm)
Requires:       tex(tcvt2986.tfm)
Requires:       tex(tcvt3583.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source250:      hfoldsty.tar.xz
Source251:      hfoldsty.doc.tar.xz

%description -n texlive-hfoldsty
The hfoldsty package provides virtual fonts for using oldstyle
(0123456789) figures with the European Computer Modern fonts.
It does a similar job as the eco package by Sebastian Kirsch
but includes a couple of improvements, i.e., better kerning
with guillemets, and support for character protruding using the
pdfcprot package.

%package -n texlive-hfoldsty-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.15svn29349
Release:        0
Summary:        Documentation for texlive-hfoldsty
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hfoldsty-doc
This package includes the documentation for texlive-hfoldsty

%post -n texlive-hfoldsty
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hfoldsty 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hfoldsty
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hfoldsty-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/hfoldsty/ChangeLog
%{_texmfdistdir}/doc/fonts/hfoldsty/Makefile
%{_texmfdistdir}/doc/fonts/hfoldsty/README
%{_texmfdistdir}/doc/fonts/hfoldsty/TODO
%{_texmfdistdir}/doc/fonts/hfoldsty/gpl.txt
%{_texmfdistdir}/doc/fonts/hfoldsty/hfoldsty.pdf
%{_texmfdistdir}/doc/fonts/hfoldsty/hfoldsty.xml
%{_texmfdistdir}/doc/fonts/hfoldsty/test-eco-hfo.tex
%{_texmfdistdir}/doc/fonts/hfoldsty/test-eco.tex
%{_texmfdistdir}/doc/fonts/hfoldsty/test-hfo.tex

%files -n texlive-hfoldsty
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobl3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfobx3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfocc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfodh3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoit3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfooc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hforb3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hform3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosl3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoso3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoss3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfost3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfosx3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfotc3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoti3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfott3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoui3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovi3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfovt3583.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0500.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0600.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0700.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0800.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc0900.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1000.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1095.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1200.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1440.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc1728.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc2074.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc2488.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc2986.tfm
%{_texmfdistdir}/fonts/tfm/public/hfoldsty/hfoxc3583.tfm
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobi3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobl3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfobx3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfocc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfodh3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoit3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfooc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hforb3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hform3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosi3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosl3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoso3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoss3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfost3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfosx3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfotc3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoti3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfott3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoui3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovi3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfovt3583.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0500.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0600.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0700.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0800.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc0900.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1000.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1095.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1200.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1440.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc1728.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc2074.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc2488.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc2986.vf
%{_texmfdistdir}/fonts/vf/public/hfoldsty/hfoxc3583.vf
%{_texmfdistdir}/tex/latex/hfoldsty/hfoldsty.sty
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hforbxslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hformslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossbxslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmitT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmitTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmnT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmnTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmslT1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/hfossmslTS1.cpa
%{_texmfdistdir}/tex/latex/hfoldsty/omlhfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/omshfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfodh.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfoss.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfott.fd
%{_texmfdistdir}/tex/latex/hfoldsty/t1hfovt.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfor.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfoss.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfott.fd
%{_texmfdistdir}/tex/latex/hfoldsty/ts1hfovtt.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hfoldsty-%{texlive_version}.%{texlive_noarch}.1.15svn29349-%{release}-zypper
%endif

%package -n texlive-hhtensor
Version:        %{texlive_version}.%{texlive_noarch}.0.0.61svn54080
Release:        0
Summary:        Print vectors, matrices, and tensors
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
Recommends:     texlive-hhtensor-doc >= %{texlive_version}
Provides:       tex(hhtensor.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(ushort.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source252:      hhtensor.tar.xz
Source253:      hhtensor.doc.tar.xz

%description -n texlive-hhtensor
This package provides commands for vectors, matrices, and
tensors with different styles -- arrows (as the LaTeX default),
underlined, and bold.

%package -n texlive-hhtensor-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.61svn54080
Release:        0
Summary:        Documentation for texlive-hhtensor
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hhtensor-doc
This package includes the documentation for texlive-hhtensor

%post -n texlive-hhtensor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hhtensor 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hhtensor
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hhtensor-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hhtensor/ChangeLog
%{_texmfdistdir}/doc/latex/hhtensor/Makefile
%{_texmfdistdir}/doc/latex/hhtensor/README
%{_texmfdistdir}/doc/latex/hhtensor/getversion.tex
%{_texmfdistdir}/doc/latex/hhtensor/hhtensor.pdf

%files -n texlive-hhtensor
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hhtensor/hhtensor.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hhtensor-%{texlive_version}.%{texlive_noarch}.0.0.61svn54080-%{release}-zypper
%endif

%package -n texlive-histogr
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Draw histograms with the LaTeX picture environment
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
Recommends:     texlive-histogr-doc >= %{texlive_version}
Provides:       tex(histogr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source254:      histogr.tar.xz
Source255:      histogr.doc.tar.xz

%description -n texlive-histogr
This is a collection pf macros to draw histogram bars inside a
LaTeX picture-environment.

%package -n texlive-histogr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Documentation for texlive-histogr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-histogr-doc
This package includes the documentation for texlive-histogr

%post -n texlive-histogr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-histogr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-histogr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-histogr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/histogr/histogr.pdf

%files -n texlive-histogr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/histogr/histogr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-histogr-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif

%package -n texlive-historische-zeitschrift
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn42635
Release:        0
Summary:        BibLaTeX style for the journal 'Historische Zeitschrift'
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
Recommends:     texlive-historische-zeitschrift-doc >= %{texlive_version}
Provides:       tex(historische-zeitschrift.bbx)
Provides:       tex(historische-zeitschrift.cbx)
Provides:       tex(historische-zeitschrift.lbx)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source256:      historische-zeitschrift.tar.xz
Source257:      historische-zeitschrift.doc.tar.xz

%description -n texlive-historische-zeitschrift
The package provides citations according with the house style
of the 'Historische Zeitschrift', a German historical journal.
The scheme is a fullcite for the first citation and 'Author,
Shorttitle (as note N, P)' for later citations (P being the
page number). For further details, see the description of the
house style at the journal's site. The package depends on
BibLaTeX (version 3.3 or higher) as well as etoolbox (version
1.5 or higher).

%package -n texlive-historische-zeitschrift-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn42635
Release:        0
Summary:        Documentation for texlive-historische-zeitschrift
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-historische-zeitschrift-doc:de;en)

%description -n texlive-historische-zeitschrift-doc
This package includes the documentation for texlive-historische-zeitschrift

%post -n texlive-historische-zeitschrift
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-historische-zeitschrift 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-historische-zeitschrift
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-historische-zeitschrift-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/historische-zeitschrift/CHANGES
%{_texmfdistdir}/doc/latex/historische-zeitschrift/LIESMICH
%{_texmfdistdir}/doc/latex/historische-zeitschrift/README

%files -n texlive-historische-zeitschrift
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/historische-zeitschrift/historische-zeitschrift.bbx
%{_texmfdistdir}/tex/latex/historische-zeitschrift/historische-zeitschrift.cbx
%{_texmfdistdir}/tex/latex/historische-zeitschrift/historische-zeitschrift.lbx
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-historische-zeitschrift-%{texlive_version}.%{texlive_noarch}.1.2svn42635-%{release}-zypper
%endif

%package -n texlive-hitec
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0betasvn15878
Release:        0
Summary:        Class for documentation
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
Recommends:     texlive-hitec-doc >= %{texlive_version}
Provides:       tex(hitec.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source258:      hitec.tar.xz
Source259:      hitec.doc.tar.xz

%description -n texlive-hitec
An article-based class designed for use for documentation in
high-technology companies.

%package -n texlive-hitec-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0betasvn15878
Release:        0
Summary:        Documentation for texlive-hitec
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hitec-doc
This package includes the documentation for texlive-hitec

%post -n texlive-hitec
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hitec 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hitec
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hitec-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hitec/README
%{_texmfdistdir}/doc/latex/hitec/hitec_doc.pdf
%{_texmfdistdir}/doc/latex/hitec/hitec_doc.tex

%files -n texlive-hitec
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hitec/hitec.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hitec-%{texlive_version}.%{texlive_noarch}.0.0.0betasvn15878-%{release}-zypper
%endif

%package -n texlive-hithesis
Version:        %{texlive_version}.%{texlive_noarch}.2.0.11svn53362
Release:        0
Summary:        Harbin Institute of Technology Thesis Template
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
Recommends:     texlive-hithesis-doc >= %{texlive_version}
Provides:       tex(ctex-fontset-siyuan.def)
Provides:       tex(hithesis.cfg)
Provides:       tex(hithesis.cls)
Provides:       tex(hithesis.sty)
Requires:       tex(CJKfntef.sty)
Requires:       tex(algorithm2e.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(ccaption.sty)
Requires:       tex(changepage.sty)
Requires:       tex(courier.sty)
Requires:       tex(ctexbook.cls)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(flafter.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(layout.sty)
Requires:       tex(layouts.sty)
Requires:       tex(lineno.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(natbib.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pifont.sty)
Requires:       tex(placeins.sty)
Requires:       tex(rotating.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(splitidx.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source260:      hithesis.tar.xz
Source261:      hithesis.doc.tar.xz

%description -n texlive-hithesis
hithesis is a LaTeX thesis template package for Harbin
Institute of Technology supporting bachelor, master, doctor
dissertations.

%package -n texlive-hithesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0.11svn53362
Release:        0
Summary:        Documentation for texlive-hithesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hithesis-doc:zh)

%description -n texlive-hithesis-doc
This package includes the documentation for texlive-hithesis

%post -n texlive-hithesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hithesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hithesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hithesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hithesis/README.md
%{_texmfdistdir}/doc/latex/hithesis/back/acknowledgements.tex
%{_texmfdistdir}/doc/latex/hithesis/back/appA.tex
%{_texmfdistdir}/doc/latex/hithesis/back/appendix01.tex
%{_texmfdistdir}/doc/latex/hithesis/back/ceindex.tex
%{_texmfdistdir}/doc/latex/hithesis/back/conclusion.tex
%{_texmfdistdir}/doc/latex/hithesis/back/publications.tex
%{_texmfdistdir}/doc/latex/hithesis/back/resume.tex
%{_texmfdistdir}/doc/latex/hithesis/body/introduction.tex
%{_texmfdistdir}/doc/latex/hithesis/dtx-style.sty
%{_texmfdistdir}/doc/latex/hithesis/figures/bthesistitle.eps
%{_texmfdistdir}/doc/latex/hithesis/figures/golfer.eps
%{_texmfdistdir}/doc/latex/hithesis/figures/hitlogo.eps
%{_texmfdistdir}/doc/latex/hithesis/front/cover.tex
%{_texmfdistdir}/doc/latex/hithesis/front/denotation.tex
%{_texmfdistdir}/doc/latex/hithesis/hithesis.pdf
%{_texmfdistdir}/doc/latex/hithesis/latexmkrc
%{_texmfdistdir}/doc/latex/hithesis/main.pdf
%{_texmfdistdir}/doc/latex/hithesis/main.tex
%{_texmfdistdir}/doc/latex/hithesis/reference.bib
%{_texmfdistdir}/doc/latex/hithesis/wct1.eps
%{_texmfdistdir}/doc/latex/hithesis/wct10.eps
%{_texmfdistdir}/doc/latex/hithesis/wct5.eps
%{_texmfdistdir}/doc/latex/hithesis/zfb.eps

%files -n texlive-hithesis
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/hithesis/hithesis.bst
%{_texmfdistdir}/makeindex/hithesis/hithesis.ist
%{_texmfdistdir}/tex/latex/hithesis/ctex-fontset-siyuan.def
%{_texmfdistdir}/tex/latex/hithesis/hithesis.cfg
%{_texmfdistdir}/tex/latex/hithesis/hithesis.cls
%{_texmfdistdir}/tex/latex/hithesis/hithesis.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hithesis-%{texlive_version}.%{texlive_noarch}.2.0.11svn53362-%{release}-zypper
%endif

%package -n texlive-hitszbeamer
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn54381
Release:        0
Summary:        A beamer theme for Harbin Institute of Technology, ShenZhen
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
Recommends:     texlive-hitszbeamer-doc >= %{texlive_version}
Provides:       tex(beamercolorthemehitszbeamer.sty)
Provides:       tex(beamerinnerthemehitszbeamer.sty)
Provides:       tex(beamerouterthemehitszbeamer.sty)
Provides:       tex(beamerthemehitszbeamer.sty)
Requires:       tex(calc.sty)
Requires:       tex(ctex.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multimedia.sty)
Requires:       tex(natbib.sty)
Requires:       tex(pgf.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source262:      hitszbeamer.tar.xz
Source263:      hitszbeamer.doc.tar.xz

%description -n texlive-hitszbeamer
This is a beamer theme designed for Harbin Institute of
Technology, ShenZhen (HITSZ).

%package -n texlive-hitszbeamer-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn54381
Release:        0
Summary:        Documentation for texlive-hitszbeamer
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hitszbeamer-doc:zh)

%description -n texlive-hitszbeamer-doc
This package includes the documentation for texlive-hitszbeamer

%post -n texlive-hitszbeamer
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hitszbeamer 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hitszbeamer
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hitszbeamer-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hitszbeamer/README.md
%{_texmfdistdir}/doc/latex/hitszbeamer/dtx-style.sty
%{_texmfdistdir}/doc/latex/hitszbeamer/figures/hitlogo-mask.jpg
%{_texmfdistdir}/doc/latex/hitszbeamer/figures/hitlogo.jpg
%{_texmfdistdir}/doc/latex/hitszbeamer/hitszbeamer.pdf
%{_texmfdistdir}/doc/latex/hitszbeamer/main.pdf
%{_texmfdistdir}/doc/latex/hitszbeamer/main.tex
%{_texmfdistdir}/doc/latex/hitszbeamer/reference.bib

%files -n texlive-hitszbeamer
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/hitszbeamer/hitszbeamer.bst
%{_texmfdistdir}/tex/latex/hitszbeamer/beamercolorthemehitszbeamer.sty
%{_texmfdistdir}/tex/latex/hitszbeamer/beamerinnerthemehitszbeamer.sty
%{_texmfdistdir}/tex/latex/hitszbeamer/beamerouterthemehitszbeamer.sty
%{_texmfdistdir}/tex/latex/hitszbeamer/beamerthemehitszbeamer.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hitszbeamer-%{texlive_version}.%{texlive_noarch}.1.0.0svn54381-%{release}-zypper
%endif

%package -n texlive-hitszthesis
Version:        %{texlive_version}.%{texlive_noarch}.3.0.4svn54709
Release:        0
Summary:        A dissertation template for Harbin Institute of Technology, ShenZhen
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
Recommends:     texlive-hitszthesis-doc >= %{texlive_version}
Provides:       tex(hitszthesis.cls)
Provides:       tex(hitszthesis.sty)
Requires:       tex(CJKfntef.sty)
Requires:       tex(algorithm2e.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(ccaption.sty)
Requires:       tex(changepage.sty)
Requires:       tex(ctexbook.cls)
Requires:       tex(enumitem.sty)
Requires:       tex(environ.sty)
Requires:       tex(etex.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(flafter.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(glossaries.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(layout.sty)
Requires:       tex(layouts.sty)
Requires:       tex(lineno.sty)
Requires:       tex(lipsum.sty)
Requires:       tex(listings.sty)
Requires:       tex(longtable.sty)
Requires:       tex(mathrsfs.sty)
Requires:       tex(multicol.sty)
Requires:       tex(multirow.sty)
Requires:       tex(natbib.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(ntheorem.sty)
Requires:       tex(pdfpages.sty)
Requires:       tex(pifont.sty)
Requires:       tex(placeins.sty)
Requires:       tex(rotating.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(splitidx.sty)
Requires:       tex(subeqnarray.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tikz.sty)
Requires:       tex(varwidth.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xltxtra.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source264:      hitszthesis.tar.xz
Source265:      hitszthesis.doc.tar.xz

%description -n texlive-hitszthesis
This package provides a dissertation template for Harbin
Institute of Technology, ShenZhen (HITSZ), including bachelor,
master and doctor dissertations.

%package -n texlive-hitszthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0.4svn54709
Release:        0
Summary:        Documentation for texlive-hitszthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hitszthesis-doc:zh)

%description -n texlive-hitszthesis-doc
This package includes the documentation for texlive-hitszthesis

%post -n texlive-hitszthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hitszthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hitszthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hitszthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hitszthesis/README.md
%{_texmfdistdir}/doc/latex/hitszthesis/back/acknowledgements.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/appendix01.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/appendix02.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/appendix03.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/appendixA.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/appendixB.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/ceindex.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/conclusion.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/publications.tex
%{_texmfdistdir}/doc/latex/hitszthesis/back/resume.tex
%{_texmfdistdir}/doc/latex/hitszthesis/body/chapter01.tex
%{_texmfdistdir}/doc/latex/hitszthesis/body/chapter02.tex
%{_texmfdistdir}/doc/latex/hitszthesis/body/chapter03.tex
%{_texmfdistdir}/doc/latex/hitszthesis/body/chapter04.tex
%{_texmfdistdir}/doc/latex/hitszthesis/body/chapter05.tex
%{_texmfdistdir}/doc/latex/hitszthesis/body/chapter06.tex
%{_texmfdistdir}/doc/latex/hitszthesis/ctex-fontset-siyuan.def
%{_texmfdistdir}/doc/latex/hitszthesis/dtx-style.sty
%{_texmfdistdir}/doc/latex/hitszthesis/figures/bthesistitle.eps
%{_texmfdistdir}/doc/latex/hitszthesis/figures/golfer.eps
%{_texmfdistdir}/doc/latex/hitszthesis/figures/hitlogo.eps
%{_texmfdistdir}/doc/latex/hitszthesis/front/coverinformation.tex
%{_texmfdistdir}/doc/latex/hitszthesis/front/denotation.tex
%{_texmfdistdir}/doc/latex/hitszthesis/hitszthesis.cfg
%{_texmfdistdir}/doc/latex/hitszthesis/hitszthesis.pdf
%{_texmfdistdir}/doc/latex/hitszthesis/latexmkrc
%{_texmfdistdir}/doc/latex/hitszthesis/main-bachelor.pdf
%{_texmfdistdir}/doc/latex/hitszthesis/main-doctor.pdf
%{_texmfdistdir}/doc/latex/hitszthesis/main-master.pdf
%{_texmfdistdir}/doc/latex/hitszthesis/main.tex
%{_texmfdistdir}/doc/latex/hitszthesis/reference.bib

%files -n texlive-hitszthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/hitszthesis/hitszthesis.bst
%{_texmfdistdir}/makeindex/hitszthesis/hitszthesis.ist
%{_texmfdistdir}/tex/latex/hitszthesis/hitszthesis.cls
%{_texmfdistdir}/tex/latex/hitszthesis/hitszthesis.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hitszthesis-%{texlive_version}.%{texlive_noarch}.3.0.4svn54709-%{release}-zypper
%endif

%package -n texlive-hletter
Version:        %{texlive_version}.%{texlive_noarch}.4.2svn30002
Release:        0
Summary:        Flexible letter typesetting with flexible page headings
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
Recommends:     texlive-hletter-doc >= %{texlive_version}
Provides:       tex(hdefine.clo)
Provides:       tex(hhead.sty)
Provides:       tex(hlete.clo)
Provides:       tex(hletf.clo)
Provides:       tex(hletg.clo)
Provides:       tex(hletter.cls)
Provides:       tex(hsetup.sty)
Provides:       tex(mergeh.sty)
Requires:       tex(babel.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source266:      hletter.tar.xz
Source267:      hletter.doc.tar.xz

%description -n texlive-hletter
The package permits the user to specify easily, with the aid of
self defined key-words, letters (with a logo and private) and
headings. The heading may include a footer and the letter
provides commands to include a scanned signature and two
signees. The package works with the merge package.

%package -n texlive-hletter-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.2svn30002
Release:        0
Summary:        Documentation for texlive-hletter
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hletter-doc
This package includes the documentation for texlive-hletter

%post -n texlive-hletter
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hletter 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hletter
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hletter-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hletter/Bruennhilde.eps
%{_texmfdistdir}/doc/latex/hletter/Bruennhilde.jpg
%{_texmfdistdir}/doc/latex/hletter/Gccs.eps
%{_texmfdistdir}/doc/latex/hletter/Gccs.jpg
%{_texmfdistdir}/doc/latex/hletter/Hletter.pdf
%{_texmfdistdir}/doc/latex/hletter/README
%{_texmfdistdir}/doc/latex/hletter/Testheader.tex
%{_texmfdistdir}/doc/latex/hletter/Testletter1.tex
%{_texmfdistdir}/doc/latex/hletter/Testletter2.tex
%{_texmfdistdir}/doc/latex/hletter/Testletter3.tex
%{_texmfdistdir}/doc/latex/hletter/Testmerge.dat
%{_texmfdistdir}/doc/latex/hletter/Testmerge.tex
%{_texmfdistdir}/doc/latex/hletter/signat.eps
%{_texmfdistdir}/doc/latex/hletter/signat.jpg

%files -n texlive-hletter
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hletter/hdefine.clo
%{_texmfdistdir}/tex/latex/hletter/hhead.sty
%{_texmfdistdir}/tex/latex/hletter/hlete.clo
%{_texmfdistdir}/tex/latex/hletter/hletf.clo
%{_texmfdistdir}/tex/latex/hletter/hletg.clo
%{_texmfdistdir}/tex/latex/hletter/hletter.cls
%{_texmfdistdir}/tex/latex/hletter/hsetup.sty
%{_texmfdistdir}/tex/latex/hletter/mergeh.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hletter-%{texlive_version}.%{texlive_noarch}.4.2svn30002-%{release}-zypper
%endif

%package -n texlive-hlist
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn44983
Release:        0
Summary:        Horizontal and columned lists
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
Recommends:     texlive-hlist-doc >= %{texlive_version}
Provides:       tex(hlist.sty)
Provides:       tex(hlist.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source268:      hlist.tar.xz
Source269:      hlist.doc.tar.xz

%description -n texlive-hlist
This plain TeX and LaTeX package provides the "hlist"
environment in which \hitem starts a horizontal and columned
item. It depends upon the simplekv package.

%package -n texlive-hlist-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn44983
Release:        0
Summary:        Documentation for texlive-hlist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hlist-doc
This package includes the documentation for texlive-hlist

%post -n texlive-hlist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hlist 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hlist
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hlist-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/hlist/README
%{_texmfdistdir}/doc/generic/hlist/hlist-fr.pdf
%{_texmfdistdir}/doc/generic/hlist/hlist-fr.tex

%files -n texlive-hlist
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hlist/hlist.sty
%{_texmfdistdir}/tex/generic/hlist/hlist.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hlist-%{texlive_version}.%{texlive_noarch}.0.0.11svn44983-%{release}-zypper
%endif

%package -n texlive-hmtrump
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn54512
Release:        0
Summary:        Describe card games
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
Requires:       texlive-hmtrump-fonts >= %{texlive_version}
Recommends:     texlive-hmtrump-doc >= %{texlive_version}
Provides:       tex(hmtrump.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source270:      hmtrump.tar.xz
Source271:      hmtrump.doc.tar.xz

%description -n texlive-hmtrump
This package provides a font with LuaLaTeX support for
describing card games.

%package -n texlive-hmtrump-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn54512
Release:        0
Summary:        Documentation for texlive-hmtrump
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hmtrump-doc:ja)

%description -n texlive-hmtrump-doc
This package includes the documentation for texlive-hmtrump


%package -n texlive-hmtrump-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn54512
Release:        0
Summary:        Severed fonts for texlive-hmtrump
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-hmtrump-fonts
The  separated fonts package for texlive-hmtrump
%post -n texlive-hmtrump
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hmtrump 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hmtrump
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-hmtrump-fonts
%files -n texlive-hmtrump-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/lualatex/hmtrump/README.md
%{_texmfdistdir}/doc/lualatex/hmtrump/by-sa.png
%{_texmfdistdir}/doc/lualatex/hmtrump/hmtrump-sample.pdf
%{_texmfdistdir}/doc/lualatex/hmtrump/hmtrump-sample.tex
%{_texmfdistdir}/doc/lualatex/hmtrump/hmtrump.pdf
%{_texmfdistdir}/doc/lualatex/hmtrump/hmtrump.tex
%{_texmfdistdir}/doc/lualatex/hmtrump/nkd04_playing_cards_index/LICENSE
%{_texmfdistdir}/doc/lualatex/hmtrump/nkd04_playing_cards_index/readme.txt

%files -n texlive-hmtrump
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/truetype/public/hmtrump/nkd04_playing_cards_index.ttf
%{_texmfdistdir}/tex/lualatex/hmtrump/hmtrump.sty

%files -n texlive-hmtrump-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-hmtrump
%{_datadir}/fontconfig/conf.avail/58-texlive-hmtrump.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hmtrump/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hmtrump/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-hmtrump/fonts.scale
%{_datadir}/fonts/texlive-hmtrump/nkd04_playing_cards_index.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hmtrump-fonts-%{texlive_version}.%{texlive_noarch}.1.2asvn54512-%{release}-zypper
%endif

%package -n texlive-hobby
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn44474
Release:        0
Summary:        An implementation of Hobby's algorithm for PGF/TikZ
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
Recommends:     texlive-hobby-doc >= %{texlive_version}
Provides:       tex(hobby.code.tex)
Provides:       tex(pgflibraryhobby.code.tex)
Provides:       tex(pml3array.sty)
Provides:       tex(tikzlibraryhobby.code.tex)
Requires:       tex(expl3.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source272:      hobby.tar.xz
Source273:      hobby.doc.tar.xz

%description -n texlive-hobby
This package defines a path generation function for PGF/TikZ
which implements Hobby's algorithm for a path built out of
Bezier curves which passes through a given set of points. The
path thus generated may by used as a TikZ 'to path'. The
implementation is in LaTeX3.

%package -n texlive-hobby-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.8svn44474
Release:        0
Summary:        Documentation for texlive-hobby
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hobby-doc
This package includes the documentation for texlive-hobby

%post -n texlive-hobby
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hobby 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hobby
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hobby-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hobby/README
%{_texmfdistdir}/doc/latex/hobby/hobby.pdf
%{_texmfdistdir}/doc/latex/hobby/hobby_code.pdf
%{_texmfdistdir}/doc/latex/hobby/hobby_doc.tex

%files -n texlive-hobby
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hobby/hobby.code.tex
%{_texmfdistdir}/tex/latex/hobby/pgflibraryhobby.code.tex
%{_texmfdistdir}/tex/latex/hobby/pml3array.sty
%{_texmfdistdir}/tex/latex/hobby/tikzlibraryhobby.code.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hobby-%{texlive_version}.%{texlive_noarch}.1.8svn44474-%{release}-zypper
%endif

%package -n texlive-hobete
Version:        %{texlive_version}.%{texlive_noarch}.svn27036
Release:        0
Summary:        Unofficial beamer theme for the University of Hohenheim
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
Recommends:     texlive-hobete-doc >= %{texlive_version}
Provides:       tex(beamercolorthemehohenheim.sty)
Provides:       tex(beamerouterthemehohenheim.sty)
Provides:       tex(beamerouterthemehohenheimposter.sty)
Provides:       tex(beamerthemehohenheim.sty)
Provides:       tex(hobete.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xfrac.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source274:      hobete.tar.xz
Source275:      hobete.doc.tar.xz

%description -n texlive-hobete
The package provides a beamer theme which features the Ci
colors of the University of Hohenheim. Please note that this is
not an official Theme, and that there will be no support for
it, from the University. Furthermore there is NO relationship
between the University and this theme.

%package -n texlive-hobete-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn27036
Release:        0
Summary:        Documentation for texlive-hobete
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-hobete-doc:de)

%description -n texlive-hobete-doc
This package includes the documentation for texlive-hobete

%post -n texlive-hobete
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hobete 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hobete
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hobete-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hobete/README
%{_texmfdistdir}/doc/latex/hobete/hobete_doc.pdf
%{_texmfdistdir}/doc/latex/hobete/hobete_doc.tex
%{_texmfdistdir}/doc/latex/hobete/poster-test.tex

%files -n texlive-hobete
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hobete/beamercolorthemehohenheim.sty
%{_texmfdistdir}/tex/latex/hobete/beamerouterthemehohenheim.sty
%{_texmfdistdir}/tex/latex/hobete/beamerouterthemehohenheimposter.sty
%{_texmfdistdir}/tex/latex/hobete/beamerthemehohenheim.sty
%{_texmfdistdir}/tex/latex/hobete/hobete.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hobete-%{texlive_version}.%{texlive_noarch}.svn27036-%{release}-zypper
%endif

%package -n texlive-hobsub
Version:        %{texlive_version}.%{texlive_noarch}.svn52810
Release:        0
Summary:        Construct package bundles
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
Recommends:     texlive-hobsub-doc >= %{texlive_version}
Provides:       tex(hobsub-generic.sty)
Provides:       tex(hobsub-hyperref.sty)
Provides:       tex(hobsub.sty)
Requires:       tex(auxhook.sty)
Requires:       tex(bigintcalc.sty)
Requires:       tex(etexcmds.sty)
Requires:       tex(hycolor.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(intcalc.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvdefinekeys.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdfescape.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source276:      hobsub.tar.xz
Source277:      hobsub.doc.tar.xz

%description -n texlive-hobsub
Heiko Oberdiek's hobsub package (and hobsub-hyperref and
hobsub-generic packages) defined a mechanism for concatenating
multiple files into a single file for faster loading. The
disadvantage is that it introduces hard dependencies between
the source files that are included and complicates distribution
and updates. It was principally used with hyperref but is not
currently used in any standard packages in TeX Live. The
packages are still distributed as simple stubs that reference
the included packages via \RequirePackage rather than copying
their source. The documented source of the original packages is
available at github, but is not distributed to CTAN.

%package -n texlive-hobsub-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn52810
Release:        0
Summary:        Documentation for texlive-hobsub
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hobsub-doc
This package includes the documentation for texlive-hobsub

%post -n texlive-hobsub
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hobsub 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hobsub
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hobsub-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hobsub/README.md
%{_texmfdistdir}/doc/latex/hobsub/hobsub.pdf
%{_texmfdistdir}/doc/latex/hobsub/hobsub.tex

%files -n texlive-hobsub
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hobsub/hobsub-generic.sty
%{_texmfdistdir}/tex/latex/hobsub/hobsub-hyperref.sty
%{_texmfdistdir}/tex/latex/hobsub/hobsub.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hobsub-%{texlive_version}.%{texlive_noarch}.svn52810-%{release}-zypper
%endif

%package -n texlive-hologo
Version:        %{texlive_version}.%{texlive_noarch}.1.14svn53048
Release:        0
Summary:        A collection of logos with bookmark support
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
Recommends:     texlive-hologo-doc >= %{texlive_version}
Provides:       tex(hologo.sty)
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(kvdefinekeys.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source278:      hologo.tar.xz
Source279:      hologo.doc.tar.xz

%description -n texlive-hologo
The package defines a single command \hologo, whose argument is
the usual case-confused ASCII version of the logo. The command
is bookmark-enabled, so that every logo becomes available in
bookmarks without further work.

%package -n texlive-hologo-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.14svn53048
Release:        0
Summary:        Documentation for texlive-hologo
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hologo-doc
This package includes the documentation for texlive-hologo

%post -n texlive-hologo
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hologo 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hologo
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hologo-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hologo/README.md
%{_texmfdistdir}/doc/latex/hologo/example/hologo-example.tex
%{_texmfdistdir}/doc/latex/hologo/hologo.pdf

%files -n texlive-hologo
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/hologo/hologo.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hologo-%{texlive_version}.%{texlive_noarch}.1.14svn53048-%{release}-zypper
%endif

%package -n texlive-hook-pre-commit-pkg
Version:        %{texlive_version}.%{texlive_noarch}.1.1.2svn41378
Release:        0
Summary:        Pre-commit git hook for LaTeX package developpers
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
Source280:      hook-pre-commit-pkg.doc.tar.xz

%description -n texlive-hook-pre-commit-pkg
This package provides a pre-commit git hook to check basic
LaTeX syntax for the use of package developers. It is installed
by copying it into the .git/.hooks file. It then checks the
following file types: .sty, .dtx, .bbx, .cbx, and .lbx. List of
performed checks: Each line must be terminated by a %, without
a space before it. Empty lines are allowed, but not lines with
nothing but spaces in them. \begin{macro} and \end{macro} must
be paired. \begin{macrocode} and \end{macrocode} must be
paired. \begin{macro} must have a second argument. One space
must be printed between % and \begin{macro} or \end{macro}. %
must be the first character in the line. Four spaces must be
printed between % and \begin{macrocode} or \end{macrocode}. \cs
argument must not start with a backslash.
%post -n texlive-hook-pre-commit-pkg
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hook-pre-commit-pkg 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hook-pre-commit-pkg
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hook-pre-commit-pkg
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/hook-pre-commit-pkg/README
%{_texmfdistdir}/doc/support/hook-pre-commit-pkg/pre-commit-latex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hook-pre-commit-pkg-%{texlive_version}.%{texlive_noarch}.1.1.2svn41378-%{release}-zypper
%endif

%package -n texlive-horoscop
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn30530
Release:        0
Summary:        Generate astrological charts in LaTeX
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
Recommends:     texlive-horoscop-doc >= %{texlive_version}
Provides:       tex(horoscop.sty)
Requires:       tex(marvosym.sty)
Requires:       tex(pict2e.sty)
Requires:       tex(starfont.sty)
Requires:       tex(trig.sty)
Requires:       tex(wasysym.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source281:      horoscop.tar.xz
Source282:      horoscop.doc.tar.xz

%description -n texlive-horoscop
The horoscop package provides a unified interface for
astrological font packages; typesetting with pict2e of standard
wheel charts and some variations, in PostScript- and
PDF-generating TeX engines; and access to external calculation
software (Astrolog and Swiss Ephemeris) for computing object
positions.

%package -n texlive-horoscop-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.92svn30530
Release:        0
Summary:        Documentation for texlive-horoscop
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-horoscop-doc
This package includes the documentation for texlive-horoscop

%post -n texlive-horoscop
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-horoscop 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-horoscop
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-horoscop-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/horoscop/README
%{_texmfdistdir}/doc/latex/horoscop/horoscop.pdf

%files -n texlive-horoscop
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/horoscop/horoscop.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-horoscop-%{texlive_version}.%{texlive_noarch}.0.0.92svn30530-%{release}-zypper
%endif

%package -n texlive-hpsdiss
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        A dissertation class
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
Recommends:     texlive-hpsdiss-doc >= %{texlive_version}
Provides:       tex(hpsdiss.cls)
Requires:       tex(book.cls)
Requires:       tex(calc.sty)
Requires:       tex(colordvi.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(mparhack.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(rotating.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source283:      hpsdiss.tar.xz
Source284:      hpsdiss.doc.tar.xz

%description -n texlive-hpsdiss
The class was developed to typeset a dissertation at ETH
Zurich. The requirements were to use A5 paper and 10pt type. A
sample of the output is shown in the PDF documentation link.

%package -n texlive-hpsdiss-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn15878
Release:        0
Summary:        Documentation for texlive-hpsdiss
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hpsdiss-doc
This package includes the documentation for texlive-hpsdiss

%post -n texlive-hpsdiss
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hpsdiss 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hpsdiss
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hpsdiss-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hpsdiss/hpsdiss.pdf

%files -n texlive-hpsdiss
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hpsdiss/hpsdiss.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hpsdiss-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif

%package -n texlive-hrefhide
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn22255
Release:        0
Summary:        Suppress hyper links when printing
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
Recommends:     texlive-hrefhide-doc >= %{texlive_version}
Provides:       tex(hrefhide.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(xcolor.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source285:      hrefhide.tar.xz
Source286:      hrefhide.doc.tar.xz

%description -n texlive-hrefhide
This package provides the command \hrefdisplayonly (which
provides a substitute for \href). While the (hyperlinked) text
appears like an ordinary \href in the compiled PDF file, the
same text will be "hidden" when printing the text. (Hiding is
actually achieved by making the text the same colour as the
background, thus preserving the layout of the rest of the
text.)

%package -n texlive-hrefhide-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn22255
Release:        0
Summary:        Documentation for texlive-hrefhide
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-hrefhide-doc
This package includes the documentation for texlive-hrefhide

%post -n texlive-hrefhide
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-hrefhide 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-hrefhide
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-hrefhide-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/hrefhide/README
%{_texmfdistdir}/doc/latex/hrefhide/hrefhide-example.pdf
%{_texmfdistdir}/doc/latex/hrefhide/hrefhide-example.tex
%{_texmfdistdir}/doc/latex/hrefhide/hrefhide.pdf

%files -n texlive-hrefhide
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/hrefhide/hrefhide.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-hrefhide-%{texlive_version}.%{texlive_noarch}.1.0fsvn22255-%{release}-zypper
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
       %{buildroot}/var/adm/update-scripts/texlive-gitfile-info-%{texlive_version}.%{texlive_noarch}.0.0.5svn51928-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/support/gitfile-info/gfi-run.py \
	       %{_texmfdistdir}/doc/support/gitfile-info/post-commit.py \
	       %{_texmfdistdir}/doc/support/gitfile-info/post-merge.py
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/support/gitfile-info/gfi-run.py \
	       %{_texmfdistdir}/doc/support/gitfile-info/post-commit.py \
	       %{_texmfdistdir}/doc/support/gitfile-info/post-merge.py
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
       %{buildroot}/var/adm/update-scripts/texlive-gitinfo-%{texlive_version}.%{texlive_noarch}.1.0svn34049-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/gitinfo/post-xxx-sample.txt
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gitinfo2-%{texlive_version}.%{texlive_noarch}.2.0.7svn38913-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/gitinfo2/post-xxx-sample.txt
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gitlog-%{texlive_version}.%{texlive_noarch}.0.0.0.betasvn38932-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gitver-%{texlive_version}.%{texlive_noarch}.1.0svn49980-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-globalvals-%{texlive_version}.%{texlive_noarch}.1.1svn49962-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glosmathtools-%{texlive_version}.%{texlive_noarch}.1.0.0svn54558-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gloss-%{texlive_version}.%{texlive_noarch}.1.5.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gloss-occitan-%{texlive_version}.%{texlive_noarch}.0.0.1svn52593-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-%{texlive_version}.%{texlive_noarch}.4.46svn54402-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/glossaries/makeglossaries \
	       %{_texmfdistdir}/scripts/glossaries/makeglossaries-lite.lua
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
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-danish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-dutch-%{texlive_version}.%{texlive_noarch}.1.1svn35685-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-english-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-estonian-%{texlive_version}.%{texlive_noarch}.1.0svn49928-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-extra-%{texlive_version}.%{texlive_noarch}.1.45svn54688-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-finnish-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-french-%{texlive_version}.%{texlive_noarch}.1.1svn42873-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-german-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-irish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-italian-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-magyar-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-polish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-portuges-%{texlive_version}.%{texlive_noarch}.1.1svn36064-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-serbian-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-slovene-%{texlive_version}.%{texlive_noarch}.1.0svn51211-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glossaries-spanish-%{texlive_version}.%{texlive_noarch}.1.0svn35665-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-glyphlist-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gmdoc-%{texlive_version}.%{texlive_noarch}.0.0.993svn21292-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gmdoc-enhance-%{texlive_version}.%{texlive_noarch}.0.0.2svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gmiflink-%{texlive_version}.%{texlive_noarch}.0.0.97svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gmp-%{texlive_version}.%{texlive_noarch}.1.0svn21691-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gmutils-%{texlive_version}.%{texlive_noarch}.0.0.996svn24287-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gmverb-%{texlive_version}.%{texlive_noarch}.0.0.98svn24288-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gmverse-%{texlive_version}.%{texlive_noarch}.0.0.73svn29803-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gnu-freefont-fonts-%{texlive_version}.%{texlive_noarch}.svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong python scripts if any
    for scr in %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/MacTT \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/OpenType \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/TrueType \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/WOFF \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/kernclasses.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/ligatureLookups.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/private_use.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/range_report.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/script-menu/nameBySlot.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/checkGlyphNumbers.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/findBackLayers.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/isMonoMono.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/validate.py \
	       %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/metafont/bulk_eps_import.py
    do
        test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/python
		.
		w
		q
	EOF
    done
    # Add shebang e.g. correct perl wrapper scripts if any
    for scr in %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/fontforge-interp.sh
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /bin/sh
		.
		w
		q
	EOF
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/hex_range.py
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
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gnu-freefont
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gnu-freefont
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gnu-freefont/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gnu-freefont/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gnu-freefont/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gnu-freefont/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gnu-freefont.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gnu-freefont    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gnu-freefont/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gnuplottex-%{texlive_version}.%{texlive_noarch}.0.0.9.5svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-go-%{texlive_version}.%{texlive_noarch}.svn28628-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gobble-%{texlive_version}.%{texlive_noarch}.0.0.2svn49608-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gofonts-fonts-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gofonts
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/bh/gofonts/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/bh/gofonts/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gofonts
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gofonts/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gofonts/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gofonts/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gofonts/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gofonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gofonts    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gofonts/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-gofonts.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-gofonts/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-gofonts.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-gofonts.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gost-%{texlive_version}.%{texlive_noarch}.1.2isvn44131-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gothic-%{texlive_version}.%{texlive_noarch}.svn49869-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gotoh-%{texlive_version}.%{texlive_noarch}.1.1svn44764-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grabbox-%{texlive_version}.%{texlive_noarch}.1.4svn51052-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gradientframe-%{texlive_version}.%{texlive_noarch}.0.0.2svn21387-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gradstudentresume-%{texlive_version}.%{texlive_noarch}.svn38832-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grafcet-%{texlive_version}.%{texlive_noarch}.1.3.5svn22509-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grant-%{texlive_version}.%{texlive_noarch}.0.0.0.3svn41905-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graph35-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn47522-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphbox-%{texlive_version}.%{texlive_noarch}.1.1svn46360-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphics-%{texlive_version}.%{texlive_noarch}.svn53640-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphics-cfg-%{texlive_version}.%{texlive_noarch}.svn41448-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphics-def-%{texlive_version}.%{texlive_noarch}.svn54522-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphics-pln-%{texlive_version}.%{texlive_noarch}.svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphicx-psmin-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphicxbox-%{texlive_version}.%{texlive_noarch}.1.0svn32630-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphicxpsd-%{texlive_version}.%{texlive_noarch}.1.1svn46477-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-graphviz-%{texlive_version}.%{texlive_noarch}.0.0.94svn31517-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grayhints-%{texlive_version}.%{texlive_noarch}.svn49052-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-greek-fontenc-%{texlive_version}.%{texlive_noarch}.0.0.14svn53955-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Correct wrong luaTeX scripts if any
    for scr in %{_texmfdistdir}/doc/latex/greek-fontenc/lgr2licr.lua
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
       %{buildroot}/var/adm/update-scripts/texlive-greek-inputenc-%{texlive_version}.%{texlive_noarch}.1.7svn51612-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-greekdates-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-greektex-%{texlive_version}.%{texlive_noarch}.svn28327-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-greektonoi-%{texlive_version}.%{texlive_noarch}.svn39419-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-greenpoint-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gregoriotex-fonts-%{texlive_version}.%{texlive_noarch}.5.2.1svn51029-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-gregoriotex
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/gregoriotex/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-gregoriotex
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-gregoriotex/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-gregoriotex/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gregoriotex/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-gregoriotex/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-gregoriotex.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-gregoriotex    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-gregoriotex/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grfext-%{texlive_version}.%{texlive_noarch}.1.3svn53024-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grffile-%{texlive_version}.%{texlive_noarch}.2.1svn52756-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grfpaste-%{texlive_version}.%{texlive_noarch}.0.0.2svn17354-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grid-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grid-system-%{texlive_version}.%{texlive_noarch}.0.0.3.0svn32981-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gridset-%{texlive_version}.%{texlive_noarch}.0.0.3svn53762-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gridslides-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grotesq-fonts-%{texlive_version}.%{texlive_noarch}.svn35859-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-grotesq
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/urw/grotesq/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-grotesq
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-grotesq/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-grotesq/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-grotesq/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-grotesq/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-grotesq.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-grotesq    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-grotesq/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-grundgesetze-%{texlive_version}.%{texlive_noarch}.1.02svn34439-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gsemthesis-%{texlive_version}.%{texlive_noarch}.0.0.9.4svn36244-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gsftopk-%{texlive_version}.%{texlive_noarch}.1.19.2svn52851-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gtl-%{texlive_version}.%{texlive_noarch}.0.0.5svn49527-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gtrcrd-%{texlive_version}.%{texlive_noarch}.1.1svn32484-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gtrlib-largetrees-%{texlive_version}.%{texlive_noarch}.1.2bsvn49062-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gu-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-guide-to-latex-%{texlive_version}.%{texlive_noarch}.svn45712-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-guitar-%{texlive_version}.%{texlive_noarch}.1.6svn32258-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-guitarchordschemes-%{texlive_version}.%{texlive_noarch}.0.0.7svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-guitartabs-%{texlive_version}.%{texlive_noarch}.svn48102-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-guitlogo-%{texlive_version}.%{texlive_noarch}.1.0.0_alpha.3svn51582-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gustlib-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/tex/plain/gustlib/plmac218/plind.bat
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gustprog-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/support/gustprog/normtext.awk
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-gzt-%{texlive_version}.%{texlive_noarch}.1.0.0svn54390-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-h2020proposal-%{texlive_version}.%{texlive_noarch}.1.0svn38428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hackthefootline-%{texlive_version}.%{texlive_noarch}.svn46494-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hacm-fonts-%{texlive_version}.%{texlive_noarch}.0.0.1svn27671-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-hacm
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/hacm/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-hacm
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-hacm/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-hacm/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-hacm/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-hacm/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-hacm.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-hacm    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-hacm/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hagenberg-thesis-%{texlive_version}.%{texlive_noarch}.svn51150-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-halloweenmath-%{texlive_version}.%{texlive_noarch}.0.0.11svn52602-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-handin-%{texlive_version}.%{texlive_noarch}.0.0.1.1svn48255-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-handout-%{texlive_version}.%{texlive_noarch}.1.6.0svn43962-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hands-%{texlive_version}.%{texlive_noarch}.svn13293-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hang-%{texlive_version}.%{texlive_noarch}.2.1svn43280-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hanging-%{texlive_version}.%{texlive_noarch}.1.2bsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hanoi-%{texlive_version}.%{texlive_noarch}.20120101svn25019-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-happy4th-%{texlive_version}.%{texlive_noarch}.20120102svn25020-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-har2nat-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-haranoaji-fonts-%{texlive_version}.%{texlive_noarch}.20200418svn54784-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-haranoaji
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/haranoaji/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-haranoaji
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-haranoaji/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-haranoaji/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-haranoaji/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-haranoaji/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-haranoaji.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-haranoaji    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-haranoaji/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-haranoaji-extra-fonts-%{texlive_version}.%{texlive_noarch}.20200418svn54783-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-haranoaji-extra
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/haranoaji-extra/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-haranoaji-extra
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-haranoaji-extra/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-haranoaji-extra/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-haranoaji-extra/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-haranoaji-extra/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-haranoaji-extra.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-haranoaji-extra    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-haranoaji-extra/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hardwrap-%{texlive_version}.%{texlive_noarch}.0.0.2svn21396-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-harmony-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-harnon-cv-%{texlive_version}.%{texlive_noarch}.1.0svn26543-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-harpoon-%{texlive_version}.%{texlive_noarch}.1.0svn21327-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-harvard-%{texlive_version}.%{texlive_noarch}.2.0.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-harveyballs-%{texlive_version}.%{texlive_noarch}.1.1svn32003-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-harvmac-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hatching-%{texlive_version}.%{texlive_noarch}.0.0.11svn23818-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hausarbeit-jura-%{texlive_version}.%{texlive_noarch}.2.0svn50762-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-havannah-%{texlive_version}.%{texlive_noarch}.svn36348-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hc-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-he-she-%{texlive_version}.%{texlive_noarch}.1.3svn41359-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hecthese-%{texlive_version}.%{texlive_noarch}.1.3.2svn50590-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-helvetic-fonts-%{texlive_version}.%{texlive_noarch}.svn31835-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-helvetic
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/urw/helvetic/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-helvetic
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-helvetic/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-helvetic/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-helvetic/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-helvetic/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-helvetic.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-helvetic    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-helvetic/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hep-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hep-paper-%{texlive_version}.%{texlive_noarch}.1.2svn54300-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hepnames-%{texlive_version}.%{texlive_noarch}.2.0svn35722-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hepparticles-%{texlive_version}.%{texlive_noarch}.2.0svn35723-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hepthesis-%{texlive_version}.%{texlive_noarch}.1.5.2svn46054-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/hepthesis/example/getNewBibtex
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/bash or similar
    for scr in %{_texmfdistdir}/doc/latex/hepthesis/example/getNewBibtex
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@^#!.*bash@#!/bin/bash@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hepunits-%{texlive_version}.%{texlive_noarch}.2.0.0svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-here-%{texlive_version}.%{texlive_noarch}.svn16135-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-heuristica-fonts-%{texlive_version}.%{texlive_noarch}.1.092svn51362-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-heuristica
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/heuristica/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/heuristica/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-heuristica
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-heuristica/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-heuristica/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-heuristica/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-heuristica/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-heuristica.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-heuristica    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-heuristica/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-heuristica.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-heuristica/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-heuristica.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-heuristica.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hexgame-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hf-tikz-%{texlive_version}.%{texlive_noarch}.0.0.3asvn34733-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hfbright-fonts-%{texlive_version}.%{texlive_noarch}.svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-hfbright
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/hfbright/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-hfbright
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-hfbright/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-hfbright/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-hfbright/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-hfbright/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-hfbright.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-hfbright    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-hfbright/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hfoldsty-%{texlive_version}.%{texlive_noarch}.1.15svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hhtensor-%{texlive_version}.%{texlive_noarch}.0.0.61svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-histogr-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-historische-zeitschrift-%{texlive_version}.%{texlive_noarch}.1.2svn42635-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hitec-%{texlive_version}.%{texlive_noarch}.0.0.0betasvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hithesis-%{texlive_version}.%{texlive_noarch}.2.0.11svn53362-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hitszbeamer-%{texlive_version}.%{texlive_noarch}.1.0.0svn54381-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hitszthesis-%{texlive_version}.%{texlive_noarch}.3.0.4svn54709-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hletter-%{texlive_version}.%{texlive_noarch}.4.2svn30002-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hlist-%{texlive_version}.%{texlive_noarch}.0.0.11svn44983-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hmtrump-fonts-%{texlive_version}.%{texlive_noarch}.1.2asvn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-hmtrump
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/hmtrump/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-hmtrump
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-hmtrump/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-hmtrump/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-hmtrump/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-hmtrump/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-hmtrump.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-hmtrump    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-hmtrump/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hobby-%{texlive_version}.%{texlive_noarch}.1.8svn44474-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hobete-%{texlive_version}.%{texlive_noarch}.svn27036-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hobsub-%{texlive_version}.%{texlive_noarch}.svn52810-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:277} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hologo-%{texlive_version}.%{texlive_noarch}.1.14svn53048-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:278} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:279} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hook-pre-commit-pkg-%{texlive_version}.%{texlive_noarch}.1.1.2svn41378-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:280} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-horoscop-%{texlive_version}.%{texlive_noarch}.0.0.92svn30530-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:281} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:282} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hpsdiss-%{texlive_version}.%{texlive_noarch}.1.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:283} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:284} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-hrefhide-%{texlive_version}.%{texlive_noarch}.1.0fsvn22255-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:285} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:286} -C %{buildroot}%{_datadir}/texlive/texmf-dist
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
