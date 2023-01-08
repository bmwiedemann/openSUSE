#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2009-2010 Pascal Bleser <pascal.bleser@opensuse.org>
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


%define svngroup svn
%define svnuser svn
%define sqlite_minimum_version 3.8.2
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
#Compat macros for SLES 15 SP2 which does not support python_site{arch,lib}
%if 0%{?sle_version} == 150200 && !0%{?is_opensuse}
  %define python_sitearch %{python3_sitearch}
  %define python_sitelib %{python3_sitelib}
%endif
%bcond_without gnome
%bcond_without kde
%bcond_with	python_ctypes
%bcond_with	all_regression_tests
%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "testsuite"
%global psuffix -testsuite
%else
%global psuffix %{nil}
%endif

Name:           subversion%{psuffix}
Version:        1.14.2
Release:        0
Summary:        Subversion version control system
License:        Apache-2.0
URL:            https://subversion.apache.org
Source0:        https://www.apache.org/dist/subversion/subversion-%{version}.tar.bz2
Source1:        subversion.conf
Source2:        subversion.README.SUSE
Source4:        contrib-1804739.tar.bz2
Source10:       subversion.sysconfig.svnserve
Source14:       svnserve.service
Source15:       svnserve.tmpfiles
Source16:       svn.sysusers
Source42:       subversion.svngrep.sh
Source43:       subversion.svndiff.sh
Source50:       https://www.apache.org/dist/subversion/subversion-%{version}.KEYS#/subversion.keyring
Source51:       https://www.apache.org/dist/subversion/subversion-%{version}.tar.bz2.asc
Source92:       subversion-rpmlintrc
Patch0:         subversion-pkgconfig.patch
Patch1:         subversion-1.10.2-javadoc.patch
Patch11:        subversion.libtool-verbose.patch
Patch20:        subversion-swig-perl-install_vendor.patch
Patch23:        subversion-swig-perl-Wall.patch
Patch30:        subversion-1.8.0-rpath.patch
Patch31:        ruby32-fixes.patch
Patch37:        subversion-no-build-date.patch
Patch39:        subversion-fix-parallel-build-support-for-perl-bindings.patch
Patch40:        subversion-perl-underlinking.patch
Patch42:        gcc10-do-not-optimize-get_externals_to_pin.patch
Patch45:        disable-fs-fs-pack-test.patch
# PATCH-FIX-OPENSUSE SLE-11901
Patch46:        remove-kdelibs4support-dependency.patch
# PATCH-FIX-UPSTREAM danilo.spinella@suse.com bsc#1195486 bsc#1193778
# Fix testCrash_RequestChannel_nativeRead_AfterException test on aarch64 and ppc64le
Patch47:        fix-javahl-test.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel >= 2.2.0
BuildRequires:  apache2-prefork
BuildRequires:  db-devel
BuildRequires:  doxygen
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1.8.0
BuildRequires:  junit
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  py3c-devel
BuildRequires:  python3-devel >= 2.7
BuildRequires:  python3-py3c
BuildRequires:  python3-xml
BuildRequires:  ruby-devel >= 1.8.2
BuildRequires:  swig
BuildRequires:  sysuser-tools
BuildRequires:  update-alternatives
BuildRequires:  utf8proc-devel
BuildRequires:  pkgconfig(apr-1) >= 1.3.0
BuildRequires:  pkgconfig(apr-util-1) >= 1.3.0
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(liblz4) >= 1.7
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(serf-1) >= 1.3.4
BuildRequires:  pkgconfig(sqlite3) >= %{sqlite_minimum_version}
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
# in openSUSE Leap 42.3, lz4 was incorrectly packaged
BuildConflicts: pkgconfig(liblz4) = 124
Requires:       libsqlite3-0 >= %{sqlite_minimum_version}
Requires(post): %fillup_prereq
%sysusers_requires
# workaround for boo#969159
Conflicts:      libsvn_auth_kwallet-1-0 < %{version}
Conflicts:      libsvn_auth_kwallet-1-0 > %{version}
Conflicts:      libsvn_gnome_keyring-1-0 < %{version}
Conflicts:      libsvn_gnome_keyring-1-0 > %{version}
Provides:       subversion-javahl = %{version}-%{release}
%{?systemd_requires}
%if %{with all_regression_tests}
# tools required for network based tests
BuildRequires:  net-tools
BuildRequires:  time
BuildRequires:  wget
%endif
%if %{with python_ctypes}
BuildRequires:  ctypesgen
%endif
%if %{with gnome}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libsecret-1)
%endif
%if %{with kde}
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
%else
# In a case we migrate from system that had the kwallet integration we need it
# gone from the package to allow update
Provides:       libsvn_auth_kwallet-1-0 = %{version}
Obsoletes:      libsvn_auth_kwallet-1-0 < %{version}
%endif

