#
# spec file for package taskwarrior
#
# Copyright (c) 2021 SUSE LLC
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


Name:           taskwarrior
Version:        2.5.3
Release:        0
Summary:        Command-line todo list manager
License:        MIT
Group:          Productivity/Office/Organizers
URL:            http://taskwarrior.org
#Source0:        http://www.taskwarrior.org/download/task-#{version}.tar.gz
Source0:        https://github.com/GothenburgBitFactory/taskwarrior/releases/download/v%{version}/task-%{version}.tar.gz
#PATCH-FIX-OPENSUSE: skip the INSTALL and LICENSE from files intended for the installation
Patch0:         task-skip-INSTALL.patch
BuildRequires:  awk
BuildRequires:  cmake >= 2.8
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  libuuid-devel
# for completion
BuildRequires:  bash
BuildRequires:  vim-base
BuildRequires:  zsh
# for sync
BuildRequires:  libgnutls-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# use the name as other distributions, so
# zypper in task will work as well
Provides:       task = %{version}-%{release}

%description
It maintains a list of tasks that you want to do, allowing you to add/remove,
and otherwise manipulate them. Task has a rich list of subcommands that allow
you to do sophisticated things with it. You'll find it has customizable
reports, charts, GTD features, Lua extensions, device synching and more.

Taskwarrior is a very active project involving people around the globe - check
often for updates.

%prep
%setup -q -n task-%{version}
%patch0 -p1

# replace __TIME__/__DATE__ with values from source code tarball
DATE=$(/bin/date -r "%{SOURCE0}" | awk '{print $2" "$3" "$6}')
TIME=$(/bin/date -r "%{SOURCE0}" | awk '{print $4}')
sed -i src/commands/CmdDiagnostics.cpp \
 -e "s/__TIME__/\"${TIME}\"/" \
 -e "s/__DATE__/\"${DATE}\"/"

%build
%cmake -DENABLE_SYNC:BOOL=ON \
    -DTASK_DOCDIR:PATH=%{_docdir}/task \
    -DTASK_MAN1DIR:PATH=%{_datadir}/man/man1/ \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_STATIC_LIBS:BOOL=OFF \
    -DTASK_MAN5DIR:PATH=%{_datadir}/man/man5/
%cmake_build

%install
%cmake_install

# this integration stuff might be in CMakeList.txt, but ...
%define scriptsdir %{buildroot}%{_docdir}/task/scripts/

install -m 0755 -d %{buildroot}%{_datadir}/bash_completion.d/
mv %{scriptsdir}bash/task.sh %{buildroot}%{_datadir}/bash_completion.d/

install -m 0755 -d %{buildroot}%{_datadir}/zsh/site-functions/
mv %{scriptsdir}zsh/_task %{buildroot}%{_datadir}/zsh/site-functions/
rmdir %{scriptsdir}zsh

install -m 0755 -d %{buildroot}%{_datadir}/fish/completions/
mv %{scriptsdir}fish/task.fish %{buildroot}%{_datadir}/fish/completions/
rmdir %{scriptsdir}fish

install -m 0755 -d %{buildroot}%{_datadir}/vim/site/ftdetect/
install -m 0755 -d %{buildroot}%{_datadir}/vim/site/syntax/
mv %{scriptsdir}vim/ftdetect/*vim %{buildroot}%{_datadir}/vim/site/ftdetect
mv %{scriptsdir}vim/syntax/*vim %{buildroot}%{_datadir}/vim/site/syntax
rm -rf %{scriptsdir}vim

# don't requre python/perl/ruby by default, so remove executable bit
find %{buildroot}/%{_docdir}/task -type f -exec chmod a-x {} +

%files
%defattr(-,root,root)
%doc %{_docdir}/task
%{_bindir}/task*
%{_datadir}/man/man1/task*
%{_datadir}/man/man5/task*
%{_datadir}/bash_completion.d/
%{_datadir}/zsh/site-functions/
%dir %{_datadir}/fish/
%{_datadir}/fish/completions/
%{_datadir}/vim/site/ftdetect/task.vim
%{_datadir}/vim/site/syntax/task*.vim

%changelog
