#
# spec file for package git-interactive-rebase-tool
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


Name:           git-interactive-rebase-tool
Version:        2.3.0~0
Release:        0
Summary:        Terminal-based sequence editor for git interactive rebase
License:        GPL-3.0-or-later
Group:          Development/Tools/Version Control
URL:            https://github.com/MitMaro/git-interactive-rebase-tool
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
Native cross-platform full feature terminal-based sequence editor for git interactive rebase.

%prep
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%{_bindir}/interactive-rebase-tool

%changelog
