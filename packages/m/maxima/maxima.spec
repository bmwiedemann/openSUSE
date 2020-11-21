#
# spec file for package maxima
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


# clisp and sbcl are available for oS, cmucl and gcl are not
%bcond_without clisp
%bcond_without sbcl
%bcond_with cmucl
%bcond_with gcl

# Inhibit automatic compressing of info files. Compressed info
# files break maxima's internal help.
%define __os_install_post %{_prefix}/lib/rpm/brp-suse

Name:           maxima
Version:        5.44.0
Release:        0
Summary:        Symbolic Computation Program/Computer Algebra System
License:        GPL-2.0-or-later
URL:            http://maxima.sourceforge.net/
Source0:        http://download.sourceforge.net/maxima/%{name}-%{version}.tar.gz
Source1:        maxima-rpmlintrc
Source2:        README.SUSE.packaging 
# PATCH-FIX-UPSTREAM maxima-python3.patch badshah400@gmail.com -- Use python3 instead of python(2) when importing vtk modules and building help; this allows maxima to be built with python3 instead of python2.
Patch0:         maxima-python3.patch
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  gzip
BuildRequires:  makeinfo
BuildRequires:  python3
BuildRequires:  update-desktop-files
Requires:       gnuplot
Requires:       maxima_exec
Requires:       plotutils
Requires:       rlwrap
Suggests:       maxima-exec-sbcl
ExcludeArch:    ppc64 ppc64le
%if 0%{?suse_version} <= 1500
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%endif
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
%if 0%{?suse_version} <= 1500
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%endif

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
Supplements:    packageand(maxima:clisp)
Provides:       maxima_exec = %{version}

%description exec-clisp
Maxima compiled with Common Lisp.
%endif

%if %{with cmucl}
%package exec-cmucl
Summary:        Maxima compiled with CMUCL
Supplements:    packageand(maxima:cmucl)
Provides:       maxima_exec = %{version}

%description    exec-cmucl
Maxima compiled with CMUCL.
%endif

%if %{with sbcl}
%package exec-sbcl
Summary:        Maxima compiled with SBCL
Supplements:    packageand(maxima:sbcl)
Requires:       sbcl
Provides:       maxima_exec = %{version}

%description exec-sbcl
Maxima compiled with SBCL.
%endif

%if %{with gcl}
%package exec-gcl
Summary:        Maxima compiled with GCL
Supplements:    packageand(maxima:gcl)
Provides:       maxima_exec = %{version}

%description exec-gcl
Maxima compiled with Gnu Common Lisp.
%endif

%package lang-de-utf8
Summary:        Maxima German UTF-8 language pack
Requires:       maxima = %{version}
Provides:       locale(maxima:de)
%if 0%{?suse_version} <= 1500
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%endif

%description lang-de-utf8
Maxima German language support (in UTF-8).

%package lang-es-utf8
Summary:        Maxima Spanish UTF-8 language pack
Requires:       maxima = %{version}
Provides:       locale(maxima:es)
%if 0%{?suse_version} <= 1500
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%endif

%description lang-es-utf8
Maxima Spanish language support (in UTF-8).

%package lang-pt-utf8
Summary:        Maxima Portuguese UTF-8 language pack
Requires:       maxima = %{version}
Provides:       locale(maxima:pt)
%if 0%{?suse_version} <= 1500
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%endif

%description lang-pt-utf8
Maxima Portuguese language support (in UTF-8).

%package lang-pt_BR-utf8
Summary:        Maxima Brazilian Portuguese UTF-8 language pack
Requires:       maxima = %{version}
Provides:       locale(maxima:pt_BR)
%if 0%{?suse_version} <= 1500
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info
%endif

%description lang-pt_BR-utf8
Maxima Brazilian Portuguese language support (in UTF-8).

%prep
%setup -q
%patch0 -p1

%build
%configure  %{?with_sbcl:--enable-sbcl} \
            %{?with_cmucl:--enable-cmucl} \
            %{?with_gcl:--enable-gcl} \
            %{?with_clisp:--enable-clisp} \
            --enable-gettext \
            --enable-lang-de-utf8 \
            --enable-lang-es-utf8 \
            --enable-lang-pt-utf8 \
            --enable-lang-pt_BR-utf8 \
            --disable-recode \
            --enable-mathjax
%make_build

