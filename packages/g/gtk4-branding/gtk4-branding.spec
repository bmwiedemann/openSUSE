#
# spec file for package gtk4-branding
#
# Copyright (c) 2024 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define branding_name %{nil}
ExclusiveArch:  do-not-build
%else
%define branding_name %{flavor}
%define dash -
%if "%{flavor}" == "SLE"
%define build_SLE 1
%else
%define build_openSUSE 1
%endif
%if (0%{?build_SLE} && 0%{?is_opensuse}) || (0%{?build_openSUSE} && ! 0%{?is_opensuse})
# Don't build SLE branding on openSUSE and vice-versa
ExclusiveArch:  do-not-build
%endif
%endif
%define gtk4_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk4)
%define gtk4_version %(rpm -q --qf '%%{version}' %{gtk4_real_package})
Name:           gtk4-branding%{?dash}%{branding_name}
Version:        15.0
Release:        0
Summary:        The GTK+ toolkit library (version 3) -- %{branding_name} theme configuration
License:        BSD-3-Clause
Group:          System/Libraries
URL:            http://www.gtk.org/
Source:         gtk4-branding-settings.ini
Source1:        gtk4-branding-COPYING
BuildRequires:  gtk4
Requires:       %{gtk4_real_package} = %{gtk4_version}
Supplements:    packageand(gtk4:branding-%{branding_name})
Conflicts:      gtk4-branding
Provides:       gtk4-branding = %{gtk4_version}
BuildArch:      noarch

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{branding_name} theme configuration for
widgets and icon themes.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{SOURCE0} settings.ini
cp -a %{SOURCE1} COPYING

%build

%install
install -d %{buildroot}%{_datadir}/gtk-4.0
install -m0644 settings.ini %{buildroot}%{_datadir}/gtk-4.0/

%files
%license COPYING
%dir %{_datadir}/gtk-4.0
%{_datadir}/gtk-4.0/settings.ini

%changelog
