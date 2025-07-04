#
# spec file for package python-seqdiag
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


%bcond_without libalternatives
Name:           python-seqdiag
Version:        3.0.0
Release:        0
Summary:        Python module to generate sequence-diagram images from text
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://blockdiag.com/
Source:         https://files.pythonhosted.org/packages/source/s/seqdiag/seqdiag-%{version}.tar.gz
BuildRequires:  %{python_module blockdiag >= 1.5.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-blockdiag >= 1.5.0
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
`seqdiag` generates sequence-diagram image files from spec-text files.

* Generate sequence-diagram from dot like text (basic feature).
* Multilingualization for node-label (UTF-8 only).

%prep
%setup -q -n seqdiag-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/seqdiag

%pre
%python_libalternatives_reset_alternative seqdiag

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/seqdiag
%{python_sitelib}/seqdiag
%{python_sitelib}/seqdiag-%{version}*-info

%changelog
