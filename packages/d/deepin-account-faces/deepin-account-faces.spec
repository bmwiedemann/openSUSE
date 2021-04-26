#
# spec file for package deepin-account-faces
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

%define _sharedstatedir /var/lib
%define _name dde-account-faces

Name:           deepin-account-faces
Version:        1.0.11
Release:        0
Summary:        Account faces for Linux Deepin
License:        GPL-2.0+
URL:            https://github.com/linuxdeepin/dde-account-faces
Source0:        https://github.com/linuxdeepin/dde-account-faces/archive/%{version}/%{_name}-%{version}.tar.gz
Group:          System/GUI/Other
BuildRequires:  fdupes
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Account face icons for Linux Deepin.

%prep
%setup -q -n %{_name}-%{version}

%build

%install
%make_install

%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md
%license debian/copyright
%dir %{_sharedstatedir}/AccountsService
%dir %{_sharedstatedir}/AccountsService/icons
%{_sharedstatedir}/AccountsService/icons/*

%changelog
