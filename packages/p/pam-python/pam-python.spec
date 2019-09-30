#
# spec file for package pam-python
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


Name:           pam-python
Version:        1.0.7
Release:        0
Summary:        PAM module that allows PAM modules to be written in Python
License:        AGPL-3.0-only
Group:          Productivity/Security
Url:            http://pam-python.sourceforge.net/
Source:         pam-python-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  pam-devel
BuildRequires:  python-devel
BuildRequires:  python-sphinx
Requires:       python = 2.7
Patch1:         werror.patch

%description
pam_python is a PAM module that runs the Python interpreter, and so
allows PAM modules to be written in Python.

%prep
%setup
%patch1 -p1

%build
# XX: the build system overrides CFLAGS, but flags for the preprocessor are passed to the C compiler
export CPPFLAGS='-DDEFAULT_SECURITY_DIR=\"/%{_lib}/security\" %{optflags}'
make

%install
export LIBDIR=$RPM_BUILD_ROOT/%{_lib}/security
make install-lib

%files
%defattr(-,root,root)
/%{_lib}/security/pam_python.so
%doc agpl-3.0.txt

%changelog
