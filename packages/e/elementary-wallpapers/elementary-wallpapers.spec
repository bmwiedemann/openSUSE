#
# spec file for package elementary-wallpapers
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           elementary-wallpapers
Version:        5.5.0
Release:        0
Summary:        The desktop backgrounds from Pantheon
License:        CC-BY-NC-SA-2.0
Group:          System/GUI/Other
Url:            https://elementary.io/
Source:         https://github.com/elementary/wallpapers/archive/%{version}.tar.gz#/wallpapers-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
Conflicts:      luna-wallpapers
Provides:       pantheon-wallpapers = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# SECTION check:
# brp-25-symlink will break the links with spaces
#!BuildIgnore:	brp-check-suse
# /SECTION

%description
This package contains quality desktop backgrounds assembled by Elementary UX.

%package -n     pantheon-wallpapers-branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(pantheon-wallpapers:branding-upstream)
Conflicts:      otherproviders(pantheon-wallpapers-branding)
Provides:       pantheon-wallpapers-branding = %{version}

%description -n pantheon-wallpapers-branding-upstream
This package provides the default wallpaper in Elementary OS.

%prep
%setup -q -n wallpapers-%{version}

%build
%meson
%meson_build

%install
%meson_install

# NOTE: cat switchboard-plug-pantheon-shell.spec
rm -f %{buildroot}%{_datadir}/backgrounds/elementaryos-default
mv elementaryos-default %{buildroot}%{_datadir}/backgrounds/default-wallpaper

%fdupes -s %{buildroot}%{_datadir}

%files
%defattr(-,root,root)
%doc README.md
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/*.jpg
%{_datadir}/metainfo/io.elementary.wallpapers.appdata.xml

%files -n pantheon-wallpapers-branding-upstream
%{_datadir}/backgrounds/default-wallpaper

%changelog
