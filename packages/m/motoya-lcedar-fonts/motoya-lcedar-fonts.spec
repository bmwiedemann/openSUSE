#
# spec file for package motoya-lcedar-fonts
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


Name:           motoya-lcedar-fonts
Version:        1.0.0
Release:        0
Summary:        Japanese gothic-typeface fonts designed by Motoya
License:        Apache-2.0
Group:          System/X11/Fonts
Url:            http://android.googlesource.com/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides a font family named "MotoyaLCedar W3 mono".
It was provided to Android platform by Motoya.

%prep
%setup -q

%build

%install
mkdir -p  %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc NOTICE
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%changelog
