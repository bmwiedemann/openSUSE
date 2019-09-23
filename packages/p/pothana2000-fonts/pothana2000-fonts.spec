#
# spec file for package pothana2000-fonts
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


%define fontname pothana2000

Name:           pothana2000-fonts
Version:        1.1
Release:        0
Summary:        OpenType Font for Telugu
License:        GPL-2.0+
Group:          System/X11/Fonts
Url:            http://www.kavya-nandanam.com/
# http://www.kavya-nandanam.com/Pothana2k.zip
# removed Pathana2k.exe from the sources and repackaged to .tar.bz2
Source0:        pothana2000.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
Provides:       scalable-font-te
Provides:       locale(te)
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      pothana2000 <= %{version}
Provides:       pothana2000 = %{version}
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Free OpenType font for Telugu created by Dr. Tirumala Krishna
Desikacharyulu

%prep
%setup -q -n %{fontname}

%build
dos2unix gpl.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc MANUAL.PDF gpl.txt Telugu2006.kmx
%{_ttfontsdir}

%changelog
