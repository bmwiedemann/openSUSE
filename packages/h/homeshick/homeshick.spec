#
# spec file for package homeshick
#
# Copyright (c) 2023 SUSE LLC
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


Name:           homeshick
Version:        2.0.1
Release:        0
Summary:        Dotfile synchronizer based on Git and Bash
License:        MIT
Group:          Productivity/File utilities
URL:            https://github.com/andsens/homeshick
Source0:        https://github.com/andsens/homeshick/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        README-openSUSE.md
Source50:       https://github.com/bats-core/bats-file/archive/v0.3.0.tar.gz#/bats-file-0.3.0.tar.gz
Source51:       https://github.com/bats-core/bats-support/archive/v0.3.0.tar.gz#/bats-support-0.3.0.tar.gz
Source52:       https://github.com/bats-core/bats-assert/archive/v2.0.0.tar.gz#/bats-assert-2.0.0.tar.gz
Source99:       homeshick.rpmlintrc
Patch0:         suse-packaging.patch
Patch1:         test-helper.patch
BuildRequires:  expect
BuildRequires:  git >= 1.5
BuildRequires:  iputils
BuildRequires:  tcsh
Requires:       bash >= 3
Requires:       git >= 1.5
BuildArch:      noarch
%if 0%{?is_opensuse}
BuildRequires:  bats
BuildRequires:  dash
BuildRequires:  fish
%endif

%description
Homeshick is a tool for users to manage configuration files, also known as
dotfiles. It leverages Git repositories to store and version dotfiles, and to
synchronize dotfile repositories between accounts and/or machines.

For example, this allows managing personal dotfiles alongside emacs or vim
plugins without clutter. It also makes it easy to install large external
frameworks, such as oh-my-zsh, found on sites like https://dotfiles.github.io/.

%prep
%autosetup -p1

# unpack test libraries
mkdir -p test/bats/lib
for lib in file support assert; do
	tar -xf %{_sourcedir}/bats-$lib-*.tar.gz -C test/bats/lib --transform "s/bats-$lib-...../$lib/"
done

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{name}.sh %{name}.fish %{name}.csh bin lib completions %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/bin/homeshick %{buildroot}%{_bindir}/%{name}
cp %{SOURCE1} .

%check
# run tests if bats is available
if type bats &>/dev/null; then
	HOMESHICK_DIR=%{buildroot}%{_datadir}/%{name} HOMESHICK_TEST_DIR="$PWD" bats test/suites
fi

%files
%doc README.md README-openSUSE.md CONTRIBUTING.md
%license LICENSE
%{_datadir}/%{name}
%{_bindir}/homeshick

%changelog
