#
# spec file for package gnome-icon-theme-extras
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gnome-icon-theme-extras
Version:        3.12.0
Release:        0
Summary:        GNOME Icon Theme Extras
License:        CC-BY-SA-3.0
Group:          System/GUI/GNOME
Url:            http://www.gnome.org/
Source:         http://download.gnome.org/sources/gnome-icon-theme-extras/3.12/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gnome-icon-theme
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils-devel >= 0.8.7
BuildRequires:  pkg-config
Requires:       gnome-icon-theme
Supplements:    gnome-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Extra GNOME icons for specific devices and file types.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}

%clean
rm -rf %{buildroot}

%post
%icon_theme_cache_post gnome

%postun
%icon_theme_cache_postun gnome

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_datadir}/icons/gnome/*/*/*

%changelog
