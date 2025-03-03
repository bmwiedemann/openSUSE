#
# spec file for package python-genson
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


Name:           python-genson
Version:        1.3.0
Release:        0
Summary:        Python JSON Schema generator
License:        MIT
URL:            https://github.com/wolverdude/genson/
Source:         https://files.pythonhosted.org/packages/source/g/genson/genson-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#wolverdude/GenSON#84
Patch0:         use-sys-executable.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
GenSON is a JSON Schema generator.

Besides taking JSON objects and generating schemas that describe
them, this generator is able to merge schemas as well.

%prep
%autosetup -p1 -n genson-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/genson
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_no_input'

%post
%python_install_alternative genson

%postun
%python_uninstall_alternative genson

%files %{python_files}
%doc AUTHORS.rst README.rst HISTORY.rst
%license LICENSE
%python_alternative %{_bindir}/genson
%{python_sitelib}/genson
%{python_sitelib}/genson-%{version}.dist-info

%changelog
