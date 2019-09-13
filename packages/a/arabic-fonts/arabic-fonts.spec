#
# spec file for package arabic-fonts
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


# missing license specification for Haydar family, 
# sent mail to sales@haydarnet.nl, info@haydarlinux.org
%define with_haydar  0
# missing license to Nesf2 family, 
# sent mail to lucdevroye@gmail.com
%define with_nesf2   0

Name:           arabic-fonts
Version:        0.20161120
Release:        0
Summary:        A Collection of Free Arabic Fonts
License:        GPL-2.0-only AND SUSE-Public-Domain AND OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.arabeyes.org/resources.php
# public domain:
Source0:        http://downloads.sourceforge.net/arabeyes/ae_fonts_mono.tar.bz2
Source1:        http://downloads.sourceforge.net/arabeyes/haydar_fonts.tar.bz2
Source2:        http://downloads.sourceforge.net/arabeyes/kacst_fonts_2.01.tar.bz2
Source3:        http://downloads.sourceforge.net/arabeyes/lateef.shaikh_fonts.tar.bz2
Source4:        http://downloads.sourceforge.net/arabeyes/sharif.univ_ttf.bz2
Source5:        http://downloads.sourceforge.net/arabeyes/ae_fonts_2.0.tar.bz2
Source6:        http://downloads.sourceforge.net/arabeyes/kacst_one_5.0.tar.bz2
Source7:        https://github.com/alif-type/amiri/releases/download/0.109/amiri-0.109.zip
BuildRequires:  bdftopcf
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%if 0%{?suse_version} >= 1220
BuildRequires:  unzip
#BuildRequires:  fontconfig
#BuildRequires:  imake
#BuildRequires:  mkfontdir
#BuildRequires:  xorg-cf-files
%else
BuildRequires:  xorg-x11
%endif
%reconfigure_fonts_prereq
Requires:       arabic-ae-fonts
Requires:       arabic-bitmap-fonts
%if %{with_haydar}
Requires:       arabic-haydar-bitmap-fonts
%endif
Requires:       arabic-kacst-fonts
Requires:       arabic-kacstone-fonts
Requires:       arabic-naqsh-fonts
%if %{with_nesf2}
Requires:       arabic-nesf2-fonts
%endif
Provides:       scalable-font-ar
Provides:       locale(ar)
Obsoletes:      fonts-arabic <= 0.20091208
Provides:       fonts-arabic = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A collection of free Arabic fonts available from
http://www.arabeyes.org/resources.php.

%package -n arabic-bitmap-fonts
Summary:        Arabic Bitmap Font
License:        SUSE-Public-Domain
Group:          System/X11/Fonts
Version:        1.0
Release:        0
# according to PS Names Copyright:
Provides:       locale(ar)

%description -n arabic-bitmap-fonts
Misc Fixed family with arabic symbols.

%if %{with_haydar}
%package -n arabic-haydar-bitmap-fonts
Summary:        Arabic Bitmap Font
License:        SUSE-Public-Domain
Group:          System/X11/Fonts
Version:        1.0
Release:        0
Provides:       locale(ar)

%description -n arabic-haydar-bitmap-fonts
Arabic bitmap font (Haydar family).
%endif

%package -n arabic-kacst-fonts
Summary:        Arabic Kacst Fonts
License:        GPL-2.0-only
Group:          System/X11/Fonts
Version:        2.01
Release:        0
Provides:       locale(ar)

%description -n arabic-kacst-fonts
TrueType families developed by Kacst institution.

%package -n arabic-kacstone-fonts
Summary:        Arabic Kacst One Fonts
License:        GPL-2.0-only
Group:          System/X11/Fonts
Version:        5.0
Release:        0
Provides:       locale(ar)

%description -n arabic-kacstone-fonts
KacstOne family developed by Kacst institution.

%package -n arabic-naqsh-fonts
Summary:        Arabic Naqsh Font
License:        GPL-2.0-only
Group:          System/X11/Fonts
Version:        2.1
Release:        0
Provides:       locale(ar)

