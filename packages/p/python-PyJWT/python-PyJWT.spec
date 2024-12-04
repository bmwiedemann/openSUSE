#
# spec file for package python-PyJWT
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
Name:           python-PyJWT
Version:        2.10.1
Release:        0
Summary:        JSON Web Token implementation in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/progrium/pyjwt
Source:         https://files.pythonhosted.org/packages/source/p/pyjwt/pyjwt-%{version}.tar.gz
BuildRequires:  %{python_module cryptography >= 3.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-cryptography >= 3.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python implementation of JSON Web Token draft 01.

%prep
%setup -q -n pyjwt-%{version}

%build
%pyproject_wheel

#remove shebang from all non executable files
find ./ -type f -name "*.py" -perm 644 -exec sed -i -e '1{\@^#!%{_bindir}/env python@d}' {} \;

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="test_verify_false_deprecated or test_get_jwt_set_sslcontext_default"
# Failing test: gh#jpadilla/pyjwt#802
donttest+=" or test_ec_to_jwk_with_invalid_curve"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitelib}/jwt
%{python_sitelib}/PyJWT-%{version}.dist-info

%changelog
