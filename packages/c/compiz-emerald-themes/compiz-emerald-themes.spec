#
# spec file for package compiz-emerald-themes
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


%define _rev    59fb196746698e41ed0f16988600b216
%define _name   emerald-themes
Name:           compiz-emerald-themes
Version:        0.8.16
Release:        0
Summary:        Various themes for Emerald decorator
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://gitlab.com/compiz/emerald-themes
Source:         https://gitlab.com/compiz/emerald-themes/uploads/%{_rev}/%{_name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  compiz-emerald
BuildRequires:  fdupes
Requires:       compiz-emerald
BuildArch:      noarch

%description
Various themes to be used with Emerald decorator of Compiz
window/compositing manager.

%prep
%setup -q -n %{_name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.bak" -delete -print
%fdupes %{buildroot}%{_datadir}/

%files
%license COPYING*
%doc NEWS README.md
%{_datadir}/emerald/themes/

%changelog
