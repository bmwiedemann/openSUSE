#
# spec file for package gnome-getting-started-docs
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


Name:           gnome-getting-started-docs
Version:        3.34.0
Release:        0
Summary:        Getting started with GNOME - Documentation
License:        CC-BY-SA-3.0
Group:          Documentation/Other
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-getting-started-docs/3.34/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  yelp-tools
Requires:       yelp
Recommends:     %{name}-lang
BuildArch:      noarch

%description
This package contains the Getting Started guide which is packaged and
shipped as gnome-getting-started-docs in the core GNOME distribution.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang gnome-help %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README
%doc %{_datadir}/help/C/gnome-help/

%files lang -f gnome-help.lang

%changelog
