#
# spec file for package rovasiras-roga-fonts
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


Name:           rovasiras-roga-fonts
Version:        20230908
Release:        0
Summary:        A ligatureless variant of the Kende Old Hungarian font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/rovasiras/roga
#https://github.com/rovasiras/roga/blob/2f079df32f5176d0f8af0324f95892d5c78ebe37/Roga.ttf
Source0:        Roga.ttf
#https://github.com/rovasiras/roga/blob/2f079df32f5176d0f8af0324f95892d5c78ebe37/README.md
Source1:        README.md
#https://github.com/rovasiras/roga/blob/2f079df32f5176d0f8af0324f95892d5c78ebe37/LICENSE
Source2:        LICENSE
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Roga is the ligatureless version of the Kende font. Both are fonts
for the Old Hungarian script.

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} Roga.ttf

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%doc README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/Roga.ttf

%changelog
