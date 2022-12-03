#
# spec file for package python-sortinghat
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


%define binaries stackalytics2sh mozilla2sh mailmap2sh grimoirelab2sh gitdm2sh eclipse2sh sortinghat sh2mg mg2sh
%define skip_python2 1
%define skip_python36 1
Name:           python-sortinghat
Version:        0.7.23
Release:        0
Summary:        A tool to manage identities
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/grimoirelab/sortinghat
Source0:        https://files.pythonhosted.org/packages/source/s/sortinghat/sortinghat-%{version}.tar.gz
# PATCH-FIX-UPSTREAM no_decl_class_registry.patch gh#chaoss/grimoirelab-sortinghat#579 mcepl@suse.com
# make the package compatible with SQLAlchemy 1.4.*
Patch0:         no_decl_class_registry.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 3.0.1
Requires:       python-PyMySQL >= 0.7.0
Requires:       python-PyYAML >= 3.12
Requires:       python-SQLAlchemy >= 1.2
Requires:       python-pandas >= 0.18.1
Requires:       python-python-dateutil >= 2.6.0
Requires:       python-requests >= 2.9
Requires:       python-urllib3 >= 1.22
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyMySQL >= 0.7.0}
BuildRequires:  %{python_module PyYAML >= 3.12}
BuildRequires:  %{python_module SQLAlchemy >= 1.2}
BuildRequires:  %{python_module httpretty >= 0.9.5}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas >= 0.25.3}
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
%autosetup -p1 -n sortinghat-%{version}

sed -i -e "s/\('pandoc'\|'wheel',\)//" -e 's/==/>=/' setup.py

%build
%pyproject_wheel
%{python_expand sed -i -e '1s@/usr/bin/.*python.*$@%{$__python}@' \
    sortinghat/misc/*.py sortinghat/bin/*.py
}

%install
%pyproject_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%{python_expand rm -r %{buildroot}%{$python_sitelib}/sortinghat/{bin,misc}
%fdupes %{buildroot}%{$python_sitelib}
}

%check
exit_code=0
user=auth_db_user
pass=auth_db_pass
port=63306
dbname=testhat
run_dir=/tmp/mysql
#
# start the mariadb server
#
%mysql_testserver_start -u $user -p $pass -t $port -d $dbname
#
# running the test
#
# this is read by TestDatabaseCaseBase.setUpClass
cat << EOF > tests/tests.conf
[Database]
name=$dbname
host=127.0.0.1
port=$port
user=$user
password=$pass
create=False
EOF
sed -i -e "s/'3306'/self.kwargs['port']/" tests/test_cmd_init.py
%pyunittest discover -b -v || exit_code=1
#
# stopping mariadb
#
%mysql_testserver_stop
exit $exit_code

%post
for b in mg2sh sh2mg sortinghat eclipse2sh gitdm2sh grimoirelab2sh mailmap2sh mozilla2sh stackalytics2sh; do
  %python_install_alternative $b
done

%postun
for b in mg2sh sh2mg sortinghat eclipse2sh gitdm2sh grimoirelab2sh mailmap2sh mozilla2sh stackalytics2sh; do
  %python_uninstall_alternative $b
done

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
%{python_sitelib}/sortinghat
%{python_sitelib}/sortinghat-%{version}*-info

%changelog
