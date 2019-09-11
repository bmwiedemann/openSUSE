#
# spec file for package python-faulthandler
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


Name:           python-faulthandler
Version:        3.1
Release:        0
Summary:        Display the Python traceback on a crash
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vstinner/faulthandler
Source:         https://files.pythonhosted.org/packages/source/f/faulthandler/faulthandler-%{version}.tar.gz
Patch0:         skip-test.patch
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
Provides:       python2-faulthandler = %{version}

%description
Fault handler for SIGSEGV, SIGFPE, SIGABRT, SIGBUS and SIGILL signals: display
the Python traceback and restore the previous handler. Allocate an alternate
stack for this handler, if sigaltstack() is available, to be able to allocate
memory on the stack, even on stack overflow (not available on Windows).

Import the module and call faulthandler.enable() to enable the fault handler.

%prep
%setup -q -n faulthandler-%{version}
%patch0 -p1

%build
%python2_build

%install
%python2_install

%check
PYTHONPATH=%{buildroot}%{python_sitearch} python tests.py --verbose

%files
%license COPYING
%doc AUTHORS README.rst
%{python_sitearch}/faulthandler*

%changelog
