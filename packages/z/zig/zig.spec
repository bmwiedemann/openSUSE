#
# spec file for package zig
#
# Copyright (c) 2025 SUSE LLC and contributors
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

%global version_suffix 0.15
%global version_current 0.15.1
%bcond_without  macro

Name:           zig
Version:        %{version_current}
Release:        0
Summary:        Compiler for the Zig language
License:        MIT
Group:          Development/Languages/Other
URL:            https://ziglang.org/
Source0:        README
Requires:       zig-implementation
Recommends:     zig%{version_suffix}


%description
General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.

* Robust - behavior is correct even for edge cases such as out of memory.
* Optimal - write programs the best way they can behave and perform.
* Reusable - the same code works in many environments which have different constraints.
* Maintainable - precisely communicate intent to the compiler and other programmers.
The language imposes a low overhead to reading code and is resilient to changing requirements and environments.

%package libs
Summary:        Zig Standard Library
BuildArch:      noarch
Requires:       zig-libs-implementation
Recommends:     zig-libs%{version_suffix}
#obsolete_zig_versioned zig-libs

%description libs
%{name} %{version_current} Standard Library

%if %{with macro}
%package        rpm-macros
Summary:        Common RPM macros for %{name}
Requires:       rpm
Requires:       zig-rpm-macros-implementation
Recommends:     zig-rpm-macros%{version_suffix}
BuildArch:      noarch
#obsolete_zig_versioned zig-rpm-macros

%description    rpm-macros
This package contains common RPM macros for %{name} version %{version_current}.
%endif

%prep

%build

%install
install -D -m 0644 %{S:0} %{buildroot}%{_datadir}/doc/packages/zig/README

%files
%defattr(-,root,root,-)
%doc %{_datadir}/doc/packages/zig

%changelog
