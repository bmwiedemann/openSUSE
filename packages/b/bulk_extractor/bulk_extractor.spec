#
# spec file for package bulk_extractor
#
# Copyright (c) 2023 SUSE LLC
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


%ifarch aarch64 %{arm}
# Workaround until fixed upstream - https://github.com/simsong/bulk_extractor/issues/360
%define _lto_cflags %{nil}
%endif

Name:           bulk_extractor
Version:        2.0.0
Release:        0
Summary:        Bulk Email and URL extraction tool
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/simsong/bulk_extractor/wiki/Introducing-bulk_extractor
Source:         https://github.com/simsong/bulk_extractor/releases/download/v2.0.0/bulk_extractor-2.0.0.tar.gz
Patch1:         gcc13.diff
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  libewf-devel
BuildRequires:  libexiv2-devel
BuildRequires:  liblightgrep-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
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
%configure
%make_build

%install
%make_install
install -dm 0755 "%{buildroot}/%{_datadir}/%{name}"

%files
%doc ChangeLog README COPYING
%doc doc
%{_mandir}/man1/bulk_extractor.1.gz
%{_bindir}/bulk_extractor
%{_bindir}/test_be
%{_datadir}/%{name}

%changelog
