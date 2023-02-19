#
# spec file for package python-tabulate
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-tabulate
Version:        0.9.0
Release:        0
Summary:        Pretty-printer for tabular data in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/astanin/python-tabulate
Source:         https://files.pythonhosted.org/packages/source/t/tabulate/tabulate-%{version}.tar.gz
BuildRequires:  %{python_module base > 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.2.0}
BuildRequires:  %{python_module wcwidth}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-wcwidth
Suggests:       python-pandas
BuildArch:      noarch
%python_subpackages

%description
Pretty-printer for tabular data in Python.

The main use cases of the library are:

 * printing small tables without hassle: just one function call,
   formatting is guided by the data itself
 * authoring tabular data for lightweight plain-text markup: multiple
   output formats suitable for further editing or transformation
 * readable presentation of mixed textual and numeric data: smart
   column alignment, configurable number formatting, alignment by a
   decimal point

%prep
%setup -q -n tabulate-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tabulate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative tabulate

%postun
%python_uninstall_alternative tabulate

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/tabulate
%{python_sitelib}/tabulate
%{python_sitelib}/tabulate-*dist-info

%changelog
