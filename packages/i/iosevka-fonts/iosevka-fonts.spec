#
# spec file for package iosevka-fonts
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


%global desc Iosevka is a sans-serif + slab-serif, monospace + quasi‑proportional\
typeface family, designed for writing code, using in terminals, and\
preparing technical documents.
Name:           iosevka-fonts
Version:        16.6.0
Release:        0
Summary:        Slender typeface for source code
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://typeof.net/Iosevka/
Source0:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-%{version}.zip
Source1:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-slab-%{version}.zip
Source2:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-curly-%{version}.zip
Source3:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-curly-slab-%{version}.zip
Source4:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-aile-%{version}.zip
Source5:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-etoile-%{version}.zip
Source6:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss01-%{version}.zip
Source7:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss02-%{version}.zip
Source8:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss03-%{version}.zip
Source9:        https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss04-%{version}.zip
Source10:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss05-%{version}.zip
Source11:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss06-%{version}.zip
Source12:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss07-%{version}.zip
Source13:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss08-%{version}.zip
Source14:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss09-%{version}.zip
Source15:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss10-%{version}.zip
Source16:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss11-%{version}.zip
Source17:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss12-%{version}.zip
Source18:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss13-%{version}.zip
Source19:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss14-%{version}.zip
Source20:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss15-%{version}.zip
Source21:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss16-%{version}.zip
Source22:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss17-%{version}.zip
Source23:       https://github.com/be5invis/Iosevka/releases/download/v%{version}/super-ttc-iosevka-ss18-%{version}.zip
Source100:      https://raw.githubusercontent.com/be5invis/Iosevka/v%{version}/LICENSE.md
Source101:      https://raw.githubusercontent.com/be5invis/Iosevka/v%{version}/README.md
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Recommends:     iosevka-aile-fonts
Recommends:     iosevka-curly-fonts
Recommends:     iosevka-curly-slab-fonts
Recommends:     iosevka-etoile-fonts
Recommends:     iosevka-slab-fonts
Recommends:     iosevka-ss01-fonts
Recommends:     iosevka-ss02-fonts
Recommends:     iosevka-ss03-fonts
Recommends:     iosevka-ss04-fonts
Recommends:     iosevka-ss05-fonts
Recommends:     iosevka-ss06-fonts
Recommends:     iosevka-ss07-fonts
Recommends:     iosevka-ss08-fonts
Recommends:     iosevka-ss09-fonts
Recommends:     iosevka-ss10-fonts
Recommends:     iosevka-ss11-fonts
Recommends:     iosevka-ss12-fonts
Recommends:     iosevka-ss13-fonts
Recommends:     iosevka-ss14-fonts
Recommends:     iosevka-ss15-fonts
Recommends:     iosevka-ss16-fonts
Recommends:     iosevka-ss17-fonts
Recommends:     iosevka-ss18-fonts
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
%{desc}

This package contains the Iosevka typeface (monospace, default).

%package -n	iosevka-slab-fonts
Summary:        Iosevka in monospace slab-serif style
Group:          System/X11/Fonts

%description -n	iosevka-slab-fonts
%{desc}

This package contains the Iosevka Slab typeface (monospace, slab-serif).

%package -n	iosevka-curly-fonts
Summary:        Iosevka in monospace curly style
Group:          System/X11/Fonts

%description -n	iosevka-curly-fonts
%{desc}

This package contains the Iosevka Curly typeface (curly style).

%package -n	iosevka-curly-slab-fonts
Summary:        Iosevka in monospace slab-serif curly style
Group:          System/X11/Fonts

%description -n	iosevka-curly-slab-fonts
%{desc}

This package contains the Iosevka Curly Slab typeface (curly style,
slab-serif).

%package -n	iosevka-aile-fonts
Summary:        Iosevka in quasi-proportional sans-serif style
Group:          System/X11/Fonts

%description -n	iosevka-aile-fonts
%{desc}

This package contains the Iosevka Aile typeface (quasi-proportional,
sans-serif).

