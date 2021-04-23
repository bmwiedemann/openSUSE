#
# spec file for package thessalonica-oldstandard-fonts
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


Name:           thessalonica-oldstandard-fonts
Version:        2.2
Release:        0
Summary:        Old Standard Font Family
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://thessalonica.org.ru/en/oldstandard.html
Source0:        http://thessalonica.org.ru/downloads/oldstandard-%{version}.otf.zip
Source1:        http://thessalonica.org.ru/downloads/oldstandard-%{version}.ttf.zip
Source2:        http://thessalonica.org.ru/downloads/oldstand-manual.pdf
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Old Standard was intended as a multilingual font family suitable for
biblical, classical and medieval studies as well as for general-purpose
typesetting in languages which use Greek or Cyrillic script. The font is
currently available in three shapes: regular, italic and bold. Old
Standard is still far from being finished, and yet it already covers
a wide range of Latin, Greek and Cyrillic characters. It also supports
early Cyrillic letters and signs (including those added in Unicode 5.1)
and thus can be used for texts containing fragments in Old Slavonic and
Church Slavonic languages.

%package -n thessalonica-oldstandard-otf-fonts
Summary:        Old Standard Font Family (OpenType Format)
Group:          System/X11/Fonts
Provides:       oldstandard-fonts-otf = %{version}
Provides:       locale(el;ru)
# FIXME: This causes a rpmlint warning; change "<=" to "<" once there's
# a new upstream version.
Obsoletes:      oldstandard-fonts-otf <= 2.2

%description -n thessalonica-oldstandard-otf-fonts
Old Standard was intended as a multilingual font family suitable for
biblical, classical and medieval studies as well as for general-purpose
typesetting in languages which use Greek or Cyrillic script. The font is
currently available in three shapes: regular, italic and bold. Old
Standard is still far from being finished, and yet it already covers
a wide range of Latin, Greek and Cyrillic characters. It also supports
early Cyrillic letters and signs (including those added in Unicode 5.1)
and thus can be used for texts containing fragments in Old Slavonic and
Church Slavonic languages.

This package contains fonts in OpenType format.

%package -n thessalonica-oldstandard-ttf-fonts
Summary:        Old Standard Font Family (TrueType Format)
Group:          System/X11/Fonts
Provides:       oldstandard-fonts-ttf = %{version}
# FIXME: This causes a rpmlint warning; change "<=" to "<" once there's
# a new upstream version.
Obsoletes:      oldstandard-fonts-ttf <= 2.2

%description -n thessalonica-oldstandard-ttf-fonts
Old Standard was intended as a multilingual font family suitable for
biblical, classical and medieval studies as well as for general-purpose
typesetting in languages which use Greek or Cyrillic script. The font is
currently available in three shapes: regular, italic and bold. Old
Standard is still far from being finished, and yet it already covers
a wide range of Latin, Greek and Cyrillic characters. It also supports
early Cyrillic letters and signs (including those added in Unicode 5.1)
and thus can be used for texts containing fragments in Old Slavonic and
Church Slavonic languages.

This package contains fonts in TrueType format.

%prep
%setup -cqn %{name}-%{version}
unzip -oq %{SOURCE1}
cp %{SOURCE2} .
sed -i 's/\r$//g' OFL-FAQ.txt

%build

%install
install -dm 0755 %{buildroot}%{_ttfontsdir}
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -n thessalonica-oldstandard-otf-fonts

%reconfigure_fonts_scriptlets -n thessalonica-oldstandard-ttf-fonts

%files -n thessalonica-oldstandard-otf-fonts
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt oldstand-manual.pdf
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%files -n thessalonica-oldstandard-ttf-fonts
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt oldstand-manual.pdf
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
