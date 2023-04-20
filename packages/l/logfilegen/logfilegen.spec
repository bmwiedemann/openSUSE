#
# spec file for package logfilegen
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           logfilegen
Version:        3.0.3
Release:        0
Summary:        Log file generator for server log files and user-defined formats
License:        Unlicense
URL:            https://psemiletov.github.io/logfilegen/
Source:         https://github.com/psemiletov/logfilegen/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake

%description
Logfilegen is a tool to generate common server (nginx, etc) or user-defined
format log files. It can generate log file with the desired rate (lines per
second), the file size, lines count and the duration. Each variable of the log
file can be redefined by the random or static value. The tool is designed to
be fast and customizable.

%prep
%autosetup -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	%{nil}
%make_build

%install
%cmake_install

%files
%license LICENSE
%doc ChangeLog README.md
%doc docs/config.md docs/templates.md
%{_bindir}/logfilegen

%changelog
