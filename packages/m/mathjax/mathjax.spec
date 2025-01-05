#
# spec file for package mathjax
#
# Copyright (c) 2023 SUSE LLC
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


%{!?_fontsdir:%global _fontsdir %{_datadir}/fonts}
Name:           mathjax
Version:        3.2.2
Release:        0
Summary:        JavaScript library to render math in the browser
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://mathjax.org
Source0:        https://github.com/mathjax/MathJax/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fontpackages-devel
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
Requires:       %{name}-ams-fonts
Requires:       %{name}-calligraphic-fonts
Requires:       %{name}-fraktur-fonts
Requires:       %{name}-main-fonts
Requires:       %{name}-math-fonts
Requires:       %{name}-sansserif-fonts
Requires:       %{name}-script-fonts
Requires:       %{name}-size1-fonts
Requires:       %{name}-size2-fonts
Requires:       %{name}-size3-fonts
Requires:       %{name}-size4-fonts
Requires:       %{name}-typewriter-fonts
Requires:       %{name}-vector-fonts
Requires:       %{name}-zero-fonts
BuildArch:      noarch
%{?nodejs_requires}

%description
MathJax is an open-source JavaScript display engine for LaTeX, MathML,
and AsciiMath notation that works in all modern browsers. It requires no
setup on the part of the user (no plugins to download or software to
install), so the page author can write web documents that include
mathematics and be confident that users will be able to view it
naturally and easily. Supports LaTeX, MathML, and AsciiMath notation
in HTML pages.

%global fontsummary Fonts used by MathJax to display math in the browser
License:        Apache-2.0

%package ams-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description ams-fonts
%{fontsummary}.

%package calligraphic-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description calligraphic-fonts
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

%package       vector-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description   vector-fonts
%{fontsummary}.

%package       zero-fonts
Summary:        %{fontsummary}
License:        OFL-1.1
Group:          System/X11/Fonts

%description   zero-fonts
%{fontsummary}.

%prep
%setup -q -n MathJax-%{version}

%build

%install
%nodejs_install
install -d %{buildroot}%{_fontsdir}
cp es5/output/chtml/fonts/woff-v2/*.woff %{buildroot}%{_fontsdir}

%files
%license LICENSE
%doc README.md
%dir %{nodejs_modulesdir}
%{nodejs_modulesdir}/%{name}

%files ams-fonts
%{_fontsdir}/MathJax_AMS-Regular.*

%files calligraphic-fonts
%{_fontsdir}/MathJax_Calligraphic-*.*

%files fraktur-fonts
%{_fontsdir}/MathJax_Fraktur-*.*

%files main-fonts
%{_fontsdir}/MathJax_Main-*.*

%files math-fonts
%{_fontsdir}/MathJax_Math-*.*

%files sansserif-fonts
%{_fontsdir}/MathJax_SansSerif-*.*

%files script-fonts
%{_fontsdir}/MathJax_Script-*.*

%files typewriter-fonts
%{_fontsdir}/MathJax_Typewriter-*.*

%files size1-fonts
%{_fontsdir}/MathJax_Size1-*.*

%files size2-fonts
%{_fontsdir}/MathJax_Size2-*.*

%files size3-fonts
%{_fontsdir}/MathJax_Size3-*.*

%files size4-fonts
%{_fontsdir}/MathJax_Size4-*.*

%files vector-fonts
%{_fontsdir}/MathJax_Vector-*.*

%files zero-fonts
%{_fontsdir}/MathJax_Zero.*

%changelog
