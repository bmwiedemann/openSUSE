#
# spec file for package python-md2workflow
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
Name:           python-md2workflow
Version:        1.4.18
Release:        0
Summary:        Tool to create a JIRA or other Workflow from markdown files
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/openSUSE/md2workflow
Source:         https://github.com/openSUSE/md2workflow/archive/%{version}.tar.gz
Source1:        LICENSE
Source2:        suse-prod.conf
Source3:        suse-devel.conf
Source6:        opensuse-prod.conf
BuildRequires:  %{python_module icalendar}
BuildRequires:  %{python_module jira}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-redmine}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-icalendar
Requires:       python-md2workflow-common
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython3
Provides:       md2workfow = %{version}
%endif
%python_subpackages

%description
A tool which can convert typically "VCS managed" mardown checklist
into e.g. a linked structure of Jira Epics. This tool can not only
create checklists, but also update them.

%package -n python-md2workflow-common
Summary:        Configuration and examples for md2workflow
Group:          Development/Languages/Python
Provides:       %{python_module md2workflow-common = %{version}}

%description -n python-md2workflow-common
Configuration and examples for md2workflow

%package 	plugins-jira
Summary:        Jira plugin for md2workflow
Group:          Development/Languages/Python
Requires:       python-jira
Requires:       python-md2workflow = %{version}

%description 	plugins-jira
Jira plugin for md2workflow

%package 	plugins-redmine
Summary:        Redmine plugin for md2workflow
Group:          Development/Languages/Python
Requires:       python-md2workflow = %{version}
Requires:       python-python-redmine

%description 	plugins-redmine
Redmine plugin for md2workflow

%prep

%setup -q -n md2workflow-%{version}
echo `pwd`
cp %{_sourcedir}/{suse-prod,suse-devel,opensuse-prod}.conf  config/
cp %{_sourcedir}/LICENSE LICENSE

%build
%python_build

%check
%pytest

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/md2workflow
%python_expand %fdupes %{buildroot}%{$python_sitelib}
ln -s -f %{_datadir}/md2workflow/config %{buildroot}%{_sysconfdir}/md2workflow

%post
%python_install_alternative md2workflow

%postun
%python_uninstall_alternative md2workflow

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/md2workflow
%if "%{python_flavor}" != "python2"
%pycache_only %{python_sitelib}/md2workflow/__pycache__
%pycache_only %{python_sitelib}/md2workflow/backend/__pycache__
%pycache_only %{python_sitelib}/md2workflow/validation/__pycache__
%endif
%dir %{python_sitelib}/md2workflow
%{python_sitelib}/md2workflow/*.py*
%dir %{python_sitelib}/md2workflow/backend
%{python_sitelib}/md2workflow/backend/*.py*
%dir %{python_sitelib}/md2workflow/validation
%{python_sitelib}/md2workflow/validation/*.py*
%{python_sitelib}/md2workflow*.egg-info

%files %{python_files plugins-jira}
%dir %{python_sitelib}/md2workflow/backend/jirabackend
%{python_sitelib}/md2workflow/backend/jirabackend/*.py*
%dir %{python_sitelib}/md2workflow/validation/jira_validation
%{python_sitelib}/md2workflow/validation/jira_validation/*.py*
%if "%{python_flavor}" != "python2"
%pycache_only %{python_sitelib}/md2workflow/backend/jirabackend/__pycache__
%pycache_only %{python_sitelib}/md2workflow/validation/jira_validation/__pycache__
%endif

%files %{python_files plugins-redmine}
%dir %{python_sitelib}/md2workflow/backend/redminebackend
%{python_sitelib}/md2workflow/backend/redminebackend/*.py*
%dir %{python_sitelib}/md2workflow/validation/redmine_validation
%{python_sitelib}/md2workflow/validation/redmine_validation/*.py*
%if "%{python_flavor}" != "python2"
%pycache_only %{python_sitelib}/md2workflow/backend/redminebackend/__pycache__
%pycache_only %{python_sitelib}/md2workflow/validation/redmine_validation/__pycache__
%endif

%files -n python-md2workflow-common
%dir %{_datadir}/md2workflow/
%dir %{_datadir}/md2workflow/config/
%{_datadir}/md2workflow/config/*
%dir %{_datadir}/md2workflow/example/
%{_datadir}/md2workflow/example/*
%{_sysconfdir}/md2workflow

%changelog
