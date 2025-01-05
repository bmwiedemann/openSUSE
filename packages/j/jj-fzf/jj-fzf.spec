#
# spec file for package jj-fzf
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


Name:           jj-fzf
Version:        0.24.0
Release:        0
Summary:        Text UI for Jujutsu based on fzf
License:        MPL-2.0
URL:            https://github.com/tim-janik/jj-fzf
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  bash >= 5.1.16
BuildRequires:  coreutils
BuildRequires:  fzf
BuildRequires:  gawk
BuildRequires:  jujutsu
BuildRequires:  sed
Requires:       bash >= 5.1.16
Requires:       coreutils
Requires:       fzf
Requires:       gawk
Requires:       jujutsu
Requires:       sed

%description
JJ-FZF is a text UI for jj based on fzf, implemented as a bash shell script.
The main view centers around jj log, providing previews for the jj diff or jj
obslog of every revision. Several key bindings are available to quickly perform
actions such as squashing, swapping, rebasing, splitting, branching,
committing, abandoning revisions and more. A separate view for the operations
log jj op log enables fast previews of old commit histories or diffs between
operations, making it easy to jj undo any previous operation. The available
hotkeys are displayed onscreen for simple discoverability. The commands and key
bindings can also be displayed with jj-fzf --help and are documented in the
wiki: jj-fzf-help

The jj-fzf script is implemented in bash-5.1, using fzf and jj with git.
Command line tools like sed, grep, gawk are assumed to provide GNU tool
semantics.

%prep
%autosetup -p1

%build
sed -i 's#env bash#bash#' %{name}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
# version output without leading "v"
%{buildroot}%{_bindir}/%{name} --version | grep %{version}

%files
%license LICENSE
%doc README.md NEWS.md
%{_bindir}/%{name}

%changelog

