#
# spec file for package git-who
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           git-who
Version:        1.3
Release:        0
Summary:        Git blame for file trees
License:        MIT
URL:            https://github.com/sinclairtarget/git-who
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  git-core
BuildRequires:  go >= 1.23
BuildRequires:  zsh

%description
git-who is a command-line tool for answering that eternal question:

    Who wrote this code?!

Unlike git blame, which can tell you who wrote a line of code, git-who tells
you the people responsible for entire components or subsystems in a codebase.
You can think of git-who sort of like git blame but for file trees rather than
individual files.

%prep
%autosetup -p 1 -a 1

%build
# hash will be shortened by COMMIT_HASH:0:8 later
COMMIT_HASH=9ad01eb363ff2617b1e9da941ec708acc20a6967

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.Version=v%{version} \
   -X main.Commit=${COMMIT_HASH:0:8}" \
   -o bin/%{name}

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} -version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
