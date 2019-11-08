#
# spec file for package python-Trolly
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  test
Name:           python-Trolly
Version:        0.2.2
Release:        0
Summary:        Trello api
License:        MIT
URL:            https://github.com/plish/Trolly
Source:         https://files.pythonhosted.org/packages/source/T/Trolly/Trolly-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module httplib2}
%endif
%python_subpackages

%description
A Python wrapper around the Trello API. Provides a group of
Python classes to represent Trello Objects. None of the classes
cache values as they are designed to be inherited and extended to
suit the needs of each user. Each class includes a basic set of
methods based on general use cases. This library was based on
work done by [sarumont](https://github.com/sarumont/py-trello).
Very little was kept from this code, but still props on the
initial work.

%prep
%setup -q -n Trolly-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec -munittest discover
%endif

%files %{python_files}
%{python_sitelib}/*

%changelog
