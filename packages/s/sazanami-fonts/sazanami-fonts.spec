#
# spec file for package sazanami-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sazanami-fonts
Version:        20040629
Release:        0
Summary:        Japanese "Sazanami" TrueType Fonts
License:        BSD-3-Clause and SUSE-Public-Domain
Group:          System/X11/Fonts
# http://wiki.fdiary.net/font/?sazanami
Url:            http://sourceforge.jp/projects/efont/files/
Source0:        http://kyushu-u.dl.sourceforge.jp/efont/10087/sazanami-20040629.tar.bz2
Source1:        fonts.scale.sazanami-fonts
Source2:        copy-uni3231
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         license-translation.patch
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-ja
Provides:       locale(ja)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains Japanese "Sazanami" TrueType fonts.

%prep
%setup -n sazanami-%{version}
%patch0 -p1

%build
# Copy U+3231 from Sazanami Gothic into Sazanami Mincho
chmod 755 $RPM_SOURCE_DIR/copy-uni3231
fontforge -lang=ff -script $RPM_SOURCE_DIR/copy-uni3231
for i in README doc/ayu/README.txt doc/kappa/README doc/misaki/misakib8.txt doc/mplus/LICENSE_J doc/shinonome/LICENSE-en
do
    iconv -f EUC-JP -t UTF-8 < $i > $i.UTF-8
    mv $i.UTF-8 $i
done
for i in doc/oradano/README.txt
do
    iconv -f SHIFT-JIS -t UTF-8 < $i > $i.UTF-8
    mv $i.UTF-8 $i
done

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}
install -c -m 644 $RPM_SOURCE_DIR/fonts.scale.* %{buildroot}%{_ttfontsdir}
# these symlinks and the fonts.scale.sazanami-fonts are a hack
# to make flash-player work with Japanese in SUSE Linux 10.1/SLES10/SLED10
# see Bugzilla #196191:
pushd %{buildroot}%{_ttfontsdir}
    ln -s sazanami-mincho.ttf smincho.ttf
    ln -s sazanami-gothic.ttf sgothic.ttf
popd

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc README*
%doc doc
%{_ttfontsdir}

%changelog
