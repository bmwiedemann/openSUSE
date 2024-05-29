#
# spec file for package python-hupper
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
Name:           python-hupper
Version:        1.12.1
Release:        0
Summary:        An in-process file monitor
License:        MIT
Group:          Development/Languages/Python
URL:            https://pylonsproject.org/
# The _service download the source and repack without the docs folder
# that has CC noncommercial license.
Source:         hupper-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-watchdog
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
Hupper is an integrated process monitor that will track changes to any
imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%prep
%autosetup -p1 -n hupper-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/hupper

%check
%pytest

%post
%python_install_alternative hupper

%postun
%python_uninstall_alternative hupper

%files %{python_files}
%python_alternative %{_bindir}/hupper
%license %{python_sitelib}/hupper-%{version}.dist-info/LICENSE.txt
%{python_sitelib}/hupper-%{version}.dist-info/
%{python_sitelib}/hupper/

%changelog
