#
# spec file for package autonym-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           autonym-fonts
Version:        1.0
Release:        0
Summary:        A font that can render all language autonyms
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            https://github.com/santhoshtr/AutonymFont
Source:         AutonymFont_1.0.tar.gz
%if 0%{?sles_version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
BuildRequires:  fontpackages-devel
BuildRequires:  gzip
BuildArch:      noarch

%description
If we want to show a large number of languages written in their own scripts
(autonyms), we cannot apply the usual webfonts to it. This is because since
each script require a webfonts, we will end up in using a large number of
webfonts. This can cause large bandwidth usage.

Autonym font tries to solve this. The font contains glyphs and opentype rules
for rendering the language autonyms. And it contains only those glyphs for a
language. For example, for Thai, the font has glyphs required for rendering ไทย 
alone.

%prep
%setup -c

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.{ttf,woff,eot} %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc COPYING CREDITS README.md

%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
