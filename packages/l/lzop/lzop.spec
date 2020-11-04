#
# spec file for package lzop
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


Name:           lzop
Version:        1.04
Release:        0
Summary:        Dictionary-based LZ-type compressor favoring speed
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://www.lzop.org
Source0:        http://www.lzop.org/download/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
BuildRequires:  cmake >= 3.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lzo2)

%description
lzop is a general-purpose file compressor similar to gzip.
It favors higher compression and decompression speed at the cost
of compression ratio.

lzop was designed with the following goals in mind:
- speed (both compression and decompression)
- reasonable drop-in compatibility to gzip
- portability

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
# Remove unwanted doc folder created during build
rm -fr %{buildroot}%{_datadir}/doc

%check
%ctest

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%license COPYING
%{_bindir}/lzop
%{_mandir}/man1/lzop.1%{?ext_man}

%changelog
