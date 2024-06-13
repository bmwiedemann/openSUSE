#
# spec file for package gettext-runtime-mini
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


%define pacname gettext
%bcond_without mini

Name:           gettext-runtime-mini
Version:        0.22.5
Release:        0
BuildRequires:  automake >= 1.14
BuildRequires:  gcc-c++
BuildRequires:  glibc-gconv-modules-extra
BuildRequires:  libtool
# To get an updated linkdupes.sh (in case there are new dupes), temproarily enable:
#BuildRequires: fdupes
%if %{without mini}
BuildRequires:  glib2-devel
BuildRequires:  libxml2-devel
BuildRequires:  perl-libintl-perl
BuildRequires:  tcl
# bug437293
%ifarch ppc64
Obsoletes:      gettext-64bit
%endif
#
#Rename done for openSUSE 11.0
Provides:       gettext = %{version}
Obsoletes:      gettext < %{version}
Conflicts:      gettext-runtime-mini
Conflicts:      gettext-tools-mini
%else
# to allow a prjconf preference which to take per build
Provides:       gettext-runtime = %{version}
# Ensure this never finds its way onto a real installation
Requires:       this-is-only-for-build-envs
# rpm-build requires gettext-tools, but we will only just be building it
#!BuildIgnore:  gettext-tools
%endif
Summary:        Tools for Native Language Support (NLS)
License:        GPL-3.0-or-later AND LGPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://www.gnu.org/software/gettext/
Source0:        https://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz.sig
Source2:        suse-start-po-mode.el
Source3:        gettext-linkdupes.sh
Source4:        baselibs.conf
Source5:        gettext-rpmlintrc
Source6:        gettext-runtime.keyring
Patch0:         gettext-0.12.1-sigfpe.patch
Patch1:         gettext-0.19.3-fix-bashisms.patch
Patch2:         gettext-0.12.1-gettextize.patch
Patch3:         use-acinit-for-libtextstyle.patch
Patch4:         gettext-po-mode.diff
Patch5:         gettext-initialize_vars.patch
# PATCH-FIX-OPENSUSE gettext-dont-test-gnulib.patch -- coolo@suse.de
Patch6:         gettext-dont-test-gnulib.patch
# PATCH-FIX-UPSTREAM boo#941629 -- pth@suse.com
Patch11:        boo941629-unnessary-rpath-on-standard-path.patch
# PATCH-FIX-SUSE Bug boo#1106843
Patch13:        reproducible.patch
# PATCH-FEATURE bsc#1165138
Patch14:        0001-msgcat-Add-feature-to-use-the-newest-po-file.patch
Patch15:        0002-msgcat-Merge-headers-when-use-first.patch

%description
This package contains the intl library as well as tools that ease the
creation and maintenance of message catalogs. It allows you to extract
strings from source code. The supplied Emacs mode (po-mode.el) helps
editing these catalogs (called PO files, for portable object) and
adding translations. A special compiler turns these PO files into
binary catalogs.

%package     -n gettext-tools%{?with_mini:-mini}
Summary:        Tools for Native Language Support (NLS)
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       xz
# gettext.sh requires envsubst
Requires:       envsubst%{?with_mini:-mini} = %{version}
# autopoint requires find
Requires:       findutils
# For non-UTF encodings
Requires:       glibc-gconv-modules-extra
%if %{without mini}
Requires(post): info
Requires(preun): info
%endif
Provides:       gettext-devel = %{version}
%if %{without mini}
# bug437293
%ifarch ppc64
Obsoletes:      gettext-devel-64bit
%endif
#
Obsoletes:      gettext-devel < %{version}
Conflicts:      gettext-runtime-mini
Conflicts:      gettext-tools-mini
%else
# to allow a prjconf preference which to take per build
Provides:       gettext-tools = %{version}
# Ensure this never finds its way onto a real installation
Requires:       this-is-only-for-build-envs
%endif
# Several tools use bison-runtime text domain:
%if 0%{?suse_version}
Recommends:     bison-lang
%endif

