#
# spec file for package bam
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


Name:           bam
Version:        0.5.1
Release:        0
Summary:        Lua-based build system
License:        Zlib
URL:            https://github.com/matricks/bam
Source:         https://github.com/matricks/bam/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM bam-0.5.1-fix-compilation-order.patch -- https://github.com/matricks/bam/issues/116
Patch0:         bam-0.5.1-fix-compilation-order.patch
# PATCH-FIX-UPSTREAM https://github.com/matricks/bam/commit/b937572d157e660af98e224523ffb3fe5810ed2c
Patch1:         support-python3.patch
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(lua5.3)

%description
Bam is a build system focusing on arbitrary build scripts. Instead of
having a custom language, it uses Lua to describe the build steps.

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags}"
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_mandir}/man1
help2man --section=1 --name="fast and flexible build system" --version-string="VERSION_STRING" --no-info ./bam > %{buildroot}%{_mandir}/man1/bam.1

%check
export PYTHON="/usr/bin/python3"
make %{?_smp_mflags} test

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/bam.1%{?ext_man}

%changelog
