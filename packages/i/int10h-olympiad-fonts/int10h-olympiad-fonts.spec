#
# spec file for package int10h-olympiad-fonts
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


Name:           int10h-olympiad-fonts
Version:        1.0
Release:        0
Summary:        Remakes of IBM 6150 prototype fonts
License:        CC-BY-SA-4.0
Group:          System/X11/Fonts
URL:            https://int10h.org/blog/2016/03/olympiad-ibm-prototype-fonts-unearthed/

Source:         http://int10h.org/filez/Olympiad_Fonts_v1.0.zip
BuildRequires:  fontpackages-devel
BuildRequires:  lcdf-typetools
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildArch:      noarch

%description
This fontpack contains remakes of prototype fonts designed for a
project codenamed Olympiad, which later became the IBM 6150, a.k.a.
the RT PC, a RISC workstation and grandaddy of the PowerPC
architecture.

%prep
%setup -Tcqa0

%build

%install
tt="%buildroot/%_ttfontsdir"
mkdir -p "$tt"
cp -av *.ttf "$tt/"

%reconfigure_fonts_scriptlets

%files
%license LICENSE.TXT
%doc README.TXT
%_ttfontsdir/

%changelog