%description -n gettext-tools%{?with_mini:-mini}
This package contains the `intl' library as well as tools that ease the
creation and maintenance of message catalogs. With it you can extract
strings from source code. The supplied Emacs mode (po-mode.el) will aid
in editing these catalogs (called PO files, for portable object) and
add translations. A special compiler will turn these PO files into
binary catalogs.

%package tools-doc
Summary:        HTML documentation and examples for gettext-runtime
License:        GPL-3.0-or-later AND LGPL-2.0-or-later
Group:          Documentation/HTML
BuildArch:      noarch

%description tools-doc
This subpackage contains the HTML version of the gettext documentation
as well as project examples.

%package -n envsubst%{?with_mini:-mini}
Summary:        Environment substitution helper binary
%if %{with mini}
Conflicts:      envsubst
Requires:       this-is-only-for-build-envs
%endif

%description -n envsubst%{?with_mini:-mini}
This package contains the envsubst helper binary to replace values from the
environment.

%if %{without mini}
%package     -n libtextstyle0
Summary:        Provides textstyling for console output
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other

%description -n libtextstyle0
GNU libtextstyle provides an easy way to add styling to programs that produce output to a console or terminal emulator window.
It does this in a way that allows the end user to customize the styling using the industry standard, namely Cascading Style Sheets (CSS).

%package     -n libtextstyle-devel
Summary:        Devel package for libtextstyle
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
Requires:       libtextstyle0 = %{version}

%description -n libtextstyle-devel
This package provides headers and static libraries for libtextstyle
%endif

%prep
%setup -q -n %{pacname}-%{version}
%patch -P 0
%patch -P 1 -p1
%patch -P 2
%patch -P 3 -p1
%patch -P 4
%patch -P 5
%patch -P 6 -p1
%patch -P 11 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1

%build
%define _lto_cflags %{nil}
# expect a couple "You should update your `aclocal.m4' by running aclocal."
autoreconf -fiv
export CFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint"
export CXXFLAGS="$CFLAGS -Dgcc_is_lint"
export LDFLAGS="-lm"
%configure --disable-static $OPTS
%if %{with mini}
# Link statically to libtextstyle from libgettextlib.so
export CFLAGS="${CFLAGS} -fPIC"
export CXXFLAGS="${CXXFLAGS} -fPIC"
(cd libtextstyle; %configure --enable-static --disable-shared ${OPTS})
%endif
make %{?_smp_mflags} GMSGFMT=../src/msgfmt V=1
# use texinfo.tex supplied by the system (texinfo)
# make -C gettext-tools/doc gettext.pdf

%install
%define my_docdir %{_defaultdocdir}/%{name}
export LC_CTYPE=ISO-8859-15
%make_install docdir=%{my_docdir}
cp -pr AUTHORS NEWS README*	%{buildroot}/%{my_docdir}
mkdir -p %{buildroot}/usr/share/emacs/site-lisp
install -m 644 %SOURCE2 %{buildroot}/usr/share/emacs/site-lisp
install -m 644 gettext-tools/emacs/po-compat.el %{buildroot}/usr/share/emacs/site-lisp
install -m 644 gettext-tools/emacs/po-mode.el %{buildroot}/usr/share/emacs/site-lisp
install -m 644 gettext-tools/emacs/start-po.el %{buildroot}/usr/share/emacs/site-lisp
#make -C gettext-tools/doc docdir=%%{buildroot}/%%{my_docdir} install-pdf
if [ -e %{buildroot}/%{_libdir}/preloadable_libintl.so ];then
	chmod 755 %{buildroot}/%{_libdir}/preloadable_libintl.so
fi
# fix rpmlint invalid-lc-messages-dir:
rm -rf %{buildroot}/%_datadir/locale/en@{bold,}quot
%{find_lang} gettext-tools
%{find_lang} gettext-runtime
#remove unwanted stuff
rm -f %{buildroot}/usr/share/doc/packages/gettext/README.{mingw,vms,woe32}
rm -f %_datadir/%name/gettext.jar
rm -f %{buildroot}/%_libdir/libtextstyle.la
%if %{with mini}
	rm -f %{buildroot}/usr/include/textstyle.h
	rm -rf %{buildroot}/usr/include/textstyle
	rm -rf %{buildroot}/usr/share/doc/packages/gettext-runtime-mini/libtextstyle_*.html
	rm -f %{buildroot}/%_libdir/libtextstyle.a
	rm  -f %{buildroot}/%{_infodir}/libtextstyle.info
%endif
#find %%{buildroot} -maxdepth 2 -name '*html' -delete
# hardlink the dupes in the documentation:
cd %{buildroot}/%{my_docdir}/examples
sh %{SOURCE3}
# moved to gettext-java and gettext-csharp:
rm -rf *csharp* *java* ../javadoc* ../csharpdoc*
rm -f %{buildroot}%{_defaultdocdir}/%name/README.woe32
rm -f %{buildroot}%{_infodir}/dir
cd %{buildroot}/%{_mandir}/man3
echo ".so man3/dngettext.3" > dcngettext.3
echo ".so man3/dgettext.3" > dcgettext.3

%if %{without mini}
%check
# s390s fails this test,
# Starting test_recursive_lock ...test-lock: pthread_mutex_lock.c:66: __pthread_mutex_lock: Assertion `mutex->__data.__owner == 0' failed.

# These fails randomly, remove them from Makefile
sed -i -e 's/test-areadlink\$(EXEEXT) //g' \
 -e 's/test-readlink\$(EXEEXT) //g' \
 gettext-tools/gnulib-tests/Makefile

