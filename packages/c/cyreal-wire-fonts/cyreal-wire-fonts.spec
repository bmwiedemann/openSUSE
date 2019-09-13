#
# spec file for package cyreal-wire-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           cyreal-wire-fonts
Version:        1.000
Release:        0
License:        OFL-1.1
Summary:        Wire Font
Url:            http://cyreal.org/archives/826
Group:          System/X11/Fonts
#Source0:       wget http://www.google.com/webfonts/download?kit=pjHAkeosJEZ1STUyWV7nsS3USBnSvpkopQaUR-2r7iU -O cyreal-wire-fonts.zip
Source0:        cyreal-wire-fonts.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Wire is a condensed monoline sans. Its modular-based characters are
flavored with a sense of art nouveau. Nearly hairline thickness suggests
usage for body text above 12px. While at display sizes it reveals its
tiny dot terminals to create a sharp mood in headlines.

For web typesetting it is recommended to adjust letter-spacing for sizes
below 30px to 0.033em and up. For 12 px we recommend the value of
0.085em.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' OFL.txt

%build

%install
install -Dm 644 WireOne.ttf \
    %{buildroot}%{_ttfontsdir}/WireOne.ttf

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/WireOne.ttf

%changelog
