#
# spec file for package last-resort-font
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


Name:           last-resort-font
Version:        13.000
Release:        0
Summary:        A special-purpose font that includes a collection of glyphs to represent types of Unicode characters
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/unicode-org/last-resort-font
Source0:        https://github.com/unicode-org/last-resort-font/releases/download/%{version}/LastResort-Regular.ttf
Source1:        https://raw.githubusercontent.com/unicode-org/last-resort-font/main/LICENSE.md
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Last Resort is a special-purpose font that includes a collection of glyphs to represent types of Unicode characters.
These glyphs are specifically designed to allow users to recognize that a code point is one of the following:

* A specific type of Unicode character
* In the PUA (Private Use Area) for which no agreement exists
* Unassigned (reserved for future assignment)
* A noncharacter

%prep
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 %{SOURCE0} %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license LICENSE.md
%{_ttfontsdir}

%changelog
