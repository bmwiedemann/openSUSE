#
# spec file for package farsi-fonts
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


Name:           farsi-fonts
Version:        0.4
Release:        0
Summary:        A Collection of Free Persian OpenType Fonts
License:        GPL-2.0+
Group:          System/X11/Fonts
Url:            http://www.farsiweb.info/wiki/Products/PersianFonts
Source0:        http://www.farsiweb.info/font/farsifonts-0.4.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Provides:       scalable-font-fa
Provides:       locale(fa)
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      farsifonts <= %{version}
Provides:       farsifonts = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains collection of free Persian OpenType fonts.

%prep
%setup -T -c %{name} -n %{name}
unzip $RPM_SOURCE_DIR/farsifonts-%{version}
chmod -R a+r *

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
for i in */*.ttf
do
    install -c -m 644 $i %{buildroot}%{_ttfontsdir}
done

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc farsifonts*/COPYING
%doc farsifonts*/NEWS
%{_ttfontsdir}

%changelog