%package -n	iosevka-etoile-fonts
Summary:        Iosevka in quasi-proportional slab-serif style
Group:          System/X11/Fonts

%description -n	iosevka-etoile-fonts
%{desc}

This package contains the Iosevka Etoile typeface (quasi-proportional,
slab-serif).

%package -n	iosevka-ss01-fonts
Summary:        Iosevka in monospace, Andale Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss01-fonts
%{desc}

This package contains the Iosevka SS01 typeface (monospace, Andale Mono style).

%package -n	iosevka-ss02-fonts
Summary:        Iosevka in monospace, Anonymous Pro style
Group:          System/X11/Fonts

%description -n	iosevka-ss02-fonts
%{desc}

This package contains the Iosevka SS02 typeface (monospace, Anonymous Pro
style).

%package -n	iosevka-ss03-fonts
Summary:        Iosevka in monospace, Consolas style
Group:          System/X11/Fonts

%description -n	iosevka-ss03-fonts
%{desc}

This package contains the Iosevka SS03 typeface (monospace, Consolas style).

%package -n	iosevka-ss04-fonts
Summary:        Iosevka in monospace, Menlo style
Group:          System/X11/Fonts

%description -n	iosevka-ss04-fonts
%{desc}

This package contains the Iosevka SS04 typeface (monospace, Menlo style).

%package -n	iosevka-ss05-fonts
Summary:        Iosevka in monospace, Fira Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss05-fonts
%{desc}

This package contains the Iosevka SS05 typeface (monospace, Fira Mono style).

%package -n	iosevka-ss06-fonts
Summary:        Iosevka in monospace, Liberation Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss06-fonts
%{desc}

This package contains the Iosevka SS06 typeface (monospace, Liberation Mono
style).

%package -n	iosevka-ss07-fonts
Summary:        Iosevka in monospace, Monaco style
Group:          System/X11/Fonts

%description -n	iosevka-ss07-fonts
%{desc}

This package contains the Iosevka SS07 typeface (monospace, Monaco style).

%package -n	iosevka-ss08-fonts
Summary:        Iosevka in monospace, Pragmata Pro style
Group:          System/X11/Fonts

%description -n	iosevka-ss08-fonts
%{desc}

This package contains the Iosevka SS08 typeface (monospace, Pragmata Pro
style).

%package -n	iosevka-ss09-fonts
Summary:        Iosevka in monospace, Source Code Pro style
Group:          System/X11/Fonts

%description -n	iosevka-ss09-fonts
%{desc}

This package contains the Iosevka SS09 typeface (monospace, Source Code Pro
style).

%package -n	iosevka-ss10-fonts
Summary:        Iosevka in monospace, Envy Code R style
Group:          System/X11/Fonts

%description -n	iosevka-ss10-fonts
%{desc}

This package contains the Iosevka SS10 typeface (monospace, Envy Code R style).

%package -n	iosevka-ss11-fonts
Summary:        Iosevka in monospace, X Windows Fixed style
Group:          System/X11/Fonts

%description -n	iosevka-ss11-fonts
%{desc}

This package contains the Iosevka SS11 typeface (monospace, X Windows Fixed
style).

%package -n	iosevka-ss12-fonts
Summary:        Iosevka in monospace, Ubuntu Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss12-fonts
%{desc}

This package contains the Iosevka SS12 typeface (monospace, Ubuntu Mono style).

%package -n	iosevka-ss13-fonts
Summary:        Iosevka in monospace, Lucida style
Group:          System/X11/Fonts

%description -n	iosevka-ss13-fonts
%{desc}

This package contains the Iosevka SS13 typeface (monospace, Lucida style).

%package -n	iosevka-ss14-fonts
Summary:        Iosevka in monospace, JetBrains Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss14-fonts
%{desc}

This package contains the Iosevka SS14 typeface (monospace, JetBrains Mono
style).

%package -n	iosevka-ss15-fonts
Summary:        Iosevka in monospace, IBM Plex Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss15-fonts
%{desc}

This package contains the Iosevka SS15 typeface (monospace, IBM Plex Mono
style).