%description
Subversion exists to be universally recognized and adopted as an open-source,
centralized version control system characterized by its reliability as a safe
haven for valuable data; the simplicity of its model and usage; and its ability
to support the needs of a wide variety of users and projects, from individuals
to large-scale enterprise operations.

%package devel
Summary:        Development package for Subversion developers
Requires:       libapr-util1-devel
Requires:       subversion = %{version}

%description devel
The subversion-devel package includes the static libraries and include
files for developers interacting with the subversion package.

%package tools
Summary:        Tools for Subversion

%description tools
This package contains some tools for subversion server and
repository admins.

%package perl
Summary:        Allows Perl scripts to directly use Subversion repositories
Requires:       perl = %{perl_version}
Requires:       perl >= 5.8
Requires:       subversion = %{version}

%description perl
Provides Perl (SWIG) support for Subversion version control system.

%package python
Summary:        Allows Python scripts to directly use Subversion repositories
Requires:       subversion = %{version}

%description python
Provides Python (SWIG) support for Subversion version control system.

%if %{with python_ctypes}
%package python-ctypes
Summary:        High-Level Python Bindings for Subversion
Requires:       subversion = %{version}

%description python-ctypes
Provides high-level Python support for Subversion, based on ctypes.
%endif

%package ruby
Summary:        Allows Ruby scripts to directly use Subversion repositories
Requires:       subversion = %{version}

%description ruby
Provides Ruby (SWIG) support for Subversion version control system.

%package server
Summary:        Apache server module for Subversion server
Requires:       %{apache_mmn}
Requires:       apache2
Requires:       subversion = %{version}

%description server
The subversion-server package adds the Subversion server Apache module
to the Apache directories and configuration.

%if %{with kde}
%package -n libsvn_auth_kwallet-1-0
Summary:        KWallet support for Subversion
Requires:       subversion = %{version}
Supplements:    (subversion and kdebase4-workspace)
Supplements:    (subversion and plasma5-workspace)

%description -n libsvn_auth_kwallet-1-0
Provides KWallet integration for Subversion
%endif

%if %{with gnome}
%package -n libsvn_auth_gnome_keyring-1-0
Summary:        GNOME keyring sypport for Subversion
Requires:       subversion = %{version}
Supplements:    (subversion and gnome-session)

%description -n libsvn_auth_gnome_keyring-1-0
Provides GNOME keyring support for Subversion
%endif

%package bash-completion
Summary:        Bash Completion for subversion
Requires:       bash-completion
Requires:       subversion = %{version}
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for subversion - completion of subcommands,
parameters and keywords for the svn command and other tools.

%prep
%setup -q -a 4 -n subversion-%{version}
%patch0 -p1
%patch1 -p1
%patch11 -p1
%patch20 -p1
%patch23 -p1
%patch30 -p1
%patch31 -p1
%patch37 -p1
%patch39
%patch40 -p1
%patch42 -p1
%patch45 -p1
%patch46 -p1
%patch47

