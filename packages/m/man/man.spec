#
# spec file for package man
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


%global         _sysconfdir %{_sysconfdir}
%global         _has_tmpfiled  %(rpm -q -f %{_prefix}/lib/tmpfiles.d | grep -c filesystem)
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%bcond_without  sdtimer
Name:           man
Version:        2.8.4
Release:        0
Summary:        A Program for Displaying man Pages
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://savannah.nongnu.org/projects/man-db
Source:         http://download.savannah.gnu.org/releases/man-db/man-db-%{version}.tar.xz
Source1:        sysconfig.cron-man
Source2:        cron.daily.do_mandb
Source4:        mancoding
Source5:        wrapper.c
Source6:        man-rpmlintrc
Source7:        man-db-create.service
Source8:        mandb.timer
Source9:        mandb.service
Source10:       man-db-2.6.3-man0.dif
Source11:       http://download.savannah.gnu.org/releases/man-db/man-db-%{version}.tar.xz.asc
Source12:       https://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=man-db&download=1#/%{name}.keyring
Patch0:         man-db-2.8.4.dif
Patch2:         man-db-2.3.19deb4.0-groff.dif
Patch4:         man-db-2.6.3-section.dif
Patch5:         man-db-2.7.1-security4.dif
Patch6:         man-db-2.7.1-firefox.dif
Patch7:         man-db-2.6.3-chinese.dif
Patch9:         man-db-2.7.1-zio.dif
Patch10:        man-db-2.6.3-listall.dif
# PATCH-FIX-SUSE Fixes the documentation for bnc#786679
Patch11:        man-MAN_POSIXLY_CORRECT-man1.dif
# PATCH-FIX-SUSE Fixes build-compare bnc#971922
Patch12:        reproducible.patch
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gdbm-devel
BuildRequires:  gettext-runtime
BuildRequires:  gettext-tools
BuildRequires:  groff
BuildRequires:  less
BuildRequires:  libbz2-devel
BuildRequires:  libpipeline-devel >= 1.5.0
BuildRequires:  libzio-devel
BuildRequires:  man-pages
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  update-alternatives
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(systemd)
Requires:       glibc-locale
Requires:       groff >= 1.18
Requires:       less
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         coreutils
PreReq:         fillup
Requires(post): update-alternatives
Requires(posttrans): systemd
Requires(postun): update-alternatives
Requires(pre):  group(man)
Requires(pre):  user(man)
Provides:       man_db
%if 0%{?suse_version} < 1500
Requires:       cron
%endif

%description
A program for displaying man pages on the screen or sending them to a
printer (using groff).

%prep
%setup -q -n man-db-%{version}
%patch2   -b .groff
%patch4   -b .sect
%patch5   -b .secu4
%patch6   -b .firefox
%patch7   -b .chinese
%patch9   -b .zio
%patch10  -b .listall
%patch11  -b .p11
%patch12 -p1 -b .p12
%patch0   -b .0

%build
    gettextize --force --copy --no-changelog
    SEC=(0 1 n l 8 3 2 5 4 9 6 7
	 1x 3x 4x 5x 6x 8x
	 1bind 3bind 5bind 7bind 8bind
	 1cn 8cn
	 1m 1mh 5mh 8mh
	 1netpbm 3netpbm 5netpbm
	 0p 1p 3p 3posix
	 1pgsql 3pgsql 5pgsql
	 3C++ 8C++
	 3blt
	 3curses 3ncurses 3form 3menu
	 3db 3gdbm 3f 3gk 3paper
	 3mm 5mm
	 3perl 3pm 3pq
	 3qt 3pub 3readline
	 1ssl 3ssl 5ssl 7ssl
	 3t 3tk 3tcl 3tclx 3tix
	 7l 7nr
	 8c
	 Cg g s m)
    SEC="${SEC[@]}"
    rm -f configure
