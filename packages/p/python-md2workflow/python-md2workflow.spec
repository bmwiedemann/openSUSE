#
# spec file for package python-md2workflow
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
Name:           python-md2workflow
Version:        1.4.9
Release:        0
Summary:        Tool to create a JIRA or other Workflow from markdown files
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/lkocman/md2workflow.git
Source:         https://files.pythonhosted.org/packages/source/m/md2workflow/md2workflow-%{version}.tar.gz
Source1:        suse-prod.conf
Source2:        suse-devel.conf
Source3:        suse-staging.conf
Source4:        suse-lutoslawski.conf
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jira
Requires:       python-md2workflow-common
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython3
Provides:       md2workfow = %{version}
%endif

%description
A tool which can convert typically "VCS managed" mardown checklist
into e.g. a linked structure of Jira Epics. This tool can not only
create checklists, but also update them.

%python_subpackages

%package -n python-md2workflow-common
Summary:        Configuration and examples for md2workflow
Group:          Development/Languages/Python
Provides:       %{python_module md2workflow-common = %{version}}

%description -n python-md2workflow-common
Configuration and examples for md2workflow

%prep

%setup -q -n md2workflow-%{version}
echo `pwd`
cp %{_sourcedir}/{suse-prod,suse-devel,suse-staging,suse-lutoslawski}.conf  config/

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/md2workflow
%python_expand %fdupes %{buildroot}%{$python_sitelib}
ln -s -f %{_datadir}/md2workflow/config %{buildroot}%{_sysconfdir}/md2workflow

%files %{python_files}
%{_bindir}/md2workflow-%{python_bin_suffix}
%python3_only %{_bindir}/md2workflow
%{python_sitelib}/*
%python_alternative %{_bindir}/md2workflow
%license LICENSE

%files -n python-md2workflow-common
%dir %{_datadir}/md2workflow/
%dir %{_datadir}/md2workflow/example/
%{_datadir}/md2workflow/example/*
%dir %{_datadir}/md2workflow/config/
%{_datadir}/md2workflow/config/local.conf
%{_datadir}/md2workflow/config/*
%{_sysconfdir}/md2workflow

%changelog
