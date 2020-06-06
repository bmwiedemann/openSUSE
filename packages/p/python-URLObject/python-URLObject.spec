#
# spec file for package python-URLObject
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
Name:           python-URLObject
Version:        2.4.3
Release:        0
Summary:        Python library for manipulating URLs (and some URIs) in a more natural way
License:        SUSE-Public-Domain
URL:            https://github.com/zacharyvoase/urlobject
Source:         https://files.pythonhosted.org/packages/source/U/URLObject/URLObject-%{version}.tar.gz
# patch-feature-upstream remove_nose.patch gh#zacharyvoase/urlobject#42 mcepl@suse.com
# Remove the need for nose and use the standard library.
Patch0:         remove_nose.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
URLObject is a utility class for manipulating URLs. The latest
incarnation of this library builds upon the ideas of its predecessor,
but aims for a clearer API, focusing on proper method names over
operator overrides. It's also being developed from the ground up in a
test-driven manner, and has full Sphinx documentation.

%prep
%setup -q -n URLObject-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license UNLICENSE
%{python_sitelib}/*

%changelog
