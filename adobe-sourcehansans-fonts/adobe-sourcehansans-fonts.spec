#
# spec file for package adobe-sourcehansans-fonts
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define shared_description Source Han Sans is an open source Pan-CJK typeface whose OpenType/CFF fonts and CID-based sources are covered under the terms of the SIL Open Font License.

Name:           adobe-sourcehansans-fonts
Version:        2.001
Release:        0
Summary:        Source Han Sans
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe-fonts/source-han-sans
Source0:        https://raw.githubusercontent.com/adobe-fonts/source-han-sans/%{version}R/SubsetOTF/SourceHanSansCN.zip
Source1:        https://raw.githubusercontent.com/adobe-fonts/source-han-sans/%{version}R/SubsetOTF/SourceHanSansHK.zip
Source2:        https://raw.githubusercontent.com/adobe-fonts/source-han-sans/%{version}R/SubsetOTF/SourceHanSansJP.zip
Source3:        https://raw.githubusercontent.com/adobe-fonts/source-han-sans/%{version}R/SubsetOTF/SourceHanSansKR.zip
Source4:        https://raw.githubusercontent.com/adobe-fonts/source-han-sans/%{version}R/SubsetOTF/SourceHanSansTW.zip
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
mv */*.otf %{buildroot}%{_ttfontsdir}

# Chinese China package
%package -n adobe-sourcehansans-cn-fonts
Summary:        Source Han Sans CN
Group:          System/X11/Fonts
Provides:       scalable-font-zh_CN
Provides:       locale(zh_CN)

%description -n adobe-sourcehansans-cn-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehansans-cn-fonts
%files -n adobe-sourcehansans-cn-fonts
%defattr(0644,root,root,755)
%license SourceHanSansCN/LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansCN-*.otf

# Chinese Hongkong package
%package -n adobe-sourcehansans-hk-fonts
Summary:        Source Han Sans HK
Group:          System/X11/Fonts
Provides:       scalable-font-zh_HK
Provides:       locale(zh_HK)

%description -n adobe-sourcehansans-hk-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehansans-hk-fonts
%files -n adobe-sourcehansans-hk-fonts
%defattr(0644,root,root,755)
%license SourceHanSansHK/LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansHK-*.otf

# Japanese package
%package -n adobe-sourcehansans-jp-fonts
Summary:        Source Han Sans JP
Group:          System/X11/Fonts
Provides:       scalable-font-jp
Provides:       locale(jp)

%description -n adobe-sourcehansans-jp-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehansans-jp-fonts
%files -n adobe-sourcehansans-jp-fonts
%defattr(0644,root,root,755)
%license SourceHanSansJP/LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansJP-*.otf

# Korean package
%package -n adobe-sourcehansans-kr-fonts
Summary:        Source Han Sans KR
Group:          System/X11/Fonts
Provides:       scalable-font-kr
Provides:       locale(kr)

%description -n adobe-sourcehansans-kr-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehansans-kr-fonts
%files -n adobe-sourcehansans-kr-fonts
%defattr(0644,root,root,755)
%license SourceHanSansKR/LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansKR-*.otf

# Chinese Taiwan package
%package -n adobe-sourcehansans-tw-fonts
Summary:        Source Han Sans TW
# Replace the old single package that only provides Taiwan fonts
Group:          System/X11/Fonts
Provides:       adobe-sourcehansans-fonts = %version-%release
Provides:       scalable-font-zh_TW
Provides:       locale(zh_TW)
Obsoletes:      adobe-sourcehansans-fonts < %version-%release

%description -n adobe-sourcehansans-tw-fonts
%{shared_description}
%reconfigure_fonts_scriptlets -n adobe-sourcehansans-tw-fonts
%files -n adobe-sourcehansans-tw-fonts
%defattr(0644,root,root,755)
%license SourceHanSansTW/LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSansTW-*.otf

%changelog
