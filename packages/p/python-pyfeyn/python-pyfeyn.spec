#
# spec file for package python-pyfeyn
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyfeyn
Version:        1.0.0
Release:        0
Summary:        A Python library to help draw Feynman diagrams
License:        GPL-2.0+
Group:          Development/Languages/Python
Url:            http://projects.hepforge.org/pyfeyn/
Source:         https://files.pythonhosted.org/packages/source/p/pyfeyn/pyfeyn-%{version}.tar.gz
BuildRequires:  %{python_module PyX}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyX
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%python3_only %{_bindir}/mkfeyndiag
%{python_sitelib}/pyfeyn/
%{python_sitelib}/pyfeyn-%{version}-py*.egg-info

%changelog
