#
# spec file for package tiro-indigo-fonts
#
# Copyright (c) 2022 SUSE LLC
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


Name:           tiro-indigo-fonts
Version:        1.52
Release:        0
Summary:        Tiro Fonts for some of the major Indian writing systems
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/TiroTypeworks/Indigo
Source0:        Indigo-%{version}.tar.xz
BuildRequires:  fontpackages-devel
Requires:       tiro-bangla-fonts
Requires:       tiro-devahindi-fonts
Requires:       tiro-devamarathi-fonts
Requires:       tiro-devasanskrit-fonts
Requires:       tiro-gurmukhi-fonts
Requires:       tiro-kannada-fonts
Requires:       tiro-tamil-fonts
Requires:       tiro-telugu-fonts
BuildArch:      noarch

%description
This packages contains all of the Tiro Indigo Fonts which have their
origins in a typeface designed for the Murty Classical Library of India
book series, so is especially suited to traditional literary publishing
but also made with the needs of today’s multiple print and screen media in mind.

%package -n tiro-bangla-fonts
Summary:        Tiro Bangla Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-bangla-fonts
Tiro Bangla has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%package -n tiro-devahindi-fonts
Summary:        Tiro Devanagari Hindi Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-devahindi-fonts
Tiro Devanagari Hindi has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%package -n tiro-devamarathi-fonts
Summary:        Tiro Devanagari Marathi Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-devamarathi-fonts
Tiro Devanagari Marathi has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%package -n tiro-devasanskrit-fonts
Summary:        Tiro Devanagari Sanskrit Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-devasanskrit-fonts
Tiro Devanagari Sanskrit has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%package -n tiro-gurmukhi-fonts
Summary:        Tiro Gurmukhi Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-gurmukhi-fonts
Tiro Gurmukhi has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%package -n tiro-kannada-fonts
Summary:        Tiro Kannada Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-kannada-fonts
Tiro Kannada has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%package -n tiro-tamil-fonts
Summary:        Tiro Tamil Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-tamil-fonts
Tiro Tamil has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%package -n tiro-telugu-fonts
Summary:        Tiro Telugu Fonts
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description -n tiro-telugu-fonts
Tiro Telugu has its origins in a typeface designed for the
Murty Classical Library of India book series, so is especially suited to
traditional literary publishing but also made with the needs of today’s
multiple print and screen media in mind.

%prep
%autosetup -n Indigo-%{version}

%build

%install
install -Dm 644 -t %{buildroot}%{_ttfontsdir} fonts/*/OTF/*.otf

%reconfigure_fonts_scriptlets -n tiro-bangla-fonts

%reconfigure_fonts_scriptlets -n tiro-devahindi-fonts

%reconfigure_fonts_scriptlets -n tiro-devamarathi-fonts

%reconfigure_fonts_scriptlets -n tiro-devasanskrit-fonts

%reconfigure_fonts_scriptlets -n tiro-gurmukhi-fonts

%reconfigure_fonts_scriptlets -n tiro-kannada-fonts

%reconfigure_fonts_scriptlets -n tiro-tamil-fonts

%reconfigure_fonts_scriptlets -n tiro-telugu-fonts

%files

%files -n tiro-bangla-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroBangla-*.otf

%files -n tiro-devahindi-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroDevaHindi-*.otf

%files -n tiro-devamarathi-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroDevaMarathi-*.otf

%files -n tiro-devasanskrit-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroDevaSanskrit-*.otf

%files -n tiro-gurmukhi-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroGurmukhi-*.otf

%files -n tiro-kannada-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroKannada-*.otf

%files -n tiro-tamil-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroTamil-*.otf

%files -n tiro-telugu-fonts
%defattr(0644,root,root,755)
%license fonts/OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/TiroTelugu-*.otf

%changelog
