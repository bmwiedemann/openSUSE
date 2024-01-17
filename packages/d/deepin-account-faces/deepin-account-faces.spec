#
# spec file for package deepin-account-faces
#
# Copyright (c) 2022 SUSE LLC
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


%define _sharedstatedir /var/lib
%define _name dde-account-faces

Name:           deepin-account-faces
Version:        1.0.12.1
Release:        0
Summary:        Account faces for Linux Deepin
# The debian package (debian subdirectory) is GPL-2.0+
License:        CC0-1.0 AND GPL-2.0-or-later
URL:            https://github.com/linuxdeepin/dde-account-faces
Source0:        %{url}/archive/%{version}/%{_name}-%{version}.tar.gz
Group:          System/GUI/Other
BuildRequires:  accountsservice
BuildRequires:  fdupes
BuildArch:      noarch

%description
Account face icons for Linux Deepin.

%prep
%setup -q -n %{_name}-%{version}

%build

%install
%make_install

%fdupes %{buildroot}

%files
%license LICENSE
%{_sharedstatedir}/AccountsService/icons/*

%changelog
