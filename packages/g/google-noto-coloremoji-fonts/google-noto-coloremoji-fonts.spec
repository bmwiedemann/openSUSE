#
# spec file for package google-noto-coloremoji-fonts
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


Name:           google-noto-coloremoji-fonts
Version:        20230315
Release:        0
Summary:        Noto Color Emoji font
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/googlefonts/noto-emoji
Source0:        https://github.com/googlefonts/noto-emoji/raw/v2.038/fonts/LICENSE
Source1:        https://github.com/googlefonts/noto-emoji/raw/v2.038/fonts/NotoColorEmoji.ttf
BuildRequires:  fontpackages-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       noto-emoji-fonts = %version
Obsoletes:      noto-emoji-fonts < %version
Obsoletes:      noto-coloremoji-fonts < 20211101
Provides:       noto-coloremoji-fonts = %{version}

%description
Noto Color Emoji font

%prep
cp %{S:0} .

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} %{S:1}

%reconfigure_fonts_scriptlets

%files
%defattr(0644,root,root,755)
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/NotoColorEmoji.ttf

%changelog
