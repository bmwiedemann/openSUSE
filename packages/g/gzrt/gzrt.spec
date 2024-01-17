#
# spec file for package gzrt
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2015, Martin Hauke <mardnh@gmx.de>
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


Name:           gzrt
Version:        0.8
Release:        0
Summary:        Recover data from a corrupted gzip file
License:        GPL-2.0-only
Group:          Productivity/Archiving/Compression
URL:            https://www.urbanophile.com/arenn/hacking/gzrt/gzrt.html
Source:         http://www.urbanophile.com/arenn/hacking/gzrt/%{name}-%{version}.tar.gz
Patch0:         grzt-cflags.diff
BuildRequires:  zlib-devel

%description
gzrecover is a program that will attempt to extract any readable data
out of a gzip file that has been corrupted.

%prep
%autosetup -p1

%build
%make_build

%install
install -Dpm 0755 gzrecover \
  %{buildroot}/%{_bindir}/gzrecover
install -Dpm 0644 gzrecover.1 \
  %{buildroot}/%{_mandir}/man1/gzrecover.1

%files
%doc ChangeLog README
%{_bindir}/gzrecover
%{_mandir}/man1/gzrecover.1%{?ext_man}

%changelog
