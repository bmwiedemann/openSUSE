#
# spec file for package bulk_extractor
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           bulk_extractor
Version:        2.1.1
Release:        0
Summary:        Bulk Email and URL extraction tool
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/simsong/bulk_extractor/wiki/Introducing-bulk_extractor
Source:         https://github.com/simsong/bulk_extractor/releases/download/v%version/bulk_extractor-%version.tar.gz
Patch1:         gcc13.diff
Patch2:         libewf-wide.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libewf)
BuildRequires:  pkgconfig(lightgrep)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)
# We need fiwalk which was added to sleuthkit in v4.1.0
Requires:       sleuthkit >= 4.1

%description
bulk_extractor is a C++ program that scans a disk image, a file, or a
directory of files and extracts useful information without parsing the
file system or file system structures. The results are stored in feature
files that can be easily inspected, parsed, or processed with automated
tools. bulk_extractor also created a histograms of features that it finds,
as features that are more common tend to be more important.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
install -dm 0755 "%{buildroot}/%{_datadir}/%{name}"

%files
%doc ChangeLog README
%doc doc
%license COPYING
%{_mandir}/man1/bulk_extractor.1.gz
%{_bindir}/bulk_extractor
%{_datadir}/%{name}

%changelog
