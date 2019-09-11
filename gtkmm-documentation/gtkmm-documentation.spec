#
# spec file for package gtkmm-documentation
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gtkmm-documentation
Version:        3.24.0
Release:        0
Summary:        C++ Bindings for GTK+ -- Documentation
License:        GFDL-1.2-only AND GPL-2.0-or-later
Group:          Documentation/Other
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/gtkmm-documentation/3.24/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(giomm-2.4) >= 2.50.0
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.24.0
Recommends:     %{name}-lang
BuildArch:      noarch

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm wraps
GTK+. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n gtkmm3-tutorial
Summary:        C++ Bindings for GTK+ -- Tutorial
Group:          Documentation/Other
Requires:       gtkmm3-doc
Supplements:    gtkmm3-doc
Conflicts:      gtkmm2-tutorial
Provides:       %{name} = %{version}
Provides:       gtkmm-tutorial = %{version}
Provides:       gtkmm3-documentation = %{version}

%description -n gtkmm3-tutorial
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm wraps
GTK+. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%lang_package -n gtkmm3-tutorial

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# Drop html version: the docbook version is more than enough
rm -r %{buildroot}%{_datadir}/doc/gtkmm-3.0/tutorial/html
%find_lang gtkmm-tutorial %{?no_lang_C}

%files -n gtkmm3-tutorial
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc %{_datadir}/help/C/gtkmm-tutorial/

%files -n gtkmm3-tutorial-lang -f gtkmm-tutorial.lang

%changelog
