#
# spec file for package morse2ascii
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           morse2ascii
Version:        1.2.1
Release:        0
Summary:        Decode morse code from PCM WAV files
License:        GPL-2.0-or-later
URL:            https://aluigi.altervista.org/mytoolz.htm#morse2ascii
Source:         https://aluigi.altervista.org/mytoolz/%{name}.zip
Source2:        http://www.gnu.org/licenses/gpl-2.0.txt
BuildRequires:  unzip

%description
Experimental tool for decoding the morse codes from a PCM WAV file using a
volume/peak based method. The tool can also decode the morse codes from text
and RAW PCM files. It contains some options for parsing abbreviations, prosigns
and qcodes.

%prep
%autosetup -p1 -c
cp %{SOURCE2} .

%build
%make_build

%install
%make_install \
	PREFIX=%{buildroot}/%{_prefix} \
	%{nil}

%files
%license gpl-2.0.txt
%{_bindir}/morse2ascii

%changelog
