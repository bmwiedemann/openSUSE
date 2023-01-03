#
# spec file for package sacad
#
# Copyright (c) 2023 SUSE LLC
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


Name:           sacad
Version:        2.7.3
Release:        0
Summary:        Search and download music album covers
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/desbma/sacad
Source:         https://github.com/desbma/sacad/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-Pillow >= 2.7.0
Requires:       python3-Unidecode >= 1.1.1
Requires:       python3-aiohttp >= 3.6
Requires:       python3-appdirs >= 1.4.0
Requires:       python3-bitarray >= 0.8.3
Requires:       python3-cssselect >= 0.9.1
Requires:       python3-fake-useragent >= 0.1.11
Requires:       python3-lxml >= 4.0.0
Requires:       python3-mutagen >= 1.31
Requires:       python3-tqdm >= 4.28.1
Requires:       python3-web_cache >= 1.1.0
BuildArch:      noarch

%description
SACAD is a multi platform command line tool to download album covers
without manual intervention, ideal for integration in scripts, audio
players, etc.

%prep
%setup -q -n sacad-%{version}

%build
%python3_build

%install
%python3_install
find %{buildroot}/%{python3_sitelib}/sacad/ -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
%fdupes %{buildroot}/%{python3_sitelib}

#%%check
# disabled - tests require an internet connection

%files
%license LICENSE
%doc README.md
%{_bindir}/sacad
%{_bindir}/sacad_r
%{python3_sitelib}/sacad*

%changelog
