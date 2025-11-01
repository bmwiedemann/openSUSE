#
# spec file for package python-annotated-doc
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


Name:           python-annotated-doc
Version:        0.0.3
Release:        0
Summary:        Document params, attributes, types and variables inline
License:        MIT
URL:            https://github.com/fastapi/annotated-doc
Source:         https://files.pythonhosted.org/packages/source/a/annotated-doc/annotated_doc-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build < 0.10.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Document parameters, class attributes, return types, and variables inline, with `Annotated`.

%prep
%autosetup -p1 -n annotated_doc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/annotated_doc
%{python_sitelib}/annotated_doc-%{version}.dist-info

%changelog
