#
# spec file for package taskwarrior
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


Name:           taskwarrior
Version:        3.1.0
Release:        0
Summary:        Command-line todo list manager
License:        MIT
Group:          Productivity/Office/Organizers
URL:            https://taskwarrior.org/
Source0:        https://github.com/GothenburgBitFactory/%{name}/releases/download/v%{version}/task-%{version}.tar.gz
Source1:        vendor.tar.zst
#PATCH-FIX-OPENSUSE: skip the INSTALL and LICENSE from files intended for the installation
Patch0:         task-skip-INSTALL.patch
BuildRequires:  awk
# for completion
BuildRequires:  bash
BuildRequires:  cmake >= 2.8
BuildRequires:  coreutils
BuildRequires:  gcc-c++
# for sync
BuildRequires:  libuuid-devel
BuildRequires:  cargo-packaging
BuildRequires:  vim-base
BuildRequires:  zsh
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
%autosetup -a1 -p1 -n task-%{version}

%build
%cmake -DTASK_DOCDIR:PATH=%{_docdir}/task \
    -DTASK_MAN1DIR:PATH=%{_mandir}/man1/ \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_STATIC_LIBS:BOOL=OFF \
    -DTASK_MAN5DIR:PATH=%{_mandir}/man5/
%cmake_build

%install
%cmake_install

# this integration stuff might be in CMakeList.txt, but ...
%define scriptsdir %{buildroot}%{_docdir}/task/scripts/

install -m 0755 -d %{buildroot}%{_datadir}/bash_completion.d/
mv %{scriptsdir}bash/task.sh %{buildroot}%{_datadir}/bash_completion.d/

install -m 0755 -d %{buildroot}%{_datadir}/zsh/site-functions/

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
%doc %{_docdir}/task
%{_bindir}/task*
%{_mandir}/man1/task*
%{_mandir}/man5/task*
%{_datadir}/bash_completion.d/
%{_datadir}/zsh/site-functions/
%dir %{_datadir}/fish/
%{_datadir}/fish/completions/
%{_datadir}/vim/site/ftdetect/task.vim
%{_datadir}/vim/site/syntax/task*.vim

%changelog
