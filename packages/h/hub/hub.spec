#
# spec file for package hub
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define ver %{version}
Name:           hub
Version:        2.12.6
Release:        0
Summary:        Command-line wrapper for git and GitHub
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/github/hub
Source:         https://github.com/github/%{name}/archive/v%{ver}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fish
BuildRequires:  go
BuildRequires:  groff
BuildRequires:  vim
BuildRequires:  zsh
Provides:       rubygem-hub = %{version}
Obsoletes:      rubygem-hub < 2.0

%description
hub is a command line tool that wraps git in order to extend it with
extra features and commands that make working with GitHub easier.

%prep
%setup -q -n %{name}-%{ver}
sed -i -e 's#bin/ronn --#ronn --#' -e 's#script/bootstrap#true#' Makefile
chmod +x script/install.sh
sed -i -e 's#cd .*#true#' script/install.sh

%build
export LANG=en_US.UTF-8
export GOPATH=$PWD
mkdir -p $GOPATH/src/github.com/github/
# Copy the vendor directory into the GOPATH
cp -r $PWD/vendor/* $GOPATH/src
ln -s $PWD $GOPATH/src/github.com/github/hub
make %{?_smp_mflags} bin/hub man-pages

%install
prefix=%{buildroot}%{_prefix} script/install.sh
install -Dpm 0644 etc/hub.bash_completion.sh \
  %{buildroot}%{_datadir}/bash-completion/completions/hub
install -Dpm 0644 etc/hub.fish_completion \
  %{buildroot}%{_datadir}/fish/vendor_completions.d/hub.fish
install -Dpm 0644 etc/hub.zsh_completion \
  %{buildroot}%{_datadir}/zsh/site-functions/_hub
# Install vim-related files to a vim runtimepath that is set per default on openSUSE
install -d %{buildroot}%{_datadir}/vim/site
mv %{buildroot}%{_datadir}/vim/vimfiles/* %{buildroot}%{_datadir}/vim/site

%check
#make test
#make test-all

%files
%doc README.md
%license LICENSE
%{_bindir}/hub
%{_mandir}/man1/hub.1%{?ext_man}
%{_mandir}/man1/hub-*.1%{?ext_man}
%{_datadir}/bash-completion/completions/hub
%{_datadir}/fish/vendor_completions.d/hub.fish
%{_datadir}/zsh/site-functions/_hub
%{_datadir}/vim/site/ftdetect/pullrequest.vim
%{_datadir}/vim/site/syntax/pullrequest.vim

%changelog
