#
# spec file for package python-poetry-dynamic-versioning
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
Name:           python-poetry-dynamic-versioning
Version:        1.4.0
Release:        0
Summary:        Plugin for Poetry to enable dynamic versioning based on VCS tags
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/mtkennerly/poetry-dynamic-versioning
Source:         https://files.pythonhosted.org/packages/source/p/poetry-dynamic-versioning/poetry_dynamic_versioning-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-dunamai >= 1.21.0
Requires:       python-tomlkit
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
%{summary}.

%prep
%autosetup -p1 -n poetry_dynamic_versioning-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/poetry-dynamic-versioning
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative poetry-dynamic-versioning

%{python_compileall}

%post
%python_install_alternative poetry-dynamic-versioning

%postun
%python_uninstall_alternative poetry-dynamic-versioning

%check
#every test reaches out to the internet

%files %{python_files}
%python_alternative %{_bindir}/poetry-dynamic-versioning
%{python_sitelib}/poetry_dynamic_versioning
%{python_sitelib}/poetry_dynamic_versioning-%{version}.dist-info

%changelog
