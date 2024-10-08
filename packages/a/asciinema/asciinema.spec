#
# spec file for package asciinema
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


%global pythons python3
Name:           asciinema
Version:        2.4.0
Release:        0
Summary:        Terminal session recorder
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://asciinema.org
Source:         https://github.com/asciinema/asciinema/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.7
BuildArch:      noarch

%description
Record of terminal sessions and sharing them on the web.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

install -Dpm644 {man/,%{buildroot}%{_mandir}/man1/}%{name}.1

rm -R %{buildroot}%{_datadir}/doc/%{name}

%check
%pytest -v

%files
%license LICENSE
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*
%{_mandir}/man?/%{name}.?%{ext_info}

%changelog
