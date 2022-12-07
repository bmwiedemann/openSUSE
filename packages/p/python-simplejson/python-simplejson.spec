#
# spec file for package python-simplejson
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
Name:           python-simplejson
Version:        3.18.0
Release:        0
Summary:        Extensible JSON encoder/decoder for Python
License:        AFL-2.1 OR MIT
Group:          Development/Languages/Python
URL:            https://github.com/simplejson/simplejson
Source:         https://files.pythonhosted.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
simplejson is an extensible JSON encoder and decoder for Python 2.5+. It is
pure Python code with no dependencies, but includes an optional C extension for
a speed boost.

%prep
%setup -q -n simplejson-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitearch}/simplejson/tests/
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.txt README.rst
%{python_sitearch}/simplejson*

%changelog
