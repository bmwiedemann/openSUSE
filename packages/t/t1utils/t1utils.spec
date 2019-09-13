#
# spec file for package t1utils
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           t1utils
Version:        1.39
Release:        0
Summary:        A collection of simple type-1 font manipulation programs
License:        ISC
Group:          Productivity/Publishing/PS
Url:            http://www.lcdf.org/type/#t1utils
Source0:        http://www.lcdf.org/type/t1utils-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The t1utils are a collection of simple type-1 font manipulation programs.
Together, they allow you to convert between PFA (ASCII) and PFB
(binary) formats, disassemble PFA or PFB files into human-readable
form, and reassemble them into PFA or PFB format. Additionally, you can
extract font resources from a Macintosh font file (ATM/Laserwriter) or
create a Macintosh Type 1 font file from a PFA or PFB font.

%prep
%setup -q

%build
rm -f config.cache
# update config.{guess,sub}
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-, root, root)
%doc NEWS README
%{_bindir}/t1ascii
%{_bindir}/t1binary
%{_bindir}/t1asm
%{_bindir}/t1disasm
%{_bindir}/t1unmac
%{_bindir}/t1mac
%{_mandir}/man1/t1asm.1.gz
%{_mandir}/man1/t1disasm.1.gz
%{_mandir}/man1/t1unmac.1.gz
%{_mandir}/man1/t1mac.1.gz
%{_mandir}/man1/t1ascii.1.gz
%{_mandir}/man1/t1binary.1.gz

%changelog
