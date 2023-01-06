#
# spec file for package orca
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


Name:           orca
Version:        43.1
Release:        0
Summary:        Screen reader for GNOME
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/Orca
Source0:        https://download.gnome.org/sources/orca/43/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  liblouis-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.3
BuildRequires:  python3-brlapi >= 0.5.1
BuildRequires:  python3-gobject >= 3.18
BuildRequires:  python3-louis
BuildRequires:  python3-speechd
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atk-bridge-2.0) >= 2.18
BuildRequires:  pkgconfig(atspi-2) >= 2.18
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.18
# the gsettings tool is used to know if a11y is enabled
Requires:       glib2-tools
# pyatspi is a virtual name that is provided by the default at-spi stack
Requires:       py3atspi
Requires:       python3-brlapi
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-louis
Requires:       python3-speechd
Recommends:     brltty >= 3.9
BuildArch:      noarch

%description
Orca is an extensible screen reader that provides access to the
graphical desktop via user-customizable combinations of speech,
braille, and/or magnification.

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/orca
%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
%{_datadir}/icons/hicolor/*/apps/orca*
%{_datadir}/orca/
%{_mandir}/man1/orca.1%{?ext_man}
%{python3_sitelib}/orca/

%files lang -f %{name}.lang

%changelog
