#
# spec file for package tui-journal
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 mantarimay
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


%bcond_without test
Name:           tui-journal
Version:        0.13.1
Release:        0
Summary:        Write and manage journals/notes from the terminal
License:        MIT
URL:            https://github.com/AmmarAbouZor/tui-journal
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  openssl-devel

%description
TUI-Journal is a terminal-based application written in Rust that allows
you to write and manage your journal/notes from within the comfort of your
terminal. It provides a simple and efficient interface for creating and
organizing your thoughts, ideas, and reflections. TUI-Journal supports two
different local back-ends: a plain text back-end in JSON format and a
database back-end using SQLite.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/tjournal -t %{buildroot}%{_bindir}

%if %{with test}
%check
%{cargo_test}
%endif

%files
%license LICEN*
%doc README*
%{_bindir}/tjournal

%changelog
