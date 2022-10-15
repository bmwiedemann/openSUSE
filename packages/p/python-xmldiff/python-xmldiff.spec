#
# spec file for package python-xmldiff
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-xmldiff
Version:        2.4
Release:        0
Summary:        Tree to tree correction between XML documents
License:        MIT
URL:            https://github.com/Shoobx/xmldiff
Source:         https://files.pythonhosted.org/packages/source/x/xmldiff/xmldiff-%{version}.tar.gz
# https://github.com/Shoobx/xmldiff/commit/34b810f4394965aadeca31204e6b76eb023fd11a
Patch0:         python-xmldiff-src-upgrades.patch
# https://github.com/Shoobx/xmldiff/issues/93
Patch1:         python-xmldiff-no-six-remains.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml >= 3.1.0
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      %{oldpython}-xmldiff < %{version}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lxml >= 3.1.0}
BuildRequires:  %{python_module setuptools}
# /SECTION
%python_subpackages

%description
XMLdiff shows the differences between two similar XML files in the same
way `diff` does with text files. It can also be used as a library or as
a command line tool and can work either with XML files or DOM trees.
The implementation is based on "Change detection in hierarchically
structured information", by S. Chawathe, A. Rajaraman, H.
Garcia-Molina, and J. Widom, Stanford University, 1996.

%prep
%setup -q -n xmldiff-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/xmlpatch
%python_clone -a %{buildroot}%{_bindir}/xmldiff
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%post
%python_install_alternative xmlpatch
%python_install_alternative xmldiff

%postun
%python_uninstall_alternative xmlpatch
%python_uninstall_alternative xmldiff

%files %{python_files}
%doc CHANGES.rst README.rst README.txt
%license LICENSE.txt
%python_alternative %{_bindir}/xmldiff
%python_alternative %{_bindir}/xmlpatch
%{python_sitelib}/*

%changelog
