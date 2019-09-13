#
# spec file for package python-nose-progressive
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
Name:           python-nose-progressive
Version:        1.5.2
Release:        0
Summary:        A testrunner with a progress bar and smarter tracebacks
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/erikrose/nose-progressive
Source:         https://files.pythonhosted.org/packages/source/n/nose-progressive/nose-progressive-%{version}.tar.gz
BuildRequires:  %{python_module blessings >= 1.3}
BuildRequires:  %{python_module nose >= 1.2.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blessings >= 1.3
Requires:       python-nose >= 1.2.1
BuildArch:      noarch
%python_subpackages

%description
nose-progressive is a nose_ plugin which displays progress in a stationary bar,
freeing the rest of the screen (as well as the scrollback buffer) for the
compact display of test failures, which it formats beautifully and usefully. It
displays failures and errors as soon as they occur and avoids scrolling them
off the screen in favor of less useful output. It also offers a number of other
human-centric features to speed the debugging process.

%prep
%setup -q -n nose-progressive-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The test files use 'import __builtin__', which is python2 only syntax. But nose does not mind and
# therefore runs into some other differences between pythons... Surprisingly, most of python3 tests pass.
python setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
