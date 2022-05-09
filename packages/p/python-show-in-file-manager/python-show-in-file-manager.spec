#
# spec file for package python-show-in-file-manager
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-show-in-file-manager
Version:        1.1.4
Release:        0
Summary:        Open the system file manager and select files in it
License:        MIT
URL:            https://github.com/damonlynch/showinfilemanager
Source:         https://files.pythonhosted.org/packages/source/s/show-in-file-manager/show-in-file-manager-%{version}.tar.gz
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyxdg >= 0.25}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires:       python-pyxdg >= 0.25
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
%endif
%python_subpackages

%description
Show in File Manager is a Python package to open the system file manager
and optionally select files in it. The point is not to open the files, but
to select them in the file manager, thereby highlighting the files and allowing
the user to quickly do something with them.

%prep
%setup -q -n show-in-file-manager-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/showinfilemanager
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# There are not python tests

%post
%python_install_alternative showinfilemanager

%postun
%python_uninstall_alternative showinfilemanager

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/showinfilemanager
%{python_sitelib}/showinfm
%{python_sitelib}/show_in_file_manager-%{version}*-info

%changelog
