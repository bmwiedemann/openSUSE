#
# spec file for package moreutils
#
# Copyright (c) 2022 SUSE LLC
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


Name:           moreutils
Version:        0.70
Release:        0
Summary:        Additional Unix Utilities
# sponge — GPL2
# isutf8 — BSD-2-Clause
# mispipe — GPL2+ or MIT
# lckdo — Public domain
# everything else — GPL2+
License:        GPL-2.0-only AND GPL-2.0-or-later AND (GPL-2.0-or-later OR MIT) AND BSD-2-Clause AND SUSE-Public-Domain
Group:          Productivity/File utilities
URL:            https://joeyh.name/code/moreutils/
Source0:         https://git.joeyh.name/index.cgi/moreutils.git/snapshot/%{name}-%{version}.tar.gz
Patch0:         makefile.patch
BuildRequires:  docbook-xsl-stylesheets

%description
This is a growing collection of the Unix tools that nobody thought to write long ago, when Unix was young.

So far, it includes the following utilities:

  - chronic: runs a command quietly unless it fails
  - combine: combine the lines in two files using boolean operations
  - errno: look up errno names and descriptions
  - ifdata: get network interface info without parsing ifconfig output
  - ifne: run a program if the standard input is not empty
  - isutf8: check if a file or standard input is utf-8
  - lckdo: execute a program with a lock held
  - mispipe: pipe two commands, returning the exit status of the first
  - parallel: run multiple jobs at once
  - pee: tee standard input to pipes
  - sponge: soak up standard input and write to a file
  - ts: timestamp standard input
  - vidir: edit a directory in your text editor
  - vipe: insert a text editor into a pipe
  - zrun: automatically uncompress arguments to command

The `moreutils` package includes errno, ifdata, ifne, isutf8, lckdo, mispipe, pee and sponge.
The remaining programs are included in the `moreutils-parallel`, `moreutils-perl`, `chronic` and `ts` packages.

%package parallel
Summary:        Run multiple jobs at once
License:        GPL-2.0-only
Conflicts:      gnu_parallel

%description parallel
parallel [options] [command]-- [argument ...]

parallel runs the specified command, passing it a single one of the specified arguments.
This is repeated for each argument. Jobs may be run in parallel. The default is to run one job per CPU.

%package perl
# Utils with only a perl-base requirment should end up here
Summary:        Additional Unix Utilities — Perl scripts
License:        GPL-2.0-or-later
Requires:       perl(File::Basename)
Requires:       perl(File::Path)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::Handle)
Requires:       perl(strict)
Requires:       perl(warnings)
Provides:       moreutils:%{_bindir}/combine
Provides:       moreutils:%{_bindir}/vidir
Provides:       moreutils:%{_bindir}/vipe
Provides:       moreutils:%{_bindir}/zrun
BuildArch:      noarch

%description perl
This is a growing collection of the Unix tools that nobody thought to write long ago, when Unix was young.

This subpackage includes the following utilities:

  - combine: combine the lines in two files using boolean operations
  - vidir: edit a directory in your text editor
  - vipe: insert a text editor into a pipe
  - zrun: automatically uncompress arguments to command

%package -n chronic
#requires perl-IPC-Run
Summary:        Runs a command quietly unless it fails
License:        GPL-2.0-or-later
Requires:       perl(Getopt::Std)
Requires:       perl(IPC::Run)
Requires:       perl(strict)
Requires:       perl(warnings)
Provides:       moreutils:%{_bindir}/chronic
BuildArch:      noarch

%description -n chronic
chronic runs a command, and arranges for its standard out and standard
error to only be displayed if the command fails (exits nonzero or crashes).
If the command succeeds, any extraneous output will be hidden.

A common use for chronic is for running a cron job. Rather than
trying to keep the command quiet, and having to deal with mails containing
accidental output when it succeeds, and not verbose enough output when it
fails, you can just run it verbosely always, and use chronic to hide
the successful output.

%package -n ts
#requires perl, perl-TimeDate and perl-Time-Duration
Summary:        Timestamp standard input
License:        GPL-2.0-or-later
Requires:       perl(Getopt::Long)
Requires:       perl(POSIX)
Requires:       perl(strict)
Requires:       perl(warnings)
Requires:       perl(Date::Parse)
Requires:       perl(Time::Duration)
Requires:       perl(Time::HiRes)
Provides:       moreutils:%{_bindir}/ts
BuildArch:      noarch

%description -n ts
ts adds a timestamp to the beginning of each line of input.

It supports custom time formats as in the strftime function. It also supports converting existing timestamps in input to relative ones.

%prep
%autosetup -p1


%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?build_ldflags}"

%if 0%{?suse_version}
export DOCBOOKXSL="%{_datadir}/xml/docbook/stylesheet/nwalsh/current"
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
export DOCBOOKXSL="%{_datadir}/sgml/docbook/xsl-stylesheets"
%endif
%make_build
echo "### before install ###"

%install
%make_install
echo "### after install ###"

%check
cd is_utf8
./test.sh

%files
%license COPYING debian/copyright
%doc README is_utf8/README.md
%{_mandir}/man1/errno.1*
%{_mandir}/man1/ifdata.1*
%{_mandir}/man1/ifne.1*
%{_mandir}/man1/isutf8.1*
%{_mandir}/man1/lckdo.1*
%{_mandir}/man1/mispipe.1*
%{_mandir}/man1/pee.1*
%{_mandir}/man1/sponge.1*
%{_bindir}/errno
%{_bindir}/ifdata
%{_bindir}/ifne
%{_bindir}/isutf8
%{_bindir}/lckdo
%{_bindir}/mispipe
%{_bindir}/pee
%{_bindir}/sponge

%files parallel
%doc README
%license COPYING debian/copyright
%{_mandir}/man1/parallel.1.gz
%{_bindir}/parallel

%files perl
%doc README
%license COPYING
%{_mandir}/man1/combine.1*
%{_mandir}/man1/vidir.1*
%{_mandir}/man1/vipe.1*
%{_mandir}/man1/zrun.1*
%{_bindir}/combine
%{_bindir}/vidir
%{_bindir}/vipe
%{_bindir}/zrun

%files -n chronic
%doc README
%license COPYING
%{_mandir}/man1/chronic.1.gz
%{_bindir}/chronic

%files -n ts
%doc README
%license COPYING
%{_mandir}/man1/ts.1.gz
%{_bindir}/ts

%changelog
