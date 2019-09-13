#
# spec file for package cyreal-lora-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           cyreal-lora-fonts
Version:        1.014
Release:        0
Summary:        Lora Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://cyreal.org/archives/803
#Source0:       wget http://www.google.com/webfonts/download?kit=iwrHM7FQEcKgsUvDuXxrPg -O cyreal-lora-fonts.zip
Source0:        cyreal-lora-fonts.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Lora is a well-balanced contemporary serif with roots in calligraphy. It
is a text typeface with moderate contrast well suited for body text.

A paragraph set in Lora will make a memorable appearance because of its
brushed curves in contrast with driving serifs. The overall typographic
voice of Lora perfectly conveys the mood of a modern-day story, or an
art essay.
Technically Lora is optimised for screen appearance, and works equally
well in print.

%prep
%setup -cqn %{name}-%{version}
sed -i 's/\r$//g' OFL.txt

%build

%install
install -dm 0755 %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
