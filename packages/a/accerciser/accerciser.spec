#
# spec file for package accerciser
#
# Copyright (c) 2019 SUSE LLC
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


Name:           accerciser
Version:        3.34.2
Release:        0
Summary:        Accessibility debugging tool
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Accerciser
Source0:        https://download.gnome.org/sources/accerciser/3.34/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  pkgconfig
# py3atspi is a virtual name that is provided by the default at-spi stack
BuildRequires:  py3atspi
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atspi-2) >= 2.5.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.1.13
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.3
# py3atspi is a virtual name that is provided by the default at-spi stack
Requires:       py3atspi
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang
BuildArch:      noarch

%description
Accerciser is an interactive Python accessibility explorer for the
GNOME desktop. It uses AT-SPI to inspect and control widgets, allowing
you to check if an application is providing correct information to
assistive technologies and automated test frameworks. Accerciser has a
simple plugin framework which you can use to create custom views of
accessibility information.

In essence, Accerciser is a next generation at-poke tool.

%package plugin-IPython
Summary:        Accessibility debugging tool - IPython console widget
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
Requires:       python3-ipython
# we need setuptools for pkg_resources
Requires:       python3-setuptools
Supplements:    packageand(%{name}:python3-ipython)

%description plugin-IPython
Accerciser is an interactive Python accessibility explorer for the
GNOME desktop.

This package provides the IPython console widget

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%configure \
	%{nil}
%make_build

%install
%make_install
%suse_update_desktop_file -r -N "Accerciser" -G "Accesibility Debugger" accerciser Utility GNOME Accessibility
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/plugins/ipython_view.py
%{_datadir}/metainfo/accerciser.appdata.xml
%{_datadir}/glib-2.0/schemas/org.a11y.Accerciser.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{ext_man}
%{python3_sitelib}/%{name}/

%files plugin-IPython
%{_datadir}/%{name}/plugins/ipython_view.py

%files lang -f %{name}.lang

%changelog
