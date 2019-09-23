#
# spec file for package python-requests-hawk
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 The openSUSE Project.
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
%bcond_with test
Name:           python-requests-hawk
Version:        1.0.0
Release:        0
Summary:        Hawk authentication strategy for the requests python library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mozilla-services/requests-hawk
Source:         https://files.pythonhosted.org/packages/source/r/requests-hawk/requests-hawk-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mohawk
Requires:       python-requests
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module mohawk}
BuildRequires:  %{python_module requests}
%endif
%python_subpackages

%description
This project allows you to use the python requests library with the hawk
authentification mechanism.

Hawk itself does not provide any mechanism for obtaining or transmitting the
set of shared credentials required, but this project proposes a scheme we use
across mozilla services projects.

%prep
%setup -q -n requests-hawk-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt README.rst
%{python_sitelib}/*

%changelog
