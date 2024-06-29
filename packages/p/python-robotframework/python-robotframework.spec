#
# spec file for package python-robotframework
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-robotframework
Version:        7.0.1
Release:        0
Summary:        Generic test automation framework for acceptance testing and ATDD
License:        Apache-2.0
URL:            https://robotframework.org/
Source:         https://files.pythonhosted.org/packages/source/r/robotframework/robotframework-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Robot Framework is a generic open source automation framework for acceptance
testing, acceptance test driven development (ATDD), and robotic process
automation (RPA). It has simple plain text syntax and it can be extended easily
with libraries implemented using Python or Java.

%prep
%setup -q -n robotframework-%{version}

# Fix rpmlint error "This script uses 'env' as an interpreter"
for file in $(grep -l '#!%{_bindir}/env python' src/robot/*.py); do
    sed -i '1{/#!\/usr\/bin\/env python/d}' $file;
done

%build
%python_build

%install
%python_install
for p in robot rebot libdoc; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative robot rebot libdoc

%postun
%python_uninstall_alternative robot

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/rebot
%python_alternative %{_bindir}/robot
%python_alternative %{_bindir}/libdoc
%{python_sitelib}/*

%changelog
