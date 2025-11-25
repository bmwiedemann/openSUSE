#
# spec file for package python-Faker
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-Faker
Version:        38.2.0
Release:        0
Summary:        Python package that generates fake data
License:        MIT
URL:            https://github.com/joke2k/faker
Source:         https://files.pythonhosted.org/packages/source/f/faker/faker-%{version}.tar.gz
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6.0.1}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module validators >= 0.13.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tzdata
Obsoletes:      python3-fake-factory < %{version}-%{release}
Provides:       python3-fake-factory = %{version}-%{release}
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
Faker is a Python package that generates fake data. It helps with
database bootstrapping, creating XML documents, persistence stress
testing, and data anonymization from production services.

%prep
%setup -q -n faker-%{version}
# Remove pre-existing bytecode files in the sdist
find . -name '*.py[co]' -delete
# do not hardcode versions
sed -i -e 's:==:>=:g' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/faker
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative faker

%post
%python_install_alternative faker

%postun
%python_uninstall_alternative faker

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.rst
%python_alternative %{_bindir}/faker
%{python_sitelib}/faker
%{python_sitelib}/[fF]aker-%{version}.dist-info

%changelog
