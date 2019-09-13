#
# spec file for package python-keepalive
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
%bcond_without test
Name:           python-keepalive
Version:        0.5
Release:        0
Summary:        Urllib keepalive support for python
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
Url:            https://github.com/wikier/keepalive
Source:         https://files.pythonhosted.org/packages/source/k/keepalive/keepalive-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
An HTTP handler for `urllib2` that supports HTTP 1.1 and keepalive.

%prep
%setup -q -n keepalive-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
