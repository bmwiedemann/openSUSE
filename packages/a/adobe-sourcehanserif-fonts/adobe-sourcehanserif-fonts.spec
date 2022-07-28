#
# spec file for package adobe-sourcehanserif-fonts
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define shared_description Source Han Serif is an open source Pan-CJK typeface whose OpenType/CFF fonts and CID-based sources are covered under the terms of the SIL Open Font License, Version 1.1.

Name:           adobe-sourcehanserif-fonts
Version:        2.001
Release:        0
Summary:        Source Han Serif fonts
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe-fonts/source-han-serif
Source0:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifCN.zip
Source1:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifHK.zip
Source2:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifJP.zip
Source3:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifKR.zip
Source4:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/SubsetOTF/SourceHanSerifTW.zip
Source5:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifCN-VF.otf
Source6:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifHK-VF.otf
Source7:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifJP-VF.otf
Source8:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifKR-VF.otf
Source9:        https://github.com/adobe-fonts/source-han-serif/raw/%{version}R/Variable/OTF/Subset/SourceHanSerifTW-VF.otf
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
%{shared_description}

%prep
unzip -o %{S:0}
unzip -o %{S:1}
unzip -o %{S:2}
unzip -o %{S:3}
unzip -o %{S:4}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
mv *.otf %{buildroot}%{_ttfontsdir}
cp -t %{buildroot}%{_ttfontsdir} %{S:5} %{S:6} %{S:7} %{S:8} %{S:9} 

# Chinese China package
%package -n adobe-sourcehanserif-cn-fonts
Summary:        Source Han Serif CN
Group:          System/X11/Fonts
Provides:       scalable-font-zh_CN
Provides:       locale(zh_CN)

%description -n adobe-sourcehanserif-cn-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-cn-fonts
%files -n adobe-sourcehanserif-cn-fonts
%defattr(0644,root,root,755)
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifCN-*.otf

# Chinese Hongkong package
%package -n adobe-sourcehanserif-hk-fonts
Summary:        Source Han Serif HK
Group:          System/X11/Fonts
Provides:       scalable-font-zh_HK
Provides:       locale(zh_HK)

%description -n adobe-sourcehanserif-hk-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-hk-fonts
%files -n adobe-sourcehanserif-hk-fonts
%defattr(0644,root,root,755)
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifHK-*.otf

# Japanese package
%package -n adobe-sourcehanserif-jp-fonts
Summary:        Source Han Serif JP
Group:          System/X11/Fonts
Provides:       scalable-font-jp
Provides:       locale(jp)

%description -n adobe-sourcehanserif-jp-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-jp-fonts
%files -n adobe-sourcehanserif-jp-fonts
%defattr(0644,root,root,755)
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifJP-*.otf

# Korean package
%package -n adobe-sourcehanserif-kr-fonts
Summary:        Source Han Serif KR
Group:          System/X11/Fonts
Provides:       scalable-font-kr
Provides:       locale(kr)

%description -n adobe-sourcehanserif-kr-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-kr-fonts
%files -n adobe-sourcehanserif-kr-fonts
%defattr(0644,root,root,755)
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifKR-*.otf

# Chinese Taiwan package
%package -n adobe-sourcehanserif-tw-fonts
Summary:        Source Han Serif TW
# Replace the old single package that only provides Taiwan fonts
Group:          System/X11/Fonts
Provides:       scalable-font-zh_TW
Provides:       locale(zh_TW)
Provides:       adobe-sourcehanserif-fonts = %version
Obsoletes:      adobe-sourcehanserif-fonts < %version

%description -n adobe-sourcehanserif-tw-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehanserif-tw-fonts
%files -n adobe-sourcehanserif-tw-fonts
%defattr(0644,root,root,755)
%license LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifTW-*.otf

%changelog
