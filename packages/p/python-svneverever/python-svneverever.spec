#
# spec file for package python-svneverever
#
# Copyright (c) 2020 SUSE LLC
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


%define mod_name svneverever
%define skip_python2 1
%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-svneverever
Version:        1.4.2
Release:        0
Summary:        Tool collecting path entries across SVN history
License:        GPL-3.0-only
URL:            https://github.com/hartwork/svneverever
Source:         https://github.com/hartwork/svneverever/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       subversion
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
Obsoletes:      %{oldpython}-svneverever
%python_subpackages

%description
Tool collecting path entries across SVN history. It runs through all SVN history
collecting additions of directories. In the end it presents a tree of all
directories ever having existed in the repository.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%python_build

%install
%python_install
%python_clone %{buildroot}%{_bindir}/%{mod_name} -a
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative %{mod_name}

%postun
%python_uninstall_alternative %{mod_name}

%files %{python_files}
%doc README.asciidoc
%python_alternative %{_bindir}/%{mod_name}
%{python_sitelib}/%{mod_name}-%{version}-*.egg-info
%{python_sitelib}/%{mod_name}/

%changelog
