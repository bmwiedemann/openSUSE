#
# spec file for package gitui
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gitui
Version:        0.26.3
Release:        0
Summary:        Terminal UI for git
License:        (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Artistic-2.0 OR CC0-1.0) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CDDL-1.0 AND ISC AND MIT AND MIT AND CC-BY-3.0 AND MPL-2.0 AND SUSE-GPL-2.0-with-linking-exception
URL:            https://github.com/extrawurst/gitui
Source0:        https://github.com/extrawurst/gitui/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(zlib)

%description
TUI for git with the following features:
  * Fast and intuitive keyboard only control
  * Context based help (no need to memorize tons of hot-keys)
  * Inspect, commit, and amend changes (incl. hooks: pre-commit,commit-msg,post-commit)
  * Stage, unstage, revert and reset files, hunks and lines
  * Stashing (save, pop, apply, drop, and inspect)
  * Push/Fetch to/from remote
  * Branch List (create, rename, delete, checkout, remotes)
  * Browse commit log, diff committed changes
  * Scalable terminal UI layout
  * Async git API for fluid control
  * Submodule support

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE.md
%doc CHANGELOG.md README.md FAQ.md THEMES.md
%{_bindir}/%{name}

%changelog
