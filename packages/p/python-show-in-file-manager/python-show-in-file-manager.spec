#
# spec file for package python-show-in-file-manager
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


%{?sle15_python_module_pythons}
Name:           python-show-in-file-manager
Version:        1.1.6
Release:        0
Summary:        Open the system file manager and select files in it
License:        MIT
URL:            https://github.com/damonlynch/showinfilemanager
Source:         https://files.pythonhosted.org/packages/source/s/show-in-file-manager/show_in_file_manager-%{version}.tar.gz
BuildRequires:  %{python_module hatch-argparse-manpage}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyxdg >= 0.25}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires:       python-pyxdg >= 0.25
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Show in File Manager is a Python package to open the system file manager
and optionally select files in it. The point is not to open the files, but
to select them in the file manager, thereby highlighting the files and allowing
the user to quickly do something with them.

%prep
%setup -q -n show_in_file_manager-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/showinfilemanager
%python_expand rm %{buildroot}%{$python_sitelib}/man/showinfilemanager.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# There are not python tests

%post
%python_install_alternative showinfilemanager

%postun
%python_uninstall_alternative showinfilemanager

%files %{python_files}
%doc CHANGELOG.md README.md RELEASE_NOTES.md
%license LICENSE
%python_alternative %{_bindir}/showinfilemanager
%{python_sitelib}/showinfm
%{python_sitelib}/show_in_file_manager-%{version}*-info

%changelog
