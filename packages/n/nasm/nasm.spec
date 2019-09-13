#
# spec file for package nasm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nasm
Version:        2.14.02
Release:        0
Summary:        Netwide Assembler (An x86 Assembler)
License:        BSD-2-Clause
Group:          Development/Languages/Other
URL:            http://www.nasm.us/
Source:         http://www.nasm.us/pub/nasm/releasebuilds/%{version}/nasm-%{version}.tar.xz
BuildRequires:  fdupes

%description
NASM is a prototype general-purpose x86 assembler. It can currently output
several binary formats, including ELF, a.out, Win32, and OS/2.

%prep
%autosetup

%build
%configure \
  --enable-lto
make %{?_smp_mflags} all

%install
%make_install rdf_install
%fdupes %{buildroot}%{_mandir}

%check
make %{?_smp_mflags} test

%files
%license LICENSE
%doc AUTHORS CHANGES ChangeLog README
%{_bindir}/ldrdf
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_bindir}/rdf2bin
%{_bindir}/rdf2com
%{_bindir}/rdf2ihx
%{_bindir}/rdf2ith
%{_bindir}/rdf2srec
%{_bindir}/rdfdump
%{_bindir}/rdflib
%{_bindir}/rdx
%{_mandir}/man1/ldrdf.1%{?ext_man}
%{_mandir}/man1/nasm.1%{?ext_man}
%{_mandir}/man1/ndisasm.1%{?ext_man}
%{_mandir}/man1/rdf2bin.1%{?ext_man}
%{_mandir}/man1/rdf2com.1%{?ext_man}
%{_mandir}/man1/rdf2ihx.1%{?ext_man}
%{_mandir}/man1/rdf2ith.1%{?ext_man}
%{_mandir}/man1/rdf2srec.1%{?ext_man}
%{_mandir}/man1/rdfdump.1%{?ext_man}
%{_mandir}/man1/rdflib.1%{?ext_man}
%{_mandir}/man1/rdx.1%{?ext_man}

%changelog
