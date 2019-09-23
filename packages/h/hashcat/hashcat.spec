#
# spec file for package hashcat
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


Name:           hashcat
Version:        5.1.0
Release:        0
Summary:        CPU-based password recovery utility
License:        MIT AND GPL-2.0-or-later
Group:          Productivity/Security
Url:            https://hashcat.net/

#Git-Clone:	git://github.com/hashcat/hashcat
Source:         https://github.com/hashcat/hashcat/archive/v%version.tar.gz
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  opencl-headers
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64

%description
Hashcat is an advanced CPU-based password recovery utility,
supporting seven unique modes of testing for over 100 optimized
hashing algorithms.

%prep
%setup -q

%build
make %{?_smp_mflags} COMPTIME=0 our_CFLAGS="%optflags" PREFIX="%_prefix"

%install
%make_install PREFIX="%_prefix" DOCUMENT_FOLDER="%_docdir/%name"
%fdupes %buildroot/%_prefix

%files
%defattr(-,root,root)
%doc README.md
%_bindir/hashcat
%_datadir/%name/
%_docdir/%name/

%changelog
