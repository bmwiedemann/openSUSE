#
# spec file for package arphic-ukai-fonts
#
# Copyright (c) 2023 SUSE LLC
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


Name:           arphic-ukai-fonts
Version:        0.2.20080216.1
Release:        0
Summary:        CJK Unicode Font Kai Style
License:        Arphic-1999
Group:          System/X11/Fonts
URL:            https://www.freedesktop.org/wiki/Software/CJKUnifonts/
# download http://ftp.tw.debian.org/debian/pool/main/t/ttf-arphic-ukai/ttf-arphic-ukai_0.2.20080216.1.orig.tar.gz
Source0:        ttf-arphic-ukai-0.2.20080216.1.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-HK
Provides:       scalable-font-zh-MO
Provides:       scalable-font-zh-SG
Provides:       scalable-font-zh-TW
Provides:       ttf-arphic-ukai = %{version}
Provides:       locale(zh_TW;zh_HK;zh_CN;zh_SG;zh_MO)
Obsoletes:      ttf-arphic-ukai <= 0.1.20060928
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This font was taken from the from the TrueType fonts generously
released by Arphic Technologies Taiwan under the Arphic Public License.
It was modified with Fontforge by Arne Goetje <arne@linux.org.tw> to
contain both Big5 and GB2312 charsets plus some european characters.

Currently it fully supports the following charsets:
ISO8859-1,2,3,4,7,9,10,13,14,15 Big5 GB2312-80 Bopomofo Extensions for
Hakka, Minnan (Unicode 4.0) and MBE variants using the Stylistic
Alternatives (salt) feature from the OTF spec.

Partly support is implemented for: HKSCS CNS 11643 GB18030 Japanese
Korean

%prep
%setup -n ttf-arphic-ukai-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttc %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc CONTRIBUTERS README FONTLOG fonts.dir fonts.scale license NEWS TODO KNOWN_ISSUES Font_Comparison_ZenKai_UKai.pdf
%{_ttfontsdir}

%changelog
