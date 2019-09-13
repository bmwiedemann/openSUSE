#
# spec file for package python-Django1
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
%define oldpython python
%if %{python3_version_nodots} > 37
%define skip_python3 1
%endif
Name:           python-Django1
Version:        1.11.23
Release:        0
Summary:        A high-level Python Web framework
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://www.djangoproject.com
Source:         https://www.djangoproject.com/m/releases/1.11/Django-%{version}.tar.gz
Source1:        https://www.djangoproject.com/m/pgp/Django-%{version}.checksum.txt#/Django-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source99:       python-Django1-rpmlintrc
Patch0:         django-sqlite-326.patch
# PATCH-FIX-OPENSUSE bmwiedemann -- fix tests after 2028 - merged in Django master only
Patch2:         fix2028.patch
BuildRequires:  %{python_module Jinja2 >= 2.9.2}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module argon2-cffi >= 16.1.0}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module geoip2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module python-memcached >= 1.59}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlparse}
BuildRequires:  %{python_module tblib}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-pytz
Requires:       python-setuptools
Requires:       python-xml
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-bcrypt
Provides:       python-Django = %{version}
Obsoletes:      python-Django < %{version}
Provides:       python-South = %{version}
Obsoletes:      python-South < %{version}
BuildArch:      noarch
# python-selenium is supported only on the Intel architecture
# Django testsuite runs just fine without, just skips the affected tests
%ifarch %{ix86} x86_64
BuildRequires:  %{python_module selenium}
%endif
%ifpython2
Obsoletes:      %{oldpython}-Django < %{version}
Provides:       %{oldpython}-Django = %{version}
Obsoletes:      %{oldpython}-django < %{version}
Provides:       %{oldpython}-django = %{version}
Obsoletes:      %{oldpython}-South < %{version}
Provides:       %{oldpython}-South = %{version}
%endif
%python_subpackages

%description
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

%prep
# The publisher doesn't sign the source tarball, but a signatures file containing multiple hashes.
# Verify hashes in that file against source tarball.
echo "`grep -e '^[0-9a-f]\{32\}  Django-%{version}.tar.gz' %{SOURCE1} | cut -c1-32`  %{SOURCE0}" | md5sum -c
echo "`grep -e '^[0-9a-f]\{40\}  Django-%{version}.tar.gz' %{SOURCE1} | cut -c1-40`  %{SOURCE0}" | sha1sum -c
echo "`grep -e '^[0-9a-f]\{64\}  Django-%{version}.tar.gz' %{SOURCE1} | cut -c1-64`  %{SOURCE0}" | sha256sum -c

%setup -q -n Django-%{version}
%patch0 -p1
%patch2 -p1

%build
%python_build

%install
%python_install

%python_clone -a %{buildroot}%{_bindir}/django-admin.py
%python_clone -a %{buildroot}%{_bindir}/django-admin

%{python_expand install -D -m 0644 extras/django_bash_completion %{buildroot}%{_datadir}/bash-completion/completions/django_bash_completion-%{$python_bin_suffix}.sh
pushd %{buildroot}%{$python_sitelib}
chmod a-x django/contrib/admin/static/admin/js/vendor/xregexp/xregexp.js
# Fix wrong-script-interpreter
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" django/bin/django-admin.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" django/conf/project_template/manage.py-tpl
%fdupes .
# Deduplicating files can generate a RPMLINT warning for pyc mtime
$python -m compileall -d %{$python_sitelib} django/bin/
$python -O -m compileall -d %{$python_sitelib} django/bin/
$python -m compileall -d %{$python_sitelib} django/conf/project_template/
$python -O -m compileall -d %{$python_sitelib} django/conf/project_template/
$python -m compileall -d %{$python_sitelib} django/conf/locale/
$python -O -m compileall -d %{$python_sitelib} django/conf/locale/
$python -m compileall -d %{$python_sitelib} django/conf/locale/ru/
$python -O -m compileall -d %{$python_sitelib} django/conf/locale/ru/
%fdupes django/bin/
popd
}

%check
export LANG=en_US.UTF8
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests/runtests.py

%post
%{python_install_alternative django-admin.py django-admin}

%preun
%python_uninstall_alternative django-admin

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%python_alternative %{_bindir}/django-admin
%python_alternative %{_bindir}/django-admin.py
%{_datadir}/bash-completion/completions/django_bash_completion-%{python_bin_suffix}.sh
%{python_sitelib}/django
%{python_sitelib}/Django-%{version}-py*.egg-info

%changelog
