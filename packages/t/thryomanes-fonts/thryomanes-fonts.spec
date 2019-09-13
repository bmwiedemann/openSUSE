#
# spec file for package thryomanes-fonts
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


Name:           thryomanes-fonts
Version:        1.2
Release:        0
Summary:        Greek TrueType Fonts
License:        GPL-2.0+
Group:          System/X11/Fonts
Url:            http://www.io.com/~hmiller/lang/
Source:         Thryomanes12.zip
Source1:        copyright
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Provides:       scalable-font-bg
Provides:       scalable-font-el
Provides:       scalable-font-ru
Provides:       locale(bg;el;ru)
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      fonts-thryomanes <= %{version}
Provides:       fonts-thryomanes = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
These fonts include a complete set of Cyrillic letters and improved
italic characters.

%prep
unzip $RPM_SOURCE_DIR/Thryomanes12.zip

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.TTF %{buildroot}%{_ttfontsdir}
mkdir -p %{buildroot}/%{_defaultdocdir}/fonts-thryomanes
install -m 644 gpl.txt \
  %{buildroot}/%{_defaultdocdir}/fonts-thryomanes
install -m 644 $RPM_SOURCE_DIR/copyright \
  %{buildroot}/%{_defaultdocdir}/fonts-thryomanes

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc %{_defaultdocdir}/*
%{_ttfontsdir}

%changelog
