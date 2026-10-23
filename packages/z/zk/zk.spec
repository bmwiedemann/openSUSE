#
# spec file for package zk
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        0.15.7
Release:        0
Summary:        Plain text note-taking assistant for markdown
# Legal-Review-Notice: Upstream zk is GPL-3.0-only (LICENSE); vendored github.com/gosimple/slug is MPL-2.0 (source included in vendor.tar.gz in src.rpm).
License:        GPL-3.0-only AND MPL-2.0
URL:            https://github.com/zk-org/zk
Source0:        https://github.com/zk-org/zk/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  c_compiler
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.25
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(sqlite3)
Requires:       fzf

%description
Zk is a plain text note-taking assistant for markdown.
It is a command-line tool helping you to maintain a plain text Zettelkasten or personal wiki.

%prep
%setup -q -a1

%build
%ifarch ppc64
BUILDMOD=""
%else
BUILDMOD="-buildmode=pie"
%endif
export RPM_OPT_FLAGS="%{optflags}"
go build -v -x -mod=vendor $BUILDMOD -a -ldflags "-s -X main.Version=%{version} -X main.Build=955cb76" --tags "icu json1 fts5 secure_delete"

%install
install -Dm755 zk %{buildroot}%{_bindir}/zk

%check
%make_build test

%files
%{_bindir}/%{name}
%license LICENSE
%doc CHANGELOG.md README.md

%changelog
