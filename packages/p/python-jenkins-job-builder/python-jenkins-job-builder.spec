#
# spec file for package python-jenkins-job-builder
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Thomas Bechtold <thomasbechtold@jpberlin.de>
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
Name:           python-jenkins-job-builder
Version:        3.0.2
Release:        0
Summary:        Program for configuring Jenkins jobs with YAML
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://opendev.org/jjb/jenkins-job-builder
Source:         https://files.pythonhosted.org/packages/source/j/jenkins-job-builder/jenkins-job-builder-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML >= 3.10.0}
BuildRequires:  %{python_module fasteners}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pbr >= 1.8}
BuildRequires:  %{python_module python-jenkins >= 0.4.15}
BuildRequires:  %{python_module setuptools-git}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module stevedore >= 1.17.1}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyYAML >= 3.10.0
Requires:       python-fasteners
Requires:       python-pbr >= 1.8
Requires:       python-python-jenkins >= 0.4.15
Requires:       python-setuptools
Requires:       python-six >= 1.9.0
Requires:       python-stevedore >= 1.17.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Jenkins Job Builder takes simple descriptions of Jenkins jobs in YAML format,
and uses them to configure Jenkins. You can keep your job descriptions in human
readable text format in a version control system to make changes and auditing
easier. It also has a flexible template system, so creating many similarly
configured jobs is easy.

%prep
%setup -q -n jenkins-job-builder-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/jenkins-jobs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m stestr.cli run

%post
%python_install_alternative jenkins-jobs

%preun
%python_uninstall_alternative jenkins-jobs

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/jenkins-jobs

%changelog
