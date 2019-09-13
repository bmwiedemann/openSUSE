#
# spec file for package python-betamax-matchers
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-betamax-matchers
Version:        0.4.0
Release:        0
Summary:        A group of experimental matchers for Betamax
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/sigmavirus24/betamax_matchers
Source:         https://files.pythonhosted.org/packages/source/b/betamax-matchers/betamax-matchers-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-betamax >= 0.3.2
Requires:       python-requests-toolbelt >= 0.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module betamax >= 0.3.2}
BuildRequires:  %{python_module requests-toolbelt >= 0.4.0}
# /SECTION
%python_subpackages

%description
Experimental set of Matchers for Betamax that may possibly end up in the
main package.

%prep
%setup -q -n betamax-matchers-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
