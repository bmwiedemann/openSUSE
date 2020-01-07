#
# spec file for package xortool
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xortool
Version:        0.98+git20191025
Release:        0
Summary:        A tool to analyze multi-byte xor cipher
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/hellman/xortool
Source:         %{name}-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-docopt
BuildRequires:  python3-setuptools
BuildArch:      noarch

%description
A tool to do some xor analysis:
 * Guess the key length (based on count of equal chars).
 * Guess the key (base on knowledge of most frequent char).

%prep
%setup -q

%build
%python3_build

%install
%python3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*

%changelog
