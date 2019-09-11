#
# spec file for package funkload
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define pkgname FunkLoad
Name:           funkload
Version:        1.17.1
Release:        0
Summary:        Functional and Load Web Tester
License:        GPL-2.0
Group:          Productivity/Networking/Web/Utilities
Url:            http://funkload.nuxeo.org/
Source:         https://github.com/nuxeo/FunkLoad/archive/%{version}/FunkLoad-%{version}.tar.gz
Source99:       funkload-rpmlintrc
# pbleser: remove shebangs from non-executable scripts
Patch1:         funkload-remove_shebang.patch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

Recommends:     python-docutils
Recommends:     python-webunit
Recommends:     gnuplot
Recommends:     tcpwatch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
# sle 11 is bOrken
%if %{suse_version} != 1110
BuildArch:      noarch
%endif

%description
FunkLoad is a functional and load Web tester whose main use cases are
functional testing of Web projects (and thus regression testing as well),
performance testing, load testing (such as volume testing or longevity
testing), and stress testing. It can also be used to write Web agents to script
any Web repetitive task, like checking whether a site is alive.

%prep
%setup -q -n %{pkgname}-%{version}
%patch1

%build
sed -i '/ez_/d' setup.py
python setup.py build

%install
python setup.py install \
    --prefix="%{_prefix}" \
    --root=%{buildroot} \
    --record-rpm=files.lst

rm -rf "%{buildroot}%{python_sitelib}/funkload/demo"
perl -n -i -e 'print unless m|^(%dir\s+)?%{python_sitelib}/funkload/demo|' files.lst

%files -f files.lst
%defattr(-,root,root)
%doc CHANGES.txt LICENSE.txt README.txt THANKS TODO.txt

%changelog
