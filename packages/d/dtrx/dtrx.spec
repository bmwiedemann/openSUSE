#
# spec file for package dtrx
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


Name:           dtrx
Version:        8.7.1
Release:        0
Summary:        Intelligent Archive Extraction Tool
License:        GPL-3.0-only
URL:            https://brettcsmith.org/2007/dtrx/
Source:         https://github.com/dtrx-py/dtrx/releases/download/%{version}/dtrx-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools >= 75
BuildRequires:  python3-wheel
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
# dtrx.py is imported, never executed (entry point is %%{_bindir}/dtrx);
# drop its stray shebang (rpmlint non-executable-script).
sed -i '1{/^#!/d}' dtrx/dtrx.py

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -B -c "import dtrx.dtrx"

%files
%license COPYING
%doc README.md
%{_bindir}/dtrx
%{python3_sitelib}/dtrx
%{python3_sitelib}/dtrx-%{version}.dist-info

%changelog
