#
# spec file for package posix_cc
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           posix_cc
Version:        1.4
Release:        0
Summary:        POSIX 1003.2 and 1003.1 2001 C Language Compilers
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
c89 is the name of the C language compiler as required by the POSIX
1003.2 standard, while c99 is the name required by the POSIX 1003.1
2001 standard. Both are actually wrappers for gcc, passing it the
options required to make it conform to said standards in addition to
the options passed via the command line.

Both will only accept those options mandated by the respective
standards.

%prep
%setup -q

%build
autoreconf -fiv
%configure

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-, root, root)
%{_bindir}/c89
%{_bindir}/c99
%{_mandir}/man1/c89.1%{ext_man}
%{_mandir}/man1/c99.1%{ext_man}

%changelog
