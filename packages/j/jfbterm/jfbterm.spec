#
# spec file for package jfbterm
#
# Copyright (c) 2025 SUSE LLC
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


Name:           jfbterm
Version:        0.4.7
Release:        0
Summary:        Framebuffer Terminal to Display Japanese Characters
License:        BSD-3-Clause
Group:          System/Console
# Summary(ja): Linux の framebuffer 上で漢字を表示するためのプログラムです。
URL:            http://jfbterm.sourceforge.jp/
Source0:        http://iij.dl.sourceforge.jp/jfbterm/13501/%{name}-%{version}.tar.gz
Source1:        terminfo.jfbterm
Source2:        termcap.jfbterm
Patch0:         jfbterm-0.4.7-conf.patch
Patch2:         jfbterm-0.4.7-remove-sticky.patch
Patch3:         jfbterm-0.4.7-infinite_loop.patch
Patch4:         jfbterm-0.4.7-userspace.patch
Patch5:         jfbterm-0.4.7-remove-warning.patch
Patch6:         jfbterm-0.4.7-mmap-newkernel.patch
Patch7:         jfbterm-0.4.7-hang-onexit.patch
Patch8:         jfbterm-0.4.7-pagemask_userspace.patch
# Some people see jfbterm hang or segv with invalid ut_id
# (bug 698532)
Patch9:         jfbterm-0.4.7-hang-on-utmp-refresh-with-invalid-utid.patch
# Fix encoding for AUTHORS
Patch10:        jfbterm-0.4.7-AUTHORS-encoding.patch
BuildRequires:  automake
BuildRequires:  ncurses-devel
Requires(post): %{_bindir}/grep
Requires(post): /bin/cat
Requires(post): permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
# SuSE series: j

%description
JFBTERM is a program to display Japanese Kanji characters using the
framebuffer. Similar to the well-known program kon, it uses a terminal
emulator on the console and hooks into its output. But JFBTERM does not
use VGA (like kon does). It uses the framebuffer instead.

%description -l ja
JFBTERM は Linux の framebuffer 上で漢字を表示するためのプログラムです。
KON 同様に疑似端末を使ってコンソール出力をフックしますが、VGA ではなく、
framebuffer に展開しています。

%prep
%setup -q
%patch -P 0 -p1 -b .conf
%patch -P 2 -p1 -b .remove_sticky
%patch -P 3 -p1 -b .userspace
%patch -P 4 -p1 -b .infinite_loop
%patch -P 5 -p1 -b .remove_warn
%patch -P 6 -p1 -b .nmap_newkernel
%patch -P 7 -p1 -b .hang_onexit
%patch -P 8 -p1 -b .pagemask
%patch -P 9 -p1 -b .utid_with_refresh
%patch -P 10 -p1
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
autoreconf -fi
#aclocal
#automake -a --gnu --include-deps
#autoconf
#touch Makefile.in aclocal.m4 config.h.in configure stamp-h.in
# fix non-position-independent-executable error
export LDFLAGS="-pie"
export CFLAGS="%{optflags} -fPIE -fomit-frame-pointer -fgnu89-inline"
# ----------------------------------
%configure
make %{?_smp_mflags}

%install
# "make install" doesn't work well here, therefore I do it manually
# there are only two files anyway.
# make prefix=$RPM_BUILD_ROOT/ install
# mv $RPM_BUILD_ROOT/etc/jfbterm.conf.sample $RPM_BUILD_ROOT/etc/jfbterm.conf
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_bindir}
install -m 4755 jfbterm %{buildroot}%{_bindir}/jfbterm
install -m 644 jfbterm.conf.sample %{buildroot}%{_sysconfdir}/jfbterm.conf
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
install -m 644 jfbterm.1 %{buildroot}%{_mandir}/man1
install -m 644 jfbterm.conf.5 %{buildroot}%{_mandir}/man5
# install terminfo entry-description
# mkdir -p $RPM_BUILD_ROOT/usr/share/terminfo/j
# TERMINFO=$RPM_BUILD_ROOT/usr/share/terminfo tic terminfo.jfbterm

%post
%if 0%{?sles_version}
%run_permissions
%else
%set_permissions %{_bindir}/jfbterm
%endif
# canuum needs a termcap entry, without it canuum won't run under jfbterm:
if [ -f etc/termcap ]; then
    if [ `grep -c '^jfbterm|japanese framebuffer terminal' etc/termcap` -eq 0 ]; then
	cat %{_defaultdocdir}/jfbterm/termcap.jfbterm >> etc/termcap
    fi
fi

%verifyscript
%verify_permissions -e %{_bindir}/jfbterm

%files
%defattr(-, root, root)
%doc NEWS AUTHORS README ChangeLog
%doc terminfo.jfbterm termcap.jfbterm
%license COPYING
%config %{_sysconfdir}/jfbterm.conf
%{_mandir}/man1/jfbterm.1*
%{_mandir}/man5/jfbterm.conf.5*
%verify(not mode) %attr(0755,root,tty) %{_bindir}/jfbterm

%changelog
