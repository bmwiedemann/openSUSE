#
# spec file for package mrrescue
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


Name:           mrrescue
Version:        1.02e
Release:        0
Summary:        Arcade-style 2D firefighting action
License:        Zlib AND MIT AND CC-BY-SA-3.0
Group:          Amusements/Games/Action/Other
URL:            http://tangramgames.dk/games/mrrescue/
Source:         https://github.com/SimonLarsen/mrrescue/archive/%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM https://github.com/SimonLarsen/mrrescue/pull/14
Patch1:         appdata.patch
# PATCH-FIX-OPENSUSE support-love-11.patch -- Fixes runtime error on Tumbleweed
Patch2:         support-love-11.patch
BuildRequires:  ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  love >= 0.10.0
BuildRequires:  update-desktop-files
BuildRequires:  zip
Requires:       love >= 0.10.0
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Mr. Rescue is an arcade styled 2d action game centered
around evacuating civilians from burning buildings.

The game features fast paced fire extinguishing action,
intense boss battles, a catchy soundtrack and lots of
throwing people around in pseudo-randomly generated
buildings.

%prep
%setup -q
%patch1 -p1
%if 0%{?suse_version}
%if 0%{?suse_version} > 1500
%patch2 -p1
%endif
%endif

%build
zip -X %{name}_%{version}.love `find -type f | sort` -x LICENSE

%install
cat > %{name} <<-EOF
#!/bin/sh
exec love %{_datadir}/%{name}/%{name}_%{version}.love
EOF

install -D -m 0644 %{name}_%{version}.love %{buildroot}%{_datadir}/%{name}/%{name}_%{version}.love
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

# Install icons and desktop
for size in 256 128 96 64 48 32 16; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps"
    convert -strip data/splash.png -resize "$size"x"$size" %{buildroot}%{_datadir}/icons/hicolor/$size"x$size/apps/%{name}.png"
done

%suse_update_desktop_file -c %{name} "Mr. Rescue" "Arcade 2D Actiongame" %{name} %{name} Game ArcadeGame
install -D -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%dir %{_datadir}/appdata/
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
