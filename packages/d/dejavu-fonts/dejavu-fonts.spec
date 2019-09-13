#
# spec file for package dejavu-fonts
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


Name:           dejavu-fonts
Version:        2.37
Release:        0
Summary:        DejaVu Truetype Fonts
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://dejavu.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/dejavu/dejavu/%{version}/%{name}-ttf-%{version}.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       desktop-data-SuSE:/usr/X11R6/lib/X11/fonts/truetype/SUSESans-Roman.ttf
Provides:       locale(bg;el;mk;ru;vi)
Obsoletes:      dejavu < 2.34
Provides:       dejavu = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The DejaVu fonts are a font family based on the Bitstream Vera Fonts.
Its purpose is to provide a wider range of characters while maintaining
the original look and feel through the process of collaborative
development.

%prep
%setup -n %{name}-ttf-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 ttf/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,755)
%doc AUTHORS BUGS LICENSE NEWS README.md *.txt fontconfig
%{_ttfontsdir}/

%changelog
