#
# spec file for package python-wolframalpha
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-wolframalpha
Version:        5.0.0
Release:        0
Summary:        WolframAlpha 2.0 API client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/wolframalpha
Source:         https://files.pythonhosted.org/packages/source/w/wolframalpha/wolframalpha-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 1.9}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.context
Requires:       python-more-itertools
Requires:       python-xmltodict
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jaraco.context}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xmltodict}
# /SECTION
%python_subpackages

%description
Python Client built against the Wolfram|Alpha (http://wolframalpha.com)
v2.0 API.

%prep
%setup -q -n wolframalpha-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# we do not provide python-pmxbot
rm wolframalpha/{test_,}pmxbot.py
%pytest -k 'not test_pmxbot'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
