#
# spec file for package gtk2
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

Name:           gtk2-branding%{?dash}%{branding_name}
Version:        15.0
Release:        0
Url:            http://www.gtk.org/
Summary:        The GTK+ toolkit library (version 2) -- %{branding_name} theme configuration
License:        BSD-3-Clause
Group:          System/Libraries
Source:         gtk2-branding-gtkrc
Source1:        gtk2-branding-COPYING
BuildRequires:  gtk2
%define gtk2_real_package %(rpm -q --qf '%%{name}' --whatprovides gtk2)
%define gtk2_version %(rpm -q --qf '%%{version}' %{gtk2_real_package})
Requires:       %{gtk2_real_package} = %{gtk2_version}
Requires:       gtk2-metatheme-adwaita
Provides:       gtk2-branding = %{gtk2_version}
Conflicts:      gtk2-branding
Supplements:    packageand(gtk2:branding-%{branding_name})
BuildArch:      noarch

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the %{branding_name} theme configuration for
widgets and icon themes.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{S:0} gtkrc
cp -a %{S:1} COPYING

%build

%install
install -d %{buildroot}%{_sysconfdir}/gtk-2.0
install -m0644 gtkrc %{buildroot}%{_sysconfdir}/gtk-2.0/

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
%doc COPYING
%config %{_sysconfdir}/gtk-2.0/gtkrc

%changelog
