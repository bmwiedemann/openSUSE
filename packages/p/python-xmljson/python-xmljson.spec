#
# spec file for package python-xmljson
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-xmljson
Version:        0.2.1
Release:        0
Summary:        Converts XML into JSON/Python dicts/arrays and vice-versa
License:        MIT
URL:            https://github.com/sanand0/xmljson
Source:         https://files.pythonhosted.org/packages/source/x/xmljson/xmljson-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%python_subpackages

%description
Converts XML into JSON/Python dicts/arrays and vice-versa

%prep
%autosetup -p1 -n xmljson-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/xml2json
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_reset_alternative xml2json

%post
%python_install_alternative xml2json

%postun
%python_uninstall_alternative xml2json

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/xml2json
%{python_sitelib}/xmljson
%{python_sitelib}/xmljson-%{version}.dist-info

%changelog
