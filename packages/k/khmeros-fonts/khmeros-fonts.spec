#
# spec file for package khmeros-fonts
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


Name:           khmeros-fonts
Version:        5.0
Release:        0
Summary:        Fonts for the Khmer Language of Cambodia
License:        LGPL-2.1+
Group:          System/X11/Fonts
Url:            http://sourceforge.net/projects/khmer
Source0:        All_KhmerOS_5.0.tar.bz2
Source1:        LICENSE
Source2:        readme.txt
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-km
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      KhmerOS-fonts <= %{version}
Provides:       KhmerOS-fonts = %{version}
Provides:       locale(km)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains fonts for the Khmer language of Cambodia.

%prep
%setup -n All_KhmerOS_5.0
cp $RPM_SOURCE_DIR/LICENSE .
cp $RPM_SOURCE_DIR/readme.txt .

%build
mv "KhmerOS .ttf" KhmerOS.ttf

%install
mkdir -p %{buildroot}%{_ttfontsdir}
for i in *.ttf
do
    install -c -m 644 "$i" %{buildroot}%{_ttfontsdir}
done

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc LICENSE readme.txt
%{_ttfontsdir}

%changelog
