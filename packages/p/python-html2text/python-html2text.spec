#
# spec file for package python-html2text
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define upname html2text
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{upname}
Version:        2019.8.11
Release:        0
Summary:        Python script for turning HTML into Markdown text
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/Alir3z4/html2text/
Source:         https://files.pythonhosted.org/packages/source/h/%{upname}/%{upname}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
html2text is a Python script that converts a page of HTML into
Markdown (a text-to-HTML format).

%prep
%setup -q -n %{upname}-%{version}
# remove useless shebang
sed -i '/^#!/d' %{upname}/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/%{upname}

# remove executable bits from egg files
%python_expand chmod -x %{buildroot}%{$python_sitelib}/%{upname}-*.egg-info/*

%post
%python_install_alternative html2text

%postun
%python_uninstall_alternative html2text

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md AUTHORS.rst ChangeLog.rst
%python_alternative %{_bindir}/%{upname}
%{python_sitelib}/*

%changelog
