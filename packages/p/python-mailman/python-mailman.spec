#
# spec file for package python-mailman
#
# Copyright (c) 2020 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-mailman%{psuffix}
Version:        3.3.0
Release:        0
Summary:        Mailman -- the GNU mailing list manager
License:        GPL-3.0-only
URL:            https://www.list.org
Source:         https://files.pythonhosted.org/packages/source/m/mailman/mailman-%{version}.tar.gz
# whitespace fix
Patch0:         python-mailman-test_interact_default_banner.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiosmtpd >= 1.1
Requires:       python-alembic
Requires:       python-atpublic
Requires:       python-authheaders >= 0.9.2
Requires:       python-authres >= 1.0.1
Requires:       python-click >= 7.0
Requires:       python-dnspython >= 1.14.0
Requires:       python-falcon > 1.0.0
Requires:       python-flufl.bounce
Requires:       python-flufl.i18n >= 2.0
Requires:       python-flufl.lock >= 3.1
Requires:       python-gunicorn
Requires:       python-lazr.config
Requires:       python-passlib
Requires:       python-python-dateutil >= 2.0
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-sqlalchemy >= 1.2.3
Requires:       python-zope.component
Requires:       python-zope.configuration
Requires:       python-zope.event
Requires:       python-zope.interface
%if 0%{?suse_version} <= 1500
Requires:       python-cffi
Requires:       python-importlib_resources
%endif
Provides:       mailman = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aiosmtpd >= 1.1}
BuildRequires:  %{python_module alembic}
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module authheaders >= 0.9.2}
BuildRequires:  %{python_module authres >= 1.0.1}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module dnspython >= 1.14.0}
BuildRequires:  %{python_module falcon > 1.0.0}
BuildRequires:  %{python_module flufl.bounce}
BuildRequires:  %{python_module flufl.i18n >= 2.0}
BuildRequires:  %{python_module flufl.lock >= 3.1}
BuildRequires:  %{python_module flufl.testing}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module lazr.config}
BuildRequires:  %{python_module mailman >= %{version}}
BuildRequires:  %{python_module nose2}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.0}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sqlalchemy >= 1.2.3}
BuildRequires:  %{python_module zope.component}
BuildRequires:  %{python_module zope.configuration}
BuildRequires:  %{python_module zope.event}
BuildRequires:  %{python_module zope.interface}
%if 0%{?suse_version} <= 1500
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module importlib_resources}
%endif
%endif
%python_subpackages

%description
Mailman -- the GNU mailing list manager

%prep
%setup -q -n mailman-%{version}
%patch0 -p1

%build
sed -i 's:/sbin:%{_prefix}/bin:' src/mailman/config/mailman.cfg
%if 0%{?suse_version} > 1500
pushd src/mailman
for i in $(grep -r '^from importlib_resources' | sed 's/\(.*\.py\):.*/\1/'); do
  line=$(grep '^from importlib_resources' $i)
  what_import=$(echo $line | sed 's:.* import ::')
  sed -i "s@^\(from importlib_resources.*\)@try:\n  from importlib.resources import $what_import\nexcept ImportError:\n    \1\n@" $i;
done
popd
sed '/importlib_resources/d' -i src/mailman.egg-info/requires.txt setup.py
%endif
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%if 0%{?suse_version} <= 1500
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
# mailman.rest.tests.test_wsgiapp.TestSupportedContentType
# AssertionError: 'application/json; charset=UTF-8' != 'application/json'
rm src/mailman/rest/tests/test_wsgiapp.py
%endif
# doctest fails miserably
find -name '*.rst' -exec rm {} \;
# used to have ports 902{4,5}
rm src/mailman/mta/tests/test_aliases.py
# PermissionError: [Errno 13] Permission denied: '/usr/bin/master'
rm src/mailman/core/tests/test_logging.py
# PermissionError: [Errno 13] Permission denied: '/usr/bin/master'
rm src/mailman/commands/tests/test_cli_control.py
# https://gitlab.com/mailman/mailman/issues/654
rm src/mailman/commands/tests/test_cli_create.py
# do not use well known ports 9024 and 9025
sed -i "s:\(902\):4\1:" src/mailman/testing/testing.cfg
#
%python_exec -m nose2 -v
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license COPYING
%python3_only %{_bindir}/runner
%python3_only %{_bindir}/mailman
%python3_only %{_bindir}/master
%{python_sitelib}/*
%endif

%changelog
