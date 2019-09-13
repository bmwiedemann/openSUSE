#
# spec file for package texlive-cjk-latex-extras
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           texlive-cjk-latex-extras
BuildRequires:  freetype-tools
BuildRequires:  texlive
%if 0%{?suse_version} < 1300
BuildRequires:  texlive-bin
%endif
PreReq:         /bin/mkdir /bin/rm /usr/bin/touch /usr/bin/updmap
Requires:       freetype-tools
Requires:       texlive-cjk
Requires:       texlive-latex
Obsoletes:      cjk-latex
Obsoletes:      cjk-latex-han-300
Obsoletes:      cjk-latex-han-600
Obsoletes:      cjk-latex-han-tfmvf
Obsoletes:      cjk-latex-han1-300
Obsoletes:      cjk-latex-han1-600
Obsoletes:      cjk-latex-han1-tfmvf
Obsoletes:      cjk-latex-hbf-cns40-1
Obsoletes:      cjk-latex-hbf-cns40-2
Obsoletes:      cjk-latex-hbf-cns40-3
Obsoletes:      cjk-latex-hbf-cns40-4
Obsoletes:      cjk-latex-hbf-cns40-5
Obsoletes:      cjk-latex-hbf-cns40-6
Obsoletes:      cjk-latex-hbf-cns40-7
Obsoletes:      cjk-latex-hbf-cns40-b5
Obsoletes:      cjk-latex-hbf-hanja65
Obsoletes:      cjk-latex-hbf-jfs56
Obsoletes:      cjk-latex-hbf-jisksp40
Obsoletes:      cjk-latex-hbf-kanji48
Obsoletes:      cjk-latex-tfm-arphic-bkai00mp
Obsoletes:      cjk-latex-tfm-arphic-bsmi00lp
Obsoletes:      cjk-latex-tfm-arphic-gbsn00lp
Obsoletes:      cjk-latex-tfm-arphic-gkai00mp
Obsoletes:      cjk-latex-tfm-baekmuk
Obsoletes:      cjk-latex-tfm-bitstream-cyberbit
Obsoletes:      cjk-latex-tfm-kochi-gothic
Obsoletes:      cjk-latex-tfm-kochi-mincho
Obsoletes:      cjk-latex-tfm-microsoft-japanese
Obsoletes:      cjk-latex-tfm-xtt-fonts
Obsoletes:      cjk-latex-wadalab-gothic
Obsoletes:      cjk-latex-wadalab-maru
Obsoletes:      cjk-latex-wadalab-maru2
Obsoletes:      cjk-latex-wadalab-mincho
Obsoletes:      cjk-latex-wadalab-mincho2
Provides:       locale(texlive-cjk:ja;ko;zh)
Version:        20070515
Release:        0
Url:            http://cjk.ffii.org/
Source0:        texlive-cjk-latex-extras-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Extra fonts and scripts for CJK LaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base

%description
This package contains some extra font setup files and scripts to
automatically generate fonts and setup files to use with CJK LaTeX.

%prep
%setup0
mv README.SuSE README.SUSE
find . -name CVS -type d | xargs rm -rf

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/texmf/tex/latex
cp -a ./texinput $RPM_BUILD_ROOT/usr/share/texmf/tex/latex/CJK
# install the scripts to generate tfm files and Type1 fonts from TrueType fonts:
mkdir -p $RPM_BUILD_ROOT/sbin/conf.d
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -p -m 755 cjk-latex-config     $RPM_BUILD_ROOT/usr/sbin/
install -p -m 755 cjk-latex-t1mapgen   $RPM_BUILD_ROOT/usr/sbin/
install -p -m 755 sfd2map              $RPM_BUILD_ROOT/usr/sbin/

%post 
[ -x usr/bin/texhash ] && usr/bin/texhash
LC_ALL=POSIX /usr/sbin/cjk-latex-config
/usr/bin/updmap -sys --enable Map=wadalab.map
exit 0

%postun
[ -x usr/bin/texhash ] && usr/bin/texhash
exit 0

%files
%defattr(-, root, root)
%doc README.SUSE
%doc examples/
/usr/sbin/cjk-latex-config
/usr/sbin/cjk-latex-t1mapgen
/usr/sbin/sfd2map
%dir /usr/share/texmf/tex/
%dir /usr/share/texmf/tex/latex/
/usr/share/texmf/tex/latex/CJK

%changelog
