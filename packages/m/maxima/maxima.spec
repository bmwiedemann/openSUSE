#
# spec file for package maxima
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# SBCL not available for older distros
%if 0%{?suse_version} < 1500 || 0%{?suse_version} == 1600
%bcond_with sbcl
%else
%bcond_without sbcl
%endif

# clisp available for oS, cmucl and gcl are not
%bcond_without clisp
%bcond_with cmucl
%bcond_with gcl

# Inhibit automatic compressing of info files. Compressed info
# files break maxima's internal help.
%define __os_install_post %{_prefix}/lib/rpm/brp-suse

# Tests take too long and time-out (last check: version 5.48.1); disable
%bcond_with tests

Name:           maxima
Version:        5.49.0
Release:        0
Summary:        Symbolic Computation Program/Computer Algebra System
License:        GPL-2.0-or-later
URL:            https://maxima.sourceforge.net/
Source0:        https://download.sourceforge.net/maxima/%{name}-%{version}.tar.gz
Source1:        maxima.rpmlintrc
Source2:        README.SUSE.packaging
# PATCH-FIX-UPSTREAM maxima-python3.patch badshah400@gmail.com -- Use python3 instead of python(2) when importing vtk modules and building help; this allows maxima to be built with python3 instead of python2.
Patch0:         maxima-python3.patch
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  gzip
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(libpq)

Requires:       gnuplot
Requires:       maxima_exec
Requires:       plotutils
Requires:       rlwrap
Suggests:       maxima-exec-sbcl
ExcludeArch:    ppc64 ppc64le

%if %{with clisp}
BuildRequires:  clisp >= 2.34.0
%endif
%if %{with cmucl}
BuildRequires:  cmucl
%endif
%if %{with gcl}
BuildRequires:  gcl
%endif
%if %{with sbcl}
BuildRequires:  sbcl
%endif

%description
Maxima is a full symbolic computation program.  It is full featured
doing symbolic manipulation of polynomials, matrices, rational
functions, integration, Todd-coxeter, graphing, bigfloats.  It has a
symbolic debugger source level debugger for maxima code.  Maxima is
based on the original Macsyma developed at MIT in the 1970's.  It is
quite reliable, and has good garbage collection, and no memory leaks.
It comes with hundreds of self tests.

%package xmaxima
Summary:        Tcl/Tk interface to Maxima
Requires:       maxima = %{version}
Requires:       tk
Provides:       xmaxima = %{version}
# Installs a shell script to bindir, not arch dependent
BuildArch:      noarch

%description xmaxima
A graphical interface to the Maxima symbolic computation program. It
also provides Openmath, a graphics program that can be used from
Maxima, and a Web browser that accepts a custom html tag to execute
Maxima commands from an html page.

Xmaxima is written in the Tcl/Tk language.

%if %{with clisp}
%package        exec-clisp
Summary:        Maxima compiled with clisp
Requires:       clisp
Supplements:    (maxima and clisp)
Provides:       maxima_exec = %{version}

%description exec-clisp
Maxima compiled with Common Lisp.
%endif

%if %{with cmucl}
%package exec-cmucl
Summary:        Maxima compiled with CMUCL
Supplements:    (maxima and cmucl)
Provides:       maxima_exec = %{version}

%description    exec-cmucl
Maxima compiled with CMUCL.
%endif

%if %{with sbcl}
%package exec-sbcl
Summary:        Maxima compiled with SBCL
Supplements:    (maxima and sbcl)
Provides:       maxima_exec = %{version}
%requires_eq    sbcl

%description exec-sbcl
Maxima compiled with SBCL.
%endif

%if %{with gcl}
%package exec-gcl
Summary:        Maxima compiled with GCL
Supplements:    (maxima and gcl)
Provides:       maxima_exec = %{version}

%description exec-gcl
Maxima compiled with Gnu Common Lisp.
%endif

# Note: Cannot use the lang_package macro since we need to provide the old lang-utf packages
%package lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Obsoletes:      maxima-lang-de-utf8 < %{version}
Provides:       maxima-lang-de-utf8 = %{version}
Obsoletes:      maxima-lang-es-utf8 < %{version}
Provides:       maxima-lang-es-utf8 = %{version}
Obsoletes:      maxima-lang-pt-utf8 < %{version}
Provides:       maxima-lang-pt-utf8 = %{version}
Obsoletes:      maxima-lang-pt_BR-utf8 < %{version}
Provides:       maxima-lang-pt_BR-utf8 = %{version}
BuildArch:      noarch