make check || {
%ifarch s390x
	echo "got this during mbuild testing on s390x (on both times which make check ran):"
	echo "Starting test_recursive_lock ...test-lock: pthread_mutex_lock.c:66: __pthread_mutex_lock: Assertion mutex->__data.__owner == 0 failed."
	echo "s390x needs kernel/glibc/gcc fix, but let it continue bootstrap for now!"
%else
	echo "make check failed, check it!"
	exit 5
%endif
}
%endif

%post -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%post -n gettext-tools%{?with_mini:-mini}
%install_info --info-dir=%{_infodir} %{_infodir}/gettext.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/autosprintf.info.gz

%preun -n gettext-tools%{?with_mini:-mini}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gettext.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/autosprintf.info.gz

%if %{without mini}
%post   -n libtextstyle0 -p /sbin/ldconfig
%postun -n libtextstyle0 -p /sbin/ldconfig
%endif

%files -f gettext-runtime.lang
%defattr(-,root,root)
%license COPYING
%dir %_datadir/gettext
%doc %dir %_docdir/%name/
%doc %_docdir/%name/gettext.1.html
%doc %_docdir/%name/ngettext.1.html
%doc %_docdir/%name/*.3.html
%doc %_docdir/%name/AUTHORS
%doc %_docdir/%name/NEWS
%doc %_docdir/%name/README
%doc %_docdir/%name/FAQ.html
%_bindir/gettext
%_bindir/ngettext
%_bindir/gettext.sh
%_bindir/msgfmt
%_libdir/libgettextlib-*.so
%_libdir/libgettextsrc-*.so
%_libdir/libasprintf.so.*
%doc %_mandir/man1/gettext.1.gz
%doc %_mandir/man1/ngettext.1.gz
%doc %_mandir/man1/msgfmt.1.gz
%doc %_mandir/man3/*
%_datadir/gettext/ABOUT-NLS
%dir %_datadir/emacs
%dir %_datadir/emacs/site-lisp
%_datadir/emacs/site-lisp/po-compat.*
%_datadir/emacs/site-lisp/po-mode.*
%_datadir/emacs/site-lisp/start-po.*
%_datadir/emacs/site-lisp/suse-start-po-mode.el

%files -n envsubst%{?with_mini:-mini}
%license COPYING
%_bindir/envsubst
%doc %_mandir/man1/envsubst.1.gz
%doc %_docdir/%name/envsubst.1.html

%files -n gettext-tools%{?with_mini:-mini} -f gettext-tools.lang
%defattr(-,root,root)
%_bindir/msg[a-eg-u]*
%_bindir/msgfilter
%_bindir/xgettext
%_bindir/gettextize
%_bindir/autopoint
%_bindir/recode-sr-latin
%doc %_mandir/man1/msg[a-eg-u]*.1.gz
%doc %_mandir/man1/msgfilter.1.gz
%doc %_mandir/man1/xgettext.1.gz
%doc %_mandir/man1/gettextize.1.gz
%doc %_mandir/man1/autopoint.1.gz
%doc %_mandir/man1/recode-sr-latin.1.gz
%doc %_infodir/gettext.info*
%doc %_infodir/autosprintf.info*
%_includedir/gettext-po.h
%_includedir/autosprintf.h
%_libdir/libasprintf.*a
%_libdir/libasprintf.so
%_libdir/libgettextlib.*
%_libdir/libgettextsrc.*
%_libdir/libgettextpo*
%_libdir/preloadable_libintl.so
%_libdir/gettext
%_datadir/%pacname/config.rpath
%_datadir/%pacname/po
%_datadir/%pacname/projects
%_datadir/%pacname/gettext.h
%_datadir/%pacname/msgunfmt.tcl
%_datadir/%pacname/javaversion.class
%_datadir/%pacname/styles
%_datadir/%pacname/archive.dir.tar.xz
%_datadir/aclocal
%dir %{_datadir}/%{pacname}-%{version}
%{_datadir}/%{pacname}-%{version}/its

%files tools-doc
%defattr(-,root,root)
%doc %dir %_docdir/%name/
%doc %_docdir/%name/examples/
%doc %_docdir/%name/auto*.html
%doc %_docdir/%name/gettext_*.html
%doc %_docdir/%name/gettextize*.html
%doc %_docdir/%name/msg*.html
%doc %_docdir/%name/tutorial*.html
%doc %_docdir/%name/xgettext*.html
%doc %_docdir/%name/recode-sr-latin.1.html

%if %{without mini}
%files -n libtextstyle0
%defattr(-,root,root)
%_libdir/libtextstyle.so.*

%files -n libtextstyle-devel
%defattr(-,root,root)
%dir %_includedir/textstyle
%_includedir/textstyle.h
%_includedir/textstyle/stdbool.h
%_includedir/textstyle/version.h
%_includedir/textstyle/woe32dll.h
%_libdir/libtextstyle.so
%doc %_docdir/gettext-runtime%{?with_mini:-mini}/libtextstyle*.html
%doc %_infodir/libtextstyle.info.gz
%endif

%changelog
