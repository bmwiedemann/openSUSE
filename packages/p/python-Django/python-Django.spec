#
# spec file for package python-Django
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


# Selenium and memcached are not operational
%bcond_with selenium
%bcond_with memcached
%{?sle15_python_module_pythons}
Name:           python-Django
Version:        5.1.5
Release:        0
Summary:        A high-level Python Web framework
License:        BSD-3-Clause
URL:            https://www.djangoproject.com
Source:         https://www.djangoproject.com/m/releases/5.1/Django-%{version}.tar.gz
Source1:        https://media.djangoproject.com/pgp/Django-%{version}.checksum.txt
Source2:        %{name}.keyring
Source99:       python-Django-rpmlintrc
BuildRequires:  %{python_module Jinja2 >= 2.9.2}
BuildRequires:  %{python_module Pillow >= 6.2.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module argon2-cffi >= 19.1.0}
BuildRequires:  %{python_module asgiref >= 3.7.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module geoip2}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlparse >= 0.3.1}
BuildRequires:  %{python_module tblib >= 1.5.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  gpg2
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-Pillow >= 6.2.0
Requires:       python-asgiref >= 3.7.0
Requires:       python-sqlparse >= 0.3.1
Requires:       python-tzdata
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-Jinja2 >= 2.9.2
Recommends:     python-PyYAML
Recommends:     python-argon2-cffi >= 19.1.0
Recommends:     python-bcrypt
Recommends:     python-geoip2
Recommends:     python-pylibmc
Recommends:     python-pymemcache
Provides:       python-django = %{version}
Obsoletes:      python-django < %{version}
Provides:       python-South = %{version}
Obsoletes:      python-South < %{version}
BuildArch:      noarch
%if %{with memcached}
BuildRequires:  %{python_module pylibmc}
BuildRequires:  %{python_module pymemcache}
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
# The publisher doesn't sign the source tarball, but a signatures file
# containing multiple hashes.
gpg --import %{SOURCE2}
gpg --verify %{SOURCE1}
#
# Verify hashes in that file against source tarball.
echo "`grep -e '^[0-9a-f]\{32\}  Django-%{version}.tar.gz' %{SOURCE1} | cut -c1-32`  %{SOURCE0}" | md5sum -c
echo "`grep -e '^[0-9a-f]\{40\}  Django-%{version}.tar.gz' %{SOURCE1} | cut -c1-40`  %{SOURCE0}" | sha1sum -c
echo "`grep -e '^[0-9a-f]\{64\}  Django-%{version}.tar.gz' %{SOURCE1} | cut -c1-64`  %{SOURCE0}" | sha256sum -c

%autosetup -p1 -n Django-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%python_clone -a %{buildroot}%{_bindir}/django-admin

%{python_expand install -D -m 0644 extras/django_bash_completion %{buildroot}%%{_datadir}/bash-completion/completions/django_bash_completion-%{$python_bin_suffix}.sh
# Fix wrong-script-interpreter
sed -i "s|^#!%{_bindir}/env python$|#!%{_bindir}/$python|" \
  %{buildroot}%{$python_sitelib}/django/conf/project_template/manage.py-tpl
}
%python_compileall
%{python_expand #
%fdupes %{buildroot}%{$python_sitelib}/django/
%fdupes %{buildroot}%{$python_sitelib}/Django-%{version}-py*.egg-info/
}

%check
export LANG=en_US.UTF8
export PYTHONDONTWRITEBYTECODE=1
%if %{with selenium}
export PATH=%{_libdir}/chromium:$PATH
%python_expand PYTHONPATH=.:%{buildroot}%{$python_sitelib} xvfb-run $python tests/runtests.py -v 2 --selenium=chrome
%else
%python_expand PYTHONPATH=.:%{buildroot}%{$python_sitelib} $python tests/runtests.py -v 2
%endif

%post
%{python_install_alternative django-admin}

%postun
%{python_uninstall_alternative django-admin}

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%python_alternative %{_bindir}/django-admin
%{_datadir}/bash-completion/completions/django_bash_completion-%{python_bin_suffix}.sh
%{python_sitelib}/django
%{python_sitelib}/Django-%{version}*-info

%changelog
