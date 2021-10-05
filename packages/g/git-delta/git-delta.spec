#
# spec file for package git-delta
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


Name:           git-delta
Version:        0.8.3
Release:        0
Summary:        A syntax-highlighter for git and diff output
License:        MIT
URL:            https://github.com/dandavison/delta
Source0:        https://github.com/dandavison/delta/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  git
Conflicts:      sccs

%description
Delta provides language syntax-highlighting, within-line insertion/deletion detection, and restructured diff output for git on the command line.

%prep
%setup -qa 1 -n delta-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%check
%{cargo_test}

%install
%{cargo_install}

# install bash completion
install -D -m 0644 %{_builddir}/delta-%{version}%{_sysconfdir}/completion/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/delta

%files
%license LICENSE
%doc README.md
%{_bindir}/delta
%{_datadir}/bash-completion/completions/delta

%changelog