%description lang
Provides translations for the %{name} package.

%prep
%autosetup -p1

%build
%configure  %{?with_sbcl:--enable-sbcl} \
            %{?with_cmucl:--enable-cmucl} \
            %{?with_gcl:--enable-gcl} \
            %{?with_clisp:--enable-clisp} \
            --enable-syntax-highlighting \
            --enable-gettext \
            --disable-recode \
            --enable-lang-de \
            --enable-lang-ja \
            --enable-lang-es \
            --enable-lang-pt \
            --enable-lang-pt_BR \
            --enable-lang-ru \
            --enable-mathjax
%make_build

%install
%make_install install-info

# Remove unnecessary hashbang
sed -Ei '1{\@^#!/bin/sh@d}' %{buildroot}%{_datadir}/maxima/%{version}/share/translators/m2mj/antlr4

#  Deal with info/dir
rm -f %{buildroot}%{_infodir}/dir
# set executable rights for example scripts
chmod +x %{buildroot}%{_datadir}/%{name}/%{version}/share/contrib/lurkmathml/mathmltest
# compress manpages
gzip %{buildroot}%{_mandir}/man1/maxima.1
gzip %{buildroot}%{_mandir}/*/man1/maxima.1
# reduce space, create symlinks
%fdupes -s %{buildroot}/%{_datadir}/%{name}/%{version}/share %{buildroot}/%{_datadir}/%{name}/%{version}/src

%fdupes %{buildroot}/%{_datadir}/

%find_lang %{name} %{?no_lang_C}

%if %{with tests}
%check
%make_build check
%endif

%files
%license COPYING
%doc AUTHORS NEWS README README.*
%{_mandir}/man1/maxima.1%{?ext_man}
%{_mandir}/*/man1/maxima.1%{?ext_man}
%dir %{_datadir}/maxima
%dir %{_datadir}/maxima/%{version}
%dir %{_libdir}/maxima
%if 0%{?sles_version} == 0
%dir %{_libexecdir}/maxima
%endif
%{_datadir}/maxima/%{version}/*
%{_libdir}/maxima/%{version}
%if %{with clisp}
%exclude %{_libdir}/maxima/%{version}/binary-clisp
%endif
%if %{with sbcl}
%exclude %{_libdir}/maxima/%{version}/binary-sbcl
%endif
%if %{with cmucl}
%exclude %{_libdir}/maxima/%{version}/binary-cmucl
%endif
%if %{with gcl}
%exclude %{_libdir}/maxima/%{version}/binary-gcl
%endif
%dir %{_libexecdir}/maxima/%{version}
%{_libexecdir}/maxima/%{version}/mgnuplot
%{_infodir}/*.info*
%{_infodir}/*.lisp
%{_bindir}/maxima
%{_bindir}/rmaxima
%{_datadir}/bash-completion/completions/maxima
%{_datadir}/bash-completion/completions/rmaxima
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*
%exclude %{_datadir}/maxima/%{version}/xmaxima
# Included in lang package
%exclude %{_datadir}/maxima/%{version}/doc/html/*/*
%exclude %{_infodir}/*/*

%files xmaxima
%dir %{_datadir}/maxima/%{version}/xmaxima
%{_bindir}/xmaxima
%{_datadir}/maxima/%{version}/xmaxima/*
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*
%{_datadir}/bash-completion/completions/xmaxima
%{_datadir}/mime/packages/x-maxima-out.xml
%{_datadir}/metainfo/*.appdata.xml

%if %{with clisp}
%files exec-clisp
%{_libdir}/maxima/%{version}/binary-clisp/
%endif

%if %{with cmucl}
%files exec-cmucl
%{_libdir}/maxima/%{version}/binary-cmucl/
%endif

%if %{with sbcl}
%files exec-sbcl
%{_libdir}/maxima/%{version}/binary-sbcl/
%endif

%if %{with gcl}
%files exec-gcl
%{_libdir}/maxima/%{version}/binary-gcl/
%endif

%files lang -f %{name}.lang
%doc %{_datadir}/maxima/%{version}/doc/html/*/
%{_infodir}/de/
%{_infodir}/es/
%{_infodir}/ja/
%{_infodir}/pt/
%{_infodir}/pt_BR/
%{_infodir}/ru/

%changelog
