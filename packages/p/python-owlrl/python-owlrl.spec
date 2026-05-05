#
# spec file for package python-owlrl
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


Name:           python-owlrl
Version:        7.1.3
Release:        0
Summary:        A simple implementation of the OWL2 RL Profile, as well as a basic RDFS inference
License:        W3C
URL:            https://pypi.org/project/owlrl/
Source0:        owlrl-%{version}.tar.gz
BuildRequires:  %{python_module rdflib}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A simple implementation of the OWL2 RL Profile, as well as a basic RDFS inference,
on top of RDFLib. Based mechanical forward chaining.

%prep
%autosetup -p1 -n owlrl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/owlrl
%{python_sitelib}/owlrl-%{version}*info

%changelog
