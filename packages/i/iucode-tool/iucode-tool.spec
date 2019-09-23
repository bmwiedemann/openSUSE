#
# spec file for package iucode-tool
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


Name:           iucode-tool
Version:        2.3.1
Release:        0
Summary:        A program to manipulate Intel microcode update collections
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://gitlab.com/iucode-tool/iucode-tool
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
ExclusiveArch:  %{ix86} x86_64

%description
iucode_tool is a program to manipulate microcode update collections for
Intel® i686 and X86-64 system processors, and prepare them for use by the
Linux kernel.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc README
%{_sbindir}/iucode_tool
%{_mandir}/man8/iucode_tool.8%{ext_man}

%changelog
