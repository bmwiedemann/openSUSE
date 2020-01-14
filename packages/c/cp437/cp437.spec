#
# spec file for package cp437
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


Name:           cp437
Version:        0.6
Release:        0
Summary:        Code page 437 emulator
License:        BSD-3-Clause
Group:          System/Console
URL:            https://github.com/keaston/cp437
Source:         https://github.com/keaston/cp437/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Cp437 is a program to emulate an old-style "code page 437" / "IBM-PC" character
set terminal on a modern terminal emulator that uses UTF-8 or similar.

It was written for the purpose of running the BitchX IRC client, which utilises
CP437 line-drawing characters in its default theme and artwork.  It should
also be broadly useful for things like viewing CP437 "ANSI art", running
nethack with the IBMgraphics option or running EPIC with scripts that use CP437
artwork.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -D -m0755 cp437 %{buildroot}%{_bindir}/cp437

%files
%license COPYRIGHT
%doc README
%{_bindir}/cp437

%changelog
