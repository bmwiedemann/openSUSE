#
# spec file for package lklug-fonts
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


%define fontname        ttf-sinhala-lklug

Name:           lklug-fonts
Version:        0.6
Release:        0
Summary:        "Lanka Linux User Group" OpenType Font for Sinhala
License:        GPL-2.0
Group:          System/X11/Fonts
Url:            http://www.lug.lk
# The font file in TrueType format can be downloaed at:
# http://sinhala.sourceforge.net/files
# CVS, which contains the SFD sources:
# cvs -d:pserver:anonymous@sinhala.cvs.sourceforge.net:/cvsroot/sinhala login
# cvs -d:pserver:anonymous@sinhala.cvs.sourceforge.net:/cvsroot/sinhala co sinhala/fonts
# GPL Copyright file is here:
# cvs -d:pserver:anonymous@sinhala.cvs.sourceforge.net:/cvsroot/sinhala co sinhala/COPYING
Source0:        %{fontname}-%{version}.tar.gz
Source1:        README.SUSE
BuildRequires:  fontpackages-devel
Provides:       scalable-font-si
Provides:       locale(si)
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      lklug <= %{version}
Provides:       lklug = %{version}
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
"Lanka Linux User Group" OpenType font for Sinhala copyright 2004 by
Yannis Haralambous.  OTF tables added by Anuradha Ratnaweera an d
Harshani Devadithya, and modified by Harshula Jayasuriya. "Kunddaliya"
glyph Copyright (c) 2006 Harshula Jayasuriya

%prep
%setup -n %{fontname}-%{version}

%build
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%clean

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc COPYING README.SUSE CREDITS
%{_ttfontsdir}

%changelog
