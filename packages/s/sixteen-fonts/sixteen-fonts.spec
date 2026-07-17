#
# spec file for package sixteen-fonts
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

Name:           sixteen-fonts
Version:        1.0
Release:        0
Summary:        A font inspired by 16-segment LED displays
URL:            https://stuffjackmakes.com/sixteen-font
License:        OFL-1.1
Source:         sixteen.zip
Source2:        sixteen-fonts.metainfo.xml
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Sixteen is a monospaced font inspired by the aesthetics of 16-segment LED 
displays, suitable for technical and decorative use.

%prep
%setup -q -c

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m 644 otf/*.otf ttf/*.ttf %{buildroot}%{_ttfontsdir} || :
install -d -m0755  %{buildroot}%{_datadir}/appdata

install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc Sixteen-LICENSE.txt README.md
%dir %{_datadir}/appdata
%{_datadir}/appdata/sixteen-fonts.metainfo.xml
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
