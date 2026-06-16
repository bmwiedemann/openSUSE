#
# spec file for package python-idna
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%{?sle15_python_module_pythons}
Name:           python-idna
Version:        3.18
Release:        0
Summary:        Internationalized Domain Names in Applications (IDNA)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/kjd/idna
Source0:        https://files.pythonhosted.org/packages/source/i/idna/idna-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20220106.80d3756
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
A library to support the Internationalised Domain Names in
Applications (IDNA) protocol as specified in RFC 5891
http://tools.ietf.org/html/rfc5891. This version of the protocol
is often referred to as “IDNA2008” and can produce different
results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement
for the “encodings.idna” module that comes with the Python standard
library but currently only supports the older 2003 specification.

%prep
%autosetup -p1 -n idna-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/idna
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%pre
%python_libalternatives_reset_alternative idna

%post
%python_install_alternative idna

%postun
%python_uninstall_alternative idna

%files %{python_files}
%license LICENSE.md
%doc README.md HISTORY.md
%python_alternative %{_bindir}/idna
%{python_sitelib}/idna
%{python_sitelib}/idna-%{version}*-info

%changelog
