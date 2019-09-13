#
# spec file for package monapo-fonts
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


Name:           monapo-fonts
Version:        20170722
Release:        0
Summary:        Monapo Japanese Truetype font
License:        IPA
Group:          System/X11/Fonts
Url:            http://linuxplayers.g1.xrea.com/modified_fonts_01.html
Source0:        monapo-%{version}.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       monapo = %{version}
Provides:       scalable-font-ja
Provides:       locale(ja)
Obsoletes:      monapo < %{version}
Provides:       monapo-font = %{version}
Obsoletes:      monapo-font <= 20090423
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides "monapo" Japanese TrueType font which is
based on IPA fonts (v3).  Monapo font is adjusted to be compatible
with MS P Gothic so that it can show Japanese Ascii Art properly.

%prep
%setup -q -n monapo-%{version}
for i in monafont-ttf-2.90/README*
do
    iconv -fsjis -tutf-8 < $i | sed "s/\r//g" > $i.tmp
    mv $i.tmp $i
done

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 644 monapo.ttf %{buildroot}%{_ttfontsdir}

%clean
rm -rf %{buildroot}

%reconfigure_fonts_scriptlets -c

%files
%defattr(-,root,root)
%doc ChangeLog README
%doc ipagp00303/IPA_Font_License_Agreement_v1.0.txt
%doc monafont-ttf-2.90/README-ttf.txt
%{_ttfontsdir}

%changelog
