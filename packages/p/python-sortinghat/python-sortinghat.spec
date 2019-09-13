#
# spec file for package python-sortinghat
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-sortinghat
Version:        0.4.3
Release:        0
Summary:        A tool to manage identities
License:        GPL-3.0-only
Group:          Development/Languages/Python
Url:            https://github.com/grimoirelab/sortinghat
Source:         https://files.pythonhosted.org/packages/source/s/sortinghat/sortinghat-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyMySQL}
BuildRequires:  %{python_module PyYAML >= 3.12}
BuildRequires:  %{python_module SQLAlchemy >= 1.0.0}
BuildRequires:  %{python_module pandas >= 0.17}
BuildRequires:  %{python_module python-dateutil >= 2.6.0}
%endif
BuildRequires:  fdupes
Requires:       python-Jinja2
Requires:       python-PyMySQL
Requires:       python-PyYAML >= 3.12
Requires:       python-SQLAlchemy >= 1.0.0
Requires:       python-pandas >= 0.17
Requires:       python-python-dateutil >= 2.6.0
BuildArch:      noarch

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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc NEWS README.md
%python3_only %{_bindir}/mg2sh
%python3_only %{_bindir}/sh2mg
%python3_only %{_bindir}/sortinghat
%python3_only %{_bindir}/eclipse2sh
%python3_only %{_bindir}/gitdm2sh
%python3_only %{_bindir}/grimoirelab2sh
%python3_only %{_bindir}/mailmap2sh
%python3_only %{_bindir}/mozilla2sh
%python3_only %{_bindir}/stackalytics2sh
%{python_sitelib}/*

%changelog
