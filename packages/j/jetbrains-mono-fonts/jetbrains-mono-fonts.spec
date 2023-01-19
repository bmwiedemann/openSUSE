#
# spec file for package jetbrains-mono-fonts
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


%define         fontname JetBrainsMono
%global         fullversion %{version}

Name:           jetbrains-mono-fonts
Version:        2.304
Release:        0
Summary:        JetBrains Mono: a typeface for developers
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://www.jetbrains.com/lp/mono
Source:         https://github.com/JetBrains/JetBrainsMono/releases/download/v%{fullversion}/%{fontname}-%{fullversion}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A typeface made for developers.

Designer: Philipp Nurullin

%prep
# Usually empty, but insert fixes here, if necessary

%setup -cT
%{uncompress:%{S:0}}

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m0644 fonts/ttf/*.ttf %{buildroot}%{_ttfontsdir}

# call fonts-config after installation or deinstallation of this package
%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%{_ttfontsdir}

%changelog
