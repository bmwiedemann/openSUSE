#
# spec file for package gtk3-branding
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define flavor @BUILD_FLAVOR@
%if "%{flavor}" == ""
%define branding_name %{nil}
ExclusiveArch:  %{nil}
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
ExclusiveArch:  %{nil}
%endif
%endif
%define gtk3_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk3)
%define gtk3_version %(rpm -q --qf '%%{version}' %{gtk3_real_package})
Name:           gtk3-branding%{?dash}%{branding_name}
Version:        15.0
Release:        0
Summary:        The GTK+ toolkit library (version 3) -- %{branding_name} theme configuration
License:        BSD-3-Clause
Group:          System/Libraries
URL:            http://www.gtk.org/
Source:         gtk3-branding-settings.ini
Source1:        gtk3-branding-COPYING
BuildRequires:  gtk3
Requires:       %{gtk3_real_package} = %{gtk3_version}
Requires:       gtk3-metatheme-adwaita
Supplements:    packageand(gtk3:branding-%{branding_name})
Conflicts:      gtk3-branding
Provides:       gtk3-branding = %{gtk3_version}
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
install -d %{buildroot}%{_sysconfdir}/gtk-3.0
install -m0644 settings.ini %{buildroot}%{_sysconfdir}/gtk-3.0/

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/gtk-3.0/settings.ini

%changelog
