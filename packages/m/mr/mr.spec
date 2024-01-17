#
# spec file for package mr
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


Name:           mr
Version:        1.20180726
Release:        0
Summary:        Version control repository manager
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            https://myrepos.branchable.com
Source0:        mr-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  make
Requires:       perl
BuildArch:      noarch

%description
The mr(1) command can checkout, update, or perform other actions on a
set of repositories as if they were one combined respository. It
supports any combination of git, svn, mercurial, bzr, darcs, cvs,
vcsh, fossil, and veracity repositories. It supports extensions which
in turn can use more version control systems.

It is configurable via shell scripting. Some examples of things it can do include:

 * Update a repository no more frequently than once every twelve hours.
 * Run an arbitrary command before committing to a repository.
 * When updating a git repository, pull from two different upstreams
   and merge the two together.
 * Run several repository updates in parallel, greatly speeding up
   the update process.
 * Remember actions that failed due to a laptop being offline, so they can be retried when it comes back online.

This package also includes the webcheckout(1) command.

%prep
%setup -q

%build
%make_build build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc
%fdupes -s %{buildroot}/%{_prefix}

%check
%make_build test

%files
%license GPL
%doc README
%{_bindir}/mr
%{_bindir}/webcheckout
%{_mandir}/man1/mr.1%{?ext_man}
%{_mandir}/man1/webcheckout.1%{?ext_man}
%dir %{_datadir}/mr
%{_datadir}/mr/dgit
%{_datadir}/mr/git-annex
%{_datadir}/mr/git-fake-bare
%{_datadir}/mr/git-subtree
%{_datadir}/mr/git-svn
%{_datadir}/mr/repo
%{_datadir}/mr/stow
%{_datadir}/mr/unison
%{_datadir}/mr/vcsh
%{_datadir}/mr/vis
%{_datadir}/mr.sh
%{_datadir}/mr/git-cvs
%{_datadir}/mr/graph
%{_datadir}/mr/remote
%{_datadir}/mr/upgrade

%changelog
