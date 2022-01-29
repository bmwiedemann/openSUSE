#
# spec file for package google-droid-fonts
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


%define fontname droid-fonts

Name:           google-droid-fonts
Version:        20121204
Release:        0
Summary:        Fonts With Extensive Style and Language Support Developed for Android
License:        Apache-2.0
Group:          System/X11/Fonts
URL:            http://www.ascendercorp.com/pr/2007-11-12/
Source:         %{fontname}-%{version}.tar.bz2
Source1:        https://github.com/aosp-mirror/platform_frameworks_base/raw/master/data/fonts/DroidSansFallbackFull.ttf
Source2:        https://github.com/aosp-mirror/platform_frameworks_base/raw/master/data/fonts/DroidSansMono.ttf
Source3:        https://github.com/aosp-mirror/platform_frameworks_base/raw/master/data/fonts/DroidSansFallback.ttf
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
# FIXME: This causes a rpmlint warning; change <= to < once there's a new upstream version
Obsoletes:      %{fontname} <= 1.0
Provides:       %{fontname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Droid family of fonts consists of Droid Sans, Droid Sans Mono and
Droid Serif. Each contains extensive character set coverage including
Western Europe, Eastern/Central Europe, Baltic, Cyrillic, Greek and
Turkish support. The Droid Sans regular font also includes support for
Simplified and Traditional Chinese, Japanese and Korean support for the
GB2312, Big 5, JIS 0208 and KSC 5601 character sets respectively. Droid
was designed by Ascender's Steve Matteson to provide optimal quality
and comfort on a mobile handset when rendered in application menus, web
browsers and for other screen text. - Ascender Press Release,
http://www.ascendercorp.com/pr/2007-11-12/

%prep
%setup -q -n %{fontname}-%{version}

%build
rm DroidSansFallbackFull.ttf
rm DroidSansMono.ttf
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README.txt NOTICE
%{_ttfontsdir}

%changelog
