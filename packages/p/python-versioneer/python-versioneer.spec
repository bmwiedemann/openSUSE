#
# spec file for package python-versioneer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-versioneer
Version:        0.18
Release:        0
Summary:        VCS-based management of project version strings
License:        SUSE-Public-Domain
Group:          Development/Languages/Python
Url:            https://github.com/warner/python-versioneer
Source:         https://files.pythonhosted.org/packages/source/v/versioneer/versioneer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
Versioneer is a tool to automatically update version strings (in
setup.py and the conventional ‘from PROJECT import _version’ pattern)
by asking the version control system about the current tree.

%prep
%setup -q -n versioneer-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/versioneer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative versioneer

%postun
%python_uninstall_alternative versioneer

%files %{python_files}
%defattr(-,root,root,-)
%doc README.md
%{python_sitelib}/*
%python_alternative %{_bindir}/versioneer

%changelog
