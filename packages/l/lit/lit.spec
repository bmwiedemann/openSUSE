#
# spec file for package lit
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
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           lit
Version:        18.1.8
Release:        0
Summary:        A portable tool for executing test suites
License:        NCSA
Group:          Development/Tools/Other
URL:            http://llvm.org/cmds/lit.html
Source0:        https://files.pythonhosted.org/packages/source/l/lit/lit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
Provides:       lit = %{version}
%python_subpackages

%description
Lit is a portable tool for executing LLVM and Clang style test suites,
summarizing their results, and providing indication of failures. Lit is
designed to be a lightweight testing tool with as simple a user interface
as possible/

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lit
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative lit

%post
%python_install_alternative lit

%postun
%python_uninstall_alternative lit

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/lit
%{python_sitelib}/lit
%{python_sitelib}/lit-%{version}.dist-info

%changelog
