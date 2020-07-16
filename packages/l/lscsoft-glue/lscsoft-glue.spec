#
# spec file for package glue
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define modname glue
Name:           lscsoft-glue
Version:        2.0.0
Release:        0
Summary:        Grid LSC User Environment
License:        GPL-2.0-only
URL:            http://software.ligo.org/lscsoft
Source:         http://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Provides:       python-glue = %{version}
Obsoletes:      python-glue < %{version}
%python_subpackages

%description
Glue is a collection of utilities for running data analysis pipelines
for online and offline analysis as well as accessing various grid
utilities.  It also provides the infrastructure for the segment
database.

%prep
%setup -q -n %{name}-%{version}

%build
%python_build

%install
%python_install

# SECTION Remove non-library config/php files
rm -fr %{buildroot}%{_prefix}%{_sysconfdir}
rm -fr %{buildroot}%{_prefix}%{_localstatedir}
# /SECTION

%python_expand %fdupes -s %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/*
%{python_sitearch}/*

%changelog