# do not use 'env python'
sed -i -e 's#%{_bindir}/env python#%{_bindir}/python3#' subversion/tests/cmdline/*.py

%build
%sysusers_generate_pre %{SOURCE16} subversion system-user-svn.conf
# Re-boot strap, needed for patch37
PATH=%{_prefix}/bin:$PATH ./autogen.sh --release

# Fix timestamp in doxygen
echo "HTML_TIMESTAMP = NO" >> doc/doxygen.conf

cat > with_jdk.files <<EOF-JAVA
%{_libdir}/libsvnjavahl*.so.*
%{_libdir}/libsvnjavahl*.so
%dir %{_libdir}/svn-javahl
%{_libdir}/svn-javahl/svn-javahl.jar
%{_datadir}/java/svn-javahl.jar
EOF-JAVA
# ### these possibly need further discussion
# swig_pydir = @libdir@/svn-python/libsvn
# swig_pydir_extra = @libdir@/svn-python/svn
sed --in-place=~ "
s@^swig_pydir = .*@swig_pydir = %{python_sitearch}/libsvn@
s@^swig_pydir_extra = .*@swig_pydir_extra = %{python_sitearch}/svn@
" Makefile.in
diff -u Makefile.in~ Makefile.in || true
sh -x autogen.sh
for i in subversion/bindings/javahl/native/*.cpp
do
	d=$(sed -n '/^#include "..\/include/{s@^[^/]\+\([^"]\+\).*@subversion/bindings/javahl\1@;H};${x;s@\n@ @gp}' $i)
	echo
	echo "# $i"
	if ! test -z "$d"
	then
		echo ${i%.cpp}.lo: $d
	fi
	echo
done >> build-outputs.mK
export CFLAGS="%{apache_cflags} %{optflags} -fstack-protector -fpie"
export CXXFLAGS="$CFLAGS"
export APACHE_LDFLAGS="-Wl,-z,relro,-z,now"
export LDFLAGS="-pie"
%configure \
	--enable-local-library-preloading \
	--with-editor="vim -c 'set tw=72 et' " \
	--with-serf=%{_prefix} \
	--with-apr=%{_prefix} \
	--with-apr-util=%{_prefix} \
	--with-apxs=%{apache_apxs} \
	--with-zlib=%{_prefix} \
	--with-berkeley-db=db.h:db.h:%{_prefix}:db \
	--with-apache-libexecdir=%{apache_libexecdir} \
	--with-jdk=%{_libdir}/jvm/java --enable-javahl \
	--with-junit="%{_datadir}/java/junit.jar" \
	--with-jikes=no \
	--with-sqlite="%{_prefix}" \
	--enable-sqlite-compatibility-version=%{sqlite_minimum_version} \
%if %{with gnome}
	--with-gnome-keyring \
%endif
%if %{with kde}
	--with-kwallet \
%endif
	--disable-mod-activation \
	--with-libmagic \
	--disable-static \
	--enable-broken-httpd-auth
%make_build
%make_build doc-api

# Bindings
%make_build extraclean-bindings
%make_build swig-py swig-rb swig-pl
%if %{with python_ctypes}
%make_build ctypes-python
%endif
# Java is not thread safe
%make_build -j1 JAVAC_FLAGS=" -encoding iso8859-1" javahl doc-javahl

%install
%if "%{flavor}" != "testsuite"
%make_install
make DESTDIR=%{buildroot} install-swig-py install-swig-pl install-javahl install-swig-rb
%if %{with python_ctypes}
make DESTDIR=%{buildroot} install-ctypes-python
# remove csvn .pyc files and recompile them because they contain the $RPM_BUILD_ROOT path:
find "%{buildroot}%{python_sitelib}/csvn/" -name "*.pyc" | xargs rm -f
%py_compile %{buildroot}/%{python_sitelib}/csvn
%endif

%perl_process_packlist
%find_lang subversion

cp -Lav %{SOURCE42} %{buildroot}%{_bindir}/svngrep
cp -Lav %{SOURCE43} %{buildroot}%{_bindir}/svndiff

mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/
cp -avL contrib/client-side/emacs/*.el %{buildroot}%{_datadir}/emacs/site-lisp/
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/vc-svn.el

cp -avL contrib/client-side/svn_apply_autoprops.py %{buildroot}%{_bindir}

mkdir -p %{buildroot}/%{apache_sysconfdir}/conf.d
cp -av %{SOURCE1} %{buildroot}/%{apache_sysconfdir}/conf.d/subversion.conf

cp -avL %{SOURCE2} README.SUSE
cp -avL subversion/mod_authz_svn/INSTALL README.mod_authz_svn
cat subversion.lang > files.subversion
cat with_jdk.files >> files.subversion

# tools
make DESTDIR=%{buildroot} install-tools
mv -v %{buildroot}%{_bindir}/svn-tools/{fsfs-access-map,svnauthz,svnauthz-validate,svn-populate-node-origins-index,svnraisetreeconflict} %{buildroot}%{_bindir}
# discard all other tools
rm -rf %{buildroot}%{_bindir}/svn-tools
# replicate svn-bench compatibility link
ln -sf svnbench %{buildroot}%{_bindir}/svn-bench

mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 -D %{SOURCE10} %{buildroot}%{_fillupdir}/sysconfig.svnserve
install -d -m 0755 %{buildroot}/srv/svn

install -m 644 -D %{SOURCE14} %{buildroot}/%{_unitdir}/svnserve.service
ln -sv service %{buildroot}%{_sbindir}/rcsvnserve
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
install -m 0644 %{SOURCE15} %{buildroot}/%{_tmpfilesdir}/svnserve.conf

#useless libtool stuff
rm -rf %{buildroot}%{python_sitearch}/*/*.{a,la}
rm -rf %{buildroot}%{_libdir}/libsvn_swig_*.{so,la,a}
rm -rf %{buildroot}%{rb_sitelib}/svn/ext/*.*a
find %{buildroot} -type f -name "*.la" -delete -print

# remove stuff produced with Perl modules
find %{buildroot} -type f \
    -a \( -name .packlist -o \( -name '*.bs' -a -empty \) \) \
    -print0 | xargs -0 rm -f

# make Perl modules writable so they get stripped
find %{buildroot}%{_prefix}/lib/perl5 -type f -perm 555 -print0 |
    xargs -0 chmod 755

install -d -m 0755 %{buildroot}/%{_datadir}/java
ln -sv %{_libdir}/svn-javahl/svn-javahl.jar %{buildroot}/%{_datadir}/java/svn-javahl.jar
rm -f %{buildroot}%{_localstatedir}/adm/perl-modules/subversion

install -D -m0644 tools/client-side/bash_completion %{buildroot}%{_datadir}/bash-completion/completions/subversion

# examples
mkdir -p %{buildroot}%{_docdir}/subversion
cp -r tools/hook-scripts tools/backup tools/bdb tools/examples tools/xslt %{buildroot}%{_docdir}/subversion
find %{buildroot}%{_docdir}/subversion -type f -print0 | xargs -0 chmod 644

# clean tools for doc
rm -rf tools/*/*.in
rm -rf doc/doxygen/html/installdox

