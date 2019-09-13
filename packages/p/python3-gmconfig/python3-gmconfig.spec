#
# spec file for package python3-gmconfig
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


Name:           python3-gmconfig
Version:        1.0.1
Release:        0
Summary:        JSON based configuration file manager for Python
License:        GPL-3.0+
Group:          Development/Languages/Python
Url:            https://gitlab.com/gabmus/python-gmconfig
Source:         %{name}-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
JSON based configuration file manager for Python 3.x.

%prep
%setup -q

%build
%python3_build

%install
%python3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog

