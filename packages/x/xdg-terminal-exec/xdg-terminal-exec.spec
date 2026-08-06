#
# spec file for package xdg-terminal-exec
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


Name:           xdg-terminal-exec
Version:        20260729+git.065925d
Release:        0
Summary:        XDG terminal execution utility and default terminal specification
License:        GPL-3.0-or-later
URL:            https://github.com/Vladimir-csp/xdg-terminal-exec/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bats
BuildRequires:  scdoc

%description
Utility for XDG terminal execution and defining a systems default graphical terminal emulator.

%prep
%autosetup -p1

%build
:

%install
%make_install prefix=%{_prefix}

%check
bats test

%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/*

%changelog
