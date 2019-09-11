#
# spec file for package wqy-microhei-fonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wqy-microhei-fonts
Version:        0.2.0+snapshot20150915
Release:        0
Summary:        WenQuanYi Micro Hei CJK Font
License:        Apache-2.0 or SUSE-GPL-3.0+-with-font-exception
Group:          System/X11/Fonts
Url:            http://wenq.org/en/
Source:         wqy-microhei-0.2.nightly-build.tar.gz
Source1:        57-wqy-microhei.conf
BuildRequires:  fontpackages-devel
Requires(pre):  fontconfig
Provides:       scalable-font-zh-CN
Provides:       scalable-font-zh-SG
Provides:       scalable-font-zh-TW
Provides:       ttf-wqy-microhei = %{version}
Obsoletes:      ttf-wqy-microhei <= 0.2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
WenQuanYi Micro Hei font family is a Sans-Serif style (also known as
Hei,
Gothic or Dotum among the Chinese/Japanese/Korean users) high quality

CJK outline font. It was derived from "Droid Sans Fallback", "Droid
Sans" and "Droid Sans Mono" released by Google Corp. This font
package
contains two faces, "Micro Hei" and "Micro Hei Mono", in form of a
True-Type Collection (ttc) file. All the unified CJK Han glyphs, i.e.

GBK Hanzi, in the range of U+4E00-U+9FC3 defined in Unicode Standard
5.1
are covered, with additional support to many other international
languages such as Latin, Extended Latin, Hanguls and Kanas. The font
file is extremely compact (~5M) compared with most known CJK fonts.
As a result, it can be used for hand-held devices or embedded systems,
or
used on PC with a significantly small memory footprint. Because both
font faces carry hinting and kerning instructions for Latin glyphs,
they are the excellent choices for desktop fonts.

%prep
%setup -q -n wqy-microhei

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -c -m 644 wqy-microhei.ttc %{buildroot}%{_ttfontsdir}
%install_fontsconf %{SOURCE1}

%reconfigure_fonts_scriptlets -c

%files
%defattr(-,root,root)
%doc README.txt ChangeLog.txt LICENSE_GPLv3.txt
%{_ttfontsdir}
%{files_fontsconf_availdir}
%files_fontsconf_file -l 57-wqy-microhei.conf

%changelog
