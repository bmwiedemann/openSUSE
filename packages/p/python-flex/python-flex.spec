#
# spec file for package python-flex
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
Name:           python-flex
Version:        6.14.1
Release:        0
Summary:        Swagger Schema validation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pipermerriam/flex
Source:         https://github.com/pipermerriam/flex/archive/v%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module click >= 3.3}
BuildRequires:  %{python_module factory_boy >= 2.4.1}
BuildRequires:  %{python_module jsonpointer >= 1.7}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest-pythonpath >= 0.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.4.3}
BuildRequires:  %{python_module responses >= 0.5.1}
BuildRequires:  %{python_module rfc3987 >= 1.3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.7.3}
BuildRequires:  %{python_module strict-rfc3339 >= 0.7}
BuildRequires:  %{python_module validate_email >= 1.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.11
Requires:       python-click >= 3.3
Requires:       python-jsonpointer >= 1.7
Requires:       python-requests >= 2.4.3
Requires:       python-rfc3987 >= 1.3.4
Requires:       python-six >= 1.7.3
Requires:       python-strict-rfc3339 >= 0.7
Requires:       python-validate_email >= 1.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Validation tooling for Swagger 2.0 specifications.

%prep
%setup -q -n flex-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/swagger-flex
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative swagger-flex

%postun
%python_uninstall_alternative swagger-flex

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.md
%{python_sitelib}/*
%python_alternative %{_bindir}/swagger-flex

%changelog
