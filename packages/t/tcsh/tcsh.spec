#
# spec file for package tcsh
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


Name:           tcsh
Version:        6.24.13
Release:        0
Summary:        The C SHell
License:        BSD-3-Clause
Group:          System/Shells
URL:            https://www.tcsh.org/
Source0:        https://astron.com/pub/%{name}/%{name}-%{version}.tar.gz
Source1:        https://astron.com/pub/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        bindkey.tcsh
Source3:        complete.tcsh
Source4:        tcsh.keyring
Patch0:         tcsh-6.21.00.dif
Patch1:         tcsh-6.15.00-pipe.dif
Patch2:         tcsh-6.16.00-norm-cmd.dif
Patch4:         tcsh-6.18.03-colorls.dif
Patch5:         tcsh-6.17.06-dspmbyte.dif
Patch6:         tcsh-6.18.03-catalogs.dif
Patch7:         tcsh-skip-utmp-service.dif
Patch8:         tcsh-6.22.02-local-dotlock.dif
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  screen
Requires:       gawk
Requires:       textutils
Recommends:     tcsh-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tcsh is an enhanced, but completely compatible, version of the Berkeley
UNIX C shell, csh(1). It is a command language interpreter usable as an
interactive login shell and a shell script command processor. It
includes a command-line editor, programmable word completion, spelling
correction, a history mechanism, job control, and a C-like syntax.

%lang_package

%prep
%setup -q
%patch -P1      -b .pipe
%patch -P2      -b .normcmd
%patch -P4      -b .colorls
%patch -P5      -b .dspmbyte
%patch -P6      -b .catalogs
%if 0%{?suse_version} >= 1699
%patch -P7      -b .noutmp
%endif
%patch -P8 -p 0 -b .dotlock
%patch -P0      -b .0

%build

    cflags ()
    {
	local flag=$1; shift
	local var=$1; shift
	test -n "${flag}" -a -n "${var}" || return
	case "${!var}" in
	*${flag}*) return
	esac
	set -o noclobber
	case "$flag" in
	-Wl,*)
	    if echo 'int main () { return 0; }' | \
	       ${CC:-gcc} -Werror $flag -o /dev/null -xc - > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	    ;;
	*)
	    if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	    if ${CXX:-g++} -Werror $flag -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	esac
	set +o noclobber
    }
    CC=gcc
    CFLAGS="%{optflags} -D_GNU_SOURCE -DBUFSIZE=8192 -pipe"
%if 0%{?suse_version} >= 1699
    #
    # There is currently no API for using systemd logind
    # for watch and who tcsh builtin.
    #
    CFLAGS="${CFLAGS} -DHAVENOUTMP"
%endif
    cflags -ftree-loop-linear      CFLAGS
    cflags -Wl,-O2                 LDFLAGS
    cflags -Wl,--as-needed         LDFLAGS
    export CC CFLAGS LDFLAGS

%ifarch %ix86
    CPU=i586
%else
    CPU=${RPM_ARCH}
%endif
    ./configure --build=${CPU}-suse-linux \
	--prefix=/usr			\
	--sysconfdir=/etc		\
	--localstatedir=/var		\
	--sharedstatedir=%{_datadir}	\
	--infodir=%{_infodir}		\
	--mandir=%{_mandir}		\
	--libexecdir=%{_libdir}/tcsh	\
	--disable-rpath			\
	--with-gnu-ld
    make %{?_smp_mflags} CC_FOR_GETHOST="$CC $CFLAGS"

%check
    SCREENDIR=$(mktemp -d ${PWD}/screen.XXXXXXXXXX) || exit 1
    SCREENRC=${SCREENDIR}/tcsh
    TMPDIR=$(mktemp -d /tmp/tcsh.XXXXXXXXXX) || exit 1
    export SCREENRC SCREENDIR TMPDIR
    exec 0< /dev/null
    SCREENLOG=${SCREENDIR}/log
    cat > $SCREENRC<<-EOF
	deflogin off
	deflog on
	logfile $SCREENLOG
	logfile flush 1
	logtstamp off
	log on
	setsid on
	scrollback 0
	silence on
	utf8 on
	EOF
    > $SCREENLOG
    tail -q -s 0.5 -f $SCREENLOG & pid=$!
    env -i HOME=$HOME TERM=$TERM TMPDIR=$TMPDIR PATH=$PATH \
	SCREENRC=$SCREENRC SCREENDIR=$SCREENDIR \
	screen -D -m make check
    sleep 1
    kill -TERM $pid
    rm -rf $SCREENDIR $TMPDIR
    if grep -iq failed testsuite.log
    then
	echo FAILED
	exit 127
    fi

%install
    for nls in nls/*.cat ; do
	msg=$nls
	nls=${nls##*/}
	nls=${nls%%.*}
	case "${nls}" in
	fi*)	nls=fi		;;
	fr*)	nls=fr		;;
	ge*)	nls=de		;;
	gr*)	nls=el		;;
	it*)	nls=it		;;
	ru*)	nls=ru_RU	;;
	sp*)	nls=es		;;
	uk*)	nls=uk_UA	;;
	C)	continue	;;
	esac
	dir=%{buildroot}%{_datadir}/locale/${nls}/LC_MESSAGES
	test ! -e ${dir}/tcsh || continue
	mkdir -p -m 0755 $dir
	install -m 0644 ${msg} ${dir}/tcsh
    done
    make DESTDIR=%{buildroot} GENCAT='%{_bindir}/gencat --new' install
    make DESTDIR=%{buildroot} GENCAT='%{_bindir}/gencat --new' install.man
    find %{buildroot}%{_datadir}/locale -name tcsh | xargs chmod 0644
    %fdupes -s %{buildroot}%{_datadir}/locale
    mkdir -p %{buildroot}%{_docdir}/tcsh
    install -m 0644 FAQ       %{buildroot}%{_docdir}/tcsh/FAQ.tcsh
    install -m 0644 Copyright %{buildroot}%{_docdir}/tcsh/Copyright
    mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
    mkdir -p %{buildroot}%{_prefix}/bin
    install -m 644 $RPM_SOURCE_DIR/bindkey.tcsh  %{buildroot}%{_sysconfdir}/profile.d/
    install -m 644 $RPM_SOURCE_DIR/complete.tcsh %{buildroot}%{_sysconfdir}/profile.d/
    rm -f  %{buildroot}%{_mandir}/man1/csh.*
    rm -rf %{buildroot}%{_datadir}/locale/C
    ln -sf tcsh           %{buildroot}/%{_bindir}/csh
    ln -sf tcsh.1.gz      %{buildroot}%{_mandir}/man1/csh.1.gz
%if 0%{?suse_version} < 1550
    mkdir -p %{buildroot}/bin
    ln -s %{_bindir}/tcsh %{buildroot}/bin/tcsh
    ln -s %{_bindir}/tcsh %{buildroot}/bin/csh
%endif

%files
%defattr(-,root,root)
%dir %{_docdir}/tcsh
%if 0%{?suse_version} < 1550
/bin/csh
/bin/tcsh
%endif
%config %{_sysconfdir}/profile.d/bindkey.tcsh
%config %{_sysconfdir}/profile.d/complete.tcsh
%{_bindir}/csh
%{_bindir}/tcsh
%doc %{_docdir}/tcsh/Copyright
%doc %{_docdir}/tcsh/FAQ.tcsh
%doc %{_mandir}/man1/csh.1.gz
%doc %{_mandir}/man1/tcsh.1.gz

%files lang
%defattr(0644,root,root)
%{_datadir}/locale/*/LC_MESSAGES/tcsh*

%changelog
