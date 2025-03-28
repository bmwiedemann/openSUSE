#
# spec file for package python-uri-template
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


%{?sle15_python_module_pythons}
Name:           python-uri-template
Version:        1.3.0
Release:        0
Summary:        RFC 6570 URI Template Processor
License:        MIT
URL:            https://github.com/plinss/uri_template/
Source:         https://files.pythonhosted.org/packages/source/u/uri-template/uri-template-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-uri_template = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
RFC 6570 URI Template Processor

%prep
%setup -q -n uri-template-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mv uri_template uri_template.moved
%{python_expand #
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -B test.py
}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/uri_template
%{python_sitelib}/uri_template-%{version}.dist-info

%changelog
