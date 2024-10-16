#
# spec file for package dtrx
#
# Copyright (c) 2024 SUSE LLC
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


Name:           dtrx
Version:        8.5.3
Release:        0
Summary:        Intelligent Archive Extraction Tool
License:        GPL-3.0-only
URL:            https://brettcsmith.org/2007/dtrx/
Source:         https://github.com/dtrx-py/dtrx/releases/download/%{version}/dtrx-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       bzip2
Requires:       cpio
Requires:       gzip
Requires:       tar
Requires:       unzip
Suggests:       cabextract
Suggests:       ncompress
Suggests:       p7zip
Suggests:       rubygems
BuildArch:      noarch

%description
dtrx stands for "Do The Right Extraction". It is a tool for Unix-like
systems for extracting different archive formats.

Features:
* Support for many archive types, including tar, zip, cpio, deb, rpm,
  gem, 7z, cab, gz, bz2, and lzma files. Extra compression like
  .tar.bz2 is recognized.
* Archives are extracted into their own dedicated directories.
* All extracted files can be read and written, while leaving the rest
  of the permissions intact.
* dtrx can find archives inside the archive and extract those too.

%prep
%autosetup

%build
%python3_build

%install
%python3_install

%files
%license COPYING
%doc README.md
%{_bindir}/dtrx
%{python3_sitelib}/*

%changelog
