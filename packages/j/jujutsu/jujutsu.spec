#
# spec file for package jujutsu
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


%define binary_name jj

Name:           jujutsu
Version:        0.18.0
Release:        0
Summary:        Git-compatible DVCS that is both simple and powerful
License:        MIT
URL:            https://github.com/martinvonz/jj
Source0:        jj-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.76
BuildRequires:  cargo-packaging
BuildRequires:  gnupg
BuildRequires:  openssh-common
BuildRequires:  openssl-devel
BuildRequires:  zstd

%description
Jujutsu is a Git-compatible DVCS. It combines features from Git (data model, speed), Mercurial (anonymous branching, simple CLI free from "the index", revsets, powerful history-rewriting), and Pijul/Darcs (first-class conflicts), with features not found in most of them (working-copy-as-a-commit, undo functionality, automatic rebase, safe replication via rsync, Dropbox, or distributed file system).

The command-line tool is called jj for now because it's easy to type and easy to replace (rare in English). The project is called "Jujutsu" because it matches "jj".

Jujutsu is relatively young, with lots of work to still be done. If you have any questions, or want to talk about future plans, please join us on Discord Discord or start a GitHub Discussion; the developers monitor both channels.

Important
Jujutsu is an experimental version control system. While Git compatibility is stable, and most developers use it daily for all their needs, there may still be work-in-progress features, suboptimal UX, and workflow gaps that make it unusable for your particular use.

%prep
%autosetup -p 1 -a 1 -n jj-%{version}
mkdir -p .cargo
rm -vf .cargo/config.toml

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{binary_name}-%{version}/target/release/%{binary_name} %{buildroot}%{_bindir}/%{binary_name}

%check
rm -rf tests/contest/
%{cargo_test}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{binary_name}

%changelog
