#
# spec file for package ttf-converter
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


%if 0%{suse_version} < 1550
%define primary_python python3
%endif
Name:           ttf-converter
Version:        1.0.7
Release:        0
Summary:        Python script that converts fonts to TrueType format
License:        GPL-3.0-only
URL:            https://github.com/antlarr-suse/ttf-converter
Source:         ttf-converter-%{version}.tar.xz
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}-base
Requires:       fontforge
Requires:       ftdump
BuildArch:      noarch

%description
This is a Python script that converts fonts to TrueType/OpenType
format. It uses the FontForge Python bindings to read/process and
write any font format. Also, as part of the conversion process, the
script tries to fix inconsistencies and do necessary changes to the
font to honor the TTF/OTF format specs.

Though TrueType is often used synonymously with outline fonts, it
supports embedded bitmaps. ttf-converter leaves the glyph kind
(outline/bitmapped) unchanged.

For converting a font to have scalable outline glyphs, see vfontas
instead.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
install ttf-converter %{buildroot}%{_bindir}
%python3_fix_shebang

%files
%license LICENSE
%doc README.md
%{_bindir}/ttf-converter

%changelog
