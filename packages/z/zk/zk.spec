#
# spec file for package zk
#
# Copyright (c) 2022 SUSE LLC
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


Name:           zk
Version:        0.12.0
Release:        0
Summary:        Plain text note-taking assistant for markdown
License:        BSD-2-Clause
Group:          System/Shells
URL:            https://github.com/mickael-menu/zk
Source0:        https://github.com/mickael-menu/zk/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
Recommends:     fzf

%description
Zk is a plain text note-taking assistant for markdown.
It is a command-line tool helping you to maintain a plain text Zettelkasten or personal wiki.

%prep
%setup -q -a 1

%build
%goprep github.com/mickael-menu/zk
%gobuild

%install
%goinstall

%files
%{_bindir}/%{name}
%license LICENSE
%doc CHANGELOG.md README.md docs/*.md

%changelog
