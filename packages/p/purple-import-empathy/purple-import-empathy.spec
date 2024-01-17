#
# spec file for package purple-import-empathy
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define plugname import-empathy
Name:           purple-import-empathy
Version:        0.1.0
Release:        0
Summary:        Empathy importer plugin for libpurple
License:        GPL-3.0+
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/FelixZhang/purple-import-empathy
Source:         https://github.com/FelixZhang/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(purple)

%description
Empathy importer plugin for libpurple.

%package -n libpurple-plugin-%{plugname}
Summary:        Empathy importer plugin for libpurple
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple

%description -n libpurple-plugin-%{plugname}
Empathy importer plugin for libpurple

%prep
%setup -q

%build
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files -n libpurple-plugin-%{plugname}
%doc LICENSE README.md
%{_libdir}/purple-2/import-empathy.so

%changelog
