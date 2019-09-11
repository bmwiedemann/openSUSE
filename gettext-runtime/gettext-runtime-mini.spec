#
# spec file for package gettext-runtime-mini
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


%define pacname gettext
# datadir was not changed in 0.19.8.1 patch release
%define dataversion 0.19.8
%bcond_without mini

Name:           gettext-runtime-mini
Version:        0.19.8.1
Release:        0
BuildRequires:  gcc-c++
BuildRequires:  libtool
# To get an updated linkdupes.sh (in case there are new dupes), temproarily enable:
#BuildRequires: fdupes
%if %{without mini}
BuildRequires:  glib2-devel
BuildRequires:  libcroco-devel
BuildRequires:  libxml2-devel
BuildRequires:  perl-libintl-perl
BuildRequires:  tcl
BuildRequires:  xz
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
# rpm-build requires gettext-tools, but we will only just be building it
#!BuildIgnore:  gettext-tools
%endif
Summary:        Tools for Native Language Support (NLS)
License:        GPL-3.0-or-later AND LGPL-2.0-or-later
Group:          Development/Tools/Other
Url:            http://www.gnu.org/software/gettext/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz
Source1:        gettext-rpmlintrc
Source2:        suse-start-po-mode.el
Source3:        gettext-linkdupes.sh
Source4:        baselibs.conf
Source5:        http://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz.sig
Source6:        %name.keyring
Patch:          gettext-0.12.1-sigfpe.patch
Patch1:         gettext-0.19.3-fix-bashisms.patch
Patch2:         gettext-0.12.1-gettextize.patch
Patch4:         gettext-po-mode.diff
Patch5:         gettext-initialize_vars.patch
# PATCH-FIX-OPENSUSE gettext-dont-test-gnulib.patch -- coolo@suse.de 
Patch6:         gettext-dont-test-gnulib.patch
Patch9:         gettext-needlessly_init_vars.patch
# PATCH-FIX-UPSTREAM https://savannah.gnu.org/bugs/?49654 -- bmwiedemann@opensuse.org
Patch10:        msgfmt-remove-pot-creation-date.patch
# PATCH-FIX-UPSTREAM boo#941629 -- pth@suse.com
Patch11:        boo941629-unnessary-rpath-on-standard-path.patch
# PATCH-FIX-SUSE Bug boo#1106843 
Patch12:        msgfmt-reset-msg-length-after-remove.patch
Patch13:        reproducible.patch

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
Conflicts:      gettext-tools-mini
Conflicts:      gettext-runtime-mini
%else
# to allow a prjconf preference which to take per build
Provides:       gettext-tools = %{version}
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

%prep
%setup -q -n %{pacname}-%{version}
%patch
%patch1 -p1
%patch2
%patch4
%patch5
%patch6 -p1
%patch9
%patch10 -p1
%patch11 -p1
%patch12 -p0
%patch13 -p1

%build
%define _lto_cflags %{nil}
# expect a couple "You should update your `aclocal.m4' by running aclocal."
autoreconf -fiv
#sh autogen.sh
export CFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint"
export CXXFLAGS="$CFLAGS -Dgcc_is_lint"
%if 0%{?qemu_user_space_build:1}
  OPTS="--disable-openmp"
%endif
%configure --enable-shared $OPTS
make %{?_smp_mflags} GMSGFMT=../src/msgfmt V=1
# use texinfo.tex supplied by the system (texinfo)
# make -C gettext-tools/doc gettext.pdf

%install
%define my_docdir %{_defaultdocdir}/%{name}
export LC_CTYPE=ISO-8859-15
make install DESTDIR=%{buildroot} docdir=%{my_docdir}
cp -pr AUTHORS NEWS README*	%{buildroot}/%{my_docdir}
mkdir -p %{buildroot}/usr/share/emacs/site-lisp
install -m 644 %SOURCE2 %{buildroot}/usr/share/emacs/site-lisp
install -m 644 gettext-tools/misc/po-compat.el %{buildroot}/usr/share/emacs/site-lisp
install -m 644 gettext-tools/misc/po-mode.el %{buildroot}/usr/share/emacs/site-lisp
install -m 644 gettext-tools/misc/start-po.el %{buildroot}/usr/share/emacs/site-lisp
#make -C gettext-tools/doc docdir=%{buildroot}/%{my_docdir} install-pdf
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
#find %{buildroot} -maxdepth 2 -name '*html' | xargs rm -f
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

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%post -n gettext-tools%{?with_mini:-mini}
%install_info --info-dir=%{_infodir} %{_infodir}/gettext.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/autosprintf.info.gz

%preun -n gettext-tools%{?with_mini:-mini}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gettext.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/autosprintf.info.gz

%files -f gettext-runtime.lang
%defattr(-,root,root)
%license COPYING
%dir %_datadir/gettext
%doc %dir %_docdir/%name/
%doc %_docdir/%name/gettext.1.html
%doc %_docdir/%name/ngettext.1.html
%doc %_docdir/%name/envsubst.1.html
%doc %_docdir/%name/*.3.html
%doc %_docdir/%name/AUTHORS
%doc %_docdir/%name/NEWS
%doc %_docdir/%name/README
%doc %_docdir/%name/FAQ.html
%_bindir/gettext
%_bindir/ngettext
%_bindir/envsubst
%_bindir/gettext.sh
%_bindir/msgfmt
%_libdir/libgettextlib-*.so
%_libdir/libgettextsrc-*.so
%_libdir/libasprintf.so.*
%doc %_mandir/man1/gettext.1.gz
%doc %_mandir/man1/ngettext.1.gz
%doc %_mandir/man1/envsubst.1.gz
%doc %_mandir/man1/msgfmt.1.gz
%doc %_mandir/man3/*
%_datadir/gettext/ABOUT-NLS
%dir %_datadir/emacs
%dir %_datadir/emacs/site-lisp
%_datadir/emacs/site-lisp/po-compat.*
%_datadir/emacs/site-lisp/po-mode.*
%_datadir/emacs/site-lisp/start-po.*
%_datadir/emacs/site-lisp/suse-start-po-mode.el

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
%_datadir/%pacname/intl
%_datadir/%pacname/po
%_datadir/%pacname/projects
%_datadir/%pacname/gettext.h
%_datadir/%pacname/msgunfmt.tcl
%_datadir/%pacname/javaversion.class
%_datadir/%pacname/styles
%_datadir/%pacname/archive.dir.tar.xz
%_datadir/aclocal/*
%dir %{_datadir}/%{pacname}-%{dataversion}
%{_datadir}/%{pacname}-%{dataversion}/its

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

%changelog
