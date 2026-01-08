#
# spec file for package python-peewee-migrate
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%define run_tests 1
%else
%define run_tests 0
%endif

%{?sle15_python_module_pythons}
Name:           python-peewee-migrate
Version:        1.14.3
Release:        0
Summary:        Support for migrations in Peewee ORM
License:        MIT
URL:            https://github.com/klen/peewee_migrate
Source:         https://files.pythonhosted.org/packages/source/p/peewee-migrate/peewee_migrate-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  python-rpm-macros
%if 0%{?run_tests}
# The following are required for the testsuite
BuildRequires:  %{python_module peewee}
BuildRequires:  %{python_module pytest-mypy}
BuildRequires:  %{python_module pytest}
%endif
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-click
Requires:       python-peewee
BuildArch:      noarch
%python_subpackages

%description
A simple migration engine for Peewee_ ORM

%prep
%autosetup -p1 -n peewee_migrate-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
for p in pw-migrate pw_migrate ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%if 0%{?run_tests}
%check
%pytest
%endif

%post
%python_install_alternative pw-migrate pw_migrate

%postun
%python_uninstall_alternative pw-migrate pw_migrate

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/pw-migrate
%python_alternative %{_bindir}/pw_migrate
%{python_sitelib}/peewee_migrate
%{python_sitelib}/peewee_migrate-%{version}.dist-info

%changelog
