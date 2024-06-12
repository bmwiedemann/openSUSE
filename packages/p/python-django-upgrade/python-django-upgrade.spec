#
# spec file for package python-django-upgrade
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


%{?sle15_python_module_pythons}
Name:           python-django-upgrade
Version:        1.18.0
Release:        0
Summary:        Automatically upgrade your Django projects
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/adamchainz/django-upgrade
Source:         https://github.com/adamchainz/django-upgrade/archive/refs/tags/%{version}.tar.gz#/django-upgrade-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tokenize-rt
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tokenize-rt}
# /SECTION
%python_subpackages

%description
Automatically upgrade your Django projects.

%prep
%setup -q -n django-upgrade-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/django-upgrade
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative django-upgrade

%postun
%python_uninstall_alternative django-upgrade

%check
%pytest -k 'not test_main_version'

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/django-upgrade
%{python_sitelib}/django[_-]upgrade*/

%changelog
