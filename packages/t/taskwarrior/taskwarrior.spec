#
# spec file for package taskwarrior
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


Name:           taskwarrior
Version:        3.4.2
Release:        0
Summary:        Command-line todo list manager
License:        MIT
Group:          Productivity/Office/Organizers
URL:            https://taskwarrior.org/
Source0:        https://github.com/GothenburgBitFactory/%{name}/releases/download/v%{version}/task-%{version}.tar.gz
Source1:        vendor.tar.zst
#PATCH-FIX-OPENSUSE: skip the INSTALL and LICENSE from files intended for the installation
Patch0:         task-skip-INSTALL.patch
Patch1:         fix-corrosion.patch
Patch2:         fix_cmake_ignore_hash.patch
BuildRequires:  awk
# for completion
BuildRequires:  bash
BuildRequires:  cmake >= 2.8
BuildRequires:  coreutils
BuildRequires:  corrosion
BuildRequires:  gcc-c++
# for sync
BuildRequires:  libuuid-devel
BuildRequires:  cargo-packaging
BuildRequires:  cxxbridge
BuildRequires:  execstack
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

# Setup cargo dir for when corrosion tries to pull in the crates
%cmake -DBUILD_SHARED_LIBS:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DSYSTEM_CORROSION=ON -DTASK_DOCDIR=share/doc/packages/task -DTASK_RCDIR=share/doc/packages/task/rc
# Mark stack as non-executable
export LDFLAGS=$LDFLAGS:"-z noexecstack"
%cmake_build

%install
%cmake_install

# This should go into /usr/share/doc/PACKAGES/task!

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

# Mark stack as non-executable. This happens due to some quirks in the hybrid build, missing linker flags.
execstack -c %{buildroot}%{_bindir}/task

#check
#cmake --build build --target test_runner
#ctest --test-dir build

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
