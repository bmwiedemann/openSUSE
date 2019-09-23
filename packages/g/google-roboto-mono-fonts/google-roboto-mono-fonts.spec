#
# spec file for package google-roboto-mono-fonts
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           google-roboto-mono-fonts
Version:        20160111
Release:        0
Summary:        Google Roboto Mono fonts
License:        Apache-2.0
Group:          System/X11/Fonts
Url:            https://www.google.com/fonts/specimen/Roboto+Mono
Source0:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-Regular.ttf
Source1:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-Bold.ttf
Source2:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-Italic.ttf
Source3:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-BoldItalic.ttf
Source4:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-Medium.ttf
Source5:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-MediumItalic.ttf
Source6:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-Light.ttf
Source7:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-LightItalic.ttf
Source8:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-Thin.ttf
Source9:        https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/RobotoMono-ThinItalic.ttf
Source10:       https://raw.githubusercontent.com/google/fonts/master/apache/robotomono/LICENSE.txt
BuildRequires:  fontpackages-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Roboto Mono is a monospaced addition to the Roboto type family. Like the
other members of the Roboto family, the fonts are optimized for readability
on screens across a wide variety of devices and reading environments. While
the monospaced version is related to its variable width cousin, it doesn't
hesitate to change forms to better fit the constraints of a monospaced
environment. For example, narrow glyphs like 'I', 'l' and 'i' have added
serifs for more even texture while wider glyphs are adjusted for weight.
Curved caps like 'C' and 'O' take on the straighter sides from Roboto
Condensed.

%prep
cp -p \
    %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
    %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} .

%build
# Nothing to build here

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc LICENSE.txt
%{_ttfontsdir}

%changelog
