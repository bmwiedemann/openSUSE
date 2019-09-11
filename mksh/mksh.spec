#
# spec file for package mksh
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Guido Berhoerster.
# Copyright (c) 2013, 2014, 2019 Thorsten Glaser.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# Please see OBS home:mirabile/mksh for a package for other distributions.

Name:           mksh
Version:        57
Release:        0
Summary:        MirBSD Korn Shell
License:        MirOS AND ISC
Group:          System/Shells
Url:            http://www.mirbsd.org/mksh.htm
Source:         https://www.mirbsd.org/MirOS/dist/mir/mksh/%{name}-R%{version}.tgz
# PATCH-FEATURE-OPENSUSE mksh-vendor-mkshrc.patch gber@opensuse.org -- Add support for a vendor-supplied kshrc which is read by interactive shells before $ENV or $HOME/.mkshrc are processed
Patch0:         mksh-vendor-mkshrc.patch
BuildRequires:  ed
# for %%check
BuildRequires:  perl
BuildRequires:  screen
BuildRequires:  sed
BuildRequires:  update-alternatives
%if 0%{?suse_version} >= 1315
# replaces pdksh in openSUSE >= 13.2 and SLES >= 12
Provides:       pdksh = %{version}
Obsoletes:      pdksh < %{version}
%if !0%{?is_opensuse}
Provides:       ksh = %{version}
Obsoletes:      ksh < %{version}
%endif
Provides:       /bin/ksh
Requires(post): update-alternatives
Requires(preun): update-alternatives
%else
# for SLES or openSUSE < 13.2 which do not mksh
Requires(post): grep
Requires(postun): awk
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The MirBSD Korn Shell is an actively developed free implementation of the Korn
Shell programming language and a successor to the Public Domain Korn Shell
(pdksh).

%prep
%setup -q -n %{name}
%patch0 -p1 -b .p0

ed -s mksh.1 <<-'EOF'
	/insert-your-name-here/s/^\.\\" //
	s/insert-your-name-here/SUSE/
	w
	EOF
# " Stupid double quote for vi

ln -s . examples

%build
#
# sys_errlist and sys_siglist *are* deprecated
# Be aware of the _SYS_SIGLIST and _SYS_ERRLIST macros as well
#
HAVE_SYS_SIGLIST=0
HAVE_SYS_ERRLIST=0
HAVE__SYS_SIGLIST=0
HAVE__SYS_ERRLIST=0
export HAVE_SYS_SIGLIST HAVE_SYS_ERRLIST HAVE__SYS_SIGLIST HAVE__SYS_ERRLIST

#
# -ftree-loop-linear
#    Perform loop nest optimizations.  Same as -floop-nest-optimize.
#    To use this code transformation, GCC has to be configured with
#    --with-isl to enable the Graphite loop transformation infrastructure.
#
export CC=gcc
if $CC -Werror -ftree-loop-linear -S -o /dev/null -xc /dev/null > /dev/null 2>&1
then
    export CFLAGS='%{optflags} -Wuninitialized -Wall -Wextra -ftree-loop-linear -pipe'
else
    export CFLAGS='%{optflags} -Wuninitialized -Wall -Wextra -pipe'
fi
case "$(uname -m)" in
ppc64)   CFLAGS="$CFLAGS -mbig-endian -mcpu=power4"  ;;
ppc64le) CFLAGS="$CFLAGS -mtune=power8 -mcpu=power8" ;;
esac
export CPPFLAGS='-DMKSH_VENDOR_MKSHRC_PATH=\"/etc/mkshrc\" -DMKSH_EARLY_LOCALE_TRACKING -DMKSH_ASSUME_UTF8'
export LDFLAGS='-Wl,--as-needed -Wl,-O2'
vendor=OpenBuildService
%if 0%{?suse_version} > 0
%if !0%{?is_opensuse}
vendor=SLES
%else
vendor=openSUSE
%endif
%endif
CPPFLAGS="$CPPFLAGS -DKSH_VERSIONNAME_VENDOR_EXT=\\\"\ +$vendor\\\""
if grep -q _DEFAULT_SOURCE /usr/include/features.h; then
	CPPFLAGS="$CPPFLAGS -D_DEFAULT_SOURCE"
fi
# filter compiler warnings and errors from configuration tests
{
    sh Build.sh -r || touch build.failed
    mv test.sh test-mksh.sh
    # build lksh to automatically enable -o posix if called as sh
    CPPFLAGS="$CPPFLAGS -DMKSH_BINSHPOSIX"
    sh Build.sh -L -r || touch build.failed
    mv test.sh test-lksh.sh
} 2>&1 | sed -r \
  -e 's!conftest.c:([0-9]*(:[0-9]*)*): error:!cE(\1) -!g' \
  -e 's!conftest.c:([0-9]*(:[0-9]*)*): warning:!cW(\1) -!g' \
  -e 's!conftest.c:([0-9]*(:[0-9]*)*): note:!cN(\1) -!g'
