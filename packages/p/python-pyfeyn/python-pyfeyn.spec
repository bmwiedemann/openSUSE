#
# spec file for package python-pyfeyn
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-pyfeyn
Version:        1.0.0
Release:        0
Summary:        A Python library to help draw Feynman diagrams
License:        GPL-2.0-or-later
URL:            http://projects.hepforge.org/pyfeyn/
Source:         https://files.pythonhosted.org/packages/source/p/pyfeyn/pyfeyn-%{version}.tar.gz
BuildRequires:  %{python_module PyX}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyX
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     texlive-hepnames
BuildArch:      noarch
%python_subpackages

%description
PyFeyn is a package to programmaticaly draw Feynman diagrams. These
are important constructs in perturbative field theory, so being able
to draw them in a programmatic fashion is important if attempting to
enumerate a large number of diagram configurations is important.
PyFeyn can output into PDF or EPS. Special effects can be obtained by
using constructs from PyX, which PyFeyn is based around.

%prep
%setup -q -n pyfeyn-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mkfeyndiag
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative mkfeyndiag

%postun
%python_uninstall_alternative mkfeyndiag

%files %{python_files}
%python_alternative %{_bindir}/mkfeyndiag
%{python_sitelib}/pyfeyn/
%{python_sitelib}/pyfeyn-%{version}.dist-info

%changelog
