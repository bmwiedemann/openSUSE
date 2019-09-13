#
# spec file for package python-adapt-parser
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-adapt-parser
Version:        0.3.3
Release:        0
Summary:        A text-to-intent parsing framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/MycroftAI/adapt
Source:         https://github.com/MycroftAI/adapt/archive/release/v%{version}.tar.gz
BuildRequires:  %{python_module pyee >= 1.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module unittest-xml-reporting}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyee >= 1.0.1
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
The Adapt Intent Parser is a flexible and extensible intent definition and
determination framework. It is intended to parse natural language text into
a structured intent that can then be invoked programatically.

%prep
%setup -q -n adapt-release-v%{version}
sed -i -s "s/==/>=/" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec run_tests.py --fail-on-error

%files %{python_files}
%license LICENSE.md
%doc README.md SUPPORT.md GETTING_STARTED.md
%{python_sitelib}/*

%changelog
