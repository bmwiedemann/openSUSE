#
# spec file for package deepin-gtk-theme
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           deepin-gtk-theme
Version:        17.10.11
Release:        0
Summary:        Deepin Style GTK Theme
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/deepin-gtk-theme
Source0:        https://github.com/linuxdeepin/deepin-gtk-theme/archive/%{version}/%{name}-%{version}.tar.gz
Group:          System/GUI/Other
BuildRequires:  fdupes
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains GTK+ themes for Deepin Desktop Environment.

%prep
%setup -q

%build

%install
%make_install PREFIX=%{_prefix}

#Fix Permission
chmod -x %{buildroot}%{_datadir}/themes/*/gtk-3.0/*.css

%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%{_datadir}/themes/deepin/
%{_datadir}/themes/deepin-dark/

%changelog
