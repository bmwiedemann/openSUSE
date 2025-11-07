#
# spec file for package python-Markdown
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-Markdown%{psuffix}
Version:        3.10
Release:        0
Summary:        Python implementation of Markdown
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://python-markdown.github.io/
Source:         https://files.pythonhosted.org/packages/source/m/markdown/markdown-%{version}.tar.gz
Patch0:         markdown-3.0-python37.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 77.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module Markdown = %{version}}
BuildRequires:  %{python_module PyYAML}
%endif
%python_subpackages

%description
This is a Python implementation of John Gruber's [Markdown][].
It is almost completely compliant with the reference implementation,
though there are a few known issues. See [Features][] for information
on what exactly is supported and what is not. Additional features are
supported by the [Available Extensions][].

%prep
%autosetup -p1 -n markdown-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/markdown_py
%endif

%check
%if %{with test}
%pyunittest discover -v
%endif

%if %{without test}
%post
%python_install_alternative markdown_py

%postun
%python_uninstall_alternative markdown_py

%pre
%python_libalternatives_reset_alternative markdown_py

%files %{python_files}
%license LICENSE.md
%doc README.md docs/*
%python_alternative %{_bindir}/markdown_py
%{python_sitelib}/markdown
%{python_sitelib}/[mM]arkdown-%{version}.dist-info
%endif

%changelog
