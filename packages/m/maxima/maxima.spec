#
# spec file for package maxima
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


# This can be changed by modifying the variables below.
%define enable_clisp 1
%define clisp_flags --enable-clisp
%define clisp_version 2.33
%define enable_cmucl 0
%define cmucl_flags --disable-cmucl
%define enable_sbcl 0
%define sbcl_flags --disable-sbcl
%define enable_gcl 0
%define gcl_flags --disable-gcl

Name:           maxima
Version:        5.43.0
Release:        0
%define major_version 5.43
Summary:        Symbolic Computation Program/Computer Algebra System
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://maxima.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://download.sourceforge.net/maxima/%{name}-%{version}.tar.gz
Source1:        maxima-rpmlintrc
## SECTION Manually include texi sources missed by upstream tarball (https://sourceforge.net/p/maxima/bugs/3558/)
Source2:        https://sourceforge.net/p/maxima/code/ci/5e38cb/tree/doc/info/de/include-maxima.de.texi?format=raw#/include-maxima.de.texi 
Source3:        https://sourceforge.net/p/maxima/code/ci/5e38cb/tree/doc/info/pt/include-maxima.texi.in?format=raw#/include-maxima.texi.in
# /SECTION
%if 0%{?suse_version}
PreReq:         %install_info_prereq
%endif
BuildRequires:  bash-completion
BuildRequires:  gzip
BuildRequires:  makeinfo
BuildRequires:  python
Requires:       gnuplot
Requires:       maxima_exec
Requires:       plotutils
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%if 0%{?enable_clisp}
BuildRequires:  clisp >= 2.34.0
%endif
ExcludeArch:    ppc64 ppc64le

# Inhibit automatic compressing of info files. Compressed info
# files break maxima's internal help.
%define __os_install_post /usr/lib/rpm/brp-suse

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
Group:          Development/Languages/Other
PreReq:         %install_info_prereq
Requires:       maxima = %{version}
Requires:       tk
Provides:       xmaxima = %{version}

%description xmaxima
A graphical interface to the Maxima symbolic computation program. It
also provides Openmath, a graphics program that can be used from
Maxima, and a Web browser that accepts a custom html tag to execute
Maxima commands from an html page.

Xmaxima is written in the Tcl/Tk language.

%if 0%{?enable_clisp}
%package        exec-clisp
Summary:        Maxima compiled with clisp
Group:          Development/Languages/Other
BuildRequires:  clisp
Requires:       maxima = %{version}
Provides:       maxima_exec = %{version}

%description exec-clisp
Maxima compiled with Common Lisp.
%endif

%if 0%{?enable_cmucl}
%package exec-cmucl
Summary:        Maxima compiled with CMUCL
Group:          Development/Languages/Other
Requires:       maxima = %{version}
Provides:       maxima_exec = %{version}

%description    exec-cmucl
Maxima compiled with CMUCL.
%endif

%if 0%{?enable_sbcl}
%package exec-sbcl
Summary:        Maxima compiled with SBCL
Group:          Development/Languages/Other
Requires:       maxima = %{version}
Requires:       sbcl
Provides:       maxima_exec = %{version}

%description exec-sbcl
Maxima compiled with SBCL.
%endif

%if 0%{?enable_gcl}
%package exec-gcl
Summary:        Maxima compiled with GCL
Group:          Development/Languages/Other
Requires:       maxima = %{version}
Provides:       maxima_exec = %{version}

%description exec-gcl
Maxima compiled with Gnu Common Lisp.
%endif

%package lang-de-utf8
Summary:        Maxima German UTF-8 language pack
Group:          Productivity/Scientific/Math
PreReq:         %install_info_prereq
Requires:       maxima = %{version}
Provides:       locale(maxima:de)

%description lang-de-utf8
Maxima German language support (in UTF-8).

%package lang-es-utf8
Summary:        Maxima Spanish UTF-8 language pack
Group:          Productivity/Scientific/Math
PreReq:         %install_info_prereq
Requires:       maxima = %{version}
Provides:       locale(maxima:es)

%description lang-es-utf8
Maxima Spanish language support (in UTF-8).

%package lang-pt-utf8
Summary:        Maxima Portuguese UTF-8 language pack
Group:          Productivity/Scientific/Math
PreReq:         %install_info_prereq
Requires:       maxima = %{version}
Provides:       locale(maxima:pt)

%description lang-pt-utf8
Maxima Portuguese language support (in UTF-8).

%package lang-pt_BR-utf8
Summary:        Maxima Brazilian Portuguese UTF-8 language pack
Group:          Productivity/Scientific/Math
PreReq:         %install_info_prereq
Requires:       maxima = %{version}
Provides:       locale(maxima:pt_BR)

%description lang-pt_BR-utf8
Maxima Brazilian Portuguese language support (in UTF-8).

%prep
%setup -q
cp %{SOURCE2} doc/info/de/
cp %{SOURCE3} doc/info/pt/

%build
%configure  %{?sbcl_flags:} %{?cmucl_flags:} %{?gcl_flags:} %{?clisp_flags:} \
            --enable-gettext \
            --enable-lang-de-utf8 \
            --enable-lang-es-utf8 \
            --enable-lang-pt-utf8 \
            --enable-lang-pt_BR-utf8 \
            --disable-recode
make %{?_smp_mflags}

%install
%makeinstall install-info
  make \
    prefix=%{?buildroot:%{buildroot}}%{_prefix} \
    exec_prefix=%{?buildroot:%{buildroot}}%{_exec_prefix} \
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
gzip %{buildroot}%{_mandir}/*/*
# reduce space, create symlinks
%fdupes -s %{buildroot}/%{_datadir}/%{name}/%{version}/share %{buildroot}/%{_datadir}/%{name}/%{version}/src

%fdupes %{buildroot}/%{_datadir}/

%suse_update_desktop_file net.sourceforge.maxima.xmaxima

# FIXME CHECKS TAKE TOO LONG AND TIME-OUT
#%%check
#make check
# /FIXME

%if 0%{?suse_version}
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
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS NEWS README README.*
%{_mandir}/man1/maxima.1*
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
%exclude %{_libdir}/maxima/%{version}/binary-clisp
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
%defattr(-,root,root,-)
%dir %{_datadir}/maxima/%{version}/xmaxima
%{_bindir}/xmaxima
%{_datadir}/maxima/%{version}/xmaxima/*
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/xmaxima
%{_datadir}/mime/packages/x-maxima-out.xml
%{_datadir}/pixmaps/*
%{_datadir}/metainfo/*.appdata.xml

%if 0%{?enable_clisp}
%files exec-clisp
%defattr(-,root,root,-)
%dir %{_libdir}/maxima/%{version}/binary-clisp/
%defattr(-,root,root,-)
%{_libdir}/maxima/%{version}/binary-clisp/*
%endif

%if 0%{?enable_cmucl}
%files exec-cmucl
%defattr(-,root,root,-)
%{_libdir}/maxima/%{version}/binary-cmucl/*
%endif

%if 0%{?enable_sbcl}
%files exec-sbcl
%defattr(-,root,root,-)
%{_libdir}/maxima/%{version}/binary-sbcl/*
%endif

%if 0%{?enable_gcl}
%files exec-gcl
%defattr(-,root,root,-)
%{_libdir}/maxima/%{version}/binary-gcl/*
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
