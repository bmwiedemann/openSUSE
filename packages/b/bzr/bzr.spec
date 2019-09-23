#
# spec file for package bzr
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


Name:           bzr
Version:        2.7.0
Release:        0
Summary:        A distributed version control system
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
Url:            http://bazaar.canonical.com/
Source0:        https://launchpad.net/bzr/2.7/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        https://launchpad.net/bzr/2.7/%{version}/+download/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Patch0:         bzr-doc-timestamp.patch
# FIX-UPSTREAM-PATCH: fix for python 2.7.13 and later (boo#1020047)
Patch1:         python-2_7_13.patch
# FIX-UPSTREAM-PATCH: avoid code execution (boo#1020047)
Patch2:         bzr-2.7.0-ssh_hostnames-lp1710979
BuildRequires:  fdupes
BuildRequires:  python-Cython
BuildRequires:  python-devel
# Testsuite requirements:
# For httplib.HTTPSConnection SSL:
#BuildRequires:  python
#BuildRequires:  python-testtools
#BuildRequires:  python-xml
Requires:       python-xml
Recommends:     %{name}-lang = %{version}

%description
Bazaar is a distributed version control system. It can
adapt to many workflows and is extendable.

%package test
Summary:        Testsuite for the Bazaar distributed version control system
Group:          Development/Tools/Version Control
Requires:       %{name} = %{version}

%description test
This package contains testsuite files for %{name}.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
sed -i "s|\"share/locale\"|\"locale\"|" setup.py # Fix the locale installation path

%build
CFLAGS="%{optflags} -fno-strict-aliasing" python setup.py build
# TODO: generate documentation:
#make docs

%install
python setup.py install --root %{buildroot} --prefix %{_prefix} --install-data %{_datadir}

# Install bash completion
install -D -m 0644 contrib/bash/bzr \
  %{buildroot}%{_datadir}/bash-completion/completions/bzr

%find_lang %{name}

# TODO: Disable for now, takes ages:
#%%check
#python bzr selftest

%files
%doc COPYING.txt NEWS* README
%{_bindir}/bzr
%{python_sitearch}/bzrlib
%{python_sitearch}/bzr-%{version}-*.egg-info
%exclude %{python_sitearch}/bzrlib/tests
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/bash-completion/completions/%{name}

%files lang -f %{name}.lang

%files test
%{python_sitearch}/bzrlib/tests

%changelog
