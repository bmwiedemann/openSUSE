#
# spec file
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


# Upstream also supports shimming python2.7, but we assume Python >= 3.6 here (if 15.3 were resolvable for the python3 flavor)
%global skip_python2 1
%define modname pytz-deprecation-shim
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        0.1.0.post0
Release:        0
Summary:        Shims to make deprecation of pytz easier
License:        Apache-2.0
URL:            https://github.com/pganssle/pytz-deprecation-shim
Source:         https://files.pythonhosted.org/packages/source/p/pytz_deprecation_shim/pytz_deprecation_shim-%{version}.tar.gz
BuildRequires:  %{python_module backports.zoneinfo if %python-base < 3.9}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 39
Requires:       python-backports.zoneinfo
%endif
BuildArch:      noarch
%python_subpackages

%description
pytz has served the Python community well for many years, but it is no longer
the best option for providing time zones. pytz has a non-standard interface
that is very easy to misuse; this interface was necessary when pytz was
created, because datetime had no way to represent ambiguous datetimes, but this
was solved in in Python 3.6, which added a fold attribute to datetimes in PEP
495. With the addition of the zoneinfo module in Python 3.9 (PEP 615), there
has never been a better time to migrate away from pytz.

However, since pytz time zones are used very differently from a standard
tzinfo, and many libraries have built pytz zones into their standard time zone
interface (and thus may have users relying on the existence of the localize and
normalize methods); this library provides shim classes that are compatible with
both PEP 495 and pytz’s interface, to make it easier for libraries to deprecate
pytz.

%prep
%setup -q -n pytz_deprecation_shim-%{version}
# assume that we have tzdata from the system and never need the PyPI package
sed -i '/tzdata/ d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/pytz_deprecation_shim
%{python_sitelib}/pytz_deprecation_shim-%{version}*-info

%changelog