%package -n	iosevka-ss16-fonts
Summary:        Iosevka in monospace, PT Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss16-fonts
%{desc}

This package contains the Iosevka SS16 typeface (monospace, PT Mono style).

%package -n	iosevka-ss17-fonts
Summary:        Iosevka in monospace, Recursive Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss17-fonts
%{desc}

This package contains the Iosevka SS17 typeface (monospace, Recursive Mono
style).

%package -n	iosevka-ss18-fonts
Summary:        Iosevka in monospace, Input Mono style
Group:          System/X11/Fonts

%description -n	iosevka-ss18-fonts
%{desc}

This package contains the Iosevka SS18 typeface (monospace, Input Mono style).

%prep
%autosetup -cT
for s in %{_sourcedir}/super-ttc-iosevka*%{version}.zip; do
	unzip -qq $s '*.ttc'
done
cp %{SOURCE100} %{SOURCE101} .

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -m0644 iosevka.ttc %{buildroot}%{_ttfontsdir}/Iosevka.ttc
install -m0644 iosevka-aile.ttc %{buildroot}%{_ttfontsdir}/IosevkaAile.ttc
install -m0644 iosevka-curly.ttc %{buildroot}%{_ttfontsdir}/IosevkaCurly.ttc
install -m0644 iosevka-curly-slab.ttc %{buildroot}%{_ttfontsdir}/IosevkaCurlySlab.ttc
install -m0644 iosevka-etoile.ttc %{buildroot}%{_ttfontsdir}/IosevkaEtoile.ttc
install -m0644 iosevka-curly-slab.ttc %{buildroot}%{_ttfontsdir}/IosevkaCurlySlab.ttc
install -m0644 iosevka-slab.ttc %{buildroot}%{_ttfontsdir}/IosevkaSlab.ttc
for i in $(seq -w 1 18); do
	install -m0644 iosevka-ss$i.ttc %{buildroot}%{_ttfontsdir}/IosevkaSS$i.ttc
done

%reconfigure_fonts_scriptlets
%reconfigure_fonts_scriptlets -n iosevka-slab-fonts
%reconfigure_fonts_scriptlets -n iosevka-curly-fonts
%reconfigure_fonts_scriptlets -n iosevka-curly-slab-fonts
%reconfigure_fonts_scriptlets -n iosevka-aile-fonts
%reconfigure_fonts_scriptlets -n iosevka-etoile-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss01-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss02-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss03-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss04-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss05-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss06-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss07-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss08-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss09-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss10-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss11-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss12-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss13-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss14-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss15-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss16-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss17-fonts
%reconfigure_fonts_scriptlets -n iosevka-ss18-fonts

%files
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/Iosevka.ttc

%files -n iosevka-slab-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSlab.ttc

%files -n iosevka-curly-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaCurly.ttc

%files -n iosevka-curly-slab-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaCurlySlab.ttc

%files -n iosevka-aile-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaAile.ttc

%files -n iosevka-etoile-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaEtoile.ttc

%files -n iosevka-ss01-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS01.ttc

%files -n iosevka-ss02-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS02.ttc

%files -n iosevka-ss03-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS03.ttc

%files -n iosevka-ss04-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS04.ttc

%files -n iosevka-ss05-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS05.ttc

%files -n iosevka-ss06-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS06.ttc

%files -n iosevka-ss07-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS07.ttc

%files -n iosevka-ss08-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS08.ttc

%files -n iosevka-ss09-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS09.ttc

%files -n iosevka-ss10-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS10.ttc

%files -n iosevka-ss11-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS11.ttc

%files -n iosevka-ss12-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS12.ttc

%files -n iosevka-ss13-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS13.ttc

%files -n iosevka-ss14-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS14.ttc

%files -n iosevka-ss15-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS15.ttc

%files -n iosevka-ss16-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS16.ttc

%files -n iosevka-ss17-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS17.ttc

%files -n iosevka-ss18-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSS18.ttc

%changelog