%install
%makeinstall install-info
  make \
    prefix=%{?buildroot:%{buildroot}}%{_prefix} \
    exec_prefix=%{?buildroot:%{buildroot}}%{_prefix} \
    bindir=%{?buildroot:%{buildroot}}%{_bindir} \
    sbindir=%{?buildroot:%{buildroot}}%{_sbindir} \
    sysconfdir=%{?buildroot:%{buildroot}}%{_sysconfdir} \
    datadir=%{?buildroot:%{buildroot}}%{_datadir} \
    includedir=%{?buildroot:%{buildroot}}%{_includedir} \
    libdir=%{?buildroot:%{buildroot}}%{_libdir} \
    libexecdir=%{?buildroot:%{buildroot}}%{_libexecdir} \
    localstatedir=%{?buildroot:%{buildroot}}%{_localstatedir} \
    sharedstatedir=%{?buildroot:%{buildroot}}%{_sharedstatedir} \
    mandir=%{?buildroot:%{buildroot}}%{_mandir} \
    infodir=%{?buildroot:%{buildroot}}%{_infodir} \
  install-info

#  Deal with info/dir
rm -f %{buildroot}%{_infodir}/dir
# set executable rights for example scripts
chmod +x %{buildroot}%{_datadir}/%{name}/%{version}/share/contrib/lurkmathml/mathmltest
# zip the manpage
gzip %{buildroot}%{_mandir}/man1/maxima.1
gzip %{buildroot}%{_mandir}/*/man1/maxima.1
# reduce space, create symlinks
%fdupes -s %{buildroot}/%{_datadir}/%{name}/%{version}/share %{buildroot}/%{_datadir}/%{name}/%{version}/src

%fdupes %{buildroot}/%{_datadir}/

%suse_update_desktop_file net.sourceforge.maxima.xmaxima

# FIXME CHECKS TAKE TOO LONG AND TIME-OUT (LAST CHECK: VERSION 5.44.0)
#%%check
#make check
# /FIXME

%if 0%{?suse_version} <= 1500
%post
%install_info --info-dir=%{_infodir} %{_infodir}/maxima.info

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/maxima.info

%post xmaxima
%install_info --info-dir=%{_infodir} %{_infodir}/xmaxima.info
%mime_database_post
%desktop_database_post

%postun xmaxima
%install_info_delete --info-dir=%{_infodir} %{_infodir}/xmaxima.info
%mime_database_postun
%desktop_database_postun

%post lang-de-utf8
%install_info --info-dir=%{_infodir} %{_infodir}/de.utf8/maxima.info

%postun lang-de-utf8
%install_info_delete --info-dir=%{_infodir} %{_infodir}/de.utf8/maxima.info

%post lang-es-utf8
%install_info --info-dir=%{_infodir} %{_infodir}/es.utf8/maxima.info

%postun lang-es-utf8
%install_info_delete --info-dir=%{_infodir} %{_infodir}/es.utf8/maxima.info

%post lang-pt-utf8
%install_info --info-dir=%{_infodir} %{_infodir}/pt.utf8/maxima.info

%postun lang-pt-utf8
%install_info_delete --info-dir=%{_infodir} %{_infodir}/pt.utf8/maxima.info

%post lang-pt_BR-utf8
%install_info --info-dir=%{_infodir} %{_infodir}/pt_BR.utf8/maxima.info

%postun lang-pt_BR-utf8
%install_info_delete --info-dir=%{_infodir} %{_infodir}/pt_BR.utf8/maxima.info
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
%exclude %{_datadir}/maxima/%{version}/xmaxima
%exclude %{_datadir}/maxima/%{version}/doc/html/de.utf8
%exclude %{_datadir}/maxima/%{version}/doc/html/es.utf8
%exclude %{_datadir}/maxima/%{version}/doc/html/pt.utf8
%exclude %{_datadir}/maxima/%{version}/doc/html/pt_BR.utf8
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
%{_infodir}/*
%exclude %{_infodir}/de.utf8
%exclude %{_infodir}/es.utf8
%exclude %{_infodir}/pt.utf8
%exclude %{_infodir}/pt_BR.utf8
%{_bindir}/maxima
%{_bindir}/rmaxima
%{_datadir}/bash-completion/completions/maxima
%{_datadir}/bash-completion/completions/rmaxima
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*

%files xmaxima
%dir %{_datadir}/maxima/%{version}/xmaxima
%{_bindir}/xmaxima
%{_datadir}/maxima/%{version}/xmaxima/*
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/xmaxima
%{_datadir}/mime/packages/x-maxima-out.xml
%{_datadir}/pixmaps/*
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

%files lang-de-utf8
%doc %{_datadir}/maxima/%{version}/doc/html/de.utf8
%{_infodir}/de.utf8

%files lang-es-utf8
%doc %{_datadir}/maxima/%{version}/doc/html/es.utf8
%{_datadir}/locale/es/LC_MESSAGES/maxima.mo
%{_infodir}/es.utf8

%files lang-pt-utf8
%doc %{_datadir}/maxima/%{version}/doc/html/pt.utf8
%{_datadir}/locale/pt/LC_MESSAGES/maxima.mo
%{_infodir}/pt.utf8

%files lang-pt_BR-utf8
%doc %{_datadir}/maxima/%{version}/doc/html/pt_BR.utf8
%{_infodir}/pt_BR.utf8

%changelog
