#
# spec file for package python-python-debian
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017 Free Software Foundation Europe e.V.
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


Name:           python-python-debian
Version:        0.1.52
Release:        0
Summary:        Debian package related modules
License:        GPL-3.0-or-later
URL:            https://salsa.debian.org/python-debian-team/python-debian
Source:         https://salsa.debian.org/python-debian-team/python-debian/-/archive/%{version}/python-debian-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gpg2
BuildRequires:  python-rpm-macros
Requires:       python-charset-normalizer
Requires:       zstd
BuildArch:      noarch
Provides:       python-debian = %{version}-%{release}
Obsoletes:      python-debian < %{version}-%{release}
%python_subpackages

%description
This is a collection of modules that are for dealing with Debian related
data. Currently handled are:

* Debtags information (debian.debtags module)
* debian/changelog (debian.changelog module)
* Packages files, pdiffs (debian.debian_support module)
* Control files of single or multiple RFC822-style paragraphs, e.g.
  debian/control, .changes, .dsc, Packages, Sources, Release, etc.
  (debian.deb822 module)
* Raw .deb and .ar files, with (read-only) access to contained
  files and meta-information

%prep
%setup -q -n python-debian-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/debian
%{python_sitelib}/python_debian-%{version}.dist-info

%changelog
