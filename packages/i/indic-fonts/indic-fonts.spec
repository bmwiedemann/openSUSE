#
# spec file for package indic-fonts
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


%define lohit_version 20140220

Name:           indic-fonts
Version:        20160512
Release:        0
Summary:        Professional Indian Language TrueType Fonts
License:        GPL-2.0+ and OFL-1.1
Group:          System/X11/Fonts
Url:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/lohit-ttf-%{lohit_version}.tar.gz
# Other free indic fonts collected by
# Amish Munshi <amunshi@novell.com> (he is not working at Novell anymore):
Source1:        indic-fonts.tar.bz2
Source2:        clear-latin-instrs.ff
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
Recommends:     pothana2000
Provides:       scalable-font-bn
Provides:       scalable-font-gu
Provides:       scalable-font-hi
Provides:       scalable-font-mr
Provides:       scalable-font-pa
Provides:       scalable-font-ta
Provides:       locale(ta;bn;gu;hi;mr;pa)
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains many professional Indian language TrueType fonts
contributed by the community and some also donated by organizations to
open source. All fonts are available under GPL-2.0+ or OFL-1.1.

%prep
%setup -q -n lohit-ttf-%{lohit_version} -a 1
mv indic/doc docs-for-non-lohit-fonts

%build
# bsc#977195
pushd indic/fonts/gujrati
for file in aakar-medium.ttf padmaa-Bold.1.1.ttf padmaa-Medium-0.5.ttf Rekha.ttf; do
  fontforge -lang=ff -script %{SOURCE2} $file
  mv fixed.$file $file
done
popd

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
# Lohit fonts:
install -m 644 ./*.?tf %{buildroot}%{_ttfontsdir}
# other fonts:
install -m 644 ./indic//fonts/*/*.?tf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc docs-for-non-lohit-fonts
%doc COPYRIGHT OFL.txt
%{_ttfontsdir}

%changelog