%global optflags %{optflags} -funroll-loops -pipe -Wall
    if grep -q _DEFAULT_SOURCE %{_includedir}/features.h ; then
	CFLAGS="%{optflags} -D_GNU_SOURCE -D_DEFAULT_SOURCE"
    else
	CFLAGS="%{optflags} -D_GNU_SOURCE -D_SVID_SOURCE"
    fi
    LDFLAGS=
    LIBS=
    LINGUAS=
    for d in $(cat man/LINGUAS*) ; do
	test -d %{_datadir}/locale/$d || continue
	LINGUAS="${LINGUAS:+$LINGUAS }$d"
    done
    export CFLAGS LDFLAGS LIBS LINGUAS
    aclocal  -I ${PWD} -I ${PWD}/m4 -I ${PWD}/gl/m4
    autoconf -B ${PWD} -B ${PWD}/m4 -B ${PWD}/gl/m4
    automake --add-missing
    find -name 'Makefile.*' | xargs \
	sed -ri -e '/^pkglibdir/{ s@^(pkglibdir[[:blank:]]+=[[:blank:]]+\$\(libdir\)).*@\1@p }'
    %configure				\
	--enable-dups			\
	--enable-cache-owner=man	\
	--with-device=utf8		\
	--with-zio			\
	--with-gnu-ld			\
	--disable-rpath			\
	--disable-automatic-create	\
	--enable-automatic-update	\
	--disable-cats			\
	--enable-threads=posix		\
	--enable-mb-groff		\
	--with-db=gdbm			\
	--enable-nls			\
	--with-config-file=%{_sysconfdir}/manpath.config \
	--without-included-gettext	\
	--with-sections="${SEC}"
    %make_build nls=all
    for man in $(find man/ -type f -a -name '*.[0-9]'); do
	pp="$(head -n 1 $man)"
	case "$pp" in
	\'\\\"*\ -\*-\ coding:\ *\ -\*-)
	    continue
	    ;;
	\'\\\"*)
	    sed -ri "1{ s/('\\\\\".*)/\\1 -\*- coding: UTF-8 -\*-/ }" $man
	    ;;
	*)
	    sed -ri "1 i\
		'\\\\\" -\*- coding: UTF-8 -\*-\
		"  $man
	esac
    done
    patch --backup --suffix=.s10 ${FUZZ+"--fuzz=$FUZZ"} -p0 < %{SOURCE10}
    gcc $CFLAGS -I gl/lib/ -I include/ --include config.h -D LOCALEDIR="\"%{_datarootdir}/locale\"" \
	-D  LIBEXECDIR="\"%{_libexecdir}\"" -o wrapper %{SOURCE5} -L gl/lib/.libs/ -lgnu

%check
if ! make check; then
	cat src/tests/test-suite.log
	exit 1
fi

%install
%if 0%{?suse_version} <= 1030
    export MKDIR_P="mkdir -p"
