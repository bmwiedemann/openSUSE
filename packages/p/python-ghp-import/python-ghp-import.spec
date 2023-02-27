#
# spec file for package python-ghp-import
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


%define skip_python2 1
Name:           python-ghp-import
Version:        2.1.0
Release:        0
Summary:        Utility to import docs into a gh-pages branch
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://pypi.org/project/ghp-import/
Source:         https://files.pythonhosted.org/packages/source/g/ghp-import/ghp-import-%{version}.tar.gz
BuildRequires:  %{python_module dateutil >= 2.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dateutil >= 2.8.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A utility to import docs to a gh-pages branch.
This will destroy the gh-pages branch. This script assumes that
gh-pages is 100%% derivative. You should never edit files in your
gh-pages branch by hand if you're using this script because you
will lose your work.

%prep
%autosetup -n ghp-import-%{version}
sed -i '1d' ghp_import.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ghp-import

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ghp-import

%postun
%python_uninstall_alternative ghp-import

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/ghp-import
%{python_sitelib}/ghp_import.py
%{python_sitelib}/__pycache__/ghp_import*.pyc
%{python_sitelib}/ghp_import-%{version}*-info

%changelog
