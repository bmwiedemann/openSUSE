#
# spec file for package memleax
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


Name:           memleax
Version:        1.1.1
Release:        0
Summary:        Debugs memory leak of a running process
License:        GPL-2.0-only
URL:            https://wubingzheng.github.io/memleax/
Source0:        https://github.com/WuBingzheng/memleax/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libunwind-devel
ExclusiveArch:  %ix86 x86_64 %arm aarch64

%description
Memleax is capable of debugging memory leak of a running process by
attaching to it. There is no need to recompile the program or restart the
target process.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
# not an autotools configure
./configure --prefix=%{_prefix}
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/memleax
%{_mandir}/man1/memleax.1%{?ext_man}

%changelog
