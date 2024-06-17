#
# spec file for package python-annotated-types
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
Name:           python-annotated-types
Version:        0.7.0
Release:        0
Summary:        Reusable constraint types to use with typing.Annotated
License:        MIT
URL:            https://github.com/annotated-types/annotated-types/
Source:         https://files.pythonhosted.org/packages/source/a/annotated-types/annotated_types-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PEP-593 added `typing.Annotated` as a way of adding context-specific metadata to
existing types, and specifies that `Annotated[T, x]` _should_ be treated as `T` by
any tool or library without special logic for `x`.

This package provides metadata objects which can be used to represent common
constraints such as upper and lower bounds on scalar values and collection sizes,
a `Predicate` marker for runtime checks, and
descriptions of how we intend these metadata to be interpreted. In some cases,
we also note alternative representations which do not require this package.

%prep
%autosetup -p1 -n annotated_types-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/annotated_types
%{python_sitelib}/annotated_types-%{version}.dist-info

%changelog
