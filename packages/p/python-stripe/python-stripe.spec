#
# spec file for package python-stripe
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python2 1
Name:           python-stripe
Version:        2.63.0
Release:        0
Summary:        Python bindings for the Stripe API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/stripe/stripe-python
Source:         https://files.pythonhosted.org/packages/source/s/stripe/stripe-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-mock >= 2.0}
BuildRequires:  %{python_module requests >= 2.20}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.20
Conflicts:      python-stripe-api
BuildArch:      noarch
%python_subpackages

%description
Python bindings for the Stripe API.

%prep
%setup -q -n stripe-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -rs --nomock

%files %{python_files}
%doc CHANGELOG.md README.md examples/
%license LICENSE
%{python_sitelib}/stripe*

%changelog
