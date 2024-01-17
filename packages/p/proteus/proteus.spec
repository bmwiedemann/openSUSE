#
# spec file for package proteus
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2014-2021 Dr. Axel Braun
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


%define majorver 6.0
Name:           proteus
Version:        %{majorver}.8
Release:        0
Summary:        A library to access Tryton's modules like a client
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source0:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source1:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
Source2:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python3-defusedxml
BuildRequires:  python3-pip
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  trytond
Requires:       python3-defusedxml
Requires:       python3-python-dateutil
Requires:       trytond
BuildArch:      noarch

%description
Proteus allows you to access Tryton's modules like a client. Useful for automation, data load etc.

%prep
%setup -q

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{python3_sitelib}
python3 -m unittest -v

%files
%defattr(-,root,root)
%doc README.rst
%license LICENSE
%{python3_sitelib}/proteus
%{python3_sitelib}/proteus-%{version}.dist-info

%changelog
