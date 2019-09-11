#
# spec file for package xortool
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


Name:           xortool
Version:        0.96
Release:        0
Summary:        A tool to analyze multi-byte xor cipher
License:        MIT
Group:          Productivity/Security
Url:            https://github.com/hellman/xortool
Source:         https://github.com/hellman/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
A tool to do some xor analysis:
 * Guess the key length (based on count of equal chars).
 * Guess the key (base on knowledge of most frequent char).

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=%{_prefix}

%files
%defattr (-,root,root)
%doc LICENSE README.md
%{_bindir}/%{name}*
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-*

%changelog
