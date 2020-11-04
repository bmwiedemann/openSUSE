#
# spec file for package dracula-gtk-theme
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dracula-gtk-theme
Version:        2.0+git8.9dde49c
Release:        0
Summary:        A dark theme for GTK
License:        GPL-3.0-only
Url:            https://github.com/dracula/gtk
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch

%description
This is a dark theme for GTK-3 and GTK-2 based desktop environments like
Gnome, XFCE, Mate, Cinnamon, etc. Also provides support for KDE plasma.

%prep
%setup -q -n %{name}-%{version}

# Remove useless stuff
rm -rf \
    ./unity                             \
    ./.github                           \
    ./kde/aurorae/Dracula/.shade.svg    \
    ./kde/sddm/Dracula/faces/.face.icon \
    ./Art                               \
    ./gtk-2.0/render-assets.sh          \
    ./gtk-3.20/assets/render-gtk3-assets-hidpi.py    \
    ./gtk-3.20/assets/render-gtk3-assets.py          \
    ./src

# Fix executable permissions. We don't need this.
chmod -R -x+X .

%build
# Nothing to build

%install
mkdir -p  %{buildroot}%{_datadir}/themes/%{name}
cp -a ./ %{buildroot}%{_datadir}/themes/%{name}/
chmod 0644  %{buildroot}%{_datadir}/themes/%{name}/index.theme

# fix duplicate files
%fdupes -s %{buildroot}/%{_datadir}/themes/

# Remove duplicate documents
rm %{buildroot}%{_datadir}/themes/%{name}/README.md
rm %{buildroot}%{_datadir}/themes/%{name}/LICENSE

%files
%doc README.md 
%license LICENSE
%{_datadir}/themes/%{name}/

%changelog

