#
# spec file for package python-injector
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-injector
Version:        0.18.3
Release:        0
Summary:        Python dependency injection framework, inspired by Guice
License:        BSD-3-Clause
URL:            https://github.com/alecthomas/injector
Source:         https://github.com/alecthomas/injector/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 3.7.4}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  ((python3-dataclasses and python3-base < 3.7) or (python36-dataclasses and python36-base))
Requires:       python
Requires:       python-typing_extensions >= 3.7.4
BuildArch:      noarch
%python_subpackages

%description
Dependency injection as a formal pattern is less useful in Python than
in other languages, primarily due to its support for keyword
arguments, the ease with which objects can be mocked, and its dynamic
nature.

That said, a framework for assisting in this process can remove a lot
of boiler-plate from larger applications. That's where Injector can
help. It automatically and transitively provides keyword arguments
with their values. As an added benefit, Injector encourages nicely
compartmentalised code through the use of Module s.

While being inspired by Guice, it does not slavishly replicate its
API. Providing a Pythonic API trumps faithfulness.

%prep
%setup -q -n injector-%{version}
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/*

%changelog
