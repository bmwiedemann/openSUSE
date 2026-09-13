# vim: set ts=4 sw=4 et:
#
# spec file for package patool
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           patool
Version:        4.1.0
Release:        0
Summary:        Portable Command Line Archive File Manager
License:        GPL-3.0-or-later
URL:            https://github.com/wummel/patool
Source:         https://github.com/wummel/patool/releases/download/%{version}/patool-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.12
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  unzip
BuildRequires:  zip
# upstream no longer provides a bash completion file
Obsoletes:      %{name}-bash-completion
Provides:       %{name}-bash-completion
BuildArch:      noarch

%description
patool is a portable command line archive file manager. Various archive types
can be created, extracted, tested and listed by patool.
The advantage of patool is its simplicity in handling archive files without
having to remember a myriad of programs and options.
The archive format is determined by the file(1) program and as a fallback by
the archive file extension.

patool supports 7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc), ARJ
(.arj), BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio), DEB (.deb), GZIP
(.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma), LZOP (.lzo),
RPM (.rpm), RAR (.rar), TAR (.tar), XZ (.xz), and ZIP (.zip, .jar) formats.

It relies on helper applications to handle those archive formats.

%prep
%autosetup -n patool-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}

%check
# single-flavor spec (python3_* macros): run the suite with the default
# interpreter; the bare pytest macro would expand over all pythons flavors.
# TestPyzipPasswordfile is broken upstream (create_zip takes no password,
# fails with and without zip installed), so deselect it.
python3 -m pytest tests/ --deselect tests/archives/test_pyzipfile.py::TestPyzipPasswordfile::test_py_zipfile

%files
%license COPYING
%doc doc/*.txt
%{_bindir}/patool
%{python3_sitelib}/patoolib
%{python3_sitelib}/patool-%{version}*-info

%changelog
