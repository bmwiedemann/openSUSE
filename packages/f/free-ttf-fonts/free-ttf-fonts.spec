#
# spec file for package free-ttf-fonts
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


Name:           free-ttf-fonts
Version:        1.0
Release:        0
Summary:        Free TrueType Art Fonts
License:        Artistic-1.0 and GPL-2.0+ and SUSE-Public-Domain
Group:          System/X11/Fonts
# Fonts from http://www.dustismo.com/
# Licensed under GPL
Source0:        Dustismo.zip
Source1:        Junkyard.zip
Source2:        Swift.zip
Source3:        El_Abogado_Loco.zip
Source4:        MarkedFool.zip
Source5:        Wargames.zip
Source6:        balker.zip
Source7:        ItWasntMe.zip
Source8:        PenguinAttack.zip
Source9:        Winks.zip
Source10:       flatline.zip
# Fonts from http://www.thibault.org/fonts/isabella/
# Licensed under GPL
Source11:       Isabella.ttf.tar.gz
Source12:       latex-xft-fonts-0.1.tar.gz
# Fonts from http://www.larabiefonts.com/
# Licensed under a freeware license
Source100:      allfonts.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
More than 300 free fonts in True Type format. Most of them are in the
art style and unusable as desktop fonts, but are great for any poster
or illustration.

The fonts are copyrighted under the GPL or a Freeware license, but
donations are requested by the artists. Look in
/usr/share/doc/packages/free-ttf-fonts/ for further information.

%prep

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
mkdir -p %{buildroot}/%_docdir/%{name}
pushd %{buildroot}%{_ttfontsdir}/
    for i in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE100} \
      ; do
	unzip -o "$i"
    done
    for i in *.TTF *.TXT; do
        mv "$i" "`echo $i|tr '[A-Z]' '[a-z]'`"
    done
    dos2unix *.txt
    install -m 0644 *.txt %{buildroot}/%_docdir/%{name}
    rm %{buildroot}%{_ttfontsdir}/*.txt
popd
mkdir Isabella
pushd Isabella
    tar xfvz $RPM_SOURCE_DIR/Isabella.ttf.tar.gz
    install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}
    install -m 0644 README.txt %{buildroot}/%_docdir/%{name}/README.Isabella.txt
    install -m 0644 COPYING %{buildroot}/%_docdir/%{name}/COPYING.Isabella
popd
mkdir latex-xft
pushd latex-xft
    tar xfvz $RPM_SOURCE_DIR/latex-xft-fonts-0.1.tar.gz
    install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}
    install -m 0644 readme.latex-fonts %{buildroot}/%_docdir/%{name}
popd

%reconfigure_fonts_scriptlets

%files
%defattr(0644,root,root,755)
%_docdir/%{name}
%{_ttfontsdir}

%changelog
