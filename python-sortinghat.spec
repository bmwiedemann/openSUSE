#
# spec file for package python-sortinghat
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
Name:           python-sortinghat
Version:        0.7.7
Release:        0
Summary:        A tool to manage identities
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/grimoirelab/sortinghat
Source0:        https://files.pythonhosted.org/packages/source/s/sortinghat/sortinghat-%{version}.tar.gz
# workaround for https://github.com/chaoss/grimoirelab-sortinghat/issues/121
# reverting https://github.com/chaoss/grimoirelab-sortinghat/commit/5f69ed899c94584de17d47b37152098f64012e10
# plus, test_is_top_domain_invalid_type and test_is_bot_invalid_type tests exception thrown from
# CoerceToBool(), thus disabling
Patch0:         python-sortinghat-gh-121-workaround.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyMySQL >= 0.7.0
Requires:       python-PyYAML >= 3.12
Requires:       python-SQLAlchemy >= 1.2
Requires:       python-pandas >= 0.18.1
Requires:       python-python-dateutil >= 2.6.0
Requires:       python-requests >= 2.9
Requires:       python-urllib3 >= 1.22
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyMySQL >= 0.7.0}
BuildRequires:  %{python_module PyYAML >= 3.12}
BuildRequires:  %{python_module SQLAlchemy >= 1.2}
BuildRequires:  %{python_module httpretty >= 0.9.5}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pandas >= 0.17}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.6.0}
BuildRequires:  %{python_module requests >= 2.9}
BuildRequires:  mariadb-rpm-macros
# /SECTION
%python_subpackages

%description
A tool to manage identities.

Sorting Hat maintains an SQL database with identities coming
(potentially) from different sources. Identities corresponding to the
same real person can be merged in the same unique identity, with a
unique uuid. For each unique identity, a profile can be defined, with
the name and other data to show for the corresponding person by default.

In addition, each unique identity can be related to one or more
affiliations, for different time periods. This will usually correspond
to different organizations in which the person was employed during those
time periods.

Sorting Hat is a part of the GrimoireLab
toolset <https://grimoirelab.github.io>, which provides for Python
modules and scripts to analyze data sources with information about
software development, and allows to produce interactive dashboards to
visualize that information.

In the context of GrimoireLab, Sorting Hat is usually run after data is
retrieved with Perceval <https://github.com/grimmoirelab/perceval>,
to store the identities obtained into its database, and later merge them
into unique identities (and maybe affiliate them).

%prep
%setup -q -n sortinghat-%{version}
%patch0 -p1
sed -i -e "s/\('pandoc'\|'wheel',\)//" -e 's/==/>=/' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/stackalytics2sh
%python_clone -a %{buildroot}%{_bindir}/mozilla2sh
%python_clone -a %{buildroot}%{_bindir}/mailmap2sh
%python_clone -a %{buildroot}%{_bindir}/grimoirelab2sh
%python_clone -a %{buildroot}%{_bindir}/gitdm2sh
%python_clone -a %{buildroot}%{_bindir}/eclipse2sh
%python_clone -a %{buildroot}%{_bindir}/sortinghat
%python_clone -a %{buildroot}%{_bindir}/sh2mg
%python_clone -a %{buildroot}%{_bindir}/mg2sh
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
exit_code=0
user=auth_db_user
pass=auth_db_pass
port=63306
run_dir=/tmp/mysql
#
# start the mariadb server
#
%mysql_testserver_start -u $user -p $pass -t $port
#
# running the test
#
cat << EOF > tests/tests.conf
[Database]
name=testhat
host=127.0.0.1
port=$port
user=$user
password=$pass
create=False
EOF
sed -i -e "s/'3306'/self.kwargs['port']/" tests/test_cmd_init.py
%{python_expand $python setup.py test || exit_code=1}
#
# stopping mariadb
#
%mysql_testserver_stop
exit $exit_code

%post
%python_install_alternative stackalytics2sh
%python_install_alternative mozilla2sh
%python_install_alternative mailmap2sh
%python_install_alternative grimoirelab2sh
%python_install_alternative gitdm2sh
%python_install_alternative eclipse2sh
%python_install_alternative sortinghat
%python_install_alternative sh2mg
%python_install_alternative mg2sh

%postun
%python_uninstall_alternative stackalytics2sh
%python_uninstall_alternative mozilla2sh
%python_uninstall_alternative mailmap2sh
%python_uninstall_alternative grimoirelab2sh
%python_uninstall_alternative gitdm2sh
%python_uninstall_alternative eclipse2sh
%python_uninstall_alternative sortinghat
%python_uninstall_alternative sh2mg
%python_uninstall_alternative mg2sh

%files %{python_files}
%doc NEWS README.md
%python_alternative %{_bindir}/mg2sh
%python_alternative %{_bindir}/sh2mg
%python_alternative %{_bindir}/sortinghat
%python_alternative %{_bindir}/eclipse2sh
%python_alternative %{_bindir}/gitdm2sh
%python_alternative %{_bindir}/grimoirelab2sh
%python_alternative %{_bindir}/mailmap2sh
%python_alternative %{_bindir}/mozilla2sh
%python_alternative %{_bindir}/stackalytics2sh
%{python_sitelib}/*

%changelog
