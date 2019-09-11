#
# spec file for package hex
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hex
# I am not inclined towards the update to 1.8, see bsc#806703
Version:        1.4
Release:        0
Summary:        Yet Another Hex Dumper
License:        BSD-3-Clause
Group:          Development/Tools/Other
Url:            http://www.catb.org/~esr/hexdump/
Source:         http://www.catb.org/~esr/hexdump/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.diff
Provides:       util-linux:%{_bindir}/hex
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A hex dumper that does CP/M and EBCDIC formatting and has
internationalization support.

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags} clean
make CFLAGS="%{optflags} -Wall" CC="gcc" %{?_smp_mflags}

%install
mkdir -p %{buildroot}{%{_mandir}/man1,%{_bindir}}
make install DESTDIR=%{buildroot} MANDIR=%{_mandir}

%files
%defattr(-,root,root)
%doc READ.ME
%doc %{_mandir}/man?/*
%{_bindir}/hex

%changelog
