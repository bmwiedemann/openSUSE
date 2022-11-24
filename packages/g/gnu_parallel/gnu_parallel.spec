#
# spec file for package gnu_parallel
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


Name:           gnu_parallel
Version:        20221122
Release:        0
Summary:        Shell tool for executing jobs in parallel
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://www.gnu.org/software/parallel/
Source:         https://ftp.gnu.org/gnu/parallel/parallel-%version.tar.bz2
Source2:        https://ftp.gnu.org/gnu/parallel/parallel-%version.tar.bz2.sig
Source3:        %name.keyring
Source9:        %name-rpmlintrc
Patch0:         parallel-remove-nag-screen.patch
BuildArch:      noarch

%description
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers. A job can be a single command or a small script
that has to be run for each of the lines in the input. The typical
input is a list of files, a list of hosts, a list of users, a list of
URLs, or a list of tables. A job can also be a command that reads from
a pipe. GNU Parallel can then split the input and pipe it into
commands in parallel.

%package doc
Summary:        Documentation for GNU parallel
License:        CC-BY-SA-3.0 AND GFDL-1.3-only
Group:          Documentation/HTML

%description doc
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers.
This subpackage contains the documentation for Parallel.

%package bash-completion
Summary:        zsh completion for GNU parallel
Requires:       %name = %version
Supplements:    (%name and bash-completion)
BuildRequires:  bash

%description bash-completion
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers.
This subpackage contains the bash completion for Parallel.

%package zsh-completion
Summary:        zsh completion for GNU parallel
Requires:       %name = %version
Supplements:    (%name and zsh)
BuildRequires:  zsh

%description zsh-completion
GNU Parallel is a shell tool for executing jobs in parallel using one
or more computers.
This subpackage contains the zsh completion for Parallel.

%prep
%autosetup -n parallel-%version -p1

%build
%configure --docdir="%_docdir/%name"
%make_build

%install
%make_install
cp -a CITATION NEWS README "%buildroot/%_docdir/%name/"

# fix shebang to to not use env & preserve the time stamps
sed -i.orig "s:^#\!/usr/bin/env\s\+perl\s\?$:#!/usr/bin/perl:" "%buildroot/%_bindir/parallel"
touch -r "%buildroot/%_bindir/parallel.orig" "%buildroot/%_bindir/parallel"
rm "%buildroot/%_bindir/parallel.orig"

%files
%license LICENSES/GPL-3.0-or-later.txt LICENSES/CC-BY-SA-4.0.txt LICENSES/GFDL-1.3-or-later.txt
%_bindir/env_parallel*
%_bindir/niceload
%_bindir/par*
%_bindir/sem
%_bindir/sql
%_mandir/man1/*.1*
%_mandir/man7/*.7*

%files bash-completion
%_datadir/bash-completion/

%files zsh-completion
%_datadir/zsh/

%files doc
%_docdir/%name/

%changelog
