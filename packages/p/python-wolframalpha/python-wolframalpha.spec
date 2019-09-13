#
# spec file for package python-wolframalpha
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with test
Name:           python-wolframalpha
Version:        3.0.1
Release:        0
License:        MIT
Summary:        WolframAlpha 2.0 API client
Url:            https://github.com/jaraco/wolframalpha
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/w/wolframalpha/wolframalpha-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm >= 1.9}
%if %{with test}
BuildRequires:  %{python_module jaraco.itertools >= 2.0}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xmltodict}
%endif
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pmxbot}
BuildRequires:  %{python_module pytest >= 2.8}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-jaraco.itertools >= 2.0
Requires:       python-six
Requires:       python-xmltodict
BuildArch:      noarch

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

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
