#
# spec file for package jefferson
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           jefferson
Version:        0.3+git.20160616
Release:        0
Summary:        JFFS2 filesystem extraction tool
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/sviehb/jefferson
Source:         %{name}-%{version}.tar.xz
# Add support for python3
Patch0:         https://github.com/sviehb/jefferson/pull/18.patch
Patch1:         jefferson-use-pylzma.patch
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
BuildRequires:  python3-cstruct >= 1.5
BuildRequires:  python3-setuptools
BuildRequires:  python3-pylzma
Requires:       python3-cstruct >= 1.5
Requires:       python3-pylzma
BuildArch:      noarch

%description
A JFFS2 filesystem extraction tool written in python.

Features:
 - Big/Little Endian support
 - JFFS2_COMPR_ZLIB, JFFS2_COMPR_RTIME, and
   JFFS2_COMPR_LZMA compression support
 - CRC checks - for now only enforced on hdr_crc
 - Extraction of symlinks, directories, files, and device nodes
 - Detection/handling of duplicate inode numbers. Occurs if multiple
   JFFS2 filesystems are found in one file and causes jefferson
   to treat segments as separate filesystems

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod -x README.md

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
help2man %{buildroot}/%{_bindir}/jefferson --no-discard-stderr --version-string="%{version}" --no-info > jefferson.1
install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/jefferson
%{_mandir}/man1/jefferson.1%{?ext_man}
%{python3_sitelib}/jefferson*

%changelog
