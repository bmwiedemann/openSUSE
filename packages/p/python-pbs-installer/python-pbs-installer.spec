#
# spec file for package python-pbs-installer
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


Name:           python-pbs-installer
Version:        2024.4.24
Release:        0
Summary:        Installer for Python Build Standalone
License:        MIT
URL:            https://github.com/frostming/pbs-installer
Source:         https://files.pythonhosted.org/packages/source/p/pbs-installer/pbs_installer-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-httpx >= 0.27.0
Suggests:       python-zstandard >= 0.21.0
Suggests:       python-pbs-installer
BuildArch:      noarch
%python_subpackages

%description
An installer for @indygreg's python-build-standalone

%prep
%autosetup -p1 -n pbs_installer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pbs-install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No tests
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import pbs_installer"}

%post
%python_install_alternative pbs-install

%postun
%python_uninstall_alternative pbs-install

%files %{python_files}
%python_alternative %{_bindir}/pbs-install
%{python_sitelib}/pbs_installer
%{python_sitelib}/pbs_installer-%{version}.dist-info

%changelog
