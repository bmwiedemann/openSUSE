#
# spec file for package python-marathon
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-marathon
Version:        0.13.0
Release:        0
Summary:        Marathon Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thefactory/marathon-python
Source:         https://github.com/thefactory/marathon-python/archive/refs/tags/%{version}.tar.gz#/marathon-%{version}.tar.gz
# https://github.com/thefactory/marathon-python/issues/284
Patch0:         python-marathon-no-2to3.patch
# https://github.com/thefactory/marathon-python/commit/1850734b5b916d1455416833f0aed239b308dd9f.diff
Patch1:         python-marathon-use-collections.abc.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.4.0
Requires:       python-requests-toolbelt >= 0.4.0
BuildArch:      noarch
%python_subpackages

%description
Python interface to the Mesos Marathon REST API.

%prep
%setup -q -n marathon-python-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
