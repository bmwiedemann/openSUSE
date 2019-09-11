#
# spec file for package python-seqdiag
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif
Name:           python-seqdiag
Version:        0.9.6
Release:        0
Summary:        Python module to generate sequence-diagram images from text
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://blockdiag.com/
Source:         https://files.pythonhosted.org/packages/source/s/seqdiag/seqdiag-%{version}.tar.gz
BuildRequires:  %{python_module blockdiag >= 1.5.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-blockdiag >= 1.5.0
Requires:       python-setuptools
%python_subpackages

%description
`seqdiag` generates sequence-diagram image files from spec-text files.

* Generate sequence-diagram from dot like text (basic feature).
* Multilingualization for node-label (UTF-8 only).

%prep
%setup -q -n seqdiag-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%python3_only %{_bindir}/seqdiag
%{python_sitelib}/*

%changelog