%endif
    rm -rf   %{buildroot}%{_localstatedir}/cache/man
    mkdir -p %{buildroot}%{_docdir}/man
    mkdir -p %{buildroot}%{_libexecdir}/man-db
    mkdir -p %{buildroot}%{_bindir}
    mkdir -p %{buildroot}%{_sysconfdir}
    mkdir -p %{buildroot}%{_mandir}
    mkdir -p %{buildroot}%{_sysconfdir}/alternatives
    make nls=all install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -delete -print
    mv	     %{buildroot}%{_datadir}/doc/man-db/man-db-manual.* \
	     %{buildroot}%{_docdir}/man/
    # wrapper which drops roots privileges if root executes man or mandb
    mv -vf   %{buildroot}%{_bindir}/man          %{buildroot}%{_libexecdir}/man-db/
    mv -vf   %{buildroot}%{_bindir}/mandb        %{buildroot}%{_libexecdir}/man-db/
    rm -vf   %{buildroot}%{_bindir}/apropos
    mv -vf   %{buildroot}%{_bindir}/whatis       %{buildroot}%{_libexecdir}/man-db/
    install wrapper %{buildroot}%{_libexecdir}/man-db/
    ln -sf   %{_libexecdir}/man-db/wrapper       %{buildroot}%{_sysconfdir}/alternatives/man
    ln -sf   %{_libexecdir}/man-db/wrapper       %{buildroot}%{_bindir}/mandb
    ln -sf   %{_libexecdir}/man-db/whatis        %{buildroot}%{_sysconfdir}/alternatives/apropos
    ln -sf   %{_libexecdir}/man-db/whatis        %{buildroot}%{_sysconfdir}/alternatives/whatis
    ln -sf   %{_sysconfdir}/alternatives/man     %{buildroot}%{_bindir}/man
    ln -sf   %{_sysconfdir}/alternatives/apropos %{buildroot}%{_bindir}/apropos
    ln -sf   %{_sysconfdir}/alternatives/whatis  %{buildroot}%{_bindir}/whatis
    pushd %{buildroot}%{_mandir}/
    rm -rf *.ascii/
    for d in *.UTF-8 ; do
	find -name '*.[1-9nlop]' | xargs gzip -9f
    done
    for d in `find -name manpath.5%{?ext_man} -printf '%%h '` ; do
	ln -sf manpath.5%{?ext_man} $d/manpath.config.5%{?ext_man}
    done

    for man in apropos man whatis
    do
	mv man1/${man}.1%{?ext_man} man1/${man}-db.1%{?ext_man}
	ln -sf %{_sysconfdir}/alternatives/${man}.1%{?ext_man} man1/${man}.1%{?ext_man}
	ln -sf %{_mandir}/man1/${man}-db.1%{?ext_man} %{buildroot}%{_sysconfdir}/alternatives/${man}.1%{?ext_man}
    done

    # remove japanese pages, as they are in man-pages-ja
    # (need to cross verify at some point that they are up to date there)
    rm -rf ja

    popd
    install -m 644 src/man_db.conf %{buildroot}%{_sysconfdir}/manpath.config
    sh ./mk_catdirs %{buildroot}
    mkdir -p %{buildroot}%{_datadir}/groff/site-tmac
    install -m 0644 groff/tmac.andb     %{buildroot}%{_datadir}/groff/site-tmac/
    install -m 0644 groff/tmac.andocdb  %{buildroot}%{_datadir}/groff/site-tmac/
    mkdir -p %{buildroot}%{_fillupdir}
    mkdir -p %{buildroot}%{_unitdir}/
%if 0%{?suse_version} < 1500
    mkdir -p %{buildroot}%{_sysconfdir}/cron.daily
%endif
    install -m 0644 %{SOURCE1} %{buildroot}%{_fillupdir}
%if 0%{?suse_version} < 1500
    install -m 0744 %{SOURCE2} %{buildroot}%{_sysconfdir}/cron.daily/suse-do_mandb
%else
    install -m 0744 %{SOURCE2} %{buildroot}/%{_libexecdir}/man-db/do_mandb
%endif
%if %{with sdtimer}
    install -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/
%if 0%{?suse_version} >= 1500
    install -m 0644 %{SOURCE8} %{buildroot}%{_unitdir}/
    install -m 0644 %{SOURCE9} %{buildroot}%{_unitdir}/
    sed -ri 's|@@LIBEXECDIR@@|%{_libexecdir}|' %{buildroot}%{_unitdir}/mandb.service
%endif
%endif

%find_lang man-db --all-name --with-man

%pre
test -d var/catman/ && rm -rf var/catman/ || true
%if %{with sdtimer}
%if 0%{?suse_version} >= 1500
%service_add_pre man-db-create.service mandb.service mandb.timer
%else
%service_add_pre man-db-create.service
%endif
%endif

%post
%{fillup_only -an cron}
/sbin/ldconfig
%if %{with sdtimer}
%service_add_post man-db-create.service
%if 0%{?suse_version} >= 1500
%service_add_post mandb.service mandb.timer
%endif
%endif
# Remark: soelim(1)     is part of package groff or mandoc and
#         makewhatis(8) is part of package makewhat or mandoc
%{_sbindir}/update-alternatives --quiet --force \
	--install %{_bindir}/man     man     %{_libexecdir}/man-db/wrapper 1010 \
	--slave   %{_bindir}/apropos apropos %{_libexecdir}/man-db/whatis \
	--slave   %{_bindir}/whatis  whatis  %{_libexecdir}/man-db/whatis \
	--slave   %{_mandir}/man1/man.1%{?ext_man}     man.1%{?ext_man}     %{_mandir}/man1/man-db.1%{?ext_man} \
	--slave   %{_mandir}/man1/apropos.1%{?ext_man} apropos.1%{?ext_man} %{_mandir}/man1/apropos-db.1%{?ext_man} \
	--slave   %{_mandir}/man1/whatis.1%{?ext_man}  whatis.1%{?ext_man}  %{_mandir}/man1/whatis-db.1%{?ext_man}

