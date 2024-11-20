#
# spec file for package symbols-only-nerd-fonts
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


Name:           symbols-only-nerd-fonts
Version:        3.3.0
Release:        0
Summary:        A glyphs-only version of Nerd Fonts
License:        Apache-2.0 AND CC-BY-4.0 AND MIT AND OFL-1.1-no-RFN AND SUSE-Freeware
Group:          System/X11/Fonts
URL:            https://github.com/ryanoasis/nerd-fonts
Source:         %{url}/releases/download/v%{version}/NerdFontsSymbolsOnly.tar.xz#/%{name}-%{version}.tar.xz
Source10:       https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%{version}/license-audit.md
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Nerd Fonts takes popular programming fonts and adds a bunch of glyphs.
This package only contains the symbols without including a base font.

%prep
%autosetup -c

%build

%check

%install
install -d %{buildroot}%{_ttfontsdir} %{buildroot}%{_docdir}/%{name} %{buildroot}%{_licensedir}/%{name}
install -m644 *.ttf %{buildroot}%{_ttfontsdir}
install -m644 -t %{buildroot}%{_docdir}/%{name} README.md %{SOURCE10}
install -m644 LICENSE %{buildroot}%{_licensedir}/%{name}

%reconfigure_fonts_scriptlets

%files
%doc README.md license-audit.md
%license LICENSE
%{_ttfontsdir}

%changelog
