#
# spec file for package rmit-sansforgetica-fonts
#
# Copyright (c) 2019 SUSE Linux GmbH, Nuernberg, Germany.
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


Name:           rmit-sansforgetica-fonts
Version:        1.000
Release:        0
Summary:        Sans Forgetica Font
License:        CC-BY-NC-4.0
Group:          System/X11/Fonts
Url:		https://sansforgetica.rmit/
Source0:        rmit-sansforgetica-fonts.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch

%description
Sans Forgetica is more difficult to read than most typefaces – and that's by design.
The 'desirable difficulty' you experience whee reading information formatted in
Sans Forgetica prompts your brain to engage in deeper processing. Sans Forgetica is
designed for non-commercial use only. It is bound by a creative commons, non-commercial,
attributed (CCBYNC) license.

%prep
%setup -q -n "Sans Forgetica"

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc "The story of Sans Forgetica.pdf"
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
