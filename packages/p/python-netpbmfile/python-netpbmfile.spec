#
# spec file for package python-netpbmfile
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


%{?sle15_python_module_pythons}
Name:           python-netpbmfile
Version:        2024.5.24
Release:        0
Summary:        Read and write image files in the Netpbm format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/cgohlke/netpbmfile/
Source:         https://github.com/cgohlke/netpbmfile/archive/v%{version}.tar.gz#/netpbmfile-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module matplotlib >= 3.2}
BuildRequires:  %{python_module numpy >= 1.26.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.2
Requires:       python-numpy >= 1.26.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Netpbmfile is a Python library to read and write image files in the Netpbm
format.

%prep
%setup -q -n netpbmfile-%{version}
# Fix warning: wrong end-of-line encoding
sed -i 's/\r//' README.rst

%build
%pyproject_wheel

%install
%pyproject_install
for p in netpbmfile ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative netpbmfile

%post
%python_install_alternative netpbmfile

%postun
%python_uninstall_alternative netpbmfile

%check
# Test not provided

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/netpbmfile
%{python_sitelib}/netpbmfile
%{python_sitelib}/netpbmfile-%{version}.dist-info

%changelog
