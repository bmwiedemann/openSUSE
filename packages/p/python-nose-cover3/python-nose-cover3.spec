#
# spec file for package python-nose-cover3
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-nose-cover3
Version:        0.1.0
Release:        0
Url:            http://github.com/ask/nosecover3
Summary:        Coverage 3.x support for Nose
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/n/nose-cover3/nose-cover3-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-2to3
Requires:       python-coverage
Requires:       python-nose
BuildArch:      noarch
%python_subpackages

%description
Coverage 3.x support for Nose.

%prep
%setup -q -n nose-cover3-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README lgpl.txt
%{python_sitelib}/*

%changelog