test ! -e build.failed

%install
install -d %{buildroot}/bin
for shell in mksh lksh; do
    install -D -p -m 755 ${shell} %{buildroot}%{_bindir}/${shell}
    install -D -p -m 644 ${shell}.1 %{buildroot}%{_mandir}/man1/${shell}.1
    ln -s %{_bindir}/${shell} %{buildroot}/bin/${shell}
done
install -d -m 755 %{buildroot}%{_sysconfdir}/alternatives
ln -s %{_sysconfdir}/bash.bashrc %{buildroot}%{_sysconfdir}/mkshrc
%if 0%{?suse_version} >= 1315
# compatibility symlinks for pdksh, lksh replaces pdksh in openSUSE >= 13.2
ln -s /bin/lksh %{buildroot}/bin/pdksh
ln -s %{_bindir}/lksh %{buildroot}%{_bindir}/pdksh
ln -s %{_mandir}/man1/lksh.1%{ext_man} \
    %{buildroot}%{_mandir}/man1/pdksh.1%{ext_man}
# symlinks for update-alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/ksh \
    %{buildroot}%{_sysconfdir}/alternatives/usr-bin-ksh \
    %{buildroot}%{_sysconfdir}/alternatives/ksh.1%{ext_man}
ln -sf %{_sysconfdir}/alternatives/ksh %{buildroot}/bin/ksh
ln -sf %{_sysconfdir}/alternatives/usr-bin-ksh %{buildroot}/%{_bindir}/ksh
ln -sf %{_sysconfdir}/alternatives/ksh.1%{ext_man} \
    %{buildroot}/%{_mandir}/man1/ksh.1%{ext_man}
%endif

%check
# should always run in a clean environment as otherwise
# tests might fail due wrong line numbering
SCREENDIR=$(mktemp -d ${PWD}/screen.XXXXXX) || exit 1
trap 'rm -rf $SCREENDIR' EXIT
SCREENRC=${SCREENDIR}/mksh
export SCREENRC SCREENDIR
export HOME=${SCREENDIR}
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
for shell in mksh lksh; do
    screen -D -m sh -c "./test-${shell}.sh -v -f || > failed"
done
kill -TERM $pid
if test -e failed
then
    sed -rn '/FAIL /,/^pass /p' $SCREENLOG
    exit 1
fi

%clean
rm -Rf %{buildroot}

%if 0%{?suse_version} >= 1315
%post
%{_sbindir}/update-alternatives \
  --install /bin/ksh ksh %{_bindir}/lksh 15 \
  --slave %{_bindir}/ksh usr-bin-ksh %{_bindir}/lksh \
  --slave %{_mandir}/man1/ksh.1%{?ext_man} ksh.1%{?ext_man} %{_mandir}/man1/lksh.1%{?ext_man}

%preun
if test $1 -eq 0 ; then
    %{_sbindir}/update-alternatives --remove ksh /bin/lksh
fi
%else
# for SLE or openSUSE < 13.2 which do not support mksh
%post
for entry in /bin/mksh %{_bindir}/mksh; do
    grep -q ${entry} %{_sysconfdir}/shells ||\
        printf '%%s\n' ${entry} >>%{_sysconfdir}/shells
done

%postun
test -x %{_bindir}/mksh && awk '
($1 != "/bin/mksh") && ($1 != "%{_bindir}/mksh") {
    line[n++] = $0
}
END {
    for (i = 0; i < n; i++) {
        print line[i] >"%{_sysconfdir}/shells"
    }
}' '%{_sysconfdir}/shells' || true
%endif

%files
%defattr(-,root,root)
%doc examples/dot.mkshrc
%{_sysconfdir}/mkshrc
/bin/mksh
/bin/lksh
%{_bindir}/mksh
%{_bindir}/lksh
%{_mandir}/man1/mksh.1%{?ext_man}
%{_mandir}/man1/lksh.1%{?ext_man}
%if 0%{?suse_version} >= 1315
/bin/pdksh
%{_bindir}/pdksh
%{_mandir}/man1/pdksh.1%{?ext_man}
/bin/ksh
%{_bindir}/ksh
%{_mandir}/man1/ksh.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/ksh
%ghost %{_sysconfdir}/alternatives/usr-bin-ksh
%ghost %{_sysconfdir}/alternatives/ksh.1%{?ext_man}
%endif

%changelog
