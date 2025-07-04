#
# spec file for package python-k5test
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-k5test
Version:        0.10.4
Release:        0
Summary:        A library for testing Python applications in krb5 environments
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pythongssapi/k5test
Source:         https://files.pythonhosted.org/packages/source/k/k5test/k5test-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       krb5-client
Requires:       krb5-server
BuildArch:      noarch
%python_subpackages

%description
k5test is a library for setting up self-contained Kerberos 5 environments,
and running Python unit tests inside those environments.  It is based on
the file of the same name found alongside the MIT Kerberos 5 unit tests.

%prep
%setup -q -n k5test-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no testsuite found

%files %{python_files}
%license *LICENSE*
%doc README.md
%{python_sitelib}/k5test*

%changelog
