#
# spec file for package gtkmm-documentation
#
# Copyright (c) 2023 SUSE LLC
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
Version:        4.0.3
Release:        0
Summary:        C++ Bindings for GTK+ -- Documentation
License:        GFDL-1.2-only AND GPL-2.0-or-later
Group:          Documentation/Other
URL:            https://gtkmm.org
Source0:        https://download.gnome.org/sources/gtkmm-documentation/4.0/%{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc

BuildRequires:  c++_compiler
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(giomm-2.68) >= 2.68.0
BuildRequires:  pkgconfig(gtkmm-4.0) >= 4.0.0
BuildArch:      noarch

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm wraps
GTK+. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n gtkmm4-tutorial
Summary:        C++ Bindings for GTK+ -- Tutorial
Group:          Documentation/Other
Requires:       gtkmm4-doc
Supplements:    gtkmm4-doc
Conflicts:      gtkmm2-tutorial
Conflicts:      gtkmm3-tutorial
Obsoletes:      gtkmm3-tutorial < 3.97.1
Obsoletes:      gtkmm3-tutorial-lang < 3.97.1
Provides:       %{name} = %{version}
Provides:       gtkmm-tutorial = %{version}
Provides:       gtkmm4-documentation = %{version}

%description -n gtkmm4-tutorial
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm wraps
GTK+. Highlights include typesafe callbacks, widgets extensible via
inheritance, and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%lang_package -n gtkmm4-tutorial

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

# Drop html version: the docbook version is more than enough
rm -r %{buildroot}%{_datadir}/doc/gtkmm-4.0/tutorial/html
%find_lang gtkmm-tutorial %{?no_lang_C}

%files -n gtkmm4-tutorial
%license COPYING
%doc AUTHORS ChangeLog NEWS README.md
%{_datadir}/help/C/gtkmm-tutorial/

%files -n gtkmm4-tutorial-lang -f gtkmm-tutorial.lang

%changelog
