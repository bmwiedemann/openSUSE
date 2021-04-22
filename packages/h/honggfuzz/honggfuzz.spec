#
# spec file for package honggfuzz
#
# Copyright (c) 2021 SUSE LLC
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


Name:           honggfuzz
Version:        2.4
Release:        0
Summary:        Security-oriented fuzzer with various analysis options
License:        Apache-2.0
Group:          Development/Tools/Other
URL:            https://honggfuzz.com
Source:         https://github.com/google/honggfuzz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  binutils-devel
BuildRequires:  libunwind-devel
BuildRequires:  zlib-devel

%description
Security-oriented fuzzer with powerful analysis options. Supports
evolutionary, feedback-driven fuzzing based on code coverage
(software and hardware).

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
%make_build ARCH_LDFLAGS="-L/usr/local/include -L/usr/include -lpthread -lunwind-ptrace -lunwind-generic -lbfd -lopcodes -lrt -liberty -lz -ldl"

%install
install -Dpm 0755 %{name} \
  %{buildroot}%{_bindir}/%{name}

%files
%license COPYING
%doc CHANGELOG CONTRIBUTING.md README.md
%{_bindir}/%{name}

%changelog
