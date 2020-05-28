#
# spec file for package jc
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           jc
Version:        1.11.1
Release:        0
Summary:        JSON CLI output utility
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/kellyjonbrazil/jc
Source:         https://github.com/kellyjonbrazil/jc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-Pygments >= 2.4.2
Requires:       python3-ifconfig-parser >= 0.0.5
Requires:       python3-ruamel.yaml >= 0.15.0
Requires:       python3-xmltodict >= 0.12.0
Recommends:     jq
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-Pygments >= 2.4.2
BuildRequires:  python3-ifconfig-parser >= 0.0.5
BuildRequires:  python3-pytest
BuildRequires:  python3-ruamel.yaml >= 0.15.0
BuildRequires:  python3-xmltodict >= 0.12.0
# /SECTION

%description
jc is used to JSONify the output of many standard linux cli tools
and file types for easier parsing in scripts.

%prep
%setup -q

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%check
python3 -m pytest -v

%files
%license LICENSE.md
%doc changelog.txt README.md
%{_bindir}/jc
%{python3_sitelib}/jc*

%changelog
