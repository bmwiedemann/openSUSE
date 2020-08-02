#
# spec file for package texlive-specs-g
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

Name:           texlive-specs-g
Version:        2020
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for g
License:        Artistic-1.0 and GFDL-1.2 and GPL-2.0+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-g-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-datetime2-basque
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn47064
Release:        0
Summary:        Basque language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-basque-doc >= %{texlive_version}
Provides:       tex(datetime2-basque.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source1:        datetime2-basque.tar.xz
Source2:        datetime2-basque.doc.tar.xz

%description -n texlive-datetime2-basque
This module provides the "basque" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-basque-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn47064
Release:        0
Summary:        Documentation for texlive-datetime2-basque
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-basque-doc
This package includes the documentation for texlive-datetime2-basque

%post -n texlive-datetime2-basque
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-basque 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-basque
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-basque-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-basque/CHANGES
%{_texmfdistdir}/doc/latex/datetime2-basque/Makefile
%{_texmfdistdir}/doc/latex/datetime2-basque/README.txt
%{_texmfdistdir}/doc/latex/datetime2-basque/datetime2-basque-small-test.tex
%{_texmfdistdir}/doc/latex/datetime2-basque/datetime2-basque-test.tex

%files -n texlive-datetime2-basque
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-basque/datetime2-basque.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-basque-%{texlive_version}.%{texlive_noarch}.1.2asvn47064-%{release}-zypper
%endif

%package -n texlive-datetime2-breton
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn52647
Release:        0
Summary:        Breton language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-breton-doc >= %{texlive_version}
Provides:       tex(datetime2-breton-ascii.ldf)
Provides:       tex(datetime2-breton-utf8.ldf)
Provides:       tex(datetime2-breton.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source3:        datetime2-breton.tar.xz
Source4:        datetime2-breton.doc.tar.xz

%description -n texlive-datetime2-breton
This module provides the "breton" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-breton-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn52647
Release:        0
Summary:        Documentation for texlive-datetime2-breton
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-breton-doc
This package includes the documentation for texlive-datetime2-breton

%post -n texlive-datetime2-breton
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-breton 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-breton
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-breton-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-breton/README
%{_texmfdistdir}/doc/latex/datetime2-breton/datetime2-breton.pdf

%files -n texlive-datetime2-breton
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-breton/datetime2-breton-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-breton/datetime2-breton-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-breton/datetime2-breton.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-breton-%{texlive_version}.%{texlive_noarch}.1.2svn52647-%{release}-zypper
%endif

%package -n texlive-datetime2-bulgarian
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47031
Release:        0
Summary:        Bulgarian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-bulgarian-doc >= %{texlive_version}
Provides:       tex(datetime2-bulgarian-ascii.ldf)
Provides:       tex(datetime2-bulgarian-utf8.ldf)
Provides:       tex(datetime2-bulgarian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source5:        datetime2-bulgarian.tar.xz
Source6:        datetime2-bulgarian.doc.tar.xz

%description -n texlive-datetime2-bulgarian
This module provides the "bulgarian" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-bulgarian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47031
Release:        0
Summary:        Documentation for texlive-datetime2-bulgarian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-bulgarian-doc
This package includes the documentation for texlive-datetime2-bulgarian

%post -n texlive-datetime2-bulgarian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-bulgarian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-bulgarian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-bulgarian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-bulgarian/README
%{_texmfdistdir}/doc/latex/datetime2-bulgarian/datetime2-bulgarian.pdf

%files -n texlive-datetime2-bulgarian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-bulgarian/datetime2-bulgarian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-bulgarian/datetime2-bulgarian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-bulgarian/datetime2-bulgarian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-bulgarian-%{texlive_version}.%{texlive_noarch}.1.1svn47031-%{release}-zypper
%endif

%package -n texlive-datetime2-catalan
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47032
Release:        0
Summary:        Catalan language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-catalan-doc >= %{texlive_version}
Provides:       tex(datetime2-catalan-ascii.ldf)
Provides:       tex(datetime2-catalan-utf8.ldf)
Provides:       tex(datetime2-catalan.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source7:        datetime2-catalan.tar.xz
Source8:        datetime2-catalan.doc.tar.xz

%description -n texlive-datetime2-catalan
This module provides the "catalan" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-catalan-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47032
Release:        0
Summary:        Documentation for texlive-datetime2-catalan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-catalan-doc
This package includes the documentation for texlive-datetime2-catalan

%post -n texlive-datetime2-catalan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-catalan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-catalan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-catalan-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-catalan/README
%{_texmfdistdir}/doc/latex/datetime2-catalan/datetime2-catalan.pdf

%files -n texlive-datetime2-catalan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-catalan/datetime2-catalan-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-catalan/datetime2-catalan-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-catalan/datetime2-catalan.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-catalan-%{texlive_version}.%{texlive_noarch}.1.1svn47032-%{release}-zypper
%endif

%package -n texlive-datetime2-croatian
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36682
Release:        0
Summary:        Croatian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-croatian-doc >= %{texlive_version}
Provides:       tex(datetime2-croatian-ascii.ldf)
Provides:       tex(datetime2-croatian-utf8.ldf)
Provides:       tex(datetime2-croatian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source9:        datetime2-croatian.tar.xz
Source10:       datetime2-croatian.doc.tar.xz

%description -n texlive-datetime2-croatian
This module provides the "croatian" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-croatian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36682
Release:        0
Summary:        Documentation for texlive-datetime2-croatian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-croatian-doc
This package includes the documentation for texlive-datetime2-croatian

%post -n texlive-datetime2-croatian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-croatian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-croatian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-croatian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-croatian/README
%{_texmfdistdir}/doc/latex/datetime2-croatian/datetime2-croatian.pdf

%files -n texlive-datetime2-croatian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-croatian/datetime2-croatian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-croatian/datetime2-croatian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-croatian/datetime2-croatian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-croatian-%{texlive_version}.%{texlive_noarch}.1.0svn36682-%{release}-zypper
%endif

%package -n texlive-datetime2-czech
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47033
Release:        0
Summary:        Czech language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-czech-doc >= %{texlive_version}
Provides:       tex(datetime2-czech-ascii.ldf)
Provides:       tex(datetime2-czech-utf8.ldf)
Provides:       tex(datetime2-czech.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source11:       datetime2-czech.tar.xz
Source12:       datetime2-czech.doc.tar.xz

%description -n texlive-datetime2-czech
This module provides the "czech" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-czech-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47033
Release:        0
Summary:        Documentation for texlive-datetime2-czech
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-czech-doc
This package includes the documentation for texlive-datetime2-czech

%post -n texlive-datetime2-czech
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-czech 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-czech
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-czech-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-czech/README
%{_texmfdistdir}/doc/latex/datetime2-czech/datetime2-czech.pdf

%files -n texlive-datetime2-czech
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-czech/datetime2-czech-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-czech/datetime2-czech-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-czech/datetime2-czech.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-czech-%{texlive_version}.%{texlive_noarch}.1.1svn47033-%{release}-zypper
%endif

%package -n texlive-datetime2-danish
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47034
Release:        0
Summary:        Danish language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-danish-doc >= %{texlive_version}
Provides:       tex(datetime2-danish-ascii.ldf)
Provides:       tex(datetime2-danish-utf8.ldf)
Provides:       tex(datetime2-danish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source13:       datetime2-danish.tar.xz
Source14:       datetime2-danish.doc.tar.xz

%description -n texlive-datetime2-danish
This module provides the "danish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-danish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47034
Release:        0
Summary:        Documentation for texlive-datetime2-danish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-danish-doc
This package includes the documentation for texlive-datetime2-danish

%post -n texlive-datetime2-danish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-danish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-danish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-danish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-danish/README
%{_texmfdistdir}/doc/latex/datetime2-danish/datetime2-danish.pdf

%files -n texlive-datetime2-danish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-danish/datetime2-danish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-danish/datetime2-danish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-danish/datetime2-danish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-danish-%{texlive_version}.%{texlive_noarch}.1.1svn47034-%{release}-zypper
%endif

%package -n texlive-datetime2-dutch
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47355
Release:        0
Summary:        Dutch language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-dutch-doc >= %{texlive_version}
Provides:       tex(datetime2-dutch.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source15:       datetime2-dutch.tar.xz
Source16:       datetime2-dutch.doc.tar.xz

%description -n texlive-datetime2-dutch
This module provides the "dutch" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-dutch-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47355
Release:        0
Summary:        Documentation for texlive-datetime2-dutch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-dutch-doc
This package includes the documentation for texlive-datetime2-dutch

%post -n texlive-datetime2-dutch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-dutch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-dutch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-dutch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-dutch/README
%{_texmfdistdir}/doc/latex/datetime2-dutch/datetime2-dutch.pdf

%files -n texlive-datetime2-dutch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-dutch/datetime2-dutch.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-dutch-%{texlive_version}.%{texlive_noarch}.1.1svn47355-%{release}-zypper
%endif

%package -n texlive-datetime2-en-fulltext
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36705
Release:        0
Summary:        English Full Text styles for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-en-fulltext-doc >= %{texlive_version}
Provides:       tex(datetime2-en-fulltext.sty)
Requires:       tex(datetime2.sty)
Requires:       tex(fmtcount.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source17:       datetime2-en-fulltext.tar.xz
Source18:       datetime2-en-fulltext.doc.tar.xz

%description -n texlive-datetime2-en-fulltext
English date and time styles that use words for the numbers and
ordinals. This package provides the following date and time
styles: "en-fulltext", "en-FullText", "en-FULLTEXT", and the
additional time style "en-Fulltext". (The date equivalent can
be obtained through commands like \Today.) Unlike the base
styles provided by datetime2.sty, these styles aren't
expandable styles. This means that you can't use the date or
time in PDF bookmarks or in the argument of certain commands,
such as \MakeUppercase, while these styles are in use.

%package -n texlive-datetime2-en-fulltext-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36705
Release:        0
Summary:        Documentation for texlive-datetime2-en-fulltext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-en-fulltext-doc
This package includes the documentation for texlive-datetime2-en-fulltext

%post -n texlive-datetime2-en-fulltext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-en-fulltext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-en-fulltext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-en-fulltext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-en-fulltext/README
%{_texmfdistdir}/doc/latex/datetime2-en-fulltext/datetime2-en-fulltext.pdf
%{_texmfdistdir}/doc/latex/datetime2-en-fulltext/sample-en-fulltext.pdf
%{_texmfdistdir}/doc/latex/datetime2-en-fulltext/sample-en-fulltext.tex

%files -n texlive-datetime2-en-fulltext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-en-fulltext/datetime2-en-fulltext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-en-fulltext-%{texlive_version}.%{texlive_noarch}.1.0svn36705-%{release}-zypper
%endif

%package -n texlive-datetime2-english
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn52479
Release:        0
Summary:        English language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-english-doc >= %{texlive_version}
Provides:       tex(datetime2-en-AU.ldf)
Provides:       tex(datetime2-en-CA.ldf)
Provides:       tex(datetime2-en-GB.ldf)
Provides:       tex(datetime2-en-GG.ldf)
Provides:       tex(datetime2-en-IE.ldf)
Provides:       tex(datetime2-en-IM.ldf)
Provides:       tex(datetime2-en-JE.ldf)
Provides:       tex(datetime2-en-MT.ldf)
Provides:       tex(datetime2-en-NZ.ldf)
Provides:       tex(datetime2-en-US.ldf)
Provides:       tex(datetime2-english-base.ldf)
Provides:       tex(datetime2-english.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source19:       datetime2-english.tar.xz
Source20:       datetime2-english.doc.tar.xz

%description -n texlive-datetime2-english
This module provides the following styles that can be set using
\DTMsetstyle provided by datetime2.sty. The region not only
determines the date/time format but also the time zone
abbreviations if the zone mapping setting is on. english
(English - no region) en-GB (English - United Kingdom of Great
Britain and Northern Ireland) en-US (English - United States of
America) en-CA (English - Canada) en-AU (English - Commonwealth
of Australia) en-NZ (English - New Zealand) en-GG (English -
Bailiwick of Guernsey) en-JE (English - Bailiwick of Jersey)
en-IM (English - Isle of Man) en-MT (English - Republic of
Malta) en-IE (English - Republic of Ireland)

%package -n texlive-datetime2-english-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn52479
Release:        0
Summary:        Documentation for texlive-datetime2-english
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-english-doc
This package includes the documentation for texlive-datetime2-english

%post -n texlive-datetime2-english
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-english 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-english
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-english-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-english/CHANGES
%{_texmfdistdir}/doc/latex/datetime2-english/README
%{_texmfdistdir}/doc/latex/datetime2-english/datetime2-english-sample.pdf
%{_texmfdistdir}/doc/latex/datetime2-english/datetime2-english-sample.tex
%{_texmfdistdir}/doc/latex/datetime2-english/datetime2-english.pdf

%files -n texlive-datetime2-english
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-AU.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-CA.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-GB.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-GG.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-IE.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-IM.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-JE.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-MT.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-NZ.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-en-US.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-english-base.ldf
%{_texmfdistdir}/tex/latex/datetime2-english/datetime2-english.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-english-%{texlive_version}.%{texlive_noarch}.1.05svn52479-%{release}-zypper
%endif

%package -n texlive-datetime2-esperanto
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47356
Release:        0
Summary:        Esperanto language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-esperanto-doc >= %{texlive_version}
Provides:       tex(datetime2-esperanto-ascii.ldf)
Provides:       tex(datetime2-esperanto-utf8.ldf)
Provides:       tex(datetime2-esperanto.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source21:       datetime2-esperanto.tar.xz
Source22:       datetime2-esperanto.doc.tar.xz

%description -n texlive-datetime2-esperanto
This module provides the "esperanto" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-esperanto-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47356
Release:        0
Summary:        Documentation for texlive-datetime2-esperanto
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-esperanto-doc
This package includes the documentation for texlive-datetime2-esperanto

%post -n texlive-datetime2-esperanto
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-esperanto 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-esperanto
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-esperanto-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-esperanto/README
%{_texmfdistdir}/doc/latex/datetime2-esperanto/datetime2-esperanto.pdf

%files -n texlive-datetime2-esperanto
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-esperanto/datetime2-esperanto-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-esperanto/datetime2-esperanto-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-esperanto/datetime2-esperanto.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-esperanto-%{texlive_version}.%{texlive_noarch}.1.1svn47356-%{release}-zypper
%endif

%package -n texlive-datetime2-estonian
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47565
Release:        0
Summary:        Estonian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-estonian-doc >= %{texlive_version}
Provides:       tex(datetime2-estonian-ascii.ldf)
Provides:       tex(datetime2-estonian-utf8.ldf)
Provides:       tex(datetime2-estonian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source23:       datetime2-estonian.tar.xz
Source24:       datetime2-estonian.doc.tar.xz

%description -n texlive-datetime2-estonian
This module provides the "estonian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-estonian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47565
Release:        0
Summary:        Documentation for texlive-datetime2-estonian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-estonian-doc
This package includes the documentation for texlive-datetime2-estonian

%post -n texlive-datetime2-estonian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-estonian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-estonian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-estonian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-estonian/README
%{_texmfdistdir}/doc/latex/datetime2-estonian/datetime2-estonian.pdf

%files -n texlive-datetime2-estonian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-estonian/datetime2-estonian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-estonian/datetime2-estonian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-estonian/datetime2-estonian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-estonian-%{texlive_version}.%{texlive_noarch}.1.1svn47565-%{release}-zypper
%endif

%package -n texlive-datetime2-finnish
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn47047
Release:        0
Summary:        Finnish language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-finnish-doc >= %{texlive_version}
Provides:       tex(datetime2-finnish-ascii.ldf)
Provides:       tex(datetime2-finnish-utf8.ldf)
Provides:       tex(datetime2-finnish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source25:       datetime2-finnish.tar.xz
Source26:       datetime2-finnish.doc.tar.xz

%description -n texlive-datetime2-finnish
This module provides the "finnish" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-finnish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn47047
Release:        0
Summary:        Documentation for texlive-datetime2-finnish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-finnish-doc
This package includes the documentation for texlive-datetime2-finnish

%post -n texlive-datetime2-finnish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-finnish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-finnish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-finnish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-finnish/CHANGES
%{_texmfdistdir}/doc/latex/datetime2-finnish/README
%{_texmfdistdir}/doc/latex/datetime2-finnish/datetime2-finnish.pdf

%files -n texlive-datetime2-finnish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-finnish/datetime2-finnish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-finnish/datetime2-finnish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-finnish/datetime2-finnish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-finnish-%{texlive_version}.%{texlive_noarch}.1.2svn47047-%{release}-zypper
%endif

%package -n texlive-datetime2-french
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn43742
Release:        0
Summary:        French language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-french-doc >= %{texlive_version}
Provides:       tex(datetime2-french-ascii.ldf)
Provides:       tex(datetime2-french-utf8.ldf)
Provides:       tex(datetime2-french.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source27:       datetime2-french.tar.xz
Source28:       datetime2-french.doc.tar.xz

%description -n texlive-datetime2-french
This module provides the "french" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-french-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn43742
Release:        0
Summary:        Documentation for texlive-datetime2-french
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-french-doc
This package includes the documentation for texlive-datetime2-french

%post -n texlive-datetime2-french
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-french 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-french
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-french-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-french/README
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french-test-luatex.pdf
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french-test-luatex.tex
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french-test-pdftex.pdf
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french-test-pdftex.tex
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french-test-xetex.pdf
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french-test-xetex.tex
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french-test.tex
%{_texmfdistdir}/doc/latex/datetime2-french/datetime2-french.pdf

%files -n texlive-datetime2-french
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-french/datetime2-french-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-french/datetime2-french-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-french/datetime2-french.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-french-%{texlive_version}.%{texlive_noarch}.1.02svn43742-%{release}-zypper
%endif

%package -n texlive-datetime2-galician
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn47631
Release:        0
Summary:        Galician language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-galician-doc >= %{texlive_version}
Provides:       tex(datetime2-galician-ascii.ldf)
Provides:       tex(datetime2-galician-utf8.ldf)
Provides:       tex(datetime2-galician.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source29:       datetime2-galician.tar.xz
Source30:       datetime2-galician.doc.tar.xz

%description -n texlive-datetime2-galician
This module provides the "galician" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-galician-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn47631
Release:        0
Summary:        Documentation for texlive-datetime2-galician
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-galician-doc
This package includes the documentation for texlive-datetime2-galician

%post -n texlive-datetime2-galician
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-galician 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-galician
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-galician-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-galician/README
%{_texmfdistdir}/doc/latex/datetime2-galician/datetime2-galician.pdf

%files -n texlive-datetime2-galician
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-galician/datetime2-galician-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-galician/datetime2-galician-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-galician/datetime2-galician.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-galician-%{texlive_version}.%{texlive_noarch}.1.0svn47631-%{release}-zypper
%endif

%package -n texlive-datetime2-german
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn53125
Release:        0
Summary:        German language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-german-doc >= %{texlive_version}
Provides:       tex(datetime2-de-AT.ldf)
Provides:       tex(datetime2-de-CH.ldf)
Provides:       tex(datetime2-de-DE.ldf)
Provides:       tex(datetime2-german-base-ascii.ldf)
Provides:       tex(datetime2-german-base-utf8.ldf)
Provides:       tex(datetime2-german-base.ldf)
Provides:       tex(datetime2-german.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source31:       datetime2-german.tar.xz
Source32:       datetime2-german.doc.tar.xz

%description -n texlive-datetime2-german
This module provides the "german" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-german-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn53125
Release:        0
Summary:        Documentation for texlive-datetime2-german
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-german-doc
This package includes the documentation for texlive-datetime2-german

%post -n texlive-datetime2-german
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-german 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-german
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-german-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-german/README.md
%{_texmfdistdir}/doc/latex/datetime2-german/datetime2-german-doc.pdf

%files -n texlive-datetime2-german
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-german/datetime2-de-AT.ldf
%{_texmfdistdir}/tex/latex/datetime2-german/datetime2-de-CH.ldf
%{_texmfdistdir}/tex/latex/datetime2-german/datetime2-de-DE.ldf
%{_texmfdistdir}/tex/latex/datetime2-german/datetime2-german-base-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-german/datetime2-german-base-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-german/datetime2-german-base.ldf
%{_texmfdistdir}/tex/latex/datetime2-german/datetime2-german.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-german-%{texlive_version}.%{texlive_noarch}.3.0svn53125-%{release}-zypper
%endif

%package -n texlive-datetime2-greek
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47533
Release:        0
Summary:        Greek language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-greek-doc >= %{texlive_version}
Provides:       tex(datetime2-greek-ascii.ldf)
Provides:       tex(datetime2-greek-utf8.ldf)
Provides:       tex(datetime2-greek.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source33:       datetime2-greek.tar.xz
Source34:       datetime2-greek.doc.tar.xz

%description -n texlive-datetime2-greek
This module provides the "greek" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-greek-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47533
Release:        0
Summary:        Documentation for texlive-datetime2-greek
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-greek-doc
This package includes the documentation for texlive-datetime2-greek

%post -n texlive-datetime2-greek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-greek 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-greek
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-greek-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-greek/README
%{_texmfdistdir}/doc/latex/datetime2-greek/datetime2-greek.pdf

%files -n texlive-datetime2-greek
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-greek/datetime2-greek-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-greek/datetime2-greek-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-greek/datetime2-greek.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-greek-%{texlive_version}.%{texlive_noarch}.1.1svn47533-%{release}-zypper
%endif

%package -n texlive-datetime2-hebrew
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47534
Release:        0
Summary:        Hebrew language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-hebrew-doc >= %{texlive_version}
Provides:       tex(datetime2-hebrew.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source35:       datetime2-hebrew.tar.xz
Source36:       datetime2-hebrew.doc.tar.xz

%description -n texlive-datetime2-hebrew
This module provides the "hebrew" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-hebrew-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47534
Release:        0
Summary:        Documentation for texlive-datetime2-hebrew
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-hebrew-doc
This package includes the documentation for texlive-datetime2-hebrew

%post -n texlive-datetime2-hebrew
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-hebrew 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-hebrew
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-hebrew-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-hebrew/README
%{_texmfdistdir}/doc/latex/datetime2-hebrew/datetime2-hebrew.pdf

%files -n texlive-datetime2-hebrew
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-hebrew/datetime2-hebrew.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-hebrew-%{texlive_version}.%{texlive_noarch}.1.1svn47534-%{release}-zypper
%endif

%package -n texlive-datetime2-icelandic
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47501
Release:        0
Summary:        Icelandic language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-icelandic-doc >= %{texlive_version}
Provides:       tex(datetime2-icelandic-ascii.ldf)
Provides:       tex(datetime2-icelandic-utf8.ldf)
Provides:       tex(datetime2-icelandic.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source37:       datetime2-icelandic.tar.xz
Source38:       datetime2-icelandic.doc.tar.xz

%description -n texlive-datetime2-icelandic
This module provides the "icelandic" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-icelandic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47501
Release:        0
Summary:        Documentation for texlive-datetime2-icelandic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-icelandic-doc
This package includes the documentation for texlive-datetime2-icelandic

%post -n texlive-datetime2-icelandic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-icelandic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-icelandic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-icelandic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-icelandic/README
%{_texmfdistdir}/doc/latex/datetime2-icelandic/datetime2-icelandic.pdf

%files -n texlive-datetime2-icelandic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-icelandic/datetime2-icelandic-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-icelandic/datetime2-icelandic-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-icelandic/datetime2-icelandic.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-icelandic-%{texlive_version}.%{texlive_noarch}.1.1svn47501-%{release}-zypper
%endif

%package -n texlive-datetime2-irish
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47632
Release:        0
Summary:        Irish Gaelic Language Module for the datetime2 Package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-irish-doc >= %{texlive_version}
Provides:       tex(datetime2-ga-GB.ldf)
Provides:       tex(datetime2-ga-IE.ldf)
Provides:       tex(datetime2-irish-ascii.ldf)
Provides:       tex(datetime2-irish-utf8.ldf)
Provides:       tex(datetime2-irish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source39:       datetime2-irish.tar.xz
Source40:       datetime2-irish.doc.tar.xz

%description -n texlive-datetime2-irish
This module provides the "irish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-irish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47632
Release:        0
Summary:        Documentation for texlive-datetime2-irish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-irish-doc
This package includes the documentation for texlive-datetime2-irish

%post -n texlive-datetime2-irish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-irish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-irish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-irish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-irish/README
%{_texmfdistdir}/doc/latex/datetime2-irish/datetime2-irish.pdf

%files -n texlive-datetime2-irish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-irish/datetime2-ga-GB.ldf
%{_texmfdistdir}/tex/latex/datetime2-irish/datetime2-ga-IE.ldf
%{_texmfdistdir}/tex/latex/datetime2-irish/datetime2-irish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-irish/datetime2-irish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-irish/datetime2-irish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-irish-%{texlive_version}.%{texlive_noarch}.1.1svn47632-%{release}-zypper
%endif

%package -n texlive-datetime2-it-fulltext
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn54779
Release:        0
Summary:        Italian full text styles for the datetime2 package
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
Recommends:     texlive-datetime2-it-fulltext-doc >= %{texlive_version}
Provides:       tex(datetime2-it-fulltext-ascii.ldf)
Provides:       tex(datetime2-it-fulltext-utf8.ldf)
Provides:       tex(datetime2-it-fulltext.sty)
Requires:       tex(datetime2.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(itnumpar.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source41:       datetime2-it-fulltext.tar.xz
Source42:       datetime2-it-fulltext.doc.tar.xz

%description -n texlive-datetime2-it-fulltext
Italian date and time styles that use words for the numbers and
ordinals. This package provides the following date and time
styles: "it-fulltext" and "it-fulltext-twenty-four". The first
style uses a format "am pm", the second a format "24 hours".
The necessary packages are datetime2, itnumpar, ifxetex, and
ifluatex. This package is the translation and adaptation of
datetime2-en-fulltext.

%package -n texlive-datetime2-it-fulltext-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn54779
Release:        0
Summary:        Documentation for texlive-datetime2-it-fulltext
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-it-fulltext-doc
This package includes the documentation for texlive-datetime2-it-fulltext

%post -n texlive-datetime2-it-fulltext
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-it-fulltext 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-it-fulltext
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-it-fulltext-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/README
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/datetime2-it-fulltext.pdf
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/BatTest.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/BatTestDate.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/it-fulltext-en-fulltext.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/sample-it-fulltext-second.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/sample-it-fulltext-semplice.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/sample-it-fulltext-twenty-four-second.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/sample-it-fulltext-twenty-four.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/sample-it-fulltext.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/sample-it-timedatestyle1.tex
%{_texmfdistdir}/doc/latex/datetime2-it-fulltext/samples/sample-it-timedatestyle2.tex

%files -n texlive-datetime2-it-fulltext
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-it-fulltext/datetime2-it-fulltext-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-it-fulltext/datetime2-it-fulltext-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-it-fulltext/datetime2-it-fulltext.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-it-fulltext-%{texlive_version}.%{texlive_noarch}.1.6svn54779-%{release}-zypper
%endif

%package -n texlive-datetime2-italian
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn37146
Release:        0
Summary:        Italian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-italian-doc >= %{texlive_version}
Provides:       tex(datetime2-italian-ascii.ldf)
Provides:       tex(datetime2-italian-utf8.ldf)
Provides:       tex(datetime2-italian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source43:       datetime2-italian.tar.xz
Source44:       datetime2-italian.doc.tar.xz

%description -n texlive-datetime2-italian
This module provides the "italian" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-italian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn37146
Release:        0
Summary:        Documentation for texlive-datetime2-italian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-italian-doc
This package includes the documentation for texlive-datetime2-italian

%post -n texlive-datetime2-italian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-italian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-italian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-italian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-italian/README
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/datetime1.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/datetime2-sample-babel.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/datetime2-sample-calc.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/datetime2-sample-hyperref.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/datetime2-sample-styles.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio1.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio10.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio11.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio12.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio13.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio2.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio3.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio4.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio5.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio6.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio6a.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio7.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio8.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/esempio9.tex
%{_texmfdistdir}/doc/latex/datetime2-italian/sample/tomorrow.tex

%files -n texlive-datetime2-italian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-italian/datetime2-italian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-italian/datetime2-italian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-italian/datetime2-italian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-italian-%{texlive_version}.%{texlive_noarch}.1.3svn37146-%{release}-zypper
%endif

%package -n texlive-datetime2-latin
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn47748
Release:        0
Summary:        Latin language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-latin-doc >= %{texlive_version}
Provides:       tex(datetime2-latin.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source45:       datetime2-latin.tar.xz
Source46:       datetime2-latin.doc.tar.xz

%description -n texlive-datetime2-latin
This module provides the "latin" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-latin-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn47748
Release:        0
Summary:        Documentation for texlive-datetime2-latin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-latin-doc
This package includes the documentation for texlive-datetime2-latin

%post -n texlive-datetime2-latin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-latin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-latin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-latin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-latin/README
%{_texmfdistdir}/doc/latex/datetime2-latin/datetime2-latin.pdf

%files -n texlive-datetime2-latin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-latin/datetime2-latin.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-latin-%{texlive_version}.%{texlive_noarch}.1.0svn47748-%{release}-zypper
%endif

%package -n texlive-datetime2-lsorbian
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47749
Release:        0
Summary:        Lower Sorbian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-lsorbian-doc >= %{texlive_version}
Provides:       tex(datetime2-lsorbian-ascii.ldf)
Provides:       tex(datetime2-lsorbian-utf8.ldf)
Provides:       tex(datetime2-lsorbian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source47:       datetime2-lsorbian.tar.xz
Source48:       datetime2-lsorbian.doc.tar.xz

%description -n texlive-datetime2-lsorbian
This module provides the "lsorbian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-lsorbian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn47749
Release:        0
Summary:        Documentation for texlive-datetime2-lsorbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-lsorbian-doc
This package includes the documentation for texlive-datetime2-lsorbian

%post -n texlive-datetime2-lsorbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-lsorbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-lsorbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-lsorbian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-lsorbian/README
%{_texmfdistdir}/doc/latex/datetime2-lsorbian/datetime2-lsorbian.pdf

%files -n texlive-datetime2-lsorbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-lsorbian/datetime2-lsorbian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-lsorbian/datetime2-lsorbian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-lsorbian/datetime2-lsorbian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-lsorbian-%{texlive_version}.%{texlive_noarch}.1.1svn47749-%{release}-zypper
%endif

%package -n texlive-datetime2-magyar
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48266
Release:        0
Summary:        Magyar language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-magyar-doc >= %{texlive_version}
Provides:       tex(datetime2-magyar-ascii.ldf)
Provides:       tex(datetime2-magyar-utf8.ldf)
Provides:       tex(datetime2-magyar.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source49:       datetime2-magyar.tar.xz
Source50:       datetime2-magyar.doc.tar.xz

%description -n texlive-datetime2-magyar
This module provides the "magyar" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-magyar-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48266
Release:        0
Summary:        Documentation for texlive-datetime2-magyar
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-magyar-doc
This package includes the documentation for texlive-datetime2-magyar

%post -n texlive-datetime2-magyar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-magyar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-magyar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-magyar-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-magyar/README
%{_texmfdistdir}/doc/latex/datetime2-magyar/datetime2-magyar.pdf

%files -n texlive-datetime2-magyar
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-magyar/datetime2-magyar-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-magyar/datetime2-magyar-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-magyar/datetime2-magyar.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-magyar-%{texlive_version}.%{texlive_noarch}.1.1svn48266-%{release}-zypper
%endif

%package -n texlive-datetime2-norsk
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48267
Release:        0
Summary:        Norsk language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-norsk-doc >= %{texlive_version}
Provides:       tex(datetime2-norsk-ascii.ldf)
Provides:       tex(datetime2-norsk-utf8.ldf)
Provides:       tex(datetime2-norsk.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source51:       datetime2-norsk.tar.xz
Source52:       datetime2-norsk.doc.tar.xz

%description -n texlive-datetime2-norsk
This module provides the "norsk" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-norsk-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48267
Release:        0
Summary:        Documentation for texlive-datetime2-norsk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-norsk-doc
This package includes the documentation for texlive-datetime2-norsk

%post -n texlive-datetime2-norsk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-norsk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-norsk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-norsk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-norsk/README
%{_texmfdistdir}/doc/latex/datetime2-norsk/datetime2-norsk.pdf

%files -n texlive-datetime2-norsk
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-norsk/datetime2-norsk-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-norsk/datetime2-norsk-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-norsk/datetime2-norsk.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-norsk-%{texlive_version}.%{texlive_noarch}.1.1svn48267-%{release}-zypper
%endif

%package -n texlive-datetime2-polish
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48456
Release:        0
Summary:        Polish language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-polish-doc >= %{texlive_version}
Provides:       tex(datetime2-polish-ascii.ldf)
Provides:       tex(datetime2-polish-utf8.ldf)
Provides:       tex(datetime2-polish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source53:       datetime2-polish.tar.xz
Source54:       datetime2-polish.doc.tar.xz

%description -n texlive-datetime2-polish
This module provides the "polish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-polish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48456
Release:        0
Summary:        Documentation for texlive-datetime2-polish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-polish-doc
This package includes the documentation for texlive-datetime2-polish

%post -n texlive-datetime2-polish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-polish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-polish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-polish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-polish/README
%{_texmfdistdir}/doc/latex/datetime2-polish/datetime2-polish.pdf

%files -n texlive-datetime2-polish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-polish/datetime2-polish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-polish/datetime2-polish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-polish/datetime2-polish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-polish-%{texlive_version}.%{texlive_noarch}.1.1svn48456-%{release}-zypper
%endif

%package -n texlive-datetime2-portuges
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48457
Release:        0
Summary:        Portuguese language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-portuges-doc >= %{texlive_version}
Provides:       tex(datetime2-portuges-ascii.ldf)
Provides:       tex(datetime2-portuges-utf8.ldf)
Provides:       tex(datetime2-portuges.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source55:       datetime2-portuges.tar.xz
Source56:       datetime2-portuges.doc.tar.xz

%description -n texlive-datetime2-portuges
This module provides the "portuges" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-portuges-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn48457
Release:        0
Summary:        Documentation for texlive-datetime2-portuges
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-portuges-doc
This package includes the documentation for texlive-datetime2-portuges

%post -n texlive-datetime2-portuges
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-portuges 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-portuges
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-portuges-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-portuges/README
%{_texmfdistdir}/doc/latex/datetime2-portuges/datetime2-portuges.pdf

%files -n texlive-datetime2-portuges
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-portuges/datetime2-portuges-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-portuges/datetime2-portuges-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-portuges/datetime2-portuges.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-portuges-%{texlive_version}.%{texlive_noarch}.1.1svn48457-%{release}-zypper
%endif

%package -n texlive-datetime2-romanian
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn43743
Release:        0
Summary:        Romanian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-romanian-doc >= %{texlive_version}
Provides:       tex(datetime2-romanian-ascii.ldf)
Provides:       tex(datetime2-romanian-utf8.ldf)
Provides:       tex(datetime2-romanian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source57:       datetime2-romanian.tar.xz
Source58:       datetime2-romanian.doc.tar.xz

%description -n texlive-datetime2-romanian
This module provides the "romanian" style that can be set using
\DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-romanian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn43743
Release:        0
Summary:        Documentation for texlive-datetime2-romanian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-romanian-doc
This package includes the documentation for texlive-datetime2-romanian

%post -n texlive-datetime2-romanian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-romanian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-romanian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-romanian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-romanian/README
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian-test-luatex.pdf
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian-test-luatex.tex
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian-test-pdftex.pdf
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian-test-pdftex.tex
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian-test-xetex.pdf
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian-test-xetex.tex
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian-test.tex
%{_texmfdistdir}/doc/latex/datetime2-romanian/datetime2-romanian.pdf

%files -n texlive-datetime2-romanian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-romanian/datetime2-romanian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-romanian/datetime2-romanian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-romanian/datetime2-romanian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-romanian-%{texlive_version}.%{texlive_noarch}.1.01svn43743-%{release}-zypper
%endif

%package -n texlive-datetime2-russian
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49345
Release:        0
Summary:        Russian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-russian-doc >= %{texlive_version}
Provides:       tex(datetime2-russian-ascii.ldf)
Provides:       tex(datetime2-russian-utf8.ldf)
Provides:       tex(datetime2-russian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source59:       datetime2-russian.tar.xz
Source60:       datetime2-russian.doc.tar.xz

%description -n texlive-datetime2-russian
This module provides the "russian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-russian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49345
Release:        0
Summary:        Documentation for texlive-datetime2-russian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-russian-doc
This package includes the documentation for texlive-datetime2-russian

%post -n texlive-datetime2-russian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-russian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-russian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-russian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-russian/README
%{_texmfdistdir}/doc/latex/datetime2-russian/datetime2-russian.pdf

%files -n texlive-datetime2-russian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-russian/datetime2-russian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-russian/datetime2-russian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-russian/datetime2-russian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-russian-%{texlive_version}.%{texlive_noarch}.1.1svn49345-%{release}-zypper
%endif

%package -n texlive-datetime2-samin
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49346
Release:        0
Summary:        Northern Sami language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-samin-doc >= %{texlive_version}
Provides:       tex(datetime2-samin-ascii.ldf)
Provides:       tex(datetime2-samin-utf8.ldf)
Provides:       tex(datetime2-samin.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source61:       datetime2-samin.tar.xz
Source62:       datetime2-samin.doc.tar.xz

%description -n texlive-datetime2-samin
This module provides the "samin" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-samin-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49346
Release:        0
Summary:        Documentation for texlive-datetime2-samin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-samin-doc
This package includes the documentation for texlive-datetime2-samin

%post -n texlive-datetime2-samin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-samin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-samin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-samin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-samin/README
%{_texmfdistdir}/doc/latex/datetime2-samin/datetime2-samin.pdf

%files -n texlive-datetime2-samin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-samin/datetime2-samin-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-samin/datetime2-samin-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-samin/datetime2-samin.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-samin-%{texlive_version}.%{texlive_noarch}.1.1svn49346-%{release}-zypper
%endif

%package -n texlive-datetime2-scottish
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52101
Release:        0
Summary:        Scottish Gaelic Language Module for the datetime2 Package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-scottish-doc >= %{texlive_version}
Provides:       tex(datetime2-scottish-ascii.ldf)
Provides:       tex(datetime2-scottish-utf8.ldf)
Provides:       tex(datetime2-scottish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source63:       datetime2-scottish.tar.xz
Source64:       datetime2-scottish.doc.tar.xz

%description -n texlive-datetime2-scottish
This module provides the "scottish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-scottish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52101
Release:        0
Summary:        Documentation for texlive-datetime2-scottish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-scottish-doc
This package includes the documentation for texlive-datetime2-scottish

%post -n texlive-datetime2-scottish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-scottish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-scottish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-scottish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-scottish/README
%{_texmfdistdir}/doc/latex/datetime2-scottish/datetime2-scottish.pdf

%files -n texlive-datetime2-scottish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-scottish/datetime2-scottish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-scottish/datetime2-scottish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-scottish/datetime2-scottish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-scottish-%{texlive_version}.%{texlive_noarch}.1.1svn52101-%{release}-zypper
%endif

%package -n texlive-datetime2-serbian
Version:        %{texlive_version}.%{texlive_noarch}.2.1.0svn52893
Release:        0
Summary:        Serbian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-serbian-doc >= %{texlive_version}
Provides:       tex(datetime2-serbian-base-ascii.ldf)
Provides:       tex(datetime2-serbian-base-utf8.ldf)
Provides:       tex(datetime2-serbian-base.ldf)
Provides:       tex(datetime2-serbian.ldf)
Provides:       tex(datetime2-serbianc.ldf)
Provides:       tex(datetime2-sr-Cyrl-BA.ldf)
Provides:       tex(datetime2-sr-Cyrl-ME.ldf)
Provides:       tex(datetime2-sr-Cyrl-RS.ldf)
Provides:       tex(datetime2-sr-Cyrl.ldf)
Provides:       tex(datetime2-sr-Latn-BA.ldf)
Provides:       tex(datetime2-sr-Latn-ME.ldf)
Provides:       tex(datetime2-sr-Latn-RS.ldf)
Provides:       tex(datetime2-sr-Latn.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source65:       datetime2-serbian.tar.xz
Source66:       datetime2-serbian.doc.tar.xz

%description -n texlive-datetime2-serbian
This module provides the "serbian" style that can be set using
\DTMsetstyle provided by datetime2.sty. It provides both
Cyrillic and Latin, Ekavian and Ijekavian variants of Serbian
date formats, regionalized and non-regionalized.

%package -n texlive-datetime2-serbian-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1.0svn52893
Release:        0
Summary:        Documentation for texlive-datetime2-serbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-serbian-doc
This package includes the documentation for texlive-datetime2-serbian

%post -n texlive-datetime2-serbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-serbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-serbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-serbian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-serbian/README.md
%{_texmfdistdir}/doc/latex/datetime2-serbian/datetime2-serbian.pdf

%files -n texlive-datetime2-serbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-serbian-base-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-serbian-base-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-serbian-base.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-serbian.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-serbianc.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Cyrl-BA.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Cyrl-ME.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Cyrl-RS.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Cyrl.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Latn-BA.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Latn-ME.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Latn-RS.ldf
%{_texmfdistdir}/tex/latex/datetime2-serbian/datetime2-sr-Latn.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-serbian-%{texlive_version}.%{texlive_noarch}.2.1.0svn52893-%{release}-zypper
%endif

%package -n texlive-datetime2-slovak
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52281
Release:        0
Summary:        Slovak language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-slovak-doc >= %{texlive_version}
Provides:       tex(datetime2-slovak-ascii.ldf)
Provides:       tex(datetime2-slovak-utf8.ldf)
Provides:       tex(datetime2-slovak.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source67:       datetime2-slovak.tar.xz
Source68:       datetime2-slovak.doc.tar.xz

%description -n texlive-datetime2-slovak
This module provides the "slovak" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-slovak-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52281
Release:        0
Summary:        Documentation for texlive-datetime2-slovak
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-slovak-doc
This package includes the documentation for texlive-datetime2-slovak

%post -n texlive-datetime2-slovak
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-slovak 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-slovak
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-slovak-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-slovak/README
%{_texmfdistdir}/doc/latex/datetime2-slovak/datetime2-slovak.pdf

%files -n texlive-datetime2-slovak
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-slovak/datetime2-slovak-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-slovak/datetime2-slovak-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-slovak/datetime2-slovak.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-slovak-%{texlive_version}.%{texlive_noarch}.1.1svn52281-%{release}-zypper
%endif

%package -n texlive-datetime2-slovene
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52282
Release:        0
Summary:        Slovene language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-slovene-doc >= %{texlive_version}
Provides:       tex(datetime2-slovene-ascii.ldf)
Provides:       tex(datetime2-slovene-utf8.ldf)
Provides:       tex(datetime2-slovene.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source69:       datetime2-slovene.tar.xz
Source70:       datetime2-slovene.doc.tar.xz

%description -n texlive-datetime2-slovene
This module provides the "slovene" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-slovene-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52282
Release:        0
Summary:        Documentation for texlive-datetime2-slovene
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-slovene-doc
This package includes the documentation for texlive-datetime2-slovene

%post -n texlive-datetime2-slovene
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-slovene 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-slovene
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-slovene-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-slovene/README
%{_texmfdistdir}/doc/latex/datetime2-slovene/datetime2-slovene.pdf

%files -n texlive-datetime2-slovene
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-slovene/datetime2-slovene-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-slovene/datetime2-slovene-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-slovene/datetime2-slovene.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-slovene-%{texlive_version}.%{texlive_noarch}.1.1svn52282-%{release}-zypper
%endif

%package -n texlive-datetime2-spanish
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn45785
Release:        0
Summary:        Spanish language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-spanish-doc >= %{texlive_version}
Provides:       tex(datetime2-spanish-ascii.ldf)
Provides:       tex(datetime2-spanish-utf8.ldf)
Provides:       tex(datetime2-spanish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source71:       datetime2-spanish.tar.xz
Source72:       datetime2-spanish.doc.tar.xz

%description -n texlive-datetime2-spanish
This module provides the "spanish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-spanish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn45785
Release:        0
Summary:        Documentation for texlive-datetime2-spanish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-spanish-doc
This package includes the documentation for texlive-datetime2-spanish

%post -n texlive-datetime2-spanish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-spanish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-spanish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-spanish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-spanish/README
%{_texmfdistdir}/doc/latex/datetime2-spanish/datetime2-spanish.pdf

%files -n texlive-datetime2-spanish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-spanish/datetime2-spanish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-spanish/datetime2-spanish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-spanish/datetime2-spanish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-spanish-%{texlive_version}.%{texlive_noarch}.1.1svn45785-%{release}-zypper
%endif

%package -n texlive-datetime2-swedish
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36700
Release:        0
Summary:        Swedish language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-swedish-doc >= %{texlive_version}
Provides:       tex(datetime2-swedish-ascii.ldf)
Provides:       tex(datetime2-swedish-utf8.ldf)
Provides:       tex(datetime2-swedish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source73:       datetime2-swedish.tar.xz
Source74:       datetime2-swedish.doc.tar.xz

%description -n texlive-datetime2-swedish
This module provides the "swedish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-swedish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn36700
Release:        0
Summary:        Documentation for texlive-datetime2-swedish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-swedish-doc
This package includes the documentation for texlive-datetime2-swedish

%post -n texlive-datetime2-swedish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-swedish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-swedish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-swedish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-swedish/README
%{_texmfdistdir}/doc/latex/datetime2-swedish/datetime2-swedish.pdf

%files -n texlive-datetime2-swedish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-swedish/datetime2-swedish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-swedish/datetime2-swedish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-swedish/datetime2-swedish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-swedish-%{texlive_version}.%{texlive_noarch}.1.0svn36700-%{release}-zypper
%endif

%package -n texlive-datetime2-turkish
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52331
Release:        0
Summary:        Turkish language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-turkish-doc >= %{texlive_version}
Provides:       tex(datetime2-turkish-ascii.ldf)
Provides:       tex(datetime2-turkish-utf8.ldf)
Provides:       tex(datetime2-turkish.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source75:       datetime2-turkish.tar.xz
Source76:       datetime2-turkish.doc.tar.xz

%description -n texlive-datetime2-turkish
This module provides the "turkish" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-turkish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52331
Release:        0
Summary:        Documentation for texlive-datetime2-turkish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-turkish-doc
This package includes the documentation for texlive-datetime2-turkish

%post -n texlive-datetime2-turkish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-turkish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-turkish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-turkish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-turkish/README
%{_texmfdistdir}/doc/latex/datetime2-turkish/datetime2-turkish.pdf

%files -n texlive-datetime2-turkish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-turkish/datetime2-turkish-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-turkish/datetime2-turkish-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-turkish/datetime2-turkish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-turkish-%{texlive_version}.%{texlive_noarch}.1.1svn52331-%{release}-zypper
%endif

%package -n texlive-datetime2-ukrainian
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn47552
Release:        0
Summary:        Ukrainian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-ukrainian-doc >= %{texlive_version}
Provides:       tex(datetime2-ukrainian-ascii.ldf)
Provides:       tex(datetime2-ukrainian-utf8.ldf)
Provides:       tex(datetime2-ukrainian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source77:       datetime2-ukrainian.tar.xz
Source78:       datetime2-ukrainian.doc.tar.xz

%description -n texlive-datetime2-ukrainian
This module provides the "ukrainian" style that can be set
using \DTMsetstyle provided by datetime2.sty.

%package -n texlive-datetime2-ukrainian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2asvn47552
Release:        0
Summary:        Documentation for texlive-datetime2-ukrainian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-ukrainian-doc
This package includes the documentation for texlive-datetime2-ukrainian

%post -n texlive-datetime2-ukrainian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-ukrainian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-ukrainian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-ukrainian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-ukrainian/README.md
%{_texmfdistdir}/doc/latex/datetime2-ukrainian/datetime2-ukrainian.pdf

%files -n texlive-datetime2-ukrainian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-ukrainian/datetime2-ukrainian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-ukrainian/datetime2-ukrainian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-ukrainian/datetime2-ukrainian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-ukrainian-%{texlive_version}.%{texlive_noarch}.1.2asvn47552-%{release}-zypper
%endif

%package -n texlive-datetime2-usorbian
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52375
Release:        0
Summary:        Upper Sorbian language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-usorbian-doc >= %{texlive_version}
Provides:       tex(datetime2-usorbian-ascii.ldf)
Provides:       tex(datetime2-usorbian-utf8.ldf)
Provides:       tex(datetime2-usorbian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source79:       datetime2-usorbian.tar.xz
Source80:       datetime2-usorbian.doc.tar.xz

%description -n texlive-datetime2-usorbian
This module provides the "usorbian" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-usorbian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52375
Release:        0
Summary:        Documentation for texlive-datetime2-usorbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-usorbian-doc
This package includes the documentation for texlive-datetime2-usorbian

%post -n texlive-datetime2-usorbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-usorbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-usorbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-usorbian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-usorbian/README
%{_texmfdistdir}/doc/latex/datetime2-usorbian/datetime2-usorbian.pdf

%files -n texlive-datetime2-usorbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-usorbian/datetime2-usorbian-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-usorbian/datetime2-usorbian-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-usorbian/datetime2-usorbian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-usorbian-%{texlive_version}.%{texlive_noarch}.1.1svn52375-%{release}-zypper
%endif

%package -n texlive-datetime2-welsh
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52553
Release:        0
Summary:        Welsh language module for the datetime2 package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-datetime2-welsh-doc >= %{texlive_version}
Provides:       tex(datetime2-welsh-ascii.ldf)
Provides:       tex(datetime2-welsh-utf8.ldf)
Provides:       tex(datetime2-welsh.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source81:       datetime2-welsh.tar.xz
Source82:       datetime2-welsh.doc.tar.xz

%description -n texlive-datetime2-welsh
This module provides the "welsh" style that can be set using
\DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%package -n texlive-datetime2-welsh-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn52553
Release:        0
Summary:        Documentation for texlive-datetime2-welsh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-datetime2-welsh-doc
This package includes the documentation for texlive-datetime2-welsh

%post -n texlive-datetime2-welsh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-datetime2-welsh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-datetime2-welsh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-datetime2-welsh-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/datetime2-welsh/README
%{_texmfdistdir}/doc/latex/datetime2-welsh/datetime2-welsh.pdf

%files -n texlive-datetime2-welsh
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/datetime2-welsh/datetime2-welsh-ascii.ldf
%{_texmfdistdir}/tex/latex/datetime2-welsh/datetime2-welsh-utf8.ldf
%{_texmfdistdir}/tex/latex/datetime2-welsh/datetime2-welsh.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-datetime2-welsh-%{texlive_version}.%{texlive_noarch}.1.1svn52553-%{release}-zypper
%endif

%package -n texlive-dblfloatfix
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn28983
Release:        0
Summary:        Fixes for twocolumn floats
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dblfloatfix-doc >= %{texlive_version}
Provides:       tex(dblfloatfix.sty)
Requires:       tex(fixltx2e.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source83:       dblfloatfix.tar.xz
Source84:       dblfloatfix.doc.tar.xz

%description -n texlive-dblfloatfix
The package solves two problems: floats in a twocolumn document
come out in the right order and allowed float positions are now
[tbp]. The package actually merges facilities from fixltx2e and
stfloats.

%package -n texlive-dblfloatfix-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn28983
Release:        0
Summary:        Documentation for texlive-dblfloatfix
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dblfloatfix-doc
This package includes the documentation for texlive-dblfloatfix

%post -n texlive-dblfloatfix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dblfloatfix 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dblfloatfix
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dblfloatfix-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dblfloatfix/dblfloatfix.pdf
%{_texmfdistdir}/doc/latex/dblfloatfix/dblfloatfix.tex

%files -n texlive-dblfloatfix
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dblfloatfix/dblfloatfix.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dblfloatfix-%{texlive_version}.%{texlive_noarch}.1.0asvn28983-%{release}-zypper
%endif

%package -n texlive-dccpaper
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn54512
Release:        0
Summary:        Typeset papers for the International Journal of Digital Curation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dccpaper-doc >= %{texlive_version}
Provides:       tex(dccpaper-base.sty)
Provides:       tex(idcc.cls)
Provides:       tex(ijdc-v14.cls)
Provides:       tex(ijdc-v9.cls)
Requires:       tex(GoSans.sty)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(atbegshi.sty)
Requires:       tex(babel.sty)
Requires:       tex(baskervald.sty)
Requires:       tex(baskervillef.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(helvet.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(mathptmx.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(tgheros.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xpatch.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source85:       dccpaper.tar.xz
Source86:       dccpaper.doc.tar.xz

%description -n texlive-dccpaper
The LaTeX class ijdc-v14 produces camera-ready papers and
articles suitable for inclusion in the International Journal of
Digital Curation, with applicability from volume 14 onwards; a
legacy class ijdc-v9 is provided for papers and articles
written for volumes 9-13. The similar idcc class can be used
for submissions to the International Digital Curation
Conference, beginning with the 2015 conference.

%package -n texlive-dccpaper-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn54512
Release:        0
Summary:        Documentation for texlive-dccpaper
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dccpaper-doc
This package includes the documentation for texlive-dccpaper

%post -n texlive-dccpaper
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dccpaper 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dccpaper
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dccpaper-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dccpaper/README.md
%{_texmfdistdir}/doc/latex/dccpaper/dccpaper-apacite.bib
%{_texmfdistdir}/doc/latex/dccpaper/dccpaper-biblatex.bib
%{_texmfdistdir}/doc/latex/dccpaper/dccpaper.pdf

%files -n texlive-dccpaper
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dccpaper/dccpaper-base.sty
%{_texmfdistdir}/tex/latex/dccpaper/dccpaper-by.eps
%{_texmfdistdir}/tex/latex/dccpaper/dccpaper-by.pdf
%{_texmfdistdir}/tex/latex/dccpaper/idcc.cls
%{_texmfdistdir}/tex/latex/dccpaper/ijdc-v14.cls
%{_texmfdistdir}/tex/latex/dccpaper/ijdc-v9.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dccpaper-%{texlive_version}.%{texlive_noarch}.2.0svn54512-%{release}-zypper
%endif

%package -n texlive-dcpic
Version:        %{texlive_version}.%{texlive_noarch}.5.0.0svn30206
Release:        0
Summary:        Commutative diagrams in a LaTeX and TeX documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dcpic-doc >= %{texlive_version}
Provides:       tex(dcpic.sty)
Provides:       tex(europroc.cls)
Requires:       tex(article.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source87:       dcpic.tar.xz
Source88:       dcpic.doc.tar.xz

%description -n texlive-dcpic
DCpic is a package for typesetting Commutative Diagrams within
a LaTeX and TeX documents. Its distinguishing features are: a
powerful graphical engine, the PiCTeX package; an easy
specification syntax in which a commutative diagram is
described in terms of its objects and its arrows (morphism),
positioned in a Cartesian coordinate system.

%package -n texlive-dcpic-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.0.0svn30206
Release:        0
Summary:        Documentation for texlive-dcpic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-dcpic-doc:en;pt)

%description -n texlive-dcpic-doc
This package includes the documentation for texlive-dcpic

%post -n texlive-dcpic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dcpic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dcpic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dcpic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/dcpic/README
%{_texmfdistdir}/doc/generic/dcpic/eurotex2001.pdf
%{_texmfdistdir}/doc/generic/dcpic/eurotex2001.tex
%{_texmfdistdir}/doc/generic/dcpic/examples.pdf
%{_texmfdistdir}/doc/generic/dcpic/examples.tex
%{_texmfdistdir}/doc/generic/dcpic/manDCPiC.pdf
%{_texmfdistdir}/doc/generic/dcpic/manDCPiC.tex
%{_texmfdistdir}/doc/generic/dcpic/manDCPiCpt.pdf
%{_texmfdistdir}/doc/generic/dcpic/manDCPiCpt.tex

%files -n texlive-dcpic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/dcpic/dcpic.sty
%{_texmfdistdir}/tex/generic/dcpic/europroc.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dcpic-%{texlive_version}.%{texlive_noarch}.5.0.0svn30206-%{release}-zypper
%endif

%package -n texlive-ddphonism
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn52009
Release:        0
Summary:        Dodecaphonic diagrams: twelve-tone matrices, clock diagrams, etcetera
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ddphonism-doc >= %{texlive_version}
Provides:       tex(ddphonism.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source89:       ddphonism.tar.xz
Source90:       ddphonism.doc.tar.xz

%description -n texlive-ddphonism
This is a music-related package which is focused on notation
from the Twelve-Tone System, also called Dodecaphonism. It
provides LaTeX algorithms that produce typical dodecaphonic
notation based off a musical series, or row sequence, of
variable length. The package requires etoolbox, pgfkeys, TikZ,
xparse, and xstring.

%package -n texlive-ddphonism-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn52009
Release:        0
Summary:        Documentation for texlive-ddphonism
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ddphonism-doc
This package includes the documentation for texlive-ddphonism

%post -n texlive-ddphonism
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ddphonism 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ddphonism
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ddphonism-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ddphonism/README.md
%{_texmfdistdir}/doc/latex/ddphonism/ddphonism.pdf
%{_texmfdistdir}/doc/latex/ddphonism/ddphonism.tex

%files -n texlive-ddphonism
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ddphonism/ddphonism.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ddphonism-%{texlive_version}.%{texlive_noarch}.0.0.2svn52009-%{release}-zypper
%endif

%package -n texlive-de-macro
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn26355
Release:        0
Summary:        Expand private macros in a document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-de-macro-bin >= %{texlive_version}
#!BuildIgnore: texlive-de-macro-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-de-macro-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source91:       de-macro.tar.xz
Source92:       de-macro.doc.tar.xz

%description -n texlive-de-macro
De-macro is a Python script that helps authors who like to use
private LaTeX macros (for example, as abbreviations). A
technical editor or a cooperating author may balk at such a
manuscript; you can avoid manuscript rejection misery by
running de-macro on it. De-macro will expand macros defined in
\(re)newcommand or \(re)newenvironment commands, within the
document, or in the document's "private" package file.

%package -n texlive-de-macro-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn26355
Release:        0
Summary:        Documentation for texlive-de-macro
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-de-macro-doc
This package includes the documentation for texlive-de-macro

%post -n texlive-de-macro
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-de-macro 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-de-macro
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-de-macro-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/de-macro/README
%{_texmfdistdir}/doc/support/de-macro/user-guide.pdf
%{_texmfdistdir}/doc/support/de-macro/user-guide.tex

%files -n texlive-de-macro
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/de-macro/de-macro
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-de-macro-%{texlive_version}.%{texlive_noarch}.1.3svn26355-%{release}-zypper
%endif

%package -n texlive-decimal
Version:        %{texlive_version}.%{texlive_noarch}.svn23374
Release:        0
Summary:        LaTeX package for the English raised decimal point
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-decimal-doc >= %{texlive_version}
Provides:       tex(decimal.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source93:       decimal.tar.xz
Source94:       decimal.doc.tar.xz

%description -n texlive-decimal
This LaTeX package should be used by people who need the
traditional English raised decimal point, instead of the
American-style period.

%package -n texlive-decimal-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn23374
Release:        0
Summary:        Documentation for texlive-decimal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-decimal-doc
This package includes the documentation for texlive-decimal

%post -n texlive-decimal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-decimal 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-decimal
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-decimal-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/decimal/decimal.pdf

%files -n texlive-decimal
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/decimal/decimal.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-decimal-%{texlive_version}.%{texlive_noarch}.svn23374-%{release}-zypper
%endif

%package -n texlive-decorule
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn23487
Release:        0
Summary:        Decorative swelled rule using font character
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-decorule-doc >= %{texlive_version}
Provides:       tex(decorule.sty)
Requires:       tex(fix-cm.sty)
Requires:       tex(graphicx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source95:       decorule.tar.xz
Source96:       decorule.doc.tar.xz

%description -n texlive-decorule
The package implements a decorative swelled rule using only a
symbol from a font installed with all distributions of TeX, so
it works independently, without the need to install any
additional software or fonts. This is the packaged version of
the macro which was originally published in the "Typographers'
Inn" column in TUGboat 31:1 (2010).

%package -n texlive-decorule-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn23487
Release:        0
Summary:        Documentation for texlive-decorule
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-decorule-doc
This package includes the documentation for texlive-decorule

%post -n texlive-decorule
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-decorule 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-decorule
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-decorule-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/decorule/MANIFEST
%{_texmfdistdir}/doc/latex/decorule/README
%{_texmfdistdir}/doc/latex/decorule/decorule.pdf

%files -n texlive-decorule
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/decorule/decorule.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-decorule-%{texlive_version}.%{texlive_noarch}.0.0.6svn23487-%{release}-zypper
%endif

%package -n texlive-dehyph
Version:        %{texlive_version}.%{texlive_noarch}.svn48599
Release:        0
Summary:        German hyphenation patterns for traditional orthography
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       tex(dehyphn.tex)
Provides:       tex(dehypht.tex)
Provides:       tex(dehyphtex.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source97:       dehyph.tar.xz

%description -n texlive-dehyph
The package provides older hyphenation patterns for the German
language. Please note that by default only pdfLaTeX uses these
patterns (mainly for backwards compatibility). The older
packages ghyphen and gnhyph are now bundled together with
dehyph, and are no longer be updated. Both XeLaTeX and LuaLaTeX
use the current German hyphenation patterns taken from
Hyphenation patterns in UTF-8, and using the Experimental
hyphenation patterns for the German language package it is
possible to make pdfLaTeX use the new German patterns as well.
%post -n texlive-dehyph
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dehyph 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dehyph
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dehyph
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/dehyph/README
%{_texmfdistdir}/tex/generic/dehyph/dehyphn.tex
%{_texmfdistdir}/tex/generic/dehyph/dehypht.tex
%{_texmfdistdir}/tex/generic/dehyph/dehyphtex.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dehyph-%{texlive_version}.%{texlive_noarch}.svn48599-%{release}-zypper
%endif

%package -n texlive-dehyph-exptl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn54512
Release:        0
Summary:        Experimental hyphenation patterns for the German language
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-hyph-utf8 >= %{texlive_version}
#!BuildIgnore: texlive-hyph-utf8
Requires:       texlive-hyphen-base >= %{texlive_version}
#!BuildIgnore: texlive-hyphen-base
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
Recommends:     texlive-dehyph-exptl-doc >= %{texlive_version}
Provides:       tex(dehyphn-x-2019-04-04.tex)
Provides:       tex(dehypht-x-2019-04-04.tex)
Provides:       tex(dehyphts-x-2019-04-04.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source98:       dehyph-exptl.tar.xz
Source99:       dehyph-exptl.doc.tar.xz

%description -n texlive-dehyph-exptl
The package provides experimental hyphenation patterns for the
German language, covering both traditional and reformed
orthography. The patterns can be used with packages Babel and
hyphsubst from the Oberdiek bundle. Dieses Paket enthalt
experimentelle Trennmuster fur die deutsche Sprache. Die
Trennmuster decken das in Deutschland, Osterreich und der
Schweiz gebrauchliche Standarddeutsch in der traditionellen und
reformierten Rechtschreibung ab und konnen mit den Paketen
Babel und hyphsubst aus dem Oberdiek-Bundel verwendet werden.

%package -n texlive-dehyph-exptl-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn54512
Release:        0
Summary:        Documentation for texlive-dehyph-exptl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-dehyph-exptl-doc:de)

%description -n texlive-dehyph-exptl-doc
This package includes the documentation for texlive-dehyph-exptl

%post -n texlive-dehyph-exptl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
> /var/run/texlive/run-fmtutil.language
> /var/run/texlive/run-hyphen

%postun -n texlive-dehyph-exptl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    > /var/run/texlive/run-fmtutil.language
    > /var/run/texlive/run-hyphen
    exit 0
fi

%posttrans -n texlive-dehyph-exptl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dehyph-exptl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/dehyph-exptl/CHANGES
%{_texmfdistdir}/doc/generic/dehyph-exptl/INSTALL
%{_texmfdistdir}/doc/generic/dehyph-exptl/LICENSE.data
%{_texmfdistdir}/doc/generic/dehyph-exptl/LICENSE.documentation
%{_texmfdistdir}/doc/generic/dehyph-exptl/README
%{_texmfdistdir}/doc/generic/dehyph-exptl/dehyph-exptl.bib
%{_texmfdistdir}/doc/generic/dehyph-exptl/dehyph-exptl.pdf
%{_texmfdistdir}/doc/generic/dehyph-exptl/dehyph-exptl.tex

%files -n texlive-dehyph-exptl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphn-x-2019-04-04.pat
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphn-x-2019-04-04.tex
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehypht-x-2019-04-04.pat
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehypht-x-2019-04-04.tex
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphts-x-2019-04-04.pat
%{_texmfdistdir}/tex/generic/dehyph-exptl/dehyphts-x-2019-04-04.tex
%{_texmfdistdir}/tex/generic/config/language.splits/dehyph-exptl.dat
%{_texmfdistdir}/tex/generic/config/language.splits/dehyph-exptl.def
%{_texmfdistdir}/tex/generic/config/language.splits/dehyph-exptl.dat.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dehyph-exptl-%{texlive_version}.%{texlive_noarch}.0.0.6svn54512-%{release}-zypper
%endif

%package -n texlive-dejavu
Version:        %{texlive_version}.%{texlive_noarch}.2.34svn31771
Release:        0
Summary:        LaTeX support for the DejaVu fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
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
Requires:       texlive-dejavu-fonts >= %{texlive_version}
Recommends:     texlive-dejavu-doc >= %{texlive_version}
Provides:       tex(DejaVuSans-Bold-tlf-il2.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-lgr.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-ot1.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-qx--base.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-qx.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-qx.vf)
Provides:       tex(DejaVuSans-Bold-tlf-t1--base.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-t1.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-t1.vf)
Provides:       tex(DejaVuSans-Bold-tlf-t2a.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-t2b.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-t2c.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-ts1.tfm)
Provides:       tex(DejaVuSans-Bold-tlf-ts1.vf)
Provides:       tex(DejaVuSans-Bold-tlf-x2.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-il2.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-lgr.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-ot1.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-qx--base.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-qx.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-qx.vf)
Provides:       tex(DejaVuSans-BoldOblique-tlf-t1--base.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-t1.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-t1.vf)
Provides:       tex(DejaVuSans-BoldOblique-tlf-t2a.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-t2b.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-t2c.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-ts1.tfm)
Provides:       tex(DejaVuSans-BoldOblique-tlf-ts1.vf)
Provides:       tex(DejaVuSans-BoldOblique-tlf-x2.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-il2.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-lgr.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-ot1.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-qx--base.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-qx.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-qx.vf)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t1--base.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t1.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t1.vf)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2a--base.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2a.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2a.vf)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2b--base.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2b.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2b.vf)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2c--base.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2c.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-t2c.vf)
Provides:       tex(DejaVuSans-ExtraLight-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-ts1.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-ts1.vf)
Provides:       tex(DejaVuSans-ExtraLight-tlf-x2--base.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-x2.tfm)
Provides:       tex(DejaVuSans-ExtraLight-tlf-x2.vf)
Provides:       tex(DejaVuSans-Oblique-tlf-il2.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-lgr.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-ot1.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-qx--base.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-qx.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-qx.vf)
Provides:       tex(DejaVuSans-Oblique-tlf-t1--base.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-t1.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-t1.vf)
Provides:       tex(DejaVuSans-Oblique-tlf-t2a.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-t2b.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-t2c.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-ts1.tfm)
Provides:       tex(DejaVuSans-Oblique-tlf-ts1.vf)
Provides:       tex(DejaVuSans-Oblique-tlf-x2.tfm)
Provides:       tex(DejaVuSans-tlf-il2.tfm)
Provides:       tex(DejaVuSans-tlf-lgr.tfm)
Provides:       tex(DejaVuSans-tlf-ot1.tfm)
Provides:       tex(DejaVuSans-tlf-qx--base.tfm)
Provides:       tex(DejaVuSans-tlf-qx.tfm)
Provides:       tex(DejaVuSans-tlf-qx.vf)
Provides:       tex(DejaVuSans-tlf-t1--base.tfm)
Provides:       tex(DejaVuSans-tlf-t1.tfm)
Provides:       tex(DejaVuSans-tlf-t1.vf)
Provides:       tex(DejaVuSans-tlf-t2a.tfm)
Provides:       tex(DejaVuSans-tlf-t2b.tfm)
Provides:       tex(DejaVuSans-tlf-t2c.tfm)
Provides:       tex(DejaVuSans-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSans-tlf-ts1.tfm)
Provides:       tex(DejaVuSans-tlf-ts1.vf)
Provides:       tex(DejaVuSans-tlf-x2.tfm)
Provides:       tex(DejaVuSans.sty)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-il2.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-lgr.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ot1.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-qx.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-qx.vf)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t1.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t1.vf)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t2a.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t2b.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-t2c.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ts1.tfm)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-ts1.vf)
Provides:       tex(DejaVuSansCondensed-Bold-tlf-x2.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-il2.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-lgr.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ot1.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-qx.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-qx.vf)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t1.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t1.vf)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t2a.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t2b.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-t2c.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ts1.tfm)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-ts1.vf)
Provides:       tex(DejaVuSansCondensed-BoldOblique-tlf-x2.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-il2.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-lgr.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ot1.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-qx.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-qx.vf)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t1.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t1.vf)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t2a.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t2b.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-t2c.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ts1.tfm)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-ts1.vf)
Provides:       tex(DejaVuSansCondensed-Oblique-tlf-x2.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-il2.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-lgr.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-ot1.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-qx.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-qx.vf)
Provides:       tex(DejaVuSansCondensed-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-t1.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-t1.vf)
Provides:       tex(DejaVuSansCondensed-tlf-t2a.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-t2b.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-t2c.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-ts1.tfm)
Provides:       tex(DejaVuSansCondensed-tlf-ts1.vf)
Provides:       tex(DejaVuSansCondensed-tlf-x2.tfm)
Provides:       tex(DejaVuSansCondensed.sty)
Provides:       tex(DejaVuSansMono-Bold-tlf-il2.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-lgr--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-lgr.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-lgr.vf)
Provides:       tex(DejaVuSansMono-Bold-tlf-ot1.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-qx.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-qx.vf)
Provides:       tex(DejaVuSansMono-Bold-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t1.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t1.vf)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2a--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2a.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2a.vf)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2b--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2b.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2b.vf)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2c--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2c.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-t2c.vf)
Provides:       tex(DejaVuSansMono-Bold-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-ts1.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-ts1.vf)
Provides:       tex(DejaVuSansMono-Bold-tlf-x2--base.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-x2.tfm)
Provides:       tex(DejaVuSansMono-Bold-tlf-x2.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-il2.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-lgr--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-lgr.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-lgr.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ot1.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-qx.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-qx.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t1.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t1.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2a--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2a.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2a.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2b--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2b.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2b.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2c--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2c.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-t2c.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ts1.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-ts1.vf)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-x2--base.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-x2.tfm)
Provides:       tex(DejaVuSansMono-BoldOblique-tlf-x2.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-il2.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-lgr--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-lgr.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-lgr.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-ot1.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-qx.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-qx.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t1.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t1.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2a--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2a.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2a.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2b--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2b.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2b.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2c--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2c.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-t2c.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-ts1.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-ts1.vf)
Provides:       tex(DejaVuSansMono-Oblique-tlf-x2--base.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-x2.tfm)
Provides:       tex(DejaVuSansMono-Oblique-tlf-x2.vf)
Provides:       tex(DejaVuSansMono-tlf-il2.tfm)
Provides:       tex(DejaVuSansMono-tlf-lgr--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-lgr.tfm)
Provides:       tex(DejaVuSansMono-tlf-lgr.vf)
Provides:       tex(DejaVuSansMono-tlf-ot1.tfm)
Provides:       tex(DejaVuSansMono-tlf-qx--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-qx.tfm)
Provides:       tex(DejaVuSansMono-tlf-qx.vf)
Provides:       tex(DejaVuSansMono-tlf-t1--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-t1.tfm)
Provides:       tex(DejaVuSansMono-tlf-t1.vf)
Provides:       tex(DejaVuSansMono-tlf-t2a--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-t2a.tfm)
Provides:       tex(DejaVuSansMono-tlf-t2a.vf)
Provides:       tex(DejaVuSansMono-tlf-t2b--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-t2b.tfm)
Provides:       tex(DejaVuSansMono-tlf-t2b.vf)
Provides:       tex(DejaVuSansMono-tlf-t2c--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-t2c.tfm)
Provides:       tex(DejaVuSansMono-tlf-t2c.vf)
Provides:       tex(DejaVuSansMono-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-ts1.tfm)
Provides:       tex(DejaVuSansMono-tlf-ts1.vf)
Provides:       tex(DejaVuSansMono-tlf-x2--base.tfm)
Provides:       tex(DejaVuSansMono-tlf-x2.tfm)
Provides:       tex(DejaVuSansMono-tlf-x2.vf)
Provides:       tex(DejaVuSansMono.sty)
Provides:       tex(DejaVuSerif-Bold-tlf-il2.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-lgr.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-ot1.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-qx.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-qx.vf)
Provides:       tex(DejaVuSerif-Bold-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-t1.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-t1.vf)
Provides:       tex(DejaVuSerif-Bold-tlf-t2a.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-t2b.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-t2c.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-ts1.tfm)
Provides:       tex(DejaVuSerif-Bold-tlf-ts1.vf)
Provides:       tex(DejaVuSerif-Bold-tlf-x2.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-il2.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-lgr.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ot1.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-qx.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-qx.vf)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t1.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t1.vf)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t2a.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t2b.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-t2c.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ts1.tfm)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-ts1.vf)
Provides:       tex(DejaVuSerif-BoldItalic-tlf-x2.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-il2.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-lgr.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-ot1.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-qx.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-qx.vf)
Provides:       tex(DejaVuSerif-Italic-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-t1.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-t1.vf)
Provides:       tex(DejaVuSerif-Italic-tlf-t2a.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-t2b.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-t2c.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-ts1.tfm)
Provides:       tex(DejaVuSerif-Italic-tlf-ts1.vf)
Provides:       tex(DejaVuSerif-Italic-tlf-x2.tfm)
Provides:       tex(DejaVuSerif-tlf-il2.tfm)
Provides:       tex(DejaVuSerif-tlf-lgr.tfm)
Provides:       tex(DejaVuSerif-tlf-ot1.tfm)
Provides:       tex(DejaVuSerif-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerif-tlf-qx.tfm)
Provides:       tex(DejaVuSerif-tlf-qx.vf)
Provides:       tex(DejaVuSerif-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerif-tlf-t1.tfm)
Provides:       tex(DejaVuSerif-tlf-t1.vf)
Provides:       tex(DejaVuSerif-tlf-t2a.tfm)
Provides:       tex(DejaVuSerif-tlf-t2b.tfm)
Provides:       tex(DejaVuSerif-tlf-t2c.tfm)
Provides:       tex(DejaVuSerif-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerif-tlf-ts1.tfm)
Provides:       tex(DejaVuSerif-tlf-ts1.vf)
Provides:       tex(DejaVuSerif-tlf-x2.tfm)
Provides:       tex(DejaVuSerif.sty)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-il2.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-lgr.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ot1.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-qx.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-qx.vf)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t1.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t1.vf)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t2a.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t2b.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-t2c.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ts1.tfm)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-ts1.vf)
Provides:       tex(DejaVuSerifCondensed-Bold-tlf-x2.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-il2.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-lgr.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ot1.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-qx.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-qx.vf)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t1.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t1.vf)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t2a.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t2b.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-t2c.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ts1.tfm)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-ts1.vf)
Provides:       tex(DejaVuSerifCondensed-BoldItalic-tlf-x2.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-il2.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-lgr.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ot1.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-qx.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-qx.vf)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t1.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t1.vf)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t2a.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t2b.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-t2c.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ts1.tfm)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-ts1.vf)
Provides:       tex(DejaVuSerifCondensed-Italic-tlf-x2.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-il2.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-lgr.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-ot1.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-qx--base.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-qx.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-qx.vf)
Provides:       tex(DejaVuSerifCondensed-tlf-t1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-t1.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-t1.vf)
Provides:       tex(DejaVuSerifCondensed-tlf-t2a.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-t2b.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-t2c.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-ts1--base.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-ts1.tfm)
Provides:       tex(DejaVuSerifCondensed-tlf-ts1.vf)
Provides:       tex(DejaVuSerifCondensed-tlf-x2.tfm)
Provides:       tex(DejaVuSerifCondensed.sty)
Provides:       tex(IL2DejaVuSans-TLF.fd)
Provides:       tex(IL2DejaVuSansCondensed-TLF.fd)
Provides:       tex(IL2DejaVuSansMono-TLF.fd)
Provides:       tex(IL2DejaVuSerif-TLF.fd)
Provides:       tex(IL2DejaVuSerifCondensed-TLF.fd)
Provides:       tex(LGRDejaVuSans-TLF.fd)
Provides:       tex(LGRDejaVuSansCondensed-TLF.fd)
Provides:       tex(LGRDejaVuSansMono-TLF.fd)
Provides:       tex(LGRDejaVuSerif-TLF.fd)
Provides:       tex(LGRDejaVuSerifCondensed-TLF.fd)
Provides:       tex(OT1DejaVuSans-TLF.fd)
Provides:       tex(OT1DejaVuSansCondensed-TLF.fd)
Provides:       tex(OT1DejaVuSansMono-TLF.fd)
Provides:       tex(OT1DejaVuSerif-TLF.fd)
Provides:       tex(OT1DejaVuSerifCondensed-TLF.fd)
Provides:       tex(QXDejaVuSans-TLF.fd)
Provides:       tex(QXDejaVuSansCondensed-TLF.fd)
Provides:       tex(QXDejaVuSansMono-TLF.fd)
Provides:       tex(QXDejaVuSerif-TLF.fd)
Provides:       tex(QXDejaVuSerifCondensed-TLF.fd)
Provides:       tex(T1DejaVuSans-TLF.fd)
Provides:       tex(T1DejaVuSansCondensed-TLF.fd)
Provides:       tex(T1DejaVuSansMono-TLF.fd)
Provides:       tex(T1DejaVuSerif-TLF.fd)
Provides:       tex(T1DejaVuSerifCondensed-TLF.fd)
Provides:       tex(T2ADejaVuSans-TLF.fd)
Provides:       tex(T2ADejaVuSansCondensed-TLF.fd)
Provides:       tex(T2ADejaVuSansMono-TLF.fd)
Provides:       tex(T2ADejaVuSerif-TLF.fd)
Provides:       tex(T2ADejaVuSerifCondensed-TLF.fd)
Provides:       tex(T2BDejaVuSans-TLF.fd)
Provides:       tex(T2BDejaVuSansCondensed-TLF.fd)
Provides:       tex(T2BDejaVuSansMono-TLF.fd)
Provides:       tex(T2BDejaVuSerif-TLF.fd)
Provides:       tex(T2BDejaVuSerifCondensed-TLF.fd)
Provides:       tex(T2CDejaVuSans-TLF.fd)
Provides:       tex(T2CDejaVuSansCondensed-TLF.fd)
Provides:       tex(T2CDejaVuSansMono-TLF.fd)
Provides:       tex(T2CDejaVuSerif-TLF.fd)
Provides:       tex(T2CDejaVuSerifCondensed-TLF.fd)
Provides:       tex(TS1DejaVuSans-TLF.fd)
Provides:       tex(TS1DejaVuSansCondensed-TLF.fd)
Provides:       tex(TS1DejaVuSansMono-TLF.fd)
Provides:       tex(TS1DejaVuSerif-TLF.fd)
Provides:       tex(TS1DejaVuSerifCondensed-TLF.fd)
Provides:       tex(X2DejaVuSans-TLF.fd)
Provides:       tex(X2DejaVuSansCondensed-TLF.fd)
Provides:       tex(X2DejaVuSansMono-TLF.fd)
Provides:       tex(X2DejaVuSerif-TLF.fd)
Provides:       tex(X2DejaVuSerifCondensed-TLF.fd)
Provides:       tex(dejavu-truetype.map)
Provides:       tex(dejavu-type1.map)
Provides:       tex(dejavu.sty)
Provides:       tex(dejavumono_il2.enc)
Provides:       tex(dejavumono_lgr.enc)
Provides:       tex(dejavumono_ot1.enc)
Provides:       tex(dejavumono_qx.enc)
Provides:       tex(dejavumono_t1-truetype.enc)
Provides:       tex(dejavumono_t1-type1.enc)
Provides:       tex(dejavumono_t2a.enc)
Provides:       tex(dejavumono_t2b.enc)
Provides:       tex(dejavumono_t2c.enc)
Provides:       tex(dejavumono_ts1.enc)
Provides:       tex(dejavumono_x2.enc)
Provides:       tex(dejavusans_il2.enc)
Provides:       tex(dejavusans_lgr.enc)
Provides:       tex(dejavusans_ot1.enc)
Provides:       tex(dejavusans_qx.enc)
Provides:       tex(dejavusans_t1-truetype.enc)
Provides:       tex(dejavusans_t1-type1.enc)
Provides:       tex(dejavusans_t2a.enc)
Provides:       tex(dejavusans_t2b.enc)
Provides:       tex(dejavusans_t2c.enc)
Provides:       tex(dejavusans_ts1.enc)
Provides:       tex(dejavusans_x2.enc)
Provides:       tex(dejavusanslight_il2.enc)
Provides:       tex(dejavusanslight_lgr.enc)
Provides:       tex(dejavusanslight_ot1.enc)
Provides:       tex(dejavusanslight_qx.enc)
Provides:       tex(dejavusanslight_t1-truetype.enc)
Provides:       tex(dejavusanslight_t1-type1.enc)
Provides:       tex(dejavusanslight_t2a.enc)
Provides:       tex(dejavusanslight_t2b.enc)
Provides:       tex(dejavusanslight_t2c.enc)
Provides:       tex(dejavusanslight_ts1.enc)
Provides:       tex(dejavusanslight_x2.enc)
Provides:       tex(dejavuserif_il2.enc)
Provides:       tex(dejavuserif_lgr.enc)
Provides:       tex(dejavuserif_ot1.enc)
Provides:       tex(dejavuserif_qx.enc)
Provides:       tex(dejavuserif_t1-truetype.enc)
Provides:       tex(dejavuserif_t1-type1.enc)
Provides:       tex(dejavuserif_t2a.enc)
Provides:       tex(dejavuserif_t2b.enc)
Provides:       tex(dejavuserif_t2c.enc)
Provides:       tex(dejavuserif_ts1.enc)
Provides:       tex(dejavuserif_x2.enc)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source100:      dejavu.tar.xz
Source101:      dejavu.doc.tar.xz

%description -n texlive-dejavu
The package contains LaTeX support for the DejaVu fonts, which
are derived from the Vera fonts but contain more characters and
styles. The fonts are included in the original TrueType format,
and in converted Type 1 format. The (currently) supported
encodings are: OT1, T1, IL2, TS1, T2*, X2, QX, and LGR. The
package doesn't (currently) support mathematics. More encodings
and/or features are expected.

%package -n texlive-dejavu-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.34svn31771
Release:        0
Summary:        Documentation for texlive-dejavu
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dejavu-doc
This package includes the documentation for texlive-dejavu


%package -n texlive-dejavu-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.34svn31771
Release:        0
Summary:        Severed fonts for texlive-dejavu
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-dejavu-fonts
The  separated fonts package for texlive-dejavu
%post -n texlive-dejavu
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap dejavu-type1.map' >> /var/run/texlive/run-updmap

%postun -n texlive-dejavu 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap dejavu-type1.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-dejavu
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-dejavu-fonts
%files -n texlive-dejavu-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dejavu/AUTHORS
%{_texmfdistdir}/doc/fonts/dejavu/BUGS
%{_texmfdistdir}/doc/fonts/dejavu/CHANGELOG
%{_texmfdistdir}/doc/fonts/dejavu/LICENSE
%{_texmfdistdir}/doc/fonts/dejavu/NEWS
%{_texmfdistdir}/doc/fonts/dejavu/README-font
%{_texmfdistdir}/doc/fonts/dejavu/README.doc
%{_texmfdistdir}/doc/fonts/dejavu/dejavu-sample.pdf
%{_texmfdistdir}/doc/fonts/dejavu/dejavu-sample.tex
%{_texmfdistdir}/doc/fonts/dejavu/dejavu.pdf
%{_texmfdistdir}/doc/fonts/dejavu/dejavu.tex
%{_texmfdistdir}/doc/fonts/dejavu/extrakerns.zip
%{_texmfdistdir}/doc/fonts/dejavu/langcover.txt
%{_texmfdistdir}/doc/fonts/dejavu/manifest.txt
%{_texmfdistdir}/doc/fonts/dejavu/status.txt
%{_texmfdistdir}/doc/fonts/dejavu/unicover.txt

%files -n texlive-dejavu
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans-BoldOblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans-ExtraLight.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans-Oblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSans.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed-BoldOblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed-Oblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansCondensed.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono-BoldOblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono-Oblique.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSansMono.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif-Italic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerif.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed-Italic.afm
%{_texmfdistdir}/fonts/afm/public/dejavu/DejaVuSerifCondensed.afm
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_qx.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t1-truetype.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t1-type1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavumono_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_qx.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t1-truetype.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t1-type1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusans_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_qx.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_t1-truetype.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_t1-type1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavusanslight_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_lgr.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_qx.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t1-truetype.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t1-type1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/dejavu/dejavuserif_x2.enc
%{_texmfdistdir}/fonts/map/dvips/dejavu/dejavu-truetype.map
%{_texmfdistdir}/fonts/map/dvips/dejavu/dejavu-type1.map
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-BoldOblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-ExtraLight-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-Oblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSans-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-Oblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansCondensed-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-BoldOblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-Oblique-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSansMono-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerif-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-qx--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-qx.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/dejavu/DejaVuSerifCondensed-tlf-x2.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans-BoldOblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans-ExtraLight.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans-Oblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSans.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed-BoldOblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed-Oblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansCondensed.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono-BoldOblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono-Oblique.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSansMono.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif-BoldItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerif.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed-BoldItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/dejavu/DejaVuSerifCondensed.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Bold.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-BoldOblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-BoldOblique.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-ExtraLight.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-ExtraLight.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Oblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans-Oblique.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSans.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Bold.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-BoldOblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-BoldOblique.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Oblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed-Oblique.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansCondensed.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Bold.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-BoldOblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-BoldOblique.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Oblique.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono-Oblique.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSansMono.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Bold.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-BoldItalic.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif-Italic.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerif.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Bold.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-BoldItalic.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed-Italic.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed.pfb
%{_texmfdistdir}/fonts/type1/public/dejavu/DejaVuSerifCondensed.pfm
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-BoldOblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-BoldOblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-BoldOblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-ExtraLight-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-ExtraLight-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-ExtraLight-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-ExtraLight-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-ExtraLight-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-ExtraLight-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-ExtraLight-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Oblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Oblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-Oblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSans-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-BoldOblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Oblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Oblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-Oblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansCondensed-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Bold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-BoldOblique-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-Oblique-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSansMono-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-BoldItalic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Italic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerif-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Bold-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Italic-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-tlf-qx.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/dejavu/DejaVuSerifCondensed-tlf-ts1.vf
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSans.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSansCondensed.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSansMono.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSerif.sty
%{_texmfdistdir}/tex/latex/dejavu/DejaVuSerifCondensed.sty
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/IL2DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/LGRDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/OT1DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/QXDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T1DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2ADejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2BDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/T2CDejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/TS1DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSans-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSansCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSansMono-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSerif-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/X2DejaVuSerifCondensed-TLF.fd
%{_texmfdistdir}/tex/latex/dejavu/dejavu.sty

%files -n texlive-dejavu-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-dejavu
%{_datadir}/fontconfig/conf.avail/58-texlive-dejavu.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-dejavu.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-dejavu.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dejavu/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dejavu/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dejavu/fonts.scale
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-Bold.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-BoldOblique.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-ExtraLight.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-Oblique.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSans.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed-Bold.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed-BoldOblique.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed-Oblique.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono-Bold.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono-BoldOblique.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono-Oblique.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif-Bold.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif-BoldItalic.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif-Italic.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed-Bold.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed-Italic.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed.ttf
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-Bold.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-BoldOblique.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-ExtraLight.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSans-Oblique.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSans.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed-Bold.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed-BoldOblique.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed-Oblique.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansCondensed.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono-Bold.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono-BoldOblique.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono-Oblique.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSansMono.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif-Bold.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif-BoldItalic.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif-Italic.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerif.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed-Bold.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed-BoldItalic.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed-Italic.pfb
%{_datadir}/fonts/texlive-dejavu/DejaVuSerifCondensed.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dejavu-fonts-%{texlive_version}.%{texlive_noarch}.2.34svn31771-%{release}-zypper
%endif

%package -n texlive-dejavu-otf
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn45991
Release:        0
Summary:        Support for the ttf and otf DejaVu fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dejavu-otf-doc >= %{texlive_version}
Provides:       tex(dejavu-otf.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source102:      dejavu-otf.tar.xz
Source103:      dejavu-otf.doc.tar.xz

%description -n texlive-dejavu-otf
Package dejavu-otf supports the free ttf-fonts from the DejaVu
project which are available from GitHub or already part of your
system (Windows/Linux/...) and the OpenType version of the
TeXGyre Math, which is part of any TeX distribution.. Following
font files are supported: DejaVuSans-BoldOblique.ttf
DejaVuSans-Bold.ttf DejaVuSansCondensed-BoldOblique.ttf
DejaVuSansCondensed-Bold.ttf DejaVuSansCondensed-Oblique.ttf
DejaVuSansCondensed.ttf DejaVuSans-ExtraLight.ttf
DejaVuSansMono-BoldOblique.ttf DejaVuSansMono-Bold.ttf
DejaVuSansMono-Oblique.ttf DejaVuSansMono.ttf
DejaVuSans-Oblique.ttf DejaVuSans.ttf
DejaVuSerif-BoldItalic.ttf DejaVuSerif-Bold.ttf
DejaVuSerifCondensed-BoldItalic.ttf
DejaVuSerifCondensed-Bold.ttf DejaVuSerifCondensed-Italic.ttf
DejaVuSerifCondensed.ttf DejaVuSerif-Italic.ttf DejaVuSerif.ttf
texgyredejavu-math.otf

%package -n texlive-dejavu-otf-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.04svn45991
Release:        0
Summary:        Documentation for texlive-dejavu-otf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dejavu-otf-doc
This package includes the documentation for texlive-dejavu-otf

%post -n texlive-dejavu-otf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dejavu-otf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dejavu-otf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dejavu-otf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dejavu-otf/Changes
%{_texmfdistdir}/doc/fonts/dejavu-otf/README.md
%{_texmfdistdir}/doc/fonts/dejavu-otf/dejavu-otf-doc.bib
%{_texmfdistdir}/doc/fonts/dejavu-otf/dejavu-otf-doc.fonts
%{_texmfdistdir}/doc/fonts/dejavu-otf/dejavu-otf-doc.pdf
%{_texmfdistdir}/doc/fonts/dejavu-otf/dejavu-otf-doc.tex

%files -n texlive-dejavu-otf
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dejavu-otf/dejavu-otf.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dejavu-otf-%{texlive_version}.%{texlive_noarch}.0.0.04svn45991-%{release}-zypper
%endif

%package -n texlive-delim
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23974
Release:        0
Summary:        Simplify typesetting mathematical delimiters
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-delim-doc >= %{texlive_version}
Provides:       tex(delim.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source104:      delim.tar.xz
Source105:      delim.doc.tar.xz

%description -n texlive-delim
The package permits simpler control of delimiters without
excessive use of \big... commands (and the like).

%package -n texlive-delim-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn23974
Release:        0
Summary:        Documentation for texlive-delim
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-delim-doc
This package includes the documentation for texlive-delim

%post -n texlive-delim
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-delim 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-delim
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-delim-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/delim/README
%{_texmfdistdir}/doc/latex/delim/delim.pdf

%files -n texlive-delim
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/delim/delim.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-delim-%{texlive_version}.%{texlive_noarch}.1.0svn23974-%{release}-zypper
%endif

%package -n texlive-delimseasy
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn39589
Release:        0
Summary:        Delimiter commands that are easy to use and resize
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-delimseasy-doc >= %{texlive_version}
Provides:       tex(delimseasy.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source106:      delimseasy.tar.xz
Source107:      delimseasy.doc.tar.xz

%description -n texlive-delimseasy
This package provides commands to give a consistent,
easy-to-remember, easy to edit way to control the size and
blackness of delimiters: append 1-4 "b"s to command for larger
sizes; prepend "B" for for boldface. These commands reduce the
likelihood of incomplete delimeter pairs and typically use
fewer characters than the LaTeX default.

%package -n texlive-delimseasy-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn39589
Release:        0
Summary:        Documentation for texlive-delimseasy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-delimseasy-doc
This package includes the documentation for texlive-delimseasy

%post -n texlive-delimseasy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-delimseasy 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-delimseasy
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-delimseasy-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/delimseasy/README.txt
%{_texmfdistdir}/doc/latex/delimseasy/delimseasyMan.pdf
%{_texmfdistdir}/doc/latex/delimseasy/delimseasyMan.tex

%files -n texlive-delimseasy
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/delimseasy/delimseasy.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-delimseasy-%{texlive_version}.%{texlive_noarch}.2.0svn39589-%{release}-zypper
%endif

%package -n texlive-delimset
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49544
Release:        0
Summary:        Typeset and declare sets of delimiters with convenient size control
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-delimset-doc >= %{texlive_version}
Provides:       tex(delimset.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source108:      delimset.tar.xz
Source109:      delimset.doc.tar.xz

%description -n texlive-delimset
delimset is a LaTeX2e package to typeset and declare sets of
delimiters in math mode whose size can be adjusted
conveniently.

%package -n texlive-delimset-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn49544
Release:        0
Summary:        Documentation for texlive-delimset
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-delimset-doc
This package includes the documentation for texlive-delimset

%post -n texlive-delimset
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-delimset 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-delimset
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-delimset-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/delimset/README.txt
%{_texmfdistdir}/doc/latex/delimset/delimset.pdf
%{_texmfdistdir}/doc/latex/delimset/dlmssamp.tex

%files -n texlive-delimset
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/delimset/delimset.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-delimset-%{texlive_version}.%{texlive_noarch}.1.1svn49544-%{release}-zypper
%endif

%package -n texlive-delimtxt
Version:        %{texlive_version}.%{texlive_noarch}.svn16549
Release:        0
Summary:        Read and parse text tables
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-delimtxt-doc >= %{texlive_version}
Provides:       tex(delimtxt.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source110:      delimtxt.tar.xz
Source111:      delimtxt.doc.tar.xz

%description -n texlive-delimtxt
This experimental package can read and parse text tables
delimited by user-defined tokens (e.g., tab). It can be used
for serial letters and the like, making it easier to export the
data file from MS-Excel/MS-Word

%package -n texlive-delimtxt-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn16549
Release:        0
Summary:        Documentation for texlive-delimtxt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-delimtxt-doc
This package includes the documentation for texlive-delimtxt

%post -n texlive-delimtxt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-delimtxt 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-delimtxt
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-delimtxt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/delimtxt/delimtxt.pdf
%{_texmfdistdir}/doc/latex/delimtxt/resulta.dat
%{_texmfdistdir}/doc/latex/delimtxt/resultb.dat
%{_texmfdistdir}/doc/latex/delimtxt/resultc.dat
%{_texmfdistdir}/doc/latex/delimtxt/test1.tex
%{_texmfdistdir}/doc/latex/delimtxt/test2.tex
%{_texmfdistdir}/doc/latex/delimtxt/test3.tex

%files -n texlive-delimtxt
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/delimtxt/delimtxt.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-delimtxt-%{texlive_version}.%{texlive_noarch}.svn16549-%{release}-zypper
%endif

%package -n texlive-denisbdoc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn54584
Release:        0
Summary:        A personal dirty package for documenting packages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-denisbdoc-doc >= %{texlive_version}
Provides:       tex(denisbdoc.sty)
Requires:       tex(accsupp.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(attachfile2.sty)
Requires:       tex(babel.sty)
Requires:       tex(biblatex.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(cmap.sty)
Requires:       tex(comment.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(datetime.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(expl3.sty)
Requires:       tex(fixfoot.sty)
Requires:       tex(fontawesome.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(glossaries-extra.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hypcap.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iflang.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(imakeidx.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(lscape.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(morewrites.sty)
Requires:       tex(mparhack.sty)
Requires:       tex(multirow.sty)
Requires:       tex(mweights.sty)
Requires:       tex(nameref.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(parskip.sty)
Requires:       tex(path.sty)
Requires:       tex(pdflscape.sty)
Requires:       tex(refcount.sty)
Requires:       tex(rotating.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(textcase.sty)
Requires:       tex(tikz.sty)
Requires:       tex(tocbibind.sty)
Requires:       tex(tocvsec2.sty)
Requires:       tex(translator.sty)
Requires:       tex(varioref.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xpatch.sty)
Requires:       tex(xspace.sty)
Requires:       tex(zref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source112:      denisbdoc.tar.xz
Source113:      denisbdoc.doc.tar.xz

%description -n texlive-denisbdoc
A personal dirty package for documenting packages.

%package -n texlive-denisbdoc-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn54584
Release:        0
Summary:        Documentation for texlive-denisbdoc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-denisbdoc-doc
This package includes the documentation for texlive-denisbdoc

%post -n texlive-denisbdoc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-denisbdoc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-denisbdoc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-denisbdoc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/denisbdoc/README.md
%{_texmfdistdir}/doc/latex/denisbdoc/denisbdoc-chng.xdy
%{_texmfdistdir}/doc/latex/denisbdoc/denisbdoc.xdy

%files -n texlive-denisbdoc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/denisbdoc/denisbdoc.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-denisbdoc-%{texlive_version}.%{texlive_noarch}.0.0.8svn54584-%{release}-zypper
%endif

%package -n texlive-derivative
Version:        %{texlive_version}.%{texlive_noarch}.0.0.97svn53654
Release:        0
Summary:        Nice and easy derivatives
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-derivative-doc >= %{texlive_version}
Provides:       tex(derivative.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source114:      derivative.tar.xz
Source115:      derivative.doc.tar.xz

%description -n texlive-derivative
This package provides a set of commands \NewOdvVariant,
\NewPdvVariant etc. that can be used to define derivatives.
Each derivative comes with a great number of options that tweak
the derivative's format to your liking. The following types of
derivatives come readily defined: \odv Ordinary derivative,
\pdv Partial derivative, \fdv Functional derivative, \mdv
Material derivative, \adv Average rate of change, \jdv
Jacobian.

%package -n texlive-derivative-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.97svn53654
Release:        0
Summary:        Documentation for texlive-derivative
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-derivative-doc
This package includes the documentation for texlive-derivative

%post -n texlive-derivative
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-derivative 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-derivative
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-derivative-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/derivative/README.md
%{_texmfdistdir}/doc/latex/derivative/derivative.pdf
%{_texmfdistdir}/doc/latex/derivative/derivative.tex

%files -n texlive-derivative
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/derivative/derivative.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-derivative-%{texlive_version}.%{texlive_noarch}.0.0.97svn53654-%{release}-zypper
%endif

%package -n texlive-detex
Version:        %{texlive_version}.%{texlive_noarch}.svn54512
Release:        0
Summary:        Strip TeX from a source file
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-detex-bin >= %{texlive_version}
#!BuildIgnore: texlive-detex-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       man(detex.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source116:      detex.doc.tar.xz

%description -n texlive-detex
Detex is a program to remove TeX constructs from a text file.
It recognizes the \input command. The program assumes it is
dealing with LaTeX input if it sees the string \begin{document}
in the text. In this case, it also recognizes the \include and
\includeonly commands. The author now considers this program to
be "retired" and Piotr Kubowicz's OpenDetex as its successor.
%post -n texlive-detex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-detex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-detex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-detex
%defattr(-,root,root,755)
%{_mandir}/man1/detex.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-detex-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif

%package -n texlive-dhua
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn24035
Release:        0
Summary:        German abbreviations using thin space
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dhua-doc >= %{texlive_version}
Provides:       tex(dhua.cfg)
Provides:       tex(dhua.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source117:      dhua.tar.xz
Source118:      dhua.doc.tar.xz

%description -n texlive-dhua
The package provides commands for those abbreviations of German
phrases for which the use of thin space is recommended. Setup
commands \newdhua and \newtwopartdhua are provided, as well as
commands for single cases (such as \zB for 'z. B.', saving the
user from typing such as 'z.\,B.'). To typeset the
documentation, the niceverb package, version 0.44, or later, is
required. Das Paket `dhua' stellt Befehle fur sog.
mehrgliedrige Abkurzungen bereit, fur die schmale Leerzeichen
(Festabstande) empfohlen werden (Duden, Wikipedia). In die
englische Paketdokumentation sind deutsche Erlauterungen
eingestreut.

%package -n texlive-dhua-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn24035
Release:        0
Summary:        Documentation for texlive-dhua
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dhua-doc
This package includes the documentation for texlive-dhua

%post -n texlive-dhua
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dhua 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dhua
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dhua-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dhua/README
%{_texmfdistdir}/doc/latex/dhua/README.pdf
%{_texmfdistdir}/doc/latex/dhua/SrcFILEs.txt
%{_texmfdistdir}/doc/latex/dhua/dhua.pdf

%files -n texlive-dhua
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dhua/dhua.cfg
%{_texmfdistdir}/tex/latex/dhua/dhua.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dhua-%{texlive_version}.%{texlive_noarch}.0.0.11svn24035-%{release}-zypper
%endif

%package -n texlive-diadia
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn37656
Release:        0
Summary:        Package to keep a diabetes diary
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-diadia-bin >= %{texlive_version}
#!BuildIgnore: texlive-diadia-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-diadia-doc >= %{texlive_version}
Provides:       tex(diadia.cfg)
Provides:       tex(diadia.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(colortbl.sty)
Requires:       tex(environ.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(multicol.sty)
Requires:       tex(pgfcalendar.sty)
Requires:       tex(pgfplots.sty)
Requires:       tex(pgfplotstable.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(tcolorbox.sty)
Requires:       tex(translations.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source119:      diadia.tar.xz
Source120:      diadia.doc.tar.xz

%description -n texlive-diadia
The diadia package allows you to keep a diabetes diary.
Usually, this means keeping record of certain medical values
like blood sugar, blood pressure, pulse or weight. It might
also include other medical, pharmaceutical or nutritional data
(HbA1c, insulin doses, carbohydrate units). The diadia package
supports all of this plus more - simply by adding more columns
to the data file! It is able to evaluate the data file and
typesets formatted tables and derived plots. Furthermore, it
supports medication charts and info boxes. Supported languages:
English, German. Feel free to provide other translation files!

%package -n texlive-diadia-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn37656
Release:        0
Summary:        Documentation for texlive-diadia
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-diadia-doc
This package includes the documentation for texlive-diadia

%post -n texlive-diadia
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-diadia 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-diadia
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-diadia-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/diadia/201502.dat
%{_texmfdistdir}/doc/latex/diadia/201503.dat
%{_texmfdistdir}/doc/latex/diadia/201504.dat
%{_texmfdistdir}/doc/latex/diadia/README
%{_texmfdistdir}/doc/latex/diadia/ddbsl1avg.dat
%{_texmfdistdir}/doc/latex/diadia/diadia-example.pdf
%{_texmfdistdir}/doc/latex/diadia/diadia-example.tex
%{_texmfdistdir}/doc/latex/diadia/diadia.dat
%{_texmfdistdir}/doc/latex/diadia/diadia.dtx
%{_texmfdistdir}/doc/latex/diadia/diadia.pdf
%{_texmfdistdir}/doc/latex/diadia/hba1c.dat
%{_texmfdistdir}/doc/latex/diadia/makefile
%{_texmfdistdir}/doc/latex/diadia/manifest.txt

%files -n texlive-diadia
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/diadia/diadia.lua
%{_texmfdistdir}/tex/latex/diadia/diadia-english.trsl
%{_texmfdistdir}/tex/latex/diadia/diadia-fallback.trsl
%{_texmfdistdir}/tex/latex/diadia/diadia-german.trsl
%{_texmfdistdir}/tex/latex/diadia/diadia.cfg
%{_texmfdistdir}/tex/latex/diadia/diadia.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-diadia-%{texlive_version}.%{texlive_noarch}.1.1svn37656-%{release}-zypper
%endif

%package -n texlive-diagbox
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn54080
Release:        0
Summary:        Table heads with diagonal lines
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-diagbox-doc >= %{texlive_version}
Provides:       tex(diagbox.sty)
Requires:       tex(array.sty)
Requires:       tex(calc.sty)
Requires:       tex(fp.sty)
Requires:       tex(keyval.sty)
Requires:       tex(pict2e.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source121:      diagbox.tar.xz
Source122:      diagbox.doc.tar.xz

%description -n texlive-diagbox
The package's principal command, \diagbox, takes two arguments
(texts for the slash-separated parts of the box), and an
optional argument with which the direction the slash will go,
the box dimensions, etc., may be controlled. The package also
provides \slashbox and \backslashbox commands for compatibility
with the slashbox package, which it supersedes. diagbox depends
on e-TeX as well as the packages array, calc, fp, keyval, and
pict2e.

%package -n texlive-diagbox-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn54080
Release:        0
Summary:        Documentation for texlive-diagbox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-diagbox-doc
This package includes the documentation for texlive-diagbox

%post -n texlive-diagbox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-diagbox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-diagbox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-diagbox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/diagbox/README
%{_texmfdistdir}/doc/latex/diagbox/diagbox.pdf

%files -n texlive-diagbox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/diagbox/diagbox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-diagbox-%{texlive_version}.%{texlive_noarch}.2.4svn54080-%{release}-zypper
%endif

%package -n texlive-diagmac2
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn15878
Release:        0
Summary:        Diagram macros, using pict2e
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-diagmac2-doc >= %{texlive_version}
Provides:       tex(diagmac2.sty)
Requires:       tex(pict2e.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source123:      diagmac2.tar.xz
Source124:      diagmac2.doc.tar.xz

%description -n texlive-diagmac2
This is a development of the long-established diagmac package,
using pict2e so that the restrictions on line direction are
removed.

%package -n texlive-diagmac2-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn15878
Release:        0
Summary:        Documentation for texlive-diagmac2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-diagmac2-doc
This package includes the documentation for texlive-diagmac2

%post -n texlive-diagmac2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-diagmac2 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-diagmac2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-diagmac2-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/diagmac2/README
%{_texmfdistdir}/doc/latex/diagmac2/doc/diagmac2.pdf
%{_texmfdistdir}/doc/latex/diagmac2/doc/diagmac2.tex
%{_texmfdistdir}/doc/latex/diagmac2/doc/diagmactest.pdf
%{_texmfdistdir}/doc/latex/diagmac2/doc/diagmactest.tex

%files -n texlive-diagmac2
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/diagmac2/diagmac2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-diagmac2-%{texlive_version}.%{texlive_noarch}.2.1svn15878-%{release}-zypper
%endif

%package -n texlive-diagnose
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn19387
Release:        0
Summary:        A diagnostic tool for a TeX installation
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
Recommends:     texlive-diagnose-doc >= %{texlive_version}
Provides:       tex(diagnose.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source125:      diagnose.tar.xz
Source126:      diagnose.doc.tar.xz

%description -n texlive-diagnose
Provides macros to assist evaluation of the capabilities of a
TeX installation (i.e., what extensions it supports). An
example document that examines the installation is available.

%package -n texlive-diagnose-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn19387
Release:        0
Summary:        Documentation for texlive-diagnose
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-diagnose-doc
This package includes the documentation for texlive-diagnose

%post -n texlive-diagnose
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-diagnose 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-diagnose
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-diagnose-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/diagnose/INSTALL
%{_texmfdistdir}/doc/latex/diagnose/README
%{_texmfdistdir}/doc/latex/diagnose/diagnose.pdf
%{_texmfdistdir}/doc/latex/diagnose/diagnose.tex
%{_texmfdistdir}/doc/latex/diagnose/mls-diag.tex

%files -n texlive-diagnose
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/diagnose/diagnose.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-diagnose-%{texlive_version}.%{texlive_noarch}.0.0.2svn19387-%{release}-zypper
%endif

%package -n texlive-dialogl
Version:        %{texlive_version}.%{texlive_noarch}.svn28946
Release:        0
Summary:        Macros for constructing interactive LaTeX scripts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dialogl-doc >= %{texlive_version}
Provides:       tex(dialog.sty)
Provides:       tex(grabhedr.sty)
Provides:       tex(listout.tex)
Provides:       tex(menus.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source127:      dialogl.tar.xz
Source128:      dialogl.doc.tar.xz

%description -n texlive-dialogl
Gathers together a bunch of code and examples about how to
write macros to carry on a dialogue with the user.

%package -n texlive-dialogl-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn28946
Release:        0
Summary:        Documentation for texlive-dialogl
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dialogl-doc
This package includes the documentation for texlive-dialogl

%post -n texlive-dialogl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dialogl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dialogl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dialogl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dialogl/Makefile
%{_texmfdistdir}/doc/latex/dialogl/README
%{_texmfdistdir}/doc/latex/dialogl/cnvunits.tex
%{_texmfdistdir}/doc/latex/dialogl/codialog.pdf
%{_texmfdistdir}/doc/latex/dialogl/default.los
%{_texmfdistdir}/doc/latex/dialogl/dia-driv.pdf
%{_texmfdistdir}/doc/latex/dialogl/dia-driv.tex
%{_texmfdistdir}/doc/latex/dialogl/dialogl-doc.sty
%{_texmfdistdir}/doc/latex/dialogl/diatest.tex
%{_texmfdistdir}/doc/latex/dialogl/fontmenu.lg
%{_texmfdistdir}/doc/latex/dialogl/fontmenu.tex
%{_texmfdistdir}/doc/latex/dialogl/manifest.txt

%files -n texlive-dialogl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dialogl/dialog.sty
%{_texmfdistdir}/tex/latex/dialogl/grabhedr.sty
%{_texmfdistdir}/tex/latex/dialogl/listout.tex
%{_texmfdistdir}/tex/latex/dialogl/menus.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dialogl-%{texlive_version}.%{texlive_noarch}.svn28946-%{release}-zypper
%endif

%package -n texlive-dice
Version:        %{texlive_version}.%{texlive_noarch}.svn28501
Release:        0
Summary:        A font for die faces
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dice-doc >= %{texlive_version}
Provides:       tex(dice3d.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source129:      dice.tar.xz
Source130:      dice.doc.tar.xz

%description -n texlive-dice
A Metafont font that can produce die faces in 2D or with
various 3D effects.

%package -n texlive-dice-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn28501
Release:        0
Summary:        Documentation for texlive-dice
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dice-doc
This package includes the documentation for texlive-dice

%post -n texlive-dice
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dice 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dice
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dice-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dice/dice3d.tex

%files -n texlive-dice
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/dice/dice3d.mf
%{_texmfdistdir}/fonts/tfm/public/dice/dice3d.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dice-%{texlive_version}.%{texlive_noarch}.svn28501-%{release}-zypper
%endif

%package -n texlive-dichokey
Version:        %{texlive_version}.%{texlive_noarch}.svn17192
Release:        0
Summary:        Construct dichotomous identification keys
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
Recommends:     texlive-dichokey-doc >= %{texlive_version}
Provides:       tex(dichokey.sty)
Requires:       tex(calc.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source131:      dichokey.tar.xz
Source132:      dichokey.doc.tar.xz

%description -n texlive-dichokey
The package can be used to construct dichotomous identification
keys (used especially in biology for species identification),
taking care of numbering and indentation of successive key
steps automatically. An example file is provided, which
demonstrates usage.

%package -n texlive-dichokey-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17192
Release:        0
Summary:        Documentation for texlive-dichokey
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dichokey-doc
This package includes the documentation for texlive-dichokey

%post -n texlive-dichokey
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dichokey 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dichokey
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dichokey-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dichokey/dichokey.pdf
%{_texmfdistdir}/doc/latex/dichokey/dichokey.tex
%{_texmfdistdir}/doc/latex/dichokey/rhodocyb.pdf
%{_texmfdistdir}/doc/latex/dichokey/rhodocyb.tex

%files -n texlive-dichokey
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dichokey/dichokey.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dichokey-%{texlive_version}.%{texlive_noarch}.svn17192-%{release}-zypper
%endif

%package -n texlive-dickimaw
Version:        %{texlive_version}.%{texlive_noarch}.svn32925
Release:        0
Summary:        Books and tutorials from the "Dickimaw LaTeX Series"
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
Source133:      dickimaw.doc.tar.xz

%description -n texlive-dickimaw
The package provides some of the books and tutorials that form
part of the "Dickimaw LaTeX Series". Only the A4 PDF of each
book is detailed here. Other formats, such as HTML or screen
optimized PDF, are available from the package home page. Books
included are: "LaTeX for Complete Novices": an introductory
guide to LaTeX. "Using LaTeX to Write a PhD Thesis": a
follow-on from "LaTeX for Complete Novices" geared towards
students who want to use LaTeX to write their PhD thesis.
"Creating a LaTeX minimal example": describes how to create a
minimal example, which can be used as a debugging aid when you
encounter errors in your LaTeX documents.
%post -n texlive-dickimaw
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dickimaw 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dickimaw
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dickimaw
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dickimaw/ERRATA
%{_texmfdistdir}/doc/latex/dickimaw/README
%{_texmfdistdir}/doc/latex/dickimaw/dickimaw-minexample.pdf
%{_texmfdistdir}/doc/latex/dickimaw/dickimaw-novices.pdf
%{_texmfdistdir}/doc/latex/dickimaw/dickimaw-thesis.pdf
%{_texmfdistdir}/doc/latex/dickimaw/src/fdl.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/minexample/dickimaw-minexample.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/minexample/minexample.sty
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/dickimaw-novices.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/glsentries.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/keywords.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices-a4paper.sty
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices-index.ist
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices.bib
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/novices.cls
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/acrobat.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/backtic.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/circle.pdf
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom3.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom4.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom5.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom6.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/cmdprom7.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dinglist.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer3.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/dirviewer4.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/draftimage.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/entersymbol.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/errormessage.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/exsamp.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/incgraph.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/incgraph2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/letterbox.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/maths.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/miktex1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/newdoc-1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/newdoc-2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/notepad1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/notepad2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/rectangle.pdf
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/reflbox.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/resizbox.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/rotbox.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/scalbox.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/shapes.pdf
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/tds.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal-texdoc.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal10.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal11.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal3.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal4.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal5.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal6.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal7.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal8.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/terminal9.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-latexmk.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-preferences.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig3.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks-toolconfig4.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks3.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks4.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks5-annote.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks5.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks6.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks7.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks8.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/texworks9.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/pictures/yap1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/argument.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/auxiliary.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/cls.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/command.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/declaration.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/dvi.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/environment.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/fragile.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/group.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/hyphenation.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/intersentencespacing.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/introduction.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/length.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/mandatory.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/optional.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/output.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/perl.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/preamble.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/robust.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/short.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/source.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/terminal.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/novices/term-defs/tex.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/dickimaw-thesis.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/dickimawthesis.cls
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/glsentries.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/imgsource/titlepage.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/listing-samples/helloworld.c
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/listing-samples/sqrt.c
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/arara-installer.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/bibertool.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/doibutton.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/generatekey.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-dataprop-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-dataprop.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-pref-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-pref.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport1-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport2-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport3-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref-textimport3.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref1-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref1.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref10-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref10.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref11.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref12-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref12.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref3-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref3.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref4-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref4.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref5-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref5.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref6-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref6.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref7-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref7.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref8-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref8.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref9-thumbnail.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/jabref9.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/pagestyle.tex
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-addbutton.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-arara.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-arara2.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-bibtex.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-latexmk.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-latexmkbibtex.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-makeglossaries.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-pdflatex.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-pref.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/texworks-texindy.png
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/pictures/titlepage.pdf
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/thesis-a4paper.sty
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/thesis-index.ist
%{_texmfdistdir}/doc/latex/dickimaw/src/thesis/thesis.bib
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dickimaw-%{texlive_version}.%{texlive_noarch}.svn32925-%{release}-zypper
%endif

%package -n texlive-dictsym
Version:        %{texlive_version}.%{texlive_noarch}.svn20031
Release:        0
Summary:        DictSym font and macro package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
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
Requires:       texlive-dictsym-fonts >= %{texlive_version}
Recommends:     texlive-dictsym-doc >= %{texlive_version}
Provides:       tex(dictsym.map)
Provides:       tex(dictsym.sty)
Provides:       tex(dictsym.tfm)
Requires:       tex(keyval.sty)
Requires:       tex(pifont.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source134:      dictsym.tar.xz
Source135:      dictsym.doc.tar.xz

%description -n texlive-dictsym
This directory contains the DictSym Type1 font designed by
Georg Verweyen and all files required to use it with LaTeX on
the Unix or PC platforms. The font provides a number of symbols
commonly used in dictionaries. The accompanying macro package
makes the symbols accessible as LaTeX commands.

%package -n texlive-dictsym-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20031
Release:        0
Summary:        Documentation for texlive-dictsym
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dictsym-doc
This package includes the documentation for texlive-dictsym


%package -n texlive-dictsym-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn20031
Release:        0
Summary:        Severed fonts for texlive-dictsym
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-dictsym-fonts
The  separated fonts package for texlive-dictsym
%post -n texlive-dictsym
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap dictsym.map' >> /var/run/texlive/run-updmap

%postun -n texlive-dictsym 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap dictsym.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-dictsym
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-dictsym-fonts
%files -n texlive-dictsym-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dictsym/README
%{_texmfdistdir}/doc/fonts/dictsym/dictsym.pdf
%{_texmfdistdir}/doc/fonts/dictsym/dictsym.tex

%files -n texlive-dictsym
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/dictsym/dictsym.afm
%{_texmfdistdir}/fonts/map/dvips/dictsym/dictsym.map
%{_texmfdistdir}/fonts/tfm/public/dictsym/dictsym.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dictsym/dictsym.pfb
%{_texmfdistdir}/fonts/type1/public/dictsym/dictsym.pfm
%{_texmfdistdir}/tex/latex/dictsym/dictsym.sty

%files -n texlive-dictsym-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-dictsym
%{_datadir}/fontconfig/conf.avail/58-texlive-dictsym.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dictsym/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dictsym/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dictsym/fonts.scale
%{_datadir}/fonts/texlive-dictsym/dictsym.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dictsym-fonts-%{texlive_version}.%{texlive_noarch}.svn20031-%{release}-zypper
%endif

%package -n texlive-diffcoeff
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn53244
Release:        0
Summary:        Write differential coefficients easily and consistently
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-diffcoeff-doc >= %{texlive_version}
Provides:       tex(diffcoeff-doc.def)
Provides:       tex(diffcoeff.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xtemplate.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source136:      diffcoeff.tar.xz
Source137:      diffcoeff.doc.tar.xz

%description -n texlive-diffcoeff
diffcoeff.sty allows the easy and consistent writing of
ordinary, partial and other derivatives of arbitrary (algebraic
or numeric) order. For mixed partial derivatives, the total
order of differentiation is calculated by the package. Optional
arguments allow specification of points of evaluation (ordinary
derivatives), or variables held constant (partial derivatives),
and the placement of the differentiand (numerator or appended).
The package is built on xtemplate, allowing systematic
fine-tuning of the display and generation and use of variant
forms (like derivatives built from D, \Delta or \delta). A
command for differentials ensures the dx used in e.g. integrals
is consistent with the form used in derivatives. The package
requires the LaTeX3 bundles l3kernel and l3packages.

%package -n texlive-diffcoeff-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn53244
Release:        0
Summary:        Documentation for texlive-diffcoeff
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-diffcoeff-doc
This package includes the documentation for texlive-diffcoeff

%post -n texlive-diffcoeff
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-diffcoeff 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-diffcoeff
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-diffcoeff-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/diffcoeff/README.txt
%{_texmfdistdir}/doc/latex/diffcoeff/diffcoeff.pdf
%{_texmfdistdir}/doc/latex/diffcoeff/diffcoeff.tex

%files -n texlive-diffcoeff
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/diffcoeff/diffcoeff-doc.def
%{_texmfdistdir}/tex/latex/diffcoeff/diffcoeff.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-diffcoeff-%{texlive_version}.%{texlive_noarch}.3.2svn53244-%{release}-zypper
%endif

%package -n texlive-digiconfigs
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn15878
Release:        0
Summary:        Writing "configurations"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-digiconfigs-doc >= %{texlive_version}
Provides:       tex(digiconfigs.sty)
Requires:       tex(amsmath.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source138:      digiconfigs.tar.xz
Source139:      digiconfigs.doc.tar.xz

%description -n texlive-digiconfigs
In Stochastic Geometry and Digital Image Analysis some problems
can be solved in terms of so-called "configurations". A
configuration is basically a square matrix of \circ and \bullet
symbols. This package provides a convenient and compact
mechanism for displaying these configurations.

%package -n texlive-digiconfigs-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn15878
Release:        0
Summary:        Documentation for texlive-digiconfigs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-digiconfigs-doc
This package includes the documentation for texlive-digiconfigs

%post -n texlive-digiconfigs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-digiconfigs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-digiconfigs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-digiconfigs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/digiconfigs/README
%{_texmfdistdir}/doc/latex/digiconfigs/digiconfigs.pdf
%{_texmfdistdir}/doc/latex/digiconfigs/digiconfigs.tex

%files -n texlive-digiconfigs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/digiconfigs/digiconfigs.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-digiconfigs-%{texlive_version}.%{texlive_noarch}.0.0.5svn15878-%{release}-zypper
%endif

%package -n texlive-dijkstra
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn45256
Release:        0
Summary:        Dijkstra algorithm for LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dijkstra-doc >= %{texlive_version}
Provides:       tex(dijkstra.sty)
Requires:       tex(simplekv.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source140:      dijkstra.tar.xz
Source141:      dijkstra.doc.tar.xz

%description -n texlive-dijkstra
This small package uses the Dijkstra algorithm for weighted
graphs,directed or not: the search table of the shortest path
can be displayed, the minimum distance between two vertices and
the corresponding path are stored in macros. This packages
depends on simplekv.

%package -n texlive-dijkstra-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.11svn45256
Release:        0
Summary:        Documentation for texlive-dijkstra
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-dijkstra-doc:fr)

%description -n texlive-dijkstra-doc
This package includes the documentation for texlive-dijkstra

%post -n texlive-dijkstra
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dijkstra 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dijkstra
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dijkstra-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dijkstra/README
%{_texmfdistdir}/doc/latex/dijkstra/dijkstra-fr.pdf
%{_texmfdistdir}/doc/latex/dijkstra/dijkstra-fr.tex

%files -n texlive-dijkstra
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dijkstra/dijkstra.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dijkstra-%{texlive_version}.%{texlive_noarch}.0.0.11svn45256-%{release}-zypper
%endif

%package -n texlive-din1505
Version:        %{texlive_version}.%{texlive_noarch}.svn19441
Release:        0
Summary:        Bibliography styles for German texts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-din1505-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source142:      din1505.tar.xz
Source143:      din1505.doc.tar.xz

%description -n texlive-din1505
A set of bibliography styles that conformt to DIN 1505, and
match the original BibTeX standard set (plain, unsrt, alpha and
abbrv), together with a style natdin to work with natbib.

%package -n texlive-din1505-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn19441
Release:        0
Summary:        Documentation for texlive-din1505
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-din1505-doc
This package includes the documentation for texlive-din1505

%post -n texlive-din1505
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-din1505 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-din1505
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-din1505-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/din1505/README.TEXLIVE
%{_texmfdistdir}/doc/latex/din1505/leitbild.bib
%{_texmfdistdir}/doc/latex/din1505/natbib.cfg

%files -n texlive-din1505
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/din1505/abbrvdin.bst
%{_texmfdistdir}/bibtex/bst/din1505/alphadin.bst
%{_texmfdistdir}/bibtex/bst/din1505/natdin.bst
%{_texmfdistdir}/bibtex/bst/din1505/plaindin.bst
%{_texmfdistdir}/bibtex/bst/din1505/unsrtdin.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-din1505-%{texlive_version}.%{texlive_noarch}.svn19441-%{release}-zypper
%endif

%package -n texlive-dinat
Version:        %{texlive_version}.%{texlive_noarch}.2.5svn15878
Release:        0
Summary:        Bibliography style for German texts
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
Recommends:     texlive-dinat-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source144:      dinat.tar.xz
Source145:      dinat.doc.tar.xz

%description -n texlive-dinat
Bibliography style files intended for texts in german. They
draw up bibliographies in accordance with the german DIN 1505,
parts 2 and 3.

%package -n texlive-dinat-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.5svn15878
Release:        0
Summary:        Documentation for texlive-dinat
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-dinat-doc:de)

%description -n texlive-dinat-doc
This package includes the documentation for texlive-dinat

%post -n texlive-dinat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dinat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dinat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dinat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/dinat/dinat-index.html
%{_texmfdistdir}/doc/bibtex/dinat/history.html

%files -n texlive-dinat
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/dinat/dinat.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dinat-%{texlive_version}.%{texlive_noarch}.2.5svn15878-%{release}-zypper
%endif

%package -n texlive-dinbrief
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        German letter DIN style
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dinbrief-doc >= %{texlive_version}
Provides:       tex(dinbrief.cfg)
Provides:       tex(dinbrief.cls)
Provides:       tex(dinbrief.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source146:      dinbrief.tar.xz
Source147:      dinbrief.doc.tar.xz

%description -n texlive-dinbrief
Implements a document layout for writing letters according to
the rules of DIN (Deutsches Institut fur Normung, German
standardisation institute). A style file for LaTeX 2.09 (with
limited support of the features) is part of the package. Since
the letter layout is based on a German standard, the user guide
is written in German, but most macros have English names from
which the user can recognize what they are used for. In
addition there are example files showing how letters may be
created with the package. A graphical interface for use of the
dinbrief is provided in the dinbrief-GUI bundle.

%package -n texlive-dinbrief-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-dinbrief
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-dinbrief-doc:de;en)

%description -n texlive-dinbrief-doc
This package includes the documentation for texlive-dinbrief

%post -n texlive-dinbrief
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dinbrief 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dinbrief
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dinbrief-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dinbrief/brfbody.tex
%{_texmfdistdir}/doc/latex/dinbrief/brfkopf.tex
%{_texmfdistdir}/doc/latex/dinbrief/dbold.tex
%{_texmfdistdir}/doc/latex/dinbrief/dinbrief.pdf
%{_texmfdistdir}/doc/latex/dinbrief/dinbrief.tex
%{_texmfdistdir}/doc/latex/dinbrief/dintab.tex
%{_texmfdistdir}/doc/latex/dinbrief/example.tex
%{_texmfdistdir}/doc/latex/dinbrief/liesmich
%{_texmfdistdir}/doc/latex/dinbrief/readme
%{_texmfdistdir}/doc/latex/dinbrief/test10.tex
%{_texmfdistdir}/doc/latex/dinbrief/test11.tex
%{_texmfdistdir}/doc/latex/dinbrief/test12.tex
%{_texmfdistdir}/doc/latex/dinbrief/testnorm.tex

%files -n texlive-dinbrief
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dinbrief/dinbrief.cfg
%{_texmfdistdir}/tex/latex/dinbrief/dinbrief.cls
%{_texmfdistdir}/tex/latex/dinbrief/dinbrief.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dinbrief-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-dingbat
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn27918
Release:        0
Summary:        Two dingbat symbol fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dingbat-doc >= %{texlive_version}
Provides:       tex(ark10.tfm)
Provides:       tex(dingbat.sty)
Provides:       tex(dingbat.tfm)
Provides:       tex(uark.fd)
Provides:       tex(udingbat.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source148:      dingbat.tar.xz
Source149:      dingbat.doc.tar.xz

%description -n texlive-dingbat
The fonts (ark10 and dingbat) are specified in Metafont;
support macros are provided for use in LaTeX. An Adobe Type 1
version of the fonts is available in the niceframe fonts
bundle.

%package -n texlive-dingbat-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn27918
Release:        0
Summary:        Documentation for texlive-dingbat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dingbat-doc
This package includes the documentation for texlive-dingbat

%post -n texlive-dingbat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dingbat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dingbat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dingbat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dingbat/README
%{_texmfdistdir}/doc/fonts/dingbat/dingbat.pdf
%{_texmfdistdir}/doc/fonts/dingbat/dingbat.tex

%files -n texlive-dingbat
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/dingbat/ark10.mf
%{_texmfdistdir}/fonts/source/public/dingbat/dingbat.mf
%{_texmfdistdir}/fonts/tfm/public/dingbat/ark10.tfm
%{_texmfdistdir}/fonts/tfm/public/dingbat/dingbat.tfm
%{_texmfdistdir}/tex/latex/dingbat/dingbat.sty
%{_texmfdistdir}/tex/latex/dingbat/uark.fd
%{_texmfdistdir}/tex/latex/dingbat/udingbat.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dingbat-%{texlive_version}.%{texlive_noarch}.1.0svn27918-%{release}-zypper
%endif

%package -n texlive-directory
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn15878
Release:        0
Summary:        An address book using BibTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-directory-doc >= %{texlive_version}
Provides:       tex(directory.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source150:      directory.tar.xz
Source151:      directory.doc.tar.xz

%description -n texlive-directory
A package for LaTeX and BibTeX that facilitates the
construction, maintenance and exploitation of an address
book-like database.

%package -n texlive-directory-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn15878
Release:        0
Summary:        Documentation for texlive-directory
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-directory-doc
This package includes the documentation for texlive-directory

%post -n texlive-directory
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-directory 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-directory
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-directory-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/directory/README
%{_texmfdistdir}/doc/latex/directory/directory.pdf
%{_texmfdistdir}/doc/latex/directory/directory.tex

%files -n texlive-directory
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/directory/business.bib
%{_texmfdistdir}/bibtex/bib/directory/family.bib
%{_texmfdistdir}/bibtex/bst/directory/address-html.bst
%{_texmfdistdir}/bibtex/bst/directory/address-ldif.bst
%{_texmfdistdir}/bibtex/bst/directory/address-vcard.bst
%{_texmfdistdir}/bibtex/bst/directory/address.bst
%{_texmfdistdir}/bibtex/bst/directory/birthday.bst
%{_texmfdistdir}/bibtex/bst/directory/email-html.bst
%{_texmfdistdir}/bibtex/bst/directory/email.bst
%{_texmfdistdir}/bibtex/bst/directory/letter.bst
%{_texmfdistdir}/bibtex/bst/directory/phone.bst
%{_texmfdistdir}/tex/latex/directory/directory.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-directory-%{texlive_version}.%{texlive_noarch}.1.20svn15878-%{release}-zypper
%endif

%package -n texlive-dirtree
Version:        %{texlive_version}.%{texlive_noarch}.0.0.32svn42428
Release:        0
Summary:        Display trees in the style of windows explorer
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dirtree-doc >= %{texlive_version}
Provides:       tex(dirtree.sty)
Provides:       tex(dirtree.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source152:      dirtree.tar.xz
Source153:      dirtree.doc.tar.xz

%description -n texlive-dirtree
This package is designed to emulate the way windows explorer
displays directory and file trees, with the root at top left,
and each level of subtree displaying one step in to the right.
The macros work equally well with Plain TeX and with LaTeX.

%package -n texlive-dirtree-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.32svn42428
Release:        0
Summary:        Documentation for texlive-dirtree
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dirtree-doc
This package includes the documentation for texlive-dirtree

%post -n texlive-dirtree
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dirtree 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dirtree
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dirtree-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/dirtree/README
%{_texmfdistdir}/doc/generic/dirtree/dirtree.pdf

%files -n texlive-dirtree
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/dirtree/dirtree.sty
%{_texmfdistdir}/tex/generic/dirtree/dirtree.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dirtree-%{texlive_version}.%{texlive_noarch}.0.0.32svn42428-%{release}-zypper
%endif

%package -n texlive-dirtytalk
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20520
Release:        0
Summary:        A package to typeset quotations easier
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
Recommends:     texlive-dirtytalk-doc >= %{texlive_version}
Provides:       tex(dirtytalk.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source154:      dirtytalk.tar.xz
Source155:      dirtytalk.doc.tar.xz

%description -n texlive-dirtytalk
The package provides a macro to typeset quotations, using the
command \say{stuff}. The quotation mark glyphs are inserted by
the macro; nested quotations are detected.

%package -n texlive-dirtytalk-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn20520
Release:        0
Summary:        Documentation for texlive-dirtytalk
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dirtytalk-doc
This package includes the documentation for texlive-dirtytalk

%post -n texlive-dirtytalk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dirtytalk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dirtytalk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dirtytalk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dirtytalk/README
%{_texmfdistdir}/doc/latex/dirtytalk/dirtytalk.pdf

%files -n texlive-dirtytalk
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dirtytalk/dirtytalk.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dirtytalk-%{texlive_version}.%{texlive_noarch}.1.0svn20520-%{release}-zypper
%endif

%package -n texlive-disser
Version:        %{texlive_version}.%{texlive_noarch}.1.5.0svn43417
Release:        0
Summary:        Class and templates for typesetting dissertations in Russian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-disser-doc >= %{texlive_version}
Provides:       tex(autoref.rtx)
Provides:       tex(bachelor.rtx)
Provides:       tex(candidate.rtx)
Provides:       tex(disser.cls)
Provides:       tex(doctor.rtx)
Provides:       tex(gost732.cls)
Provides:       tex(master.rtx)
Provides:       tex(specialist.rtx)
Provides:       tex(titledefs.rtx)
Requires:       tex(caption.sty)
Requires:       tex(cmap.sty)
Requires:       tex(color.sty)
Requires:       tex(exscale.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(natbib.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(textcase.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source156:      disser.tar.xz
Source157:      disser.doc.tar.xz

%description -n texlive-disser
Disser comprises a document class and set of templates for
typesetting dissertations in Russian. One of its primary
advantages is a simplicity of format specification for
titlepage, headers and elements of automatically generated
lists (table of contents, list of figures, etc). Bibliography
styles, that conform to the requirements of the Russian
standard GOST R 7.0.11-2011, are provided.

%package -n texlive-disser-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5.0svn43417
Release:        0
Summary:        Documentation for texlive-disser
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-disser-doc:ru;en)

%description -n texlive-disser-doc
This package includes the documentation for texlive-disser

%post -n texlive-disser
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-disser 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-disser
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-disser-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/disser/ChangeLog
%{_texmfdistdir}/doc/latex/disser/Makefile
%{_texmfdistdir}/doc/latex/disser/README-ru.md
%{_texmfdistdir}/doc/latex/disser/README.md
%{_texmfdistdir}/doc/latex/disser/include/latex.fig.mk
%{_texmfdistdir}/doc/latex/disser/include/latex.fig.nmk.cmd
%{_texmfdistdir}/doc/latex/disser/include/latex.mk
%{_texmfdistdir}/doc/latex/disser/include/latex.nmk.cmd
%{_texmfdistdir}/doc/latex/disser/manual.tex
%{_texmfdistdir}/doc/latex/disser/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/1.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/a.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/fig/fig.eps
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates-utf8/bachelor/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/1.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/a.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/autoref.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/common.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/dict.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/fig/facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/fig/sec-facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/review.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates-utf8/candidate/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/1.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/a.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/autoref.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/common.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/dict.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/fig/facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/fig/sec-facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/review.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates-utf8/doctor/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/1.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/a.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates-utf8/master/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/1.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/a.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/fig/fig.eps
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates-utf8/specialist/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/1.tex
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/a.tex
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/fig/fig.eps
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates/bachelor/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/1.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/candidate/a.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/autoref.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/common.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/dict.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/candidate/fig/sec-facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates/candidate/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/candidate/review.tex
%{_texmfdistdir}/doc/latex/disser/templates/candidate/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates/candidate/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/1.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/doctor/a.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/autoref.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/common.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/dict.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/doctor/fig/sec-facsimile.eps
%{_texmfdistdir}/doc/latex/disser/templates/doctor/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/doctor/review.tex
%{_texmfdistdir}/doc/latex/disser/templates/doctor/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates/doctor/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates/master/1.tex
%{_texmfdistdir}/doc/latex/disser/templates/master/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/master/a.tex
%{_texmfdistdir}/doc/latex/disser/templates/master/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates/master/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/master/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/master/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates/master/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/master/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates/master/thesis.tex
%{_texmfdistdir}/doc/latex/disser/templates/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/specialist/1.tex
%{_texmfdistdir}/doc/latex/disser/templates/specialist/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/specialist/a.tex
%{_texmfdistdir}/doc/latex/disser/templates/specialist/concl.tex
%{_texmfdistdir}/doc/latex/disser/templates/specialist/fig/Makefile
%{_texmfdistdir}/doc/latex/disser/templates/specialist/fig/fig.eps
%{_texmfdistdir}/doc/latex/disser/templates/specialist/fig/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/specialist/intro.tex
%{_texmfdistdir}/doc/latex/disser/templates/specialist/nomake.cmd
%{_texmfdistdir}/doc/latex/disser/templates/specialist/thesis.bib
%{_texmfdistdir}/doc/latex/disser/templates/specialist/thesis.tex

%files -n texlive-disser
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/disser/dtx.ist
%{_texmfdistdir}/tex/latex/disser/autoref.rtx
%{_texmfdistdir}/tex/latex/disser/bachelor.rtx
%{_texmfdistdir}/tex/latex/disser/candidate.rtx
%{_texmfdistdir}/tex/latex/disser/disser.cls
%{_texmfdistdir}/tex/latex/disser/doctor.rtx
%{_texmfdistdir}/tex/latex/disser/gost732.cls
%{_texmfdistdir}/tex/latex/disser/master.rtx
%{_texmfdistdir}/tex/latex/disser/specialist.rtx
%{_texmfdistdir}/tex/latex/disser/titledefs.rtx
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-disser-%{texlive_version}.%{texlive_noarch}.1.5.0svn43417-%{release}-zypper
%endif

%package -n texlive-ditaa
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn48932
Release:        0
Summary:        Use ditaa diagrams within LaTeX documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ditaa-doc >= %{texlive_version}
Provides:       tex(ditaa.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source158:      ditaa.tar.xz
Source159:      ditaa.doc.tar.xz

%description -n texlive-ditaa
With this package ditaa (DIagrams Through Ascii Art) diagrams
can be embedded directly into LaTeX files.

%package -n texlive-ditaa-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn48932
Release:        0
Summary:        Documentation for texlive-ditaa
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ditaa-doc
This package includes the documentation for texlive-ditaa

%post -n texlive-ditaa
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ditaa 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ditaa
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ditaa-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ditaa/README
%{_texmfdistdir}/doc/latex/ditaa/ditaa.pdf
%{_texmfdistdir}/doc/latex/ditaa/ditaa.tex
%{_texmfdistdir}/doc/latex/ditaa/example.tex
%{_texmfdistdir}/doc/latex/ditaa/resources/ditaa/ditaaexample.ditaa
%{_texmfdistdir}/doc/latex/ditaa/resources/ditaa/ditaaexample.png
%{_texmfdistdir}/doc/latex/ditaa/resources/ditaa/ditaaexample2.ditaa
%{_texmfdistdir}/doc/latex/ditaa/resources/ditaa/ditaaexample2.png

%files -n texlive-ditaa
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ditaa/ditaa.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ditaa-%{texlive_version}.%{texlive_noarch}.0.0.9svn48932-%{release}-zypper
%endif

%package -n texlive-dithesis
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn34295
Release:        0
Summary:        A class for undergraduate theses at the University of Athens
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dithesis-doc >= %{texlive_version}
Provides:       tex(dithesis.cls)
Requires:       tex(article.cls)
Requires:       tex(fancyhdr.sty)
Requires:       tex(float.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(parskip.sty)
Requires:       tex(setspace.sty)
Requires:       tex(subfig.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(titletoc.sty)
Requires:       tex(titling.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(xifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source160:      dithesis.tar.xz
Source161:      dithesis.doc.tar.xz

%description -n texlive-dithesis
The class conforms to the requirements of the Department of
Informatics and Telecommunications at the University of Athens
regarding the preparation of undergraduate theses, as of Sep 1,
2011. The class is designed for use with XeLaTeX; by default
(on a Windows platform), the font Arial is used, but provision
is made for use under Linux (with a different sans-serif font).

%package -n texlive-dithesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn34295
Release:        0
Summary:        Documentation for texlive-dithesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dithesis-doc
This package includes the documentation for texlive-dithesis

%post -n texlive-dithesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dithesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dithesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dithesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dithesis/README
%{_texmfdistdir}/doc/latex/dithesis/athena.jpg
%{_texmfdistdir}/doc/latex/dithesis/sample.pdf
%{_texmfdistdir}/doc/latex/dithesis/sample.tex
%{_texmfdistdir}/doc/latex/dithesis/sampleNoArial.pdf
%{_texmfdistdir}/doc/latex/dithesis/sampleNoArial.tex

%files -n texlive-dithesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dithesis/dithesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dithesis-%{texlive_version}.%{texlive_noarch}.0.0.2svn34295-%{release}-zypper
%endif

%package -n texlive-dk-bib
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn15878
Release:        0
Summary:        Danish variants of standard BibTeX styles
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dk-bib-doc >= %{texlive_version}
Provides:       tex(dk-apali.sty)
Provides:       tex(dk-bib.sty)
Requires:       tex(url.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source162:      dk-bib.tar.xz
Source163:      dk-bib.doc.tar.xz

%description -n texlive-dk-bib
Dk-bib is a translation of the four standard BibTeX style files
(abbrv, alpha, plain and unsrt) and the apalike style file into
Danish. The files have been extended with URL, ISBN, ISSN,
annote and printing fields which can be enabled through a LaTeX
style file. Dk-bib also comes with a couple of Danish sorting
order files for BibTeX8.

%package -n texlive-dk-bib-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn15878
Release:        0
Summary:        Documentation for texlive-dk-bib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dk-bib-doc
This package includes the documentation for texlive-dk-bib

%post -n texlive-dk-bib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dk-bib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dk-bib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dk-bib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dk-bib/COPYRIGHT
%{_texmfdistdir}/doc/latex/dk-bib/README
%{_texmfdistdir}/doc/latex/dk-bib/dk-bib.ltx
%{_texmfdistdir}/doc/latex/dk-bib/dk-bib.pdf

%files -n texlive-dk-bib
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/dk-bib/litteratur.bib
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-abbrv.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-alpha.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-apali.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-plain.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-unsrt.bst
%{_texmfdistdir}/bibtex/csf/dk-bib/88591-dk.csf
%{_texmfdistdir}/bibtex/csf/dk-bib/cp850-dk.csf
%{_texmfdistdir}/bibtex/csf/dk-bib/mac-dk.csf
%{_texmfdistdir}/bibtex/csf/dk-bib/utf8-dk.csf
%{_texmfdistdir}/tex/latex/dk-bib/dk-apali.sty
%{_texmfdistdir}/tex/latex/dk-bib/dk-bib.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dk-bib-%{texlive_version}.%{texlive_noarch}.0.0.6svn15878-%{release}-zypper
%endif

%package -n texlive-dlfltxb
Version:        %{texlive_version}.%{texlive_noarch}.svn17337
Release:        0
Summary:        Macros related to "Introdktion til LaTeX"
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dlfltxb-doc >= %{texlive_version}
Provides:       tex(dlfltxbcodetips.sty)
Provides:       tex(dlfltxbmarkup.sty)
Provides:       tex(dlfltxbmarkupbookkeys.sty)
Provides:       tex(dlfltxbmisc.sty)
Provides:       tex(dlfltxbtocconfig.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(calc.sty)
Requires:       tex(chngpage.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source164:      dlfltxb.tar.xz
Source165:      dlfltxb.doc.tar.xz

%description -n texlive-dlfltxb
The bundle contains various macros either used for creating the
author's book "Introduktion til LaTeX" (in Danish), or
presented in the book as code tips. The bundle comprises:
dlfltxbcodetips: various macros helpful in typesetting
mathematics; dlfltxbmarkup: provides macros used throughout,
for registering macro names, packages etc. in the text, in the
margin and in the index, all by using categorised keys (note, a
configuration file may be used; a sample is included in the
distribution); dlfltxbtocconfig: macros for the two tables of
contents that the book has; dlfltxbmisc: various macros for
typesetting LaTeX arguments, and the macro used in the
bibliography that can wrap a URL up into a BibTeX entry.
Interested parties may review the book itself on the web at the
author's institution (it is written in Danish).

%package -n texlive-dlfltxb-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17337
Release:        0
Summary:        Documentation for texlive-dlfltxb
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dlfltxb-doc
This package includes the documentation for texlive-dlfltxb

%post -n texlive-dlfltxb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dlfltxb 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dlfltxb
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dlfltxb-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dlfltxb/README
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbbibtex.dbj
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbcodetips.pdf
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbcodetips.tex
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup-showkeys.pdf
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup-showkeys.tex
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup.pdf
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup.tex
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmisc.pdf
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmisc.tex
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbtocconfig.pdf
%{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbtocconfig.tex
%{_texmfdistdir}/doc/latex/dlfltxb/package_doc.bib

%files -n texlive-dlfltxb
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/dlfltxb/dlfltxbbibtex.bst
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbcodetips.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbmarkup.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbmarkupbookkeys.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbmisc.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbtocconfig.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dlfltxb-%{texlive_version}.%{texlive_noarch}.svn17337-%{release}-zypper
%endif

%package -n texlive-dnaseq
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn17194
Release:        0
Summary:        Format DNA base sequences
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dnaseq-doc >= %{texlive_version}
Provides:       tex(dnaseq.sty)
Requires:       tex(color.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source166:      dnaseq.tar.xz
Source167:      dnaseq.doc.tar.xz

%description -n texlive-dnaseq
Defines a means of specifying sequences of bases. The bases may
be numbered (per line) and you may specify that subsequences be
coloured. For a more 'vanilla-flavoured' way of typesetting
base sequences, the user might consider the seqsplit package.

%package -n texlive-dnaseq-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01svn17194
Release:        0
Summary:        Documentation for texlive-dnaseq
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dnaseq-doc
This package includes the documentation for texlive-dnaseq

%post -n texlive-dnaseq
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dnaseq 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dnaseq
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dnaseq-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dnaseq/DNAtest.tex
%{_texmfdistdir}/doc/latex/dnaseq/README
%{_texmfdistdir}/doc/latex/dnaseq/dnaseq.pdf

%files -n texlive-dnaseq
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dnaseq/dnaseq.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dnaseq-%{texlive_version}.%{texlive_noarch}.0.0.01svn17194-%{release}-zypper
%endif

%package -n texlive-dnp
Version:        %{texlive_version}.%{texlive_noarch}.svn54074
Release:        0
Summary:        Subfont numbers for DNP font encoding
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
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
Source168:      dnp.tar.xz

%description -n texlive-dnp
part of the CJK package, ctan.org/pkg/cjk
%post -n texlive-dnp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dnp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dnp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dnp
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/sfd/dnp/DNP.sfd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dnp-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif

%package -n texlive-doc-pictex
Version:        %{texlive_version}.%{texlive_noarch}.svn24927
Release:        0
Summary:        A summary list of PicTeX documentation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
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
Source169:      doc-pictex.doc.tar.xz

%description -n texlive-doc-pictex
A summary of available resources providing (or merely
discussing) documentation of PicTeX.
%post -n texlive-doc-pictex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-doc-pictex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-doc-pictex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-doc-pictex
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/doc-pictex/Doc-PiCTeX.txt
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-doc-pictex-%{texlive_version}.%{texlive_noarch}.svn24927-%{release}-zypper
%endif

%package -n texlive-docbytex
Version:        %{texlive_version}.%{texlive_noarch}.svn34294
Release:        0
Summary:        Creating documentation from source code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-docbytex-doc >= %{texlive_version}
Provides:       tex(docby.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source170:      docbytex.tar.xz
Source171:      docbytex.doc.tar.xz

%description -n texlive-docbytex
The package creates documentation from C source code, or other
programming languages.

%package -n texlive-docbytex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn34294
Release:        0
Summary:        Documentation for texlive-docbytex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-docbytex-doc:cs)

%description -n texlive-docbytex-doc
This package includes the documentation for texlive-docbytex

%post -n texlive-docbytex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-docbytex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-docbytex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-docbytex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/docbytex/README
%{_texmfdistdir}/doc/generic/docbytex/annonce
%{_texmfdistdir}/doc/generic/docbytex/base.c
%{_texmfdistdir}/doc/generic/docbytex/base.d
%{_texmfdistdir}/doc/generic/docbytex/cosi.c
%{_texmfdistdir}/doc/generic/docbytex/docby-e.d
%{_texmfdistdir}/doc/generic/docbytex/docby-e.pdf
%{_texmfdistdir}/doc/generic/docbytex/docby.d
%{_texmfdistdir}/doc/generic/docbytex/docby.pdf
%{_texmfdistdir}/doc/generic/docbytex/lup.pdf
%{_texmfdistdir}/doc/generic/docbytex/lup.tex
%{_texmfdistdir}/doc/generic/docbytex/main.c
%{_texmfdistdir}/doc/generic/docbytex/main.d
%{_texmfdistdir}/doc/generic/docbytex/win.c
%{_texmfdistdir}/doc/generic/docbytex/win.d

%files -n texlive-docbytex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/docbytex/docby.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-docbytex-%{texlive_version}.%{texlive_noarch}.svn34294-%{release}-zypper
%endif

%package -n texlive-doclicense
Version:        %{texlive_version}.%{texlive_noarch}.1.10.1svn54758
Release:        0
Summary:        Support for putting documents under a license
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-doclicense-doc >= %{texlive_version}
Provides:       tex(doclicense-CC-by-3.0-latex.tex)
Provides:       tex(doclicense-CC-by-3.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-4.0-latex.tex)
Provides:       tex(doclicense-CC-by-4.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nc-3.0-latex.tex)
Provides:       tex(doclicense-CC-by-nc-3.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nc-4.0-latex.tex)
Provides:       tex(doclicense-CC-by-nc-4.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nc-nd-3.0-latex.tex)
Provides:       tex(doclicense-CC-by-nc-nd-3.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nc-nd-4.0-latex.tex)
Provides:       tex(doclicense-CC-by-nc-nd-4.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nc-sa-3.0-latex.tex)
Provides:       tex(doclicense-CC-by-nc-sa-3.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nc-sa-4.0-latex.tex)
Provides:       tex(doclicense-CC-by-nc-sa-4.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nd-3.0-latex.tex)
Provides:       tex(doclicense-CC-by-nd-3.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-nd-4.0-latex.tex)
Provides:       tex(doclicense-CC-by-nd-4.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-sa-3.0-latex.tex)
Provides:       tex(doclicense-CC-by-sa-3.0-plaintext.tex)
Provides:       tex(doclicense-CC-by-sa-4.0-latex.tex)
Provides:       tex(doclicense-CC-by-sa-4.0-plaintext.tex)
Provides:       tex(doclicense-CC-zero-1.0-latex.tex)
Provides:       tex(doclicense-CC-zero-1.0-plaintext.tex)
Provides:       tex(doclicense-UKenglish.ldf)
Provides:       tex(doclicense-USenglish.ldf)
Provides:       tex(doclicense-acadian.ldf)
Provides:       tex(doclicense-american.ldf)
Provides:       tex(doclicense-australian.ldf)
Provides:       tex(doclicense-brazilian.ldf)
Provides:       tex(doclicense-british.ldf)
Provides:       tex(doclicense-canadian.ldf)
Provides:       tex(doclicense-canadien.ldf)
Provides:       tex(doclicense-catalan.ldf)
Provides:       tex(doclicense-chinese-gbk.ldf)
Provides:       tex(doclicense-chinese-utf8.ldf)
Provides:       tex(doclicense-english.ldf)
Provides:       tex(doclicense-french.ldf)
Provides:       tex(doclicense-galician.ldf)
Provides:       tex(doclicense-german.ldf)
Provides:       tex(doclicense-italian.ldf)
Provides:       tex(doclicense-newzealand.ldf)
Provides:       tex(doclicense-ngerman.ldf)
Provides:       tex(doclicense-polish.ldf)
Provides:       tex(doclicense-portuguese.ldf)
Provides:       tex(doclicense-russian.ldf)
Provides:       tex(doclicense-spanish.ldf)
Provides:       tex(doclicense.sty)
Requires:       tex(ccicons.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(verbatim.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source172:      doclicense.tar.xz
Source173:      doclicense.doc.tar.xz

%description -n texlive-doclicense
This package allows you to put your document under a license
and include a link to read about the license or include an icon
or image of the license. Currently, only Creative Commons is
supported, but this package is designed to handle all kinds of
licenses.

%package -n texlive-doclicense-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.10.1svn54758
Release:        0
Summary:        Documentation for texlive-doclicense
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-doclicense-doc
This package includes the documentation for texlive-doclicense

%post -n texlive-doclicense
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-doclicense 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-doclicense
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-doclicense-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/doclicense/README
%{_texmfdistdir}/doc/latex/doclicense/doclicense.pdf

%files -n texlive-doclicense
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/doclicense/doclicense-UKenglish.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-USenglish.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-acadian.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-american.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-australian.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-brazilian.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-british.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-canadian.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-canadien.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-catalan.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-chinese-gbk.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-chinese-utf8.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-english.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-french.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-galician.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-german.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-italian.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-newzealand.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-ngerman.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-polish.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-portuguese.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-russian.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense-spanish.ldf
%{_texmfdistdir}/tex/latex/doclicense/doclicense.sty
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-nc-eu.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-nc-nd-eu.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-nc-nd.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-nc-sa-eu.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-nc-sa.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-nc.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-nd.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by-sa.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-by.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-pd.pdf
%{_texmfdistdir}/tex/latex/doclicense/images/doclicense-CC-zero.pdf
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-3.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-3.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-4.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-4.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-3.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-3.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-4.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-4.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-nd-3.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-nd-3.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-nd-4.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-nd-4.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-sa-3.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-sa-3.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-sa-4.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nc-sa-4.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nd-3.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nd-3.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nd-4.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-nd-4.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-sa-3.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-sa-3.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-sa-4.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-by-sa-4.0-plaintext.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-zero-1.0-latex.tex
%{_texmfdistdir}/tex/latex/doclicense/license-texts/doclicense-CC-zero-1.0-plaintext.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-doclicense-%{texlive_version}.%{texlive_noarch}.1.10.1svn54758-%{release}-zypper
%endif

%package -n texlive-docmfp
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn15878
Release:        0
Summary:        Document non-LaTeX code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-docmfp-doc >= %{texlive_version}
Provides:       tex(docmfp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source174:      docmfp.tar.xz
Source175:      docmfp.doc.tar.xz

%description -n texlive-docmfp
Extends the doc package to cater for documenting non-LaTeX
code, such as Metafont or MetaPost, or other programming
languages.

%package -n texlive-docmfp-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2dsvn15878
Release:        0
Summary:        Documentation for texlive-docmfp
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-docmfp-doc
This package includes the documentation for texlive-docmfp

%post -n texlive-docmfp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-docmfp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-docmfp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-docmfp-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/docmfp/README
%{_texmfdistdir}/doc/latex/docmfp/docmfp.pdf

%files -n texlive-docmfp
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/docmfp/docmfp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-docmfp-%{texlive_version}.%{texlive_noarch}.1.2dsvn15878-%{release}-zypper
%endif

%package -n texlive-docmute
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn25741
Release:        0
Summary:        Input files ignoring LaTeX preamble, etcetera
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-docmute-doc >= %{texlive_version}
Provides:       tex(docmute.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source176:      docmute.tar.xz
Source177:      docmute.doc.tar.xz

%description -n texlive-docmute
Input or include stand-alone LaTeX documents, ignoring
everything but the material between \begin{document} and
\end{document}.

%package -n texlive-docmute-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn25741
Release:        0
Summary:        Documentation for texlive-docmute
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-docmute-doc
This package includes the documentation for texlive-docmute

%post -n texlive-docmute
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-docmute 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-docmute
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-docmute-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/docmute/README
%{_texmfdistdir}/doc/latex/docmute/docmute.pdf

%files -n texlive-docmute
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/docmute/docmute.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-docmute-%{texlive_version}.%{texlive_noarch}.1.4svn25741-%{release}-zypper
%endif

%package -n texlive-docsurvey
Version:        %{texlive_version}.%{texlive_noarch}.svn48931
Release:        0
Summary:        A survey of LaTeX documentation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
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
Source178:      docsurvey.doc.tar.xz

%description -n texlive-docsurvey
A survey of programming-related documentation for LaTeX.
Included are references to printed and electronic books and
manuals, symbol lists, FAQs, the LaTeX source code, CTAN and
distributions, programming-related packages, users groups and
online communities, and information on creating packages and
documentation.
%post -n texlive-docsurvey
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-docsurvey 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-docsurvey
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-docsurvey
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/docsurvey/README.txt
%{_texmfdistdir}/doc/latex/docsurvey/docsurvey.pdf
%{_texmfdistdir}/doc/latex/docsurvey/docsurvey.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-docsurvey-%{texlive_version}.%{texlive_noarch}.svn48931-%{release}-zypper
%endif

%package -n texlive-doctools
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn34474
Release:        0
Summary:        Tools for the documentation of LaTeX code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-doctools-doc >= %{texlive_version}
Provides:       tex(doctools.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(cmap.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(kvoptions-patch.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(listings.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xspace.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source179:      doctools.tar.xz
Source180:      doctools.doc.tar.xz

%description -n texlive-doctools
The package provides a collection of tools for use either in an
"ordinary" LaTeX document, or within a .dtx file.

%package -n texlive-doctools-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn34474
Release:        0
Summary:        Documentation for texlive-doctools
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-doctools-doc
This package includes the documentation for texlive-doctools

%post -n texlive-doctools
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-doctools 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-doctools
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-doctools-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/doctools/README
%{_texmfdistdir}/doc/latex/doctools/doctools.pdf

%files -n texlive-doctools
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/doctools/doctools.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-doctools-%{texlive_version}.%{texlive_noarch}.0.0.1svn34474-%{release}-zypper
%endif

%package -n texlive-documentation
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn34521
Release:        0
Summary:        Documentation support for C, Java and assembler code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-documentation-doc >= %{texlive_version}
Provides:       tex(documentation.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source181:      documentation.tar.xz
Source182:      documentation.doc.tar.xz

%description -n texlive-documentation
The package provides a simple means of typesetting computer
programs such that the result is acceptable for inclusion in
reports, etc.

%package -n texlive-documentation-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn34521
Release:        0
Summary:        Documentation for texlive-documentation
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-documentation-doc
This package includes the documentation for texlive-documentation

%post -n texlive-documentation
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-documentation 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-documentation
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-documentation-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/documentation/README
%{_texmfdistdir}/doc/latex/documentation/documentation.pdf

%files -n texlive-documentation
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/documentation/documentation.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-documentation-%{texlive_version}.%{texlive_noarch}.0.0.1svn34521-%{release}-zypper
%endif

%package -n texlive-doi
Version:        %{texlive_version}.%{texlive_noarch}.svn48634
Release:        0
Summary:        Create correct hyperlinks for DOI numbers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-doi-doc >= %{texlive_version}
Provides:       tex(doi.sty)
Requires:       tex(hyperref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source183:      doi.tar.xz
Source184:      doi.doc.tar.xz

%description -n texlive-doi
You can hyperlink DOI numbers to doi.org. However, some
publishers have elected to use nasty characters in their DOI
numbering scheme ('<', '>', '_' and ';' have all been spotted).
This will either upset (La)TeX, or your PDF reader. This
package contains a single user-level command \doi{}, which
takes a DOI number, and creates a correct hyperlink to the
target of the DOI.

%package -n texlive-doi-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn48634
Release:        0
Summary:        Documentation for texlive-doi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-doi-doc
This package includes the documentation for texlive-doi

%post -n texlive-doi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-doi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-doi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-doi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/doi/README.md

%files -n texlive-doi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/doi/doi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-doi-%{texlive_version}.%{texlive_noarch}.svn48634-%{release}-zypper
%endif

%package -n texlive-doipubmed
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Special commands for use in bibliographies
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-doipubmed-doc >= %{texlive_version}
Provides:       tex(doipubmed.sty)
Requires:       tex(url.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source185:      doipubmed.tar.xz
Source186:      doipubmed.doc.tar.xz

%description -n texlive-doipubmed
The package provides the commands \doi, \pubmed and \citeurl.
These commands are primarily designed for use in
bibliographies. A LaTeX2HTML style file is also provided.

%package -n texlive-doipubmed-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn15878
Release:        0
Summary:        Documentation for texlive-doipubmed
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-doipubmed-doc
This package includes the documentation for texlive-doipubmed

%post -n texlive-doipubmed
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-doipubmed 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-doipubmed
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-doipubmed-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/doipubmed/CHANGES
%{_texmfdistdir}/doc/latex/doipubmed/README
%{_texmfdistdir}/doc/latex/doipubmed/doipubmed-manual.html
%{_texmfdistdir}/doc/latex/doipubmed/doipubmed.pdf
%{_texmfdistdir}/doc/latex/doipubmed/doipubmed.perl

%files -n texlive-doipubmed
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/doipubmed/doipubmed.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-doipubmed-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif

%package -n texlive-domitian
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn54512
Release:        0
Summary:        Drop-in replacement for Palatino
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
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
Requires:       texlive-domitian-fonts >= %{texlive_version}
Recommends:     texlive-domitian-doc >= %{texlive_version}
Provides:       tex(Domitian-Bold-inf-lgr--base.tfm)
Provides:       tex(Domitian-Bold-inf-lgr.tfm)
Provides:       tex(Domitian-Bold-inf-lgr.vf)
Provides:       tex(Domitian-Bold-inf-ly1--base.tfm)
Provides:       tex(Domitian-Bold-inf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-inf-ly1.tfm)
Provides:       tex(Domitian-Bold-inf-ly1.vf)
Provides:       tex(Domitian-Bold-inf-ot1--base.tfm)
Provides:       tex(Domitian-Bold-inf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-inf-ot1.tfm)
Provides:       tex(Domitian-Bold-inf-ot1.vf)
Provides:       tex(Domitian-Bold-inf-t1--base.tfm)
Provides:       tex(Domitian-Bold-inf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-inf-t1.tfm)
Provides:       tex(Domitian-Bold-inf-t1.vf)
Provides:       tex(Domitian-Bold-inf-t2a--base.tfm)
Provides:       tex(Domitian-Bold-inf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Bold-inf-t2a.tfm)
Provides:       tex(Domitian-Bold-inf-t2a.vf)
Provides:       tex(Domitian-Bold-inf-t2b--base.tfm)
Provides:       tex(Domitian-Bold-inf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Bold-inf-t2b.tfm)
Provides:       tex(Domitian-Bold-inf-t2b.vf)
Provides:       tex(Domitian-Bold-inf-t2c--base.tfm)
Provides:       tex(Domitian-Bold-inf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Bold-inf-t2c.tfm)
Provides:       tex(Domitian-Bold-inf-t2c.vf)
Provides:       tex(Domitian-Bold-sup-lgr--base.tfm)
Provides:       tex(Domitian-Bold-sup-lgr.tfm)
Provides:       tex(Domitian-Bold-sup-lgr.vf)
Provides:       tex(Domitian-Bold-sup-ly1--base.tfm)
Provides:       tex(Domitian-Bold-sup-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-sup-ly1.tfm)
Provides:       tex(Domitian-Bold-sup-ly1.vf)
Provides:       tex(Domitian-Bold-sup-ot1--base.tfm)
Provides:       tex(Domitian-Bold-sup-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-sup-ot1.tfm)
Provides:       tex(Domitian-Bold-sup-ot1.vf)
Provides:       tex(Domitian-Bold-sup-t1--base.tfm)
Provides:       tex(Domitian-Bold-sup-t1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-sup-t1.tfm)
Provides:       tex(Domitian-Bold-sup-t1.vf)
Provides:       tex(Domitian-Bold-sup-t2a--base.tfm)
Provides:       tex(Domitian-Bold-sup-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Bold-sup-t2a.tfm)
Provides:       tex(Domitian-Bold-sup-t2a.vf)
Provides:       tex(Domitian-Bold-sup-t2b--base.tfm)
Provides:       tex(Domitian-Bold-sup-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Bold-sup-t2b.tfm)
Provides:       tex(Domitian-Bold-sup-t2b.vf)
Provides:       tex(Domitian-Bold-sup-t2c--base.tfm)
Provides:       tex(Domitian-Bold-sup-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Bold-sup-t2c.tfm)
Provides:       tex(Domitian-Bold-sup-t2c.vf)
Provides:       tex(Domitian-Bold-tlf-lgr--base.tfm)
Provides:       tex(Domitian-Bold-tlf-lgr.tfm)
Provides:       tex(Domitian-Bold-tlf-lgr.vf)
Provides:       tex(Domitian-Bold-tlf-ly1--base.tfm)
Provides:       tex(Domitian-Bold-tlf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tlf-ly1.tfm)
Provides:       tex(Domitian-Bold-tlf-ly1.vf)
Provides:       tex(Domitian-Bold-tlf-ot1--base.tfm)
Provides:       tex(Domitian-Bold-tlf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tlf-ot1.tfm)
Provides:       tex(Domitian-Bold-tlf-ot1.vf)
Provides:       tex(Domitian-Bold-tlf-t1--base.tfm)
Provides:       tex(Domitian-Bold-tlf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tlf-t1.tfm)
Provides:       tex(Domitian-Bold-tlf-t1.vf)
Provides:       tex(Domitian-Bold-tlf-t2a--base.tfm)
Provides:       tex(Domitian-Bold-tlf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tlf-t2a.tfm)
Provides:       tex(Domitian-Bold-tlf-t2a.vf)
Provides:       tex(Domitian-Bold-tlf-t2b--base.tfm)
Provides:       tex(Domitian-Bold-tlf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tlf-t2b.tfm)
Provides:       tex(Domitian-Bold-tlf-t2b.vf)
Provides:       tex(Domitian-Bold-tlf-t2c--base.tfm)
Provides:       tex(Domitian-Bold-tlf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tlf-t2c.tfm)
Provides:       tex(Domitian-Bold-tlf-t2c.vf)
Provides:       tex(Domitian-Bold-tlf-ts1--base.tfm)
Provides:       tex(Domitian-Bold-tlf-ts1.tfm)
Provides:       tex(Domitian-Bold-tlf-ts1.vf)
Provides:       tex(Domitian-Bold-tosf-lgr--base.tfm)
Provides:       tex(Domitian-Bold-tosf-lgr.tfm)
Provides:       tex(Domitian-Bold-tosf-lgr.vf)
Provides:       tex(Domitian-Bold-tosf-ly1--base.tfm)
Provides:       tex(Domitian-Bold-tosf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tosf-ly1.tfm)
Provides:       tex(Domitian-Bold-tosf-ly1.vf)
Provides:       tex(Domitian-Bold-tosf-ot1--base.tfm)
Provides:       tex(Domitian-Bold-tosf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tosf-ot1.tfm)
Provides:       tex(Domitian-Bold-tosf-ot1.vf)
Provides:       tex(Domitian-Bold-tosf-t1--base.tfm)
Provides:       tex(Domitian-Bold-tosf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tosf-t1.tfm)
Provides:       tex(Domitian-Bold-tosf-t1.vf)
Provides:       tex(Domitian-Bold-tosf-t2a--base.tfm)
Provides:       tex(Domitian-Bold-tosf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tosf-t2a.tfm)
Provides:       tex(Domitian-Bold-tosf-t2a.vf)
Provides:       tex(Domitian-Bold-tosf-t2b--base.tfm)
Provides:       tex(Domitian-Bold-tosf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tosf-t2b.tfm)
Provides:       tex(Domitian-Bold-tosf-t2b.vf)
Provides:       tex(Domitian-Bold-tosf-t2c--base.tfm)
Provides:       tex(Domitian-Bold-tosf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Bold-tosf-t2c.tfm)
Provides:       tex(Domitian-Bold-tosf-t2c.vf)
Provides:       tex(Domitian-Bold-tosf-ts1--base.tfm)
Provides:       tex(Domitian-Bold-tosf-ts1.tfm)
Provides:       tex(Domitian-Bold-tosf-ts1.vf)
Provides:       tex(Domitian-BoldItalic-inf-lgr--base.tfm)
Provides:       tex(Domitian-BoldItalic-inf-lgr.tfm)
Provides:       tex(Domitian-BoldItalic-inf-lgr.vf)
Provides:       tex(Domitian-BoldItalic-inf-ly1--base.tfm)
Provides:       tex(Domitian-BoldItalic-inf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-inf-ly1.tfm)
Provides:       tex(Domitian-BoldItalic-inf-ly1.vf)
Provides:       tex(Domitian-BoldItalic-inf-ot1--base.tfm)
Provides:       tex(Domitian-BoldItalic-inf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-inf-ot1.tfm)
Provides:       tex(Domitian-BoldItalic-inf-ot1.vf)
Provides:       tex(Domitian-BoldItalic-inf-t1--base.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t1.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t1.vf)
Provides:       tex(Domitian-BoldItalic-inf-t2a--base.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2a.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2a.vf)
Provides:       tex(Domitian-BoldItalic-inf-t2b--base.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2b.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2b.vf)
Provides:       tex(Domitian-BoldItalic-inf-t2c--base.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2c.tfm)
Provides:       tex(Domitian-BoldItalic-inf-t2c.vf)
Provides:       tex(Domitian-BoldItalic-sup-lgr--base.tfm)
Provides:       tex(Domitian-BoldItalic-sup-lgr.tfm)
Provides:       tex(Domitian-BoldItalic-sup-lgr.vf)
Provides:       tex(Domitian-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(Domitian-BoldItalic-sup-ly1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-sup-ly1.tfm)
Provides:       tex(Domitian-BoldItalic-sup-ly1.vf)
Provides:       tex(Domitian-BoldItalic-sup-ot1--base.tfm)
Provides:       tex(Domitian-BoldItalic-sup-ot1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-sup-ot1.tfm)
Provides:       tex(Domitian-BoldItalic-sup-ot1.vf)
Provides:       tex(Domitian-BoldItalic-sup-t1--base.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t1.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t1.vf)
Provides:       tex(Domitian-BoldItalic-sup-t2a--base.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2a--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2a.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2a.vf)
Provides:       tex(Domitian-BoldItalic-sup-t2b--base.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2b--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2b.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2b.vf)
Provides:       tex(Domitian-BoldItalic-sup-t2c--base.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2c--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2c.tfm)
Provides:       tex(Domitian-BoldItalic-sup-t2c.vf)
Provides:       tex(Domitian-BoldItalic-tlf-lgr--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-lgr.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-lgr.vf)
Provides:       tex(Domitian-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ly1.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ly1.vf)
Provides:       tex(Domitian-BoldItalic-tlf-ot1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ot1.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ot1.vf)
Provides:       tex(Domitian-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t1.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t1.vf)
Provides:       tex(Domitian-BoldItalic-tlf-t2a--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2a.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2a.vf)
Provides:       tex(Domitian-BoldItalic-tlf-t2b--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2b.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2b.vf)
Provides:       tex(Domitian-BoldItalic-tlf-t2c--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2c.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-t2c.vf)
Provides:       tex(Domitian-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ts1.tfm)
Provides:       tex(Domitian-BoldItalic-tlf-ts1.vf)
Provides:       tex(Domitian-BoldItalic-tosf-lgr--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-lgr.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-lgr.vf)
Provides:       tex(Domitian-BoldItalic-tosf-ly1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ly1.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ly1.vf)
Provides:       tex(Domitian-BoldItalic-tosf-ot1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ot1.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ot1.vf)
Provides:       tex(Domitian-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t1--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t1.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t1.vf)
Provides:       tex(Domitian-BoldItalic-tosf-t2a--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2a.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2a.vf)
Provides:       tex(Domitian-BoldItalic-tosf-t2b--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2b.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2b.vf)
Provides:       tex(Domitian-BoldItalic-tosf-t2c--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2c.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-t2c.vf)
Provides:       tex(Domitian-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ts1.tfm)
Provides:       tex(Domitian-BoldItalic-tosf-ts1.vf)
Provides:       tex(Domitian-Italic-inf-lgr--base.tfm)
Provides:       tex(Domitian-Italic-inf-lgr.tfm)
Provides:       tex(Domitian-Italic-inf-lgr.vf)
Provides:       tex(Domitian-Italic-inf-ly1--base.tfm)
Provides:       tex(Domitian-Italic-inf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-inf-ly1.tfm)
Provides:       tex(Domitian-Italic-inf-ly1.vf)
Provides:       tex(Domitian-Italic-inf-ot1--base.tfm)
Provides:       tex(Domitian-Italic-inf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-inf-ot1.tfm)
Provides:       tex(Domitian-Italic-inf-ot1.vf)
Provides:       tex(Domitian-Italic-inf-t1--base.tfm)
Provides:       tex(Domitian-Italic-inf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-inf-t1.tfm)
Provides:       tex(Domitian-Italic-inf-t1.vf)
Provides:       tex(Domitian-Italic-inf-t2a--base.tfm)
Provides:       tex(Domitian-Italic-inf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Italic-inf-t2a.tfm)
Provides:       tex(Domitian-Italic-inf-t2a.vf)
Provides:       tex(Domitian-Italic-inf-t2b--base.tfm)
Provides:       tex(Domitian-Italic-inf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Italic-inf-t2b.tfm)
Provides:       tex(Domitian-Italic-inf-t2b.vf)
Provides:       tex(Domitian-Italic-inf-t2c--base.tfm)
Provides:       tex(Domitian-Italic-inf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Italic-inf-t2c.tfm)
Provides:       tex(Domitian-Italic-inf-t2c.vf)
Provides:       tex(Domitian-Italic-sup-lgr--base.tfm)
Provides:       tex(Domitian-Italic-sup-lgr.tfm)
Provides:       tex(Domitian-Italic-sup-lgr.vf)
Provides:       tex(Domitian-Italic-sup-ly1--base.tfm)
Provides:       tex(Domitian-Italic-sup-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-sup-ly1.tfm)
Provides:       tex(Domitian-Italic-sup-ly1.vf)
Provides:       tex(Domitian-Italic-sup-ot1--base.tfm)
Provides:       tex(Domitian-Italic-sup-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-sup-ot1.tfm)
Provides:       tex(Domitian-Italic-sup-ot1.vf)
Provides:       tex(Domitian-Italic-sup-t1--base.tfm)
Provides:       tex(Domitian-Italic-sup-t1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-sup-t1.tfm)
Provides:       tex(Domitian-Italic-sup-t1.vf)
Provides:       tex(Domitian-Italic-sup-t2a--base.tfm)
Provides:       tex(Domitian-Italic-sup-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Italic-sup-t2a.tfm)
Provides:       tex(Domitian-Italic-sup-t2a.vf)
Provides:       tex(Domitian-Italic-sup-t2b--base.tfm)
Provides:       tex(Domitian-Italic-sup-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Italic-sup-t2b.tfm)
Provides:       tex(Domitian-Italic-sup-t2b.vf)
Provides:       tex(Domitian-Italic-sup-t2c--base.tfm)
Provides:       tex(Domitian-Italic-sup-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Italic-sup-t2c.tfm)
Provides:       tex(Domitian-Italic-sup-t2c.vf)
Provides:       tex(Domitian-Italic-tlf-lgr--base.tfm)
Provides:       tex(Domitian-Italic-tlf-lgr.tfm)
Provides:       tex(Domitian-Italic-tlf-lgr.vf)
Provides:       tex(Domitian-Italic-tlf-ly1--base.tfm)
Provides:       tex(Domitian-Italic-tlf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tlf-ly1.tfm)
Provides:       tex(Domitian-Italic-tlf-ly1.vf)
Provides:       tex(Domitian-Italic-tlf-ot1--base.tfm)
Provides:       tex(Domitian-Italic-tlf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tlf-ot1.tfm)
Provides:       tex(Domitian-Italic-tlf-ot1.vf)
Provides:       tex(Domitian-Italic-tlf-t1--base.tfm)
Provides:       tex(Domitian-Italic-tlf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tlf-t1.tfm)
Provides:       tex(Domitian-Italic-tlf-t1.vf)
Provides:       tex(Domitian-Italic-tlf-t2a--base.tfm)
Provides:       tex(Domitian-Italic-tlf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tlf-t2a.tfm)
Provides:       tex(Domitian-Italic-tlf-t2a.vf)
Provides:       tex(Domitian-Italic-tlf-t2b--base.tfm)
Provides:       tex(Domitian-Italic-tlf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tlf-t2b.tfm)
Provides:       tex(Domitian-Italic-tlf-t2b.vf)
Provides:       tex(Domitian-Italic-tlf-t2c--base.tfm)
Provides:       tex(Domitian-Italic-tlf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tlf-t2c.tfm)
Provides:       tex(Domitian-Italic-tlf-t2c.vf)
Provides:       tex(Domitian-Italic-tlf-ts1--base.tfm)
Provides:       tex(Domitian-Italic-tlf-ts1.tfm)
Provides:       tex(Domitian-Italic-tlf-ts1.vf)
Provides:       tex(Domitian-Italic-tosf-lgr--base.tfm)
Provides:       tex(Domitian-Italic-tosf-lgr.tfm)
Provides:       tex(Domitian-Italic-tosf-lgr.vf)
Provides:       tex(Domitian-Italic-tosf-ly1--base.tfm)
Provides:       tex(Domitian-Italic-tosf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tosf-ly1.tfm)
Provides:       tex(Domitian-Italic-tosf-ly1.vf)
Provides:       tex(Domitian-Italic-tosf-ot1--base.tfm)
Provides:       tex(Domitian-Italic-tosf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tosf-ot1.tfm)
Provides:       tex(Domitian-Italic-tosf-ot1.vf)
Provides:       tex(Domitian-Italic-tosf-t1--base.tfm)
Provides:       tex(Domitian-Italic-tosf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tosf-t1.tfm)
Provides:       tex(Domitian-Italic-tosf-t1.vf)
Provides:       tex(Domitian-Italic-tosf-t2a--base.tfm)
Provides:       tex(Domitian-Italic-tosf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tosf-t2a.tfm)
Provides:       tex(Domitian-Italic-tosf-t2a.vf)
Provides:       tex(Domitian-Italic-tosf-t2b--base.tfm)
Provides:       tex(Domitian-Italic-tosf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tosf-t2b.tfm)
Provides:       tex(Domitian-Italic-tosf-t2b.vf)
Provides:       tex(Domitian-Italic-tosf-t2c--base.tfm)
Provides:       tex(Domitian-Italic-tosf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Italic-tosf-t2c.tfm)
Provides:       tex(Domitian-Italic-tosf-t2c.vf)
Provides:       tex(Domitian-Italic-tosf-ts1--base.tfm)
Provides:       tex(Domitian-Italic-tosf-ts1.tfm)
Provides:       tex(Domitian-Italic-tosf-ts1.vf)
Provides:       tex(Domitian-Roman-inf-lgr--base.tfm)
Provides:       tex(Domitian-Roman-inf-lgr.tfm)
Provides:       tex(Domitian-Roman-inf-lgr.vf)
Provides:       tex(Domitian-Roman-inf-ly1--base.tfm)
Provides:       tex(Domitian-Roman-inf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-inf-ly1.tfm)
Provides:       tex(Domitian-Roman-inf-ly1.vf)
Provides:       tex(Domitian-Roman-inf-ot1--base.tfm)
Provides:       tex(Domitian-Roman-inf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-inf-ot1.tfm)
Provides:       tex(Domitian-Roman-inf-ot1.vf)
Provides:       tex(Domitian-Roman-inf-t1--base.tfm)
Provides:       tex(Domitian-Roman-inf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-inf-t1.tfm)
Provides:       tex(Domitian-Roman-inf-t1.vf)
Provides:       tex(Domitian-Roman-inf-t2a--base.tfm)
Provides:       tex(Domitian-Roman-inf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Roman-inf-t2a.tfm)
Provides:       tex(Domitian-Roman-inf-t2a.vf)
Provides:       tex(Domitian-Roman-inf-t2b--base.tfm)
Provides:       tex(Domitian-Roman-inf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Roman-inf-t2b.tfm)
Provides:       tex(Domitian-Roman-inf-t2b.vf)
Provides:       tex(Domitian-Roman-inf-t2c--base.tfm)
Provides:       tex(Domitian-Roman-inf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Roman-inf-t2c.tfm)
Provides:       tex(Domitian-Roman-inf-t2c.vf)
Provides:       tex(Domitian-Roman-sup-lgr--base.tfm)
Provides:       tex(Domitian-Roman-sup-lgr.tfm)
Provides:       tex(Domitian-Roman-sup-lgr.vf)
Provides:       tex(Domitian-Roman-sup-ly1--base.tfm)
Provides:       tex(Domitian-Roman-sup-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-sup-ly1.tfm)
Provides:       tex(Domitian-Roman-sup-ly1.vf)
Provides:       tex(Domitian-Roman-sup-ot1--base.tfm)
Provides:       tex(Domitian-Roman-sup-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-sup-ot1.tfm)
Provides:       tex(Domitian-Roman-sup-ot1.vf)
Provides:       tex(Domitian-Roman-sup-t1--base.tfm)
Provides:       tex(Domitian-Roman-sup-t1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-sup-t1.tfm)
Provides:       tex(Domitian-Roman-sup-t1.vf)
Provides:       tex(Domitian-Roman-sup-t2a--base.tfm)
Provides:       tex(Domitian-Roman-sup-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Roman-sup-t2a.tfm)
Provides:       tex(Domitian-Roman-sup-t2a.vf)
Provides:       tex(Domitian-Roman-sup-t2b--base.tfm)
Provides:       tex(Domitian-Roman-sup-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Roman-sup-t2b.tfm)
Provides:       tex(Domitian-Roman-sup-t2b.vf)
Provides:       tex(Domitian-Roman-sup-t2c--base.tfm)
Provides:       tex(Domitian-Roman-sup-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Roman-sup-t2c.tfm)
Provides:       tex(Domitian-Roman-sup-t2c.vf)
Provides:       tex(Domitian-Roman-tlf-lgr--base.tfm)
Provides:       tex(Domitian-Roman-tlf-lgr.tfm)
Provides:       tex(Domitian-Roman-tlf-lgr.vf)
Provides:       tex(Domitian-Roman-tlf-ly1--base.tfm)
Provides:       tex(Domitian-Roman-tlf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-ly1.tfm)
Provides:       tex(Domitian-Roman-tlf-ly1.vf)
Provides:       tex(Domitian-Roman-tlf-ot1--base.tfm)
Provides:       tex(Domitian-Roman-tlf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-ot1.tfm)
Provides:       tex(Domitian-Roman-tlf-ot1.vf)
Provides:       tex(Domitian-Roman-tlf-sc-lgr--base.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-lgr.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-lgr.vf)
Provides:       tex(Domitian-Roman-tlf-sc-ly1--base.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-ly1.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-ly1.vf)
Provides:       tex(Domitian-Roman-tlf-sc-ot1--base.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-ot1.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-ot1.vf)
Provides:       tex(Domitian-Roman-tlf-sc-t1--base.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t1.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t1.vf)
Provides:       tex(Domitian-Roman-tlf-sc-t2a--base.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2a.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2a.vf)
Provides:       tex(Domitian-Roman-tlf-sc-t2b--base.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2b.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2b.vf)
Provides:       tex(Domitian-Roman-tlf-sc-t2c--base.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2c.tfm)
Provides:       tex(Domitian-Roman-tlf-sc-t2c.vf)
Provides:       tex(Domitian-Roman-tlf-t1--base.tfm)
Provides:       tex(Domitian-Roman-tlf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-t1.tfm)
Provides:       tex(Domitian-Roman-tlf-t1.vf)
Provides:       tex(Domitian-Roman-tlf-t2a--base.tfm)
Provides:       tex(Domitian-Roman-tlf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-t2a.tfm)
Provides:       tex(Domitian-Roman-tlf-t2a.vf)
Provides:       tex(Domitian-Roman-tlf-t2b--base.tfm)
Provides:       tex(Domitian-Roman-tlf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-t2b.tfm)
Provides:       tex(Domitian-Roman-tlf-t2b.vf)
Provides:       tex(Domitian-Roman-tlf-t2c--base.tfm)
Provides:       tex(Domitian-Roman-tlf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tlf-t2c.tfm)
Provides:       tex(Domitian-Roman-tlf-t2c.vf)
Provides:       tex(Domitian-Roman-tlf-ts1--base.tfm)
Provides:       tex(Domitian-Roman-tlf-ts1.tfm)
Provides:       tex(Domitian-Roman-tlf-ts1.vf)
Provides:       tex(Domitian-Roman-tosf-lgr--base.tfm)
Provides:       tex(Domitian-Roman-tosf-lgr.tfm)
Provides:       tex(Domitian-Roman-tosf-lgr.vf)
Provides:       tex(Domitian-Roman-tosf-ly1--base.tfm)
Provides:       tex(Domitian-Roman-tosf-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-ly1.tfm)
Provides:       tex(Domitian-Roman-tosf-ly1.vf)
Provides:       tex(Domitian-Roman-tosf-ot1--base.tfm)
Provides:       tex(Domitian-Roman-tosf-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-ot1.tfm)
Provides:       tex(Domitian-Roman-tosf-ot1.vf)
Provides:       tex(Domitian-Roman-tosf-sc-lgr--base.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-lgr.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-lgr.vf)
Provides:       tex(Domitian-Roman-tosf-sc-ly1--base.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-ly1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-ly1.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-ly1.vf)
Provides:       tex(Domitian-Roman-tosf-sc-ot1--base.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-ot1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-ot1.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-ot1.vf)
Provides:       tex(Domitian-Roman-tosf-sc-t1--base.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t1.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t1.vf)
Provides:       tex(Domitian-Roman-tosf-sc-t2a--base.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2a.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2a.vf)
Provides:       tex(Domitian-Roman-tosf-sc-t2b--base.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2b.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2b.vf)
Provides:       tex(Domitian-Roman-tosf-sc-t2c--base.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2c.tfm)
Provides:       tex(Domitian-Roman-tosf-sc-t2c.vf)
Provides:       tex(Domitian-Roman-tosf-t1--base.tfm)
Provides:       tex(Domitian-Roman-tosf-t1--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-t1.tfm)
Provides:       tex(Domitian-Roman-tosf-t1.vf)
Provides:       tex(Domitian-Roman-tosf-t2a--base.tfm)
Provides:       tex(Domitian-Roman-tosf-t2a--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-t2a.tfm)
Provides:       tex(Domitian-Roman-tosf-t2a.vf)
Provides:       tex(Domitian-Roman-tosf-t2b--base.tfm)
Provides:       tex(Domitian-Roman-tosf-t2b--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-t2b.tfm)
Provides:       tex(Domitian-Roman-tosf-t2b.vf)
Provides:       tex(Domitian-Roman-tosf-t2c--base.tfm)
Provides:       tex(Domitian-Roman-tosf-t2c--lcdfj.tfm)
Provides:       tex(Domitian-Roman-tosf-t2c.tfm)
Provides:       tex(Domitian-Roman-tosf-t2c.vf)
Provides:       tex(Domitian-Roman-tosf-ts1--base.tfm)
Provides:       tex(Domitian-Roman-tosf-ts1.tfm)
Provides:       tex(Domitian-Roman-tosf-ts1.vf)
Provides:       tex(Domitian.map)
Provides:       tex(LGRDomitian-Inf.fd)
Provides:       tex(LGRDomitian-Sup.fd)
Provides:       tex(LGRDomitian-TLF.fd)
Provides:       tex(LGRDomitian-TOsF.fd)
Provides:       tex(LY1Domitian-Inf.fd)
Provides:       tex(LY1Domitian-Sup.fd)
Provides:       tex(LY1Domitian-TLF.fd)
Provides:       tex(LY1Domitian-TOsF.fd)
Provides:       tex(OT1Domitian-Inf.fd)
Provides:       tex(OT1Domitian-Sup.fd)
Provides:       tex(OT1Domitian-TLF.fd)
Provides:       tex(OT1Domitian-TOsF.fd)
Provides:       tex(T1Domitian-Inf.fd)
Provides:       tex(T1Domitian-Sup.fd)
Provides:       tex(T1Domitian-TLF.fd)
Provides:       tex(T1Domitian-TOsF.fd)
Provides:       tex(T2ADomitian-Inf.fd)
Provides:       tex(T2ADomitian-Sup.fd)
Provides:       tex(T2ADomitian-TLF.fd)
Provides:       tex(T2ADomitian-TOsF.fd)
Provides:       tex(T2BDomitian-Inf.fd)
Provides:       tex(T2BDomitian-Sup.fd)
Provides:       tex(T2BDomitian-TLF.fd)
Provides:       tex(T2BDomitian-TOsF.fd)
Provides:       tex(T2CDomitian-Inf.fd)
Provides:       tex(T2CDomitian-Sup.fd)
Provides:       tex(T2CDomitian-TLF.fd)
Provides:       tex(T2CDomitian-TOsF.fd)
Provides:       tex(TS1Domitian-TLF.fd)
Provides:       tex(TS1Domitian-TOsF.fd)
Provides:       tex(a_4ivb7d.enc)
Provides:       tex(a_6377uz.enc)
Provides:       tex(a_6i6esj.enc)
Provides:       tex(a_6ikg3w.enc)
Provides:       tex(a_6scvia.enc)
Provides:       tex(a_7a7dfs.enc)
Provides:       tex(a_7plddl.enc)
Provides:       tex(a_7xwqay.enc)
Provides:       tex(a_b7m3mh.enc)
Provides:       tex(a_bhlgjd.enc)
Provides:       tex(a_bqrttn.enc)
Provides:       tex(a_bxerws.enc)
Provides:       tex(a_cekwsu.enc)
Provides:       tex(a_emqd3c.enc)
Provides:       tex(a_fivy6z.enc)
Provides:       tex(a_fxkipf.enc)
Provides:       tex(a_ghqtel.enc)
Provides:       tex(a_gzbwdd.enc)
Provides:       tex(a_hjkpcv.enc)
Provides:       tex(a_hofxhi.enc)
Provides:       tex(a_hucpnb.enc)
Provides:       tex(a_hxu6ib.enc)
Provides:       tex(a_iobvua.enc)
Provides:       tex(a_ka64dt.enc)
Provides:       tex(a_kvnmfl.enc)
Provides:       tex(a_mf4elt.enc)
Provides:       tex(a_mnfltk.enc)
Provides:       tex(a_mpk3tx.enc)
Provides:       tex(a_mwmumz.enc)
Provides:       tex(a_myj6j5.enc)
Provides:       tex(a_n6jnlw.enc)
Provides:       tex(a_ni6bof.enc)
Provides:       tex(a_rs25bv.enc)
Provides:       tex(a_rzgskp.enc)
Provides:       tex(a_vbh7z5.enc)
Provides:       tex(a_veicm7.enc)
Provides:       tex(a_vhhklz.enc)
Provides:       tex(a_walexi.enc)
Provides:       tex(a_wnmxsi.enc)
Provides:       tex(a_wqsro2.enc)
Provides:       tex(a_x44hng.enc)
Provides:       tex(a_xa7i5w.enc)
Provides:       tex(a_xammmp.enc)
Provides:       tex(a_xlssed.enc)
Provides:       tex(a_yvovof.enc)
Provides:       tex(a_zkzzwq.enc)
Provides:       tex(a_zoccsd.enc)
Provides:       tex(domitian.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(mweights.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source187:      domitian.tar.xz
Source188:      domitian.doc.tar.xz

%description -n texlive-domitian
The Domitian fonts are a free and open-source OpenType font
family, based on the Palatino design by Hermann Zapf
(1918-2015), as implemented in Palladio, the version
distributed as part of URW's free Core 35 PostScript fonts
(2.0). Domitian is meant as a drop-in replacement for Adobe's
version of Palatino. It extends Palladio with small capitals,
old-style figures and scientific inferiors. The metrics have
been adjusted to more closely match Adobe Palatino, and hinting
has been improved.

%package -n texlive-domitian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn54512
Release:        0
Summary:        Documentation for texlive-domitian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-domitian-doc
This package includes the documentation for texlive-domitian


%package -n texlive-domitian-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn54512
Release:        0
Summary:        Severed fonts for texlive-domitian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-domitian-fonts
The  separated fonts package for texlive-domitian
%post -n texlive-domitian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap Domitian.map' >> /var/run/texlive/run-updmap

%postun -n texlive-domitian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap Domitian.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-domitian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-domitian-fonts
%files -n texlive-domitian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/domitian/COPYING
%{_texmfdistdir}/doc/fonts/domitian/README
%{_texmfdistdir}/doc/fonts/domitian/domitian-doc.pdf
%{_texmfdistdir}/doc/fonts/domitian/domitian-doc.tex

%files -n texlive-domitian
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_4ivb7d.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_6377uz.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_6i6esj.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_6ikg3w.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_6scvia.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_7a7dfs.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_7plddl.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_7xwqay.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_b7m3mh.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_bhlgjd.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_bqrttn.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_bxerws.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_cekwsu.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_emqd3c.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_fivy6z.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_fxkipf.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_ghqtel.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_gzbwdd.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_hjkpcv.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_hofxhi.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_hucpnb.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_hxu6ib.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_iobvua.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_ka64dt.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_kvnmfl.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_mf4elt.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_mnfltk.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_mpk3tx.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_mwmumz.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_myj6j5.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_n6jnlw.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_ni6bof.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_rs25bv.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_rzgskp.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_vbh7z5.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_veicm7.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_vhhklz.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_walexi.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_wnmxsi.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_wqsro2.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_x44hng.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_xa7i5w.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_xammmp.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_xlssed.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_yvovof.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_zkzzwq.enc
%{_texmfdistdir}/fonts/enc/dvips/domitian/a_zoccsd.enc
%{_texmfdistdir}/fonts/map/dvips/domitian/Domitian.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/domitian/Domitian-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/domitian/Domitian-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/domitian/Domitian-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/domitian/Domitian-Roman.otf
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-inf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-sup-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-sc-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-lgr--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-lgr.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-ly1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-ot1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-sc-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t1--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2a--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2b--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2c--lcdfj.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/domitian/Domitian-Roman-tosf-ts1.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-BoldItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-BoldLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-ItalicLCDFJ.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-Roman.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/domitian/Domitian-RomanLCDFJ.pfb
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-inf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-inf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-inf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-inf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-inf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-inf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-sup-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-sup-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-sup-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-inf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-inf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-inf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-inf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-inf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-inf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-sup-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-sup-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-sup-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-inf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-inf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-inf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-inf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-inf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-inf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-sup-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-sup-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-sup-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-inf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-inf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-inf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-inf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-inf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-inf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-inf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-sup-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-sup-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-sup-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-sup-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-sup-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-sc-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-sc-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-sc-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-sc-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-sc-lgr.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-sc-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-sc-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-sc-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-t2a.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-t2b.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-t2c.vf
%{_texmfdistdir}/fonts/vf/public/domitian/Domitian-Roman-tosf-ts1.vf
%{_texmfdistdir}/tex/latex/domitian/LGRDomitian-Inf.fd
%{_texmfdistdir}/tex/latex/domitian/LGRDomitian-Sup.fd
%{_texmfdistdir}/tex/latex/domitian/LGRDomitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/LGRDomitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/LY1Domitian-Inf.fd
%{_texmfdistdir}/tex/latex/domitian/LY1Domitian-Sup.fd
%{_texmfdistdir}/tex/latex/domitian/LY1Domitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/LY1Domitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/OT1Domitian-Inf.fd
%{_texmfdistdir}/tex/latex/domitian/OT1Domitian-Sup.fd
%{_texmfdistdir}/tex/latex/domitian/OT1Domitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/OT1Domitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/T1Domitian-Inf.fd
%{_texmfdistdir}/tex/latex/domitian/T1Domitian-Sup.fd
%{_texmfdistdir}/tex/latex/domitian/T1Domitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/T1Domitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/T2ADomitian-Inf.fd
%{_texmfdistdir}/tex/latex/domitian/T2ADomitian-Sup.fd
%{_texmfdistdir}/tex/latex/domitian/T2ADomitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/T2ADomitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/T2BDomitian-Inf.fd
%{_texmfdistdir}/tex/latex/domitian/T2BDomitian-Sup.fd
%{_texmfdistdir}/tex/latex/domitian/T2BDomitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/T2BDomitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/T2CDomitian-Inf.fd
%{_texmfdistdir}/tex/latex/domitian/T2CDomitian-Sup.fd
%{_texmfdistdir}/tex/latex/domitian/T2CDomitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/T2CDomitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/TS1Domitian-TLF.fd
%{_texmfdistdir}/tex/latex/domitian/TS1Domitian-TOsF.fd
%{_texmfdistdir}/tex/latex/domitian/domitian.sty

%files -n texlive-domitian-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-domitian
%{_datadir}/fontconfig/conf.avail/58-texlive-domitian.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-domitian.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-domitian.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-domitian/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-domitian/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-domitian/fonts.scale
%{_datadir}/fonts/texlive-domitian/Domitian-Bold.otf
%{_datadir}/fonts/texlive-domitian/Domitian-BoldItalic.otf
%{_datadir}/fonts/texlive-domitian/Domitian-Italic.otf
%{_datadir}/fonts/texlive-domitian/Domitian-Roman.otf
%{_datadir}/fonts/texlive-domitian/Domitian-Bold.pfb
%{_datadir}/fonts/texlive-domitian/Domitian-BoldItalic.pfb
%{_datadir}/fonts/texlive-domitian/Domitian-BoldItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-domitian/Domitian-BoldLCDFJ.pfb
%{_datadir}/fonts/texlive-domitian/Domitian-Italic.pfb
%{_datadir}/fonts/texlive-domitian/Domitian-ItalicLCDFJ.pfb
%{_datadir}/fonts/texlive-domitian/Domitian-Roman.pfb
%{_datadir}/fonts/texlive-domitian/Domitian-RomanLCDFJ.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-domitian-fonts-%{texlive_version}.%{texlive_noarch}.1.0csvn54512-%{release}-zypper
%endif

%package -n texlive-dosepsbin
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn29752
Release:        0
Summary:        Deal with DOS binary EPS files
License:        Artistic-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-dosepsbin-bin >= %{texlive_version}
#!BuildIgnore: texlive-dosepsbin-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dosepsbin-doc >= %{texlive_version}
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(Pod::Usage)
#!BuildIgnore:  perl(Pod::Usage)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source189:      dosepsbin.tar.xz
Source190:      dosepsbin.doc.tar.xz

%description -n texlive-dosepsbin
A Encapsulated PostScript (EPS) file may given in a special
binary format to support the inclusion of a thumbnail. This
file format, commonly known as DOS EPS format starts with a
binary header that contains the positions of the possible
sections: PostScript (PS); Windows Metafile Format (WMF); and
Tag Image File Format (TIFF). The PS section must be present
and either the WMF file or the TIFF file should be given. The
package provides a Perl program that will extract any of the
sections of such a file, in particular providing a 'text'-form
EPS file for use with (La)TeX.

%package -n texlive-dosepsbin-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn29752
Release:        0
Summary:        Documentation for texlive-dosepsbin
License:        Artistic-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(dosepsbin.1)

%description -n texlive-dosepsbin-doc
This package includes the documentation for texlive-dosepsbin

%post -n texlive-dosepsbin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dosepsbin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dosepsbin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dosepsbin-doc
%defattr(-,root,root,755)
%{_mandir}/man1/dosepsbin.1*
%{_texmfdistdir}/doc/support/dosepsbin/Makefile.in
%{_texmfdistdir}/doc/support/dosepsbin/README
%{_texmfdistdir}/doc/support/dosepsbin/clean-case.pl
%{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.html
%{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.ltx
%{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.pdf
%{_texmfdistdir}/doc/support/dosepsbin/dosepsbin.txt
%{_texmfdistdir}/doc/support/dosepsbin/version.pl

%files -n texlive-dosepsbin
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/dosepsbin/dosepsbin.pl
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dosepsbin-%{texlive_version}.%{texlive_noarch}.1.2svn29752-%{release}-zypper
%endif

%package -n texlive-dot2texi
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn26237
Release:        0
Summary:        Create graphs within LaTeX using the dot2tex tool
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
Recommends:     texlive-dot2texi-doc >= %{texlive_version}
Provides:       tex(dot2texi.sty)
Requires:       tex(moreverb.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source191:      dot2texi.tar.xz
Source192:      dot2texi.doc.tar.xz

%description -n texlive-dot2texi
The dot2texi package allows you to embed graphs in the DOT
graph description language in your LaTeX documents. The dot2tex
tool is used to invoke Graphviz for graph layout, and to
transform the output from Graphviz to LaTeX code. The generated
code relies on the TikZ and PGF package or the PSTricks
package. The process is automated if shell escape is enabled.

%package -n texlive-dot2texi-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn26237
Release:        0
Summary:        Documentation for texlive-dot2texi
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dot2texi-doc
This package includes the documentation for texlive-dot2texi

%post -n texlive-dot2texi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dot2texi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dot2texi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dot2texi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dot2texi/README
%{_texmfdistdir}/doc/latex/dot2texi/dot2texi.pdf
%{_texmfdistdir}/doc/latex/dot2texi/dot2texi.tex
%{_texmfdistdir}/doc/latex/dot2texi/examples/d2tpstexamples.pdf
%{_texmfdistdir}/doc/latex/dot2texi/examples/d2tpstexamples.tex
%{_texmfdistdir}/doc/latex/dot2texi/examples/d2ttikzexamples.pdf
%{_texmfdistdir}/doc/latex/dot2texi/examples/d2ttikzexamples.tex
%{_texmfdistdir}/doc/latex/dot2texi/examples/docgraphs.pdf
%{_texmfdistdir}/doc/latex/dot2texi/examples/docgraphs.tex
%{_texmfdistdir}/doc/latex/dot2texi/examples/docgraphsorig.pdf
%{_texmfdistdir}/doc/latex/dot2texi/gpl.txt

%files -n texlive-dot2texi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dot2texi/dot2texi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dot2texi-%{texlive_version}.%{texlive_noarch}.3.0svn26237-%{release}-zypper
%endif

%package -n texlive-dotarrow
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01asvn15878
Release:        0
Summary:        Extendable dotted arrows
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dotarrow-doc >= %{texlive_version}
Provides:       tex(DotArrow.sty)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source193:      dotarrow.tar.xz
Source194:      dotarrow.doc.tar.xz

%description -n texlive-dotarrow
The package can draw dotted arrows that are extendable, in the
same was as \xrightarrow.

%package -n texlive-dotarrow-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.01asvn15878
Release:        0
Summary:        Documentation for texlive-dotarrow
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dotarrow-doc
This package includes the documentation for texlive-dotarrow

%post -n texlive-dotarrow
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dotarrow 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dotarrow
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dotarrow-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dotarrow/DotArrow.pdf
%{_texmfdistdir}/doc/latex/dotarrow/DotArrow.tex
%{_texmfdistdir}/doc/latex/dotarrow/README

%files -n texlive-dotarrow
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dotarrow/DotArrow.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dotarrow-%{texlive_version}.%{texlive_noarch}.0.0.01asvn15878-%{release}-zypper
%endif

%package -n texlive-dotlessi
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51476
Release:        0
Summary:        Provides dotless i's and j's for use in any math font
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dotlessi-doc >= %{texlive_version}
Provides:       tex(dotlessi.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source195:      dotlessi.tar.xz
Source196:      dotlessi.doc.tar.xz

%description -n texlive-dotlessi
The package provides two commands: \dotlessi and \dotlessj,
which give access to dotless i's and j's in math mode. They are
intended for symbols in non English languages.

%package -n texlive-dotlessi-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn51476
Release:        0
Summary:        Documentation for texlive-dotlessi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dotlessi-doc
This package includes the documentation for texlive-dotlessi

%post -n texlive-dotlessi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dotlessi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dotlessi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dotlessi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dotlessi/README.md

%files -n texlive-dotlessi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dotlessi/dotlessi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dotlessi-%{texlive_version}.%{texlive_noarch}.1.1svn51476-%{release}-zypper
%endif

%package -n texlive-dotseqn
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn17195
Release:        0
Summary:        Flush left equations with dotted leaders to the numbers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dotseqn-doc >= %{texlive_version}
Provides:       tex(dotseqn.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source197:      dotseqn.tar.xz
Source198:      dotseqn.doc.tar.xz

%description -n texlive-dotseqn
The package provides a different format for typesetting
equations, one reportedly used in 'old style Britsh books':
equations aligned on the left, with dots on the right leading
to the equation number. In default of an equation number, the
package operates much like the fleqn class option (no leaders).

%package -n texlive-dotseqn-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn17195
Release:        0
Summary:        Documentation for texlive-dotseqn
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dotseqn-doc
This package includes the documentation for texlive-dotseqn

%post -n texlive-dotseqn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dotseqn 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dotseqn
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dotseqn-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dotseqn/dotseqn.pdf
%{_texmfdistdir}/doc/latex/dotseqn/readme

%files -n texlive-dotseqn
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dotseqn/dotseqn.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dotseqn-%{texlive_version}.%{texlive_noarch}.1.1svn17195-%{release}-zypper
%endif

%package -n texlive-dottex
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn15878
Release:        0
Summary:        Use dot code in LaTeX
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
Recommends:     texlive-dottex-doc >= %{texlive_version}
Provides:       tex(dottex.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(keyval.sty)
Requires:       tex(moreverb.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source199:      dottex.tar.xz
Source200:      dottex.doc.tar.xz

%description -n texlive-dottex
The dottex package allows you to encapsulate 'dot' and 'neato'
files in your document (dot and neato are both part of
graphviz; dot creates directed graphs, neato undirected
graphs). If you have shell-escape enabled, the package will
arrange for your files to be processed at LaTeX time;
otherwise, the conversion must be done manually as an
intermediate process before a second LaTeX run.

%package -n texlive-dottex-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn15878
Release:        0
Summary:        Documentation for texlive-dottex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dottex-doc
This package includes the documentation for texlive-dottex

%post -n texlive-dottex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dottex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dottex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dottex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dottex/README
%{_texmfdistdir}/doc/latex/dottex/dottex.pdf
%{_texmfdistdir}/doc/latex/dottex/example.tex
%{_texmfdistdir}/doc/latex/dottex/gpl.txt

%files -n texlive-dottex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dottex/dottex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dottex-%{texlive_version}.%{texlive_noarch}.0.0.6svn15878-%{release}-zypper
%endif

%package -n texlive-doublestroke
Version:        %{texlive_version}.%{texlive_noarch}.1.111svn15878
Release:        0
Summary:        Typeset mathematical double stroke symbols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
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
Requires:       texlive-doublestroke-fonts >= %{texlive_version}
Recommends:     texlive-doublestroke-doc >= %{texlive_version}
Provides:       tex(Udsrom.fd)
Provides:       tex(Udsss.fd)
Provides:       tex(dsfont.sty)
Provides:       tex(dsrom10.tfm)
Provides:       tex(dsrom12.tfm)
Provides:       tex(dsrom8.tfm)
Provides:       tex(dsss10.tfm)
Provides:       tex(dsss12.tfm)
Provides:       tex(dsss8.tfm)
Provides:       tex(dstroke.map)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source201:      doublestroke.tar.xz
Source202:      doublestroke.doc.tar.xz

%description -n texlive-doublestroke
A font based on Computer Modern Roman useful for typesetting
the mathematical symbols for the natural numbers (N), whole
numbers (Z), rational numbers (Q), real numbers (R) and complex
numbers (C); coverage includes all Roman capital letters, '1',
'h' and 'k'. The font is available both as Metafont source and
in Adobe Type 1 format, and LaTeX macros for its use are
provided. The fonts appear in the blackboard bold sampler.

%package -n texlive-doublestroke-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.111svn15878
Release:        0
Summary:        Documentation for texlive-doublestroke
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-doublestroke-doc
This package includes the documentation for texlive-doublestroke


%package -n texlive-doublestroke-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.111svn15878
Release:        0
Summary:        Severed fonts for texlive-doublestroke
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-doublestroke-fonts
The  separated fonts package for texlive-doublestroke
%post -n texlive-doublestroke
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap dstroke.map' >> /var/run/texlive/run-updmap

%postun -n texlive-doublestroke 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap dstroke.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-doublestroke
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-doublestroke-fonts
%files -n texlive-doublestroke-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/doublestroke/README
%{_texmfdistdir}/doc/fonts/doublestroke/dsdoc.pdf
%{_texmfdistdir}/doc/fonts/doublestroke/dsdoc.tex

%files -n texlive-doublestroke
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/doublestroke/dstroke.map
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom10.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom12.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsrom8.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsromo.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsromu.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsss10.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsss12.mf
%{_texmfdistdir}/fonts/source/public/doublestroke/dsss8.mf
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsrom10.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsrom12.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsrom8.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsss10.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsss12.tfm
%{_texmfdistdir}/fonts/tfm/public/doublestroke/dsss8.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/doublestroke/dsrom10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/doublestroke/dsrom12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/doublestroke/dsrom8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/doublestroke/dsss10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/doublestroke/dsss12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/doublestroke/dsss8.pfb
%{_texmfdistdir}/tex/latex/doublestroke/Udsrom.fd
%{_texmfdistdir}/tex/latex/doublestroke/Udsss.fd
%{_texmfdistdir}/tex/latex/doublestroke/dsfont.sty

%files -n texlive-doublestroke-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-doublestroke
%{_datadir}/fontconfig/conf.avail/58-texlive-doublestroke.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-doublestroke/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-doublestroke/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-doublestroke/fonts.scale
%{_datadir}/fonts/texlive-doublestroke/dsrom10.pfb
%{_datadir}/fonts/texlive-doublestroke/dsrom12.pfb
%{_datadir}/fonts/texlive-doublestroke/dsrom8.pfb
%{_datadir}/fonts/texlive-doublestroke/dsss10.pfb
%{_datadir}/fonts/texlive-doublestroke/dsss12.pfb
%{_datadir}/fonts/texlive-doublestroke/dsss8.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-doublestroke-fonts-%{texlive_version}.%{texlive_noarch}.1.111svn15878-%{release}-zypper
%endif

%package -n texlive-dowith
Version:        %{texlive_version}.%{texlive_noarch}.r0.32svn38860
Release:        0
Summary:        Apply a command to a list of items
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dowith-doc >= %{texlive_version}
Provides:       tex(domore.sty)
Provides:       tex(dowith.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source203:      dowith.tar.xz
Source204:      dowith.doc.tar.xz

%description -n texlive-dowith
The package provides macros for applying a command to all
elements of a list without separators, such as
'\DoWithAllIn{<cmd>}{<list-macro>}', and also for extending and
reducing macros storing such lists. Applications in mind
belonged to LaTeX, but the package should work with other
formats as well. Loop and list macros in other packages are
discussed. A further package, domore, is also provided, which
enhances the functionality of dowith.

%package -n texlive-dowith-doc
Version:        %{texlive_version}.%{texlive_noarch}.r0.32svn38860
Release:        0
Summary:        Documentation for texlive-dowith
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dowith-doc
This package includes the documentation for texlive-dowith

%post -n texlive-dowith
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dowith 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dowith
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dowith-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/dowith/Announce.txt
%{_texmfdistdir}/doc/generic/dowith/README
%{_texmfdistdir}/doc/generic/dowith/SrcFILEs.txt
%{_texmfdistdir}/doc/generic/dowith/domore.pdf
%{_texmfdistdir}/doc/generic/dowith/dowith.pdf

%files -n texlive-dowith
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/dowith/domore.sty
%{_texmfdistdir}/tex/generic/dowith/dowith.RLS
%{_texmfdistdir}/tex/generic/dowith/dowith.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dowith-%{texlive_version}.%{texlive_noarch}.r0.32svn38860-%{release}-zypper
%endif

%package -n texlive-download
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn52257
Release:        0
Summary:        Allow LaTeX to download files using an external process
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-download-doc >= %{texlive_version}
Provides:       tex(download.sty)
Requires:       tex(expl3.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source205:      download.tar.xz
Source206:      download.doc.tar.xz

%description -n texlive-download
The package allows the user to download files (using cURL or
wget), from within a document. To run the external commands,
LaTeX (or whatever) needs to be run with the --shell-escape
flag; this creates a tension between your needs and the
security implications of the flag; users should exercise due
caution.

%package -n texlive-download-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn52257
Release:        0
Summary:        Documentation for texlive-download
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-download-doc
This package includes the documentation for texlive-download

%post -n texlive-download
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-download 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-download
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-download-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/download/README
%{_texmfdistdir}/doc/latex/download/download.pdf

%files -n texlive-download
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/download/download.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-download-%{texlive_version}.%{texlive_noarch}.1.2svn52257-%{release}-zypper
%endif

%package -n texlive-dox
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn46011
Release:        0
Summary:        Extend the doc package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dox-doc >= %{texlive_version}
Provides:       tex(dox.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source207:      dox.tar.xz
Source208:      dox.doc.tar.xz

%description -n texlive-dox
The doc package provides LaTeX developers with means to
describe the usage and the definition of new macros and
environments. However, there is no simple way to extend this
functionality to other items (options or counters, for
instance). The DoX package is designed to circumvent this
limitation.

%package -n texlive-dox-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.4svn46011
Release:        0
Summary:        Documentation for texlive-dox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dox-doc
This package includes the documentation for texlive-dox

%post -n texlive-dox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dox/NEWS
%{_texmfdistdir}/doc/latex/dox/README.md
%{_texmfdistdir}/doc/latex/dox/THANKS
%{_texmfdistdir}/doc/latex/dox/dox.el
%{_texmfdistdir}/doc/latex/dox/dox.pdf
%{_texmfdistdir}/doc/latex/dox/header.inc

%files -n texlive-dox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dox/dox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dox-%{texlive_version}.%{texlive_noarch}.2.4svn46011-%{release}-zypper
%endif

%package -n texlive-dozenal
Version:        %{texlive_version}.%{texlive_noarch}.7.2svn47680
Release:        0
Summary:        Typeset documents using base twelve numbering (also called "dozenal")
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-dozenal-fonts >= %{texlive_version}
Recommends:     texlive-dozenal-doc >= %{texlive_version}
Provides:       tex(dozchars10.tfm)
Provides:       tex(dozchars12.tfm)
Provides:       tex(dozchars17.tfm)
Provides:       tex(dozchars6.tfm)
Provides:       tex(dozchars7.tfm)
Provides:       tex(dozchars8.tfm)
Provides:       tex(dozchars9.tfm)
Provides:       tex(dozchb10.tfm)
Provides:       tex(dozchbx10.tfm)
Provides:       tex(dozchbx12.tfm)
Provides:       tex(dozchbx5.tfm)
Provides:       tex(dozchbx6.tfm)
Provides:       tex(dozchbx7.tfm)
Provides:       tex(dozchbx8.tfm)
Provides:       tex(dozchbx9.tfm)
Provides:       tex(dozchbxi10.tfm)
Provides:       tex(dozchbxsl10.tfm)
Provides:       tex(dozchit10.tfm)
Provides:       tex(dozchit12.tfm)
Provides:       tex(dozchit7.tfm)
Provides:       tex(dozchit8.tfm)
Provides:       tex(dozchit9.tfm)
Provides:       tex(dozchsl10.tfm)
Provides:       tex(dozchsl12.tfm)
Provides:       tex(dozchsl8.tfm)
Provides:       tex(dozchsl9.tfm)
Provides:       tex(dozenal.map)
Provides:       tex(dozenal.sty)
Provides:       tex(gray.tfm)
Requires:       tex(fixltx2e.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(mfirstuc.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source209:      dozenal.tar.xz
Source210:      dozenal.doc.tar.xz

%description -n texlive-dozenal
The package supports typesetting documents whose counters are
represented in base twelve, also called "dozenal". It includes
a macro by David Kastrup for converting positive whole numbers
to dozenal from decimal (base ten) representation. The package
also includes a few other macros and redefines all the standard
counters to produce dozenal output. Fonts, in Roman, italic,
slanted, and boldface versions, provide ten and eleven (the
Pitman characters preferred by the Dozenal Society of Great
Britain). The fonts were designed to blend well with the
Computer Modern fonts, and are available both as Metafont
source and in Adobe Type 1 format.

%package -n texlive-dozenal-doc
Version:        %{texlive_version}.%{texlive_noarch}.7.2svn47680
Release:        0
Summary:        Documentation for texlive-dozenal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dozenal-doc
This package includes the documentation for texlive-dozenal


%package -n texlive-dozenal-fonts
Version:        %{texlive_version}.%{texlive_noarch}.7.2svn47680
Release:        0
Summary:        Severed fonts for texlive-dozenal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-dozenal-fonts
The  separated fonts package for texlive-dozenal
%post -n texlive-dozenal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dozenal 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dozenal
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-dozenal-fonts
%files -n texlive-dozenal-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dozenal/CHANGES
%{_texmfdistdir}/doc/fonts/dozenal/README
%{_texmfdistdir}/doc/fonts/dozenal/dozenal.pdf
%{_texmfdistdir}/doc/fonts/dozenal/dozenalfilelist.txt
%{_texmfdistdir}/doc/fonts/dozenal/lppl.txt

%files -n texlive-dozenal
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchars10.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchars12.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchars17.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchars6.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchars7.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchars8.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchars9.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchb10.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbx10.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbx12.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbx5.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbx6.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbx7.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbx8.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbx9.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbxi10.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchbxsl10.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchit10.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchit12.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchit7.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchit8.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchit9.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchsl10.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchsl12.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchsl8.afm
%{_texmfdistdir}/fonts/afm/public/dozenal/dozchsl9.afm
%{_texmfdistdir}/fonts/map/dvips/dozenal/dozenal.map
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars17.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars6.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars7.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchars9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchb10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx5.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx6.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx7.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbx9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbxi10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchbxsl10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit7.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchit9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl10.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl12.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl8.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozchsl9.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenal.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenalb.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenali.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenalitalic.mf
%{_texmfdistdir}/fonts/source/public/dozenal/dozenalroman.mf
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars17.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars6.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars7.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchars9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchb10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbxi10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit7.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchit9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/dozchsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/dozenal/gray.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchars10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchars12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchars17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchars6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchars7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchars8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchars9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbx5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbxi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchbxsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchit10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchit12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchit7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchit8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchit9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchsl12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchsl8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dozenal/dozchsl9.pfb
%{_texmfdistdir}/tex/latex/dozenal/dozenal.sty

%files -n texlive-dozenal-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-dozenal
%{_datadir}/fontconfig/conf.avail/58-texlive-dozenal.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dozenal/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dozenal/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dozenal/fonts.scale
%{_datadir}/fonts/texlive-dozenal/dozchars10.pfb
%{_datadir}/fonts/texlive-dozenal/dozchars12.pfb
%{_datadir}/fonts/texlive-dozenal/dozchars17.pfb
%{_datadir}/fonts/texlive-dozenal/dozchars6.pfb
%{_datadir}/fonts/texlive-dozenal/dozchars7.pfb
%{_datadir}/fonts/texlive-dozenal/dozchars8.pfb
%{_datadir}/fonts/texlive-dozenal/dozchars9.pfb
%{_datadir}/fonts/texlive-dozenal/dozchb10.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbx10.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbx12.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbx5.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbx6.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbx7.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbx8.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbx9.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbxi10.pfb
%{_datadir}/fonts/texlive-dozenal/dozchbxsl10.pfb
%{_datadir}/fonts/texlive-dozenal/dozchit10.pfb
%{_datadir}/fonts/texlive-dozenal/dozchit12.pfb
%{_datadir}/fonts/texlive-dozenal/dozchit7.pfb
%{_datadir}/fonts/texlive-dozenal/dozchit8.pfb
%{_datadir}/fonts/texlive-dozenal/dozchit9.pfb
%{_datadir}/fonts/texlive-dozenal/dozchsl10.pfb
%{_datadir}/fonts/texlive-dozenal/dozchsl12.pfb
%{_datadir}/fonts/texlive-dozenal/dozchsl8.pfb
%{_datadir}/fonts/texlive-dozenal/dozchsl9.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dozenal-fonts-%{texlive_version}.%{texlive_noarch}.7.2svn47680-%{release}-zypper
%endif

%package -n texlive-dpcircling
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54750
Release:        0
Summary:        Decorated text boxes using TikZ
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dpcircling-doc >= %{texlive_version}
Provides:       tex(DPcircling.sty)
Requires:       tex(keyval.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source211:      dpcircling.tar.xz
Source212:      dpcircling.doc.tar.xz

%description -n texlive-dpcircling
This simple package provides four types of text decorations
using TikZ. You can frame your text with circles, rectangles,
jagged rectangles, and fan-shapes. The baseline will be
adjusted properly according to the surroundings. You can use
these decorations both in text mode and in math mode. You can
specify line color, line width, width, and height using option
keys.

%package -n texlive-dpcircling-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54750
Release:        0
Summary:        Documentation for texlive-dpcircling
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dpcircling-doc
This package includes the documentation for texlive-dpcircling

%post -n texlive-dpcircling
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dpcircling 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dpcircling
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dpcircling-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dpcircling/DPcircling.pdf
%{_texmfdistdir}/doc/latex/dpcircling/DPcircling.tex
%{_texmfdistdir}/doc/latex/dpcircling/LICENSE
%{_texmfdistdir}/doc/latex/dpcircling/README.md

%files -n texlive-dpcircling
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dpcircling/DPcircling.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dpcircling-%{texlive_version}.%{texlive_noarch}.1.0svn54750-%{release}-zypper
%endif

%package -n texlive-dpfloat
Version:        %{texlive_version}.%{texlive_noarch}.svn17196
Release:        0
Summary:        Support for double-page floats
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dpfloat-doc >= %{texlive_version}
Provides:       tex(dpfloat.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source213:      dpfloat.tar.xz
Source214:      dpfloat.doc.tar.xz

%description -n texlive-dpfloat
Provides fullpage and leftfullpage environments, that may be
used inside a figure, table, or other float environment. If the
first of a 2-page spread uses a "leftfullpage" environment, the
float will only be typeset on an even-numbered page, and the
two floats will appear side-by-side in a two-sided document.

%package -n texlive-dpfloat-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn17196
Release:        0
Summary:        Documentation for texlive-dpfloat
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dpfloat-doc
This package includes the documentation for texlive-dpfloat

%post -n texlive-dpfloat
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dpfloat 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dpfloat
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dpfloat-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dpfloat/README
%{_texmfdistdir}/doc/latex/dpfloat/dpfloat.pdf
%{_texmfdistdir}/doc/latex/dpfloat/dpfloat.tex

%files -n texlive-dpfloat
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dpfloat/dpfloat.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dpfloat-%{texlive_version}.%{texlive_noarch}.svn17196-%{release}-zypper
%endif

%package -n texlive-dprogress
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        LaTeX-relevant log information for debugging
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dprogress-doc >= %{texlive_version}
Provides:       tex(dprogress.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source215:      dprogress.tar.xz
Source216:      dprogress.doc.tar.xz

%description -n texlive-dprogress
The package logs LaTeX's progress through the file, making the
LaTeX output more verbose. This helps to make LaTeX debugging
easier, as it is simpler to find where exactly LaTeX failed.
The package outputs the typesetting of section, subsection and
subsubsection headers and (if amsmath is loaded) details of the
align environment.

%package -n texlive-dprogress-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn15878
Release:        0
Summary:        Documentation for texlive-dprogress
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dprogress-doc
This package includes the documentation for texlive-dprogress

%post -n texlive-dprogress
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dprogress 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dprogress
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dprogress-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dprogress/README
%{_texmfdistdir}/doc/latex/dprogress/dprogress.pdf

%files -n texlive-dprogress
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dprogress/dprogress.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dprogress-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif

%package -n texlive-drac
Version:        %{texlive_version}.%{texlive_noarch}.1svn15878
Release:        0
Summary:        Declare active character substitution, robustly
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-drac-doc >= %{texlive_version}
Provides:       tex(drac.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source217:      drac.tar.xz
Source218:      drac.doc.tar.xz

%description -n texlive-drac
The package provides macros \DeclareRobustActChar and
\ReDeclareRobActChar. One uses \DeclareRobustActChar in the
same way one would use \DeclareRobustCommand; the macro
\protects the active character when it appears in a moving
argument. \ReDeclareRobActChar redefines an active character
previously defined with \DeclareRobustActChar, in the same way
that \renewcommand works for ordinary commands.

%package -n texlive-drac-doc
Version:        %{texlive_version}.%{texlive_noarch}.1svn15878
Release:        0
Summary:        Documentation for texlive-drac
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-drac-doc:fr;en)

%description -n texlive-drac-doc
This package includes the documentation for texlive-drac

%post -n texlive-drac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-drac 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-drac
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-drac-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/drac/drac-fr.pdf
%{_texmfdistdir}/doc/latex/drac/drac.pdf

%files -n texlive-drac
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/drac/drac.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-drac-%{texlive_version}.%{texlive_noarch}.1svn15878-%{release}-zypper
%endif

%package -n texlive-draftcopy
Version:        %{texlive_version}.%{texlive_noarch}.2.16svn15878
Release:        0
Summary:        Identify draft copies
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-draftcopy-doc >= %{texlive_version}
Provides:       tex(draftcopy.cfg)
Provides:       tex(draftcopy.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source219:      draftcopy.tar.xz
Source220:      draftcopy.doc.tar.xz

%description -n texlive-draftcopy
Places the word DRAFT (or other words) in light grey diagonally
across the background (or at the bottom) of each (or selected)
pages of the document. The package uses PostScript \special
commands, and may not therefore be used with pdfLaTeX. For that
usage, consider the wallpaper or draftwatermark packages.

%package -n texlive-draftcopy-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.16svn15878
Release:        0
Summary:        Documentation for texlive-draftcopy
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-draftcopy-doc
This package includes the documentation for texlive-draftcopy

%post -n texlive-draftcopy
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-draftcopy 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-draftcopy
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-draftcopy-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/draftcopy/README
%{_texmfdistdir}/doc/latex/draftcopy/THIS-IS-VERSION-2.16
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-1.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-10.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-11.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-12.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-13.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-14.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-15.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-16.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-2.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-3.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-4.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-5.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-6.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-7.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-8.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy-test-9.tex
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy.doc
%{_texmfdistdir}/doc/latex/draftcopy/draftcopy.pdf

%files -n texlive-draftcopy
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/draftcopy/draftcopy.cfg
%{_texmfdistdir}/tex/latex/draftcopy/draftcopy.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-draftcopy-%{texlive_version}.%{texlive_noarch}.2.16svn15878-%{release}-zypper
%endif

%package -n texlive-draftfigure
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn44854
Release:        0
Summary:        Replace figures with a white box and additional features
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-draftfigure-doc >= %{texlive_version}
Provides:       tex(draftfigure.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source221:      draftfigure.tar.xz
Source222:      draftfigure.doc.tar.xz

%description -n texlive-draftfigure
With this package you can control the outcome of a figure which
is set to draft and modify the display with various options.

%package -n texlive-draftfigure-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn44854
Release:        0
Summary:        Documentation for texlive-draftfigure
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-draftfigure-doc
This package includes the documentation for texlive-draftfigure

%post -n texlive-draftfigure
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-draftfigure 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-draftfigure
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-draftfigure-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/draftfigure/README.md
%{_texmfdistdir}/doc/latex/draftfigure/draftfigure.pdf
%{_texmfdistdir}/doc/latex/draftfigure/draftfigure.tex

%files -n texlive-draftfigure
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/draftfigure/draftfigure.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-draftfigure-%{texlive_version}.%{texlive_noarch}.0.0.2svn44854-%{release}-zypper
%endif

%package -n texlive-draftwatermark
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn54317
Release:        0
Summary:        Put a grey textual watermark on document pages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-draftwatermark-doc >= %{texlive_version}
Provides:       tex(draftwatermark.sty)
Requires:       tex(color.sty)
Requires:       tex(everypage.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(kvoptions.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source223:      draftwatermark.tar.xz
Source224:      draftwatermark.doc.tar.xz

%description -n texlive-draftwatermark
The package provides a means to add a textual, light grey
watermark on every page or on the first page of a document.
Typical usage may consist in writing words such as DRAFT or
CONFIDENTIAL across document pages. The package performs a
similar function to that of draftcopy, but its implementation
is output device independent, and made very simple by relying
on everypage.

%package -n texlive-draftwatermark-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn54317
Release:        0
Summary:        Documentation for texlive-draftwatermark
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-draftwatermark-doc
This package includes the documentation for texlive-draftwatermark

%post -n texlive-draftwatermark
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-draftwatermark 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-draftwatermark
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-draftwatermark-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/draftwatermark/README
%{_texmfdistdir}/doc/latex/draftwatermark/draftwatermark.pdf
%{_texmfdistdir}/doc/latex/draftwatermark/test_draftwatermark1.tex
%{_texmfdistdir}/doc/latex/draftwatermark/test_draftwatermark2.tex
%{_texmfdistdir}/doc/latex/draftwatermark/test_draftwatermark3.tex
%{_texmfdistdir}/doc/latex/draftwatermark/test_draftwatermark4.tex

%files -n texlive-draftwatermark
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/draftwatermark/draftwatermark.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-draftwatermark-%{texlive_version}.%{texlive_noarch}.2.0svn54317-%{release}-zypper
%endif

%package -n texlive-dramatist
Version:        %{texlive_version}.%{texlive_noarch}.1.2esvn35866
Release:        0
Summary:        Typeset dramas, both in verse and in prose
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
Recommends:     texlive-dramatist-doc >= %{texlive_version}
Provides:       tex(dramatist.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source225:      dramatist.tar.xz
Source226:      dramatist.doc.tar.xz

%description -n texlive-dramatist
This package is intended for typesetting drama of any length.
It provides two environments for typesetting dialogues in prose
or in verse; new document divisions corresponding to acts and
scenes; macros that control the appearance of characters and
stage directions; and automatic generation of a `dramatis
personae' list.

%package -n texlive-dramatist-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2esvn35866
Release:        0
Summary:        Documentation for texlive-dramatist
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dramatist-doc
This package includes the documentation for texlive-dramatist

%post -n texlive-dramatist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dramatist 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dramatist
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dramatist-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dramatist/README
%{_texmfdistdir}/doc/latex/dramatist/dramatist.pdf

%files -n texlive-dramatist
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dramatist/dramatist.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dramatist-%{texlive_version}.%{texlive_noarch}.1.2esvn35866-%{release}-zypper
%endif

%package -n texlive-dratex
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        General drawing macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dratex-doc >= %{texlive_version}
Provides:       tex(AlDraTex.sty)
Provides:       tex(DraTex.sty)
Provides:       tex(TeXProject.sty)
Provides:       tex(wotree.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source227:      dratex.tar.xz
Source228:      dratex.doc.tar.xz

%description -n texlive-dratex
A low level (DraTex.sty) and a high-level (AlDraTex.sty)
drawing package written entirely in TeX.

%package -n texlive-dratex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-dratex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dratex-doc
This package includes the documentation for texlive-dratex

%post -n texlive-dratex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dratex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dratex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dratex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/dratex/Examples.tex
%{_texmfdistdir}/doc/generic/dratex/README

%files -n texlive-dratex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/dratex/AlDraTex.sty
%{_texmfdistdir}/tex/generic/dratex/DraTex.sty
%{_texmfdistdir}/tex/generic/dratex/TeXProject.sty
%{_texmfdistdir}/tex/generic/dratex/wotree.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dratex-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-drawmatrix
Version:        %{texlive_version}.%{texlive_noarch}.1.5.0svn44471
Release:        0
Summary:        Draw visual representations of matrices in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-drawmatrix-doc >= %{texlive_version}
Provides:       tex(drawmatrix.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source229:      drawmatrix.tar.xz
Source230:      drawmatrix.doc.tar.xz

%description -n texlive-drawmatrix
The package provides macros to visually represent matrices.
Various options allow to change the visualizations, e.g.,
drawing rectangular, triangular, or banded matrices.

%package -n texlive-drawmatrix-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5.0svn44471
Release:        0
Summary:        Documentation for texlive-drawmatrix
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-drawmatrix-doc
This package includes the documentation for texlive-drawmatrix

%post -n texlive-drawmatrix
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-drawmatrix 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-drawmatrix
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-drawmatrix-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/drawmatrix/README.md
%{_texmfdistdir}/doc/latex/drawmatrix/drawmatrix.pdf

%files -n texlive-drawmatrix
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/drawmatrix/drawmatrix.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-drawmatrix-%{texlive_version}.%{texlive_noarch}.1.5.0svn44471-%{release}-zypper
%endif

%package -n texlive-drawstack
Version:        %{texlive_version}.%{texlive_noarch}.svn28582
Release:        0
Summary:        Draw execution stacks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-drawstack-doc >= %{texlive_version}
Provides:       tex(drawstack.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(tikz.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source231:      drawstack.tar.xz
Source232:      drawstack.doc.tar.xz

%description -n texlive-drawstack
This simple LaTeX package provides support for drawing
execution stack (typically to illustrate assembly language
notions). The code is written on top of TikZ.

%package -n texlive-drawstack-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn28582
Release:        0
Summary:        Documentation for texlive-drawstack
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-drawstack-doc
This package includes the documentation for texlive-drawstack

%post -n texlive-drawstack
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-drawstack 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-drawstack
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-drawstack-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/drawstack/Makefile
%{_texmfdistdir}/doc/latex/drawstack/README
%{_texmfdistdir}/doc/latex/drawstack/stack-example.pdf
%{_texmfdistdir}/doc/latex/drawstack/stack-example.tex

%files -n texlive-drawstack
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/drawstack/drawstack.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-drawstack-%{texlive_version}.%{texlive_noarch}.svn28582-%{release}-zypper
%endif

%package -n texlive-drm
Version:        %{texlive_version}.%{texlive_noarch}.4.4svn38157
Release:        0
Summary:        A complete family of fonts written in Metafont
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-drm-fonts >= %{texlive_version}
Recommends:     texlive-drm-doc >= %{texlive_version}
Provides:       tex(drm.map)
Provides:       tex(drm.sty)
Provides:       tex(drm10.tfm)
Provides:       tex(drm100.tfm)
Provides:       tex(drm11.tfm)
Provides:       tex(drm12.tfm)
Provides:       tex(drm14.tfm)
Provides:       tex(drm17.tfm)
Provides:       tex(drm24.tfm)
Provides:       tex(drm6.tfm)
Provides:       tex(drm7.tfm)
Provides:       tex(drm8.tfm)
Provides:       tex(drm9.tfm)
Provides:       tex(drmb10.tfm)
Provides:       tex(drmb11.tfm)
Provides:       tex(drmb12.tfm)
Provides:       tex(drmb14.tfm)
Provides:       tex(drmb17.tfm)
Provides:       tex(drmb24.tfm)
Provides:       tex(drmb6.tfm)
Provides:       tex(drmb7.tfm)
Provides:       tex(drmb8.tfm)
Provides:       tex(drmb9.tfm)
Provides:       tex(drmbs10.tfm)
Provides:       tex(drmbx10.tfm)
Provides:       tex(drmbx11.tfm)
Provides:       tex(drmbx12.tfm)
Provides:       tex(drmbx14.tfm)
Provides:       tex(drmbx17.tfm)
Provides:       tex(drmbx24.tfm)
Provides:       tex(drmbx6.tfm)
Provides:       tex(drmbx7.tfm)
Provides:       tex(drmbx8.tfm)
Provides:       tex(drmbx9.tfm)
Provides:       tex(drmdoz10.tfm)
Provides:       tex(drmdoz11.tfm)
Provides:       tex(drmdoz12.tfm)
Provides:       tex(drmdoz14.tfm)
Provides:       tex(drmdoz17.tfm)
Provides:       tex(drmdoz24.tfm)
Provides:       tex(drmdoz6.tfm)
Provides:       tex(drmdoz7.tfm)
Provides:       tex(drmdoz8.tfm)
Provides:       tex(drmdoz9.tfm)
Provides:       tex(drmdozb10.tfm)
Provides:       tex(drmdozb11.tfm)
Provides:       tex(drmdozb12.tfm)
Provides:       tex(drmdozb14.tfm)
Provides:       tex(drmdozb17.tfm)
Provides:       tex(drmdozb24.tfm)
Provides:       tex(drmdozb6.tfm)
Provides:       tex(drmdozb7.tfm)
Provides:       tex(drmdozb8.tfm)
Provides:       tex(drmdozb9.tfm)
Provides:       tex(drmdozbx10.tfm)
Provides:       tex(drmdozbx11.tfm)
Provides:       tex(drmdozbx12.tfm)
Provides:       tex(drmdozbx14.tfm)
Provides:       tex(drmdozbx17.tfm)
Provides:       tex(drmdozbx24.tfm)
Provides:       tex(drmdozbx6.tfm)
Provides:       tex(drmdozbx7.tfm)
Provides:       tex(drmdozbx8.tfm)
Provides:       tex(drmdozbx9.tfm)
Provides:       tex(drmdozit10.tfm)
Provides:       tex(drmdozit11.tfm)
Provides:       tex(drmdozit12.tfm)
Provides:       tex(drmdozit14.tfm)
Provides:       tex(drmdozit17.tfm)
Provides:       tex(drmdozit24.tfm)
Provides:       tex(drmdozit6.tfm)
Provides:       tex(drmdozit7.tfm)
Provides:       tex(drmdozit8.tfm)
Provides:       tex(drmdozit9.tfm)
Provides:       tex(drmdozitbx10.tfm)
Provides:       tex(drmdozitbx11.tfm)
Provides:       tex(drmdozitbx12.tfm)
Provides:       tex(drmdozitbx14.tfm)
Provides:       tex(drmdozitbx17.tfm)
Provides:       tex(drmdozitbx24.tfm)
Provides:       tex(drmdozitbx6.tfm)
Provides:       tex(drmdozitbx7.tfm)
Provides:       tex(drmdozitbx8.tfm)
Provides:       tex(drmdozitbx9.tfm)
Provides:       tex(drmdozitsc10.tfm)
Provides:       tex(drmdozitsc11.tfm)
Provides:       tex(drmdozitsc12.tfm)
Provides:       tex(drmdozitsc14.tfm)
Provides:       tex(drmdozitsc17.tfm)
Provides:       tex(drmdozitsc24.tfm)
Provides:       tex(drmdozitsc6.tfm)
Provides:       tex(drmdozitsc7.tfm)
Provides:       tex(drmdozitsc8.tfm)
Provides:       tex(drmdozitsc9.tfm)
Provides:       tex(drmdozittc10.tfm)
Provides:       tex(drmdozittc11.tfm)
Provides:       tex(drmdozittc12.tfm)
Provides:       tex(drmdozittc14.tfm)
Provides:       tex(drmdozittc17.tfm)
Provides:       tex(drmdozittc24.tfm)
Provides:       tex(drmdozittc6.tfm)
Provides:       tex(drmdozittc7.tfm)
Provides:       tex(drmdozittc8.tfm)
Provides:       tex(drmdozittc9.tfm)
Provides:       tex(drmdozl10.tfm)
Provides:       tex(drmdozl11.tfm)
Provides:       tex(drmdozl12.tfm)
Provides:       tex(drmdozl14.tfm)
Provides:       tex(drmdozl17.tfm)
Provides:       tex(drmdozl24.tfm)
Provides:       tex(drmdozl6.tfm)
Provides:       tex(drmdozl7.tfm)
Provides:       tex(drmdozl8.tfm)
Provides:       tex(drmdozl9.tfm)
Provides:       tex(drmdozsc10.tfm)
Provides:       tex(drmdozsc11.tfm)
Provides:       tex(drmdozsc12.tfm)
Provides:       tex(drmdozsc14.tfm)
Provides:       tex(drmdozsc17.tfm)
Provides:       tex(drmdozsc24.tfm)
Provides:       tex(drmdozsc6.tfm)
Provides:       tex(drmdozsc7.tfm)
Provides:       tex(drmdozsc8.tfm)
Provides:       tex(drmdozsc9.tfm)
Provides:       tex(drmdozscbx10.tfm)
Provides:       tex(drmdozscbx11.tfm)
Provides:       tex(drmdozscbx12.tfm)
Provides:       tex(drmdozscbx14.tfm)
Provides:       tex(drmdozscbx17.tfm)
Provides:       tex(drmdozscbx24.tfm)
Provides:       tex(drmdozscbx6.tfm)
Provides:       tex(drmdozscbx7.tfm)
Provides:       tex(drmdozscbx8.tfm)
Provides:       tex(drmdozscbx9.tfm)
Provides:       tex(drmdozsl10.tfm)
Provides:       tex(drmdozsl11.tfm)
Provides:       tex(drmdozsl12.tfm)
Provides:       tex(drmdozsl14.tfm)
Provides:       tex(drmdozsl17.tfm)
Provides:       tex(drmdozsl24.tfm)
Provides:       tex(drmdozsl6.tfm)
Provides:       tex(drmdozsl7.tfm)
Provides:       tex(drmdozsl8.tfm)
Provides:       tex(drmdozsl9.tfm)
Provides:       tex(drmdoztc10.tfm)
Provides:       tex(drmdoztc11.tfm)
Provides:       tex(drmdoztc12.tfm)
Provides:       tex(drmdoztc14.tfm)
Provides:       tex(drmdoztc17.tfm)
Provides:       tex(drmdoztc24.tfm)
Provides:       tex(drmdoztc6.tfm)
Provides:       tex(drmdoztc7.tfm)
Provides:       tex(drmdoztc8.tfm)
Provides:       tex(drmdoztc9.tfm)
Provides:       tex(drmdoztcbx10.tfm)
Provides:       tex(drmdoztcbx11.tfm)
Provides:       tex(drmdoztcbx12.tfm)
Provides:       tex(drmdoztcbx14.tfm)
Provides:       tex(drmdoztcbx17.tfm)
Provides:       tex(drmdoztcbx24.tfm)
Provides:       tex(drmdoztcbx6.tfm)
Provides:       tex(drmdoztcbx7.tfm)
Provides:       tex(drmdoztcbx8.tfm)
Provides:       tex(drmdoztcbx9.tfm)
Provides:       tex(drmdozui10.tfm)
Provides:       tex(drmdozui11.tfm)
Provides:       tex(drmdozui12.tfm)
Provides:       tex(drmdozui14.tfm)
Provides:       tex(drmdozui17.tfm)
Provides:       tex(drmdozui24.tfm)
Provides:       tex(drmdozui6.tfm)
Provides:       tex(drmdozui7.tfm)
Provides:       tex(drmdozui8.tfm)
Provides:       tex(drmdozui9.tfm)
Provides:       tex(drmdozuibx10.tfm)
Provides:       tex(drmdozuibx11.tfm)
Provides:       tex(drmdozuibx12.tfm)
Provides:       tex(drmdozuibx14.tfm)
Provides:       tex(drmdozuibx17.tfm)
Provides:       tex(drmdozuibx24.tfm)
Provides:       tex(drmdozuibx6.tfm)
Provides:       tex(drmdozuibx7.tfm)
Provides:       tex(drmdozuibx8.tfm)
Provides:       tex(drmdozuibx9.tfm)
Provides:       tex(drmfigs10.tfm)
Provides:       tex(drmfigs11.tfm)
Provides:       tex(drmfigs12.tfm)
Provides:       tex(drmfigs14.tfm)
Provides:       tex(drmfigs17.tfm)
Provides:       tex(drmfigs24.tfm)
Provides:       tex(drmfigs6.tfm)
Provides:       tex(drmfigs7.tfm)
Provides:       tex(drmfigs8.tfm)
Provides:       tex(drmfigs9.tfm)
Provides:       tex(drmgrk10.tfm)
Provides:       tex(drminf10.tfm)
Provides:       tex(drminf11.tfm)
Provides:       tex(drminf12.tfm)
Provides:       tex(drminf14.tfm)
Provides:       tex(drminf17.tfm)
Provides:       tex(drminf24.tfm)
Provides:       tex(drminf6.tfm)
Provides:       tex(drminf7.tfm)
Provides:       tex(drminf8.tfm)
Provides:       tex(drminf9.tfm)
Provides:       tex(drmit10.tfm)
Provides:       tex(drmit11.tfm)
Provides:       tex(drmit12.tfm)
Provides:       tex(drmit14.tfm)
Provides:       tex(drmit17.tfm)
Provides:       tex(drmit24.tfm)
Provides:       tex(drmit6.tfm)
Provides:       tex(drmit7.tfm)
Provides:       tex(drmit8.tfm)
Provides:       tex(drmit9.tfm)
Provides:       tex(drmitbx10.tfm)
Provides:       tex(drmitbx11.tfm)
Provides:       tex(drmitbx12.tfm)
Provides:       tex(drmitbx14.tfm)
Provides:       tex(drmitbx17.tfm)
Provides:       tex(drmitbx24.tfm)
Provides:       tex(drmitbx6.tfm)
Provides:       tex(drmitbx7.tfm)
Provides:       tex(drmitbx8.tfm)
Provides:       tex(drmitbx9.tfm)
Provides:       tex(drmitsc10.tfm)
Provides:       tex(drmitsc11.tfm)
Provides:       tex(drmitsc12.tfm)
Provides:       tex(drmitsc14.tfm)
Provides:       tex(drmitsc17.tfm)
Provides:       tex(drmitsc24.tfm)
Provides:       tex(drmitsc6.tfm)
Provides:       tex(drmitsc7.tfm)
Provides:       tex(drmitsc8.tfm)
Provides:       tex(drmitsc9.tfm)
Provides:       tex(drmittc10.tfm)
Provides:       tex(drmittc11.tfm)
Provides:       tex(drmittc12.tfm)
Provides:       tex(drmittc14.tfm)
Provides:       tex(drmittc17.tfm)
Provides:       tex(drmittc24.tfm)
Provides:       tex(drmittc6.tfm)
Provides:       tex(drmittc7.tfm)
Provides:       tex(drmittc8.tfm)
Provides:       tex(drmittc9.tfm)
Provides:       tex(drml10.tfm)
Provides:       tex(drml11.tfm)
Provides:       tex(drml12.tfm)
Provides:       tex(drml14.tfm)
Provides:       tex(drml17.tfm)
Provides:       tex(drml24.tfm)
Provides:       tex(drml6.tfm)
Provides:       tex(drml7.tfm)
Provides:       tex(drml8.tfm)
Provides:       tex(drml9.tfm)
Provides:       tex(drmmi10.tfm)
Provides:       tex(drmomx10.tfm)
Provides:       tex(drmorns.tfm)
Provides:       tex(drmsc10.tfm)
Provides:       tex(drmsc11.tfm)
Provides:       tex(drmsc12.tfm)
Provides:       tex(drmsc14.tfm)
Provides:       tex(drmsc17.tfm)
Provides:       tex(drmsc24.tfm)
Provides:       tex(drmsc6.tfm)
Provides:       tex(drmsc7.tfm)
Provides:       tex(drmsc8.tfm)
Provides:       tex(drmsc9.tfm)
Provides:       tex(drmscbx10.tfm)
Provides:       tex(drmscbx11.tfm)
Provides:       tex(drmscbx12.tfm)
Provides:       tex(drmscbx14.tfm)
Provides:       tex(drmscbx17.tfm)
Provides:       tex(drmscbx24.tfm)
Provides:       tex(drmscbx6.tfm)
Provides:       tex(drmscbx7.tfm)
Provides:       tex(drmscbx8.tfm)
Provides:       tex(drmscbx9.tfm)
Provides:       tex(drmsl10.tfm)
Provides:       tex(drmsl11.tfm)
Provides:       tex(drmsl12.tfm)
Provides:       tex(drmsl14.tfm)
Provides:       tex(drmsl17.tfm)
Provides:       tex(drmsl24.tfm)
Provides:       tex(drmsl6.tfm)
Provides:       tex(drmsl7.tfm)
Provides:       tex(drmsl8.tfm)
Provides:       tex(drmsl9.tfm)
Provides:       tex(drmsy10.tfm)
Provides:       tex(drmsym10.tfm)
Provides:       tex(drmsym11.tfm)
Provides:       tex(drmsym12.tfm)
Provides:       tex(drmsym14.tfm)
Provides:       tex(drmsym17.tfm)
Provides:       tex(drmsym24.tfm)
Provides:       tex(drmsym7.tfm)
Provides:       tex(drmsym8.tfm)
Provides:       tex(drmsym9.tfm)
Provides:       tex(drmtc10.tfm)
Provides:       tex(drmtc11.tfm)
Provides:       tex(drmtc12.tfm)
Provides:       tex(drmtc14.tfm)
Provides:       tex(drmtc17.tfm)
Provides:       tex(drmtc24.tfm)
Provides:       tex(drmtc6.tfm)
Provides:       tex(drmtc7.tfm)
Provides:       tex(drmtc8.tfm)
Provides:       tex(drmtc9.tfm)
Provides:       tex(drmtcbx10.tfm)
Provides:       tex(drmtcbx11.tfm)
Provides:       tex(drmtcbx12.tfm)
Provides:       tex(drmtcbx14.tfm)
Provides:       tex(drmtcbx17.tfm)
Provides:       tex(drmtcbx24.tfm)
Provides:       tex(drmtcbx6.tfm)
Provides:       tex(drmtcbx7.tfm)
Provides:       tex(drmtcbx8.tfm)
Provides:       tex(drmtcbx9.tfm)
Provides:       tex(drmui10.tfm)
Provides:       tex(drmui11.tfm)
Provides:       tex(drmui12.tfm)
Provides:       tex(drmui14.tfm)
Provides:       tex(drmui17.tfm)
Provides:       tex(drmui24.tfm)
Provides:       tex(drmui6.tfm)
Provides:       tex(drmui7.tfm)
Provides:       tex(drmui8.tfm)
Provides:       tex(drmui9.tfm)
Provides:       tex(drmuibx10.tfm)
Provides:       tex(drmuibx11.tfm)
Provides:       tex(drmuibx12.tfm)
Provides:       tex(drmuibx14.tfm)
Provides:       tex(drmuibx17.tfm)
Provides:       tex(drmuibx24.tfm)
Provides:       tex(drmuibx6.tfm)
Provides:       tex(drmuibx7.tfm)
Provides:       tex(drmuibx8.tfm)
Provides:       tex(drmuibx9.tfm)
Requires:       tex(amsmath.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(gmp.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(modroman.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source233:      drm.tar.xz
Source234:      drm.doc.tar.xz

%description -n texlive-drm
The package provides access to the DRM (Don's Revised Modern)
family of fonts, which includes a variety of optical sizes in
Roman (in four weights), italic, and small caps, among other
shapes, along with a set of symbols and ornaments. It is
intended to be a full-body text font, but its larger sizes can
also be used for simple display purposes, and its significant
body of symbols can stand on its own. It comes complete with
textual ("old-style") and lining figures, and even has
small-caps figures. It also comes with extensible decorative
rules to be used with ornaments from itself or other fonts,
along with an extremely flexible ellipsis package.

%package -n texlive-drm-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.4svn38157
Release:        0
Summary:        Documentation for texlive-drm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-drm-doc
This package includes the documentation for texlive-drm


%package -n texlive-drm-fonts
Version:        %{texlive_version}.%{texlive_noarch}.4.4svn38157
Release:        0
Summary:        Severed fonts for texlive-drm
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-drm-fonts
The  separated fonts package for texlive-drm
%post -n texlive-drm
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-drm 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-drm
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-drm-fonts
%files -n texlive-drm-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/drm/CHANGES
%{_texmfdistdir}/doc/fonts/drm/OFL.txt
%{_texmfdistdir}/doc/fonts/drm/README
%{_texmfdistdir}/doc/fonts/drm/allcomp.sh
%{_texmfdistdir}/doc/fonts/drm/allfonts.sh
%{_texmfdistdir}/doc/fonts/drm/chartscript.sh
%{_texmfdistdir}/doc/fonts/drm/convert.sh
%{_texmfdistdir}/doc/fonts/drm/drm.pdf
%{_texmfdistdir}/doc/fonts/drm/drm_font_tables.pdf
%{_texmfdistdir}/doc/fonts/drm/drmfilelist.txt
%{_texmfdistdir}/doc/fonts/drm/fontconvert.sh
%{_texmfdistdir}/doc/fonts/drm/gpl-3.0.txt
%{_texmfdistdir}/doc/fonts/drm/lppl-1-3c.tex
%{_texmfdistdir}/doc/fonts/drm/ofl_v1-1.tex
%{_texmfdistdir}/doc/fonts/drm/small_specimen.pdf
%{_texmfdistdir}/doc/fonts/drm/small_specimen.tex
%{_texmfdistdir}/doc/fonts/drm/specimen.pdf
%{_texmfdistdir}/doc/fonts/drm/specimen.tex

%files -n texlive-drm
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/drm/drm10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drm9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmb9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoz9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozb9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozit9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozitsc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozittc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozl9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozscbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozsl9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdoztcbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozui9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmdozuibx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmfigs9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmgrk10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drminf9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmit9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmitsc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmittc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drml9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmmi10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmscbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsl9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsy10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmsym9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtc9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmtcbx9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmui9.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx10.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx11.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx12.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx14.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx17.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx24.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx6.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx7.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx8.afm
%{_texmfdistdir}/fonts/afm/public/drm/drmuibx9.afm
%{_texmfdistdir}/fonts/map/dvips/drm/drm.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drm9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmb9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoz9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozb9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozit9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozitsc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozittc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozl9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozscbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozsl9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdoztcbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozui9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmdozuibx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmfigs9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmgrk10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drminf9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmit9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmitsc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmittc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drml9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmmi10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmscbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsl9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsy10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmsym9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtc9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmtcbx9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmui9.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx10.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx11.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx12.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx14.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx17.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx24.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx6.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx7.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx8.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/drm/drmuibx9.otf
%{_texmfdistdir}/fonts/source/public/drm/backslanttest.mf
%{_texmfdistdir}/fonts/source/public/drm/drm.mf
%{_texmfdistdir}/fonts/source/public/drm/drm10.mf
%{_texmfdistdir}/fonts/source/public/drm/drm11.mf
%{_texmfdistdir}/fonts/source/public/drm/drm12.mf
%{_texmfdistdir}/fonts/source/public/drm/drm14.mf
%{_texmfdistdir}/fonts/source/public/drm/drm17.mf
%{_texmfdistdir}/fonts/source/public/drm/drm24.mf
%{_texmfdistdir}/fonts/source/public/drm/drm6.mf
%{_texmfdistdir}/fonts/source/public/drm/drm7.mf
%{_texmfdistdir}/fonts/source/public/drm/drm8.mf
%{_texmfdistdir}/fonts/source/public/drm/drm9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmacc.mf
%{_texmfdistdir}/fonts/source/public/drm/drmacclet.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmb9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmcap.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoz9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozb9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozit9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozitsc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozittc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozl9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozscdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozsl9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdoztcdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozui9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmdozuibx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmfigs9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrk10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrkacc.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrkacclet.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrkcap.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrkligs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrklow.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrkpunct.mf
%{_texmfdistdir}/fonts/source/public/drm/drmgrkup.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf10.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf11.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf12.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf14.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf17.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf24.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf6.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf7.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf8.mf
%{_texmfdistdir}/fonts/source/public/drm/drminf9.mf
%{_texmfdistdir}/fonts/source/public/drm/drminffigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmit9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitacclet.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitcap.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitligs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitlow.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitoldstydigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitpunct.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmitsc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmittc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drml10.mf
%{_texmfdistdir}/fonts/source/public/drm/drml11.mf
%{_texmfdistdir}/fonts/source/public/drm/drml12.mf
%{_texmfdistdir}/fonts/source/public/drm/drml14.mf
%{_texmfdistdir}/fonts/source/public/drm/drml17.mf
%{_texmfdistdir}/fonts/source/public/drm/drml24.mf
%{_texmfdistdir}/fonts/source/public/drm/drml6.mf
%{_texmfdistdir}/fonts/source/public/drm/drml7.mf
%{_texmfdistdir}/fonts/source/public/drm/drml8.mf
%{_texmfdistdir}/fonts/source/public/drm/drml9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmligs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmlow.mf
%{_texmfdistdir}/fonts/source/public/drm/drmlowmac.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmatharrows.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathcal.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathcursell.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathfrac.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathgrklow.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathgrkup.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathheb.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathoms.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathomx.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmathsym.mf
%{_texmfdistdir}/fonts/source/public/drm/drmmi10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmoe.mf
%{_texmfdistdir}/fonts/source/public/drm/drmoldstyfracs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmoldstynums.mf
%{_texmfdistdir}/fonts/source/public/drm/drmomx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmornaments.mf
%{_texmfdistdir}/fonts/source/public/drm/drmornbars.mf
%{_texmfdistdir}/fonts/source/public/drm/drmornfont.mf
%{_texmfdistdir}/fonts/source/public/drm/drmorns.mf
%{_texmfdistdir}/fonts/source/public/drm/drmpunct.mf
%{_texmfdistdir}/fonts/source/public/drm/drmromannums.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscacclet.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscap.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscdol.mf
%{_texmfdistdir}/fonts/source/public/drm/drmscligs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsl9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsupfigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsy10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsym9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmsymbols.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtc9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcacclet.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcap.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcbx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcdigs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcdol.mf
%{_texmfdistdir}/fonts/source/public/drm/drmtcligs.mf
%{_texmfdistdir}/fonts/source/public/drm/drmttcap.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmui9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx10.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx11.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx12.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx14.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx17.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx24.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx6.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx7.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx8.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuibx9.mf
%{_texmfdistdir}/fonts/source/public/drm/drmuiligs.mf
%{_texmfdistdir}/fonts/tfm/public/drm/drm10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm100.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drm9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmb9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbs10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoz9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozb9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozit9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozitsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozittc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozl9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozscbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdoztcbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozui9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmdozuibx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmfigs9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmgrk10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drminf9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmit9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmitsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmittc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drml9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmomx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmorns.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmscbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsy10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmsym9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtc9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmtcbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmui9.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx10.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx11.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx12.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx14.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx17.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx24.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx6.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx7.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx8.tfm
%{_texmfdistdir}/fonts/tfm/public/drm/drmuibx9.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drm9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmb9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoz9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozb9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozit9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozitsc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozittc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozl9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozscbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozsl9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdoztcbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozui9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmdozuibx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmfigs9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmgrk10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drminf9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmit9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmitsc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmittc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drml9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmmi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmscbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsl9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsy10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmsym9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtc9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmtcbx9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmui9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx11.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx14.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx17.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/drm/drmuibx9.pfb
%{_texmfdistdir}/tex/latex/drm/drm.sty

%files -n texlive-drm-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-drm
%{_datadir}/fontconfig/conf.avail/58-texlive-drm.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-drm.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-drm.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-drm/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-drm/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-drm/fonts.scale
%{_datadir}/fonts/texlive-drm/drm10.otf
%{_datadir}/fonts/texlive-drm/drm11.otf
%{_datadir}/fonts/texlive-drm/drm12.otf
%{_datadir}/fonts/texlive-drm/drm14.otf
%{_datadir}/fonts/texlive-drm/drm17.otf
%{_datadir}/fonts/texlive-drm/drm24.otf
%{_datadir}/fonts/texlive-drm/drm6.otf
%{_datadir}/fonts/texlive-drm/drm7.otf
%{_datadir}/fonts/texlive-drm/drm8.otf
%{_datadir}/fonts/texlive-drm/drm9.otf
%{_datadir}/fonts/texlive-drm/drmb10.otf
%{_datadir}/fonts/texlive-drm/drmb11.otf
%{_datadir}/fonts/texlive-drm/drmb12.otf
%{_datadir}/fonts/texlive-drm/drmb14.otf
%{_datadir}/fonts/texlive-drm/drmb17.otf
%{_datadir}/fonts/texlive-drm/drmb24.otf
%{_datadir}/fonts/texlive-drm/drmb6.otf
%{_datadir}/fonts/texlive-drm/drmb7.otf
%{_datadir}/fonts/texlive-drm/drmb8.otf
%{_datadir}/fonts/texlive-drm/drmb9.otf
%{_datadir}/fonts/texlive-drm/drmbx10.otf
%{_datadir}/fonts/texlive-drm/drmbx11.otf
%{_datadir}/fonts/texlive-drm/drmbx12.otf
%{_datadir}/fonts/texlive-drm/drmbx14.otf
%{_datadir}/fonts/texlive-drm/drmbx17.otf
%{_datadir}/fonts/texlive-drm/drmbx24.otf
%{_datadir}/fonts/texlive-drm/drmbx6.otf
%{_datadir}/fonts/texlive-drm/drmbx7.otf
%{_datadir}/fonts/texlive-drm/drmbx8.otf
%{_datadir}/fonts/texlive-drm/drmbx9.otf
%{_datadir}/fonts/texlive-drm/drmdoz10.otf
%{_datadir}/fonts/texlive-drm/drmdoz11.otf
%{_datadir}/fonts/texlive-drm/drmdoz12.otf
%{_datadir}/fonts/texlive-drm/drmdoz14.otf
%{_datadir}/fonts/texlive-drm/drmdoz17.otf
%{_datadir}/fonts/texlive-drm/drmdoz24.otf
%{_datadir}/fonts/texlive-drm/drmdoz6.otf
%{_datadir}/fonts/texlive-drm/drmdoz7.otf
%{_datadir}/fonts/texlive-drm/drmdoz8.otf
%{_datadir}/fonts/texlive-drm/drmdoz9.otf
%{_datadir}/fonts/texlive-drm/drmdozb10.otf
%{_datadir}/fonts/texlive-drm/drmdozb11.otf
%{_datadir}/fonts/texlive-drm/drmdozb12.otf
%{_datadir}/fonts/texlive-drm/drmdozb14.otf
%{_datadir}/fonts/texlive-drm/drmdozb17.otf
%{_datadir}/fonts/texlive-drm/drmdozb24.otf
%{_datadir}/fonts/texlive-drm/drmdozb6.otf
%{_datadir}/fonts/texlive-drm/drmdozb7.otf
%{_datadir}/fonts/texlive-drm/drmdozb8.otf
%{_datadir}/fonts/texlive-drm/drmdozb9.otf
%{_datadir}/fonts/texlive-drm/drmdozbx10.otf
%{_datadir}/fonts/texlive-drm/drmdozbx11.otf
%{_datadir}/fonts/texlive-drm/drmdozbx12.otf
%{_datadir}/fonts/texlive-drm/drmdozbx14.otf
%{_datadir}/fonts/texlive-drm/drmdozbx17.otf
%{_datadir}/fonts/texlive-drm/drmdozbx24.otf
%{_datadir}/fonts/texlive-drm/drmdozbx6.otf
%{_datadir}/fonts/texlive-drm/drmdozbx7.otf
%{_datadir}/fonts/texlive-drm/drmdozbx8.otf
%{_datadir}/fonts/texlive-drm/drmdozbx9.otf
%{_datadir}/fonts/texlive-drm/drmdozit10.otf
%{_datadir}/fonts/texlive-drm/drmdozit11.otf
%{_datadir}/fonts/texlive-drm/drmdozit12.otf
%{_datadir}/fonts/texlive-drm/drmdozit14.otf
%{_datadir}/fonts/texlive-drm/drmdozit17.otf
%{_datadir}/fonts/texlive-drm/drmdozit24.otf
%{_datadir}/fonts/texlive-drm/drmdozit6.otf
%{_datadir}/fonts/texlive-drm/drmdozit7.otf
%{_datadir}/fonts/texlive-drm/drmdozit8.otf
%{_datadir}/fonts/texlive-drm/drmdozit9.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx10.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx11.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx12.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx14.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx17.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx24.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx6.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx7.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx8.otf
%{_datadir}/fonts/texlive-drm/drmdozitbx9.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc10.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc11.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc12.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc14.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc17.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc24.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc6.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc7.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc8.otf
%{_datadir}/fonts/texlive-drm/drmdozitsc9.otf
%{_datadir}/fonts/texlive-drm/drmdozittc10.otf
%{_datadir}/fonts/texlive-drm/drmdozittc11.otf
%{_datadir}/fonts/texlive-drm/drmdozittc12.otf
%{_datadir}/fonts/texlive-drm/drmdozittc14.otf
%{_datadir}/fonts/texlive-drm/drmdozittc17.otf
%{_datadir}/fonts/texlive-drm/drmdozittc24.otf
%{_datadir}/fonts/texlive-drm/drmdozittc6.otf
%{_datadir}/fonts/texlive-drm/drmdozittc7.otf
%{_datadir}/fonts/texlive-drm/drmdozittc8.otf
%{_datadir}/fonts/texlive-drm/drmdozittc9.otf
%{_datadir}/fonts/texlive-drm/drmdozl10.otf
%{_datadir}/fonts/texlive-drm/drmdozl11.otf
%{_datadir}/fonts/texlive-drm/drmdozl12.otf
%{_datadir}/fonts/texlive-drm/drmdozl14.otf
%{_datadir}/fonts/texlive-drm/drmdozl17.otf
%{_datadir}/fonts/texlive-drm/drmdozl24.otf
%{_datadir}/fonts/texlive-drm/drmdozl6.otf
%{_datadir}/fonts/texlive-drm/drmdozl7.otf
%{_datadir}/fonts/texlive-drm/drmdozl8.otf
%{_datadir}/fonts/texlive-drm/drmdozl9.otf
%{_datadir}/fonts/texlive-drm/drmdozsc10.otf
%{_datadir}/fonts/texlive-drm/drmdozsc11.otf
%{_datadir}/fonts/texlive-drm/drmdozsc12.otf
%{_datadir}/fonts/texlive-drm/drmdozsc14.otf
%{_datadir}/fonts/texlive-drm/drmdozsc17.otf
%{_datadir}/fonts/texlive-drm/drmdozsc24.otf
%{_datadir}/fonts/texlive-drm/drmdozsc6.otf
%{_datadir}/fonts/texlive-drm/drmdozsc7.otf
%{_datadir}/fonts/texlive-drm/drmdozsc8.otf
%{_datadir}/fonts/texlive-drm/drmdozsc9.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx10.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx11.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx12.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx14.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx17.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx24.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx6.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx7.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx8.otf
%{_datadir}/fonts/texlive-drm/drmdozscbx9.otf
%{_datadir}/fonts/texlive-drm/drmdozsl10.otf
%{_datadir}/fonts/texlive-drm/drmdozsl11.otf
%{_datadir}/fonts/texlive-drm/drmdozsl12.otf
%{_datadir}/fonts/texlive-drm/drmdozsl14.otf
%{_datadir}/fonts/texlive-drm/drmdozsl17.otf
%{_datadir}/fonts/texlive-drm/drmdozsl24.otf
%{_datadir}/fonts/texlive-drm/drmdozsl6.otf
%{_datadir}/fonts/texlive-drm/drmdozsl7.otf
%{_datadir}/fonts/texlive-drm/drmdozsl8.otf
%{_datadir}/fonts/texlive-drm/drmdozsl9.otf
%{_datadir}/fonts/texlive-drm/drmdoztc10.otf
%{_datadir}/fonts/texlive-drm/drmdoztc11.otf
%{_datadir}/fonts/texlive-drm/drmdoztc12.otf
%{_datadir}/fonts/texlive-drm/drmdoztc14.otf
%{_datadir}/fonts/texlive-drm/drmdoztc17.otf
%{_datadir}/fonts/texlive-drm/drmdoztc24.otf
%{_datadir}/fonts/texlive-drm/drmdoztc6.otf
%{_datadir}/fonts/texlive-drm/drmdoztc7.otf
%{_datadir}/fonts/texlive-drm/drmdoztc8.otf
%{_datadir}/fonts/texlive-drm/drmdoztc9.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx10.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx11.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx12.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx14.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx17.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx24.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx6.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx7.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx8.otf
%{_datadir}/fonts/texlive-drm/drmdoztcbx9.otf
%{_datadir}/fonts/texlive-drm/drmdozui10.otf
%{_datadir}/fonts/texlive-drm/drmdozui11.otf
%{_datadir}/fonts/texlive-drm/drmdozui12.otf
%{_datadir}/fonts/texlive-drm/drmdozui14.otf
%{_datadir}/fonts/texlive-drm/drmdozui17.otf
%{_datadir}/fonts/texlive-drm/drmdozui24.otf
%{_datadir}/fonts/texlive-drm/drmdozui6.otf
%{_datadir}/fonts/texlive-drm/drmdozui7.otf
%{_datadir}/fonts/texlive-drm/drmdozui8.otf
%{_datadir}/fonts/texlive-drm/drmdozui9.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx10.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx11.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx12.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx14.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx17.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx24.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx6.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx7.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx8.otf
%{_datadir}/fonts/texlive-drm/drmdozuibx9.otf
%{_datadir}/fonts/texlive-drm/drmfigs10.otf
%{_datadir}/fonts/texlive-drm/drmfigs11.otf
%{_datadir}/fonts/texlive-drm/drmfigs12.otf
%{_datadir}/fonts/texlive-drm/drmfigs14.otf
%{_datadir}/fonts/texlive-drm/drmfigs17.otf
%{_datadir}/fonts/texlive-drm/drmfigs24.otf
%{_datadir}/fonts/texlive-drm/drmfigs6.otf
%{_datadir}/fonts/texlive-drm/drmfigs7.otf
%{_datadir}/fonts/texlive-drm/drmfigs8.otf
%{_datadir}/fonts/texlive-drm/drmfigs9.otf
%{_datadir}/fonts/texlive-drm/drmgrk10.otf
%{_datadir}/fonts/texlive-drm/drminf10.otf
%{_datadir}/fonts/texlive-drm/drminf11.otf
%{_datadir}/fonts/texlive-drm/drminf12.otf
%{_datadir}/fonts/texlive-drm/drminf14.otf
%{_datadir}/fonts/texlive-drm/drminf17.otf
%{_datadir}/fonts/texlive-drm/drminf24.otf
%{_datadir}/fonts/texlive-drm/drminf6.otf
%{_datadir}/fonts/texlive-drm/drminf7.otf
%{_datadir}/fonts/texlive-drm/drminf8.otf
%{_datadir}/fonts/texlive-drm/drminf9.otf
%{_datadir}/fonts/texlive-drm/drmit10.otf
%{_datadir}/fonts/texlive-drm/drmit11.otf
%{_datadir}/fonts/texlive-drm/drmit12.otf
%{_datadir}/fonts/texlive-drm/drmit14.otf
%{_datadir}/fonts/texlive-drm/drmit17.otf
%{_datadir}/fonts/texlive-drm/drmit24.otf
%{_datadir}/fonts/texlive-drm/drmit6.otf
%{_datadir}/fonts/texlive-drm/drmit7.otf
%{_datadir}/fonts/texlive-drm/drmit8.otf
%{_datadir}/fonts/texlive-drm/drmit9.otf
%{_datadir}/fonts/texlive-drm/drmitbx10.otf
%{_datadir}/fonts/texlive-drm/drmitbx11.otf
%{_datadir}/fonts/texlive-drm/drmitbx12.otf
%{_datadir}/fonts/texlive-drm/drmitbx14.otf
%{_datadir}/fonts/texlive-drm/drmitbx17.otf
%{_datadir}/fonts/texlive-drm/drmitbx24.otf
%{_datadir}/fonts/texlive-drm/drmitbx6.otf
%{_datadir}/fonts/texlive-drm/drmitbx7.otf
%{_datadir}/fonts/texlive-drm/drmitbx8.otf
%{_datadir}/fonts/texlive-drm/drmitbx9.otf
%{_datadir}/fonts/texlive-drm/drmitsc10.otf
%{_datadir}/fonts/texlive-drm/drmitsc11.otf
%{_datadir}/fonts/texlive-drm/drmitsc12.otf
%{_datadir}/fonts/texlive-drm/drmitsc14.otf
%{_datadir}/fonts/texlive-drm/drmitsc17.otf
%{_datadir}/fonts/texlive-drm/drmitsc24.otf
%{_datadir}/fonts/texlive-drm/drmitsc6.otf
%{_datadir}/fonts/texlive-drm/drmitsc7.otf
%{_datadir}/fonts/texlive-drm/drmitsc8.otf
%{_datadir}/fonts/texlive-drm/drmitsc9.otf
%{_datadir}/fonts/texlive-drm/drmittc10.otf
%{_datadir}/fonts/texlive-drm/drmittc11.otf
%{_datadir}/fonts/texlive-drm/drmittc12.otf
%{_datadir}/fonts/texlive-drm/drmittc14.otf
%{_datadir}/fonts/texlive-drm/drmittc17.otf
%{_datadir}/fonts/texlive-drm/drmittc24.otf
%{_datadir}/fonts/texlive-drm/drmittc6.otf
%{_datadir}/fonts/texlive-drm/drmittc7.otf
%{_datadir}/fonts/texlive-drm/drmittc8.otf
%{_datadir}/fonts/texlive-drm/drmittc9.otf
%{_datadir}/fonts/texlive-drm/drml10.otf
%{_datadir}/fonts/texlive-drm/drml11.otf
%{_datadir}/fonts/texlive-drm/drml12.otf
%{_datadir}/fonts/texlive-drm/drml14.otf
%{_datadir}/fonts/texlive-drm/drml17.otf
%{_datadir}/fonts/texlive-drm/drml24.otf
%{_datadir}/fonts/texlive-drm/drml6.otf
%{_datadir}/fonts/texlive-drm/drml7.otf
%{_datadir}/fonts/texlive-drm/drml8.otf
%{_datadir}/fonts/texlive-drm/drml9.otf
%{_datadir}/fonts/texlive-drm/drmmi10.otf
%{_datadir}/fonts/texlive-drm/drmsc10.otf
%{_datadir}/fonts/texlive-drm/drmsc11.otf
%{_datadir}/fonts/texlive-drm/drmsc12.otf
%{_datadir}/fonts/texlive-drm/drmsc14.otf
%{_datadir}/fonts/texlive-drm/drmsc17.otf
%{_datadir}/fonts/texlive-drm/drmsc24.otf
%{_datadir}/fonts/texlive-drm/drmsc6.otf
%{_datadir}/fonts/texlive-drm/drmsc7.otf
%{_datadir}/fonts/texlive-drm/drmsc8.otf
%{_datadir}/fonts/texlive-drm/drmsc9.otf
%{_datadir}/fonts/texlive-drm/drmscbx10.otf
%{_datadir}/fonts/texlive-drm/drmscbx11.otf
%{_datadir}/fonts/texlive-drm/drmscbx12.otf
%{_datadir}/fonts/texlive-drm/drmscbx14.otf
%{_datadir}/fonts/texlive-drm/drmscbx17.otf
%{_datadir}/fonts/texlive-drm/drmscbx24.otf
%{_datadir}/fonts/texlive-drm/drmscbx6.otf
%{_datadir}/fonts/texlive-drm/drmscbx7.otf
%{_datadir}/fonts/texlive-drm/drmscbx8.otf
%{_datadir}/fonts/texlive-drm/drmscbx9.otf
%{_datadir}/fonts/texlive-drm/drmsl10.otf
%{_datadir}/fonts/texlive-drm/drmsl11.otf
%{_datadir}/fonts/texlive-drm/drmsl12.otf
%{_datadir}/fonts/texlive-drm/drmsl14.otf
%{_datadir}/fonts/texlive-drm/drmsl17.otf
%{_datadir}/fonts/texlive-drm/drmsl24.otf
%{_datadir}/fonts/texlive-drm/drmsl6.otf
%{_datadir}/fonts/texlive-drm/drmsl7.otf
%{_datadir}/fonts/texlive-drm/drmsl8.otf
%{_datadir}/fonts/texlive-drm/drmsl9.otf
%{_datadir}/fonts/texlive-drm/drmsy10.otf
%{_datadir}/fonts/texlive-drm/drmsym10.otf
%{_datadir}/fonts/texlive-drm/drmsym11.otf
%{_datadir}/fonts/texlive-drm/drmsym12.otf
%{_datadir}/fonts/texlive-drm/drmsym14.otf
%{_datadir}/fonts/texlive-drm/drmsym17.otf
%{_datadir}/fonts/texlive-drm/drmsym24.otf
%{_datadir}/fonts/texlive-drm/drmsym7.otf
%{_datadir}/fonts/texlive-drm/drmsym8.otf
%{_datadir}/fonts/texlive-drm/drmsym9.otf
%{_datadir}/fonts/texlive-drm/drmtc10.otf
%{_datadir}/fonts/texlive-drm/drmtc11.otf
%{_datadir}/fonts/texlive-drm/drmtc12.otf
%{_datadir}/fonts/texlive-drm/drmtc14.otf
%{_datadir}/fonts/texlive-drm/drmtc17.otf
%{_datadir}/fonts/texlive-drm/drmtc24.otf
%{_datadir}/fonts/texlive-drm/drmtc6.otf
%{_datadir}/fonts/texlive-drm/drmtc7.otf
%{_datadir}/fonts/texlive-drm/drmtc8.otf
%{_datadir}/fonts/texlive-drm/drmtc9.otf
%{_datadir}/fonts/texlive-drm/drmtcbx10.otf
%{_datadir}/fonts/texlive-drm/drmtcbx11.otf
%{_datadir}/fonts/texlive-drm/drmtcbx12.otf
%{_datadir}/fonts/texlive-drm/drmtcbx14.otf
%{_datadir}/fonts/texlive-drm/drmtcbx17.otf
%{_datadir}/fonts/texlive-drm/drmtcbx24.otf
%{_datadir}/fonts/texlive-drm/drmtcbx6.otf
%{_datadir}/fonts/texlive-drm/drmtcbx7.otf
%{_datadir}/fonts/texlive-drm/drmtcbx8.otf
%{_datadir}/fonts/texlive-drm/drmtcbx9.otf
%{_datadir}/fonts/texlive-drm/drmui10.otf
%{_datadir}/fonts/texlive-drm/drmui11.otf
%{_datadir}/fonts/texlive-drm/drmui12.otf
%{_datadir}/fonts/texlive-drm/drmui14.otf
%{_datadir}/fonts/texlive-drm/drmui17.otf
%{_datadir}/fonts/texlive-drm/drmui24.otf
%{_datadir}/fonts/texlive-drm/drmui6.otf
%{_datadir}/fonts/texlive-drm/drmui7.otf
%{_datadir}/fonts/texlive-drm/drmui8.otf
%{_datadir}/fonts/texlive-drm/drmui9.otf
%{_datadir}/fonts/texlive-drm/drmuibx10.otf
%{_datadir}/fonts/texlive-drm/drmuibx11.otf
%{_datadir}/fonts/texlive-drm/drmuibx12.otf
%{_datadir}/fonts/texlive-drm/drmuibx14.otf
%{_datadir}/fonts/texlive-drm/drmuibx17.otf
%{_datadir}/fonts/texlive-drm/drmuibx24.otf
%{_datadir}/fonts/texlive-drm/drmuibx6.otf
%{_datadir}/fonts/texlive-drm/drmuibx7.otf
%{_datadir}/fonts/texlive-drm/drmuibx8.otf
%{_datadir}/fonts/texlive-drm/drmuibx9.otf
%{_datadir}/fonts/texlive-drm/drm10.pfb
%{_datadir}/fonts/texlive-drm/drm11.pfb
%{_datadir}/fonts/texlive-drm/drm12.pfb
%{_datadir}/fonts/texlive-drm/drm14.pfb
%{_datadir}/fonts/texlive-drm/drm17.pfb
%{_datadir}/fonts/texlive-drm/drm24.pfb
%{_datadir}/fonts/texlive-drm/drm6.pfb
%{_datadir}/fonts/texlive-drm/drm7.pfb
%{_datadir}/fonts/texlive-drm/drm8.pfb
%{_datadir}/fonts/texlive-drm/drm9.pfb
%{_datadir}/fonts/texlive-drm/drmb10.pfb
%{_datadir}/fonts/texlive-drm/drmb11.pfb
%{_datadir}/fonts/texlive-drm/drmb12.pfb
%{_datadir}/fonts/texlive-drm/drmb14.pfb
%{_datadir}/fonts/texlive-drm/drmb17.pfb
%{_datadir}/fonts/texlive-drm/drmb24.pfb
%{_datadir}/fonts/texlive-drm/drmb6.pfb
%{_datadir}/fonts/texlive-drm/drmb7.pfb
%{_datadir}/fonts/texlive-drm/drmb8.pfb
%{_datadir}/fonts/texlive-drm/drmb9.pfb
%{_datadir}/fonts/texlive-drm/drmbx10.pfb
%{_datadir}/fonts/texlive-drm/drmbx11.pfb
%{_datadir}/fonts/texlive-drm/drmbx12.pfb
%{_datadir}/fonts/texlive-drm/drmbx14.pfb
%{_datadir}/fonts/texlive-drm/drmbx17.pfb
%{_datadir}/fonts/texlive-drm/drmbx24.pfb
%{_datadir}/fonts/texlive-drm/drmbx6.pfb
%{_datadir}/fonts/texlive-drm/drmbx7.pfb
%{_datadir}/fonts/texlive-drm/drmbx8.pfb
%{_datadir}/fonts/texlive-drm/drmbx9.pfb
%{_datadir}/fonts/texlive-drm/drmdoz10.pfb
%{_datadir}/fonts/texlive-drm/drmdoz11.pfb
%{_datadir}/fonts/texlive-drm/drmdoz12.pfb
%{_datadir}/fonts/texlive-drm/drmdoz14.pfb
%{_datadir}/fonts/texlive-drm/drmdoz17.pfb
%{_datadir}/fonts/texlive-drm/drmdoz24.pfb
%{_datadir}/fonts/texlive-drm/drmdoz6.pfb
%{_datadir}/fonts/texlive-drm/drmdoz7.pfb
%{_datadir}/fonts/texlive-drm/drmdoz8.pfb
%{_datadir}/fonts/texlive-drm/drmdoz9.pfb
%{_datadir}/fonts/texlive-drm/drmdozb10.pfb
%{_datadir}/fonts/texlive-drm/drmdozb11.pfb
%{_datadir}/fonts/texlive-drm/drmdozb12.pfb
%{_datadir}/fonts/texlive-drm/drmdozb14.pfb
%{_datadir}/fonts/texlive-drm/drmdozb17.pfb
%{_datadir}/fonts/texlive-drm/drmdozb24.pfb
%{_datadir}/fonts/texlive-drm/drmdozb6.pfb
%{_datadir}/fonts/texlive-drm/drmdozb7.pfb
%{_datadir}/fonts/texlive-drm/drmdozb8.pfb
%{_datadir}/fonts/texlive-drm/drmdozb9.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx10.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx11.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx12.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx14.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx17.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx24.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx6.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx7.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx8.pfb
%{_datadir}/fonts/texlive-drm/drmdozbx9.pfb
%{_datadir}/fonts/texlive-drm/drmdozit10.pfb
%{_datadir}/fonts/texlive-drm/drmdozit11.pfb
%{_datadir}/fonts/texlive-drm/drmdozit12.pfb
%{_datadir}/fonts/texlive-drm/drmdozit14.pfb
%{_datadir}/fonts/texlive-drm/drmdozit17.pfb
%{_datadir}/fonts/texlive-drm/drmdozit24.pfb
%{_datadir}/fonts/texlive-drm/drmdozit6.pfb
%{_datadir}/fonts/texlive-drm/drmdozit7.pfb
%{_datadir}/fonts/texlive-drm/drmdozit8.pfb
%{_datadir}/fonts/texlive-drm/drmdozit9.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx10.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx11.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx12.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx14.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx17.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx24.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx6.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx7.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx8.pfb
%{_datadir}/fonts/texlive-drm/drmdozitbx9.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc10.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc11.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc12.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc14.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc17.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc24.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc6.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc7.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc8.pfb
%{_datadir}/fonts/texlive-drm/drmdozitsc9.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc10.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc11.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc12.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc14.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc17.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc24.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc6.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc7.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc8.pfb
%{_datadir}/fonts/texlive-drm/drmdozittc9.pfb
%{_datadir}/fonts/texlive-drm/drmdozl10.pfb
%{_datadir}/fonts/texlive-drm/drmdozl11.pfb
%{_datadir}/fonts/texlive-drm/drmdozl12.pfb
%{_datadir}/fonts/texlive-drm/drmdozl14.pfb
%{_datadir}/fonts/texlive-drm/drmdozl17.pfb
%{_datadir}/fonts/texlive-drm/drmdozl24.pfb
%{_datadir}/fonts/texlive-drm/drmdozl6.pfb
%{_datadir}/fonts/texlive-drm/drmdozl7.pfb
%{_datadir}/fonts/texlive-drm/drmdozl8.pfb
%{_datadir}/fonts/texlive-drm/drmdozl9.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc10.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc11.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc12.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc14.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc17.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc24.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc6.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc7.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc8.pfb
%{_datadir}/fonts/texlive-drm/drmdozsc9.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx10.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx11.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx12.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx14.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx17.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx24.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx6.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx7.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx8.pfb
%{_datadir}/fonts/texlive-drm/drmdozscbx9.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl10.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl11.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl12.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl14.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl17.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl24.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl6.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl7.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl8.pfb
%{_datadir}/fonts/texlive-drm/drmdozsl9.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc10.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc11.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc12.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc14.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc17.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc24.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc6.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc7.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc8.pfb
%{_datadir}/fonts/texlive-drm/drmdoztc9.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx10.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx11.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx12.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx14.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx17.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx24.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx6.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx7.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx8.pfb
%{_datadir}/fonts/texlive-drm/drmdoztcbx9.pfb
%{_datadir}/fonts/texlive-drm/drmdozui10.pfb
%{_datadir}/fonts/texlive-drm/drmdozui11.pfb
%{_datadir}/fonts/texlive-drm/drmdozui12.pfb
%{_datadir}/fonts/texlive-drm/drmdozui14.pfb
%{_datadir}/fonts/texlive-drm/drmdozui17.pfb
%{_datadir}/fonts/texlive-drm/drmdozui24.pfb
%{_datadir}/fonts/texlive-drm/drmdozui6.pfb
%{_datadir}/fonts/texlive-drm/drmdozui7.pfb
%{_datadir}/fonts/texlive-drm/drmdozui8.pfb
%{_datadir}/fonts/texlive-drm/drmdozui9.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx10.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx11.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx12.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx14.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx17.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx24.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx6.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx7.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx8.pfb
%{_datadir}/fonts/texlive-drm/drmdozuibx9.pfb
%{_datadir}/fonts/texlive-drm/drmfigs10.pfb
%{_datadir}/fonts/texlive-drm/drmfigs11.pfb
%{_datadir}/fonts/texlive-drm/drmfigs12.pfb
%{_datadir}/fonts/texlive-drm/drmfigs14.pfb
%{_datadir}/fonts/texlive-drm/drmfigs17.pfb
%{_datadir}/fonts/texlive-drm/drmfigs24.pfb
%{_datadir}/fonts/texlive-drm/drmfigs6.pfb
%{_datadir}/fonts/texlive-drm/drmfigs7.pfb
%{_datadir}/fonts/texlive-drm/drmfigs8.pfb
%{_datadir}/fonts/texlive-drm/drmfigs9.pfb
%{_datadir}/fonts/texlive-drm/drmgrk10.pfb
%{_datadir}/fonts/texlive-drm/drminf10.pfb
%{_datadir}/fonts/texlive-drm/drminf11.pfb
%{_datadir}/fonts/texlive-drm/drminf12.pfb
%{_datadir}/fonts/texlive-drm/drminf14.pfb
%{_datadir}/fonts/texlive-drm/drminf17.pfb
%{_datadir}/fonts/texlive-drm/drminf24.pfb
%{_datadir}/fonts/texlive-drm/drminf6.pfb
%{_datadir}/fonts/texlive-drm/drminf7.pfb
%{_datadir}/fonts/texlive-drm/drminf8.pfb
%{_datadir}/fonts/texlive-drm/drminf9.pfb
%{_datadir}/fonts/texlive-drm/drmit10.pfb
%{_datadir}/fonts/texlive-drm/drmit11.pfb
%{_datadir}/fonts/texlive-drm/drmit12.pfb
%{_datadir}/fonts/texlive-drm/drmit14.pfb
%{_datadir}/fonts/texlive-drm/drmit17.pfb
%{_datadir}/fonts/texlive-drm/drmit24.pfb
%{_datadir}/fonts/texlive-drm/drmit6.pfb
%{_datadir}/fonts/texlive-drm/drmit7.pfb
%{_datadir}/fonts/texlive-drm/drmit8.pfb
%{_datadir}/fonts/texlive-drm/drmit9.pfb
%{_datadir}/fonts/texlive-drm/drmitbx10.pfb
%{_datadir}/fonts/texlive-drm/drmitbx11.pfb
%{_datadir}/fonts/texlive-drm/drmitbx12.pfb
%{_datadir}/fonts/texlive-drm/drmitbx14.pfb
%{_datadir}/fonts/texlive-drm/drmitbx17.pfb
%{_datadir}/fonts/texlive-drm/drmitbx24.pfb
%{_datadir}/fonts/texlive-drm/drmitbx6.pfb
%{_datadir}/fonts/texlive-drm/drmitbx7.pfb
%{_datadir}/fonts/texlive-drm/drmitbx8.pfb
%{_datadir}/fonts/texlive-drm/drmitbx9.pfb
%{_datadir}/fonts/texlive-drm/drmitsc10.pfb
%{_datadir}/fonts/texlive-drm/drmitsc11.pfb
%{_datadir}/fonts/texlive-drm/drmitsc12.pfb
%{_datadir}/fonts/texlive-drm/drmitsc14.pfb
%{_datadir}/fonts/texlive-drm/drmitsc17.pfb
%{_datadir}/fonts/texlive-drm/drmitsc24.pfb
%{_datadir}/fonts/texlive-drm/drmitsc6.pfb
%{_datadir}/fonts/texlive-drm/drmitsc7.pfb
%{_datadir}/fonts/texlive-drm/drmitsc8.pfb
%{_datadir}/fonts/texlive-drm/drmitsc9.pfb
%{_datadir}/fonts/texlive-drm/drmittc10.pfb
%{_datadir}/fonts/texlive-drm/drmittc11.pfb
%{_datadir}/fonts/texlive-drm/drmittc12.pfb
%{_datadir}/fonts/texlive-drm/drmittc14.pfb
%{_datadir}/fonts/texlive-drm/drmittc17.pfb
%{_datadir}/fonts/texlive-drm/drmittc24.pfb
%{_datadir}/fonts/texlive-drm/drmittc6.pfb
%{_datadir}/fonts/texlive-drm/drmittc7.pfb
%{_datadir}/fonts/texlive-drm/drmittc8.pfb
%{_datadir}/fonts/texlive-drm/drmittc9.pfb
%{_datadir}/fonts/texlive-drm/drml10.pfb
%{_datadir}/fonts/texlive-drm/drml11.pfb
%{_datadir}/fonts/texlive-drm/drml12.pfb
%{_datadir}/fonts/texlive-drm/drml14.pfb
%{_datadir}/fonts/texlive-drm/drml17.pfb
%{_datadir}/fonts/texlive-drm/drml24.pfb
%{_datadir}/fonts/texlive-drm/drml6.pfb
%{_datadir}/fonts/texlive-drm/drml7.pfb
%{_datadir}/fonts/texlive-drm/drml8.pfb
%{_datadir}/fonts/texlive-drm/drml9.pfb
%{_datadir}/fonts/texlive-drm/drmmi10.pfb
%{_datadir}/fonts/texlive-drm/drmsc10.pfb
%{_datadir}/fonts/texlive-drm/drmsc11.pfb
%{_datadir}/fonts/texlive-drm/drmsc12.pfb
%{_datadir}/fonts/texlive-drm/drmsc14.pfb
%{_datadir}/fonts/texlive-drm/drmsc17.pfb
%{_datadir}/fonts/texlive-drm/drmsc24.pfb
%{_datadir}/fonts/texlive-drm/drmsc6.pfb
%{_datadir}/fonts/texlive-drm/drmsc7.pfb
%{_datadir}/fonts/texlive-drm/drmsc8.pfb
%{_datadir}/fonts/texlive-drm/drmsc9.pfb
%{_datadir}/fonts/texlive-drm/drmscbx10.pfb
%{_datadir}/fonts/texlive-drm/drmscbx11.pfb
%{_datadir}/fonts/texlive-drm/drmscbx12.pfb
%{_datadir}/fonts/texlive-drm/drmscbx14.pfb
%{_datadir}/fonts/texlive-drm/drmscbx17.pfb
%{_datadir}/fonts/texlive-drm/drmscbx24.pfb
%{_datadir}/fonts/texlive-drm/drmscbx6.pfb
%{_datadir}/fonts/texlive-drm/drmscbx7.pfb
%{_datadir}/fonts/texlive-drm/drmscbx8.pfb
%{_datadir}/fonts/texlive-drm/drmscbx9.pfb
%{_datadir}/fonts/texlive-drm/drmsl10.pfb
%{_datadir}/fonts/texlive-drm/drmsl11.pfb
%{_datadir}/fonts/texlive-drm/drmsl12.pfb
%{_datadir}/fonts/texlive-drm/drmsl14.pfb
%{_datadir}/fonts/texlive-drm/drmsl17.pfb
%{_datadir}/fonts/texlive-drm/drmsl24.pfb
%{_datadir}/fonts/texlive-drm/drmsl6.pfb
%{_datadir}/fonts/texlive-drm/drmsl7.pfb
%{_datadir}/fonts/texlive-drm/drmsl8.pfb
%{_datadir}/fonts/texlive-drm/drmsl9.pfb
%{_datadir}/fonts/texlive-drm/drmsy10.pfb
%{_datadir}/fonts/texlive-drm/drmsym10.pfb
%{_datadir}/fonts/texlive-drm/drmsym11.pfb
%{_datadir}/fonts/texlive-drm/drmsym12.pfb
%{_datadir}/fonts/texlive-drm/drmsym14.pfb
%{_datadir}/fonts/texlive-drm/drmsym17.pfb
%{_datadir}/fonts/texlive-drm/drmsym24.pfb
%{_datadir}/fonts/texlive-drm/drmsym7.pfb
%{_datadir}/fonts/texlive-drm/drmsym8.pfb
%{_datadir}/fonts/texlive-drm/drmsym9.pfb
%{_datadir}/fonts/texlive-drm/drmtc10.pfb
%{_datadir}/fonts/texlive-drm/drmtc11.pfb
%{_datadir}/fonts/texlive-drm/drmtc12.pfb
%{_datadir}/fonts/texlive-drm/drmtc14.pfb
%{_datadir}/fonts/texlive-drm/drmtc17.pfb
%{_datadir}/fonts/texlive-drm/drmtc24.pfb
%{_datadir}/fonts/texlive-drm/drmtc6.pfb
%{_datadir}/fonts/texlive-drm/drmtc7.pfb
%{_datadir}/fonts/texlive-drm/drmtc8.pfb
%{_datadir}/fonts/texlive-drm/drmtc9.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx10.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx11.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx12.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx14.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx17.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx24.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx6.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx7.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx8.pfb
%{_datadir}/fonts/texlive-drm/drmtcbx9.pfb
%{_datadir}/fonts/texlive-drm/drmui10.pfb
%{_datadir}/fonts/texlive-drm/drmui11.pfb
%{_datadir}/fonts/texlive-drm/drmui12.pfb
%{_datadir}/fonts/texlive-drm/drmui14.pfb
%{_datadir}/fonts/texlive-drm/drmui17.pfb
%{_datadir}/fonts/texlive-drm/drmui24.pfb
%{_datadir}/fonts/texlive-drm/drmui6.pfb
%{_datadir}/fonts/texlive-drm/drmui7.pfb
%{_datadir}/fonts/texlive-drm/drmui8.pfb
%{_datadir}/fonts/texlive-drm/drmui9.pfb
%{_datadir}/fonts/texlive-drm/drmuibx10.pfb
%{_datadir}/fonts/texlive-drm/drmuibx11.pfb
%{_datadir}/fonts/texlive-drm/drmuibx12.pfb
%{_datadir}/fonts/texlive-drm/drmuibx14.pfb
%{_datadir}/fonts/texlive-drm/drmuibx17.pfb
%{_datadir}/fonts/texlive-drm/drmuibx24.pfb
%{_datadir}/fonts/texlive-drm/drmuibx6.pfb
%{_datadir}/fonts/texlive-drm/drmuibx7.pfb
%{_datadir}/fonts/texlive-drm/drmuibx8.pfb
%{_datadir}/fonts/texlive-drm/drmuibx9.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-drm-fonts-%{texlive_version}.%{texlive_noarch}.4.4svn38157-%{release}-zypper
%endif

%package -n texlive-droid
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn54512
Release:        0
Summary:        LaTeX support for the Droid font families
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
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
Requires:       texlive-droid-fonts >= %{texlive_version}
Recommends:     texlive-droid-doc >= %{texlive_version}
Provides:       tex(DroidSans-Bold-LGR--base.tfm)
Provides:       tex(DroidSans-Bold-LGR-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-LGR-Slanted.tfm)
Provides:       tex(DroidSans-Bold-LGR-Slanted.vf)
Provides:       tex(DroidSans-Bold-LGR.tfm)
Provides:       tex(DroidSans-Bold-LGR.vf)
Provides:       tex(DroidSans-Bold-OT1--base.tfm)
Provides:       tex(DroidSans-Bold-OT1-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-OT1-Slanted.tfm)
Provides:       tex(DroidSans-Bold-OT1-Slanted.vf)
Provides:       tex(DroidSans-Bold-OT1.tfm)
Provides:       tex(DroidSans-Bold-OT1.vf)
Provides:       tex(DroidSans-Bold-T1--base.tfm)
Provides:       tex(DroidSans-Bold-T1-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-T1-Slanted.tfm)
Provides:       tex(DroidSans-Bold-T1-Slanted.vf)
Provides:       tex(DroidSans-Bold-T1.tfm)
Provides:       tex(DroidSans-Bold-T1.vf)
Provides:       tex(DroidSans-Bold-T2A--base.tfm)
Provides:       tex(DroidSans-Bold-T2A-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-T2A-Slanted.tfm)
Provides:       tex(DroidSans-Bold-T2A-Slanted.vf)
Provides:       tex(DroidSans-Bold-T2A.tfm)
Provides:       tex(DroidSans-Bold-T2A.vf)
Provides:       tex(DroidSans-Bold-T2B--base.tfm)
Provides:       tex(DroidSans-Bold-T2B-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-T2B-Slanted.tfm)
Provides:       tex(DroidSans-Bold-T2B-Slanted.vf)
Provides:       tex(DroidSans-Bold-T2B.tfm)
Provides:       tex(DroidSans-Bold-T2B.vf)
Provides:       tex(DroidSans-Bold-T2C--base.tfm)
Provides:       tex(DroidSans-Bold-T2C-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-T2C-Slanted.tfm)
Provides:       tex(DroidSans-Bold-T2C-Slanted.vf)
Provides:       tex(DroidSans-Bold-T2C.tfm)
Provides:       tex(DroidSans-Bold-T2C.vf)
Provides:       tex(DroidSans-Bold-TS1--base.tfm)
Provides:       tex(DroidSans-Bold-TS1-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-TS1-Slanted.tfm)
Provides:       tex(DroidSans-Bold-TS1-Slanted.vf)
Provides:       tex(DroidSans-Bold-TS1.tfm)
Provides:       tex(DroidSans-Bold-TS1.vf)
Provides:       tex(DroidSans-Bold-X2--base.tfm)
Provides:       tex(DroidSans-Bold-X2-Slanted--base.tfm)
Provides:       tex(DroidSans-Bold-X2-Slanted.tfm)
Provides:       tex(DroidSans-Bold-X2-Slanted.vf)
Provides:       tex(DroidSans-Bold-X2.tfm)
Provides:       tex(DroidSans-Bold-X2.vf)
Provides:       tex(DroidSans-LGR--base.tfm)
Provides:       tex(DroidSans-LGR-Slanted--base.tfm)
Provides:       tex(DroidSans-LGR-Slanted.tfm)
Provides:       tex(DroidSans-LGR-Slanted.vf)
Provides:       tex(DroidSans-LGR.tfm)
Provides:       tex(DroidSans-LGR.vf)
Provides:       tex(DroidSans-OT1--base.tfm)
Provides:       tex(DroidSans-OT1-Slanted--base.tfm)
Provides:       tex(DroidSans-OT1-Slanted.tfm)
Provides:       tex(DroidSans-OT1-Slanted.vf)
Provides:       tex(DroidSans-OT1.tfm)
Provides:       tex(DroidSans-OT1.vf)
Provides:       tex(DroidSans-T1--base.tfm)
Provides:       tex(DroidSans-T1-Slanted--base.tfm)
Provides:       tex(DroidSans-T1-Slanted.tfm)
Provides:       tex(DroidSans-T1-Slanted.vf)
Provides:       tex(DroidSans-T1.tfm)
Provides:       tex(DroidSans-T1.vf)
Provides:       tex(DroidSans-T2A--base.tfm)
Provides:       tex(DroidSans-T2A-Slanted--base.tfm)
Provides:       tex(DroidSans-T2A-Slanted.tfm)
Provides:       tex(DroidSans-T2A-Slanted.vf)
Provides:       tex(DroidSans-T2A.tfm)
Provides:       tex(DroidSans-T2A.vf)
Provides:       tex(DroidSans-T2B--base.tfm)
Provides:       tex(DroidSans-T2B-Slanted--base.tfm)
Provides:       tex(DroidSans-T2B-Slanted.tfm)
Provides:       tex(DroidSans-T2B-Slanted.vf)
Provides:       tex(DroidSans-T2B.tfm)
Provides:       tex(DroidSans-T2B.vf)
Provides:       tex(DroidSans-T2C--base.tfm)
Provides:       tex(DroidSans-T2C-Slanted--base.tfm)
Provides:       tex(DroidSans-T2C-Slanted.tfm)
Provides:       tex(DroidSans-T2C-Slanted.vf)
Provides:       tex(DroidSans-T2C.tfm)
Provides:       tex(DroidSans-T2C.vf)
Provides:       tex(DroidSans-TS1--base.tfm)
Provides:       tex(DroidSans-TS1-Slanted--base.tfm)
Provides:       tex(DroidSans-TS1-Slanted.tfm)
Provides:       tex(DroidSans-TS1-Slanted.vf)
Provides:       tex(DroidSans-TS1.tfm)
Provides:       tex(DroidSans-TS1.vf)
Provides:       tex(DroidSans-X2--base.tfm)
Provides:       tex(DroidSans-X2-Slanted--base.tfm)
Provides:       tex(DroidSans-X2-Slanted.tfm)
Provides:       tex(DroidSans-X2-Slanted.vf)
Provides:       tex(DroidSans-X2.tfm)
Provides:       tex(DroidSans-X2.vf)
Provides:       tex(DroidSansMono-LGR--base.tfm)
Provides:       tex(DroidSansMono-LGR-Slanted--base.tfm)
Provides:       tex(DroidSansMono-LGR-Slanted.tfm)
Provides:       tex(DroidSansMono-LGR-Slanted.vf)
Provides:       tex(DroidSansMono-LGR.tfm)
Provides:       tex(DroidSansMono-LGR.vf)
Provides:       tex(DroidSansMono-OT1--base.tfm)
Provides:       tex(DroidSansMono-OT1-Slanted--base.tfm)
Provides:       tex(DroidSansMono-OT1-Slanted.tfm)
Provides:       tex(DroidSansMono-OT1-Slanted.vf)
Provides:       tex(DroidSansMono-OT1.tfm)
Provides:       tex(DroidSansMono-OT1.vf)
Provides:       tex(DroidSansMono-T1--base.tfm)
Provides:       tex(DroidSansMono-T1-Slanted--base.tfm)
Provides:       tex(DroidSansMono-T1-Slanted.tfm)
Provides:       tex(DroidSansMono-T1-Slanted.vf)
Provides:       tex(DroidSansMono-T1.tfm)
Provides:       tex(DroidSansMono-T1.vf)
Provides:       tex(DroidSansMono-T2A--base.tfm)
Provides:       tex(DroidSansMono-T2A-Slanted--base.tfm)
Provides:       tex(DroidSansMono-T2A-Slanted.tfm)
Provides:       tex(DroidSansMono-T2A-Slanted.vf)
Provides:       tex(DroidSansMono-T2A.tfm)
Provides:       tex(DroidSansMono-T2A.vf)
Provides:       tex(DroidSansMono-T2B--base.tfm)
Provides:       tex(DroidSansMono-T2B-Slanted--base.tfm)
Provides:       tex(DroidSansMono-T2B-Slanted.tfm)
Provides:       tex(DroidSansMono-T2B-Slanted.vf)
Provides:       tex(DroidSansMono-T2B.tfm)
Provides:       tex(DroidSansMono-T2B.vf)
Provides:       tex(DroidSansMono-T2C--base.tfm)
Provides:       tex(DroidSansMono-T2C-Slanted--base.tfm)
Provides:       tex(DroidSansMono-T2C-Slanted.tfm)
Provides:       tex(DroidSansMono-T2C-Slanted.vf)
Provides:       tex(DroidSansMono-T2C.tfm)
Provides:       tex(DroidSansMono-T2C.vf)
Provides:       tex(DroidSansMono-TS1--base.tfm)
Provides:       tex(DroidSansMono-TS1-Slanted--base.tfm)
Provides:       tex(DroidSansMono-TS1-Slanted.tfm)
Provides:       tex(DroidSansMono-TS1-Slanted.vf)
Provides:       tex(DroidSansMono-TS1.tfm)
Provides:       tex(DroidSansMono-TS1.vf)
Provides:       tex(DroidSansMono-X2--base.tfm)
Provides:       tex(DroidSansMono-X2-Slanted--base.tfm)
Provides:       tex(DroidSansMono-X2-Slanted.tfm)
Provides:       tex(DroidSansMono-X2-Slanted.vf)
Provides:       tex(DroidSansMono-X2.tfm)
Provides:       tex(DroidSansMono-X2.vf)
Provides:       tex(DroidSerif-Bold-LGR-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-LGR.tfm)
Provides:       tex(DroidSerif-Bold-OT1--base.tfm)
Provides:       tex(DroidSerif-Bold-OT1-Slanted--base.tfm)
Provides:       tex(DroidSerif-Bold-OT1-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-OT1-Slanted.vf)
Provides:       tex(DroidSerif-Bold-OT1.tfm)
Provides:       tex(DroidSerif-Bold-OT1.vf)
Provides:       tex(DroidSerif-Bold-T1--base.tfm)
Provides:       tex(DroidSerif-Bold-T1-Slanted--base.tfm)
Provides:       tex(DroidSerif-Bold-T1-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-T1-Slanted.vf)
Provides:       tex(DroidSerif-Bold-T1.tfm)
Provides:       tex(DroidSerif-Bold-T1.vf)
Provides:       tex(DroidSerif-Bold-T2A--base.tfm)
Provides:       tex(DroidSerif-Bold-T2A-Slanted--base.tfm)
Provides:       tex(DroidSerif-Bold-T2A-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-T2A-Slanted.vf)
Provides:       tex(DroidSerif-Bold-T2A.tfm)
Provides:       tex(DroidSerif-Bold-T2A.vf)
Provides:       tex(DroidSerif-Bold-T2B--base.tfm)
Provides:       tex(DroidSerif-Bold-T2B-Slanted--base.tfm)
Provides:       tex(DroidSerif-Bold-T2B-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-T2B-Slanted.vf)
Provides:       tex(DroidSerif-Bold-T2B.tfm)
Provides:       tex(DroidSerif-Bold-T2B.vf)
Provides:       tex(DroidSerif-Bold-T2C--base.tfm)
Provides:       tex(DroidSerif-Bold-T2C-Slanted--base.tfm)
Provides:       tex(DroidSerif-Bold-T2C-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-T2C-Slanted.vf)
Provides:       tex(DroidSerif-Bold-T2C.tfm)
Provides:       tex(DroidSerif-Bold-T2C.vf)
Provides:       tex(DroidSerif-Bold-TS1--base.tfm)
Provides:       tex(DroidSerif-Bold-TS1-Slanted--base.tfm)
Provides:       tex(DroidSerif-Bold-TS1-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-TS1-Slanted.vf)
Provides:       tex(DroidSerif-Bold-TS1.tfm)
Provides:       tex(DroidSerif-Bold-TS1.vf)
Provides:       tex(DroidSerif-Bold-X2--base.tfm)
Provides:       tex(DroidSerif-Bold-X2-Slanted--base.tfm)
Provides:       tex(DroidSerif-Bold-X2-Slanted.tfm)
Provides:       tex(DroidSerif-Bold-X2-Slanted.vf)
Provides:       tex(DroidSerif-Bold-X2.tfm)
Provides:       tex(DroidSerif-Bold-X2.vf)
Provides:       tex(DroidSerif-BoldItalic-LGR-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-LGR.tfm)
Provides:       tex(DroidSerif-BoldItalic-OT1--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-OT1-Upright--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-OT1-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-OT1-Upright.vf)
Provides:       tex(DroidSerif-BoldItalic-OT1.tfm)
Provides:       tex(DroidSerif-BoldItalic-OT1.vf)
Provides:       tex(DroidSerif-BoldItalic-T1--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T1-Upright--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T1-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-T1-Upright.vf)
Provides:       tex(DroidSerif-BoldItalic-T1.tfm)
Provides:       tex(DroidSerif-BoldItalic-T1.vf)
Provides:       tex(DroidSerif-BoldItalic-T2A--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2A-Upright--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2A-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2A-Upright.vf)
Provides:       tex(DroidSerif-BoldItalic-T2A.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2A.vf)
Provides:       tex(DroidSerif-BoldItalic-T2B--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2B-Upright--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2B-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2B-Upright.vf)
Provides:       tex(DroidSerif-BoldItalic-T2B.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2B.vf)
Provides:       tex(DroidSerif-BoldItalic-T2C--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2C-Upright--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2C-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2C-Upright.vf)
Provides:       tex(DroidSerif-BoldItalic-T2C.tfm)
Provides:       tex(DroidSerif-BoldItalic-T2C.vf)
Provides:       tex(DroidSerif-BoldItalic-TS1--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-TS1-Upright--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-TS1-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-TS1-Upright.vf)
Provides:       tex(DroidSerif-BoldItalic-TS1.tfm)
Provides:       tex(DroidSerif-BoldItalic-TS1.vf)
Provides:       tex(DroidSerif-BoldItalic-X2--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-X2-Upright--base.tfm)
Provides:       tex(DroidSerif-BoldItalic-X2-Upright.tfm)
Provides:       tex(DroidSerif-BoldItalic-X2-Upright.vf)
Provides:       tex(DroidSerif-BoldItalic-X2.tfm)
Provides:       tex(DroidSerif-BoldItalic-X2.vf)
Provides:       tex(DroidSerif-Italic-LGR-Upright.tfm)
Provides:       tex(DroidSerif-Italic-LGR.tfm)
Provides:       tex(DroidSerif-Italic-OT1--base.tfm)
Provides:       tex(DroidSerif-Italic-OT1-Upright--base.tfm)
Provides:       tex(DroidSerif-Italic-OT1-Upright.tfm)
Provides:       tex(DroidSerif-Italic-OT1-Upright.vf)
Provides:       tex(DroidSerif-Italic-OT1.tfm)
Provides:       tex(DroidSerif-Italic-OT1.vf)
Provides:       tex(DroidSerif-Italic-T1--base.tfm)
Provides:       tex(DroidSerif-Italic-T1-Upright--base.tfm)
Provides:       tex(DroidSerif-Italic-T1-Upright.tfm)
Provides:       tex(DroidSerif-Italic-T1-Upright.vf)
Provides:       tex(DroidSerif-Italic-T1.tfm)
Provides:       tex(DroidSerif-Italic-T1.vf)
Provides:       tex(DroidSerif-Italic-T2A--base.tfm)
Provides:       tex(DroidSerif-Italic-T2A-Upright--base.tfm)
Provides:       tex(DroidSerif-Italic-T2A-Upright.tfm)
Provides:       tex(DroidSerif-Italic-T2A-Upright.vf)
Provides:       tex(DroidSerif-Italic-T2A.tfm)
Provides:       tex(DroidSerif-Italic-T2A.vf)
Provides:       tex(DroidSerif-Italic-T2B--base.tfm)
Provides:       tex(DroidSerif-Italic-T2B-Upright--base.tfm)
Provides:       tex(DroidSerif-Italic-T2B-Upright.tfm)
Provides:       tex(DroidSerif-Italic-T2B-Upright.vf)
Provides:       tex(DroidSerif-Italic-T2B.tfm)
Provides:       tex(DroidSerif-Italic-T2B.vf)
Provides:       tex(DroidSerif-Italic-T2C--base.tfm)
Provides:       tex(DroidSerif-Italic-T2C-Upright--base.tfm)
Provides:       tex(DroidSerif-Italic-T2C-Upright.tfm)
Provides:       tex(DroidSerif-Italic-T2C-Upright.vf)
Provides:       tex(DroidSerif-Italic-T2C.tfm)
Provides:       tex(DroidSerif-Italic-T2C.vf)
Provides:       tex(DroidSerif-Italic-TS1--base.tfm)
Provides:       tex(DroidSerif-Italic-TS1-Upright--base.tfm)
Provides:       tex(DroidSerif-Italic-TS1-Upright.tfm)
Provides:       tex(DroidSerif-Italic-TS1-Upright.vf)
Provides:       tex(DroidSerif-Italic-TS1.tfm)
Provides:       tex(DroidSerif-Italic-TS1.vf)
Provides:       tex(DroidSerif-Italic-X2--base.tfm)
Provides:       tex(DroidSerif-Italic-X2-Upright--base.tfm)
Provides:       tex(DroidSerif-Italic-X2-Upright.tfm)
Provides:       tex(DroidSerif-Italic-X2-Upright.vf)
Provides:       tex(DroidSerif-Italic-X2.tfm)
Provides:       tex(DroidSerif-Italic-X2.vf)
Provides:       tex(DroidSerif-Regular-LGR-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-LGR.tfm)
Provides:       tex(DroidSerif-Regular-OT1--base.tfm)
Provides:       tex(DroidSerif-Regular-OT1-Slanted--base.tfm)
Provides:       tex(DroidSerif-Regular-OT1-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-OT1-Slanted.vf)
Provides:       tex(DroidSerif-Regular-OT1.tfm)
Provides:       tex(DroidSerif-Regular-OT1.vf)
Provides:       tex(DroidSerif-Regular-T1--base.tfm)
Provides:       tex(DroidSerif-Regular-T1-Slanted--base.tfm)
Provides:       tex(DroidSerif-Regular-T1-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-T1-Slanted.vf)
Provides:       tex(DroidSerif-Regular-T1.tfm)
Provides:       tex(DroidSerif-Regular-T1.vf)
Provides:       tex(DroidSerif-Regular-T2A--base.tfm)
Provides:       tex(DroidSerif-Regular-T2A-Slanted--base.tfm)
Provides:       tex(DroidSerif-Regular-T2A-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-T2A-Slanted.vf)
Provides:       tex(DroidSerif-Regular-T2A.tfm)
Provides:       tex(DroidSerif-Regular-T2A.vf)
Provides:       tex(DroidSerif-Regular-T2B--base.tfm)
Provides:       tex(DroidSerif-Regular-T2B-Slanted--base.tfm)
Provides:       tex(DroidSerif-Regular-T2B-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-T2B-Slanted.vf)
Provides:       tex(DroidSerif-Regular-T2B.tfm)
Provides:       tex(DroidSerif-Regular-T2B.vf)
Provides:       tex(DroidSerif-Regular-T2C--base.tfm)
Provides:       tex(DroidSerif-Regular-T2C-Slanted--base.tfm)
Provides:       tex(DroidSerif-Regular-T2C-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-T2C-Slanted.vf)
Provides:       tex(DroidSerif-Regular-T2C.tfm)
Provides:       tex(DroidSerif-Regular-T2C.vf)
Provides:       tex(DroidSerif-Regular-TS1--base.tfm)
Provides:       tex(DroidSerif-Regular-TS1-Slanted--base.tfm)
Provides:       tex(DroidSerif-Regular-TS1-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-TS1-Slanted.vf)
Provides:       tex(DroidSerif-Regular-TS1.tfm)
Provides:       tex(DroidSerif-Regular-TS1.vf)
Provides:       tex(DroidSerif-Regular-X2--base.tfm)
Provides:       tex(DroidSerif-Regular-X2-Slanted--base.tfm)
Provides:       tex(DroidSerif-Regular-X2-Slanted.tfm)
Provides:       tex(DroidSerif-Regular-X2-Slanted.vf)
Provides:       tex(DroidSerif-Regular-X2.tfm)
Provides:       tex(DroidSerif-Regular-X2.vf)
Provides:       tex(LGRdroidsans.fd)
Provides:       tex(LGRdroidsansmono.fd)
Provides:       tex(LGRdroidserif.fd)
Provides:       tex(OT1droidsans.fd)
Provides:       tex(OT1droidsansmono.fd)
Provides:       tex(OT1droidserif.fd)
Provides:       tex(T1droidsans.fd)
Provides:       tex(T1droidsansmono.fd)
Provides:       tex(T1droidserif.fd)
Provides:       tex(T2Adroidsans.fd)
Provides:       tex(T2Adroidsansmono.fd)
Provides:       tex(T2Adroidserif.fd)
Provides:       tex(T2Bdroidsans.fd)
Provides:       tex(T2Bdroidsansmono.fd)
Provides:       tex(T2Bdroidserif.fd)
Provides:       tex(T2Cdroidsans.fd)
Provides:       tex(T2Cdroidsansmono.fd)
Provides:       tex(T2Cdroidserif.fd)
Provides:       tex(TS1droidsans.fd)
Provides:       tex(TS1droidsansmono.fd)
Provides:       tex(TS1droidserif.fd)
Provides:       tex(X2droidsans.fd)
Provides:       tex(X2droidsansmono.fd)
Provides:       tex(X2droidserif.fd)
Provides:       tex(a_55mctf.enc)
Provides:       tex(a_6t6vor.enc)
Provides:       tex(a_7xkq4l.enc)
Provides:       tex(a_atrmj4.enc)
Provides:       tex(a_auqje4.enc)
Provides:       tex(a_dhbph5.enc)
Provides:       tex(a_es3zal.enc)
Provides:       tex(a_gyeryq.enc)
Provides:       tex(a_hyyrer.enc)
Provides:       tex(a_i77vuw.enc)
Provides:       tex(a_joxy3n.enc)
Provides:       tex(a_k2ku5j.enc)
Provides:       tex(a_l5aj6z.enc)
Provides:       tex(a_lzb5hy.enc)
Provides:       tex(a_nm2gjd.enc)
Provides:       tex(a_nwf7uv.enc)
Provides:       tex(a_slcnpg.enc)
Provides:       tex(a_vtfkvv.enc)
Provides:       tex(a_w466e2.enc)
Provides:       tex(a_xgvdme.enc)
Provides:       tex(a_zpgv3j.enc)
Provides:       tex(droid.sty)
Provides:       tex(droidsans.map)
Provides:       tex(droidsans.sty)
Provides:       tex(droidsansmono.map)
Provides:       tex(droidsansmono.sty)
Provides:       tex(droidserif.map)
Provides:       tex(droidserif.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source235:      droid.tar.xz
Source236:      droid.doc.tar.xz

%description -n texlive-droid
The Droid typeface family was designed in the fall of 2006 by
Steve Matteson, as a commission from Google to create a set of
system fonts for its Android platform. The goal was to provide
optimal quality and comfort on a mobile handset when rendered
in application menus, web browsers and for other screen text.
The Droid family consists of Droid Serif, Droid Sans and Droid
Sans Mono fonts, licensed under the Apache License Version 2.0.
The bundle includes the fonts in both TrueType and Adobe Type 1
formats. The package does not support the Droid Pro family of
fonts, available for purchase from the Ascender foundry.

%package -n texlive-droid-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn54512
Release:        0
Summary:        Documentation for texlive-droid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-droid-doc
This package includes the documentation for texlive-droid


%package -n texlive-droid-fonts
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn54512
Release:        0
Summary:        Severed fonts for texlive-droid
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-droid-fonts
The  separated fonts package for texlive-droid
%post -n texlive-droid
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap droidsans.map' >> /var/run/texlive/run-updmap
echo 'addMap droidsansmono.map' >> /var/run/texlive/run-updmap
echo 'addMap droidserif.map' >> /var/run/texlive/run-updmap

%postun -n texlive-droid 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap droidsans.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap droidsansmono.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap droidserif.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-droid
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-droid-fonts
%files -n texlive-droid-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/droid/CHANGES
%{_texmfdistdir}/doc/fonts/droid/README
%{_texmfdistdir}/doc/fonts/droid/droid-samples.pdf
%{_texmfdistdir}/doc/fonts/droid/droid.pdf

%files -n texlive-droid
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/droid/a_55mctf.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_6t6vor.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_7xkq4l.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_atrmj4.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_auqje4.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_dhbph5.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_es3zal.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_gyeryq.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_hyyrer.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_i77vuw.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_joxy3n.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_k2ku5j.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_l5aj6z.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_lzb5hy.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_nm2gjd.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_nwf7uv.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_slcnpg.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_vtfkvv.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_w466e2.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_xgvdme.enc
%{_texmfdistdir}/fonts/enc/dvips/droid/a_zpgv3j.enc
%{_texmfdistdir}/fonts/map/dvips/droid/droidsans.map
%{_texmfdistdir}/fonts/map/dvips/droid/droidsansmono.map
%{_texmfdistdir}/fonts/map/dvips/droid/droidserif.map
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-LGR--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-LGR-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-LGR-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-LGR.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-OT1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-OT1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-OT1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-OT1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2A--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2A-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2A-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2A.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2B--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2B-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2B-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2B.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2C--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2C-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2C-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-T2C.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-TS1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-TS1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-TS1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-TS1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-X2--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-X2-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-X2-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-Bold-X2.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-LGR--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-LGR-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-LGR-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-LGR.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-OT1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-OT1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-OT1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-OT1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2A--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2A-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2A-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2A.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2B--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2B-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2B-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2B.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2C--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2C-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2C-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-T2C.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-TS1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-TS1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-TS1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-TS1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-X2--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-X2-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-X2-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsans/DroidSans-X2.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-LGR--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-LGR-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-LGR-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-LGR.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-OT1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-OT1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-OT1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-OT1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2A--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2A-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2A-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2A.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2B--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2B-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2B-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2B.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2C--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2C-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2C-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-T2C.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-TS1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-TS1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-TS1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-TS1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-X2--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-X2-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-X2-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidsansmono/DroidSansMono-X2.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-LGR-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-LGR.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-OT1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-OT1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-OT1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-OT1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2A--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2A-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2A-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2A.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2B--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2B-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2B-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2B.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2C--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2C-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2C-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-T2C.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-TS1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-TS1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-TS1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-TS1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-X2--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-X2-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-X2-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Bold-X2.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-LGR-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-LGR.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-OT1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-OT1-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-OT1-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-OT1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T1-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T1-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2A--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2A-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2A-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2A.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2B--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2B-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2B-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2B.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2C--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2C-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2C-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-T2C.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-TS1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-TS1-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-TS1-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-TS1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-X2--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-X2-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-X2-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-BoldItalic-X2.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-LGR-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-LGR.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-OT1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-OT1-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-OT1-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-OT1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T1-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T1-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2A--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2A-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2A-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2A.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2B--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2B-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2B-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2B.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2C--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2C-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2C-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-T2C.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-TS1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-TS1-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-TS1-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-TS1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-X2--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-X2-Upright--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-X2-Upright.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Italic-X2.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-LGR-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-LGR.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-OT1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-OT1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-OT1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-OT1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2A--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2A-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2A-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2A.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2B--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2B-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2B-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2B.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2C--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2C-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2C-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-T2C.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-TS1--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-TS1-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-TS1-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-TS1.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-X2--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-X2-Slanted--base.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-X2-Slanted.tfm
%{_texmfdistdir}/fonts/tfm/ascender/droid/droidserif/DroidSerif-Regular-X2.tfm
%verify(link) %{_texmfdistdir}/fonts/truetype/ascender/droid/droidsans/DroidSans-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/ascender/droid/droidsans/DroidSans.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/ascender/droid/droidsansmono/DroidSansMono.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/ascender/droid/droidserif/DroidSerif-Bold.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/ascender/droid/droidserif/DroidSerif-BoldItalic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/ascender/droid/droidserif/DroidSerif-Italic.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/ascender/droid/droidserif/DroidSerif-Regular.ttf
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidsans/DroidSans-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidsans/DroidSans.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidsansmono/DroidSansMono.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidserif/DroidSerif-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidserif/DroidSerif-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidserif/DroidSerif-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidserif/DroidSerif-Regular.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/ascender/droid/droidserif/DroidSerif.pfb
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-LGR-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-LGR.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-OT1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-OT1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T2A-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T2A.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T2B-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T2B.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T2C-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-T2C.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-TS1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-TS1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-X2-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-Bold-X2.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-LGR-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-LGR.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-OT1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-OT1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T2A-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T2A.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T2B-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T2B.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T2C-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-T2C.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-TS1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-TS1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-X2-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsans/DroidSans-X2.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-LGR-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-LGR.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-OT1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-OT1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T2A-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T2A.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T2B-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T2B.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T2C-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-T2C.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-TS1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-TS1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-X2-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidsansmono/DroidSansMono-X2.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-OT1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-OT1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T2A-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T2A.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T2B-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T2B.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T2C-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-T2C.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-TS1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-TS1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-X2-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Bold-X2.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-OT1-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-OT1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T1-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T2A-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T2A.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T2B-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T2B.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T2C-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-T2C.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-TS1-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-TS1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-X2-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-BoldItalic-X2.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-OT1-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-OT1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T1-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T2A-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T2A.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T2B-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T2B.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T2C-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-T2C.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-TS1-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-TS1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-X2-Upright.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Italic-X2.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-OT1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-OT1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T2A-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T2A.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T2B-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T2B.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T2C-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-T2C.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-TS1-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-TS1.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-X2-Slanted.vf
%{_texmfdistdir}/fonts/vf/ascender/droid/droidserif/DroidSerif-Regular-X2.vf
%{_texmfdistdir}/tex/latex/droid/LGRdroidsans.fd
%{_texmfdistdir}/tex/latex/droid/LGRdroidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/LGRdroidserif.fd
%{_texmfdistdir}/tex/latex/droid/OT1droidsans.fd
%{_texmfdistdir}/tex/latex/droid/OT1droidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/OT1droidserif.fd
%{_texmfdistdir}/tex/latex/droid/T1droidsans.fd
%{_texmfdistdir}/tex/latex/droid/T1droidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/T1droidserif.fd
%{_texmfdistdir}/tex/latex/droid/T2Adroidsans.fd
%{_texmfdistdir}/tex/latex/droid/T2Adroidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/T2Adroidserif.fd
%{_texmfdistdir}/tex/latex/droid/T2Bdroidsans.fd
%{_texmfdistdir}/tex/latex/droid/T2Bdroidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/T2Bdroidserif.fd
%{_texmfdistdir}/tex/latex/droid/T2Cdroidsans.fd
%{_texmfdistdir}/tex/latex/droid/T2Cdroidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/T2Cdroidserif.fd
%{_texmfdistdir}/tex/latex/droid/TS1droidsans.fd
%{_texmfdistdir}/tex/latex/droid/TS1droidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/TS1droidserif.fd
%{_texmfdistdir}/tex/latex/droid/X2droidsans.fd
%{_texmfdistdir}/tex/latex/droid/X2droidsansmono.fd
%{_texmfdistdir}/tex/latex/droid/X2droidserif.fd
%{_texmfdistdir}/tex/latex/droid/droid.sty
%{_texmfdistdir}/tex/latex/droid/droidsans.sty
%{_texmfdistdir}/tex/latex/droid/droidsansmono.sty
%{_texmfdistdir}/tex/latex/droid/droidserif.sty

%files -n texlive-droid-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-droid
%{_datadir}/fontconfig/conf.avail/58-texlive-droid.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-droid.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-droid.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-droid/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-droid/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-droid/fonts.scale
%{_datadir}/fonts/texlive-droid/DroidSans-Bold.ttf
%{_datadir}/fonts/texlive-droid/DroidSans.ttf
%{_datadir}/fonts/texlive-droid/DroidSansMono.ttf
%{_datadir}/fonts/texlive-droid/DroidSerif-Bold.ttf
%{_datadir}/fonts/texlive-droid/DroidSerif-BoldItalic.ttf
%{_datadir}/fonts/texlive-droid/DroidSerif-Italic.ttf
%{_datadir}/fonts/texlive-droid/DroidSerif-Regular.ttf
%{_datadir}/fonts/texlive-droid/DroidSans-Bold.pfb
%{_datadir}/fonts/texlive-droid/DroidSans.pfb
%{_datadir}/fonts/texlive-droid/DroidSansMono.pfb
%{_datadir}/fonts/texlive-droid/DroidSerif-Bold.pfb
%{_datadir}/fonts/texlive-droid/DroidSerif-BoldItalic.pfb
%{_datadir}/fonts/texlive-droid/DroidSerif-Italic.pfb
%{_datadir}/fonts/texlive-droid/DroidSerif-Regular.pfb
%{_datadir}/fonts/texlive-droid/DroidSerif.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-droid-fonts-%{texlive_version}.%{texlive_noarch}.3.2svn54512-%{release}-zypper
%endif

%package -n texlive-droit-fr
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn39802
Release:        0
Summary:        Document class and bibliographic style for French law
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-droit-fr-doc >= %{texlive_version}
Provides:       tex(droit-fr.bbx)
Provides:       tex(droit-fr.cbx)
Provides:       tex(droit-fr.cls)
Requires:       tex(babel.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(engrec.sty)
Requires:       tex(filecontents.sty)
Requires:       tex(footmisc.sty)
Requires:       tex(ifdraft.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(refcount.sty)
Requires:       tex(verbose-ibid.bbx)
Requires:       tex(verbose-ibid.cbx)
Requires:       tex(xifthen.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source237:      droit-fr.tar.xz
Source238:      droit-fr.doc.tar.xz

%description -n texlive-droit-fr
The bundle provides a toolkit intended for students writing a
thesis in French law. It features: a LaTeX document class; a
bibliographic style for BibLaTeX package; a practical example
of french thesis document; and documentation. The class assumes
use of biber and BibLaTeX.

%package -n texlive-droit-fr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2svn39802
Release:        0
Summary:        Documentation for texlive-droit-fr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-droit-fr-doc:fr)

%description -n texlive-droit-fr-doc
This package includes the documentation for texlive-droit-fr

%post -n texlive-droit-fr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-droit-fr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-droit-fr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-droit-fr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/droit-fr/droit-fr.pdf
%{_texmfdistdir}/doc/latex/droit-fr/droit-fr.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/annexes.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/bibliographie.bib
%{_texmfdistdir}/doc/latex/droit-fr/example/bibliographie.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/conclusion.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/glossaire.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/index.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/introduction.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/journaux.bib
%{_texmfdistdir}/doc/latex/droit-fr/example/latexmkrc
%{_texmfdistdir}/doc/latex/droit-fr/example/main.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/misc.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/partie1.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/partie2.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/resume.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/sommaire.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/titre.tex
%{_texmfdistdir}/doc/latex/droit-fr/example/toc.tex
%{_texmfdistdir}/doc/latex/droit-fr/latexmkrc

%files -n texlive-droit-fr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/droit-fr/droit-fr.bbx
%{_texmfdistdir}/tex/latex/droit-fr/droit-fr.cbx
%{_texmfdistdir}/tex/latex/droit-fr/droit-fr.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-droit-fr-%{texlive_version}.%{texlive_noarch}.1.2svn39802-%{release}-zypper
%endif

%package -n texlive-drs
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn19232
Release:        0
Summary:        Typeset Discourse Representation Structures (DRS)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-drs-doc >= %{texlive_version}
Provides:       tex(drs.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source239:      drs.tar.xz
Source240:      drs.doc.tar.xz

%description -n texlive-drs
The package draws Discourse Representation Structures (DRSs).
It can draw embedded DRSs, if-then conditions and
quantificational "duplex conditions" (with a properly scaled
connecting diamond). Formatting parameters allow the user to
control the appearance and placement of DRSs, and of DRS
variables and conditions. The package is based on DRS macros in
the covington package.

%package -n texlive-drs-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1bsvn19232
Release:        0
Summary:        Documentation for texlive-drs
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-drs-doc
This package includes the documentation for texlive-drs

%post -n texlive-drs
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-drs 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-drs
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-drs-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/drs/README
%{_texmfdistdir}/doc/latex/drs/drsdoc.pdf
%{_texmfdistdir}/doc/latex/drs/drsdoc.tex

%files -n texlive-drs
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/drs/drs.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-drs-%{texlive_version}.%{texlive_noarch}.1.1bsvn19232-%{release}-zypper
%endif

%package -n texlive-drv
Version:        %{texlive_version}.%{texlive_noarch}.0.0.97svn29349
Release:        0
Summary:        Derivation trees with MetaPost
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-drv-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source241:      drv.tar.xz
Source242:      drv.doc.tar.xz

%description -n texlive-drv
A set of MetaPost macros for typesetting derivation trees (such
as used in sequent calculus, type inference, programming
language semantics...). No MetaPost knowledge is needed to use
these macros.

%package -n texlive-drv-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.97svn29349
Release:        0
Summary:        Documentation for texlive-drv
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-drv-doc
This package includes the documentation for texlive-drv

%post -n texlive-drv
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-drv 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-drv
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-drv-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/drv/README
%{_texmfdistdir}/doc/metapost/drv/doc/drv-guide.mp
%{_texmfdistdir}/doc/metapost/drv/doc/drv-guide.tex
%{_texmfdistdir}/doc/metapost/drv/doc/drv.mp
%{_texmfdistdir}/doc/metapost/drv/doc/makefile
%{_texmfdistdir}/doc/metapost/drv/doc/readme.sh
%{_texmfdistdir}/doc/metapost/drv/drv-guide.pdf
%{_texmfdistdir}/doc/metapost/drv/sample/coq-sample.mp
%{_texmfdistdir}/doc/metapost/drv/sample/coq-sample.tex
%{_texmfdistdir}/doc/metapost/drv/sample/drv.mp
%{_texmfdistdir}/doc/metapost/drv/sample/makefile
%{_texmfdistdir}/doc/metapost/drv/sample/readme.sh
%{_texmfdistdir}/doc/metapost/drv/template/drv.mp
%{_texmfdistdir}/doc/metapost/drv/template/makefile
%{_texmfdistdir}/doc/metapost/drv/template/readme.sh
%{_texmfdistdir}/doc/metapost/drv/template/template.mp
%{_texmfdistdir}/doc/metapost/drv/template/template.tex

%files -n texlive-drv
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/drv/drv.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-drv-%{texlive_version}.%{texlive_noarch}.0.0.97svn29349-%{release}-zypper
%endif

%package -n texlive-dsptricks
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn34724
Release:        0
Summary:        Macros for Digital Signal Processing plots
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dsptricks-doc >= %{texlive_version}
Provides:       tex(dspblocks.sty)
Provides:       tex(dspfunctions.sty)
Provides:       tex(dsptricks.sty)
Requires:       tex(calc.sty)
Requires:       tex(fmtcount.sty)
Requires:       tex(fp.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(pst-xkey.sty)
Requires:       tex(pstricks-add.sty)
Requires:       tex(pstricks.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source243:      dsptricks.tar.xz
Source244:      dsptricks.doc.tar.xz

%description -n texlive-dsptricks
The package provides a set of LaTeX macros (based on PSTricks)
for plotting the kind of graphs and figures that are usually
employed in digital signal processing publications. DSPTricks
provides facilities for standard discrete-time "lollipop"
plots, continuous-time and frequency plots, and pole-zero
plots. The companion package DSPFunctions (dspfunctions.sty)
provides macros for computing frequency responses and DFTs,
while the package DSPBlocks (dspblocks.sty) supports DSP block
diagrams.

%package -n texlive-dsptricks-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn34724
Release:        0
Summary:        Documentation for texlive-dsptricks
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dsptricks-doc
This package includes the documentation for texlive-dsptricks

%post -n texlive-dsptricks
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dsptricks 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dsptricks
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dsptricks-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dsptricks/README
%{_texmfdistdir}/doc/latex/dsptricks/dspTricksManual.pdf
%{_texmfdistdir}/doc/latex/dsptricks/dspTricksManual.tex

%files -n texlive-dsptricks
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dsptricks/dspblocks.sty
%{_texmfdistdir}/tex/latex/dsptricks/dspfunctions.sty
%{_texmfdistdir}/tex/latex/dsptricks/dsptricks.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dsptricks-%{texlive_version}.%{texlive_noarch}.1.0svn34724-%{release}-zypper
%endif

%package -n texlive-dsserif
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn54512
Release:        0
Summary:        A double-struck serifed font for mathematical use
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
Requires:       texlive-dsserif-fonts >= %{texlive_version}
Recommends:     texlive-dsserif-doc >= %{texlive_version}
Provides:       tex(DSSerif-Bold.tfm)
Provides:       tex(DSSerif.map)
Provides:       tex(DSSerif.tfm)
Provides:       tex(DSSerifUni-Bold.tfm)
Provides:       tex(DSSerifUni.tfm)
Provides:       tex(dsserif.sty)
Provides:       tex(udsserif.fd)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source245:      dsserif.tar.xz
Source246:      dsserif.doc.tar.xz

%description -n texlive-dsserif
DSSerif is a mathematical font package with double struck
serifed digits, upper and lower case letters, in regular and
bold weights. The design was inspired by the STIX double struck
fonts, which are sans serif, but starting from a Courier-like
base.

%package -n texlive-dsserif-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn54512
Release:        0
Summary:        Documentation for texlive-dsserif
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dsserif-doc
This package includes the documentation for texlive-dsserif


%package -n texlive-dsserif-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.01svn54512
Release:        0
Summary:        Severed fonts for texlive-dsserif
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-dsserif-fonts
The  separated fonts package for texlive-dsserif
%post -n texlive-dsserif
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap DSSerif.map' >> /var/run/texlive/run-updmap

%postun -n texlive-dsserif 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap DSSerif.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-dsserif
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-dsserif-fonts
%files -n texlive-dsserif-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dsserif/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/dsserif/OFL.txt
%{_texmfdistdir}/doc/fonts/dsserif/README
%{_texmfdistdir}/doc/fonts/dsserif/dsserif-doc.pdf
%{_texmfdistdir}/doc/fonts/dsserif/dsserif-doc.tex

%files -n texlive-dsserif
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/dsserif/DSSerif-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dsserif/DSSerif.afm
%{_texmfdistdir}/fonts/afm/public/dsserif/DSSerifUni-Bold.afm
%{_texmfdistdir}/fonts/afm/public/dsserif/DSSerifUni.afm
%{_texmfdistdir}/fonts/map/dvips/dsserif/DSSerif.map
%{_texmfdistdir}/fonts/tfm/public/dsserif/DSSerif-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/dsserif/DSSerif.tfm
%{_texmfdistdir}/fonts/tfm/public/dsserif/DSSerifUni-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/dsserif/DSSerifUni.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dsserif/DSSerif-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dsserif/DSSerif.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dsserif/DSSerifUni-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dsserif/DSSerifUni.pfb
%{_texmfdistdir}/tex/latex/dsserif/dsserif.sty
%{_texmfdistdir}/tex/latex/dsserif/udsserif.fd

%files -n texlive-dsserif-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-dsserif
%{_datadir}/fontconfig/conf.avail/58-texlive-dsserif.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dsserif/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dsserif/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dsserif/fonts.scale
%{_datadir}/fonts/texlive-dsserif/DSSerif-Bold.pfb
%{_datadir}/fonts/texlive-dsserif/DSSerif.pfb
%{_datadir}/fonts/texlive-dsserif/DSSerifUni-Bold.pfb
%{_datadir}/fonts/texlive-dsserif/DSSerifUni.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dsserif-fonts-%{texlive_version}.%{texlive_noarch}.1.01svn54512-%{release}-zypper
%endif

%package -n texlive-dtk
Version:        %{texlive_version}.%{texlive_noarch}.2.08gsvn54080
Release:        0
Summary:        Document class for the journal of DANTE
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dtk-doc >= %{texlive_version}
Provides:       tex(dtk-author.clo)
Provides:       tex(dtk-extern.sty)
Provides:       tex(dtk-full.clo)
Provides:       tex(dtk-logos.sty)
Provides:       tex(dtk-new-engines.clo)
Provides:       tex(dtk-old-engines.clo)
Provides:       tex(dtk-url.sty)
Provides:       tex(dtk.bbx)
Provides:       tex(dtk.cbx)
Provides:       tex(dtk.cls)
Requires:       tex(AnonymousPro.sty)
Requires:       tex(atveryend.sty)
Requires:       tex(babel.sty)
Requires:       tex(chem-angew.bbx)
Requires:       tex(csquotes.sty)
Requires:       tex(dantelogo.sty)
Requires:       tex(datetime2.sty)
Requires:       tex(embedfile.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(eurosym.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(fetamont.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hvqrurl.sty)
Requires:       tex(hyphsubst.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifvtex.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(libertine.sty)
Requires:       tex(libertinus-otf.sty)
Requires:       tex(listings.sty)
Requires:       tex(lstautogobble.sty)
Requires:       tex(luatex85.sty)
Requires:       tex(marginnote.sty)
Requires:       tex(multicol.sty)
Requires:       tex(newunicodechar.sty)
Requires:       tex(numeric.cbx)
Requires:       tex(pdfescape.sty)
Requires:       tex(picture.sty)
Requires:       tex(ragged2e.sty)
Requires:       tex(scrhack.sty)
Requires:       tex(scrlayer-scrpage.sty)
Requires:       tex(selnolig.sty)
Requires:       tex(shellesc.sty)
Requires:       tex(splitidx.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(trimspaces.sty)
Requires:       tex(unicode-math.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source247:      dtk.tar.xz
Source248:      dtk.doc.tar.xz

%description -n texlive-dtk
The bundle provides a class and style file for typesetting "Die
TeXnische Komodie" -- the communications of the German TeX
Users Group DANTE e.V. The arrangement means that the class may
be used by article writers to typeset a single article, as well
as to produce the complete journal.

%package -n texlive-dtk-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.08gsvn54080
Release:        0
Summary:        Documentation for texlive-dtk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-dtk-doc:de)

%description -n texlive-dtk-doc
This package includes the documentation for texlive-dtk

%post -n texlive-dtk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dtk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dtk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dtk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dtk/README.md
%{_texmfdistdir}/doc/latex/dtk/doc/beispiel.bib
%{_texmfdistdir}/doc/latex/dtk/doc/beispiel.pdf
%{_texmfdistdir}/doc/latex/dtk/doc/beispiel.tex
%{_texmfdistdir}/doc/latex/dtk/doc/dtk-extern-test.tex
%{_texmfdistdir}/doc/latex/dtk/dtk-ruecken.tex
%{_texmfdistdir}/doc/latex/dtk/dtk.nolig
%{_texmfdistdir}/doc/latex/dtk/dtk.xdy
%{_texmfdistdir}/doc/latex/dtk/dtk0.tex

%files -n texlive-dtk
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dtk/dtk-author.clo
%{_texmfdistdir}/tex/latex/dtk/dtk-extern.sty
%{_texmfdistdir}/tex/latex/dtk/dtk-full.clo
%{_texmfdistdir}/tex/latex/dtk/dtk-logos.sty
%{_texmfdistdir}/tex/latex/dtk/dtk-new-engines.clo
%{_texmfdistdir}/tex/latex/dtk/dtk-old-engines.clo
%{_texmfdistdir}/tex/latex/dtk/dtk-url.sty
%{_texmfdistdir}/tex/latex/dtk/dtk.bbx
%{_texmfdistdir}/tex/latex/dtk/dtk.cbx
%{_texmfdistdir}/tex/latex/dtk/dtk.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dtk-%{texlive_version}.%{texlive_noarch}.2.08gsvn54080-%{release}-zypper
%endif

%package -n texlive-dtl
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6.1svn52851
Release:        0
Summary:        Tools to dis-assemble and re-assemble DVI files
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-dtl-bin >= %{texlive_version}
#!BuildIgnore: texlive-dtl-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       man(dt2dv.1)
Provides:       man(dv2dt.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source249:      dtl.doc.tar.xz

%description -n texlive-dtl
DTL (DVI Text Language) is a means of expressing the content of
a DVI file, which is readily readable by humans. The DTL bundle
contains an assembler dt2dv (which produces DVI files from DTL
files) and a disassembler dv2dt (which produces DTL files from
DVI files). The DTL bundle was developed so as to avoid some
infelicities of dvitype (among other pressing reasons).
%post -n texlive-dtl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dtl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dtl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dtl
%defattr(-,root,root,755)
%{_mandir}/man1/dt2dv.1*
%{_mandir}/man1/dv2dt.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dtl-%{texlive_version}.%{texlive_noarch}.0.0.6.1svn52851-%{release}-zypper
%endif

%package -n texlive-dtxdescribe
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn51652
Release:        0
Summary:        Describe additional object types in dtx source files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dtxdescribe-doc >= %{texlive_version}
Provides:       tex(dtxdescribe.sty)
Requires:       tex(caption.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(newfloat.sty)
Requires:       tex(pict2e.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xifthen.sty)
Requires:       tex(xparse.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source250:      dtxdescribe.tar.xz
Source251:      dtxdescribe.doc.tar.xz

%description -n texlive-dtxdescribe
The doc package includes tools for describing macros and
environments in LaTeX source .dtx format. The dtxdescribe
package adds additional tools for describing booleans, lengths,
counters, keys, packages, classes, options, files, commands,
arguments, and other objects, and also works with the standard
document classes as well, for those who do not wish to use the
.dtx format. Each item is given a margin tag similar to
\DescribeEnv, and is listed in the index by itself and also by
category. Each item may be sorted further by an optional class.
All index entries except code lines are hyperlinked. The
dtxexample environment is provided for typesetting example code
and its results. Contents are displayed verbatim along with a
caption and cross-referencing. They are then input and
executed, and the result is shown. Environments are also
provided for displaying verbatim or formatted source code,
user-interface displays, and sidebars with titles. Macros are
provided for formatting the names of inline LaTeX objects such
as packages and booleans, as well as program and file names,
file types, internet objects, the names of certain programs, a
number of logos, and inline dashes and slashes.

%package -n texlive-dtxdescribe-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.02svn51652
Release:        0
Summary:        Documentation for texlive-dtxdescribe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dtxdescribe-doc
This package includes the documentation for texlive-dtxdescribe

%post -n texlive-dtxdescribe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dtxdescribe 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dtxdescribe
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dtxdescribe-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dtxdescribe/README.txt
%{_texmfdistdir}/doc/latex/dtxdescribe/dtxdescribe.pdf

%files -n texlive-dtxdescribe
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/dtxdescribe/dtxdescribe.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dtxdescribe-%{texlive_version}.%{texlive_noarch}.1.02svn51652-%{release}-zypper
%endif

%package -n texlive-dtxgallery
Version:        %{texlive_version}.%{texlive_noarch}.1svn49504
Release:        0
Summary:        A small collection of minimal DTX examples
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
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
Source252:      dtxgallery.doc.tar.xz

%description -n texlive-dtxgallery
A collection of files that demonstrate simple things that are
possible with the flexible and under-appreciated docstrip file
format. Each file of the collection is provided as a .dtx file
and as the corresponding .pdf. The set is intended as a
companion to Scott Pakin's excellent and influential dtxtut
example of producing LaTeX packages in this way.
%post -n texlive-dtxgallery
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dtxgallery 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dtxgallery
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dtxgallery
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dtxgallery/README
%{_texmfdistdir}/doc/latex/dtxgallery/conditional-code.dtx
%{_texmfdistdir}/doc/latex/dtxgallery/conditional-code.pdf
%{_texmfdistdir}/doc/latex/dtxgallery/dtxgallery.dtx
%{_texmfdistdir}/doc/latex/dtxgallery/dtxgallery.pdf
%{_texmfdistdir}/doc/latex/dtxgallery/rearrange.dtx
%{_texmfdistdir}/doc/latex/dtxgallery/rearrange.pdf
%{_texmfdistdir}/doc/latex/dtxgallery/single-source.dtx
%{_texmfdistdir}/doc/latex/dtxgallery/single-source.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dtxgallery-%{texlive_version}.%{texlive_noarch}.1svn49504-%{release}-zypper
%endif

%package -n texlive-dtxgen
Version:        %{texlive_version}.%{texlive_noarch}.1.08svn51663
Release:        0
Summary:        Creates a template for a self-extracting .dtx file
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-dtxgen-bin >= %{texlive_version}
#!BuildIgnore: texlive-dtxgen-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-dtxgen-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source253:      dtxgen.tar.xz
Source254:      dtxgen.doc.tar.xz

%description -n texlive-dtxgen
The bash script dtxgen creates a template for a self-extracting
.dtx file. It is useful for those who plan to create a new
Documented LaTeX Source (.dtx) file.

%package -n texlive-dtxgen-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.08svn51663
Release:        0
Summary:        Documentation for texlive-dtxgen
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dtxgen-doc
This package includes the documentation for texlive-dtxgen

%post -n texlive-dtxgen
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dtxgen 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dtxgen
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dtxgen-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/dtxgen/README
%{_texmfdistdir}/doc/support/dtxgen/dtxgen.pdf

%files -n texlive-dtxgen
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/dtxgen/dtxgen
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dtxgen-%{texlive_version}.%{texlive_noarch}.1.08svn51663-%{release}-zypper
%endif

%package -n texlive-dtxtut
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn38375
Release:        0
Summary:        Tutorial on writing .dtx and .ins files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
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
Source255:      dtxtut.doc.tar.xz

%description -n texlive-dtxtut
This tutorial is intended for advanced LaTeX2e users who want
to learn how to create .ins and .dtx files for distributing
their homebrewed classes and package files.
%post -n texlive-dtxtut
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-dtxtut 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-dtxtut
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-dtxtut
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/dtxtut/README
%{_texmfdistdir}/doc/latex/dtxtut/cskeleton.dtx
%{_texmfdistdir}/doc/latex/dtxtut/cskeleton.ins
%{_texmfdistdir}/doc/latex/dtxtut/dtxtut.pdf
%{_texmfdistdir}/doc/latex/dtxtut/dtxtut.tex
%{_texmfdistdir}/doc/latex/dtxtut/skeleton.dtx
%{_texmfdistdir}/doc/latex/dtxtut/skeleton.ins
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dtxtut-%{texlive_version}.%{texlive_noarch}.2.1svn38375-%{release}-zypper
%endif

%package -n texlive-ducksay
Version:        %{texlive_version}.%{texlive_noarch}.2.5svn53631
Release:        0
Summary:        Draw ASCII art of animals saying a specified message
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ducksay-doc >= %{texlive_version}
Provides:       tex(ducksay.animals.tex)
Provides:       tex(ducksay.code.v1.tex)
Provides:       tex(ducksay.code.v2.tex)
Provides:       tex(ducksay.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source256:      ducksay.tar.xz
Source257:      ducksay.doc.tar.xz

%description -n texlive-ducksay
The package draws ASCII art of animals saying a specified
message. The following macros are available: \ducksay
\duckthink \DefaultAnimal \AddAnimal \DucksayOptions Multi-line
messages are now fully supported. The package comes with two
versions, choosable with the version key.

%package -n texlive-ducksay-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.5svn53631
Release:        0
Summary:        Documentation for texlive-ducksay
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ducksay-doc
This package includes the documentation for texlive-ducksay

%post -n texlive-ducksay
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ducksay 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ducksay
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ducksay-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ducksay/README.md
%{_texmfdistdir}/doc/latex/ducksay/ducksay.pdf

%files -n texlive-ducksay
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/ducksay/ducksay.animals.tex
%{_texmfdistdir}/tex/latex/ducksay/ducksay.code.v1.tex
%{_texmfdistdir}/tex/latex/ducksay/ducksay.code.v2.tex
%{_texmfdistdir}/tex/latex/ducksay/ducksay.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ducksay-%{texlive_version}.%{texlive_noarch}.2.5svn53631-%{release}-zypper
%endif

%package -n texlive-duckuments
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn52271
Release:        0
Summary:        Create duckified dummy content
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-duckuments-doc >= %{texlive_version}
Provides:       tex(duckuments.sty)
Requires:       tex(l3keys2e.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(tikzducks.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source258:      duckuments.tar.xz
Source259:      duckuments.doc.tar.xz

%description -n texlive-duckuments
The package provides facilities to create duckified dummy
contents. It was inspired by the question "Getting ducks in
example images" on TeX-LaTeX Stack Exchange. The following
macros are available: \duckument[key=val] - print a short
duckument \blindduck[key=val] - print a paragraph
\ducklist(*){environment} - create a list of type environment
\ducklistlist(*){environment} - create nested lists
\duckitemize - ducklist{itemize} \duckenumerate -
ducklist{enumerate} \duckdescription - ducklist{description}
\duckumentsCreateExampleFile \duckumentsDrawRandomDucks The
package works with pdfTeX, LuaTeX, and XeTeX.

%package -n texlive-duckuments-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.5svn52271
Release:        0
Summary:        Documentation for texlive-duckuments
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-duckuments-doc
This package includes the documentation for texlive-duckuments

%post -n texlive-duckuments
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-duckuments 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-duckuments
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-duckuments-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/duckuments/README.md
%{_texmfdistdir}/doc/latex/duckuments/duckuments.pdf
%{_texmfdistdir}/doc/latex/duckuments/example-image-duck-portrait.tex
%{_texmfdistdir}/doc/latex/duckuments/example-image-duck.tex

%files -n texlive-duckuments
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/duckuments/duckuments.sty
%{_texmfdistdir}/tex/latex/duckuments/example-image-duck-portrait.pdf
%{_texmfdistdir}/tex/latex/duckuments/example-image-duck.pdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-duckuments-%{texlive_version}.%{texlive_noarch}.0.0.5svn52271-%{release}-zypper
%endif

%package -n texlive-duerer
Version:        %{texlive_version}.%{texlive_noarch}.svn20741
Release:        0
Summary:        Computer Duerer fonts
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
Recommends:     texlive-duerer-doc >= %{texlive_version}
Provides:       tex(cdb10.tfm)
Provides:       tex(cdi10.tfm)
Provides:       tex(cdr10.tfm)
Provides:       tex(cdsl10.tfm)
Provides:       tex(cdss10.tfm)
Provides:       tex(cdtt10.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source260:      duerer.tar.xz
Source261:      duerer.doc.tar.xz

%description -n texlive-duerer
These fonts are designed for titling use, and consist of
capital roman letters only. Together with the normal set of
base shapes, the family also offers an informal shape. The
distribution is as Metafont source. LaTeX support is available
in the duerer-latex bundle.

%package -n texlive-duerer-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20741
Release:        0
Summary:        Documentation for texlive-duerer
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-duerer-doc
This package includes the documentation for texlive-duerer

%post -n texlive-duerer
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-duerer 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-duerer
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-duerer-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/duerer/README

%files -n texlive-duerer
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/duerer/cdb10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdi10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdr10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdsl10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdss10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdtt10.mf
%{_texmfdistdir}/fonts/source/public/duerer/dromani.mf
%{_texmfdistdir}/fonts/source/public/duerer/dromanu.mf
%{_texmfdistdir}/fonts/source/public/duerer/dtitle.mf
%{_texmfdistdir}/fonts/tfm/public/duerer/cdb10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdi10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdr10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdss10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdtt10.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-duerer-%{texlive_version}.%{texlive_noarch}.svn20741-%{release}-zypper
%endif

%package -n texlive-duerer-latex
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        LaTeX support for the Duerer fonts
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
Recommends:     texlive-duerer-latex-doc >= %{texlive_version}
Provides:       tex(duerer.sty)
Provides:       tex(ot1cdin.fd)
Provides:       tex(ot1cdr.fd)
Provides:       tex(ot1cdss.fd)
Provides:       tex(ot1cdtt.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source262:      duerer-latex.tar.xz
Source263:      duerer-latex.doc.tar.xz

%description -n texlive-duerer-latex
LaTeX support for Hoenig's Computer Duerer fonts, using their
standard fontname names.

%package -n texlive-duerer-latex-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn15878
Release:        0
Summary:        Documentation for texlive-duerer-latex
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-duerer-latex-doc
This package includes the documentation for texlive-duerer-latex

%post -n texlive-duerer-latex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-duerer-latex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-duerer-latex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-duerer-latex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/duerer-latex/README
%{_texmfdistdir}/doc/latex/duerer-latex/duerer.pdf
%{_texmfdistdir}/doc/latex/duerer-latex/duerer.tex

%files -n texlive-duerer-latex
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/duerer-latex/duerer.sty
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdin.fd
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdr.fd
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdss.fd
%{_texmfdistdir}/tex/latex/duerer-latex/ot1cdtt.fd
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-duerer-latex-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif

%package -n texlive-duotenzor
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn18728
Release:        0
Summary:        Drawing package for circuit and duotensor diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-duotenzor-doc >= %{texlive_version}
Provides:       tex(duotenzor.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source264:      duotenzor.tar.xz
Source265:      duotenzor.doc.tar.xz

%description -n texlive-duotenzor
This is a drawing package for circuit and duotensor diagrams
within LaTeX documents. It consists of about eighty commands,
calling on TikZ for support.

%package -n texlive-duotenzor-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.00svn18728
Release:        0
Summary:        Documentation for texlive-duotenzor
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-duotenzor-doc
This package includes the documentation for texlive-duotenzor

%post -n texlive-duotenzor
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-duotenzor 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-duotenzor
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-duotenzor-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/duotenzor/README
%{_texmfdistdir}/doc/latex/duotenzor/duotenzormanual.pdf
%{_texmfdistdir}/doc/latex/duotenzor/duotenzormanual.tex

%files -n texlive-duotenzor
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/duotenzor/duotenzor.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-duotenzor-%{texlive_version}.%{texlive_noarch}.1.00svn18728-%{release}-zypper
%endif

%package -n texlive-dutchcal
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        A reworking of ESSTIX13, adding a bold version
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
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
Requires:       texlive-dutchcal-fonts >= %{texlive_version}
Recommends:     texlive-dutchcal-doc >= %{texlive_version}
Provides:       tex(dutchcal-b.tfm)
Provides:       tex(dutchcal-b.vf)
Provides:       tex(dutchcal-r.tfm)
Provides:       tex(dutchcal-r.vf)
Provides:       tex(dutchcal.map)
Provides:       tex(dutchcal.sty)
Provides:       tex(rdutchcalb.tfm)
Provides:       tex(rdutchcalr.tfm)
Provides:       tex(udutchcal.fd)
Requires:       tex(cmr10.tfm)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source266:      dutchcal.tar.xz
Source267:      dutchcal.doc.tar.xz

%description -n texlive-dutchcal
This package reworks the mathematical calligraphic font
ESSTIX13, adding a bold version. LaTeX support files are
included. The new fonts may also be accessed from the most
recent version of mathalpha. The fonts themselves are subject
to the SIL OPEN FONT LICENSE, version 1.1.

%package -n texlive-dutchcal-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Documentation for texlive-dutchcal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-dutchcal-doc
This package includes the documentation for texlive-dutchcal


%package -n texlive-dutchcal-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn54080
Release:        0
Summary:        Severed fonts for texlive-dutchcal
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-dutchcal-fonts
The  separated fonts package for texlive-dutchcal
%post -n texlive-dutchcal
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap dutchcal.map' >> /var/run/texlive/run-updmap

%postun -n texlive-dutchcal 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap dutchcal.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-dutchcal
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-dutchcal-fonts
%files -n texlive-dutchcal-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/dutchcal/README

%files -n texlive-dutchcal
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/dutchcal/DutchCalBold.afm
%{_texmfdistdir}/fonts/afm/public/dutchcal/DutchCalReg.afm
%{_texmfdistdir}/fonts/map/dvips/dutchcal/dutchcal.map
%{_texmfdistdir}/fonts/tfm/public/dutchcal/dutchcal-b.tfm
%{_texmfdistdir}/fonts/tfm/public/dutchcal/dutchcal-r.tfm
%{_texmfdistdir}/fonts/tfm/public/dutchcal/rdutchcalb.tfm
%{_texmfdistdir}/fonts/tfm/public/dutchcal/rdutchcalr.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/dutchcal/DutchCalBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/dutchcal/DutchCalReg.pfb
%{_texmfdistdir}/fonts/vf/public/dutchcal/dutchcal-b.vf
%{_texmfdistdir}/fonts/vf/public/dutchcal/dutchcal-r.vf
%{_texmfdistdir}/tex/latex/dutchcal/dutchcal.sty
%{_texmfdistdir}/tex/latex/dutchcal/udutchcal.fd

%files -n texlive-dutchcal-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-dutchcal
%{_datadir}/fontconfig/conf.avail/58-texlive-dutchcal.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dutchcal/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dutchcal/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-dutchcal/fonts.scale
%{_datadir}/fonts/texlive-dutchcal/DutchCalBold.pfb
%{_datadir}/fonts/texlive-dutchcal/DutchCalReg.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-dutchcal-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
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
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-basque-%{texlive_version}.%{texlive_noarch}.1.2asvn47064-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-breton-%{texlive_version}.%{texlive_noarch}.1.2svn52647-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-bulgarian-%{texlive_version}.%{texlive_noarch}.1.1svn47031-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-catalan-%{texlive_version}.%{texlive_noarch}.1.1svn47032-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-croatian-%{texlive_version}.%{texlive_noarch}.1.0svn36682-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-czech-%{texlive_version}.%{texlive_noarch}.1.1svn47033-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-danish-%{texlive_version}.%{texlive_noarch}.1.1svn47034-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-dutch-%{texlive_version}.%{texlive_noarch}.1.1svn47355-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-en-fulltext-%{texlive_version}.%{texlive_noarch}.1.0svn36705-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-english-%{texlive_version}.%{texlive_noarch}.1.05svn52479-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-esperanto-%{texlive_version}.%{texlive_noarch}.1.1svn47356-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-estonian-%{texlive_version}.%{texlive_noarch}.1.1svn47565-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-finnish-%{texlive_version}.%{texlive_noarch}.1.2svn47047-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-french-%{texlive_version}.%{texlive_noarch}.1.02svn43742-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-galician-%{texlive_version}.%{texlive_noarch}.1.0svn47631-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-german-%{texlive_version}.%{texlive_noarch}.3.0svn53125-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-greek-%{texlive_version}.%{texlive_noarch}.1.1svn47533-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-hebrew-%{texlive_version}.%{texlive_noarch}.1.1svn47534-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-icelandic-%{texlive_version}.%{texlive_noarch}.1.1svn47501-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-irish-%{texlive_version}.%{texlive_noarch}.1.1svn47632-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-it-fulltext-%{texlive_version}.%{texlive_noarch}.1.6svn54779-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-italian-%{texlive_version}.%{texlive_noarch}.1.3svn37146-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-latin-%{texlive_version}.%{texlive_noarch}.1.0svn47748-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-lsorbian-%{texlive_version}.%{texlive_noarch}.1.1svn47749-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-magyar-%{texlive_version}.%{texlive_noarch}.1.1svn48266-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-norsk-%{texlive_version}.%{texlive_noarch}.1.1svn48267-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-polish-%{texlive_version}.%{texlive_noarch}.1.1svn48456-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-portuges-%{texlive_version}.%{texlive_noarch}.1.1svn48457-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-romanian-%{texlive_version}.%{texlive_noarch}.1.01svn43743-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-russian-%{texlive_version}.%{texlive_noarch}.1.1svn49345-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-samin-%{texlive_version}.%{texlive_noarch}.1.1svn49346-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-scottish-%{texlive_version}.%{texlive_noarch}.1.1svn52101-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-serbian-%{texlive_version}.%{texlive_noarch}.2.1.0svn52893-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-slovak-%{texlive_version}.%{texlive_noarch}.1.1svn52281-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-slovene-%{texlive_version}.%{texlive_noarch}.1.1svn52282-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-spanish-%{texlive_version}.%{texlive_noarch}.1.1svn45785-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-swedish-%{texlive_version}.%{texlive_noarch}.1.0svn36700-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-turkish-%{texlive_version}.%{texlive_noarch}.1.1svn52331-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-ukrainian-%{texlive_version}.%{texlive_noarch}.1.2asvn47552-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-usorbian-%{texlive_version}.%{texlive_noarch}.1.1svn52375-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-datetime2-welsh-%{texlive_version}.%{texlive_noarch}.1.1svn52553-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dblfloatfix-%{texlive_version}.%{texlive_noarch}.1.0asvn28983-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dccpaper-%{texlive_version}.%{texlive_noarch}.2.0svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dcpic-%{texlive_version}.%{texlive_noarch}.5.0.0svn30206-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ddphonism-%{texlive_version}.%{texlive_noarch}.0.0.2svn52009-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-de-macro-%{texlive_version}.%{texlive_noarch}.1.3svn26355-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-decimal-%{texlive_version}.%{texlive_noarch}.svn23374-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-decorule-%{texlive_version}.%{texlive_noarch}.0.0.6svn23487-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dehyph-%{texlive_version}.%{texlive_noarch}.svn48599-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dehyph-exptl-%{texlive_version}.%{texlive_noarch}.0.0.6svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    mkdir -p %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/dehyph-exptl.dat)<<'EOF'
%% from dehyph-exptl:
german-x-2019-04-04 dehypht-x-2019-04-04.tex
=german-x-latest
ngerman-x-2019-04-04 dehyphn-x-2019-04-04.tex
=ngerman-x-latest
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/dehyph-exptl.def)<<'EOF'
%% from dehyph-exptl:
\addlanguage{german-x-2019-04-04}{dehypht-x-2019-04-04.tex}{}{2}{2}
\addlanguage{german-x-latest}{dehypht-x-2019-04-04.tex}{}{2}{2}
\addlanguage{ngerman-x-2019-04-04}{dehyphn-x-2019-04-04.tex}{}{2}{2}
\addlanguage{ngerman-x-latest}{dehyphn-x-2019-04-04.tex}{}{2}{2}
EOF
    (cat > %{buildroot}%{_texmfdistdir}/tex/generic/config/language.splits/dehyph-exptl.dat.lua)<<'EOF'
-- from dehyph-exptl:
	['german-x-2019-04-04'] = {
		loader = 'dehypht-x-2019-04-04.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'german-x-latest' },
		patterns = 'hyph-de-1901.pat.txt',
		hyphenation = '',
	},
	['ngerman-x-2019-04-04'] = {
		loader = 'dehyphn-x-2019-04-04.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = { 'ngerman-x-latest' },
		patterns = 'hyph-de-1996.pat.txt',
		hyphenation = '',
	},
EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dejavu-fonts-%{texlive_version}.%{texlive_noarch}.2.34svn31771-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-dejavu
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/dejavu/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/dejavu/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-dejavu
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-dejavu/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-dejavu/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dejavu/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dejavu/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-dejavu.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-dejavu    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-dejavu/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-dejavu.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-dejavu/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-dejavu.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-dejavu.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dejavu-otf-%{texlive_version}.%{texlive_noarch}.0.0.04svn45991-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-delim-%{texlive_version}.%{texlive_noarch}.1.0svn23974-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-delimseasy-%{texlive_version}.%{texlive_noarch}.2.0svn39589-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-delimset-%{texlive_version}.%{texlive_noarch}.1.1svn49544-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-delimtxt-%{texlive_version}.%{texlive_noarch}.svn16549-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-denisbdoc-%{texlive_version}.%{texlive_noarch}.0.0.8svn54584-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-derivative-%{texlive_version}.%{texlive_noarch}.0.0.97svn53654-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-detex-%{texlive_version}.%{texlive_noarch}.svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dhua-%{texlive_version}.%{texlive_noarch}.0.0.11svn24035-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-diadia-%{texlive_version}.%{texlive_noarch}.1.1svn37656-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/diadia/diadia.lua
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
       %{buildroot}/var/adm/update-scripts/texlive-diagbox-%{texlive_version}.%{texlive_noarch}.2.4svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-diagmac2-%{texlive_version}.%{texlive_noarch}.2.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-diagnose-%{texlive_version}.%{texlive_noarch}.0.0.2svn19387-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dialogl-%{texlive_version}.%{texlive_noarch}.svn28946-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dice-%{texlive_version}.%{texlive_noarch}.svn28501-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dichokey-%{texlive_version}.%{texlive_noarch}.svn17192-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dickimaw-%{texlive_version}.%{texlive_noarch}.svn32925-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dictsym-fonts-%{texlive_version}.%{texlive_noarch}.svn20031-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-dictsym
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/dictsym/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-dictsym
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-dictsym/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-dictsym/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dictsym/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dictsym/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-dictsym.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-dictsym    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-dictsym/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-diffcoeff-%{texlive_version}.%{texlive_noarch}.3.2svn53244-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-digiconfigs-%{texlive_version}.%{texlive_noarch}.0.0.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dijkstra-%{texlive_version}.%{texlive_noarch}.0.0.11svn45256-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-din1505-%{texlive_version}.%{texlive_noarch}.svn19441-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dinat-%{texlive_version}.%{texlive_noarch}.2.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dinbrief-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dingbat-%{texlive_version}.%{texlive_noarch}.1.0svn27918-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-directory-%{texlive_version}.%{texlive_noarch}.1.20svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dirtree-%{texlive_version}.%{texlive_noarch}.0.0.32svn42428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dirtytalk-%{texlive_version}.%{texlive_noarch}.1.0svn20520-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-disser-%{texlive_version}.%{texlive_noarch}.1.5.0svn43417-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ditaa-%{texlive_version}.%{texlive_noarch}.0.0.9svn48932-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dithesis-%{texlive_version}.%{texlive_noarch}.0.0.2svn34295-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dk-bib-%{texlive_version}.%{texlive_noarch}.0.0.6svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dlfltxb-%{texlive_version}.%{texlive_noarch}.svn17337-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dnaseq-%{texlive_version}.%{texlive_noarch}.0.0.01svn17194-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dnp-%{texlive_version}.%{texlive_noarch}.svn54074-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-doc-pictex-%{texlive_version}.%{texlive_noarch}.svn24927-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-docbytex-%{texlive_version}.%{texlive_noarch}.svn34294-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-doclicense-%{texlive_version}.%{texlive_noarch}.1.10.1svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-docmfp-%{texlive_version}.%{texlive_noarch}.1.2dsvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-docmute-%{texlive_version}.%{texlive_noarch}.1.4svn25741-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-docsurvey-%{texlive_version}.%{texlive_noarch}.svn48931-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-doctools-%{texlive_version}.%{texlive_noarch}.0.0.1svn34474-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-documentation-%{texlive_version}.%{texlive_noarch}.0.0.1svn34521-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-doi-%{texlive_version}.%{texlive_noarch}.svn48634-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-doipubmed-%{texlive_version}.%{texlive_noarch}.1.01svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/latex/doipubmed/doipubmed.perl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-domitian-fonts-%{texlive_version}.%{texlive_noarch}.1.0csvn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-domitian
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/domitian/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/domitian/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-domitian
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-domitian/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-domitian/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-domitian/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-domitian/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-domitian.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-domitian    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-domitian/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-domitian.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-domitian/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-domitian.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-domitian.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dosepsbin-%{texlive_version}.%{texlive_noarch}.1.2svn29752-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/support/dosepsbin/clean-case.pl \
	       %{_texmfdistdir}/doc/support/dosepsbin/version.pl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/dosepsbin/dosepsbin.pl \
	       %{_texmfdistdir}/doc/support/dosepsbin/clean-case.pl \
	       %{_texmfdistdir}/doc/support/dosepsbin/version.pl
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
       %{buildroot}/var/adm/update-scripts/texlive-dot2texi-%{texlive_version}.%{texlive_noarch}.3.0svn26237-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dotarrow-%{texlive_version}.%{texlive_noarch}.0.0.01asvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dotlessi-%{texlive_version}.%{texlive_noarch}.1.1svn51476-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dotseqn-%{texlive_version}.%{texlive_noarch}.1.1svn17195-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dottex-%{texlive_version}.%{texlive_noarch}.0.0.6svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-doublestroke-fonts-%{texlive_version}.%{texlive_noarch}.1.111svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-doublestroke
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/doublestroke/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-doublestroke
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-doublestroke/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-doublestroke/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-doublestroke/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-doublestroke/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-doublestroke.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-doublestroke    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-doublestroke/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dowith-%{texlive_version}.%{texlive_noarch}.r0.32svn38860-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-download-%{texlive_version}.%{texlive_noarch}.1.2svn52257-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dox-%{texlive_version}.%{texlive_noarch}.2.4svn46011-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dozenal-fonts-%{texlive_version}.%{texlive_noarch}.7.2svn47680-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-dozenal
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/dozenal/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-dozenal
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-dozenal/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-dozenal/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dozenal/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dozenal/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-dozenal.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-dozenal    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-dozenal/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dpcircling-%{texlive_version}.%{texlive_noarch}.1.0svn54750-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dpfloat-%{texlive_version}.%{texlive_noarch}.svn17196-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dprogress-%{texlive_version}.%{texlive_noarch}.0.0.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-drac-%{texlive_version}.%{texlive_noarch}.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-draftcopy-%{texlive_version}.%{texlive_noarch}.2.16svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-draftfigure-%{texlive_version}.%{texlive_noarch}.0.0.2svn44854-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-draftwatermark-%{texlive_version}.%{texlive_noarch}.2.0svn54317-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dramatist-%{texlive_version}.%{texlive_noarch}.1.2esvn35866-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dratex-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-drawmatrix-%{texlive_version}.%{texlive_noarch}.1.5.0svn44471-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-drawstack-%{texlive_version}.%{texlive_noarch}.svn28582-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-drm-fonts-%{texlive_version}.%{texlive_noarch}.4.4svn38157-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Add shebang e.g. correct perl wrapper scripts if any
    for scr in %{_texmfdistdir}/doc/fonts/drm/convert.sh
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
    # Avoid /usr/local/bin or similar
    for scr in %{_texmfdistdir}/doc/fonts/drm/fontconvert.sh
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@\(/usr/[^/]\+\|/opt\(/[^/]\+\)\?\)/bin@/usr/bin@
		.
		w
		q
	EOF
    done
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-drm
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/drm/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/drm/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-drm
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-drm/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-drm/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-drm/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-drm/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-drm.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-drm    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-drm/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-drm.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-drm/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-drm.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-drm.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-droid-fonts-%{texlive_version}.%{texlive_noarch}.3.2svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-droid
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/ascender/droid/droidsans/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/truetype/ascender/droid/droidsansmono/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/truetype/ascender/droid/droidserif/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/ascender/droid/droidsans/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/ascender/droid/droidsansmono/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/ascender/droid/droidserif/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-droid
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-droid/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-droid/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-droid/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-droid/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-droid.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-droid    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-droid/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-droid.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-droid/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-droid.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-droid.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-droit-fr-%{texlive_version}.%{texlive_noarch}.1.2svn39802-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-drs-%{texlive_version}.%{texlive_noarch}.1.1bsvn19232-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-drv-%{texlive_version}.%{texlive_noarch}.0.0.97svn29349-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dsptricks-%{texlive_version}.%{texlive_noarch}.1.0svn34724-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dsserif-fonts-%{texlive_version}.%{texlive_noarch}.1.01svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-dsserif
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/dsserif/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-dsserif
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-dsserif/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-dsserif/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dsserif/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dsserif/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-dsserif.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-dsserif    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-dsserif/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dtk-%{texlive_version}.%{texlive_noarch}.2.08gsvn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dtl-%{texlive_version}.%{texlive_noarch}.0.0.6.1svn52851-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dtxdescribe-%{texlive_version}.%{texlive_noarch}.1.02svn51652-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dtxgallery-%{texlive_version}.%{texlive_noarch}.1svn49504-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dtxgen-%{texlive_version}.%{texlive_noarch}.1.08svn51663-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dtxtut-%{texlive_version}.%{texlive_noarch}.2.1svn38375-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ducksay-%{texlive_version}.%{texlive_noarch}.2.5svn53631-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-duckuments-%{texlive_version}.%{texlive_noarch}.0.0.5svn52271-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-duerer-%{texlive_version}.%{texlive_noarch}.svn20741-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-duerer-latex-%{texlive_version}.%{texlive_noarch}.1.1svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-duotenzor-%{texlive_version}.%{texlive_noarch}.1.00svn18728-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-dutchcal-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-dutchcal
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/dutchcal/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-dutchcal
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-dutchcal/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-dutchcal/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dutchcal/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-dutchcal/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-dutchcal.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-dutchcal    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-dutchcal/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
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
