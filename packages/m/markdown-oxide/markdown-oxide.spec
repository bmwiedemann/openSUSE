#
# spec file for package markdown-oxide
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


Name:           markdown-oxide
Version:        0.25.0
Release:        0
Summary:        A markdown language server with Obsidian syntax support
License:        Apache-2.0
URL:            https://github.com/Feel-ix-343/markdown-oxide
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
A markdown language server with Obsidian syntax support.
Markdown Oxide does not aim to fully replace Obsidian; it serves to
provide a feature rich and advanced note taking experience.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%check
%{cargo_test}

%install
# locked is required due to a missing lockfile on tower-lsp
%{cargo_install} --locked

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
