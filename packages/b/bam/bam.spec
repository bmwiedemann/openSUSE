#
# spec file for package bam
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           bam
Version:        0.5.1
Release:        0
Summary:        Lua-based build system
License:        Zlib
Group:          Development/Tools/Building
Url:            http://matricks.github.com/bam/
Source:         https://github.com/matricks/bam/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM bam-0.5.1-fix-compilation-order.patch -- https://github.com/matricks/bam/issues/116
Patch0:         bam-0.5.1-fix-compilation-order.patch
BuildRequires:  gcc-c++
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(lua5.3)

%description
Bam is a build system focusing on arbitrary build scripts. Instead of
having a custom language, it uses Lua to describe the build steps.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_mandir}/man1
pandoc docs/bam.1.txt -s -t man > %{buildroot}%{_mandir}/man1/bam.1

%check
make %{?_smp_mflags} test

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/bam.1%{?ext_man}

%changelog