# sysusers
install -Dm0644 %{SOURCE16} %{buildroot}%{_sysusersdir}/system-user-svn.conf
%endif

%if "%{flavor}" == "testsuite"
%check
export LANG=C LC_ALL=C

echo "========= mount RAM disc"
test ! -e /dev/shm/svn-test-work && mkdir /dev/shm/svn-test-work
test -e subversion/tests/cmdline/svn-test-work && rm -rf subversion/tests/cmdline/svn-test-work
ln -s /dev/shm/svn-test-work subversion/tests/cmdline/

%make_build -Onone check FS_TYPE=fsfs CLEANUP=true || (cat fails.log; exit 1)
%make_build -Onone check-javahl || (cat fails.log; exit 1)
%make_build -Onone check-swig-pl || (cat fails.log; exit 1)
%if 0%{?suse_version} <= 1500
# swig bindings check failing from swig 4.0.0 and later
%make_build check-swig-py || (cat fails.log; exit 1)
%endif
%make_build check-swig-rb || (cat fails.log; exit 1)
%if %{with all_regression_tests}
%make_build svnserveautocheck CLEANUP=true FS_TYPE=fsfs || (cat fails.log; exit 1)
%make_build svnserveautocheck CLEANUP=true FS_TYPE=bdb || (cat fails.log; exit 1)
%make_build davautocheck CLEANUP=true FS_TYPE=fsfs || (cat fails.log; exit 1)
%make_build davautocheck CLEANUP=true FS_TYPE=bdb || (cat fails.log; exit 1)
%endif

%else

%pre -f subversion.pre
%service_add_pre svnserve.service

%preun
%service_del_preun svnserve.service

%post
%{fillup_only -n svnserve svnserve}
%service_add_post svnserve.service
systemd-tmpfiles --create %{_tmpfilesdir}/svnserve.conf
/sbin/ldconfig

%postun
%service_del_postun svnserve.service
/sbin/ldconfig

%post -n subversion-python -p /sbin/ldconfig
%postun -n subversion-python -p /sbin/ldconfig
%post -n subversion-perl -p /sbin/ldconfig
%postun -n subversion-perl -p /sbin/ldconfig
%post -n subversion-ruby -p /sbin/ldconfig
%postun -n subversion-ruby -p /sbin/ldconfig

%if %{with gnome}
%post -n libsvn_auth_gnome_keyring-1-0 -p /sbin/ldconfig
%postun -n libsvn_auth_gnome_keyring-1-0 -p /sbin/ldconfig
%endif

