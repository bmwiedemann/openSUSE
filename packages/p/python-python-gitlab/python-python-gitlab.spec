#
# spec file for package python-python-gitlab
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-python-gitlab
Version:        3.12.0
Release:        0
Summary:        Python module for interacting with the GitLab API
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/python-gitlab/python-gitlab
Source:         https://files.pythonhosted.org/packages/source/p/python-gitlab/python-gitlab-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.2
Requires:       python-argcomplete >= 1.10.0
Requires:       python-requests >= 2.22.0
Requires:       python-requests-toolbelt >= 0.9.1
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module httmock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.22.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.9.1}
BuildRequires:  %{python_module responses}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
The python-gitlab package provides access to the GitLab server API.

It supports the v4 API of GitLab, and provides a CLI tool (gitlab).

%prep
%autosetup -p1 -n python-gitlab-%{version}
# rpmlint non-executable-script
sed -i -e '/^#!\//, 1d' gitlab/cli.py
sed -i -e '/^#!\//, 1d' gitlab/v4/cli.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/gitlab
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
touch $HOME/.python-gitlab.cfg
# test_merge_auth:  E               gitlab.config.GitlabIDError: Impossible to get the gitlab id (not specified in config file)
%pytest tests/unit -k 'not test_merge_auth'

%post
%python_install_alternative gitlab

%postun
%python_uninstall_alternative gitlab

%files %{python_files}
%doc AUTHORS CHANGELOG.md README.rst
%license COPYING
%python_alternative %{_bindir}/gitlab
%{python_sitelib}/*

%changelog
