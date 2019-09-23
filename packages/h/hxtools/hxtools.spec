#
# spec file for package hxtools
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           hxtools
Version:        20190428
Release:        0
Summary:        Collection of day-to-day tools (binaries)
License:        GPL-2.0+ and WTFPL
Group:          Productivity/Other
Url:            http://inai.de/projects/hxtools/

Source:         http://jftp.inai.de/hxtools/%name-%version.tar.xz
Source2:        http://jftp.inai.de/hxtools/%name-%version.tar.asc
Source3:        %name.keyring
BuildRequires:  bdftopcf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel >= 2
BuildRequires:  xz
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  pkgconfig(libHX) >= 3.17
BuildRequires:  pkgconfig(libpci) >= 3
BuildRequires:  pkgconfig(mount) >= 2.20
BuildRequires:  pkgconfig(xcb) >= 1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %name-scripts = %version
Recommends:     %name-man = %version
Recommends:     hardlink
Requires:       fd0ssh
Requires:       ofl
Requires:       sysinfo = %version

%define build_profile 1
%define hldir %_libexecdir/%name

%description
A collection of various tools. Some of the important ones:

* declone(1) — break hardlinks
* fd0ssh(1) — pipe for password-over-stdin support to ssh
* ofl(1) — open file lister (replaces fuser and lsof -m)
* tailhex(1) — hex dumper with tail-following support
* utmp_register(1) — make entries in the utmp/wtmp database
* vfontas(1) — VGA font file assembler

%package scripts
Summary:        Collection of day-to-day tools (scripts)
Group:          Productivity/Other
BuildArch:      noarch
Requires:       %name
Recommends:     %name-man
Requires:       perl(Data::Dumper)
Requires:       perl(File::Find)
Requires:       perl(File::Find::Rule)
Requires:       perl(Getopt::Long)
Requires:       perl(IPC::Open2)
Requires:       perl(Text::CSV_XS)

%description scripts
Architecture-independent programs from hxtools.

* checkbrack(1) — check parenthesis and bracket count
* cwdiff(1) — run wdiff with color
* diff2php(1) — transform patch to self-serving PHP file
* doxygen-kerneldoc-filter(1) — filter for Doxygen to support kerneldoc
* filenameconv(1) — convert file name encoding
* git-author-stat(1) — show commit author statistics of a git repository
* git-export-patch(1) — produce perfect patch from git comits for mail submission
* git-forest(1) — display the commit history forest
* git-revert-stats(1) — show reverting statistics of a git repository
* git-track(1) — set up branch for tracking a remote
* man2html(1) — convert nroff manpages to HTML
* pegrep(1) — perl-regexp-based multi-line grep
* pesubst(1) — perl-regexp-based stream substitution (replaces sed for substitutions)
* recursive_lower(1) — recursively lowercase all filenames
* spec-beautifier(1) — program to clean up RPM .spec files
* vcsaview(8) — display a screen dump in VCSA format
* wktimer(1) — work timer

%package man
Summary:        Manual pages for the hxtools suite
Group:          Documentation/Man
BuildArch:      noarch

%description man
This package contains the manual pages for the binaries and scripts
from hxtools.

%package data
Summary:        Collection of day-to-day tools (data)
Group:          Productivity/Other
BuildArch:      noarch

%description data
Architecture-independent data from hxtools.

* VAIO U3 keymap
* additional fonts for console and xterm
* additional syntax highlighting definitions for mcedit

%package profile
Summary:        The hxtools shell environment
Group:          Productivity/Other
Requires:       %name = %version
Requires:       %name-data = %version
Requires:       %name-scripts = %version
BuildArch:      noarch

%description profile
Bash environment settings from hxtools. Particularly, this provides
the SUSE 6.x ls color scheme, and a reduced PS1 that shows only the
rightmost parts of a path.

%package -n sysinfo
Summary:        System diagnosis tools from hxtools
Group:          System/Base

%description -n sysinfo
This subpackage contains programs from the hxtools suite that
give info about available system components.

* clock_info(1) – show available system clocks for clock_gettime(2)
* pmap_dirty(1) — display amount of RAM a process uses hard
* sysinfo(1) — print IRC-style system information banner

%package -n fd0ssh
Summary:        Helper program for using a pipe for SSH authentication
Group:          System/Base

