#
# spec file for package zk
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


Name:           zk
Version:        0.14.1
Release:        0
Summary:        Plain text note-taking assistant for markdown
License:        BSD-2-Clause
Group:          System/Shells
URL:            https://github.com/zk-org/zk
Source0:        https://github.com/zk-org/zk/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
# PATCH-FIX-UPSTREAM fix_test.patch -- based on commit e3c5784fb84a792491724fe4cc1f26e2c9d01b60
Patch0:         fix_test.patch
BuildRequires:  c_compiler
BuildRequires:  zstd
BuildRequires:  golang(API)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(sqlite3)
Requires:       fzf

%description
Zk is a plain text note-taking assistant for markdown.
It is a command-line tool helping you to maintain a plain text Zettelkasten or personal wiki.

%prep
%setup -qa1
%autopatch -p1

%build
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export RPM_OPT_FLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.Version=%{version} -X main.Build=578894f" --tags "icu json1 fts5 secure_delete"

%install
install -Dm755 zk %{buildroot}%{_bindir}/zk

%check
make test

%files
%{_bindir}/%{name}
%license LICENSE
%doc CHANGELOG.md README.md docs/*.md

%changelog
