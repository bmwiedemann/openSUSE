#
# spec file for package humanity-icon-theme
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


%define _name   Humanity
Name:           humanity-icon-theme
Version:        0.6.16
Release:        0
Summary:        Ayatana Humanity icon theme
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://launchpad.net/humanity
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description
Humanity and Humanity Dark are nice and well polished icon themes for the Gtk
desktop.

%prep
%setup -q
for doc in AUTHORS CONTRIBUTORS COPYING; do
    mv -f %{_name}/$doc .
    rm -f %{_name}-Dark/$doc
done

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/icons/
cp -a {%{_name},%{_name}-Dark} %{buildroot}%{_datadir}/icons/
find -L %{buildroot}%{_datadir}/icons/ -type l -delete
%icon_theme_cache_create_ghost %{_name}
%icon_theme_cache_create_ghost %{_name}-Dark
%fdupes %{buildroot}%{_datadir}/icons/

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post %{_name}
%icon_theme_cache_post %{_name}-Dark

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore.
%endif

%files
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS CONTRIBUTORS
%ghost %{_datadir}/icons/%{_name}*/icon-theme.cache
%{_datadir}/icons/%{_name}*

%changelog
