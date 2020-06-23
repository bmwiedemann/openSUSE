#
# spec file for package ttf-converter
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


Name:           ttf-converter
Version:        1.0.3
Release:        0
Summary:        Python script that converts fonts to TrueType format
License:        GPL-3.0-only
URL:            https://github.com/antlarr-suse/ttf-converter
Source:         ttf-converter-%{version}.tar.xz
BuildRequires:  python3
Requires:       fontforge
Requires:       python3-base
BuildArch:      noarch

%description
A Python script that converts fonts to TrueType format. It uses
the fontforge python bindings to read/process and write any font
format. Also, as part of the conversion process, the script
tries to fix inconsistencies and do necessary changes to the font
to honor the TTF format specs.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp ttf-converter %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/ttf-converter

%changelog
