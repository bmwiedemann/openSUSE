#
# spec file for package spec
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


Name:           mathjax
Version:        2.6.0
Release:        0
Summary:        JavaScript library to render math in the browser
Group:          Development/Libraries/Java
License:        Apache-2.0
Url:            http://mathjax.org
Source0:        https://github.com/mathjax/MathJax/archive/%{version}.tar.gz
BuildRequires:  fontpackages-devel
Requires:       %{name}-ams-fonts
Requires:       %{name}-caligraphic-fonts
Requires:       %{name}-fraktur-fonts %{name}-main-fonts
Requires:       %{name}-math-fonts
Requires:       %{name}-sansserif-fonts
Requires:       %{name}-script-fonts
Requires:       %{name}-size1-fonts
Requires:       %{name}-size2-fonts
Requires:       %{name}-size3-fonts
Requires:       %{name}-size4-fonts
Requires:       %{name}-typewriter-fonts
Requires:       %{name}-winchrome-fonts
Requires:       %{name}-winie6-fonts
BuildArch:      noarch

%description
MathJax is an open-source JavaScript display engine for LaTeX, MathML,
and AsciiMath notation that works in all modern browsers. It requires no
setup on the part of the user (no plugins to download or software to
install), so the page author can write web documents that include
mathematics and be confident that users will be able to view it
naturally and easily. Supports LaTeX, MathML, and AsciiMath notation
in HTML pages.

%global fontsummary Fonts used by MathJax to display math in the browser

%package ams-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description ams-fonts
%{fontsummary}.

%package caligraphic-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description caligraphic-fonts
%{fontsummary}.

%package fraktur-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description fraktur-fonts
%{fontsummary}.

%package main-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description main-fonts
%{fontsummary}.

%package math-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description math-fonts
%{fontsummary}.

%package sansserif-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description sansserif-fonts
%{fontsummary}.

%package script-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description script-fonts
%{fontsummary}.

%package typewriter-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description typewriter-fonts
%{fontsummary}.

%package size1-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description size1-fonts
%{fontsummary}.

%package size2-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description size2-fonts
%{fontsummary}.

%package size3-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description size3-fonts
%{fontsummary}.

%package size4-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description size4-fonts
%{fontsummary}.

%package winie6-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description winie6-fonts
%{fontsummary}.

%package winchrome-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description winchrome-fonts
%{fontsummary}.

%prep
%setup -q -n MathJax-%{version}
# Remove bundled fonts
rm -rf MathJax-2.4.0/jax/output
rm -rf MathJax-2.4.0/fonts/HTML-CSS/{Asana-Math,Gyre-Pagella,Gyre-Termes,Latin-Modern,Neo-Euler,STIX-Web}

# Remove minified javascript.
for i in $(find . -type f -path '*unpacked*'); do \
  mv $i ${i//unpacked/}; done
find . -depth -type d -path '*unpacked*' -delete
for i in MathJax.js jax/output/HTML-CSS/jax.js jax/output/HTML-CSS/imageFonts.js; do \
    sed -r 's#(MathJax|BASE)[.]isPacked#1#' <$i >$i.tmp; \
    touch -r $i $i.tmp; \
    mv $i.tmp $i; \
done

%build
# minification should be performed here at some point

%install
mkdir -p %{buildroot}%{_datadir}/javascript/mathjax
cp -pr MathJax.js config/ extensions/ jax/ localization/ test/ \
    %{buildroot}%{_datadir}/javascript/mathjax/

mkdir -p %{buildroot}%{_datadir}/javascript/mathjax/fonts/HTML-CSS/TeX/
cp -pr fonts/HTML-CSS/TeX/png %{buildroot}%{_datadir}/javascript/mathjax/fonts/HTML-CSS/TeX/

mkdir -p %{buildroot}%{_fontsdir}
cp -pr fonts/HTML-CSS/TeX/*/MathJax_$i*.{eot,otf,svg} %{buildroot}%{_fontsdir}

for t in eot otf svg; do \
    mkdir -p %{buildroot}%{_datadir}/javascript/mathjax/fonts/HTML-CSS/TeX/$t; \
    for i in fonts/HTML-CSS/TeX/$t/MathJax_*.$t; do \
        ln -s %{_fontsdir}/$(basename $i) \
            %{buildroot}%{_datadir}/javascript/mathjax/fonts/HTML-CSS/TeX/$t/; \
    done \
done

%files
%defattr(-,root,root)
%dir %{_datadir}/javascript
%{_datadir}/javascript/mathjax
%doc README.md LICENSE

%files ams-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_AMS-Regular.*

%files caligraphic-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Caligraphic-*.*

%files fraktur-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Fraktur-*.*

%files main-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Main-*.*

%files math-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Math-*.*

%files sansserif-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_SansSerif-*.*

%files script-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Script-*.*

%files typewriter-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Typewriter-*.*

%files size1-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Size1-*.*

%files size2-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Size2-*.*

%files size3-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Size3-*.*

%files size4-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_Size4-*.*

%files winie6-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_WinIE6-*.*

%files winchrome-fonts
%defattr(-,root,root)
%{_fontsdir}/MathJax_WinChrome-*.*

%changelog