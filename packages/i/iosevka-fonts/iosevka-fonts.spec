#
# spec file for package iosevka-fonts
#
# Copyright (c) 2021 SUSE LLC
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


%define _buildshell /bin/bash
%global         fullversion %{version}
Name:           iosevka-fonts
Version:        6.0.1
Release:        0
Summary:        Slender typeface for source code
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://typeof.net/Iosevka/
Source0:        https://github.com/be5invis/Iosevka/releases/download/v%{fullversion}/ttc-iosevka-%{fullversion}.zip
Source1:        https://github.com/be5invis/Iosevka/releases/download/v%{fullversion}/ttc-iosevka-slab-%{fullversion}.zip
Source2:        https://github.com/be5invis/Iosevka/releases/download/v%{fullversion}/ttc-iosevka-curly-%{fullversion}.zip
Source3:        https://github.com/be5invis/Iosevka/releases/download/v%{fullversion}/ttc-iosevka-curly-slab-%{fullversion}.zip
Source4:        https://github.com/be5invis/Iosevka/releases/download/v%{fullversion}/ttc-iosevka-aile-%{fullversion}.zip
Source5:        https://github.com/be5invis/Iosevka/releases/download/v%{fullversion}/ttc-iosevka-etoile-%{fullversion}.zip
Source6:        https://raw.githubusercontent.com/be5invis/Iosevka/master/LICENSE.md
Source7:        https://raw.githubusercontent.com/be5invis/Iosevka/master/README.md
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
Recommends:     iosevka-aile-fonts
Recommends:     iosevka-curly-fonts
Recommends:     iosevka-curly-slab-fonts
Recommends:     iosevka-etoile-fonts
Recommends:     iosevka-slab-fonts
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Iosevka is a sans-serif + slab-serif, monospace + quasi‑proportional
typeface family, designed for writing code, using in terminals, and
preparing technical documents.

%package -n	iosevka-slab-fonts
Summary:        Iosevka in monospace slab-serif style

%description -n	iosevka-slab-fonts
Iosevka is a sans-serif + slab-serif, monospace + quasi‑proportional
typeface family, designed for writing code, using in terminals, and
preparing technical documents.

%package -n	iosevka-curly-fonts
Summary:        Iosevka in monospace curly style

%description -n	iosevka-curly-fonts
Iosevka is a sans-serif + slab-serif, monospace + quasi‑proportional
typeface family, designed for writing code, using in terminals, and
preparing technical documents.

%package -n	iosevka-curly-slab-fonts
Summary:        Iosevka in monospace slab-serif curly style

%description -n	iosevka-curly-slab-fonts
Iosevka is a sans-serif + slab-serif, monospace + quasi‑proportional
typeface family, designed for writing code, using in terminals, and
preparing technical documents.

%package -n	iosevka-aile-fonts
Summary:        Iosevka in quasi-proportional sans-serif style

%description -n	iosevka-aile-fonts
Iosevka is a sans-serif + slab-serif, monospace + quasi‑proportional
typeface family, designed for writing code, using in terminals, and
preparing technical documents.

%package -n	iosevka-etoile-fonts
Summary:        Iosevka in quasi-proportional slab-serif style

%description -n	iosevka-etoile-fonts
Iosevka is a sans-serif + slab-serif, monospace + quasi‑proportional
typeface family, designed for writing code, using in terminals, and
preparing technical documents.

%prep
for s in %{_sourcedir}/*.zip; do
	unzip $s '*.ttc'
done
cp %{SOURCE6} %{SOURCE7} .

%build
declare -A family=( \
		[iosevka]=Iosevka \
		[iosevka-slab]=IosevkaSlab \
		[iosevka-curly]=IosevkaCurly \
		[iosevka-curly-slab]=IosevkaCurlySlab \
		[iosevka-aile]=IosevkaAile \
		[iosevka-etoile]=IosevkaEtoile \
		)

declare -A variant=( \
		[bold]=Bold \
		[heavy]=Heavy \
		[light]=Light \
		[medium]=Medium \
		[regular]=Regular \
		[thin]=Thin \
		[extrabold]=Extrabold \
		[extralight]=Extralight \
		[semibold]=Semibold \
		)

for f in ${!family[@]};
do
	for v in ${!variant[@]};
	do
		mv $f-$v.ttc ${family[$f]}-${variant[$v]}.ttc
	done
done

%install
install -d %{buildroot}%{_ttfontsdir}
install -m0644 *.ttc %{buildroot}%{_ttfontsdir}
%reconfigure_fonts_scriptlets

%files
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/Iosevka-*.ttc

%files -n iosevka-slab-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaSlab-*.ttc

%files -n iosevka-curly-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaCurly-*.ttc

%files -n iosevka-curly-slab-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaCurlySlab-*.ttc

%files -n iosevka-aile-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaAile-*.ttc

%files -n iosevka-etoile-fonts
%doc README.md
%license LICENSE.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/IosevkaEtoile-*.ttc

%changelog
