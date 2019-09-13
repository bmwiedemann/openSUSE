#
# spec file for package ipa-fonts
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


Name:           ipa-fonts
Version:        003.03
Release:        0
Summary:        Japanese TrueType Font Made by IPA
License:        IPA
Group:          System/X11/Fonts
Url:            http://ossipedia.ipa.go.jp/ipafont/
Source0:        IPAfont00303.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-ja
Provides:       locale(ja)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%package -n ipa-pgothic-fonts
Summary:        "Proportional Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       IPAPGothic = %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Obsoletes:      IPAPGothic <= 003.02

%description -n ipa-pgothic-fonts
"Proportional Gothic" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%package -n ipa-gothic-fonts
Summary:        "Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       IPAGothic = %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Obsoletes:      IPAGothic <= 003.02

%description -n ipa-gothic-fonts
"Gothic" Japanese TrueType font made by IPA (Information-technology
Promotion Agency).

%package -n ipa-mincho-fonts
Summary:        "Mincho" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       IPAMincho = %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Obsoletes:      IPAMincho <= 003.02

%description -n ipa-mincho-fonts
"Mincho" Japanese TrueType font made by IPA (Information-technology
Promotion Agency).

%package -n ipa-pmincho-fonts
Summary:        "Proportional Mincho" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       IPAPMincho = %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Obsoletes:      IPAPMincho <= 003.02

%description -n ipa-pmincho-fonts
"Proportional Mincho" Japanese TrueType font made by IPA
(Information-technology Promotion Agency).

%prep
%setup -q -n IPAfont00303

%build
for i in *.txt
do
    dos2unix $i
done

%install
mkdir -p %{buildroot}%{_ttfontsdir}
for i in *.ttf
do
    install -m 644 $i %{buildroot}%{_ttfontsdir}
done

%reconfigure_fonts_scriptlets -c -n ipa-pgothic-fonts

%reconfigure_fonts_scriptlets -c -n ipa-gothic-fonts

%reconfigure_fonts_scriptlets -c -n ipa-mincho-fonts

%reconfigure_fonts_scriptlets -c -n ipa-pmincho-fonts

%files -n ipa-pgothic-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/ipagp.*

%files -n ipa-gothic-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/ipag.*

%files -n ipa-mincho-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/ipam.*

%files -n ipa-pmincho-fonts
%defattr(-,root,root)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/ipamp.*

%changelog
