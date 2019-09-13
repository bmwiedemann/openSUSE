#
# spec file for package python-premailer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-premailer
Version:        3.6.1
Release:        0
License:        Python-2.0
Summary:        Turns CSS blocks into style attributes
Url:            https://premailer.io
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/premailer/premailer-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# THERE ARE NO TESTS TO RUN, SO NO %%check SECTION

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
