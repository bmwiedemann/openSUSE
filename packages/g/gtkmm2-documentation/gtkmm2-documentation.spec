#
# spec file for package gtkmm2-documentation
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


%define _name   gtkmm-documentation
Name:           gtkmm2-documentation
Version:        2.24.1
Release:        0
Summary:        C++ Bindings for GTK+ -- Documentation
License:        GFDL-1.2-only AND GPL-2.0-or-later
Group:          Documentation/Other
URL:            http://www.gnome.org
Source:         %{_name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gtkmm-2.4)
Recommends:     %{name}-lang
BuildArch:      noarch

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm wraps
GTK+. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n gtkmm2-tutorial
Summary:        C++ Bindings for GTK+ -- Tutorial
Group:          Documentation/Other
Requires:       gtkmm2-doc
Supplements:    gtkmm2-doc
Conflicts:      gtkmm3-tutorial
Provides:       %{name} = %{version}

%description -n gtkmm2-tutorial
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm wraps
GTK+. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%lang_package -n gtkmm2-tutorial

%prep
%setup -q -n %{_name}-%{version}

%build
%configure\
	--disable-scrollkeeper
make %{?_smp_mflags}

%install
%make_install
# Drop html version: the docbook version is more than enough
rm -r %{buildroot}%{_datadir}/doc/gtkmm-2.4/tutorial/html
mv %{buildroot}/%{_datadir}/gnome/help/gtkmm-tutorial/ %{buildroot}/%{_datadir}/gnome/help/gtkmm-tutorial2/

%files -n gtkmm2-tutorial
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/gtkmm-tutorial2/
%doc %{_datadir}/gnome/help/gtkmm-tutorial2/C/

%files -n gtkmm2-tutorial-lang
%doc %{_datadir}/gnome/help/gtkmm-tutorial2/de/
%doc %{_datadir}/gnome/help/gtkmm-tutorial2/es/

%changelog