%if %{with kde}
%post -n libsvn_auth_kwallet-1-0 -p /sbin/ldconfig
%postun -n libsvn_auth_kwallet-1-0 -p /sbin/ldconfig
%endif

%files -f files.subversion
%license LICENSE
%doc README.SUSE BUGS CHANGES README.mod_authz_svn
%dir %{_docdir}/subversion/*
%{_docdir}/subversion
%{_sbindir}/rcsvnserve
%{_fillupdir}/sysconfig.svnserve
%dir %attr(755,%{svnuser},%{svngroup}) /srv/svn
%{_unitdir}/svnserve.service
%{_tmpfilesdir}/svnserve.conf
%{_sysusersdir}/system-user-svn.conf
%attr(755,root,root) %{_bindir}/svn
%attr(755,root,root) %{_bindir}/svnadmin
%attr(755,root,root) %{_bindir}/svndiff
%attr(755,root,root) %{_bindir}/svndumpfilter
%attr(755,root,root) %{_bindir}/svnfsfs
%attr(755,root,root) %{_bindir}/svngrep
%attr(755,root,root) %{_bindir}/svnlook
%attr(755,root,root) %{_bindir}/svnmucc
%attr(755,root,root) %{_bindir}/svnrdump
%attr(755,root,root) %{_bindir}/svnserve
%attr(755,root,root) %{_bindir}/svnsync
%attr(755,root,root) %{_bindir}/svnversion
%{_libdir}/libsvn_client*.so.*
%{_libdir}/libsvn_delta*.so.*
%{_libdir}/libsvn_diff*.so.*
%{_libdir}/libsvn_fs*.so.*
%{_libdir}/libsvn_ra*.so.*
%{_libdir}/libsvn_repos*.so.*
%{_libdir}/libsvn_subr*.so.*
%{_libdir}/libsvn_wc*.so.*
%{_mandir}/man?/svn*
%{_datadir}/emacs

%files perl
%{_mandir}/man?/SVN::*
%{_libdir}/libsvn_swig_perl-1.so.*
%{perl_vendorarch}/SVN
%{perl_vendorarch}/auto/SVN

%files python
%dir %{python_sitearch}
%dir %{python_sitearch}/svn
%dir %{python_sitearch}/libsvn
%{_libdir}/libsvn_swig_py-1.so.*
%{python_sitearch}/libsvn/*
%{python_sitearch}/svn/*

%if %{with python_ctypes}
%files python-ctypes
%doc subversion/bindings/ctypes-python/examples
%dir %{python_sitelib}
%{python_sitelib}/csvn
%{python_sitelib}/svn_ctypes_python_bindings-*-py%{py_ver}.egg-info
%endif

%files ruby
%dir %{rb_sitelib}
%{rb_sitelib}/svn
%{rb_sitelib}/*/svn
%{_libdir}/libsvn_swig_ruby-1.so.*

%files devel
%dir %{_includedir}/subversion-1
%{_libdir}/libsvn_*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/subversion-1/*
%doc doc/doxygen/html

%files tools
%{_bindir}/fsfs-access-map
%attr(755,root,root) %{_bindir}/svn_apply_autoprops.py
%{_bindir}/svnauthz
%{_bindir}/svnauthz-validate
%{_bindir}/svnbench
%{_bindir}/svn-bench
%{_bindir}/svn-populate-node-origins-index
%{_bindir}/svnraisetreeconflict

%files server
%dir %{apache_sysconfdir}/conf.d
%config (noreplace) %{apache_sysconfdir}/conf.d/subversion.conf
%dir %{apache_libexecdir}
%{apache_libexecdir}/mod_dav_svn.*
%{apache_libexecdir}/mod_authz_svn.*
%{apache_libexecdir}/mod_dontdothat.*

%if %{with gnome}
%files -n libsvn_auth_gnome_keyring-1-0
%{_libdir}/libsvn_auth_gnome_keyring-1.so.0
%{_libdir}/libsvn_auth_gnome_keyring-1.so.0.*
%endif

%if %{with kde}
%files -n libsvn_auth_kwallet-1-0
%{_libdir}/libsvn_auth_kwallet-1.so.0
%{_libdir}/libsvn_auth_kwallet-1.so.0.*
%endif

%files bash-completion
%{_datadir}/bash-completion/completions/subversion
%endif

%changelog
