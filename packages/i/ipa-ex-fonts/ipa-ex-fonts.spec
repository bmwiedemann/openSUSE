#
# spec file for package ipa-ex-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ipa-ex-fonts
Version:        004.01
Release:        0
Summary:        Scalable Japanese TrueType Fonts Made by IPA
License:        IPA
Group:          System/X11/Fonts
Url:            https://ipafont.ipa.go.jp/
Source0:        IPAexfont00401.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Japanese TrueType fonts made by IPA (Information-technology Promotion Agency).

%package -n ipa-ex-gothic-fonts
Summary:        Scalable "Gothic" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       scalable-font-ja
Provides:       locale(ja)
%reconfigure_fonts_prereq

%description -n ipa-ex-gothic-fonts
"Gothic" Japanese TrueType font made by IPA (Information-technology Promotion Agency).

%package -n ipa-ex-mincho-fonts
Summary:        Scalable "Mincho" Japanese TrueType Font Made by IPA
Group:          System/X11/Fonts
Provides:       scalable-font-ja
Provides:       locale(ja)
%reconfigure_fonts_prereq

%description -n ipa-ex-mincho-fonts
"Mincho" Japanese TrueType font made by IPA (Information-technology Promotion Agency).

%prep
%setup -q -n IPAexfont00401

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

%reconfigure_fonts_scriptlets -c -n ipa-ex-gothic-fonts

%reconfigure_fonts_scriptlets -c -n ipa-ex-mincho-fonts

%files -n ipa-ex-gothic-fonts
%defattr(644,root,root)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/ipaexg.*

%files -n ipa-ex-mincho-fonts
%defattr(644,root,root)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/ipaexm.*

%changelog
