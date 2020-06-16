#
# spec file for package scdoc
#
# Copyright (c) 2020 SUSE LLC
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


Name:           scdoc
Version:        1.11.0
Release:        0
Summary:        A man page generator written in C99
License:        MIT
Group:          Development/Tools/Doc Generators
URL:            https://git.sr.ht/~sircmpwn/scdoc/
Source:         https://git.sr.ht/~sircmpwn/scdoc/archive/%{version}.tar.gz
Source1:        scdoc-rpmlintrc
Patch0:         scdoc-1.6.1-makefile.patch
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  glibc-devel-static
BuildRequires:  make

%description
scdoc is a man page generator written for POSIX systems written in C99.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} PCDIR=%{buildroot}/usr/share/pkgconfig %{?_smp_mflags} 

%files
%{_bindir}/scdoc
%{_mandir}/man?/scdoc.?%{?ext_man}
/usr/share/pkgconfig/scdoc.pc

%changelog
