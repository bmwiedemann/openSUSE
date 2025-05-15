#
# spec file for package python-astral
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-astral
Version:        3.2
Release:        0
Summary:        Calculations for the position of the sun and moon
License:        Apache-2.0
URL:            https://github.com/sffjunkie/astral
Source:         https://files.pythonhosted.org/packages/source/a/astral/astral-%{version}.tar.gz
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz
Requires:       python-requests
Recommends:     python-dataclasses
BuildArch:      noarch
%python_subpackages

%description
This is 'astral' a Python module which calculates

* Times for various positions of the sun: dawn, sunrise, solar noon,
  sunset, dusk, solar elevation, solar azimuth and rahukaalam.
* The phase of the moon.

For documentation see the http://astral.readthedocs.io/en/latest/index.html

%prep
%setup -q -n astral-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pytest -m "not webtest"

%files %{python_files}
%doc ReadMe.md
%license LICENSE
%{python_sitelib}/astral
%{python_sitelib}/astral-%{version}*-info

%changelog
