#
# spec file for package python-Django
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
# Selenium and memcached are not operational
%bcond_with selenium
%bcond_with memcached
Name:           python-Django
# We want support LTS versions of Django -  numbered 2.2 -> 3.2 -> 4.2 etc
Version:        3.1.1
Release:        0
Summary:        A high-level Python Web framework
License:        BSD-3-Clause
URL:            https://www.djangoproject.com
Source:         https://www.djangoproject.com/m/releases/3.1/Django-%{version}.tar.gz
Source1:        https://www.djangoproject.com/m/pgp/Django-%{version}.checksum.txt#/Django-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source99:       python-Django-rpmlintrc
Patch0:         i18n_test.patch
Patch1:         test_clear_site_cache-sort.patch
# PATCH-FIX-OPENSUSE i18n_test_extraction.patch
Patch2:         i18n_test_extraction.patch
BuildRequires:  %{python_module Jinja2 >= 2.9.2}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module argon2-cffi >= 16.1.0}
BuildRequires:  %{python_module asgiref >= 3.2.10}
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module geoip2}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlparse >= 0.2.2}
BuildRequires:  %{python_module tblib}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-Pillow
Requires:       python-argon2-cffi >= 16.1.0
Requires:       python-asgiref >= 3.2.10
Requires:       python-pytz
Requires:       python-setuptools
Requires:       python-sqlparse >= 0.2.2
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-Jinja2 >= 2.9.2
Recommends:     python-PyYAML
Recommends:     python-argon2-cffi >= 16.1.0
Recommends:     python-bcrypt
Recommends:     python-geoip2
Recommends:     python-pylibmc
Recommends:     python-python-memcached >= 1.59
Provides:       python3-django = %{version}
Obsoletes:      python3-django < %{version}
Provides:       python3-South = %{version}
Obsoletes:      python3-South < %{version}
BuildArch:      noarch
%if %{with memcached}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module python-memcached >= 1.59}
%endif
%if %{with selenium}
# python-selenium is supported only on the Intel architecture.
# Additionally chromedriver is only available on x86_64.
%ifarch %{ix86} x86_64
BuildRequires:  %{python_module selenium}
BuildRequires:  chromedriver
BuildRequires:  xvfb-run
%endif
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
%autopatch -p1
chmod a-x django/contrib/admin/static/admin/js/vendor/xregexp/xregexp.js

%build
%python_build

%install
%python_install

%python_clone -a %{buildroot}%{_bindir}/django-admin.py
%python_clone -a %{buildroot}%{_bindir}/django-admin

%{python_expand install -D -m 0644 extras/django_bash_completion %{buildroot}%%{_datadir}/bash-completion/completions/django_bash_completion-%{$python_bin_suffix}.sh
# Fix wrong-script-interpreter
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" \
  %{buildroot}%{$python_sitelib}/django/bin/django-admin.py \
  %{buildroot}%{$python_sitelib}/django/conf/project_template/manage.py-tpl
%fdupes %{buildroot}%{$python_sitelib}/django/
%fdupes %{buildroot}%{$python_sitelib}/Django-%{version}-py*.egg-info/
}

%check
export LANG=en_US.UTF8
export PYTHONDONTWRITEBYTECODE=1
%if %{with selenium}
export PATH=%{_libdir}/chromium:$PATH
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run $python tests/runtests.py -v 2 --selenium=chrome
%else
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests/runtests.py
%endif

%post
%{python_install_alternative django-admin.py django-admin}

%preun
%python_uninstall_alternative django-admin

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%python_alternative %{_bindir}/django-admin
%python_alternative %{_bindir}/django-admin.py
%{_datadir}/bash-completion/completions/django_bash_completion-%{python_bin_suffix}.sh
%{python_sitelib}/django
%{python_sitelib}/Django-%{version}-py*.egg-info

%changelog
