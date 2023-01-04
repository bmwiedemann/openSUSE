#
# spec file for package python-pytz
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


# Ensure you update the tzdata_version for any minor version increase
# otherwise the update python library has the incorrect timezone data.
%define tzdata_version 2022g
%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?!pyunittest:%define pyunittest(+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-=) \\\
    %{lua: local args = rpm.expand("%**");
           local broot = rpm.expand("%buildroot");
           local intro = "%{python_expand PYTHONPATH=${PYTHONPATH:+$PYTHONPATH:}" .. broot .. "%{$python_sitelib} PYTHONDONTWRITEBYTECODE=1 $python -m unittest ";
           print(rpm.expand(intro .. args .. "}"))
    } }

Name:           python-pytz
Version:        2022.7
Release:        0
Summary:        World timezone definitions, modern and historical
License:        MIT
Group:          Development/Languages/Python
URL:            https://pythonhosted.org/pytz/
Source:         https://files.pythonhosted.org/packages/source/p/pytz/pytz-%{version}.tar.gz
Source2:        https://files.pythonhosted.org/packages/source/p/pytz/pytz-%{version}.tar.gz.asc
Source90:       %{name}.keyring
# PATCH-FIX-UPSTREAM fix-tests.patch -- Remote tests which are known to be broken
Patch0:         fix-tests.patch
# PATCH-FIX-UPSTREAM 0001-Fix-tests-for-older-timezone-versions.patch -- https://code.launchpad.net/~toabctl/pytz/+git/pytz/+merge/326419
Patch2:         0001-Fix-tests-for-older-timezone-versions.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  timezone >= %{tzdata_version}
Requires:       python-base
Requires:       timezone >= %{tzdata_version}
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-tz = %{version}
Obsoletes:      %{oldpython}-tz < %{version}
%endif
%python_subpackages

%description
pytz - World Timezone Definitions for Python
pytz brings the Olson tz database into Python. This library allows
accurate and cross platform timezone calculations using Python 2.4
or higher. It also solves the issue of ambiguous times at the end
of daylight savings, which you can read more about in the Python
Library Reference (``datetime.tzinfo``).

Amost all of the Olson timezones are supported.

%prep
%setup -q -n pytz-%{version}
%autopatch -p1

# For rpmlint warning: remove shebang from python library:
sed -i '/^#!/d' ./pytz/tzfile.py

# Help Python 2.7 unittest
touch pytz/tests/__init__.py

%build
%python_build

%install
%python_install
# Replace custom data with symlink to /usr/share/zoneinfo
%{python_expand rm -r %{buildroot}%{$python_sitelib}/pytz/zoneinfo
ln -s %{_datadir}/zoneinfo %{buildroot}%{$python_sitelib}/pytz/zoneinfo
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pyunittest discover -v

%pre
if [ $1 -gt 1 ] ; then
[ "$(readlink -e %{python_sitelib}/pytz/zoneinfo)" = "%{python_sitelib}/pytz/zoneinfo" ] && rm -rf %{python_sitelib}/pytz/zoneinfo
fi || :

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/pytz
%{python_sitelib}/pytz-%{version}-py*.egg-info

%changelog
