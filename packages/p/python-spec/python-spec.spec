#
# spec file for package python-spec
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-spec
Version:        1.4.1
Release:        0
Summary:        Specification-style output for nose
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bitprophet/spec
Source:         https://files.pythonhosted.org/packages/source/s/spec/spec-%{version}.tar.gz
# license is not included in sdist tarball, upstream fix: https://github.com/bitprophet/spec/pull/46
Source1:        https://github.com/bitprophet/spec/raw/%{version}/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-nose >= 1.3
Requires:       python-six < 2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
spec is a Python testing tool that provides colorized, specification style output, colorized tracebacks and summary, optional timing display and enables some non-default options of nose.

%prep
%setup -q -n spec-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/spec
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative spec

%postun
%python_uninstall_alternative spec

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/spec
%{python_sitelib}/*

%changelog
