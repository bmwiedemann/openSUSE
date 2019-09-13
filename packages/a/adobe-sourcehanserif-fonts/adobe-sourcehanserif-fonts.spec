#
# spec file for package adobe-sourcehanserif-fonts
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


%define shared_description Source Han Serif is an open source Pan-CJK typeface whose OpenType/CFF fonts and CID-based sources are covered under the terms of the SIL Open Font License, Version 1.1.

Name:           adobe-sourcehanserif-fonts
Version:        1.001
Release:        0
Summary:        Source Han Serif fonts
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/adobe-fonts/source-han-serif
Source0:        https://raw.githubusercontent.com/adobe-fonts/source-han-serif/%{version}R/SubsetOTF/SourceHanSerifCN.zip
Source1:        https://raw.githubusercontent.com/adobe-fonts/source-han-serif/%{version}R/SubsetOTF/SourceHanSerifJP.zip
Source2:        https://raw.githubusercontent.com/adobe-fonts/source-han-serif/%{version}R/SubsetOTF/SourceHanSerifKR.zip
Source3:        https://raw.githubusercontent.com/adobe-fonts/source-han-serif/%{version}R/SubsetOTF/SourceHanSerifTW.zip
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

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
mv */*.otf %{buildroot}%{_ttfontsdir}

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
%license SourceHanSerifCN/LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifCN-*.otf

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
%license SourceHanSerifJP/LICENSE.txt
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
%license SourceHanSerifKR/LICENSE.txt
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
%license SourceHanSerifTW/LICENSE.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/SourceHanSerifTW-*.otf

%changelog
