#
# spec file for package python-czifile
#
# Copyright (c) 2021 SUSE LLC
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


%define packagename czifile
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1
Name:           python-czifile
Version:        2019.7.2
Release:        0
Summary:        Read Carl Zeiss(r) Image (CZI) files
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://github.com/cgohlke/czifile/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module imagecodecs >= 2019.1.1}
BuildRequires:  %{python_module numpy >= 1.11.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tifffile >= 2019.7.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-imagecodecs >= 2019.1.1
Requires:       python-numpy >= 1.11.3
Requires:       python-scipy >= 1.1
Requires:       python-tifffile >= 2019.7.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Read image and metadata from Carl Zeiss(r) ZISRAW (CZI) microscopy files.

%prep
%setup -q -n %{packagename}-%{version}
# Fix W: non-executable-script
sed -i '/^#!/d' %{packagename}/czi2tif.py

# Fix warning: wrong end-of-line encoding
sed -i 's/\r//' README.rst

%build
%python_build

%install
%python_install
for p in %{packagename} ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

for p in czi2tif ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative %{packagename}
%prepare_alternative czi2tif

%post
%python_install_alternative %{packagename}
%python_install_alternative czi2tif

%postun
%python_uninstall_alternative %{packagename}
%python_uninstall_alternative czi2tif

%check
# No test provided.

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/czi2tif
%python_alternative %{_bindir}/czifile
%{python_sitelib}/*egg-info/
%{python_sitelib}/%{packagename}/

%changelog
