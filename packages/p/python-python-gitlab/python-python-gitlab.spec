#
# spec file for package python-python-gitlab
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-python-gitlab
Version:        4.6.0
Release:        0
Summary:        Python module for interacting with the GitLab API
License:        LGPL-3.0-only
URL:            https://github.com/python-gitlab/python-gitlab
Source:         https://files.pythonhosted.org/packages/source/p/python-gitlab/python-gitlab-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.1
Requires:       python-argcomplete >= 1.10.0
Requires:       python-requests >= 2.22.0
Requires:       python-requests-toolbelt >= 0.9.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module httmock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.22.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.9.1}
BuildRequires:  %{python_module responses}
# /SECTION
%python_subpackages

%description
The python-gitlab package provides access to the GitLab server API.

It supports the v4 API of GitLab, and provides a CLI tool (gitlab).

%prep
%autosetup -p1 -n python-gitlab-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gitlab
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
touch $HOME/.python-gitlab.cfg
%pytest tests/unit

%post
%python_install_alternative gitlab

%postun
%python_uninstall_alternative gitlab

%files %{python_files}
%doc AUTHORS CHANGELOG.md README.rst
%license COPYING
%python_alternative %{_bindir}/gitlab
%{python_sitelib}/gitlab
%{python_sitelib}/python_gitlab-%{version}.dist-info

%changelog
