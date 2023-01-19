#
# spec file for package debugbreak
#
# Copyright (c) 2023 SUSE LLC
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


Name:           debugbreak
Version:        1.0~git.20210702
Release:        0
BuildArch:      noarch
Summary:        Breakpoint injector for C/C++ code
License:        BSD-2-Clause
URL:            https://github.com/scottt/debugbreak
Source:         %{name}-%{version}.tar.xz

%description
debugbreak.h allows setting breakpoints in C/C++ code with a call to
the debug_break() function.

* Include one header file and insert calls to debug_break() in the code where
  you wish to trap into the debugger.
* Works well on ARM, AArch64, i686, x86-64, POWER and has a fallback code path
  for other architectures.
* Works like the DebugBreak() fuction provided by Windows and QNX.

%package devel
Summary:        Development files for debugbreak
Requires:       %{name} = %{version}

%description devel
This package contains the header file needed to use debug_break.

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 %{name}.h %{buildroot}%{_includedir}/%{name}.h

%files
%license COPYING
%doc README.md

%files devel
%{_includedir}/%{name}.h

%changelog
