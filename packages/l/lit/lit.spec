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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           lit
Version:        0.6.0
Release:        0
Summary:        A portable tool for executing test suites
License:        NCSA
Group:          Development/Tools/Other
URL:            http://llvm.org/cmds/lit.html
Source0:        https://files.pythonhosted.org/packages/source/l/lit/lit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython3
Provides:       lit = %{version}
%endif
%python_subpackages

%description
Lit is a portable tool for executing LLVM and Clang style test suites,
summarizing their results, and providing indication of failures. Lit is
designed to be a lightweight testing tool with as simple a user interface
as possible/

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/lit
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%post
%python_install_alternative lit

%postun
%python_uninstall_alternative lit

%files %{python_files}
%doc README.txt
%python_alternative %{_bindir}/lit
%{python_sitelib}/*

%changelog
