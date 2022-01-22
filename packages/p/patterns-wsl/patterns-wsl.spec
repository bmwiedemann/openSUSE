#
# spec file for package patterns
#
# Copyright (c) 2022 SUSE LLC
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

Name:           patterns-wsl
Version:        20220112
Release:        0
Summary:        Recommended packages for Windows Subsystem for Linux, WSL, WSLg
License:        MIT
Group:          Metapackages
#URL:            https://github.com/openSUSE/patterns
URL:            https://github.com/sbradnick/patterns
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

# -----

%package base
%pattern_development
Summary:        Base WSL packages
Group:          Metapackages
Provides:       pattern() = wsl_base
Provides:       pattern-icon() = wsl
Provides:       pattern-order() = 3420
Provides:       pattern-visible()
Requires:       bash
Recommends:     fish
Recommends:     zsh

%description base
This package contains the wsl_base pattern: recommended tools,libraries for using WSL.

%files base
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_base.txt

# -----

%package gui
%pattern_development
Summary:        WSL GUI packages
Group:          Metapackages
Provides:       pattern() = wsl_gui
Provides:       pattern-icon() = wsl
Provides:       pattern-order() = 3420
Provides:       pattern-visible()
Requires:       xeyes
Recommends:     adwaita-icon-theme
Recommends:     gnome-icon-theme
Recommends:     noto-sans-fonts
Recommends:     powerline-fonts

%description gui
This package contains the wsl_gui pattern: recommended tools,libraries for using WSLg.

%files gui
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/wsl_gui.txt

# -----

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_base to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_base.txt
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern wsl_gui to be installed.' > %{buildroot}/usr/share/doc/packages/patterns/wsl_gui.txt

%changelog
