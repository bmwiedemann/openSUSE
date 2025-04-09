#
# spec file for package ibm-plex-fonts
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Shawn W Dunn <sfalken@opensuse.org>
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


%global srcurl https://github.com/IBM/plex/releases/download/
%global common_description %{expand:
IBM Plex is a typeface superfamily to reflect the design principles
of IBM and to be used for all brand material across the company
internationally.
}
%define fname ibm-plex
%define sname plex-sans

Name:           ibm-plex-fonts
Version:        6.4.0
Release:        0
Summary:        A set of coordinated grotesque corporate fonts
License:        OFL-1.1
BuildArch:      noarch
URL:            https://www.ibm.com/plex
Source0:        %{srcurl}/v%{version}/OpenType.zip

BuildRequires:  fontpackages-devel
BuildRequires:  unzip

Requires:       %{fname}-mono-fonts
Requires:       %{fname}-sans-arabic-fonts
Requires:       %{fname}-sans-condensed-fonts
Requires:       %{fname}-sans-devanagari-fonts
Requires:       %{fname}-sans-fonts
Requires:       %{fname}-sans-hebrew-fonts
Requires:       %{fname}-sans-kr-fonts
Requires:       %{fname}-sans-thai-fonts
Requires:       %{fname}-sans-thai-looped-fonts
Requires:       %{fname}-serif-fonts
%reconfigure_fonts_prereq

%description
%{common_description}

%dnl --------------------------------------------------------------

%package -n %{fname}-mono-fonts
Summary:        IBM Plex Mono
%reconfigure_fonts_prereq

%description -n %{fname}-mono-fonts
%{common_description}

Plex Mono is a monospaced typeface based on Plex Sans. The italic
design was inspired by the Italic 12 typeface used on the IBM
Selectric typewriter.

%files -n %{fname}-mono-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexMono*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-fonts
Summary:        IBM Plex Sans
%reconfigure_fonts_prereq

%description -n %{fname}-sans-fonts
%{common_description}

Plex Sans is a grotesque sans-serif typeface with a design that was
inspired by Franklin Gothic. Some of Franklin Gothic's features such
as the angled terminals, a double-storey g and a horizontal line at
the baseline of the 1 are used.

%files -n %{fname}-sans-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSans-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-arabic-fonts
Summary:        IBM Plex Sans Arabic
%reconfigure_fonts_prereq

%description -n %{fname}-sans-arabic-fonts
%{common_description}
This package provides IBM Plex Sans Arabic.

%files -n %{fname}-sans-arabic-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSansArabic-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-condensed-fonts
Summary:        IBM Plex Sans Condensed
%reconfigure_fonts_prereq

%description -n %{fname}-sans-condensed-fonts
%{common_description}
This package provides IBM Plex Sans Condensed.

%files -n %{fname}-sans-condensed-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSansCondensed-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-devanagari-fonts
Summary:        IBM Plex Sans Devanagari
%reconfigure_fonts_prereq

%description -n %{fname}-sans-devanagari-fonts
%{common_description}
This package provides IBM Plex Sans Devanagari.

%files -n %{fname}-sans-devanagari-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSansDevanagari-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-hebrew-fonts
Summary:        IBM Plex Sans Hebrew
%reconfigure_fonts_prereq

%description -n %{fname}-sans-hebrew-fonts
%{common_description}
This package provides IBM Plex Sans Hebrew.

%files -n %{fname}-sans-hebrew-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSansHebrew-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-kr-fonts
Summary:        IBM Plex Sans KR
%reconfigure_fonts_prereq

%description -n %{fname}-sans-kr-fonts
%{common_description}
This package provides IBM Plex Sans KR.

%files -n %{fname}-sans-kr-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSansKR-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-thai-fonts
Summary:        IBM Plex Sans Thai
%reconfigure_fonts_prereq

%description -n %{fname}-sans-thai-fonts
%{common_description}
This package provides IBM Plex Sans Thai.

%files -n %{fname}-sans-thai-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSansThai-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-sans-thai-looped-fonts
Summary:        IBM Plex Sans Thai Looped
%reconfigure_fonts_prereq

%description -n %{fname}-sans-thai-looped-fonts
%{common_description}
This package provides IBM Plex Sans Thai Looped.

%files -n %{fname}-sans-thai-looped-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSansThaiLooped-*.otf

%dnl --------------------------------------------------------------

%package -n %{fname}-serif-fonts
Summary:        IBM Plex Serif
%reconfigure_fonts_prereq

%description -n %{fname}-serif-fonts
%{common_description}

Plex Serif is a transitional serif typeface with a design that was
inspired by Bodoni and Janson. Some of Bodoni's features such as ball
terminals and rectangular serifs are used in Plex Serif.

%files -n %{fname}-serif-fonts
%license license.txt
%{_ttfontsdir}/IBMPlexSerif*.otf

%dnl -------------------------------------------------------------

%prep
%autosetup -c

%build

%install
install -D -t %{buildroot}%{_ttfontsdir} -pm 0644 OpenType/IBM-Plex*/*.otf
install -D -t %{buildroot}%{_licensedir}/%{name} -pm 0644 OpenType/IBM-Plex-Sans/license.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-mono-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-arabic-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-condensed-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-devanagari-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-hebrew-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-kr-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-thai-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-sans-thai-looped-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt
install -D -t %{buildroot}%{_licensedir}/%{fname}-serif-fonts -pm 0644 OpenType/IBM-Plex-Sans/*.txt

%reconfigure_fonts_scriptlets -n %{fname}-mono-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-arabic-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-condensed-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-devanagari-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-hebrew-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-kr-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-thai-fonts
%reconfigure_fonts_scriptlets -n %{fname}-sans-thai-looped-fonts
%reconfigure_fonts_scriptlets -n %{fname}-serif-fonts

%files
# Include additional content for the font package, if available
%license license.txt
%dir %{_ttfontsdir}

%changelog
