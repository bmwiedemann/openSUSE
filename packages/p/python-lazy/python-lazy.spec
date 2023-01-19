#
# spec file for package python-lazy
#
# Copyright (c) 2023 SUSE LLC
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


%global modname lazy
Name:           python-lazy
Version:        1.5
Release:        0
Summary:        Lazy attributes for Python objects
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/stefanholek/lazy
Source:         https://files.pythonhosted.org/packages/source/l/lazy/lazy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of
the first call. They come handy when code should run
 * late, i.e. just before it is needed, and
 * once, i.e. not twice, in the lifetime of an object.
You can think of it as deferred initialization. The possibilities are
endless.

%prep
%setup -q -n lazy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