# Old man packages did not apply the proper update-alternatives calls to ensure
# alternative path move. As a result, the alternative path move induced by
# libexecdir move breaks man wrapper (boo#1175919). Hence the following migration
# code for upgrades from Leap 15.2 or Tumbleweed snapshots older than 20200826.
# To be removed when support for upgrades from Leap 15.2 is dropped (dec. 2021).
if [ %{_libexecdir} != %{_prefix}/lib ] && [ -f %{_prefix}/lib/man-db/wrapper ] ; then
   update-alternatives --quiet --remove man %{_prefix}/lib/man-db/wrapper
fi

%preun
%if %{with sdtimer}
%service_del_preun man-db-create.service
%if 0%{?suse_version} >= 1500
%service_del_preun mandb.service mandb.timer
%endif
%endif

%postun
/sbin/ldconfig
%if %{with sdtimer}
%service_del_postun man-db-create.service
%if 0%{?suse_version} >= 1500
%service_del_postun mandb.service mandb.timer
%endif
%endif
if [ ! -f %{_libexecdir}/man-db/wrapper ] ; then
   update-alternatives --quiet --remove man %{_libexecdir}/man-db/wrapper
fi

%posttrans
%{?tmpfiles_create:%tmpfiles_create %{_prefix}/lib/tmpfiles.d/man-db.conf}
if test -d %{_localstatedir}/cache/man
then
  mandb --quiet --create || :
fi

%files -f man-db.lang
%license docs/COPYING
%doc ChangeLog
%doc %{_docdir}/man/man-db-manual.*
%config %{_sysconfdir}/manpath.config
%if 0%{?suse_version} < 1500
%attr(0744,root,root) %{_sysconfdir}/cron.daily/suse-do_mandb
%endif
%ghost %{_sysconfdir}/alternatives/man
%ghost %{_sysconfdir}/alternatives/apropos
%ghost %{_sysconfdir}/alternatives/whatis
%ghost %{_sysconfdir}/alternatives/man.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/apropos.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/whatis.1%{ext_man}
%{_bindir}/man
%{_bindir}/apropos
%{_bindir}/whatis
%{_bindir}/mandb
%{_bindir}/catman
%{_bindir}/lexgrog
%{_bindir}/manpath
%dir %attr(0755,root,root) %{_libexecdir}/man-db
%attr(0755,root,root) %{_libexecdir}/man-db/man
%attr(0755,root,root) %{_libexecdir}/man-db/whatis
%attr(0755,root,root) %{_libexecdir}/man-db/mandb
%attr(0755,root,root) %{_libexecdir}/man-db/manconv
%attr(0755,root,root) %{_libexecdir}/man-db/globbing
%attr(0755,root,root) %{_libexecdir}/man-db/wrapper
%if 0%{?suse_version} >= 1500
%attr(0755,root,root) %{_libexecdir}/man-db/do_mandb
%endif
%{_sbindir}/accessdb
%{_libdir}/libman*.so
%{_libexecdir}/man-db/zsoelim
%if 0%{?_has_tmpfiled} == 0
%dir %{_prefix}/lib/tmpfiles.d
%endif
%{_prefix}/lib/tmpfiles.d/man-db.conf
%if %{with sdtimer}
%{_unitdir}/man-db-create.service
%if 0%{?suse_version} >= 1500
%{_unitdir}/mandb.service
%{_unitdir}/mandb.timer
%endif
%endif
%dir %{_datadir}/groff/site-tmac
%{_datadir}/groff/site-tmac/tmac.andb
%{_datadir}/groff/site-tmac/tmac.andocdb
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%dir %{_mandir}/id
%dir %{_mandir}/sr
%dir %{_mandir}/tr
%{_fillupdir}/sysconfig.cron-man
%defattr(-,man,man)
%ghost %{_localstatedir}/cache/man

%changelog
