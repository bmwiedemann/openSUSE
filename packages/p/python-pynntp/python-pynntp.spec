#
# spec file for package python-pynntp
#
# Copyright (c) 2024 SUSE LLC
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


%define modname pynntp
%{?sle15_python_module_pythons}
Name:           python-pynntp
Version:        2.0.1
Release:        0
Summary:        NNTP Library (including compressed headers)
License:        GPL-3.0-or-later
URL:            https://github.com/greenbender/pynntp
Source:         https://files.pythonhosted.org/packages/source/p/pynntp/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-nntplib = %{version}
Obsoletes:      python-nntplib <= 0.1.3
BuildArch:      noarch
%python_subpackages

%description
This package includes advanced NNTP features, including,
compressed headers.

The most important (useful) feature of this package over other
nntp libraries is the ability to use generators to produce
data. This allows for streaming download of large responses to
say an XOVER command (which can produce gigabytes of data) and
allows you to process the data at the same time is is being
received. Meaning that memory use is minimal (even for the
largest responses) and that cycles aren't being wasted waiting on
a blocking read (even in a single threaded application)

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Unfortunately, tests are completely non-mockified and required
# real NNTP server.
:

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/nntp
%{python_sitelib}/pynntp-%{version}*-info

%changelog