%description -n fd0ssh
fd0ssh a helper program used by non-interactive programs, for example
pam_mount, that want to pipe a password to ssh.

%package -n ofl
Summary:        Open File Lister from hxtools
Group:          System/Base

%description -n ofl
ofl lists processes (and can send signals to them) that have
directories or files in specific locations in use. It differs from
lsof/fuser in that it can scan recursively and won't bluntly look at
an entire mount.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
b="%buildroot"
mv "$b/%_bindir/rot13" "$b/%_libexecdir/%name/"
install -dm0755 "$b/%_datadir/mc/syntax"
install -pm0644 cooledit/*.syntax "$b/%_datadir/mc/syntax/"
install -dm0755 "$b/%_sysconfdir/openldap/schema"
ln -s "%_datadir/hxtools/rfc2307bis-utf8.schema" \
	"$b/%_sysconfdir/openldap/schema/"

%if 0%{?build_profile}
mkdir -p "$b/%_sysconfdir/bashrc.d"
ln -s "%_datadir/%name/hxtools_bashrc.bash" "$b/%_sysconfdir/bashrc.d/"
mkdir -p "$b/%_sysconfdir/profile.d"
ln -s "%_datadir/%name/hxtools_profile.bash" "$b/%_sysconfdir/profile.d/z_hxtools_profile.sh"
%else
rm -Rf "$b/%_sysconfdir/profile.d" "$b/%_sysconfdir"/hx*
%endif

%fdupes %buildroot/%_prefix

%files
%defattr(-,root,root)
%doc LICENSE*
%_bindir/bin2c
%_bindir/declone
%_bindir/gxxdm
%_bindir/hcdplay
%_bindir/tailhex
%_bindir/xcp
%dir %hldir
%hldir/bsvplay
%hldir/cctypeinfo
%hldir/pcmdiff
%hldir/peicon
%hldir/proc_iomem_count
%hldir/proc_stat_parse
%hldir/psthreads
%hldir/qplay
%hldir/rot13
%hldir/utmp_register
%hldir/vfontas

%files scripts
%defattr(-,root,root)
%_bindir/aumeta
%_bindir/checkbrack
%_bindir/cwdiff
%_bindir/fxterm
%_bindir/git-*
%_bindir/gpsh
%_bindir/man2html
%_bindir/mkvappend
%_bindir/pegrep
%_bindir/pesubst
%_bindir/qpdecode
%_bindir/qtar
%_bindir/spec-beautifier
%_bindir/ssa2srt
%_bindir/su1
%_bindir/wktimer
%dir %hldir
%hldir/diff2php
%hldir/doxygen-kerneldoc-filter
%hldir/extract_*
%hldir/git-*
%hldir/ldif-duplicate-attrs
%hldir/ldif-leading-spaces
%hldir/logontime
%hldir/mailsplit
%hldir/mod2opus
%hldir/recursive_lower
%hldir/rezip
%hldir/shared.pm
%hldir/sourcefuncsize
%hldir/stxdb
%hldir/vcsaview

%files man
%defattr(-,root,root)
%doc %_mandir/man*/*
%exclude %_mandir/man*/fd0ssh.1*
%exclude %_mandir/man*/ofl.1*

%files data
%defattr(-,root,root)
%dir %_sysconfdir/openldap
%dir %_sysconfdir/openldap/schema
%config %_sysconfdir/openldap/schema/*
%_datadir/%name
%_datadir/kbd
%_datadir/fonts/misc
%_datadir/mc

%if 0%{?build_profile}

%files profile
%defattr(-,root,root)
%config %_sysconfdir/hxloginpref.conf
%dir %_sysconfdir/bashrc.d
%config %_sysconfdir/bashrc.d/*
%config %_sysconfdir/profile.d/*
%endif

%files -n fd0ssh
%defattr(-,root,root)
%dir %hldir
%hldir/fd0ssh
%_mandir/man1/fd0ssh.1*

%files -n ofl
%defattr(-,root,root)
%_bindir/ofl
%_mandir/man1/ofl.1*

%files -n sysinfo
%defattr(-,root,root)
%_bindir/clock_info
%_bindir/pmap_dirty
%_bindir/sysinfo
%dir %hldir
%hldir/hxnetload
%hldir/paddrspacesize
%hldir/proc_stat_signal_decode

%changelog
