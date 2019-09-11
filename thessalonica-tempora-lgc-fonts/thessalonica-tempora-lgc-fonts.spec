#
# spec file for package thessalonica-tempora-lgc-fonts
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


Name:           thessalonica-tempora-lgc-fonts
Version:        0.2.1
Release:        0
Summary:        Tempora LGC Unicode Fonts
License:        GPL-2.0-with-font-exception
Group:          System/X11/Fonts
Url:            http://thessalonica.org.ru/en/fonts.html
Source0:        http://www.thessalonica.org.ru/downloads/tempora-lgc.otf.zip
Source1:        http://www.thessalonica.org.ru/downloads/tempora-lgc.ttf.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Tempora LGC Unicode is a font family, designed to provide a free
typeface suitable for word processing in languages which use 3 European
alphabets: Latin, Greek and Cyrillic. It may be especially useful for
philologists (mainly slavists and classicists), since it supports
historical Cyrillic letters available in the Unicode standard (including
letters used in Russian  pre-1918 orthography) as well as all accented
combinations and additional characters needed for fully accented Greek
(both classical and modern). Tempora LGC Unicode is a "smart" font,
intended to demonstrate nicities of the OpenType technologie, applicable
to European scripts.

%package -n thessalonica-tempora-lgc-otf-fonts
Summary:        Tempora LGC Unicode Fonts (OpenType Format)
Group:          System/X11/Fonts
Provides:       tempora-lgc-fonts-otf = %{version}
# FIXME: This causes a rpmlint warning; change "<=" to "<" once there's
# a new upstream version.
Obsoletes:      tempora-lgc-fonts-otf <= 0.2.1

%description -n thessalonica-tempora-lgc-otf-fonts
Tempora LGC Unicode is a font family, designed to provide a free
typeface suitable for word processing in languages which use 3 European
alphabets: Latin, Greek and Cyrillic. It may be especially useful for
philologists (mainly slavists and classicists), since it supports
historical Cyrillic letters available in the Unicode standard (including
letters used in Russian  pre-1918 orthography) as well as all accented
combinations and additional characters needed for fully accented Greek
(both classical and modern). Tempora LGC Unicode is a "smart" font,
intended to demonstrate nicities of the OpenType technologie, applicable
to European scripts.

This package contains fonts in OpenType format.

%package -n thessalonica-tempora-lgc-ttf-fonts
Summary:        Tempora LGC Unicode Fonts (TrueType Format)
Group:          System/X11/Fonts
Provides:       tempora-lgc-fonts-ttf = %{version}
# FIXME: This causes a rpmlint warning; change "<=" to "<" once there's
# a new upstream version.
Obsoletes:      tempora-lgc-fonts-ttf <= 0.2.1

%description -n thessalonica-tempora-lgc-ttf-fonts
Tempora LGC Unicode is a font family, designed to provide a free
typeface suitable for word processing in languages which use 3 European
alphabets: Latin, Greek and Cyrillic. It may be especially useful for
philologists (mainly slavists and classicists), since it supports
historical Cyrillic letters available in the Unicode standard (including
letters used in Russian  pre-1918 orthography) as well as all accented
combinations and additional characters needed for fully accented Greek
(both classical and modern). Tempora LGC Unicode is a "smart" font,
intended to demonstrate nicities of the OpenType technologie, applicable
to European scripts.

This package contains fonts in TrueType format.

%prep
%setup -cqn %{name}-%{version}
unzip -oq %{SOURCE1}

%build

%install
install -dm 0755 %{buildroot}%{_ttfontsdir}
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -n thessalonica-tempora-lgc-otf-fonts

%reconfigure_fonts_scriptlets -n thessalonica-tempora-lgc-ttf-fonts

%files -n thessalonica-tempora-lgc-otf-fonts
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%files -n thessalonica-tempora-lgc-ttf-fonts
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
