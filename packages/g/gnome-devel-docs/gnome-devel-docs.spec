#
# spec file for package gnome-devel-docs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-devel-docs
Version:        3.32.1
Release:        0
Summary:        GNOME Platform Documentation
License:        GFDL-1.1-only AND CC-BY-SA-4.0
Group:          Documentation/Other
URL:            https://www.gnome.org
Source:         https://download.gnome.org/sources/gnome-devel-docs/3.32/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
Recommends:     %{name}-lang
BuildArch:      noarch

%description
This package contains documents that are useful for GNOME developers.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang accessibility-devel-guide %{?no_lang_C} devel-docs.lang
%find_lang gnome-devel-demos %{no_lang_C} devel-docs.lang
%find_lang hig %{?no_lang_C} devel-docs.lang
%find_lang optimization-guide %{?no_lang_C} devel-docs.lang
%find_lang platform-overview %{?no_lang_C} devel-docs.lang
%find_lang programming-guidelines %{?no_lang_C} devel-docs.lang
%fdupes %{buildroot}

%files
%license COPYING*
%doc AUTHORS ChangeLog NEWS README
%doc %{_datadir}/help/C/accessibility-devel-guide/
%doc %{_datadir}/help/C/gnome-devel-demos/
%doc %{_datadir}/help/C/hig/
%doc %{_datadir}/help/C/optimization-guide/
%doc %{_datadir}/help/C/platform-overview/
%doc %{_datadir}/help/C/programming-guidelines/

%files lang -f devel-docs.lang

%changelog
