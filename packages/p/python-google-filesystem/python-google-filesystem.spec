#
# spec file for package python-google-filesystem
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-google-filesystem
Version:        1.0
Release:        0
Summary:        Common directories shared by Python Google modules
License:        Apache-2.0
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Common directories shared by Python Google modules

%prep
# Not needed

%build
# Not needed

%install
%{python_expand install -d -m 755 %{buildroot}%{$python_sitelib}/google}
%{python_expand touch %{buildroot}%{$python_sitelib}/google/__init__.py}

%files %{python_files}
%dir %{python_sitelib}/google
%{python_sitelib}/google/__init__.py

%changelog
