#
# spec file for package gnome-user-docs
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gnome-user-docs
Version:        3.36.6
Release:        0
Summary:        GNOME Desktop Documentation
License:        CC-BY-3.0
Group:          Documentation/Other
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-user-docs/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  yelp-tools
Requires:       yelp
Supplements:    gnome-session
BuildArch:      noarch

%description
This package contains documents that are targeted for GNOME end-users.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang gnome-help %{?no_lang_C}
%find_lang system-admin-guide %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS README
%doc %{_datadir}/help/C/gnome-help/
%doc %{_datadir}/help/C/system-admin-guide/

%files lang -f gnome-help.lang -f system-admin-guide.lang

%changelog
