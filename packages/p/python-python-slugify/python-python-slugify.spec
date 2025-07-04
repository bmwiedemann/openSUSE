#
# spec file for package python-python-slugify
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


%{?sle15_python_module_pythons}
%define short_name python-slugify
Name:           python-%{short_name}
Version:        8.0.4
Release:        0
Summary:        Slugify application that handles Unicode
License:        MIT
URL:            https://github.com/un33k/python-slugify
Source:         %{short_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module text-unidecode >= 1.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-text-unidecode >= 1.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-Unidecode >= 1.1.1
Conflicts:      python-awesome-slugify
BuildArch:      noarch
%python_subpackages

%description
A Python Slugify application that handles Unicode.

%prep
%setup -q -n %{short_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/slugify
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec ./test.py

%post
%python_install_alternative slugify

%postun
%python_uninstall_alternative slugify

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/slugify
%{python_sitelib}/python_slugify-%{version}.dist-info
%{python_sitelib}/slugify/

%changelog
