#
# spec file for package python-colander
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013-2019 LISA GmbH, Bingen, Germany.
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
Name:           python-colander
Version:        1.7.0
Release:        0
Summary:        A schema-based serialization and deserialization library
License:        BSD-4-Clause AND ZPL-2.1 AND MIT
URL:            https://github.com/Pylons/colander
Source:         https://files.pythonhosted.org/packages/source/c/colander/colander-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module translationstring}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-iso8601
Requires:       python-translationstring
BuildArch:      noarch
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx} >= 1.3.1
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pylons-sphinx-themes}
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module hupper}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module plaster-pastedeploy}
BuildRequires:  %{python_module plaster}
# /SECTION
%python_subpackages

%description
An extensible package which can be used to:

- deserialize and validate a data structure composed of strings,
  mappings, and lists.

- serialize an arbitrary data structure to a data structure composed
  of strings, mappings, and lists.

It is tested on Python 2.7, 3.3, 3.4, 3.5, and 3.6, and PyPy.

Please see http://docs.pylonsproject.org/projects/colander/en/latest/
for documentation.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}

%description doc
This package contains documentation files for %{name}.

%package lang
# FIXME: consider using %%lang_package macro
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Requires:       python-base
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations for the "%{name}" package.

%prep
%setup -q -n colander-%{version}

%build
%python_build
%python_exec setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
%python_install
%find_lang colander
%python_expand grep -F "%{$python_sitelib}" colander.lang > colander_%{$python_bin_suffix}.lang
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py nosetests --with-coverage

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/*
%exclude %{python_sitelib}/colander/locale

%if %{have_python2} && ! 0%{?skip_python2}
%files -n %{python2_prefix}-colander-lang -f colander_%{python2_bin_suffix}.lang
%license LICENSE.txt
%{python2_sitelib}/colander/locale
%endif

%if %{have_python2} && ! 0%{?skip_python3}
%files -n %{python3_prefix}-colander-lang -f colander_%{python3_bin_suffix}.lang
%license LICENSE.txt
%{python3_sitelib}/colander/locale
%endif

%files %{python_files doc}
%license LICENSE.txt
%doc build/sphinx/html

%changelog
