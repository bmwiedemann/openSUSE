#
# spec file for package python-Glymur
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-Glymur
Version:        0.14.4
Release:        0
Summary:        Tools for accessing JPEG2000 files
License:        MIT
URL:            https://github.com/quintusdias/glymur
Source:         https://github.com/quintusdias/glymur/archive/v%{version}.tar.gz#/Glymur-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-image}
# /SECTION
%python_subpackages

%description
Python interface to the OpenJPEG library

%prep
%autosetup -p1 -n glymur-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jp2dump
%python_clone -a %{buildroot}%{_bindir}/jpeg2jp2
%python_clone -a %{buildroot}%{_bindir}/tiff2jp2
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test says: "SCENARIO:  the XDG_CONFIG_HOME environment variable is not present"
# which is not true with our pytest macro
donttest+="test_config_dir_on_windows"
%pytest -k "not ($donttest)"

%post
%python_install_alternative jp2dump jpeg2jp2 tiff2jp2

%postun
%python_uninstall_alternative jp2dump

%files %{python_files}
%doc README.md CHANGES.txt
%license LICENSE.txt
%python_alternative %{_bindir}/jp2dump
%python_alternative %{_bindir}/jpeg2jp2
%python_alternative %{_bindir}/tiff2jp2
%{python_sitelib}/glymur
%{python_sitelib}/[Gg]lymur-%{version}.dist-info

%changelog
