#
# spec file for package google-roboto-fonts
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


Name:           google-roboto-fonts
Version:        2.138
Release:        0
Summary:        Neo-grotesque sans-serif typeface family from Google
License:        Apache-2.0
Group:          System/X11/Fonts
URL:            https://material.google.com/style/typography.html
Source0:        https://github.com/google/roboto/releases/download/v%{version}/roboto-android.zip
Source1:        https://raw.githubusercontent.com/googlefonts/roboto/master/LICENSE
Source2:        google-roboto.metainfo.xml
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Roboto is Google’s signature family of fonts, the default font on Android and
Chrome OS, and the recommended font for Google’s visual language, Material Design.

The font family supports all Latin, Cyrillic, and Greek characters in Unicode 7.0,
as well as the currency symbol for the Georgian lari, to be published in Unicode 8.0.

The fonts are currently available in eighteen different styles.

%prep
unzip -j -o %{SOURCE0}
cp %{SOURCE1} .
chmod 0644 LICENSE

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

# install metainfo
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/metainfo

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%{_datadir}/metainfo/google-roboto.metainfo.xml
%{_ttfontsdir}

%changelog