%description -n arabic-naqsh-fonts
Arabic TrueType font (Naqsh family).

%if %{with_nesf2}
%package -n arabic-nesf2-fonts
Summary:        Arabic Nesf2 Font
License:        SUSE-Public-Domain
Group:          System/X11/Fonts
Version:        20000102
Release:        0
Provides:       locale(ar)

%description -n arabic-nesf2-fonts
Arabic TrueType font (Nesf2 family).
%endif

%package -n arabic-ae-fonts
Summary:        Arabic Free and Open Source Fonts
License:        GPL-2.0-only
Group:          System/X11/Fonts
Version:        2.0
Release:        0
Provides:       locale(ar)

%description -n arabic-ae-fonts
Arabic TrueType fonts collected by Arab Eyes (www.arabeyes.org).

%package -n arabic-amiri-fonts
Summary:        Amiri Naksh Typeface
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.amirifont.org/
Version:        0.109
Release:        0
Provides:       locale(ar)

%description -n arabic-amiri-fonts
Amiri family is high quality Arabic Naskh typeface.

%prep
%setup -T -c %{name} -n %{name} -a 0 -a 2 -a 3 -a 5 -a 6 -a 7
%if %{with_haydar}
tar -xf %{SOURCE1}
%endif
%if %{with_nesf2}
bunzip2 --stdout %{_sourcedir}/sharif.univ_ttf.bz2 > Nesf2.ttf
%endif

%build
dos2unix License.txt

%install
mkdir -p %{buildroot}%{_miscfontsdir}
mkdir -p %{buildroot}%{_ttfontsdir}
for i in *.ttf */*.ttf */*/*.ttf
do
    # one of the kacst TrueType font files has size zero
    # make sure to install only .ttf files with size greater than zero
    # (OpenOffice even coredumps when .ttf files with size zero
    # are in the path).
    if [ -s $i ] ; then
        install -c -m 644 $i %{buildroot}%{_ttfontsdir}
    fi
done
for i in */*.bdf
do
    o="${i##*/}"
    bdftopcf "$i" | gzip -n9 >"%{buildroot}/%{_miscfontsdir}/${o%.bdf}.pcf.gz"
done

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%dir %{_miscfontsdir}
%dir %{_ttfontsdir}

%files -n arabic-bitmap-fonts
%defattr(-,root,root)
%{_miscfontsdir}/10x21.pcf.gz

%if %{with_haydar}
%files -n arabic-haydar-bitmap-fonts
%defattr(-,root,root)
%{_miscfontsdir}/haydar*.pcf.gz
%endif

%files -n arabic-kacst-fonts
%defattr(-,root,root)
%doc KacstArabicFonts-*/{Copyright,LICENSE,README}
%{_ttfontsdir}/Kacst*.ttf
%exclude %{_ttfontsdir}/KacstOne*.ttf

%files -n arabic-kacstone-fonts
%defattr(-,root,root)
%doc kacst_one_*/{BUGS,ChangeLog,Copyright,LICENSE,NEWS,README}
%{_ttfontsdir}/KacstOne*.ttf

%files -n arabic-naqsh-fonts
%defattr(-,root,root)
%doc License.txt
%{_ttfontsdir}/Naqsh.ttf

%if %{with_nesf2}
%files -n arabic-nesf2-fonts
%defattr(-,root,root)
%{_ttfontsdir}/Nesf2.ttf
%endif

%files -n arabic-ae-fonts
%defattr(-,root,root)
%doc ae_fonts_*/{ChangeLog,COPYING,README}
%{_ttfontsdir}/ae_*.ttf

%files -n arabic-amiri-fonts
%defattr(-,root,root)
%doc amiri*/*.pdf amiri*/NEWS* amiri*/OFL.txt amiri*/README*
%{_ttfontsdir}/amiri*.ttf

%changelog
