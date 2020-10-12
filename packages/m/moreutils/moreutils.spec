#
# spec file for package moreutils
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


Name:           moreutils
Version:        0.64
Release:        0
Summary:        Additional Unix Utilities
License:        GPL-2.0-or-later AND GPL-2.0-only AND MIT
Group:          Productivity/File utilities
URL:            https://joeyh.name/code/moreutils/
Source:         https://git.joeyh.name/index.cgi/moreutils.git/snapshot/%{name}-%{version}.tar.gz
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
Requires:       perl
Requires:       perl-IPC-Run
Requires:       perl-Time-Duration
Requires:       perl-TimeDate
# These perl modules add functionality to the ts command, as they are added in eval'd code they are not
# picked up automatically by rpm.
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%package parallel
Summary:        Additional unix utility - parallel command
Group:          Productivity/File utilities
Requires:       %{name} = %{version}-%{release}
Conflicts:      gnu_parallel

%description parallel
 This is a growing collection of the Unix tools that nobody thought to write long ago, when Unix was young.

 This is a sub package containing the parallel command only

  - parallel: run multiple jobs at once


%prep
%setup -q
sed -e 's/^CFLAGS =/CFLAGS ?=/' -i is_utf8/Makefile

%build
export CFLAGS="%{optflags}"
%if 0%{?suse_version}
export DOCBOOKXSL="/usr/share/xml/docbook/stylesheet/nwalsh/current"
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
export DOCBOOKXSL="/usr/share/sgml/docbook/xsl-stylesheets"
%endif
make %{?_smp_mflags}
echo "### before install ###"

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
echo "### after install ###"

%files
%defattr(-, root, root)
%doc COPYING README
%attr(644, root, root) %{_mandir}/man1/chronic.1*
%attr(644, root, root) %{_mandir}/man1/combine.1*
%attr(644, root, root) %{_mandir}/man1/errno.1*
%attr(644, root, root) %{_mandir}/man1/ifdata.1*
%attr(644, root, root) %{_mandir}/man1/ifne.1*
%attr(644, root, root) %{_mandir}/man1/isutf8.1*
%attr(644, root, root) %{_mandir}/man1/lckdo.1*
%attr(644, root, root) %{_mandir}/man1/mispipe.1*
%attr(644, root, root) %{_mandir}/man1/pee.1*
%attr(644, root, root) %{_mandir}/man1/sponge.1*
%attr(644, root, root) %{_mandir}/man1/ts.1*
%attr(644, root, root) %{_mandir}/man1/vidir.1*
%attr(644, root, root) %{_mandir}/man1/vipe.1*
%attr(644, root, root) %{_mandir}/man1/zrun.1*
%{_bindir}/chronic
%{_bindir}/combine
%{_bindir}/errno
%{_bindir}/ifdata
%{_bindir}/ifne
%{_bindir}/isutf8
%{_bindir}/lckdo
%{_bindir}/mispipe
%{_bindir}/pee
%{_bindir}/sponge
%{_bindir}/ts
%{_bindir}/vidir
%{_bindir}/vipe
%{_bindir}/zrun

%files parallel
%defattr(-,root,root)
%doc README COPYING
%attr(644, root, root) %{_mandir}/man1/parallel.1.gz
%{_bindir}/parallel

%changelog
