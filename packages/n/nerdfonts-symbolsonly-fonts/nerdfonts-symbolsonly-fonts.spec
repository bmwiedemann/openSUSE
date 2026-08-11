#
# spec file for package nerdfonts-symbolsonly-fonts
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           nerdfonts-symbolsonly-fonts
Version:        3.5.0
Release:        0
Summary:        The Nerd Fonts symbol set, without base (letter) glyphs
License:        Apache-2.0 AND CC-BY-4.0 AND MIT AND OFL-1.1-no-RFN AND LicenseRef-SUSE-Freeware
Group:          System/X11/Fonts
URL:            https://github.com/ryanoasis/nerd-fonts
Source:         https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/NerdFontsSymbolsOnly.tar.xz
Source10:       https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%{version}/license-audit.md
Source11:       README.md
Source12:       LICENSE
BuildRequires:  fontpackages-devel
BuildArch:      noarch
Obsoletes:      symbols-only-nerd-fonts < %{version}-%{release}
Provides:       symbols-only-nerd-fonts = %{version}-%{release}
%reconfigure_fonts_prereq

%description
Nerd Fonts takes popular programming fonts and adds a fair number of
dingbat glyphs (symbols, ornamentations, etc.)
This package contains a font with dingbats only, and without any
letter glyphs (e.g. Latin).

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
