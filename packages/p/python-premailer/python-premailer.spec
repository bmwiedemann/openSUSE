#
# spec file for package python-premailer
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


Name:           python-premailer
Version:        3.10.0
Release:        0
Summary:        Turns CSS blocks into style attributes
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://premailer.io
Source:         https://files.pythonhosted.org/packages/source/p/premailer/premailer-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cachetools
Requires:       python-cssselect
Requires:       python-cssutils
Requires:       python-lxml
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Premailer is a Python library based on libxml which can analyze a
HTML document and extract its CSS style sheets and then for all
CSS seletors defined, it finds the DOM nodes and puts style
attributes in instead.

%prep
%setup -q -n premailer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# THERE ARE NO TESTS TO RUN, SO NO %%check SECTION

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/premailer
%{python_sitelib}/premailer-%{version}*-info

%changelog
